# -*- coding: utf-8 -*-
"""Audita los 172 interruptores sin abrir el juego.

    python tools\\OptionAudit.py

Cuatro preguntas, y las cuatro tienen respuesta sin renderizar nada:

  1. ¿Cada interruptor declarado apaga algo?  Un id que no aparece en ningún
     otro archivo es un interruptor muerto: el jugador lo mueve y no pasa nada.
     Es el fallo más caro de un menú de este tamaño porque no se ve, y es
     exactamente lo que costaría descubrir yendo uno por uno.
  2. ¿Cada puerta del código corresponde a un interruptor declarado?  Un
     AllInfo.enabled("Typo") devuelve true para siempre, así que la línea queda
     encendida a la fuerza y nadie se entera.
  3. ¿Cada clave de traducción que nombra o describe un interruptor existe?
     En EN y en los otros nueve idiomas, porque el nombre de casi todos es una
     clave prestada de vanilla y una renombrada la deja en crudo.
  4. ¿Hay ids repetidos?  Dos addTickBox con el mismo id comparten valor en
     ModOptions.ini y el segundo pisa al primero.

Lo que esto NO puede ver es si la línea que se apaga es la correcta. Para eso
está AllInfo.SelfTest.options() dentro del juego, que apaga cada interruptor y
comprueba que el tooltip pierde una fila.
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MOD = os.path.join(HERE, "..", "mod", "42.20", "media", "lua")
CLIENT = os.path.join(MOD, "client", "AllInfo")
TRANSLATE = os.path.join(MOD, "shared", "Translate")
VANILLA = (r"C:\Program Files (x86)\Steam\steamapps\common\ProjectZomboid"
           r"\media\lua\shared\Translate\EN")

OPTIONS_LUA = os.path.join(CLIENT, "Options.lua")

# { id, default, tooltipKey, nameKey }
ENTRY = re.compile(r'\{\s*"(\w+)",\s*(?:true|false)'
                   r'(?:,\s*(nil|"\w+"))?(?:,\s*("\w+"))?\s*\}')
GROUP = re.compile(r'\{\s*key\s*=\s*"(\w+)"(?:,\s*label\s*=\s*"(\w+)")?')
SECTION = re.compile(r'key\s*=\s*"(\w+)",\s*\n\s*master\s*=\s*"(\w+)"')
# Toda forma que el codigo tiene de preguntar por un interruptor.
GATE = re.compile(r'AllInfo\.enabled\(\s*"(\w+)"\s*\)')


def lua_files():
    for root, _, names in os.walk(CLIENT):
        for name in sorted(names):
            if name.endswith(".lua"):
                yield os.path.join(root, name)


def translation_keys(folder):
    keys = set()
    if not os.path.isdir(folder):
        return keys
    for name in os.listdir(folder):
        if name.endswith(".json"):
            text = io.open(os.path.join(folder, name), encoding="utf-8-sig").read()
            keys.update(re.findall(r'"([A-Za-z0-9_]+)"\s*:', text))
    return keys


def main():
    options = io.open(OPTIONS_LUA, encoding="utf-8").read()

    declared, order = {}, []
    for m in ENTRY.finditer(options):
        oid, tip, name = m.group(1), m.group(2), m.group(3)
        order.append(oid)
        declared[oid] = {
            "tip": tip.strip('"') if tip and tip != "nil" else None,
            "name": name.strip('"') if name else "UI_AllInfo_opt_" + oid,
        }

    wanted_keys = set()
    for oid, info in declared.items():
        wanted_keys.add(info["name"])
        if info["tip"]:
            wanted_keys.add(info["tip"])
    # Una seccion se declara con la misma forma que un grupo, asi que sus
    # claves se apuntan primero y luego se descuentan: si no, cada seccion
    # pediria un UI_AllInfo_group_<key> que no existe ni tiene por que.
    sections = {}
    for section, master in SECTION.findall(options):
        sections[section] = master
        wanted_keys.add("UI_AllInfo_section_" + section)
        wanted_keys.add("UI_AllInfo_opt_" + master)
        # El interruptor maestro no se declara como entrada, pero existe.
        declared.setdefault(master, {"tip": None, "name": "UI_AllInfo_opt_" + master})

    for m in GROUP.finditer(options):
        if m.group(1) in sections:
            continue
        wanted_keys.add(m.group(2) or ("UI_AllInfo_group_" + m.group(1)))
    wanted_keys.update(re.findall(r'note\s*=\s*"(\w+)"', options))

    # ------------------------------------------------------------------ uses
    used, gated = set(), set()
    for path in lua_files():
        if os.path.samefile(path, OPTIONS_LUA):
            continue
        text = io.open(path, encoding="utf-8").read()
        gated.update(GATE.findall(text))
        for oid in declared:
            if '"%s"' % oid in text:
                used.add(oid)

    problems = []

    dead = [o for o in order if o not in used]
    if dead:
        problems.append(("interruptores que no apagan nada", dead))

    # Deliberada: SelfTest comprueba que un id desconocido responde "encendido",
    # que es lo que mantiene vivo un proveedor si Options.lua no llego a cargar.
    ghosts = sorted(g for g in gated
                    if g not in declared and g != "NoSuchOptionExists")
    if ghosts:
        problems.append(("puertas sin interruptor (siempre encendidas)", ghosts))

    seen, dupes = set(), []
    for oid in order:
        if oid in seen and oid not in dupes:
            dupes.append(oid)
        seen.add(oid)
    if dupes:
        problems.append(("ids repetidos", dupes))

    # ------------------------------------------------------------------ keys
    ours = os.path.join(TRANSLATE, "EN")
    known = translation_keys(ours) | translation_keys(VANILLA)
    if not os.path.isdir(VANILLA):
        print("aviso: no encuentro las traducciones de vanilla, "
              "las claves prestadas no se comprueban\n")
    missing = sorted(k for k in wanted_keys if k not in known)
    if missing:
        problems.append(("claves de traduccion que no existen", missing))

    # Los nueve idiomas derivados: una clave nuestra que falte en uno de ellos
    # sale en crudo en pantalla y ni el compilador ni i18n.py lo ven.
    ours_only = sorted(k for k in wanted_keys if k.startswith(("UI_AllInfo", "Tooltip_AllInfo")))
    for lang in sorted(os.listdir(TRANSLATE)):
        if lang == "EN":
            continue
        have = translation_keys(os.path.join(TRANSLATE, lang))
        gaps = [k for k in ours_only if k not in have]
        if gaps:
            problems.append(("claves nuestras que faltan en " + lang, gaps))

    # Un nombre con %1 sale literal en el menu: getText() sin argumentos no lo
    # rellena. Solo importa en el nombre, no en la descripcion.
    en_text = {}
    for name in os.listdir(ours):
        if name.endswith(".json"):
            body = io.open(os.path.join(ours, name), encoding="utf-8-sig").read()
            en_text.update(dict(re.findall(r'"([A-Za-z0-9_]+)"\s*:\s*"((?:[^"\\]|\\.)*)"', body)))
    args = sorted(set(info["name"] for info in declared.values()
                      if re.search(r"%[1-9]", en_text.get(info["name"], ""))))
    if args:
        problems.append(("nombres con %N sin rellenar", args))

    # ---------------------------------------------------------------- report
    print("%d interruptores declarados, %d claves comprobadas"
          % (len(order), len(wanted_keys)))
    if not problems:
        print("sin problemas")
        return 0

    for title, items in problems:
        print("\n%s (%d):" % (title, len(items)))
        for item in items:
            print("    " + item)
    return 1


if __name__ == "__main__":
    sys.exit(main())
