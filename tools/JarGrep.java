import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.util.zip.*;

// Lists the classes in a jar whose bytes contain a literal string.
// Useful to find callers: a class that touches Foo.bar carries "bar" in its
// constant pool. javac --release 21 JarGrep.java
public class JarGrep {
    public static void main(String[] args) throws Exception {
        byte[] needle = args[1].getBytes(StandardCharsets.UTF_8);
        String filter = args.length > 2 ? args[2] : "";

        try (ZipFile zip = new ZipFile(args[0])) {
            List<String> hits = new ArrayList<>();
            Enumeration<? extends ZipEntry> e = zip.entries();
            while (e.hasMoreElements()) {
                ZipEntry entry = e.nextElement();
                String name = entry.getName();
                if (!name.endsWith(".class") || !name.contains(filter)) continue;

                byte[] data;
                try (InputStream in = zip.getInputStream(entry)) {
                    data = in.readAllBytes();
                }
                if (indexOf(data, needle) >= 0) hits.add(name);
            }
            Collections.sort(hits);
            hits.forEach(System.out::println);
            System.out.println(hits.size() + " classes contain \"" + args[1] + "\"");
        }
    }

    private static int indexOf(byte[] haystack, byte[] needle) {
        outer:
        for (int i = 0; i <= haystack.length - needle.length; i++) {
            for (int j = 0; j < needle.length; j++) {
                if (haystack[i + j] != needle[j]) continue outer;
            }
            return i;
        }
        return -1;
    }
}
