import java.lang.reflect.*;
import java.net.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.*;

// Compiles every .lua under a folder with Project Zomboid's own Lua compiler,
// then walks the prototypes it produced to count local variables per function.
//
// javac --release 21 LuaCheck.java   (reflection only: the jar is class file 69)
// then run with the game's jre64\bin\java.exe.
//
// Why the local count: Kahlua's FuncState.actvar is a short[200], and
// new_localvar() writes into it *without* a limit check when the variable comes
// from a `for` header. Go over the line there and the compiler dies with a bare
// ArrayIndexOutOfBounds instead of the friendly "more than 200 local variables"
// that a plain `local` gets. It happened to SelfTest.lua in the game while this
// tool -- calling the same compiler, on the same bytes -- compiled it clean, so
// compiling successfully here is not proof of anything near the ceiling.
// Counting the locals is: any function that registers 200 or more is a fail,
// and 150 is close enough to warn about.
public class LuaCheck {
    static final int LOCALS_FAIL = 200;
    static final int LOCALS_WARN = 150;

    static Field protoField, locvarsField, nestedField, nameField;
    static int worst;
    static String worstName = "";

    public static void main(String[] args) throws Exception {
        Path jar = Paths.get(args[0]);
        Path root = Paths.get(args[1]);

        URLClassLoader cl = new URLClassLoader(new URL[] { jar.toUri().toURL() },
                LuaCheck.class.getClassLoader());

        Class<?> compiler = Class.forName("se.krka.kahlua.luaj.compiler.LuaCompiler", true, cl);
        Class<?> tableType = Class.forName("se.krka.kahlua.vm.KahluaTable", true, cl);
        Method loadstring = compiler.getMethod("loadstring", String.class, String.class, tableType);

        Class<?> closure = Class.forName("se.krka.kahlua.vm.LuaClosure", true, cl);
        Class<?> proto = Class.forName("se.krka.kahlua.vm.Prototype", true, cl);
        protoField = closure.getField("prototype");
        locvarsField = proto.getField("locvars");
        nestedField = proto.getField("prototypes");
        nameField = proto.getField("name");

        Object env = null;
        try {
            Class<?> platform = Class.forName("se.krka.kahlua.j2se.J2SEPlatform", true, cl);
            Object p = platform.getDeclaredConstructor().newInstance();
            env = platform.getMethod("newTable").invoke(p);
        } catch (Throwable ignored) {
        }

        List<Path> files = new ArrayList<>();
        try (var s = Files.walk(root)) {
            s.filter(p -> p.toString().endsWith(".lua")).forEach(files::add);
        }
        Collections.sort(files);

        int ok = 0, bad = 0;
        for (Path p : files) {
            String src = Files.readString(p, StandardCharsets.UTF_8);
            String rel = root.relativize(p).toString();
            try {
                Object c = loadstring.invoke(null, src, p.getFileName().toString(), env);
                List<String> over = new ArrayList<>();
                walk(protoField.get(c), rel, over);
                if (over.isEmpty()) {
                    ok++;
                } else {
                    bad++;
                    for (String line : over) System.out.println("FAIL " + line);
                }
            } catch (InvocationTargetException e) {
                bad++;
                System.out.println("FAIL " + rel + " -> " + e.getCause());
            }
        }

        System.out.println(ok + " compiled, " + bad + " failed"
                + " (most locals in one function: " + worst + worstName + ")");
    }

    // Depth-first over the nested prototypes: one per function in the file.
    static void walk(Object prototype, String file, List<String> over) throws Exception {
        String[] locvars = (String[]) locvarsField.get(prototype);
        int count = locvars == null ? 0 : locvars.length;
        String where = file + " :: " + nameField.get(prototype);

        if (count > worst) {
            worst = count;
            worstName = " -- " + where;
        }
        if (count >= LOCALS_FAIL) {
            over.add(where + " declares " + count + " locals, over Kahlua's 200 ceiling");
        } else if (count >= LOCALS_WARN) {
            System.out.println("WARN " + where + " declares " + count
                    + " locals; the ceiling is 200 per function");
        }

        Object[] nested = (Object[]) nestedField.get(prototype);
        if (nested == null) return;
        for (Object child : nested) {
            if (child != null) walk(child, file, over);
        }
    }
}
