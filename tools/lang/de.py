"""German phrase table for AllInfo.

Keys are the English fragment with every number replaced by {} in order.
Numbers are never written here: they ride through untouched. Use {0} {1} ...
instead of {} when the language needs a different order -- and then index every
slot, Python refuses to mix the two forms.

Run `python tools\\i18n.py` after editing: it checks the arity of every line and
refuses to write a language file it cannot fill completely.
"""

T = {
    # Per-level skill descriptions
    "x{} weapon damage (x{} untrained)": "x{} Waffenschaden (x{} ungeübt)",
    "{} to the durability roll": "{} auf den Haltbarkeitswurf",
    "{} chance to trip vaulting a fence": "{} Stolperchance beim Überklettern eines Zauns",
    "{}%% fall damage": "{}%% Fallschaden",
    "x{} endurance recovery (x{} untrained)": "x{} Ausdauerregeneration (x{} ungeübt)",
    "x{} melee damage and knockback (x{} untrained)": "x{} Nahkampfschaden und Rückstoß (x{} ungeübt)",
    "x{} carrying capacity (x{} untrained)": "x{} Tragkraft (x{} ungeübt)",
    "x{} move speed in combat stance (x{} untrained)": "x{} Tempo in Kampfhaltung (x{} ungeübt)",
    "x{} sprint speed (x{} untrained)": "x{} Sprinttempo (x{} ungeübt)",
    "x{} chance of being spotted (x{} untrained)": "x{} Chance, entdeckt zu werden (x{} ungeübt)",
    "x{} footstep noise (x{} untrained)": "x{} Schrittgeräusch (x{} ungeübt)",
    "{} accuracy (the weapon's aiming modifier, {} on nearly every gun)":
        "{} Genauigkeit (der Zielmodifikator der Waffe, {} bei fast jeder Schusswaffe)",
    "{} wind penalty when aiming (of {})": "{} Windabzug beim Zielen (von {})",
    "x{} reload speed (x{} untrained)": "x{} Nachladetempo (x{} ungeübt)",
    "x{} racking speed (x{} untrained)": "x{} Tempo beim Durchladen (x{} ungeübt)",
    "racking costs {} of the aiming time ({} untrained)": "Durchladen kostet {} der Zielzeit ({} ungeübt)",
    "From here on you no longer count as unsteady with a firearm, as long as your Strength is {} or more: jam chance drops by {} percentage points.":
        "Ab hier giltst du mit einer Schusswaffe nicht mehr als unsicher, solange deine Stärke {} oder höher ist: die Ladehemmungschance sinkt um {} Prozentpunkte.",
    "You never count as unsteady with a firearm again, whatever your Strength.":
        "Du giltst mit einer Schusswaffe nie wieder als unsicher, egal wie hoch deine Stärke ist.",

    # Moodles
    "{} melee to-hit": "{} Trefferchance im Nahkampf",
    "{} climb chance": "{} Kletterchance",
    "{} trip chance": "{} Stolperchance",
    "{} to break a zombie's grab": "{} um sich aus dem Griff eines Zombies zu befreien",
    "{}%% strength": "{}%% Stärke",
    "{}%% healing": "{}%% Heilung",
    "losing health": "Gesundheit sinkt",
    "harder to unjam a gun": "Ladehemmung schwerer zu beheben",
    "{} move speed (of {})": "{} Bewegungstempo (von {})",
    "body at {} C": "Körpertemperatur {} C",
    "{} carry capacity": "{} Tragkraft",
    "x{} attack speed": "x{} Angriffsgeschwindigkeit",
    "endurance under {}%%": "Ausdauer unter {}%%",
    "fatigue over {}%%": "Müdigkeit über {}%%",
    "hunger over {}%%": "Hunger über {}%%",
    "thirst over {}%%": "Durst über {}%%",
    "panic over {}%%": "Panik über {}%%",
    "stress over {}%%": "Stress über {}%%",
    "boredom over {}%%": "Langeweile über {}%%",
    "unhappiness over {}%%": "Unglück über {}%%",
    "{}%% action speed": "{}%% Handlungsgeschwindigkeit",
    "anger over {}%%": "Wut über {}%%",
    "drunkenness over {}%%": "Trunkenheit über {}%%",
    "pain over {}%%": "Schmerz über {}%%",
    "slower rope climbing": "langsameres Klettern am Seil",
    "{}%% total body damage": "{}%% Gesamtschaden am Körper",
    "sickness over {}%%": "Krankheit über {}%%",
    "cold strength over {}%%": "Erkältungsstärke über {}%%",
    "wetness over {}%%": "Nässe über {}%%",
    "discomfort over {}%%": "Unbehagen über {}%%",
    "rotting corpses nearby": "verwesende Leichen in der Nähe",
    "x{} move speed": "x{} Bewegungstempo",
    "{} discomfort per level": "{} Unbehagen pro Stufe",
    "{} C on top of the air temperature": "{} C zusätzlich zur Lufttemperatur",
    "carrying {}x capacity": "Last bei {}x der Kapazität",
    "{}%% body heat": "{}%% Körperwärme",
    "no sleep without pills": "kein Schlaf ohne Tabletten",
    "erratic movement": "unstete Bewegung",
    "raises discomfort": "erhöht das Unbehagen",
    "no sprinting": "kein Sprinten",
    "no sprinting, no exercise": "kein Sprinten, kein Training",
    "zombies spot you {} sooner": "Zombies entdecken dich {} früher",
    "muscle stiffness builds up": "Muskelsteifheit baut sich auf",
    "cannot eat or open food": "kann nicht essen und keine Nahrung öffnen",
    "{} move speed with Adrenaline Junkie": "{} Tempo mit Adrenalinjunkie",
    "nightmares while asleep": "Albträume im Schlaf",
    "no sleep below {}%% fatigue without pills": "ohne Tabletten kein Schlaf unter {}%% Müdigkeit",
    "{}%% move speed": "{}%% Bewegungstempo",
    "cannot move": "kann sich nicht bewegen",
    "{} climbing walls and ropes": "{} beim Klettern an Mauern und Seilen",
    "no running, no exercise": "kein Laufen, kein Training",
    "over {}x capacity": "über {}x der Kapazität",
    "no running": "kein Laufen",
    "no sprinting until you drop the bulky item": "kein Sprinten, bis du den sperrigen Gegenstand ablegst",
    "you can sleep through high pain": "du kannst trotz starker Schmerzen schlafen",
    "no endurance recovery": "keine Ausdauerregeneration",
    "{} vision cone": "{} Sichtkegel",
    "delayed vehicle controls": "verzögerte Fahrzeugsteuerung",
    "narrowed vision cone": "verengter Sichtkegel",
    "no exercise": "kein Training",
    "{} wound bleeding": "{} blutende Wunde",
    "Rest in peace.": "Ruhe in Frieden.",
    "Infected. There is no cure.": "Infiziert. Es gibt keine Heilung.",

    # Tooltip labels
    "Stale in": "Wird schal in",
    "Rots in": "Verdirbt in",
    "Cooking time": "Garzeit",
    "Never": "Nie",
    "Critical chance": "Kritchance",
    "Trains": "Trainiert",
    "Attack speed": "Angriffsgeschwindigkeit",
    "Swing type": "Schlagart",
    "Heavy": "Schwer",
    "Swung": "Geschwungen",
    "Stabbing": "Stechend",
    "Spear": "Speer",
    "Stone": "Stein",
    "Knockback on hit": "Rückstoß bei Treffer",
    "Condition loss": "Zustandsverlust",
    "Jam chance": "Ladehemmungschance",
    "Accuracy": "Genauigkeit",
    "Noise radius": "Lärmradius",
    "Rounds": "Patronen",
    "Reload time": "Nachladezeit",
    "Aiming time": "Zielzeit",
    "Used by": "Passt zu",
    "Reading speed": "Lesegeschwindigkeit",
    "Reading time left": "Restliche Lesezeit",
    "Skill too low to learn from it": "Fertigkeit zu niedrig, um daraus zu lernen",
    "Nothing left to learn from it": "Daraus gibt es nichts mehr zu lernen",
    "Proteins": "Proteine",
    "Sow in": "Aussäen im",
    "Ready in": "Reif in",
    "Burn time": "Brenndauer",
    # Power: charge, autonomy and light
    "Duration": "Dauer",
    "Light range": "Lichtreichweite",
    "Light strength": "Lichtstärke",
    "Batteries and radios: charge left, how long it lasts and how far a torch lights": "Batterien und Radios: Restladung, Laufzeit und Reichweite einer Taschenlampe",
    "Vanilla draws the charge of a drainable as a bar with no number on it, and never says how long a torch lasts or how far it lights. A torch spends its UseDelta once every ten game minutes, and only while it is in a hand or attached to you: left in a bag it switches itself off. Light range and strength are the figures that actually light the ground.":
        "Das Spiel zeichnet die Ladung eines Verbrauchsgegenstands als Balken ohne Zahl und sagt nie, wie lange eine Taschenlampe hält oder wie weit sie leuchtet. Eine Taschenlampe verbraucht ihr UseDelta einmal alle zehn Spielminuten, und nur solange sie in der Hand oder an dir befestigt ist: im Rucksack schaltet sie sich selbst ab. Lichtreichweite und Lichtstärke sind die Zahlen, die den Boden wirklich beleuchten.",
    "Rest quality": "Erholungsqualität",
    "Discomfort": "Unbehagen",
    "Stomp damage": "Tretschaden",
    "Corpse sickness defense": "Schutz vor Leichenkrankheit",
    "Filter charge": "Filterrestwert",
    "New recipes": "Neue Rezepte",
    "Listened": "Angehört",
    "Skill too high for this tape": "Fertigkeit zu hoch für dieses Band",

    # Options screen
    "All Info": "All Info",
    "Enable everything": "Alles aktivieren",
    "Items": "Gegenstände",
    "Crafting": "Herstellung",
    "World": "Welt",
    "Character": "Charakter",
    "Everything in this section": "Alles in diesem Abschnitt",
    "Food: time left before it spoils": "Nahrung: Zeit bis zum Verderben",
    "Adds hours to stale and hours to rotten, at the current rate. Accounts for the fridge, the freezer and the sandbox spoilage speed.":
        "Zeigt, wie viele Stunden bis schal und bis verdorben bleiben, beim aktuellen Tempo. Berücksichtigt Kühlschrank, Gefrierfach und die Verderbgeschwindigkeit aus den Sandbox-Einstellungen.",
    "Cooking: add the warm-up minutes": "Garen: die Aufheizminuten dazurechnen",
    "Off by default. Cooking time is the time at temperature; this adds the four minutes the food spends heating up before it starts to cook, so an oven timer set to the figure rings when the food is done.":
        "Standardmäßig aus. Die Garzeit gilt für Essen, das schon auf Temperatur ist; dies rechnet die vier Minuten dazu, die das Essen zum Aufheizen braucht, bevor es zu garen beginnt, damit der Ofentimer genau dann klingelt, wenn es fertig ist.",
    "Food: calories, carbs, protein and fat": "Nahrung: Kalorien, Kohlenhydrate, Proteine und Fett",
    "Off by default. Showing macros on every food undoes the Nutritionist trait, which is what normally reveals them.":
        "Standardmäßig aus. Nährwerte auf jeder Nahrung zu zeigen entwertet die Eigenschaft Ernährungsberater, die sie sonst erst freilegt.",
    "Melee: exact damage, speed and durability": "Nahkampf: exakter Schaden, Tempo und Haltbarkeit",
    "Puts numbers on the condition and damage bars, and adds crit chance, swing type, attack speed, knockback and the odds of losing a condition point per hit.":
        "Schreibt Zahlen auf die Zustands- und Schadensbalken und ergänzt Kritchance, Schlagart, Angriffsgeschwindigkeit, Rückstoß und die Chance, pro Treffer einen Zustandspunkt zu verlieren.",
    "Firearms: range, jam chance and reload": "Schusswaffen: Reichweite, Ladehemmung und Nachladen",
    "Puts numbers on the condition and damage bars, and adds accuracy, effective range, jam odds and magazine size.":
        "Schreibt Zahlen auf die Zustands- und Schadensbalken und ergänzt Genauigkeit, effektive Reichweite, Ladehemmungschance und Magazingröße.",
    "Ammo: rounds left and what it fits": "Munition: Restpatronen und passende Waffen",
    "No comparison arrows here: the thing in your hands is a gun, not another magazine, so there is no honest pair to compare.":
        "Hier gibt es keine Vergleichspfeile: in deiner Hand liegt eine Waffe, kein zweites Magazin, also gibt es kein ehrliches Paar zum Vergleichen.",
    "Clothing: numbers on every bar, plus discomfort": "Kleidung: Zahlen auf allen Balken, dazu das Unbehagen",
    "Vanilla draws condition, insulation, wind, water, blood, dirt and wetness as bars with no figures. This writes the figures next to them and adds the discomfort value, which vanilla never shows at all.":
        "Das Spiel zeichnet Zustand, Isolierung, Wind, Wasser, Blut, Schmutz und Nässe als Balken ohne Zahlen. Hier stehen die Zahlen daneben, dazu der Unbehagenswert, den das Spiel nirgends zeigt.",
    "Seeds: growing time and yield": "Saatgut: Wachstumszeit und Ertrag",
    "Firewood: how long it burns": "Brennholz: wie lange es brennt",
    "Books: reading time and skill levels covered": "Bücher: Lesezeit und abgedeckte Stufen",
    "Reading time already accounts for Fast Reader, Slow Reader and reading glasses.":
        "Die Lesezeit berücksichtigt bereits Schnellleser, Langsamleser und die Lesebrille.",
    "Beds: how well you recover on them": "Betten: wie gut man sich darauf erholt",
    "Masks: filter life and protection": "Masken: Filterlebensdauer und Schutz",
    "Tapes and CDs: which skill they teach and how much XP": "Kassetten und CDs: welche Fertigkeit sie lehren und wie viel XP",
    "Show the difference against what you have equipped": "Unterschied zum Ausgerüsteten anzeigen",
    "Adds a coloured +/- next to weapon and clothing values. Weapons compare against what is in your hands, clothing against the piece worn in the same slot.":
        "Setzt ein farbiges +/- neben Waffen- und Kleidungswerte. Waffen werden mit dem verglichen, was du in der Hand hast, Kleidung mit dem Stück am selben Platz.",
    "Crafting: full item tooltip on the recipe output": "Herstellung: vollständige Gegenstandsinfo am Rezeptergebnis",
    "Hovering the result of a recipe shows the same block an item in your inventory would, comparison included, before you craft it.":
        "Zeigt beim Überfahren des Rezeptergebnisses denselben Block wie bei einem Gegenstand im Inventar, samt Vergleich, noch vor dem Herstellen.",
    "Generators: fuel time, wear and danger": "Generatoren: Kraftstoff, Verschleiß und Gefahr",
    "Adds noise radius, hours of fuel left, average time until {}%% condition and until it breaks, and the hourly odds of a backfire or a fire.":
        "Ergänzt Lärmradius, verbleibende Kraftstoffstunden, die durchschnittliche Zeit bis {}%% Zustand und bis zum Defekt sowie die stündliche Chance auf Fehlzündung oder Brand.",
    "Generators: also show times in real-world minutes": "Generatoren: Zeiten auch in echten Minuten anzeigen",
    "Off by default. Converts the in-game hours using the current day length, so you know how long you actually have to wait.":
        "Standardmäßig aus. Rechnet die Spielstunden mit der aktuellen Taglänge um, damit du weißt, wie lange du wirklich wartest.",
    "Generators: outline the powered area on the floor": "Generatoren: den versorgten Bereich auf dem Boden umranden",
    "Draws the edge of the range while the generator window is open, green when running and red when off. Only the floor you are standing on is computed.":
        "Zeichnet den Rand der Reichweite, solange das Generatorfenster offen ist: grün im Betrieb, rot im Stillstand. Berechnet wird nur die Etage, auf der du stehst.",
    "Gas pumps: fuel left and power source": "Zapfsäulen: Restmenge und Stromquelle",
    "Adds an Info entry to the right-click menu of any gas pump, with the fuel still in the tank and whether the mains or a generator is keeping it running. The game knows that number and only prints it as a debug option.":
        "Fügt dem Rechtsklickmenü jeder Zapfsäule einen Info-Eintrag hinzu, mit dem Sprit, der noch im Tank ist, und der Frage, ob Netz oder Generator sie am Laufen hält. Das Spiel kennt diese Zahl und zeigt sie nur als Debug-Option.",
    "Fuel Remaining": "Restlicher Kraftstoff",
    "Mains power": "Stromnetz",
    "Generator": "Generator",
    "Walls and doors: health under the cursor": "Wände und Türen: Stabilität unter dem Mauszeiger",
    "Shows current and maximum health as a number at the foot of whatever you point at, no clicking needed.":
        "Zeigt aktuelle und maximale Stabilität als Zahl am Fuß dessen, worauf du zeigst, ganz ohne Klick.",
    "Build menu: health of what you are about to build": "Baumenü: Stabilität dessen, was du bauen willst",
    "Also shows what that health would be with the relevant skill at {}, so you can tell whether it is worth waiting.":
        "Zeigt außerdem, wie hoch diese Stabilität mit der zugehörigen Fertigkeit auf {} wäre, damit du siehst, ob sich Warten lohnt.",
    "Crops: health, growth and water as numbers": "Pflanzen: Gesundheit, Wachstum und Wasser als Zahlen",
    "Adds rows to the crop window you get by right-clicking a plant: health out of {}, current phase, hours to the next one, water level against what the plant needs, time since the last watering and pest levels.":
        "Ergänzt das Fenster, das beim Rechtsklick auf eine Pflanze erscheint: Gesundheit von {}, aktuelle Phase, Stunden bis zur nächsten, Wasserstand gegen den Bedarf der Pflanze, Zeit seit dem letzten Gießen und die Stufe jedes Schädlings.",
    "Crops: keep vanilla's Farming level requirements": "Pflanzen: die Landwirtschaftsstufen des Spiels beibehalten",
    "Off by default, so you see everything from level {}. Turn it on and each row reappears at the Farming level vanilla itself uses for it: phase and health at {}, water at {}, pests at {}, next phase at {}.":
        "Standardmäßig aus, du siehst also alles ab Stufe {}. Eingeschaltet erscheint jede Zeile erst auf der Landwirtschaftsstufe, die das Spiel selbst dafür nutzt: Phase und Gesundheit bei {}, Wasser bei {}, Schädlinge bei {}, nächste Phase bei {}.",
    "Noise": "Lärm",
    "tiles": "Felder",
    "Down to %1%% (avg)": "Bis auf %1%% (Ø)",
    "Breaks down in (avg)": "Geht kaputt in (Ø)",
    "Backfire, loud (per hour)": "Fehlzündung, laut (pro Stunde)",
    "FIRE OR EXPLOSION (per hour)": "BRAND ODER EXPLOSION (pro Stunde)",
    "(real time)": "(Echtzeit)",
    "XP Boost: %1": "XP-Bonus: %1",
    "Skills": "Fertigkeiten",
    "Also grants": "Gewährt außerdem",
    "Disabled in multiplayer": "Im Mehrspieler deaktiviert",
    "Foraging": "Sammeln",
    "search radius": "Suchradius",
    "weather penalty": "Wetterabzug",
    "darkness penalty": "Dunkelheitsabzug",
    "Strength when built": "Stabilität beim Bau",
    "With %1 at {}": "Mit %1 auf {}",
    "Show XP boosts as a multiplier, not a percentage": "XP-Boni als Multiplikator statt als Prozentwert anzeigen",
    'Vanilla says "{}%%" for a level {} boost. The real figure is x{}, because a skill with no boost runs at a quarter rate. Fixed on all three screens that show it.':
        'Das Spiel schreibt "{}%%" für einen Bonus der Stufe {}. Der echte Wert ist x{}, denn eine Fertigkeit ohne Bonus läuft auf einem Viertel. Auf allen drei Bildschirmen korrigiert.',
    "Character creation: what each trait and job really does": "Charaktererstellung: was jede Eigenschaft und jeder Beruf wirklich tut",
    "Adds starting skill levels with their true XP multiplier, free traits granted, recipes taught and foraging bonuses to the tooltips in the creation screen.":
        "Ergänzt die Tooltips im Erstellungsbildschirm um Startstufen mit ihrem echten XP-Multiplikator, geschenkte Eigenschaften, gelehrte Rezepte und Sammelboni.",
    "In game: the same block on the info tab": "Im Spiel: derselbe Block im Info-Reiter",
    "Hover a trait icon or the job icon in the character info tab to read the same block after the world has started.":
        "Fahre im Info-Reiter über das Symbol einer Eigenschaft oder des Berufs, um denselben Block bei laufender Welt zu lesen.",
    "Add hand-written trait effects": "Von Hand geschriebene Eigenschaftseffekte ergänzen",
    "Effects hardcoded in the game's Java that cannot be read at runtime, so they are written by hand and checked against each build.":
        "Effekte, die im Java des Spiels festverdrahtet sind und zur Laufzeit nicht ausgelesen werden können, also von Hand geschrieben und gegen jede Version geprüft.",
    "Skills: which recipes each level requires": "Fertigkeiten: welche Rezepte jede Stufe verlangen",
    "Hover a level in the skills panel to see the recipes and builds that ask for it. Read from the game's own recipe list, so modded recipes appear too and nothing goes stale with a patch.":
        "Fahre im Fertigkeitenfenster über eine Stufe, um die Rezepte und Bauten zu sehen, die sie verlangen. Gelesen aus der Rezeptliste des Spiels selbst, also erscheinen auch Rezepte aus anderen Mods und nichts veraltet nach einem Patch.",
    "Needs this level": "Verlangen diese Stufe",
    "Skill and moodle descriptions are translation files. They cannot be switched off here; disable the mod to remove them.":
        "Die Beschreibungen von Fertigkeiten und Moodles sind Übersetzungsdateien. Sie lassen sich hier nicht abschalten; deaktiviere den Mod, um sie zu entfernen.",
    "Run self-test": "Selbsttest ausführen",

    # Trait and profession effects
    "{}%% footstep noise radius": "{}%% Lärmradius der Schritte",
    "more likely to fall when bumped": "fällt bei einem Stoß leichter hin",
    "less likely to fall when bumped": "fällt bei einem Stoß seltener hin",
    "{}%% run and sprint speed": "{}%% Lauf- und Sprinttempo",
    "no Fitness XP from level {} on": "ab Stufe {} keine Fitness-XP mehr",
    "double endurance drain when running": "doppelter Ausdauerverbrauch beim Laufen",
    "{}%% melee damage": "{}%% Nahkampfschaden",
    "{} chance to trip from a lunge": "{} Stolperchance bei einem Ausfallschritt",
    "starts at {} weight, and you lose health below {}": "startet mit Gewicht {}, und unter {} verlierst du Gesundheit",
    "{}%% axe swing time": "{}%% Schlagzeit mit der Axt",
    "{}%% axe damage to trees": "{}%% Axtschaden an Bäumen",
    "{}%% endurance lost running": "{}%% Ausdauerverlust beim Laufen",
    "{}%% grapple effectiveness": "{}%% Wirksamkeit im Ringen",
    "{}%% knockback": "{}%% Rückstoß",
    "can be gained by training Strength to {}": "erhält man, indem man Stärke auf {} trainiert",
    "becomes Strong at Strength {}": "wird bei Stärke {} zu Stark",
    "becomes Feeble at Strength {}": "wird bei Stärke {} zu Schwächlich",
    "lost by training Strength to {}": "verschwindet, wenn Stärke auf {} steigt",
    "{}%% panic, night terrors aside": "{}%% Panik, Nachtschreck ausgenommen",
    "{}%% stress from looting corpses": "{}%% Stress beim Durchsuchen von Leichen",
    "{}%% panic": "{}%% Panik",
    "no panic from a corpse reanimating": "keine Panik, wenn eine Leiche wieder aufsteht",
    "no stress from looting corpses": "Leichen durchsuchen erzeugt keinen Stress",
    "{} move speed at panic {}": "{} Tempo bei Panik {}",
    "still capped by the movement speed limit": "weiterhin durch die Tempoobergrenze begrenzt",
    "{}%% wind penalty when aiming": "{}%% Windabzug beim Zielen",
    "{}%% gun accuracy": "{}%% Genauigkeit mit Schusswaffen",
    "{}%% gun crit chance": "{}%% Kritchance mit Schusswaffen",
    "shorter aiming delay": "kürzere Zielverzögerung",
    "wider field of view": "größeres Sichtfeld",
    "{}%% max range on weapon sights": "{}%% maximale Reichweite von Visieren",
    "blurry vision": "verschwommene Sicht",
    "weapon sight range bonus at its minimum": "Reichweitenbonus von Visieren auf dem Minimum",
    "cancelled by wearing glasses": "wird durch eine Brille aufgehoben",
    "{}%% perception radius": "{}%% Wahrnehmungsradius",
    "zombies behind you become visible sooner": "Zombies hinter dir werden früher sichtbar",
    "muffled sound effects": "gedämpfte Geräusche",
    "zombies behind you become visible later": "Zombies hinter dir werden später sichtbar",
    "no sound at all": "überhaupt kein Ton",
    "you can still watch TV": "fernsehen geht trotzdem",
    "{}%% chance of not being injured by a zombie": "{}%% Chance, von einem Zombie nicht verletzt zu werden",
    "{}%% chance of being scratched by trees": "{}%% Chance, sich an Bäumen zu kratzen",
    "{}%% corpse sickness": "{}%% Leichenkrankheit",
    "{}%% chance of catching a cold": "{}%% Chance, sich zu erkälten",
    "{}%% cold strength": "{}%% Erkältungsstärke",
    "{}%% cold progression": "{}%% Fortschritt der Erkältung",
    "{}%% zombification speed": "{}%% Tempo der Zombifizierung",
    "{}%% severity of vehicle injuries": "{}%% Schwere von Fahrzeugverletzungen",
    "{}%% fracture severity": "{}%% Schwere von Brüchen",
    "all wounds heal much faster": "alle Wunden heilen viel schneller",
    "all wounds heal much slower": "alle Wunden heilen viel langsamer",
    "{}%% XP in every skill except Fitness and Strength": "{}%% XP in allen Fertigkeiten außer Fitness und Stärke",
    "{}%% reading speed": "{}%% Lesegeschwindigkeit",
    "{}%% XP in every weapon skill and Aiming": "{}%% XP in allen Waffenfertigkeiten und im Zielen",
    "{}%% inventory transfer time": "{}%% Zeit zum Umlagern von Gegenständen",
    "{}%% aiming delay": "{}%% Zielverzögerung",
    "guns jam less often": "Waffen klemmen seltener",
    "fewer injuries opening cans": "seltener Verletzungen beim Dosenöffnen",
    "guns jam more often": "Waffen klemmen häufiger",
    "more injuries opening cans": "häufiger Verletzungen beim Dosenöffnen",
    "{}%% container capacity": "{}%% Fassungsvermögen von Behältern",
    "crafting does not return leftover items": "beim Herstellen gibt es keine Reste zurück",
    "{}%% thirst": "{}%% Durst",
    "{}%% hunger": "{}%% Hunger",
    "{}%% food illness chance": "{}%% Chance auf Lebensmittelvergiftung",
    "{}%% food illness duration": "{}%% Dauer der Lebensmittelvergiftung",
    "{}%% harm from tainted water": "{}%% Schaden durch verunreinigtes Wasser",
    "{}%% tiredness gained while awake": "{}%% Müdigkeit, die im Wachzustand anfällt",
    "{}%% recovery while asleep": "{}%% Erholung im Schlaf",
    "{}%% sleep duration": "{}%% Schlafdauer",
    "you do not wake up at {} tiredness, so set an alarm": "du wachst bei Müdigkeit {} nicht auf, stell dir also einen Wecker",
    "harder to fall asleep": "schwerer einzuschlafen",
    "{}%% vision in the dark": "{}%% Sicht im Dunkeln",
    "smaller vision cone penalty at night": "geringerer Abzug auf den Sichtkegel bei Nacht",
    "{}%% chance of being spotted (new stealth)": "{}%% Chance, entdeckt zu werden (neues Schleichen)",
    "{}%% chance of being spotted (old stealth)": "{}%% Chance, entdeckt zu werden (altes Schleichen)",
    "{}%% chance of breaking kindling": "{}%% Chance, den Zunder zu zerbrechen",
    "{}%% weather penalty when aiming": "{}%% Wetterabzug beim Zielen",
    "lights fires twice as fast": "entzündet Feuer doppelt so schnell",
    "almost never scratched by trees": "kratzt sich fast nie an Bäumen",
    "{}%% endurance lost running, sprinting, carrying and dragging":
        "{}%% Ausdauerverlust beim Laufen, Sprinten, Tragen und Ziehen",
    "{}%% endurance lost swinging a weapon": "{}%% Ausdauerverlust beim Zuschlagen mit einer Waffe",
    "{}%% gear change speed": "{}%% Tempo beim Gangwechsel",
    "{}%% top speed": "{}%% Höchstgeschwindigkeit",
    "{}%% engine noise in reverse": "{}%% Motorlärm im Rückwärtsgang",
    "{}%% acceleration": "{}%% Beschleunigung",
    "{}%% reverse acceleration": "{}%% Beschleunigung im Rückwärtsgang",
    "capped at {} max speed": "Höchstgeschwindigkeit auf {} begrenzt",
    "engine noise unchanged": "Motorlärm bleibt gleich",
    "less likely to fail any fence climb": "scheitert seltener beim Überklettern eines Zauns",
    "slightly faster rope climbing": "etwas schnelleres Klettern am Seil",
    "bloody items transfer faster but cause stress": "blutige Gegenstände lassen sich schneller umlagern, machen aber Stress",
    "cannot read anything, map labels and calorie counts included":
        "kann überhaupt nichts lesen, auch keine Kartenbeschriftungen und Kalorienangaben",
    "{} panic per tick indoors, scaling down to {} in a {}-tile room":
        "{} Panik pro Tick in Innenräumen, sinkend bis {} in einem Raum mit {} Feldern",
    "a vehicle counts as a {}-tile room": "ein Fahrzeug zählt als Raum mit {} Feldern",
    "{} panic per tick whenever you are not in a room": "{} Panik pro Tick, solange du nicht in einem Raum bist",
    "faster building": "schnelleres Bauen",
    "faster barricading": "schnelleres Verbarrikadieren",
    "no bonus health on constructions in B{}": "gibt Bauten in B{} keine zusätzliche Stabilität",
    "recipes need one level less of their skill": "Rezepte verlangen eine Stufe weniger ihrer Fertigkeit",
    "you gain weight above {} calories a day instead of {}, while under {} weight":
        "du nimmst ab {} Kalorien am Tag zu statt ab {}, solange dein Gewicht unter {} liegt",
    "you need {} calories a day to gain weight instead of {}, while over {} weight":
        "du brauchst {} Kalorien am Tag zum Zunehmen statt {}, solange dein Gewicht über {} liegt",
    "unhappiness and stress rise as nicotine withdrawal builds":
        "Unglück und Stress steigen, während der Nikotinentzug wächst",
    "smoking clears the withdrawal and gives {} hunger": "Rauchen beendet den Entzug und gibt {} Hunger",
    "random coughs and sneezes give you away": "zufälliges Husten und Niesen verrät dich",
    "shows calories, carbohydrates, protein and fat on every food":
        "zeigt Kalorien, Kohlenhydrate, Proteine und Fett bei jeder Nahrung",
    "no measurable effect in B{}: no XP boost, no recipes, and nothing in the game's code reads it. The recipes come from the profession itself.":
        "in B{} ohne messbare Wirkung: kein XP-Bonus, keine Rezepte, und keine Stelle im Code des Spiels liest sie aus. Die Rezepte kommen vom Beruf selbst.",
    "x{} move speed through trees (x{} for everyone else)": "x{} Tempo zwischen Bäumen (x{} für alle anderen)",
    "starts every exercise at {}{} regularity instead of {}{}":
        "beginnt jede Übung mit Regelmäßigkeit {}{} statt {}{}",
    '{} move speed':
        '{} Bewegungstempo',
    '{} wind penalty when aiming':
        '{} Windabzug beim Zielen',
    '%1 °C':
        '%1 °C',
    'Adds rows to the inventory tooltip: how fast a line wears out, how much each hook helps and which fish a bait attracts.':
        'Fügt Zeilen im Inventar-Tooltip hinzu: wie schnell eine Schnur verschleißt, wie viel jeder Haken bringt und welche Fische ein Köder anlockt.',
    'ALLTHEINFO':
        'ALLTHEINFO',
    'Attracts':
        'Lockt an',
    "Back to vanilla's rules: Time needs Fishing {}, Temperature {}, Weather {}, Wind {}, and a species tells you nothing until you have caught it.":
        'Zurück zu den Regeln des Spiels: Die Zeit braucht Angeln {}, die Temperatur {}, das Wetter {}, der Wind {}, und eine Art verrät nichts, bis du sie gefangen hast.',
    'Best baits: %1':
        'Beste Köder: %1',
    'Bite chance':
        'Bisschance',
    'Breaks into':
        'Zerbricht zu',
    'Chance that one attempt hooks something: {}%% times temperature, weather, time, hook and abundance, capped at {}%%.':
        'Chance, dass ein Versuch etwas an den Haken bekommt: {}%% mal Temperatur, Wetter, Zeit, Haken und Fischbestand, gedeckelt bei {}%%.',
    'Fish bite more at dawn and dusk: x{} from {}:{} to {}:{} and from {}:{} to {}:{}. Any other hour is x{}.':
        'Fische beißen bei Morgen- und Abenddämmerung besser: x{} von {}:{} bis {}:{} und von {}:{} bis {}:{}. Jede andere Stunde ist x{}.',
    'Fishing gear: rods, lines, hooks and baits':
        'Angelausrüstung: Ruten, Schnüre, Haken und Köder',
    'Fishing panel: what each rating is worth':
        'Angel-Panel: was jede Bewertung wert ist',
    "Fishing: keep vanilla's Fishing level requirements":
        'Angeln: die Angel-Stufenanforderungen des Spiels behalten',
    'Hook':
        'Haken',
    'How much longer than the best possible case you wait between attempts. Fishing near the shore doubles it, and a bobber less than {} tiles away triples it.':
        'Wie viel länger du zwischen Versuchen wartest als im besten Fall. Angeln nahe am Ufer verdoppelt die Wartezeit, eine Pose näher als {} Felder verdreifacht sie.',
    'Lake':
        'See',
    'Line strength':
        'Schnurfestigkeit',
    'Moodles: description box that fits its text':
        'Moodles: Beschreibungsfeld passend zum Text',
    'Needs Fishing %1':
        'Braucht Angeln %1',
    'Only bites while you reel in':
        'Beißt nur, während du einholst',
    'Paperclip x{}, nail x{}, fishing hook x{}. With no hook the chance is x{}: nothing will ever bite.':
        'Büroklammer x{}, Nagel x{}, Angelhaken x{}. Ohne Haken ist die Chance x{}: es beißt nie etwas.',
    'Rain is x{}. Fog over {} or wind over {} is x{}. Fog and wind are the same x{}: they never stack.':
        'Regen ist x{}. Nebel über {} oder Wind über {} ist x{}. Nebel und Wind sind dasselbe x{}: sie summieren sich nie.',
    'Right-click water and pick Fishing. Puts the real multiplier next to Time, Temperature, Weather and Wind, adds hook, spot, bite chance and waiting time, and explains each one on hover.':
        'Rechtsklick aufs Wasser und Angeln wählen. Schreibt den echten Multiplikator neben Zeit, Temperatur, Wetter und Wind, ergänzt Haken, Stelle, Bisschance und Wartezeit und erklärt jedes davon beim Drüberfahren.',
    'River':
        'Fluss',
    'Spot':
        'Stelle',
    "The game's own moodle box is two lines tall and cuts off anything longer, which is most of AllTheInfo's descriptions. This draws the moodle column itself so the box grows with the text. Turn it off to go back to the vanilla widget.":
        'Das Moodle-Feld des Spiels ist zwei Zeilen hoch und schneidet alles Längere ab, also fast jede Beschreibung von AllTheInfo. Hier wird die Moodle-Spalte selbst gezeichnet, damit das Feld mit dem Text wächst. Ausschalten bringt das Widget des Spiels zurück.',
    'Trophy from %1 cm, Fishing {} and a {} in {} roll on a big catch':
        'Trophäe ab %1 cm, mit Angeln {} und einem Wurf von {} zu {} bei einem großen Fang',
    'Under {} fish is x{}, up to {} is x{}, over {} is x{}. Trash is what you pull out instead of a fish, and Fishing {} cuts it to {}%%, level {} to {}%% and level {} to {}%%.':
        'Unter {} Fischen ist x{}, bis {} ist x{}, über {} ist x{}. Müll ist das, was du statt eines Fisches herausziehst, und Angeln {} senkt ihn auf {}%%, Stufe {} auf {}%% und Stufe {} auf {}%%.',
    'Up to %1 cm and %2 kg':
        'Bis %1 cm und %2 kg',
    'Vanilla draws condition, insulation, wind, water, blood, dirt and wetness as bars with no figures. This writes the figures next to them and adds the discomfort value, which vanilla never shows at all. The run and combat speed modifiers get a signed figure too, which vanilla only ever draws as a bar with no sign.':
        'Das Spiel zeichnet Zustand, Isolierung, Wind, Wasser, Blut, Schmutz und Nässe als Balken ohne Zahlen. Hier stehen die Zahlen daneben, dazu der Unbehagenswert, den das Spiel überhaupt nie zeigt. Lauf- und Kampftempo-Modifikatoren bekommen ebenfalls eine Zahl mit Vorzeichen, während das Spiel sie nur als Balken ohne Vorzeichen zeichnet.',
    'Wait':
        'Wartezeit',
    'Waters: %1':
        'Gewässer: %1',
    'Wear per tug':
        'Verschleiß pro Ruck',
    'Wind has no coefficient of its own. Over {} it sets the weather to x{}, the same penalty fog sets, and the two do not add up.':
        'Der Wind hat keinen eigenen Koeffizienten. Über {} setzt er das Wetter auf x{}, dieselbe Strafe wie Nebel, und beide addieren sich nicht.',
    'With your bait: %1%%':
        'Mit deinem Köder: %1%%',
    'Your bait does not attract this one':
        'Dein Köder lockt diese Art nicht an',
    'best possible':
        'bestmöglich',
    'near shore':
        'nahe am Ufer',
    'no fish in this spot':
        'hier gibt es keine Fische',
    'none':
        'keiner',
    'trash':
        'Müll',
    '{} to {} °C is x{}. From {} to {} and from {} to {}, x{}. Over {} or below {}, x{}. Below {} °C, x{}.':
        '{} bis {} °C ist x{}. Von {} bis {} und von {} bis {}, x{}. Über {} oder unter {}, x{}. Unter {} °C, x{}.',
    'Fish':
        'Fische',
    'Trash':
        'Müll',
    'Trophy from %1 cm':
        'Trophäe ab %1 cm',
    'shore':
        'Ufer',
    'Best baits:':
        'Beste Köder:',
    'Size: %1-%2 cm, %3-%4 kg':
        'Größe: %1-%2 cm, %3-%4 kg',
    'Trophy: >%1 cm / >%2 kg':
        'Trophäe: >%1 cm / >%2 kg',
    'Under {} fish is x{}, up to {} is x{}, over {} is x{}. Fish schools move every day. Trash is what you pull out instead of a fish: it is fixed per spot, and Fishing {} cuts it to {}%%, level {} to {}%% and level {} to {}%%.':
        'Unter {} Fischen ist x{}, bis {} ist x{}, über {} ist x{}. Fischschwärme ziehen jeden Tag weiter. Müll ist das, was du statt eines Fisches herausziehst: er ist pro Stelle fest, und Angeln {} senkt ihn auf {}%%, Stufe {} auf {}%% und Stufe {} auf {}%%.',
    'Fishing gear: hide the combat stats':
        'Angelausrüstung: Kampfwerte ausblenden',
    "Fog over {}%% sets the weather to x{}, the same penalty wind sets, and the two never stack. Vanilla's Weather row reports neither: it says Good for rain even in a gale.":
        'Nebel über {}%% setzt das Wetter auf x{}, dieselbe Strafe wie Wind, und beide summieren sich nie. Die Wetterzeile des Spiels meldet keines von beiden: Bei Regen schreibt sie Gut, auch im Sturm.',
    'Rain is x{}. Fog over {}%% or wind over {}%% is x{}. Fog and wind are the same x{}: they never stack.':
        'Regen ist x{}. Nebel über {}%% oder Wind über {}%% ist x{}. Nebel und Wind sind dasselbe x{}: sie summieren sich nie.',
    "Rods, nets and fishing spears are weapons in the game's own scripts, so they get crit chance, swing type, attack speed and knockback. This drops that block on fishing gear. The condition and damage bars are drawn by the game in one call and cannot be removed by any mod.":
        'Ruten, Netze und Fischspeere sind in den Skripten des Spiels Waffen und bekommen deshalb Kritchance, Schlagart, Angriffstempo und Rückstoß. Das entfernt diesen Block bei Angelausrüstung. Die Balken für Zustand und Schaden zeichnet das Spiel in einem einzigen Aufruf, kein Mod kann sie entfernen.',
    'Wind has no coefficient of its own. Over {}%% it sets the weather to x{}, the same penalty fog sets, and the two do not add up.':
        'Der Wind hat keinen eigenen Koeffizienten. Über {}%% setzt er das Wetter auf x{}, dieselbe Strafe wie Nebel, und beide addieren sich nicht.',
    'Against the best possible case':
        'Gegenüber dem bestmöglichen Fall',
    'Any other hour: x{}':
        'Jede andere Stunde: x{}',
    'Below {} °C: x{}':
        'Unter {} °C: x{}',
    'Bobber under {} tiles away: x{}':
        'Pose näher als {} Felder: x{}',
    'Capped at {}%%':
        'Gedeckelt bei {}%%',
    'Fishing hook: x{}':
        'Angelhaken: x{}',
    'Fishing {}, {} and {} cut trash to {}%%, {}%% and {}%%':
        'Angeln {}, {} und {} senken den Müll auf {}%%, {}%% und {}%%',
    'Fog and wind never stack':
        'Nebel und Wind summieren sich nie',
    'Fog over {}%% or wind over {}%%: x{}':
        'Nebel über {}%% oder Wind über {}%%: x{}',
    'Nail: x{}':
        'Nagel: x{}',
    'Near shore: x{}':
        'Nahe am Ufer: x{}',
    'No hook: x{}, nothing ever bites':
        'Ohne Haken: x{}, es beißt nie etwas',
    'Over {} or below {} °C: x{}':
        'Über {} oder unter {} °C: x{}',
    'Over {}%%: x{} on the weather':
        'Über {}%%: x{} aufs Wetter',
    'Over {}: x{}':
        'Über {}: x{}',
    'Paperclip: x{}':
        'Büroklammer: x{}',
    'Rain: x{}':
        'Regen: x{}',
    'Rolled once per attempt':
        'Einmal pro Versuch gewürfelt',
    'Same penalty as fog, they never stack':
        'Dieselbe Strafe wie Nebel, sie summieren sich nie',
    'Same penalty as wind, they never stack':
        'Dieselbe Strafe wie Wind, sie summieren sich nie',
    'Schools move every day':
        'Schwärme ziehen jeden Tag weiter',
    'This row reports neither':
        'Diese Zeile meldet keines von beiden',
    'Trash is fixed per spot':
        'Der Müll ist pro Stelle fest',
    'Under {} fish: x{}':
        'Unter {} Fischen: x{}',
    '{} to {} and {} to {} °C: x{}':
        '{} bis {} und {} bis {} °C: x{}',
    '{} to {} °C: x{}':
        '{} bis {} °C: x{}',
    '{} to {}: x{}':
        '{} bis {}: x{}',
    '{}%% x temperature x weather x time x hook x fish':
        '{}%% x Temperatur x Wetter x Zeit x Haken x Fische',
    '{}:{} to {}:{} and {}:{} to {}:{}: x{}':
        '{}:{} bis {}:{} und {}:{} bis {}:{}: x{}',
    'Fishing {}, {} and {}: trash x{}, x{}, x{}':
        'Angeln {}, {} und {}: Müll x{}, x{}, x{}',
    'x time x hook x fish':
        'x Zeit x Haken x Fische',
    '{}%% x temperature x weather':
        '{}%% x Temperatur x Wetter',

    # Round 11: moodles rewritten from bytecode + wiki
    "melee damage {}%%": "{}%% Nahkampfschaden",
    "melee damage {}": "{} Nahkampfschaden",
    "move speed {}%%": "{}%% Bewegungstempo",
    "move speed {}%% with Adrenaline Junkie": "{}%% Bewegungstempo mit Adrenalinjunkie",
    "attack speed {}%%": "{}%% Angriffsgeschwindigkeit",
    "combat speed {}%%": "{}%% Kampftempo",
    "run speed {}%%": "{}%% Lauftempo",
    "crit chance {}%%": "{}%% Kritchance",
    "firearm accuracy {}%%": "{}%% Schusswaffen-Treffsicherheit",
    "firearm accuracy {}%% at {} tiles": "{0}%% Schusswaffen-Treffsicherheit auf {1} Felder",
    "clearing a jam {}%%": "{}%% Chance, eine Ladehemmung zu beheben",
    "climbing {}%%": "{}%% Klettern",
    "climbing fences {}%%": "{}%% Zäune überklettern",
    "climbing walls and ropes {}%%": "{}%% Mauern und Seile erklimmen",
    "tripping over fences {}%%": "{}%% Stolperchance an Zäunen",
    "blocking an attack {}%%": "{}%% Angriff blocken",
    "foraging {}%%": "{}%% Sammeln",
    "carry capacity {}": "{} Tragkraft",
    "healing {}%%": "{}%% Heilung",
    "healing x{}": "x{} Heilung",
    "poison wears off {}%% faster": "Gift klingt {}%% schneller ab",
    "heat dissipation {}%%": "{}%% Wärmeabgabe",
    "heat loss {}%%": "{}%% Wärmeverlust",
    "discomfort {}%%": "{}%% Unbehagen",
    "medicine {}%% less effective": "Medikamente wirken {}%% schwächer",
    "sleep {}{}%% less effective": "Schlaf wirkt {0}{1}%% schwächer",
    "panic x{} per wound": "x{} Panik pro Wunde",
    "over {}%% of capacity": "Über {}%% deiner Tragkraft",
    "health under {}%%": "Gesundheit unter {}%%",
    "health {}%% per hour": "{}%% Gesundheit pro Stunde",
    "health drops to {}%%": "Gesundheit fällt auf {}%%",
    "health drops to {}%%, then to {}%%": "Gesundheit fällt auf {0}%%, dann auf {1}%%",
    "health drops to {}%% when the air is above {} C": "Gesundheit fällt auf {0}%%, wenn die Luft über {1} C liegt",
    "health drops when the air is below {} C": "Gesundheit fällt, wenn die Luft unter {} C liegt",
    "only heals indoors, dry, under {}%% fatigue and under {}%% hunger and thirst": "Heilt nur drinnen, trocken, unter {}%% Müdigkeit und unter {}%% Hunger und Durst",
    "vision cone narrows, cancelling Eagle Eyed": "Sichtkegel wird enger und hebt Luchsaugen auf",
    "{} C colder than the air": "{} C kälter als die Luft",
    "{} wounds bleeding": "{} blutende Wunden",
    "{} wounds, or a bleeding neck": "{} Wunden oder eine blutende Halswunde",
    "no healing": "Keine Heilung",
    "no natural healing": "Keine natürliche Heilung",
    "slower healing": "Langsamere Heilung",
    "much slower healing": "Viel langsamere Heilung",
    "slower endurance recovery": "Langsamere Ausdauererholung",
    "much slower endurance recovery": "Viel langsamere Ausdauererholung",
    "endurance barely recovers": "Ausdauer erholt sich kaum",
    "endurance drains as you move and never recovers": "Ausdauer schwindet beim Gehen und erholt sich nie",
    "no sprinting or running": "Kein Sprinten und kein Laufen",
    "you cannot run": "Du kannst nicht laufen",
    "you cannot sleep": "Du kannst nicht schlafen",
    "you cannot eat any more": "Du kannst nichts mehr essen",
    "you can sleep on the ground and through pain": "Du kannst auf dem Boden und trotz Schmerzen schlafen",
    "cannot swing a sledgehammer": "Kein Vorschlaghammer mehr",
    "hunger does not rise": "Hunger steigt nicht",
    "less body heat generated": "Weniger Körperwärme",
    "body heat rises": "Körpertemperatur steigt",
    "body heat rises sharply": "Körpertemperatur steigt stark",
    "thirst and fatigue rise faster": "Durst und Müdigkeit steigen schneller",
    "you lose heat in the cold": "Du verlierst Wärme in der Kälte",
    "more likely to catch a cold": "Höheres Erkältungsrisiko",
    "more likely to fall ill": "Höheres Krankheitsrisiko",
    "much more likely to fall ill": "Viel höheres Krankheitsrisiko",
    "narrower vision cone": "Engerer Sichtkegel",
    "narrower vision and awareness": "Engere Sicht und Wahrnehmung",
    "movement, damage and attack speed drop with the wound": "Tempo, Schaden und Angriffsgeschwindigkeit sinken je nach Wunde",
    "you make noise": "Du machst Geräusche",
    "you complain out loud": "Du beschwerst dich laut",
    "you get up faster": "Du stehst schneller auf",
    "you weave as you walk": "Du torkelst beim Gehen",
    "timed actions take longer": "Handlungen dauern länger",
    "unhappiness rises": "Unzufriedenheit steigt",
    "unhappiness rises slowly": "Unzufriedenheit steigt langsam",
    "unhappiness rises fast": "Unzufriedenheit steigt schnell",
    "stress rises": "Stress steigt",
    "boredom is wiped and held down": "Langeweile wird gelöscht und bleibt unten",
    "the Desensitized trait cancels it": "Das Merkmal Abgestumpft hebt es auf",
    "no effect until NPCs return": "Ohne Wirkung, bis es NPCs gibt",
    "discomfort while in a vehicle": "Unbehagen im Fahrzeug",
    "hypothermia is hidden": "Unterkühlung wird verdeckt",
    "it wakes you up": "Es weckt dich auf",
    "you sneeze now and then": "Du niest ab und zu",
    "you sneeze and cough often": "Du niest und hustest oft",
    "you cough so much that hiding gets hard": "Du hustest so sehr, dass Verstecken schwerfällt",
    "you cough constantly and draw zombies": "Du hustest ständig und lockst Zombies an",
    "health loss": "Gesundheitsverlust",
    "slow health loss": "Langsamer Gesundheitsverlust",
    "serious health loss": "Schwerer Gesundheitsverlust",
    "health slowly drops": "Gesundheit sinkt langsam",
    "health drops if this is infection or poison": "Gesundheit sinkt, wenn es Infektion oder Gift ist",
    "death without first aid": "Tod ohne Erste Hilfe",
    "sickness starts to build": "Übelkeit baut sich auf",
    "sickness builds noticeably": "Übelkeit steigt spürbar",
    "many rotting corpses": "Viele verwesende Leichen",
    "more rotting corpses": "Mehr verwesende Leichen",
    "the worst corpses can do": "Das Schlimmste, was Leichen anrichten",
    "a generator running indoors": "Ein Generator läuft im Innenraum",
    "it will not kill you outright": "Es tötet dich nicht direkt",
    "a gas mask or SCBA prevents it": "Eine Gasmaske oder ein Atemschutzgerät verhindert es",
    "caused by heavy clothing, bags, bare feet or leg injuries": "Verursacht durch schwere Kleidung, Taschen, nackte Füße oder Beinverletzungen",

    # Animals (round 10, block C)
    "Animals: butchering yield, milk, wool and old age":
        "Tiere: Fleischertrag, Milch, Wolle und Alter",
    "Adds rows to the animal window you get by right-clicking an animal: meat yield, blood, feathers, old age and weight ceiling, which no screen shows, plus health, hunger, thirst, attitude, milk, wool and pregnancy as numbers instead of words.":
        "Fügt dem Tierfenster per Rechtsklick Zeilen hinzu: Fleischertrag, Blut, Federn, Alter und Höchstgewicht, die kein Bildschirm zeigt, dazu Gesundheit, Hunger, Durst, Verhalten, Milch, Wolle und Trächtigkeit als Zahlen statt als Worte.",
    "Animals: keep vanilla's Animal Care level requirements":
        "Tiere: Stufenanforderungen der Tierpflege beibehalten",
    "Off by default, so you see everything from level {}. Turn it on and each row reappears at the Animal Care level vanilla itself uses for it: pregnancy at {}, weight at {}, attitude at {}.":
        "Standardmäßig aus, du siehst also alles ab Stufe {}. Schalte es ein, und jede Zeile erscheint wieder auf der Tierpflege-Stufe, die das Spiel selbst dafür nutzt: Trächtigkeit auf {}, Gewicht auf {}, Verhalten auf {}.",
    "Meat yield":
        "Fleischertrag",
    "full in %1":
        "voll in %1",

    # Animal hover descriptions (round 12)
    "Size x meat gene.":
        "Größe x Fleischgen.",
    "Multiplies the number of meat pieces and the calories of each one.":
        "Multipliziert die Anzahl der Fleischstücke und die Kalorien jedes Stücks.",
    "Butchering adds x{} every {} levels.":
        "Schlachten gibt alle {} Stufen x{} dazu.",
    "Off the ground x{}, on a butcher hook x{}.":
        "Am Boden x{}, am Schlachthaken x{}.",
    "Litres you can drain into a bucket once it is dead.":
        "Liter, die du nach dem Tod in einen Eimer ablassen kannst.",
    "Grows with weight.":
        "Wächst mit dem Gewicht.",
    "Feathers you get for butchering it.":
        "Federn, die das Schlachten einbringt.",
    "Breed maximum x size.":
        "Rassenmaximum x Größe.",
    "{}%% until {}%% of its life expectancy, then it climbs to {}%%.":
        "{}%% bis zu {}%% der Lebenserwartung, danach steigt es auf {}%%.",
    "Over {}%% it loses {}%% health every hour.":
        "Über {}%% verliert es jede Stunde {}%% Gesundheit.",
    "Current weight and the most this animal can reach.":
        "Aktuelles Gewicht und das Höchste, was dieses Tier erreicht.",
    "Meat and blood both scale with it.":
        "Fleisch und Blut richten sich danach.",
    "Over {}%% hunger it starts losing weight.":
        "Über {}%% Hunger verliert es Gewicht.",
    "{}{}, how much this animal puts up with you.":
        "{}{}, wie viel dieses Tier von dir hinnimmt.",
    "Each point takes {} off the chance it breaks free while being sheared.":
        "Jeder Punkt senkt die Chance um {}, dass es sich beim Scheren losreißt.",
    "Every gain is {}, plus {} per Animal Care level.":
        "Jeder Zuwachs ist {}, plus {} pro Tierpflege-Stufe.",
    "Healthy over {}%%, off colour over {}%%, sickly over {}%%, dying below.":
        "Gesund über {}%%, angeschlagen über {}%%, kränklich über {}%%, sterbend darunter.",
    "Higher is worse.":
        "Höher ist schlechter.",
    "Well fed under {}%%, underfed under {}%%, starving over it.":
        "Gut genährt unter {}%%, unterernährt unter {}%%, verhungernd darüber.",
    "Over {}%% it starts losing weight.":
        "Über {}%% verliert es Gewicht.",
    "Fully watered under {}%%, thirsty under {}%%, dying of thirst over it.":
        "Getränkt unter {}%%, durstig unter {}%%, verdurstend darüber.",
    "{}{}. Calm under {}, unnerved under {}, agitated under {}, wild over it.":
        "{}{}. Ruhig unter {}, nervös unter {}, aufgeregt unter {}, wild darüber.",
    "Over {} milk and wool grow at {} / stress of their rate.":
        "Über {} wachsen Milch und Wolle nur mit {} / Stress ihrer Rate.",
    "Over {} a pregnancy can be lost.":
        "Über {} kann eine Trächtigkeit verloren gehen.",
    "Milking with stress over {} and Animal Care {} or less always fails and spills the bucket.":
        "Melken bei Stress über {} und Tierpflege {} oder weniger misslingt immer und verschüttet den Eimer.",
    "Litres in the udder and what it holds.":
        "Liter im Euter und was hineinpasst.",
    "It fills by capacity / {} per game hour, times the sandbox milk modifier.":
        "Füllt sich um Kapazität / {} pro Spielstunde, mal dem Sandbox-Milchmodifikator.",
    "Stress over {} slows it down.":
        "Stress über {} bremst das.",
    "Wool grown and the maximum.":
        "Gewachsene Wolle und das Maximum.",
    "It grows by maximum / {} per game hour: {} days for a full fleece.":
        "Wächst um Maximum / {} pro Spielstunde: {} Tage für ein volles Vlies.",
    "Days left before it gives birth.":
        "Tage bis zur Geburt.",
    "Stress over {} can end the pregnancy.":
        "Stress über {} kann die Trächtigkeit beenden.",
    "Hours this female stays fertilised.":
        "Stunden, die dieses Weibchen befruchtet bleibt.",
    "When it runs out she is no longer fertilised.":
        "Danach ist es nicht mehr befruchtet.",

    # Wounds and healing
    "Wounds: how long each one still needs":
        "Wunden: wie lange jede noch braucht",
    "Adds an Info entry under the treatments you get by clicking a body part in the health panel. Hover it and the box beside it gives the time left on every wound, what bandaging or a poultice would save, how long the bandage lasts and whether the part is mending or getting worse. The game knows all of it and only prints it in debug mode.":
        "Fügt unter den Behandlungen, die ein Klick auf ein Körperteil im Gesundheitsfenster öffnet, einen Eintrag Info hinzu. Beim Überfahren zeigt der Kasten daneben die Restzeit jeder Wunde, was ein Verband oder ein Wickel sparen würde, wie lange der Verband hält und ob das Körperteil heilt oder schlechter wird. Das Spiel weiß das alles und druckt es nur im Debug-Modus.",
    "Wounds: keep vanilla's Doctor level requirements":
        "Wunden: Stufenanforderungen der Humanmedizin beibehalten",
    "Off by default, so you see everything from level {}. Turn it on and each row reappears at the Doctor level vanilla itself uses for it: scratches and lacerations at {}, deep wounds and splints at {}, fractures and stitches at {}, wound infection at {}.":
        "Standardmäßig aus, du siehst also alles ab Stufe {}. Schalte es ein, und jede Zeile erscheint wieder auf der Humanmedizin-Stufe, die das Spiel selbst dafür nutzt: Kratzer und Schnittwunden auf {}, tiefe Wunden und Schienen auf {}, Brüche und Nähte auf {}, Wundinfektion auf {}.",
    "Full recovery":
        "Vollständige Genesung",
    "Getting worse":
        "Wird schlechter",
    "Healing":
        "Heilung",
    "normal":
        "normal",
    "slowed by hunger, thirst or illness":
        "durch Hunger, Durst oder Krankheit verlangsamt",
    "stopped by hunger or thirst":
        "durch Hunger oder Durst gestoppt",
    "asleep, ten times faster":
        "im Schlaf, zehnmal schneller",
    "wounded parts share it":
        "verletzte Körperteile teilen sie sich",
    "Bandage life":
        "Verbandsdauer",
    "ready to remove":
        "bereit zum Entfernen",

    # Wounds and healing, redesigned tooltip
    "Healing speed":
        "Heilungstempo",
    "clean for":
        "sauber noch",
    "Poultice":
        "Wickel",
    "Wound infection":
        "Wundinfektion",
    "won't close, glass inside":
        "schließt nicht, Glas steckt darin",
    "won't close while unbandaged":
        "schließt nicht ohne Verband",
    "rising":
        "steigend",

    # Wounds: shorter recovery label and infection risk
    "Recovery":
        "Genesung",
    "Infection risk":
        "Infektionsrisiko",

    # Percentages, ported from the multiplier wording
    "{}%% weapon damage": "{}%% Waffenschaden",
    "{}%% endurance recovery": "{}%% Ausdauerregeneration",
    "{}%% melee damage and knockback": "{}%% Nahkampfschaden und Rückstoß",
    "{}%% move speed in combat stance": "{}%% Tempo in Kampfhaltung",
    "{}%% sprint speed": "{}%% Sprinttempo",
    "{}%% chance of being spotted": "{}%% Chance, entdeckt zu werden",
    "{}%% footstep noise": "{}%% Schrittgeräusch",
    "{}%% recoil delay": "{}%% Rückstoßverzögerung",
    "{}%% aim settling speed": "{}%% Tempo beim Beruhigen des Ziels",
    "{}%% aim penalty for moving (shared with Nimble)":
        "{}%% Zielabzug durch Bewegung (geteilt mit Wendigkeit)",
    "{}%% reload speed": "{}%% Nachladetempo",
    "{}%% racking speed": "{}%% Tempo beim Durchladen",
    "{}%% XP in every Crafting skill": "{}%% XP in allen Handwerksfertigkeiten",
    "{}%% move speed through trees": "{}%% Tempo zwischen Bäumen",
    "spotting another player {}%%": "{}%% andere Spieler entdecken",
    "timed actions {}%%": "{}%% Dauer für Handlungen",
    "endurance drain {}%%": "{}%% Ausdauerverbrauch",
    "alcohol hits {}%%, and {}%% over {}%% hunger": "Alkohol wirkt {0}%%, und {1}%% über {2}%% Hunger",
    "Fitness {}, which is {}%% endurance recovery instead of {}%%":
        "Fitness {}, also {}%% Ausdauerregeneration statt {}%%",
    "{}%% attack speed": "{}%% Angriffsgeschwindigkeit",
    "{}%% crit chance": "{}%% Kritchance",
    "racking costs {}%% of the aiming time": "Durchladen kostet {}%% der Zielzeit",
    "carrying capacity {}": "Tragkraft {}",
    "{} to every weapon's durability roll.": "{} auf den Haltbarkeitswurf jeder Waffe.",
    "Condition loss (handle)": "Zustandsverlust (Griff)",
    "Condition loss (head)": "Zustandsverlust (Kopf)",

    # Ronda 4: medicine, traps, weapon components, skill levels
    '%1 corpses nearby': '%1 Leichen in der Nähe',
    '%1%% attack time': '%1%% Angriffsgeschwindigkeit',
    '%1%% crit chance': '%1%% kritische Trefferchance',
    '%1%% muscle strain': '%1%% Muskelbelastung',
    '%1%% weapon damage': '%1%% Waffenschaden',
    '+%1 to the durability roll': '+%1 auf den Haltbarkeitswurf',
    'Adds an Info entry to a placed trap: the odds of it catching anything in an hour, which animals it can take and the share of the catch each one gets, the bait and its freshness, the zone, the hourly odds of losing bait or trap, and the warning that a trap catches nothing while you stand next to it. Bait foods get a row naming what they attract.': 'Fügt einer aufgestellten Falle einen Info-Eintrag hinzu: die Chance, dass sie in einer Stunde überhaupt etwas fängt, welche Tiere sie fangen kann und welcher Anteil des Fangs auf jedes entfällt, den Köder und seine Frische, die Zone, die stündliche Chance, Köder oder Falle zu verlieren, und den Hinweis, dass eine Falle nichts fängt, solange du daneben stehst. Köder-Lebensmittel bekommen eine Zeile mit dem, was sie anlocken.',
    'Bait': 'Köder',
    'Bait lost per hour': 'Köderverlust pro Stunde',
    'In the trap for': 'In der Falle seit',
    'Filter left': 'Filter übrig',
    'Hits before it breaks': 'Treffer bis zum Bruch',
    'Medicine: duration, delay and effect': 'Medizin: Dauer, Verzögerung und Wirkung',
    'Medicine: the full list of effects': 'Medizin: die vollständige Liste der Wirkungen',
    'Muscle strain per hit': 'Muskelbelastung pro Treffer',
    'Off by default, so you see everything from level {}. Turn it on and the trap tooltip only appears from Trapping {}, which is the level vanilla itself uses elsewhere.': 'Standardmäßig aus, du siehst also alles ab Stufe {}. Eingeschaltet erscheint der Fallen-Tooltip erst ab Fallenstellen {}, der Stufe, die das Spiel selbst anderswo verwendet.',
    'Off by default. Adds everything else each pill does: what cancels it, what intoxication costs it, and the sleeping tablet overdose table.': 'Standardmäßig aus. Fügt alles Weitere hinzu, was jede Tablette tut: was sie aufhebt, was Rausch sie kostet und die Überdosis-Tabelle der Schlaftabletten.',
    'Painkillers, beta blockers, antidepressants, sleeping tablets and antibiotics get how long they last, how long they take to start and what they do per minute. Every figure is recomputed from the sandbox day length.': 'Schmerzmittel, Betablocker, Antidepressiva, Schlaftabletten und Antibiotika zeigen, wie lange sie wirken, wie lange sie bis zum Wirkungsbeginn brauchen und was sie pro Minute tun. Jeder Wert wird aus der Tageslänge der Sandbox neu berechnet.',
    'Prey': 'Beute',
    'Rots once thawed': 'Verdirbt nach dem Auftauen',
    'Stale once thawed': 'Wird nach dem Auftauen alt',
    'Takes effect in': 'Wirkt nach',
    'Trap lost per hour': 'Fallenverlust pro Stunde',
    'Traps: catch odds, bait and hours': 'Fallen: Fangchancen, Köder und Zeiten',
    "Traps: keep vanilla's Trapping level requirements": 'Fallen: die Stufenanforderungen des Spiels beim Fallenstellen beibehalten',
    'Zone': 'Zone',
    'a second dose resets the clock, it does not add': 'eine zweite Dosis setzt die Uhr zurück, sie addiert nicht',
    'a third of the strength above {} intoxication': 'ein Drittel der Stärke über {} Rausch',
    'fresh for %1': 'frisch für %1',
    'half the strength above {} intoxication': 'die halbe Stärke über {} Rausch',
    'each pill counts double above {} intoxication': 'jede Tablette zählt doppelt über {} Rausch',
    'holds the fever, does not cure it': 'hält das Fieber auf, heilt es nicht',
    'incoming panic {}%% per pill, down to nothing': 'eingehende Panik {}%% pro Tablette, bis auf null',
    'it catches nothing while you are near it': 'sie fängt nichts, solange du in der Nähe bist',
    'only the first dose has to wait': 'nur die erste Dosis muss warten',
    'overdose: {} pills cost {} health, {} cost {}, {} kill': 'Überdosis: {} Tabletten kosten {} Gesundheit, {} kosten {}, {} töten',
    'sleeping cancels the effect': 'Schlafen hebt die Wirkung auf',
    'stale, catches nothing': 'alt, lockt nichts an',
    'the longer it waits, the likelier it comes out dead': 'je länger es wartet, desto wahrscheinlicher kommt es tot heraus',
    'to full in %1': 'voll in %1',
    'to zero in %1': 'auf null in %1',
    'wound pain stops being recalculated while it lasts': 'Wundschmerz wird nicht mehr neu berechnet, solange sie wirkt',
    'zombie fever held': 'Zombiefieber aufgehalten',
    '{}%% reading time': '{}%% Lesezeit',
    'Effect': 'Wirkung',

    # Ronda 4, segunda pasada
    '%1 s': '%1 s',
    '%1 s per round': '%1 s pro Schuss',
    '%1%% attack speed': '%1%% Angriffsgeschwindigkeit',
    'Details': 'Details',
    'Info': 'Info',
    'Possible prey': 'Mögliche Beute',
    'Trap breaks per hour': 'Falle bricht pro Stunde',
    'holds the fever': 'hält das Fieber auf',
    'not being used (%1 corpses nearby)': 'wird nicht verbraucht (%1 Leichen in der Nähe)',
    'Bird': 'Vogel',
    'Active hours': 'Aktive Stunden',
    'Possible prey, share of the catch': 'Mögliche Beute, Anteil am Fang',
    'Catch chance': 'Fangchance',
    'Bait condition': 'Köderzustand',
    'Trap condition': 'Fallenzustand',
    'while you are near it, it neither catches nor breaks': 'solange du in der Nähe bist, fängt sie nichts und bricht auch nicht',
    'Bait loss risk, per hour': 'Risiko, den Köder zu verlieren, pro Stunde',
    'Wrecked by an animal, per hour': 'Von einem Tier zerstört, pro Stunde',
    '%1 / h': '%1 / h',
    'Bait loss risk': 'Risiko, den Köder zu verlieren',
    'Chance of being wrecked': 'Chance, zerstört zu werden',
    'Critical damage': 'Kritischer Schaden',
    'Effective durability': 'Effektive Haltbarkeit',
    'Damage with your character': 'Schaden mit deinem Charakter',
    'Reach (tiles)': 'Reichweite (Felder)',

    # Bags and the torch beam (0.9.20)
    'All round': 'Rundum',
    'Beam (degrees)': 'Lichtkegel (Grad)',
    'Bags: how much they slow you down': 'Taschen: wie sehr sie dich bremsen',
    "The run and combat speed a bag costs you, which the game applies and never shows. The run figure is the one you are paying right now: a bag's penalty grows by half again as it fills up, so the same pack goes from {}%% empty to {}%% full. It counts the same in your hands as on your back.": 'Die Lauf- und Kampfgeschwindigkeit, die dich eine Tasche kostet, vom Spiel angewendet und nirgends angezeigt. Der Laufwert ist der, den du gerade zahlst: Die Strafe wächst um die Hälfte, je voller die Tasche wird, also geht dieselbe Tasche von {}%% leer auf {}%% voll. In den Händen zählt sie genauso wie auf dem Rücken.',

    # Trait figures corrected against bytecode (0.9.21)
    "Aiming and Maintenance are not affected":
        "Zielen und Instandhaltung sind nicht betroffen",
    "ambient light never drops below {} in the dark":
        "das Umgebungslicht fällt im Dunkeln nie unter {}",
    "can tell a poisonous wild plant from a safe one":
        "erkennt, ob eine Wildpflanze giftig ist",
    "lights a fire with a notched plank twice as fast":
        "entzündet ein Feuer mit Kerbbrett doppelt so schnell",
    "no harm at all from tainted water":
        "verschmutztes Wasser richtet überhaupt keinen Schaden an",
    "{} health on every construction":
        "{} Lebenspunkte auf jedes Bauwerk",
    "{} tiles of perception instead of {}":
        "{} Felder Wahrnehmung statt {}",
    "{}%% XP in the six melee weapon skills":
        "{}%% XP in den sechs Nahkampfwaffenfertigkeiten",
    "{}%% chance of tearing your clothes on a tree":
        "{}%% Chance, sich die Kleidung an einem Baum aufzureißen",
    "{}%% from any other poison":
        "{}%% von jedem anderen Gift",
    "{}%% from any other poison, bleach aside":
        "{}%% von jedem anderen Gift, außer Bleiche",
    "{}%% weather penalty in combat":
        "{}%% Wetterabzug im Kampf",

    # Per-level lines for the twenty craft skills (0.9.21)
    "%1 crop health at planting":
        "%1 Pflanzengesundheit beim Setzen",
    "%1%% chance the crop is cursed if planted out of its month":
        "%1%% Chance, dass die Pflanze verflucht ist, wenn sie außerhalb ihres Monats gesetzt wird",
    "%1%% chance of a bonus harvest planted in its best month":
        "%1%% Chance auf Bonusernte, wenn im besten Monat gesetzt",
    "%1 disease removed per treatment":
        "%1 Krankheit pro Behandlung entfernt",
    "%1%% chance of harvesting %2 extra vegetables":
        "%1%% Chance, %2 Gemüse mehr zu ernten",
    "%1%% back strain planting and harvesting":
        "%1%% Rückenbelastung beim Setzen und Ernten",
    "%1 points off the chance a stressed animal breaks off milking or shearing":
        "%1 Punkte auf die Chance, dass ein gestresstes Tier beim Melken oder Scheren ausbricht",
    "a stressed animal never breaks off milking or shearing":
        "ein gestresstes Tier bricht beim Melken oder Scheren nicht mehr aus",
    "x%1 chance of each extra part off a carcass":
        "x%1 Chance auf jedes zusätzliche Teil eines Kadavers",
    "x%1 of each part":
        "x%1 von jedem Teil",
    "up to %1 blood splatters on you":
        "bis zu %1 Blutspritzer auf dir",
    "%1 health on everything you build":
        "%1 Lebenspunkte auf alles, was du baust",
    "%1%% build time":
        "%1%% Bauzeit",
    "%1%% barricading time":
        "%1%% Zeit zum Verbarrikadieren",
    "%1%% chance of recovering material when dismantling":
        "%1%% Chance, beim Abbauen Material zurückzubekommen",
    "%1%% of the ingredient used per addition":
        "%1%% der Zutat pro Zugabe verbraucht",
    "x%1 nutrients from each ingredient":
        "x%1 Nährwert aus jeder Zutat",
    "rotten food can go in evolved recipes, worth %1%% of its hunger":
        "du kannst etwas verdorbenes Essen in entwickelte Rezepte geben",
    "x%1 fracture healing with a splint":
        "x%1 Bruchheilung mit Schiene",
    "a bandage lasts %1 to %2 longer":
        "ein Verband hält %1 bis %2 länger",
    "%1%% time for every medical action":
        "%1%% Zeit für jede medizinische Handlung",
    "you can judge how bad a wound is":
        "du kannst einschätzen, wie schlimm eine Wunde ist",
    "you can read pain, and spot the burns that need washing":
        "du kannst Schmerz lesen und siehst, welche Verbrennungen gewaschen werden müssen",
    "you can tell when stitches are ready to come out":
        "du erkennst, wann Nähte gezogen werden können",
    "you spot a wound infection straight away":
        "du bemerkst eine Wundinfektion sofort",
    "%1%% chance of getting the patch back":
        "%1%% Chance, den Flicken zurückzubekommen",
    "%1%% time to add or remove a patch":
        "%1%% Zeit zum Anbringen oder Entfernen eines Flickens",
    "a hole can be repaired completely, defense and insulation included":
        "ein Loch lässt sich vollständig reparieren, samt Schutz und Isolierung",
    "+%1%% generator condition per repair":
        "+%1%% Generatorzustand pro Reparatur",
    "%1 points to the chance of hotwiring a car":
        "%1 Punkte auf die Chance, ein Auto kurzzuschließen",
    "%1%% chance of setting off the car alarm":
        "%1%% Chance, die Autoalarmanlage auszulösen",
    "you can salvage and repair a standard engine":
        "du kannst einen Standardmotor ausschlachten und reparieren",
    "you can salvage and repair a heavy-duty engine":
        "du kannst einen Schwerlastmotor ausschlachten und reparieren",
    "you can salvage and repair a sport engine":
        "du kannst einen Sportmotor ausschlachten und reparieren",
    "you can build the sturdier brick wall":
        "du kannst die stabilere Ziegelmauer bauen",
    "small %1%%, medium %2%%, large %3%%":
        "klein %1%%, mittel %2%%, groß %3%%",
    "%1 points to the chance a berry or mushroom is poisonous":
        "%1 Punkte auf die Chance, dass eine Beere oder ein Pilz giftig ist",
    "%1%% time to inspect a track":
        "%1%% Zeit, um eine Spur zu untersuchen",
    "no effect of its own, this level only unlocks the recipes below":
        "keine eigene Wirkung, diese Stufe schaltet nur die Rezepte unten frei",

    # 0.9.21 follow-up
    "%1 rags when you rip up clothing, capped by the parts it covers":
        "%1 Fetzen beim Zerreißen von Kleidung, begrenzt durch das, was sie bedeckt",
    "rotten food can go in evolved recipes, worth %1%% of its hunger":
        "verdorbenes Essen taugt für entwickelte Rezepte, es zählt %1%% seines Sättigungswerts",

    # 0.9.21 follow-up 2
    "%1%% time per litre shearing an animal":
        "%1%% Zeit pro Liter beim Scheren eines Tiers",
    "%1 rags when you rip up clothing, capped by the parts it covers":
        "%1 Lumpen beim Zerreißen von Kleidung, begrenzt durch die bedeckten Körperteile",
    "%1 to the most aramid thread you can pull out":
        "%1 auf das Maximum an Aramidfaden, das herauskommt",
    "starts at {} weight, becomes Emaciated at {} or less and Low Weight above {}":
        "startet mit Gewicht {}, bei {} oder weniger wird daraus Abgemagert und über {} Untergewichtig",
    "starts at {} weight, becomes High Weight below {}":
        "startet mit Gewicht {}, unter {} wird daraus Übergewichtig",
    "starts at {} weight, becomes Very High Weight at {} and is lost below {}":
        "startet mit Gewicht {}, bei {} wird daraus Fettleibig und unter {} geht es verloren",
    "starts at {} weight, becomes Very Low Weight at {} or less and is lost above {}":
        "startet mit Gewicht {}, bei {} oder weniger wird daraus Sehr Untergewichtig und über {} geht es verloren",
    "XP awarded":
        "Gewährte EP",
    "{} chance to trip when a zombie lunges through a window":
        "{} Stolperchance, wenn ein Zombie durch ein Fenster stürmt",
    "{} to the roll that keeps you on your feet when a zombie shoves you":
        "{} auf den Wurf, der dich auf den Beinen hält, wenn ein Zombie dich stößt",
    "{}%% muscle strain":
        "{}%% Muskelbelastung",
    "{}%% axe attack speed, chopping trees included":
        "{}%% Angriffsgeschwindigkeit mit der Axt, Bäumefällen eingeschlossen",

    # B42.20 trait corrections
    "Another x{} at panic level {}":
        "weitere x{} bei Panikstufe {}",
    "Can hotwire without Electrical {} and Mechanics {}":
        "kann ohne Elektrik {} und Mechanik {} kurzschließen",
    "Engine revs three times faster in reverse":
        "Motor dreht im Rückwärtsgang dreimal schneller hoch",
    "Halves your rope climbing bonus":
        "halbiert deinen Kletterbonus am Seil",
    "No unhappiness from looting corpses":
        "Leichen durchsuchen erzeugt kein Unglück",
    "Stress from handling bloody items":
        "Stress beim Umgang mit blutigen Gegenständen",
    "{} move speed at panic level {}, {} at level {}":
        "{} Tempo bei Panikstufe {}, {} bei Stufe {}",
    "{} to the rope climbing roll":
        "{} auf den Seilkletterwurf",
    "{}%% acceleration, fading out above {}%% of the car's top speed":
        "{}%% Beschleunigung, die über {}%% der Höchstgeschwindigkeit des Autos ausläuft",
    "{}%% carry capacity":
        "{}%% Tragkraft",
    "{}%% chance of breaking a window lock instead of {}%%":
        "{}%% das Fensterschloss zu brechen statt {}%%",
    "{}%% endurance cost on every exertion":
        "{}%% Ausdauerkosten pro Anstrengung",
    "{}%% reverse acceleration, gone past {} km/h":
        "{}%% Beschleunigung im Rückwärtsgang, ab {} km/h keine mehr",
    "{}%% unhappiness from looting corpses":
        "{}%% Unglück beim Durchsuchen von Leichen",

    # Repair recipes
    "Repair: +%1 condition, %2 chance of failing":
        "Reparatur: +%1 Zustand, %2 Fehlschlag",
    "Repair: +%1 condition, %2 chance of failing, repaired %3 times":
        "Reparatur: +%1 Zustand, %2 Fehlschlag, schon %3 Mal repariert",

    # Corpse count and temperature figures
    "Body temperature: the number on every bar":
        "Körpertemperatur: die Zahl auf jedem Balken",
    "Nauseous: how many corpses are making you ill":
        "Übelkeit: wie viele Leichen dich krank machen",
    "Rotting corpses nearby raise food sickness, and the game never says how many are close enough. Five or fewer do nothing. The count is read back out of the game, so it follows the sandbox setting.":
        "Verwesende Leichen in der Nähe erhöhen die Lebensmittelvergiftung, und das Spiel sagt nie, wie viele nah genug sind. Fünf oder weniger bewirken nichts. Die Zahl wird aus dem Spiel selbst gelesen und folgt daher der Sandbox-Einstellung.",
    "The temperature view prints its value on Insulation and Wind resistance and leaves the other nine bars as a colour. This sets the same flag on the rest, so skin temperature, body response, heat and wetness read as figures. Vanilla does the drawing, and only for the body part you have selected.":
        "Die Temperaturansicht schreibt ihren Wert auf Isolierung und Windwiderstand und lässt die anderen neun Balken als Farbe stehen. Hier bekommt der Rest dasselbe Flag, also lesen sich Hauttemperatur, Körperreaktion, Wärme und Nässe als Zahlen. Gezeichnet wird vom Spiel selbst, und nur für das ausgewählte Körperteil.",

    # Options tab
    "Custom":
        "Benutzerdefiniert",
    "Nothing matches that":
        "Nichts gefunden",
    "Moodles: how many corpses are making you ill":
        "Moodles: wie viele Leichen dich krank machen",

    # Option groups
    "Every gun this box or magazine fits, one per row.":
        "Jede Waffe, in die diese Schachtel oder dieses Magazin passt, eine pro Zeile.",
    "How bloody the garment is, out of a hundred.":
        "Wie blutig das Kleidungsstück ist, von hundert.",
    "How brightly it lights what it reaches.":
        "Wie hell es das ausleuchtet, was es erreicht.",
    "How dirty the garment is, out of a hundred.":
        "Wie schmutzig das Kleidungsstück ist, von hundert.",
    "How drunk this container will get you.":
        "Wie betrunken dich dieser Behälter machen wird.",
    "How far the light reaches, in tiles.":
        "Wie weit das Licht reicht, in Feldern.",
    "How far the shot is heard, which is how far the horde comes from.":
        "Wie weit der Schuss zu hören ist, also aus welcher Entfernung die Horde kommt.",
    "How long before the pill starts working, and only while you have none running.":
        "Wie lange es dauert, bis die Tablette wirkt, und nur solange keine wirkt.",
    "How long cooked food can stay on the heat before it burns.":
        "Wie lange gegartes Essen noch auf der Hitze bleiben kann, bevor es verbrennt.",
    "How long the charge lasts with the thing switched on.":
        "Wie lange die Ladung bei eingeschaltetem Gerät reicht.",
    "How long the filter lasts at your current exposure, and how many corpses are around you.":
        "Wie lange der Filter bei deiner aktuellen Belastung hält und wie viele Leichen um dich herum liegen.",
    "How long the item burns for as fuel.":
        "Wie lange der Gegenstand als Brennstoff brennt.",
    "How long the pages you have not read yet will take.":
        "Wie lange die noch ungelesenen Seiten dauern werden.",
    "How long the pill keeps working.":
        "Wie lange die Tablette weiterwirkt.",
    "How long the plant takes to be ready, at the current farming speed.":
        "Wie lange die Pflanze bis zur Reife braucht, bei der aktuellen Anbaugeschwindigkeit.",
    "How long until the food goes stale, at the current rot speed.":
        "Wie lange es dauert, bis das Essen altbacken wird, bei der aktuellen Verderbgeschwindigkeit.",
    "How long until the food is rotten, at the current rot speed.":
        "Wie lange es dauert, bis das Essen verdorben ist, bei der aktuellen Verderbgeschwindigkeit.",
    "How many hits the weapon has left in it, which is the one figure that compares any two weapons.":
        "Wie viele Treffer die Waffe noch hat, die einzige Zahl, die zwei beliebige Waffen vergleicht.",
    "How much cold the garment keeps out. The game only draws a bar.":
        "Wie viel Kälte das Kleidungsstück abhält. Das Spiel zeichnet nur einen Balken.",
    "How much is left in the filter.":
        "Wie viel im Filter übrig ist.",
    "How much of it you have already heard.":
        "Wie viel davon du schon gehört hast.",
    "How much of the corpse sickness the mask keeps off you. {}%% is immunity.":
        "Wie viel der Leichenkrankheit die Maske von dir fernhält. {}%% ist Immunität.",
    "How much of your hunger bar the drink covers.":
        "Wie viel deiner Hungerleiste das Getränk abdeckt.",
    "How much of your thirst bar the drink covers.":
        "Wie viel deiner Durstleiste das Getränk abdeckt.",
    "How much pull the rod takes before the line gives.":
        "Wie viel Zug die Rute aushält, bevor die Schnur nachgibt.",
    "How much rain the garment keeps out. The game only draws a bar.":
        "Wie viel Regen das Kleidungsstück abhält. Das Spiel zeichnet nur einen Balken.",
    "How much the bag slows you down, with its weight and what is inside counted.":
        "Wie sehr die Tasche dich bremst, mit ihrem Gewicht und dem Inhalt gerechnet.",
    "How much the bag slows your swing.":
        "Wie sehr die Tasche deinen Schlag bremst.",
    "How much the garment slows you down, as the penalty itself rather than a bar.":
        "Wie sehr das Kleidungsstück dich bremst, als Abzug selbst statt als Balken.",
    "How much the garment slows your swing, as the penalty itself rather than a bar.":
        "Wie sehr das Kleidungsstück deinen Schlag bremst, als Abzug selbst statt als Balken.",
    "How much tiredness this surface actually clears, your traits included.":
        "Wie viel Müdigkeit diese Unterlage tatsächlich abbaut, deine Eigenschaften eingerechnet.",
    "How much wind the garment keeps out. The game only draws a bar.":
        "Wie viel Wind das Kleidungsstück abhält. Das Spiel zeichnet nur einen Balken.",
    "How often a hit crits, with your level in the weapon's own skill counted.":
        "Wie oft ein Treffer kritisch ist, mit deinem Level in der Fertigkeit der Waffe gerechnet.",
    "How often a shot crits.":
        "Wie oft ein Schuss kritisch ist.",
    "How wet the garment is, out of a hundred.":
        "Wie nass das Kleidungsstück ist, von hundert.",
    "In tiles. A swing landed at the edge of your reach does up to twice the damage of one landed close in.":
        "In Feldern. Ein Schlag am Rand deiner Reichweite macht bis zu doppelt so viel Schaden wie einer aus der Nähe.",
    "Off by default: the game only reveals this block for packaged food or a Nutritionist.":
        "Standardmäßig aus: Das Spiel zeigt diesen Block nur bei verpacktem Essen oder mit Ernährungsberater.",
    "Rounds in the magazine right now, out of what it holds.":
        "Patronen im Magazin gerade jetzt, von dem, was hineinpasst.",
    "The calibre the magazine takes.":
        "Das Kaliber, das das Magazin nimmt.",
    "The calories in what is actually in the container, mixtures included.":
        "Die Kalorien dessen, was wirklich im Behälter ist, Mischungen eingeschlossen.",
    "The carbohydrates in what is actually in the container.":
        "Die Kohlenhydrate dessen, was wirklich im Behälter ist.",
    "The charge left, as a number instead of a bar.":
        "Die verbleibende Ladung, als Zahl statt als Balken.",
    "The edge, and the ceiling a worn head puts on it: blunt, the weapon loses the top of its damage range.":
        "Die Schärfe und die Grenze, die ein abgenutzter Kopf ihr setzt: stumpf verliert die Waffe den oberen Teil ihres Schadens.",
    "The exact minimum and maximum. The game only ever draws it as a bar.":
        "Das genaue Minimum und Maximum. Das Spiel zeichnet es nur als Balken.",
    "The exact points left, and the head's own count on a weapon that has one.":
        "Die genauen verbleibenden Punkte, und die eigene Zahl des Kopfes bei einer Waffe, die einen hat.",
    "The exact points left, where the game only draws a bar.":
        "Die genauen verbleibenden Punkte, wo das Spiel nur einen Balken zeichnet.",
    "The fat in what is actually in the container.":
        "Das Fett dessen, was wirklich im Behälter ist.",
    "The fatigue each swing costs you.":
        "Die Erschöpfung, die dich jeder Schlag kostet.",
    "The furthest tile the gun can hit.":
        "Das entfernteste Feld, das die Waffe treffen kann.",
    "The gun's own hit chance, before your aiming skill.":
        "Die eigene Trefferchance der Waffe, vor deiner Zielfertigkeit.",
    "The hook fitted, and what it does to your odds of a bite.":
        "Der montierte Haken und was er mit deiner Bisschance macht.",
    "The line fitted, and how much of it each tug wears away.":
        "Die montierte Schnur und wie viel davon jeder Ruck abnutzt.",
    "The months it can be sown in, one per row.":
        "Die Monate, in denen gesät werden kann, einer pro Zeile.",
    "The multiplier your shoes put on stomping a downed zombie. Footwear only.":
        "Der Multiplikator, den deine Schuhe dem Zertreten eines liegenden Zombies geben. Nur Schuhwerk.",
    "The multiplier your skill puts on this weapon's swing.":
        "Der Multiplikator, den deine Fertigkeit dem Schlag dieser Waffe gibt.",
    "The net pace of the pill, which is what compares two of them at a glance.":
        "Das Nettotempo der Tablette, das zwei davon auf einen Blick vergleicht.",
    "The odds of losing a point of condition on a hit, with Maintenance and the weapon's skill counted.":
        "Die Chance, bei einem Treffer einen Zustandspunkt zu verlieren, mit Instandhaltung und der Fertigkeit der Waffe gerechnet.",
    "The odds of losing a point of condition per shot.":
        "Die Chance, pro Schuss einen Zustandspunkt zu verlieren.",
    "The poison the drink carries, and only while the game is willing to tell you.":
        "Die echte Chance auf eine Ladehemmung, Abnutzung und schwacher Griff eingeschlossen.",
    "The proteins in what is actually in the container.":
        "Die Proteine dessen, was wirklich im Behälter ist.",
    "The real odds of a jam, wear and a weak grip included.":
        "Das Gift, das das Getränk trägt, und nur solange das Spiel bereit ist, es dir zu sagen.",
    "The real seconds a reload takes, with your reloading skill and your panic counted.":
        "Die echten Sekunden, die ein Nachladen dauert, mit deiner Nachladefertigkeit und Panik gerechnet.",
    "The real seconds spent lining up the shot, with your aiming skill and your traits counted.":
        "Die echten Sekunden fürs Anlegen des Schusses, mit deiner Zielfertigkeit und deinen Eigenschaften gerechnet.",
    "The recipes it teaches that you do not know yet, one per row.":
        "Die Rezepte, die es lehrt und die du noch nicht kennst, eines pro Zeile.",
    "The swing animation, which is what really separates a slow weapon from a fast one.":
        "Die Schlaganimation, die eine langsame Waffe wirklich von einer schnellen trennt.",
    "What a critical is worth, from {}%% to {}%% depending on the weapon. The game shows it nowhere.":
        "Was ein Kritischer wert ist, von {}%% bis {}%% je nach Waffe. Das Spiel zeigt es nirgends.",
    "What feeds the Uncomfortable moodle. The game never shows it on the garment at all.":
        "Was das Moodle für Unbehagen speist. Das Spiel zeigt es am Kleidungsstück überhaupt nicht.",
    "What is left in your hands when the rod breaks.":
        "Was dir in den Händen bleibt, wenn die Rute bricht.",
    "What sleeping here costs you in comfort.":
        "Was dich das Schlafen hier an Komfort kostet.",
    "What the drink does to boredom and unhappiness, which move together here.":
        "Was das Getränk mit Langeweile und Unzufriedenheit macht, die hier zusammen laufen.",
    "What the drink does to your fatigue bar.":
        "Was das Getränk mit deiner Erschöpfungsleiste macht.",
    "What the drink does to your stress.":
        "Was das Getränk mit deinem Stress macht.",
    "What the food still needs, and the temperature the figure assumes.":
        "Was dem Essen noch fehlt, und die Temperatur, die die Zahl annimmt.",
    "Whether it is a cone you aim or a lamp that lights all around, and how wide the cone is.":
        "Ob es ein Kegel ist, den du richtest, oder eine Lampe, die rundum leuchtet, und wie weit der Kegel öffnet.",
    "Which fish this bait brings in.":
        "Welche Fische dieser Köder anlockt.",
    "Which skill the tape or disc trains and how much experience is left in it.":
        "Welche Fertigkeit das Band oder die Scheibe schult und wie viel Erfahrung noch darin steckt.",
    "Which skill the weapon trains, and therefore which one drives its damage and its speed.":
        "Welche Fertigkeit die Waffe schult, und damit welche ihren Schaden und ihr Tempo antreibt.",
    "Your own reading speed, traits, glasses and sitting down included.":
        "Dein eigenes Lesetempo, Eigenschaften, Brille und Sitzen eingeschlossen.",
    "Nutrition":
        "Nährwerte",
    "Sleep":
        "Schlaf",
    "How much the bag slows your attack. It multiplies the weapon's own swing speed, not your walking.":
        "Wie sehr die Tasche deinen Angriff bremst. Sie multipliziert das Schlagtempo der Waffe selbst, nicht dein Gehen.",
    "How much the garment slows your attack. It multiplies the weapon's own swing speed, not your walking.":
        "Wie sehr das Kleidungsstück deinen Angriff bremst. Es multipliziert das Schlagtempo der Waffe selbst, nicht dein Gehen.",
    "Best baits":
        "Beste Köder",
    "Every animal this trap can catch and its share of the catch.":
        "Jedes Tier, das diese Falle fangen kann, und sein Anteil am Fang.",
    "Feathers":
        "Federn",
    "Fog on a line of its own, because the game lumps it into weather and then reports neither.":
        "Nebel in einer eigenen Zeile, weil das Spiel ihn ins Wetter wirft und dann über keins von beiden berichtet.",
    "Glass or a bullet still in the wound, which stops it healing until it is out.":
        "Glas oder eine Kugel noch in der Wunde, die sie am Heilen hindert, bis sie draußen ist.",
    "How far the disease has gone, out of a hundred.":
        "Wie weit die Krankheit fortgeschritten ist, von hundert.",
    "How far the generator is heard, halved when it stands indoors.":
        "Wie weit der Generator zu hören ist, halbiert, wenn er drinnen steht.",
    "How full the udder is and whether it can be milked yet.":
        "Wie voll das Euter ist und ob schon gemolken werden kann.",
    "How hungry the animal is, and how long its feed will last.":
        "Wie hungrig das Tier ist und wie lange sein Futter reicht.",
    "How long before old age starts costing the animal its yield.":
        "Wie lange, bis das Alter dem Tier seinen Ertrag zu kosten beginnt.",
    "How long each cut, scratch, burn or bite still needs.":
        "Wie lange jeder Schnitt, Kratzer, jede Verbrennung oder jeder Biss noch braucht.",
    "How long is left of a pregnancy, or of an egg being fertilised.":
        "Wie viel von einer Trächtigkeit übrig ist, oder davon, dass ein Ei befruchtet wird.",
    "How long since the last watering. The game works it out to pick a colour and then never shows it.":
        "Wie lange das letzte Gießen her ist. Das Spiel rechnet es aus, um eine Farbe zu wählen, und zeigt es nie.",
    "How long the bandage lasts before it is dirty and worth changing.":
        "Wie lange der Verband hält, bevor er schmutzig ist und ein Wechsel sich lohnt.",
    "How long the catch has been waiting in there.":
        "Wie lange der Fang schon dort drin wartet.",
    "How long the fracture needs, and what the splint on it is worth.":
        "Wie lange der Bruch braucht und was die Schiene daran wert ist.",
    "How long the fuel in the tank lasts at the current draw.":
        "Wie lange der Kraftstoff im Tank beim aktuellen Verbrauch reicht.",
    "How long the part needs to be whole again, and how fast it is healing.":
        "Wie lange das Körperteil braucht, um wieder heil zu sein, und wie schnell es heilt.",
    "How long the stiffness in that limb takes to pass.":
        "Wie lange die Steifheit in diesem Glied zum Vergehen braucht.",
    "How long the stitches need, and when they can come out.":
        "Wie lange die Nähte brauchen und wann sie raus können.",
    "How long until it breaks down for good, on average.":
        "Wie lange, bis er endgültig kaputtgeht, im Schnitt.",
    "How long until it wears down to the point where it can catch fire.":
        "Wie lange, bis er so weit abgenutzt ist, dass er Feuer fangen kann.",
    "How long until the crop moves to its next stage.":
        "Wie lange, bis die Pflanze in ihre nächste Stufe geht.",
    "How long you will wait compared with the best possible spot.":
        "Wie lange du wartest, verglichen mit der bestmöglichen Stelle.",
    "How many feathers butchering will give.":
        "Wie viele Federn das Zerlegen bringt.",
    "How many fish this spot still holds, and what that is worth.":
        "Wie viele Fische diese Stelle noch hat und was das wert ist.",
    "How much blood butchering will give.":
        "Wie viel Blut das Zerlegen bringt.",
    "How much fertiliser the plot holds. Above one is the too much case in the game's own code.":
        "Wie viel Dünger das Beet hält. Über eins ist im Code des Spiels selbst der Fall von zu viel.",
    "How much meat butchering will give, which is what answers whether it is worth killing yet.":
        "Wie viel Fleisch das Zerlegen bringt, und genau das beantwortet, ob sich das Schlachten schon lohnt.",
    "How much of the bait is still good.":
        "Wie viel vom Köder noch gut ist.",
    "How much the animal trusts you, which is what lets you handle it.":
        "Wie sehr das Tier dir vertraut, und genau das erlaubt dir den Umgang mit ihm.",
    "How much wool has grown back and whether it can be sheared yet.":
        "Wie viel Wolle nachgewachsen ist und ob schon geschoren werden kann.",
    "How stressed the animal is, out of a hundred.":
        "Wie gestresst das Tier ist, von hundert.",
    "How the wound infection is going, and whether it is still rising.":
        "Wie es um die Wundinfektion steht und ob sie noch steigt.",
    "How thirsty the animal is, and how long its water will last.":
        "Wie durstig das Tier ist und wie lange sein Wasser reicht.",
    "Level needed":
        "Benötigtes Level",
    "Lodged objects":
        "Steckengebliebene Objekte",
    "Odds with your bait":
        "Chance mit deinem Köder",
    "Predator":
        "Raubfisch",
    "Size and weight":
        "Größe und Gewicht",
    "Strength at the top skill level":
        "Stabilität auf der höchsten Stufe",
    "The Fishing level this species needs before it will bite.":
        "Das Angel-Level, das diese Art braucht, bevor sie anbeißt.",
    "The animal's health as a number.":
        "Die Gesundheit des Tieres als Zahl.",
    "The animal's weight, and how far it still has to grow.":
        "Das Gewicht des Tieres und wie weit es noch wachsen kann.",
    "The chance of this exact species with the bait you are using.":
        "Die Chance auf genau diese Art mit dem Köder, den du benutzt.",
    "The crop's health out of a hundred. The game only prints it with debug on.":
        "Die Gesundheit der Pflanze von hundert. Das Spiel schreibt sie nur mit Debug an.",
    "The fuel still in the tank. The game knows the number and only prints it as a debug option.":
        "Der Kraftstoff, der noch im Tank ist. Das Spiel kennt die Zahl und zeigt sie nur als Debug-Option.",
    "The health the wall or door will have when you build it at your current level.":
        "Die Stabilität, die die Wand oder die Tür hat, wenn du sie auf deinem jetzigen Level baust.",
    "The hourly odds of a bang loud enough to pull zombies in.":
        "Die stündliche Chance auf einen Knall, laut genug, um Zombies anzuziehen.",
    "The hourly odds of a fire or an explosion, which set the generator to zero outright.":
        "Die stündliche Chance auf Feuer oder Explosion, die den Generator sofort auf null setzen.",
    "The hourly odds of the bait being taken without a catch.":
        "Die stündliche Chance, dass der Köder ohne Fang geholt wird.",
    "The hourly odds of the trap being wrecked.":
        "Die stündliche Chance, dass die Falle zerstört wird.",
    "The hourly odds of the wound becoming infected.":
        "Die stündliche Chance, dass sich die Wunde entzündet.",
    "The hours of the day the trap actually works.":
        "Die Tagesstunden, in denen die Falle tatsächlich arbeitet.",
    "The kind of ground the trap is standing on, which decides what can come.":
        "Die Art Boden, auf der die Falle steht, die entscheidet, was kommen kann.",
    "The odds of a bite once every factor is put together.":
        "Die Chance auf einen Biss, wenn jeder Faktor zusammengerechnet ist.",
    "The odds of catching anything at all in an hour.":
        "Die Chance, in einer Stunde überhaupt etwas zu fangen.",
    "The range of lengths and weights this species comes in.":
        "Die Spanne an Längen und Gewichten, in der diese Art vorkommt.",
    "The share of your catches that will be junk here.":
        "Der Anteil deiner Fänge, der hier Müll sein wird.",
    "The two things the game never says: a long wait kills the catch, and standing nearby stops the trap.":
        "Die zwei Dinge, die das Spiel nie sagt: langes Warten tötet den Fang, und in der Nähe zu stehen legt die Falle still.",
    "The water level as a number, and the amount this seed actually needs.":
        "Der Wasserstand als Zahl, und die Menge, die dieses Saatgut wirklich braucht.",
    "Time to the danger threshold":
        "Zeit bis zur Gefahrenschwelle",
    "Trophy size":
        "Trophäengröße",
    "Warnings":
        "Warnungen",
    "Warns that the species only bites while you reel in.":
        "Warnt davor, dass die Art nur beim Einholen anbeißt.",
    "What a catch has to beat to count as a trophy.":
        "Was ein Fang übertreffen muss, um als Trophäe zu zählen.",
    "What the herbs in the bandage are adding.":
        "Was die Kräuter im Verband beitragen.",
    "What the same build would have at level {}, which is the reason to know the figure before building.":
        "Was derselbe Bau auf Level {} hätte, und genau darum lohnt sich die Zahl vor dem Bauen.",
    "What the time of day is worth, as the multiplier behind the game's own rating.":
        "Was die Tageszeit wert ist, als der Multiplikator hinter der Bewertung des Spiels.",
    "What the water temperature is worth, with the actual reading in degrees.":
        "Was die Wassertemperatur wert ist, mit der tatsächlichen Anzeige in Grad.",
    "What the weather is worth, as the multiplier behind the game's own rating.":
        "Was das Wetter wert ist, als der Multiplikator hinter der Bewertung des Spiels.",
    "What the wind is worth. Past half strength it costs the same penalty fog does, and the two never stack.":
        "Was der Wind wert ist. Über halber Stärke kostet er denselben Abzug wie Nebel, und beide stapeln sich nie.",
    "Whether the mains or a generator is keeping the pump running.":
        "Ob das Netz oder ein Generator die Zapfsäule am Laufen hält.",
    "Which animals a bait item brings in.":
        "Welche Tiere ein als Köder benutzter Gegenstand anlockt.",
    "Which bait is in the trap, and whether it is still fresh.":
        "Welcher Köder in der Falle liegt und ob er noch frisch ist.",
    "Which baits work best on this species.":
        "Welche Köder bei dieser Art am besten wirken.",
    "Which growth stage the crop is on, out of the total.":
        "In welcher Wachstumsstufe die Pflanze ist, von allen.",
    "Which hook is fitted and what it does to your odds.":
        "Welcher Haken montiert ist und was er mit deinen Chancen macht.",
    "Raw eggs never make you ill":
        "Rohe Eier machen dich nie krank",
    "{}%% wait before another anti-nausea food works":
        "{}%% Wartezeit, bis ein weiteres Mittel gegen Übelkeit wirkt",
    "{}%% weapon sight range":
        "{}%% Reichweite von Zielfernrohren",
    "At Axe {} you swing as fast as a maxed axe user":
        "Mit Axt auf {} schlägst du so schnell wie ein Axtmeister",
    "{}%% from any poisonous food or drink":
        "{}%% von jedem giftigen Essen oder Getränk",
    "{}%% chance of illness from rotten food":
        "{}%% Chance, von verdorbenem Essen krank zu werden",
    "Melee weapons":
        "Nahkampfwaffen",
    "Firearms":
        "Schusswaffen",
    "Drinks":
        "Getränke",
    "Skill XP":
        "Fertigkeits-XP",
    "Weapons":
        "Waffen",
    "Worn and carried":
        "Kleidung und Behälter",
    "Medicine and reading":
        "Medizin und Lektüre",
    "Supplies":
        "Vorräte",
    "Comparison":
        "Vergleich",
    "Power and fuel":
        "Strom und Treibstoff",
    "Animals and traps":
        "Tiere und Fallen",
    "Traits and jobs":
        "Eigenschaften und Berufe",
    "Moodles":
        "Moodles",
}
