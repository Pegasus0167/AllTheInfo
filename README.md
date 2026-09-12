# AllTheInfo

A client-side information mod for **Project Zomboid B42.20**. It prints the
numbers the game keeps to itself: exact item stats on top of every bare
condition bar, clothing comparisons against what you are wearing, crafting
outcomes, cooking and burning times, generators, gas pumps, structures, crops,
wounds, traits, professions, skills and all 26 moodles.

[On the Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=3781129962)
· [Léeme en español](README.es.md)

---

## The rule the whole thing is built on

**Every figure is derived from the game's own code, never estimated.** If a
number cannot be traced to a field or a method in `projectzomboid.jar`, the row
is not printed at all. A missing row is better than a plausible lie, because a
player will act on a number the moment they read it.

In practice that means the work is mostly not Lua. It is reading decompiled
bytecode to find out what the game actually does, then writing the four lines
that report it. Two examples that ended up in the code as comments:

- Repair failure chance is one point higher than the formula suggests. The game
  rolls `Rand.Next(100) <= fail` on a value that comes out 0 to 99, so a chance
  the maths clips to 0 still fails one time in a hundred. The mod shows the real
  odds, not the formula's.
- `ObjectTooltip.padLeft` is a public Java field, but the Lua binding exposes
  methods only, so reading it yields `nil`. `checkFont()` sets it to
  `MeasureStringX(font, "0")`, so the mod derives it the same way and matches
  vanilla at any UI scale instead of hardcoding a pixel count.

Around 205 findings like these are written up in the project's internal notes,
each one verified in bytecode before it was allowed to change a line of output.

## How it is put together

```
Core.lua        provider registry, 500 ms cache, formatting and colors
Render.lua      the only file that draws, wraps vanilla's tooltip
providers/      17 files: melee, firearms, ammo, food, clothing, medicine, ...
world/          generators, crops, animals, traps, fishing, structures
character/      skills, traits, health, XP multipliers, character creation
Options.lua     172 individual toggles
SelfTest.lua    in-game test suite, run from the debug console
```

Two hard rules hold the layers apart, and they are stated at the top of
`Core.lua`: **the core never knows what an item is, and a provider never
draws.** A provider is a function `fn(out, item, chr)` that appends rows; where
those rows end up on screen is none of its business. Adding a new piece of
information is one file and one `AllInfo.register` call.

Vanilla functions are **wrapped, never replaced**, so the mod composes with
other mods that hook the same tooltip instead of fighting them for it.

## Options

Every line the mod prints is its own switch, 172 of them, grouped into items,
world, character and crafting. Not a switch per feature, a switch per *line*: if
one row in one tooltip bothers you, that row goes and nothing else goes with it.

A switch that is off is not a hidden row. It is a provider that never runs, so
turning off an area costs nothing at all at runtime.

## Translations

Ten languages: English, Simplified Chinese, Russian, Spanish, Brazilian
Portuguese, German, Turkish, French, Japanese and Polish.

Only English and Spanish are hand-written. The other eight are **generated** by
`tools/i18n.py` from phrase tables in `tools/lang/`, and the generator refuses
to write a file if it meets a fragment it does not know. That is the point: a
new English key can never leave a translated file silently speaking English.

The unit of translation is not the key, it is the fragment with its numbers
pulled out:

```
"-15 climb chance"   ->   template "{} climb chance",  numbers ["-15"]
```

That turns 436 keys per language into about 310 phrases, keeps the wording
consistent everywhere, and means no figure can ever be mistranslated, since the
numbers ride through untouched. Adding a language is one file plus one line.

Where vanilla already has a key for something (`Tooltip_weapon_Condition`,
`IGUI_perks_*`), the mod reuses it and inherits all 29 of the game's languages
for free.

## Tooling

Four tools, because the game's runtime is a bad place to find out you were
wrong:

| Tool | What it does |
|---|---|
| `tools/LuaCheck.java` | Compiles every `.lua` with the game's own Kahlua compiler, which rejects syntax the reference Lua accepts, and counts locals per function. Kahlua allows 200 and blows up the whole file at 201, so it warns at 150 |
| `tools/JarGrep.java` | Scans `projectzomboid.jar` for every class that touches a given field or method, so a change can be checked against the real callers |
| `tools/i18n.py` | Generates and validates the eight derived languages |
| `tools/OptionAudit.py` | Audits the 172 switches without launching the game: toggles that disable nothing, ids that do not exist, translation keys missing in any of the ten languages, duplicate ids |

On top of that, `SelfTest.lua` runs inside the game from the debug console. It
flips every tooltip switch against a sample item and checks that the rows
actually change, and it names out loud whatever it could not prove.

## Repository layout

```
mod/42.20/      the mod exactly as it ships, 40 Lua files, ~11k lines
tools/          the four tools above, plus the phrase tables
```

`mod.info` must live inside `mod/42.20/`, not at the top of the mod folder: B42
does not detect a flat mod.

## Installing from source

Copy `mod/` into `%USERPROFILE%\Zomboid\mods\AllInfo`, then restart the game to
the desktop. Returning to the main menu is not enough, mod Lua is read once at
startup.

## License

MIT, see [LICENSE](LICENSE).
