"""Generates every non-source translation file from the English one.

    python tools\\i18n.py            check only, lists anything untranslated
    python tools\\i18n.py --write    rewrite mod\\...\\Translate\\<LANG>\\*.json

EN and ES are hand-written and are the source. Every other language is
*generated* from a phrase table in tools/lang/, so a new English key can never
leave a translated file silently speaking English: the script refuses to write
and prints the fragments it does not know.

How it works. Almost every string in this mod is a `<br>`-joined list of short
numeric fragments, and the same fragments repeat across 436 keys. So the unit of
translation is not the key, it is the fragment with its numbers pulled out:

    "-15 climb chance"      ->  template "{} climb chance"   numbers ["-15"]

That turns 436 keys x N languages into ~310 phrases x N, keeps the wording
consistent everywhere, and gives a native speaker one flat table to review
instead of four JSON files. Numbers ride through untouched, so no figure can be
mistranslated -- the worst a bad table entry can do is word it badly.

Adding a language is one file in tools/lang/ plus one line in LANGS.

`%1`-style Translator arguments are masked out before the numbers are
extracted, and `%%` is left exactly as it is -- it is how a literal `%` survives
String.format (see plans/allinfo-estado.md, trap 3.23).
"""
import importlib.util
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TRANSLATE = os.path.join(HERE, "..", "mod", "42.20", "media", "lua", "shared", "Translate")
FILES = ("UI", "Tooltip", "IG_UI", "Moodles")

# PZ folder name -> tools/lang module. EN and ES are absent on purpose: they are
# the hand-written source, not an output.
LANGS = {
    "RU": "ru",       # Russian
    "CN": "cn",       # Chinese, Simplified
    "PTBR": "ptbr",   # Portuguese, Brazilian
    "DE": "de",       # German
    "TR": "tr",       # Turkish
    "FR": "fr",       # French
    "JP": "jp",       # Japanese
    "PL": "pl",       # Polish
}

ARG = re.compile(r"%[1-9]")
NUM = re.compile(r"[-+]?\d+(?:\.\d+)?")
SLOT = re.compile(r"\{\d*\}")
MASK = "\x01"


def split(fragment):
    """'-15 climb chance' -> ('{} climb chance', ['-15'])."""
    masked = ARG.sub(MASK, fragment)
    numbers = NUM.findall(masked)
    return NUM.sub("{}", masked).replace("{", "{{").replace("}", "}}") \
        .replace("{{}}", "{}"), numbers


def restore(template, numbers, args):
    out = template.format(*numbers) if numbers else template.replace("{{", "{").replace("}}", "}")
    for a in args:
        out = out.replace(MASK, a, 1)
    return out


# Every line the player reads opens with a capital, and the phrase tables do
# not: a table entry is a fragment, keyed by its English text in lower case, and
# capitalising there would invalidate all ~310 of them in eight languages at
# once. So the case lives at the two ends instead. Reading, a template that
# misses is retried with its first letter lowered, which is what lets the
# capitalised English source still find its entry. Writing, the first letter of
# every fragment goes back up.
#
# Only where the script has upper case at all: Chinese and Japanese have none.
# Turkish does, and its dotted capital I is not the ASCII one, hence the pair.
NO_CASE = ("CN", "JP")
UPPER = {"TR": {"i": "İ"}}


def lookup(table, template):
    hit = table.get(template)
    if hit is not None:
        return hit
    if template and template[:1].isupper():
        return table.get(template[:1].lower() + template[1:])
    return None


# 'x2.5 nutrients' opens with a letter that is really a multiplication sign, and
# 'X2.5' is not a capital, it is a typo. Left alone in every language: German
# and Japanese put the multiplier first where English does not.
MULTIPLIER = re.compile(r"^[Xx][%\d]")


def capitalise(fragment, code):
    """Only when the fragment opens with a letter. '-20%% melee damage' has
    nothing to raise, and forcing the first word of a numbered line would give
    '-20%% Melee damage'."""
    if code in NO_CASE or not fragment or not fragment[:1].isalpha():
        return fragment
    if MULTIPLIER.match(fragment):
        return fragment
    first = UPPER.get(code, {}).get(fragment[0]) or fragment[0].upper()
    return first + fragment[1:]


def load(module):
    path = os.path.join(HERE, "lang", module + ".py")
    spec = importlib.util.spec_from_file_location("allinfo_lang_" + module, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return {ARG.sub(MASK, k): ARG.sub(MASK, v) for k, v in mod.T.items()}


def check_arity(code, table):
    """A translation may reorder the numbers with {0} {1} ..., so slots are
    counted rather than matched literally. Python forbids mixing {} and {0} in
    one string, so a reordered line has to index every slot."""
    problems = []
    for en, other in table.items():
        if len(SLOT.findall(en)) != len(SLOT.findall(other)):
            problems.append("%s: arity: %s" % (code, en.replace(MASK, "%1")))
        if "{}" in other and re.search(r"\{\d\}", other):
            problems.append("%s: mixed numbering: %s" % (code, en.replace(MASK, "%1")))
    return problems


def main():
    write = "--write" in sys.argv
    tables = {code: load(module) for code, module in LANGS.items()}

    problems = []
    for code, table in tables.items():
        problems += check_arity(code, table)
    if problems:
        for p in problems:
            print(p)
        return 1

    missing = {}
    total = 0

    for code, table in tables.items():
        folder = os.path.join(TRANSLATE, code)
        for name in FILES:
            source = json.load(io.open(os.path.join(TRANSLATE, "EN", name + ".json"), encoding="utf-8"))
            out = {}
            for key, value in source.items():
                parts = []
                for fragment in value.split("<br>"):
                    template, numbers = split(fragment)
                    translated = lookup(table, template)
                    if translated is None:
                        missing.setdefault(code, set()).add(template.replace(MASK, "%1"))
                        parts.append(fragment)
                    else:
                        parts.append(capitalise(
                            restore(translated, numbers, ARG.findall(fragment)), code))
                out[key] = "<br>".join(parts)
            total += len(out)

            if write and code not in missing:
                if not os.path.isdir(folder):
                    os.makedirs(folder)
                text = "{\n" + ",\n".join(
                    '    %s: %s' % (json.dumps(k, ensure_ascii=False), json.dumps(v, ensure_ascii=False))
                    for k, v in out.items()) + "\n}\n"
                io.open(os.path.join(folder, name + ".json"), "w", encoding="utf-8", newline="\n").write(text)

    if missing:
        for code in sorted(missing):
            print("%s: %d untranslated templates" % (code, len(missing[code])))
            for m in sorted(missing[code])[:400]:
                print("    " + m)
        return 1

    print("%d strings across %s: every fragment translated."
          % (total, ", ".join(sorted(LANGS))))
    print("written" if write else "check only; pass --write to update the files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
