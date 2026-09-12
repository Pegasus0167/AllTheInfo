"""French phrase table for AllInfo.

Keys are the English fragment with every number replaced by {} in order.
Numbers are never written here: they ride through untouched. Use {0} {1} ...
instead of {} when the language needs a different order -- and then index every
slot, Python refuses to mix the two forms.

Run `python tools\\i18n.py` after editing: it checks the arity of every line and
refuses to write a language file it cannot fill completely.
"""

T = {
    # Per-level skill descriptions
    "x{} weapon damage (x{} untrained)": "x{} de dégâts de l'arme (x{} sans entraînement)",
    "{} to the durability roll": "{} au jet de durabilité",
    "{} chance to trip vaulting a fence": "{} de chance de trébucher en franchissant une clôture",
    "{}%% fall damage": "{}%% de dégâts de chute",
    "x{} endurance recovery (x{} untrained)": "x{} de récupération d'endurance (x{} sans entraînement)",
    "x{} melee damage and knockback (x{} untrained)": "x{} de dégâts au corps à corps et de recul (x{} sans entraînement)",
    "x{} carrying capacity (x{} untrained)": "x{} de capacité de charge (x{} sans entraînement)",
    "x{} move speed in combat stance (x{} untrained)": "x{} de vitesse en posture de combat (x{} sans entraînement)",
    "x{} sprint speed (x{} untrained)": "x{} de vitesse de sprint (x{} sans entraînement)",
    "x{} chance of being spotted (x{} untrained)": "x{} de chance d'être repéré (x{} sans entraînement)",
    "x{} footstep noise (x{} untrained)": "x{} de bruit de pas (x{} sans entraînement)",
    "{} accuracy (the weapon's aiming modifier, {} on nearly every gun)":
        "{} de précision (le modificateur de visée de l'arme, {} sur presque toutes)",
    "{} wind penalty when aiming (of {})": "{} de malus de vent à la visée (sur {})",
    "x{} reload speed (x{} untrained)": "x{} de vitesse de rechargement (x{} sans entraînement)",
    "x{} racking speed (x{} untrained)": "x{} de vitesse d'armement (x{} sans entraînement)",
    "racking costs {} of the aiming time ({} untrained)": "armer coûte {} du temps de visée ({} sans entraînement)",
    "From here on you no longer count as unsteady with a firearm, as long as your Strength is {} or more: jam chance drops by {} percentage points.":
        "À partir d'ici vous ne comptez plus comme instable avec une arme à feu, tant que votre Force est de {} ou plus : la chance d'enrayement baisse de {} points de pourcentage.",
    "You never count as unsteady with a firearm again, whatever your Strength.":
        "Vous ne comptez plus jamais comme instable avec une arme à feu, quelle que soit votre Force.",

    # Moodles
    "{} melee to-hit": "{} de précision au corps à corps",
    "{} climb chance": "{} de chance d'escalader",
    "{} trip chance": "{} de chance de trébucher",
    "{} to break a zombie's grab": "{} pour se libérer de la prise d'un zombie",
    "{}%% strength": "{}%% de force",
    "{}%% healing": "{}%% de guérison",
    "losing health": "la santé baisse",
    "harder to unjam a gun": "plus dur de désenrayer une arme",
    "{} move speed (of {})": "{} de vitesse de déplacement (sur {})",
    "body at {} C": "corps à {} C",
    "{} carry capacity": "{} de capacité de charge",
    "x{} attack speed": "x{} de vitesse d'attaque",
    "endurance under {}%%": "endurance sous {}%%",
    "fatigue over {}%%": "fatigue au-dessus de {}%%",
    "hunger over {}%%": "faim au-dessus de {}%%",
    "thirst over {}%%": "soif au-dessus de {}%%",
    "panic over {}%%": "panique au-dessus de {}%%",
    "stress over {}%%": "stress au-dessus de {}%%",
    "boredom over {}%%": "ennui au-dessus de {}%%",
    "unhappiness over {}%%": "tristesse au-dessus de {}%%",
    "{}%% action speed": "{}%% de vitesse des actions",
    "anger over {}%%": "colère au-dessus de {}%%",
    "drunkenness over {}%%": "ivresse au-dessus de {}%%",
    "pain over {}%%": "douleur au-dessus de {}%%",
    "slower rope climbing": "montée à la corde plus lente",
    "{}%% total body damage": "{}%% de dégâts corporels totaux",
    "sickness over {}%%": "maladie au-dessus de {}%%",
    "cold strength over {}%%": "intensité du rhume au-dessus de {}%%",
    "wetness over {}%%": "humidité au-dessus de {}%%",
    "discomfort over {}%%": "inconfort au-dessus de {}%%",
    "rotting corpses nearby": "cadavres en décomposition à proximité",
    "x{} move speed": "x{} de vitesse de déplacement",
    "{} discomfort per level": "{} d'inconfort par niveau",
    "{} C on top of the air temperature": "{} C en plus de la température de l'air",
    "carrying {}x capacity": "charge à {}x la capacité",
    "{}%% body heat": "{}%% de chaleur corporelle",
    "no sleep without pills": "pas de sommeil sans somnifères",
    "erratic movement": "déplacement erratique",
    "raises discomfort": "augmente l'inconfort",
    "no sprinting": "pas de sprint",
    "no sprinting, no exercise": "pas de sprint, pas d'exercice",
    "zombies spot you {} sooner": "les zombies vous repèrent {} plus tôt",
    "muscle stiffness builds up": "la raideur musculaire s'accumule",
    "cannot eat or open food": "impossible de manger ou d'ouvrir de la nourriture",
    "{} move speed with Adrenaline Junkie": "{} de vitesse avec Accro à l'adrénaline",
    "nightmares while asleep": "cauchemars pendant le sommeil",
    "no sleep below {}%% fatigue without pills": "sans somnifères, pas de sommeil sous {}%% de fatigue",
    "{}%% move speed": "{}%% de vitesse de déplacement",
    "cannot move": "impossible de bouger",
    "{} climbing walls and ropes": "{} pour escalader murs et cordes",
    "no running, no exercise": "pas de course, pas d'exercice",
    "over {}x capacity": "au-dessus de {}x la capacité",
    "no running": "pas de course",
    "no sprinting until you drop the bulky item": "pas de sprint tant que vous portez l'objet encombrant",
    "you can sleep through high pain": "vous pouvez dormir malgré une forte douleur",
    "no endurance recovery": "l'endurance ne remonte plus",
    "{} vision cone": "{} au cône de vision",
    "delayed vehicle controls": "commandes du véhicule retardées",
    "narrowed vision cone": "cône de vision rétréci",
    "no exercise": "pas d'exercice",
    "{} wound bleeding": "{} plaie qui saigne",
    "Rest in peace.": "Repose en paix.",
    "Infected. There is no cure.": "Infecté. Il n'y a pas de remède.",

    # Tooltip labels
    "Stale in": "Rassis dans",
    "Rots in": "Pourri dans",
    "Cooking time": "Temps de cuisson",
    "Never": "Jamais",
    "Critical chance": "Chance de critique",
    "Trains": "Entraîne",
    "Attack speed": "Vitesse d'attaque",
    "Swing type": "Type de coup",
    "Heavy": "Lourd",
    "Swung": "Balancé",
    "Stabbing": "Perforant",
    "Spear": "Lance",
    "Stone": "Pierre",
    "Knockback on hit": "Recul au contact",
    "Condition loss": "Perte d'état",
    "Jam chance": "Chance d'enrayement",
    "Accuracy": "Précision",
    "Noise radius": "Rayon de bruit",
    "Rounds": "Munitions",
    "Reload time": "Temps de rechargement",
    "Aiming time": "Temps de visée",
    "Used by": "Utilisée par",
    "Reading speed": "Vitesse de lecture",
    "Reading time left": "Lecture restante",
    "Skill too low to learn from it": "Compétence trop basse pour en apprendre",
    "Nothing left to learn from it": "Plus rien à en apprendre",
    "Proteins": "Protéines",
    "Sow in": "Semer en",
    "Ready in": "Prêt dans",
    "Burn time": "Durée de combustion",
    # Power: charge, autonomy and light
    "Duration": "Durée",
    "Light range": "Portée de la lumière",
    "Light strength": "Intensité de la lumière",
    "Batteries and radios: charge left, how long it lasts and how far a torch lights": "Piles et radios : charge restante, autonomie et portée d'une lampe torche",
    "Vanilla draws the charge of a drainable as a bar with no number on it, and never says how long a torch lasts or how far it lights. A torch spends its UseDelta once every ten game minutes, and only while it is in a hand or attached to you: left in a bag it switches itself off. Light range and strength are the figures that actually light the ground.":
        "Le jeu dessine la charge d'un consommable sous forme de barre sans chiffre, et ne dit jamais combien de temps dure une lampe torche ni jusqu'où elle éclaire. Une lampe torche dépense son UseDelta une fois toutes les dix minutes de jeu, et seulement tant qu'elle est en main ou accrochée à vous : rangée dans un sac, elle s'éteint toute seule. La portée et l'intensité de la lumière sont les chiffres qui éclairent vraiment le sol.",
    "Rest quality": "Qualité du repos",
    "Discomfort": "Inconfort",
    "Stomp damage": "Dégâts de piétinement",
    "Corpse sickness defense": "Protection contre la maladie des cadavres",
    "Filter charge": "Charge du filtre",
    "New recipes": "Nouvelles recettes",
    "Listened": "Écouté",
    "Skill too high for this tape": "Compétence trop élevée pour cette cassette",

    # Options screen
    "All Info": "All Info",
    "Enable everything": "Tout activer",
    "Items": "Objets",
    "Crafting": "Artisanat",
    "World": "Monde",
    "Character": "Personnage",
    "Everything in this section": "Tout dans cette section",
    "Food: time left before it spoils": "Nourriture : temps avant qu'elle ne s'abîme",
    "Adds hours to stale and hours to rotten, at the current rate. Accounts for the fridge, the freezer and the sandbox spoilage speed.":
        "Indique les heures avant rassissement et avant pourriture, au rythme actuel. Tient compte du frigo, du congélateur et de la vitesse de péremption du bac à sable.",
    "Cooking: add the warm-up minutes": "Cuisson : ajouter les minutes de chauffe",
    "Off by default. Cooking time is the time at temperature; this adds the four minutes the food spends heating up before it starts to cook, so an oven timer set to the figure rings when the food is done.":
        "Désactivé par défaut. Le temps de cuisson vaut pour un aliment déjà à température ; ceci ajoute les quatre minutes qu'il met à chauffer avant de commencer à cuire, pour que le minuteur du four sonne quand c'est prêt.",
    "Food: calories, carbs, protein and fat": "Nourriture : calories, glucides, protéines et lipides",
    "Off by default. Showing macros on every food undoes the Nutritionist trait, which is what normally reveals them.":
        "Désactivé par défaut. Afficher les macros sur toute la nourriture annule le trait Nutritionniste, qui sert justement à les révéler.",
    "Melee: exact damage, speed and durability": "Corps à corps : dégâts, vitesse et durabilité exacts",
    "Puts numbers on the condition and damage bars, and adds crit chance, swing type, attack speed, knockback and the odds of losing a condition point per hit.":
        "Met des chiffres sur les barres d'état et de dégâts, et ajoute la chance de critique, le type de coup, la vitesse d'attaque, le recul et la probabilité de perdre un point d'état par coup.",
    "Firearms: range, jam chance and reload": "Armes à feu : portée, enrayement et rechargement",
    "Puts numbers on the condition and damage bars, and adds accuracy, effective range, jam odds and magazine size.":
        "Met des chiffres sur les barres d'état et de dégâts, et ajoute la précision, la portée efficace, la chance d'enrayement et la taille du chargeur.",
    "Ammo: rounds left and what it fits": "Munitions : combien il en reste et à quoi elles vont",
    "No comparison arrows here: the thing in your hands is a gun, not another magazine, so there is no honest pair to compare.":
        "Pas de flèches de comparaison ici : ce que vous tenez est une arme, pas un autre chargeur, il n'y a donc aucune paire honnête à comparer.",
    "Clothing: numbers on every bar, plus discomfort": "Vêtements : des chiffres sur toutes les barres, plus l'inconfort",
    "Vanilla draws condition, insulation, wind, water, blood, dirt and wetness as bars with no figures. This writes the figures next to them and adds the discomfort value, which vanilla never shows at all.":
        "Le jeu dessine l'état, l'isolation, le vent, l'eau, le sang, la saleté et l'humidité en barres sans chiffres. Ici les chiffres sont écrits à côté, avec en plus l'inconfort, que le jeu n'affiche nulle part.",
    "Seeds: growing time and yield": "Graines : temps de pousse et récolte",
    "Firewood: how long it burns": "Bois de chauffage : durée de combustion",
    "Books: reading time and skill levels covered": "Livres : temps de lecture et niveaux couverts",
    "Reading time already accounts for Fast Reader, Slow Reader and reading glasses.":
        "Le temps de lecture tient déjà compte de Lecteur rapide, Lecteur lent et des lunettes de lecture.",
    "Beds: how well you recover on them": "Lits : la qualité du repos qu'ils offrent",
    "Masks: filter life and protection": "Masques : durée du filtre et protection",
    "Tapes and CDs: which skill they teach and how much XP": "Cassettes et CD : quelle compétence ils enseignent et combien d'XP",
    "Show the difference against what you have equipped": "Afficher la différence avec ce qui est équipé",
    "Adds a coloured +/- next to weapon and clothing values. Weapons compare against what is in your hands, clothing against the piece worn in the same slot.":
        "Ajoute un +/- coloré à côté des valeurs d'armes et de vêtements. Les armes se comparent à ce que vous tenez, les vêtements à la pièce portée au même emplacement.",
    "Crafting: full item tooltip on the recipe output": "Artisanat : infobulle complète sur le résultat de la recette",
    "Hovering the result of a recipe shows the same block an item in your inventory would, comparison included, before you craft it.":
        "Survoler le résultat d'une recette affiche le même bloc qu'un objet de votre inventaire, comparaison comprise, avant même de le fabriquer.",
    "Generators: fuel time, wear and danger": "Générateurs : carburant, usure et danger",
    "Adds noise radius, hours of fuel left, average time until {}%% condition and until it breaks, and the hourly odds of a backfire or a fire.":
        "Ajoute le rayon de bruit, les heures de carburant restantes, le temps moyen jusqu'à {}%% d'état et jusqu'à la panne, ainsi que la probabilité horaire de retour de flamme ou d'incendie.",
    "Generators: also show times in real-world minutes": "Générateurs : afficher aussi les durées en minutes réelles",
    "Off by default. Converts the in-game hours using the current day length, so you know how long you actually have to wait.":
        "Désactivé par défaut. Convertit les heures de jeu selon la durée de journée actuelle, pour savoir combien de temps vous attendez vraiment.",
    "Generators: outline the powered area on the floor": "Générateurs : tracer au sol la zone alimentée",
    "Draws the edge of the range while the generator window is open, green when running and red when off. Only the floor you are standing on is computed.":
        "Trace le bord de la portée tant que la fenêtre du générateur est ouverte, vert s'il tourne et rouge s'il est arrêté. Seul l'étage où vous vous trouvez est calculé.",
    "Gas pumps: fuel left and power source": "Pompes à essence : carburant restant et source d'alimentation",
    "Adds an Info entry to the right-click menu of any gas pump, with the fuel still in the tank and whether the mains or a generator is keeping it running. The game knows that number and only prints it as a debug option.":
        "Ajoute une entrée Info au menu clic droit de toute pompe à essence, avec le carburant qui reste dans la cuve et si c'est le réseau ou un générateur qui l'alimente. Le jeu connaît ce nombre et ne l'affiche qu'en option de débogage.",
    "Fuel Remaining": "Carburant restant",
    "Mains power": "Réseau électrique",
    "Generator": "Générateur",
    "Walls and doors: health under the cursor": "Murs et portes : solidité sous le curseur",
    "Shows current and maximum health as a number at the foot of whatever you point at, no clicking needed.":
        "Affiche la solidité actuelle et maximale en chiffres au pied de ce que vous visez, sans aucun clic.",
    "Build menu: health of what you are about to build": "Menu de construction : solidité de ce que vous allez bâtir",
    "Also shows what that health would be with the relevant skill at {}, so you can tell whether it is worth waiting.":
        "Indique aussi ce que serait cette solidité avec la compétence concernée à {}, pour savoir si cela vaut la peine d'attendre.",
    "Crops: health, growth and water as numbers": "Cultures : santé, croissance et eau en chiffres",
    "Adds rows to the crop window you get by right-clicking a plant: health out of {}, current phase, hours to the next one, water level against what the plant needs, time since the last watering and pest levels.":
        "Ajoute des lignes à la fenêtre obtenue par clic droit sur une plante : santé sur {}, phase actuelle, heures avant la suivante, niveau d'eau face au besoin de la plante, temps depuis le dernier arrosage et niveau de chaque nuisible.",
    "Crops: keep vanilla's Farming level requirements": "Cultures : conserver les paliers d'Agriculture du jeu",
    "Off by default, so you see everything from level {}. Turn it on and each row reappears at the Farming level vanilla itself uses for it: phase and health at {}, water at {}, pests at {}, next phase at {}.":
        "Désactivé par défaut, vous voyez donc tout dès le niveau {}. Activé, chaque ligne réapparaît au niveau d'Agriculture que le jeu utilise lui-même : phase et santé à {}, eau à {}, nuisibles à {}, phase suivante à {}.",
    "Noise": "Bruit",
    "tiles": "cases",
    "Down to %1%% (avg)": "Jusqu'à %1%% (moy.)",
    "Breaks down in (avg)": "Tombe en panne dans (moy.)",
    "Backfire, loud (per hour)": "Retour de flamme, bruyant (par heure)",
    "FIRE OR EXPLOSION (per hour)": "INCENDIE OU EXPLOSION (par heure)",
    "(real time)": "(temps réel)",
    "XP Boost: %1": "Bonus d'XP : %1",
    "Skills": "Compétences",
    "Also grants": "Accorde aussi",
    "Disabled in multiplayer": "Désactivé en multijoueur",
    "Foraging": "Cueillette",
    "search radius": "rayon de recherche",
    "weather penalty": "malus de météo",
    "darkness penalty": "malus d'obscurité",
    "Strength when built": "Solidité à la construction",
    "With %1 at {}": "Avec %1 à {}",
    "Show XP boosts as a multiplier, not a percentage": "Afficher les bonus d'XP en multiplicateur, pas en pourcentage",
    'Vanilla says "{}%%" for a level {} boost. The real figure is x{}, because a skill with no boost runs at a quarter rate. Fixed on all three screens that show it.':
        'Le jeu affiche "{}%%" pour un bonus de niveau {}. Le vrai chiffre est x{}, parce qu\'une compétence sans bonus tourne au quart. Corrigé sur les trois écrans concernés.',
    "Character creation: what each trait and job really does": "Création de personnage : ce que fait vraiment chaque trait et chaque métier",
    "Adds starting skill levels with their true XP multiplier, free traits granted, recipes taught and foraging bonuses to the tooltips in the creation screen.":
        "Ajoute aux infobulles de l'écran de création les niveaux de départ avec leur vrai multiplicateur d'XP, les traits offerts, les recettes enseignées et les bonus de cueillette.",
    "In game: the same block on the info tab": "En jeu : le même bloc dans l'onglet d'informations",
    "Hover a trait icon or the job icon in the character info tab to read the same block after the world has started.":
        "Survolez l'icône d'un trait ou celle du métier dans l'onglet d'informations pour lire le même bloc une fois le monde lancé.",
    "Add hand-written trait effects": "Ajouter les effets de traits écrits à la main",
    "Effects hardcoded in the game's Java that cannot be read at runtime, so they are written by hand and checked against each build.":
        "Effets codés en dur dans le Java du jeu, impossibles à lire à l'exécution : ils sont donc écrits à la main et vérifiés à chaque version.",
    "Skills: which recipes each level requires": "Compétences : quelles recettes exigent chaque niveau",
    "Hover a level in the skills panel to see the recipes and builds that ask for it. Read from the game's own recipe list, so modded recipes appear too and nothing goes stale with a patch.":
        "Survolez un niveau dans le panneau des compétences pour voir les recettes et constructions qui l'exigent. Lu dans la liste de recettes du jeu lui-même : les recettes d'autres mods apparaissent aussi et rien ne périme après un patch.",
    "Needs this level": "Exigent ce niveau",
    "Skill and moodle descriptions are translation files. They cannot be switched off here; disable the mod to remove them.":
        "Les descriptions de compétences et de moodles sont des fichiers de traduction. On ne peut pas les désactiver ici ; désactivez le mod pour les retirer.",
    "Run self-test": "Lancer l'autotest",

    # Trait and profession effects
    "{}%% footstep noise radius": "{}%% de rayon de bruit des pas",
    "more likely to fall when bumped": "tombe plus facilement quand on vous bouscule",
    "less likely to fall when bumped": "tombe moins facilement quand on vous bouscule",
    "{}%% run and sprint speed": "{}%% de vitesse de course et de sprint",
    "no Fitness XP from level {} on": "plus d'XP de Condition physique à partir du niveau {}",
    "double endurance drain when running": "deux fois plus d'endurance dépensée en courant",
    "{}%% melee damage": "{}%% de dégâts au corps à corps",
    "{} chance to trip from a lunge": "{} de chance de trébucher sur une fente",
    "starts at {} weight, and you lose health below {}": "commence à {} de poids, et en dessous de {} vous perdez de la santé",
    "{}%% axe swing time": "{}%% de temps de coup à la hache",
    "{}%% axe damage to trees": "{}%% de dégâts de hache sur les arbres",
    "{}%% endurance lost running": "{}%% d'endurance dépensée en courant",
    "{}%% grapple effectiveness": "{}%% d'efficacité au corps-à-corps agrippé",
    "{}%% knockback": "{}%% de recul",
    "can be gained by training Strength to {}": "s'obtient en montant la Force à {}",
    "becomes Strong at Strength {}": "devient Fort à Force {}",
    "becomes Feeble at Strength {}": "devient Chétif à Force {}",
    "lost by training Strength to {}": "se perd en montant la Force à {}",
    "{}%% panic, night terrors aside": "{}%% de panique, hors terreurs nocturnes",
    "{}%% stress from looting corpses": "{}%% de stress en fouillant les cadavres",
    "{}%% panic": "{}%% de panique",
    "no panic from a corpse reanimating": "aucune panique quand un cadavre se relève",
    "no stress from looting corpses": "fouiller les cadavres ne stresse pas",
    "{} move speed at panic {}": "{} de vitesse à panique {}",
    "still capped by the movement speed limit": "toujours limité par le plafond de vitesse",
    "{}%% wind penalty when aiming": "{}%% de malus de vent à la visée",
    "{}%% gun accuracy": "{}%% de précision aux armes à feu",
    "{}%% gun crit chance": "{}%% de chance de critique aux armes à feu",
    "shorter aiming delay": "délai de visée plus court",
    "wider field of view": "champ de vision plus large",
    "{}%% max range on weapon sights": "{}%% de portée maximale des viseurs",
    "blurry vision": "vision floue",
    "weapon sight range bonus at its minimum": "bonus de portée des viseurs au minimum",
    "cancelled by wearing glasses": "annulé en portant des lunettes",
    "{}%% perception radius": "{}%% de rayon de perception",
    "zombies behind you become visible sooner": "les zombies derrière vous deviennent visibles plus tôt",
    "muffled sound effects": "sons étouffés",
    "zombies behind you become visible later": "les zombies derrière vous deviennent visibles plus tard",
    "no sound at all": "aucun son du tout",
    "you can still watch TV": "vous pouvez quand même regarder la télé",
    "{}%% chance of not being injured by a zombie": "{}%% de chance de ne pas être blessé par un zombie",
    "{}%% chance of being scratched by trees": "{}%% de chance de se griffer aux arbres",
    "{}%% corpse sickness": "{}%% de maladie des cadavres",
    "{}%% chance of catching a cold": "{}%% de chance d'attraper un rhume",
    "{}%% cold strength": "{}%% d'intensité du rhume",
    "{}%% cold progression": "{}%% de progression du rhume",
    "{}%% zombification speed": "{}%% de vitesse de zombification",
    "{}%% severity of vehicle injuries": "{}%% de gravité des blessures de véhicule",
    "{}%% fracture severity": "{}%% de gravité des fractures",
    "all wounds heal much faster": "toutes les plaies guérissent bien plus vite",
    "all wounds heal much slower": "toutes les plaies guérissent bien plus lentement",
    "{}%% XP in every skill except Fitness and Strength": "{}%% d'XP dans toutes les compétences sauf Condition physique et Force",
    "{}%% reading speed": "{}%% de vitesse de lecture",
    "{}%% XP in every weapon skill and Aiming": "{}%% d'XP dans toutes les compétences d'arme et en Visée",
    "{}%% inventory transfer time": "{}%% de temps pour déplacer des objets",
    "{}%% aiming delay": "{}%% de délai de visée",
    "guns jam less often": "les armes s'enrayent moins souvent",
    "fewer injuries opening cans": "moins de blessures en ouvrant des conserves",
    "guns jam more often": "les armes s'enrayent plus souvent",
    "more injuries opening cans": "plus de blessures en ouvrant des conserves",
    "{}%% container capacity": "{}%% de capacité des conteneurs",
    "crafting does not return leftover items": "l'artisanat ne rend pas les restes",
    "{}%% thirst": "{}%% de soif",
    "{}%% hunger": "{}%% de faim",
    "{}%% food illness chance": "{}%% de chance d'intoxication alimentaire",
    "{}%% food illness duration": "{}%% de durée de l'intoxication alimentaire",
    "{}%% harm from tainted water": "{}%% de dégâts de l'eau souillée",
    "{}%% tiredness gained while awake": "{}%% de fatigue accumulée éveillé",
    "{}%% recovery while asleep": "{}%% de récupération pendant le sommeil",
    "{}%% sleep duration": "{}%% de durée du sommeil",
    "you do not wake up at {} tiredness, so set an alarm": "vous ne vous réveillez pas à {} de fatigue, mettez un réveil",
    "harder to fall asleep": "plus dur de s'endormir",
    "{}%% vision in the dark": "{}%% de vision dans le noir",
    "smaller vision cone penalty at night": "moins de malus au cône de vision la nuit",
    "{}%% chance of being spotted (new stealth)": "{}%% de chance d'être repéré (nouvelle furtivité)",
    "{}%% chance of being spotted (old stealth)": "{}%% de chance d'être repéré (ancienne furtivité)",
    "{}%% chance of breaking kindling": "{}%% de chance de casser l'amadou",
    "{}%% weather penalty when aiming": "{}%% de malus de météo à la visée",
    "lights fires twice as fast": "allume les feux deux fois plus vite",
    "almost never scratched by trees": "presque jamais griffé par les arbres",
    "{}%% endurance lost running, sprinting, carrying and dragging":
        "{}%% d'endurance dépensée en courant, sprintant, portant et traînant",
    "{}%% endurance lost swinging a weapon": "{}%% d'endurance dépensée en frappant avec une arme",
    "{}%% gear change speed": "{}%% de vitesse de passage des vitesses",
    "{}%% top speed": "{}%% de vitesse de pointe",
    "{}%% engine noise in reverse": "{}%% de bruit moteur en marche arrière",
    "{}%% acceleration": "{}%% d'accélération",
    "{}%% reverse acceleration": "{}%% d'accélération en marche arrière",
    "capped at {} max speed": "vitesse maximale limitée à {}",
    "engine noise unchanged": "le bruit moteur ne change pas",
    "less likely to fail any fence climb": "rate moins souvent l'escalade d'une clôture",
    "slightly faster rope climbing": "montée à la corde un peu plus rapide",
    "bloody items transfer faster but cause stress": "les objets ensanglantés se déplacent plus vite mais stressent",
    "cannot read anything, map labels and calorie counts included":
        "ne peut rien lire, y compris les étiquettes de carte et les calories",
    "{} panic per tick indoors, scaling down to {} in a {}-tile room":
        "{} de panique par tick en intérieur, jusqu'à {} dans une pièce de {} cases",
    "a vehicle counts as a {}-tile room": "un véhicule compte comme une pièce de {} cases",
    "{} panic per tick whenever you are not in a room": "{} de panique par tick dès que vous n'êtes pas dans une pièce",
    "faster building": "construction plus rapide",
    "faster barricading": "barricadage plus rapide",
    "no bonus health on constructions in B{}": "en B{}, n'apporte aucune solidité supplémentaire aux constructions",
    "recipes need one level less of their skill": "les recettes demandent un niveau de moins dans leur compétence",
    "you gain weight above {} calories a day instead of {}, while under {} weight":
        "vous prenez du poids au-dessus de {} calories par jour au lieu de {}, tant que votre poids est sous {}",
    "you need {} calories a day to gain weight instead of {}, while over {} weight":
        "il vous faut {} calories par jour pour prendre du poids au lieu de {}, tant que votre poids dépasse {}",
    "unhappiness and stress rise as nicotine withdrawal builds":
        "la tristesse et le stress montent à mesure que le manque de nicotine s'installe",
    "smoking clears the withdrawal and gives {} hunger": "fumer supprime le manque et donne {} de faim",
    "random coughs and sneezes give you away": "des toux et éternuements aléatoires vous trahissent",
    "shows calories, carbohydrates, protein and fat on every food":
        "affiche calories, glucides, protéines et lipides sur toute la nourriture",
    "no measurable effect in B{}: no XP boost, no recipes, and nothing in the game's code reads it. The recipes come from the profession itself.":
        "aucun effet mesurable en B{} : pas de bonus d'XP, pas de recettes, et aucun endroit du code du jeu ne le lit. Les recettes viennent du métier lui-même.",
    "x{} move speed through trees (x{} for everyone else)": "x{} de vitesse entre les arbres (x{} pour tous les autres)",
    "starts every exercise at {}{} regularity instead of {}{}":
        "commence chaque exercice avec une régularité de {}{} au lieu de {}{}",
    '{} move speed':
        '{} de vitesse de déplacement',
    '{} wind penalty when aiming':
        '{} de malus de vent à la visée',
    '%1 °C':
        '%1 °C',
    'Adds rows to the inventory tooltip: how fast a line wears out, how much each hook helps and which fish a bait attracts.':
        "Ajoute des lignes à l'infobulle de l'inventaire : à quelle vitesse un fil s'use, ce que chaque hameçon apporte et quels poissons un appât attire.",
    'ALLTHEINFO':
        'ALLTHEINFO',
    'Attracts':
        'Attire',
    "Back to vanilla's rules: Time needs Fishing {}, Temperature {}, Weather {}, Wind {}, and a species tells you nothing until you have caught it.":
        "Retour aux règles du jeu : l'heure exige Pêche {}, la température {}, la météo {}, le vent {}, et une espèce ne dit rien tant que vous ne l'avez pas pêchée.",
    'Best baits: %1':
        'Meilleurs appâts : %1',
    'Bite chance':
        'Chance de touche',
    'Breaks into':
        'Se casse en',
    'Chance that one attempt hooks something: {}%% times temperature, weather, time, hook and abundance, capped at {}%%.':
        "Chance qu'une tentative accroche quelque chose : {}%% multiplié par la température, la météo, l'heure, l'hameçon et l'abondance, plafonné à {}%%.",
    'Fish bite more at dawn and dusk: x{} from {}:{} to {}:{} and from {}:{} to {}:{}. Any other hour is x{}.':
        "Les poissons mordent plus à l'aube et au crépuscule : x{} de {}:{} à {}:{} et de {}:{} à {}:{}. Toute autre heure est x{}.",
    'Fishing gear: rods, lines, hooks and baits':
        'Matériel de pêche : cannes, fils, hameçons et appâts',
    'Fishing panel: what each rating is worth':
        'Panneau de pêche : ce que vaut chaque mention',
    "Fishing: keep vanilla's Fishing level requirements":
        'Pêche : garder les niveaux de Pêche exigés par le jeu',
    'Hook':
        'Hameçon',
    'How much longer than the best possible case you wait between attempts. Fishing near the shore doubles it, and a bobber less than {} tiles away triples it.':
        "Combien de temps de plus vous attendez entre deux tentatives par rapport au meilleur cas. Pêcher près de la rive double l'attente, et un bouchon à moins de {} cases la triple.",
    'Lake':
        'Lac',
    'Line strength':
        'Résistance du fil',
    'Moodles: description box that fits its text':
        'Moodles : cadre de description à la taille du texte',
    'Needs Fishing %1':
        'Exige Pêche %1',
    'Only bites while you reel in':
        'Ne mord que pendant que vous moulinez',
    'Paperclip x{}, nail x{}, fishing hook x{}. With no hook the chance is x{}: nothing will ever bite.':
        'Trombone x{}, clou x{}, hameçon de pêche x{}. Sans hameçon la chance est x{} : rien ne mordra jamais.',
    'Rain is x{}. Fog over {} or wind over {} is x{}. Fog and wind are the same x{}: they never stack.':
        'La pluie est x{}. Le brouillard au-dessus de {} ou le vent au-dessus de {} donne x{}. Brouillard et vent sont le même x{} : ils ne se cumulent jamais.',
    'Right-click water and pick Fishing. Puts the real multiplier next to Time, Temperature, Weather and Wind, adds hook, spot, bite chance and waiting time, and explains each one on hover.':
        "Clic droit sur l'eau puis Pêcher. Met le vrai multiplicateur à côté de l'heure, de la température, de la météo et du vent, ajoute l'hameçon, le coin, la chance de touche et l'attente, et explique chacun au survol.",
    'River':
        'Rivière',
    'Spot':
        'Coin',
    "The game's own moodle box is two lines tall and cuts off anything longer, which is most of AllTheInfo's descriptions. This draws the moodle column itself so the box grows with the text. Turn it off to go back to the vanilla widget.":
        "Le cadre de moodle du jeu fait deux lignes de haut et coupe tout ce qui dépasse, c'est-à-dire presque toutes les descriptions d'AllTheInfo. Ici la colonne de moodles est dessinée par le mod, donc le cadre grandit avec le texte. Désactivez pour retrouver le widget du jeu.",
    'Trophy from %1 cm, Fishing {} and a {} in {} roll on a big catch':
        'Trophée à partir de %1 cm, avec Pêche {} et un jet de {} sur {} sur une grosse prise',
    'Under {} fish is x{}, up to {} is x{}, over {} is x{}. Trash is what you pull out instead of a fish, and Fishing {} cuts it to {}%%, level {} to {}%% and level {} to {}%%.':
        "Moins de {} poissons c'est x{}, jusqu'à {} c'est x{}, plus de {} c'est x{}. Les déchets sont ce que vous sortez à la place d'un poisson, et Pêche {} les réduit à {}%%, le niveau {} à {}%% et le niveau {} à {}%%.",
    'Up to %1 cm and %2 kg':
        "Jusqu'à %1 cm et %2 kg",
    'Vanilla draws condition, insulation, wind, water, blood, dirt and wetness as bars with no figures. This writes the figures next to them and adds the discomfort value, which vanilla never shows at all. The run and combat speed modifiers get a signed figure too, which vanilla only ever draws as a bar with no sign.':
        "Le jeu dessine l'état, l'isolation, le vent, l'eau, le sang, la saleté et l'humidité en barres sans chiffres. Ici les chiffres sont écrits à côté, plus la valeur d'inconfort, que le jeu ne montre nulle part. Les modificateurs de vitesse de course et de combat reçoivent aussi un chiffre signé, là où le jeu ne dessine qu'une barre sans signe.",
    'Wait':
        'Attente',
    'Waters: %1':
        'Eaux : %1',
    'Wear per tug':
        'Usure par à-coup',
    'Wind has no coefficient of its own. Over {} it sets the weather to x{}, the same penalty fog sets, and the two do not add up.':
        "Le vent n'a pas de coefficient propre. Au-dessus de {} il met la météo à x{}, la même pénalité que le brouillard, et les deux ne s'additionnent pas.",
    'With your bait: %1%%':
        'Avec votre appât : %1%%',
    'Your bait does not attract this one':
        "Votre appât n'attire pas cette espèce",
    'best possible':
        'le mieux possible',
    'near shore':
        'près de la rive',
    'no fish in this spot':
        'pas de poisson ici',
    'none':
        'aucun',
    'trash':
        'déchets',
    '{} to {} °C is x{}. From {} to {} and from {} to {}, x{}. Over {} or below {}, x{}. Below {} °C, x{}.':
        "De {} à {} °C c'est x{}. De {} à {} et de {} à {}, x{}. Au-dessus de {} ou en dessous de {}, x{}. En dessous de {} °C, x{}.",
    'Fish':
        'Poissons',
    'Trash':
        'Déchets',
    'Trophy from %1 cm':
        'Trophée à partir de %1 cm',
    'shore':
        'rive',
    'Best baits:':
        'Meilleurs appâts :',
    'Size: %1-%2 cm, %3-%4 kg':
        'Taille : %1-%2 cm, %3-%4 kg',
    'Trophy: >%1 cm / >%2 kg':
        'Trophée : >%1 cm / >%2 kg',
    'Under {} fish is x{}, up to {} is x{}, over {} is x{}. Fish schools move every day. Trash is what you pull out instead of a fish: it is fixed per spot, and Fishing {} cuts it to {}%%, level {} to {}%% and level {} to {}%%.':
        "Moins de {} poissons c'est x{}, jusqu'à {} c'est x{}, plus de {} c'est x{}. Les bancs de poissons se déplacent chaque jour. Les déchets sont ce que vous sortez à la place d'un poisson : ils sont fixes par coin, et Pêche {} les réduit à {}%%, le niveau {} à {}%% et le niveau {} à {}%%.",
    'Fishing gear: hide the combat stats':
        'Matériel de pêche : masquer les stats de combat',
    "Fog over {}%% sets the weather to x{}, the same penalty wind sets, and the two never stack. Vanilla's Weather row reports neither: it says Good for rain even in a gale.":
        "Un brouillard au-dessus de {}%% met la météo à x{}, la même pénalité que le vent, et les deux ne se cumulent jamais. La ligne Météo du jeu n'en signale aucun : elle affiche Bon pour la pluie même en pleine tempête.",
    'Rain is x{}. Fog over {}%% or wind over {}%% is x{}. Fog and wind are the same x{}: they never stack.':
        'La pluie est x{}. Un brouillard au-dessus de {}%% ou un vent au-dessus de {}%% donne x{}. Brouillard et vent sont le même x{} : ils ne se cumulent jamais.',
    "Rods, nets and fishing spears are weapons in the game's own scripts, so they get crit chance, swing type, attack speed and knockback. This drops that block on fishing gear. The condition and damage bars are drawn by the game in one call and cannot be removed by any mod.":
        "Les cannes, filets et harpons sont des armes dans les scripts du jeu, donc ils reçoivent chance de critique, type de coup, vitesse d'attaque et recul. Ceci retire ce bloc sur le matériel de pêche. Les barres d'état et de dégâts sont dessinées par le jeu en un seul appel et aucun mod ne peut les enlever.",
    'Wind has no coefficient of its own. Over {}%% it sets the weather to x{}, the same penalty fog sets, and the two do not add up.':
        "Le vent n'a pas de coefficient propre. Au-dessus de {}%% il met la météo à x{}, la même pénalité que le brouillard, et les deux ne s'additionnent pas.",
    'Against the best possible case':
        'Par rapport au meilleur cas possible',
    'Any other hour: x{}':
        'Toute autre heure : x{}',
    'Below {} °C: x{}':
        'En dessous de {} °C : x{}',
    'Bobber under {} tiles away: x{}':
        'Bouchon à moins de {} cases : x{}',
    'Capped at {}%%':
        'Plafonné à {}%%',
    'Fishing hook: x{}':
        'Hameçon de pêche : x{}',
    'Fishing {}, {} and {} cut trash to {}%%, {}%% and {}%%':
        'Pêche {}, {} et {} réduisent les déchets à {}%%, {}%% et {}%%',
    'Fog and wind never stack':
        'Brouillard et vent ne se cumulent jamais',
    'Fog over {}%% or wind over {}%%: x{}':
        'Brouillard au-dessus de {}%% ou vent au-dessus de {}%% : x{}',
    'Nail: x{}':
        'Clou : x{}',
    'Near shore: x{}':
        'Près de la rive : x{}',
    'No hook: x{}, nothing ever bites':
        'Sans hameçon : x{}, rien ne mord jamais',
    'Over {} or below {} °C: x{}':
        'Au-dessus de {} ou en dessous de {} °C : x{}',
    'Over {}%%: x{} on the weather':
        'Au-dessus de {}%% : x{} sur la météo',
    'Over {}: x{}':
        'Au-dessus de {} : x{}',
    'Paperclip: x{}':
        'Trombone : x{}',
    'Rain: x{}':
        'Pluie : x{}',
    'Rolled once per attempt':
        'Lancé une fois par tentative',
    'Same penalty as fog, they never stack':
        'La même pénalité que le brouillard, ils ne se cumulent jamais',
    'Same penalty as wind, they never stack':
        'La même pénalité que le vent, ils ne se cumulent jamais',
    'Schools move every day':
        'Les bancs se déplacent chaque jour',
    'This row reports neither':
        "Cette ligne n'en signale aucun",
    'Trash is fixed per spot':
        'Les déchets sont fixes par coin',
    'Under {} fish: x{}':
        'Moins de {} poissons : x{}',
    '{} to {} and {} to {} °C: x{}':
        'De {} à {} et de {} à {} °C : x{}',
    '{} to {} °C: x{}':
        'De {} à {} °C : x{}',
    '{} to {}: x{}':
        'De {} à {} : x{}',
    '{}%% x temperature x weather x time x hook x fish':
        '{}%% x température x météo x heure x hameçon x poissons',
    '{}:{} to {}:{} and {}:{} to {}:{}: x{}':
        'De {}:{} à {}:{} et de {}:{} à {}:{} : x{}',
    'Fishing {}, {} and {}: trash x{}, x{}, x{}':
        'Pêche {}, {} et {} : déchets x{}, x{}, x{}',
    'x time x hook x fish':
        'x heure x hameçon x poissons',
    '{}%% x temperature x weather':
        '{}%% x température x météo',

    # Round 11: moodles rewritten from bytecode + wiki
    "melee damage {}%%": "{}%% de dégâts de mêlée",
    "melee damage {}": "{} de dégâts de mêlée",
    "move speed {}%%": "{}%% de vitesse de déplacement",
    "move speed {}%% with Adrenaline Junkie": "{}%% de vitesse avec Accro à l'adrénaline",
    "attack speed {}%%": "{}%% de vitesse d'attaque",
    "combat speed {}%%": "{}%% de vitesse au combat",
    "run speed {}%%": "{}%% de vitesse de course",
    "crit chance {}%%": "{}%% de chances de critique",
    "firearm accuracy {}%%": "{}%% de précision aux armes à feu",
    "firearm accuracy {}%% at {} tiles": "{0}%% de précision aux armes à feu à {1} cases",
    "clearing a jam {}%%": "{}%% de chances de débloquer une arme",
    "climbing {}%%": "{}%% pour grimper",
    "climbing fences {}%%": "{}%% pour franchir une clôture",
    "climbing walls and ropes {}%%": "{}%% pour grimper murs et cordes",
    "tripping over fences {}%%": "{}%% de risque de chute aux clôtures",
    "blocking an attack {}%%": "{}%% pour bloquer une attaque",
    "foraging {}%%": "{}%% en cueillette",
    "carry capacity {}": "{} de capacité de charge",
    "healing {}%%": "{}%% de guérison",
    "healing x{}": "guérison x{}",
    "poison wears off {}%% faster": "Le poison se dissipe {}%% plus vite",
    "heat dissipation {}%%": "{}%% de dissipation de chaleur",
    "heat loss {}%%": "{}%% de perte de chaleur",
    "discomfort {}%%": "{}%% d'inconfort",
    "medicine {}%% less effective": "Médicaments {}%% moins efficaces",
    "sleep {}{}%% less effective": "Sommeil {0}{1}%% moins réparateur",
    "panic x{} per wound": "panique x{} par blessure",
    "over {}%% of capacity": "Plus de {}%% de votre capacité",
    "health under {}%%": "Santé sous {}%%",
    "health {}%% per hour": "{}%% de santé par heure",
    "health drops to {}%%": "La santé descend à {}%%",
    "health drops to {}%%, then to {}%%": "La santé descend à {0}%%, puis à {1}%%",
    "health drops to {}%% when the air is above {} C": "La santé descend à {0}%% quand l'air dépasse {1} C",
    "health drops when the air is below {} C": "La santé baisse quand l'air est sous {} C",
    "only heals indoors, dry, under {}%% fatigue and under {}%% hunger and thirst": "Ne guérit qu'à l'intérieur, au sec, sous {}%% de fatigue et sous {}%% de faim et de soif",
    "vision cone narrows, cancelling Eagle Eyed": "Le cône de vision se rétrécit et annule Oeil de lynx",
    "{} C colder than the air": "{} C de moins que l'air",
    "{} wounds bleeding": "{} plaies qui saignent",
    "{} wounds, or a bleeding neck": "{} plaies, ou une plaie au cou",
    "no healing": "Aucune guérison",
    "no natural healing": "Aucune guérison naturelle",
    "slower healing": "Guérison plus lente",
    "much slower healing": "Guérison bien plus lente",
    "slower endurance recovery": "Récupération d'endurance plus lente",
    "much slower endurance recovery": "Récupération d'endurance bien plus lente",
    "endurance barely recovers": "L'endurance ne récupère presque plus",
    "endurance drains as you move and never recovers": "L'endurance baisse quand vous bougez et ne remonte jamais",
    "no sprinting or running": "Ni sprint ni course",
    "you cannot run": "Vous ne pouvez pas courir",
    "you cannot sleep": "Vous ne pouvez pas dormir",
    "you cannot eat any more": "Vous ne pouvez plus manger",
    "you can sleep on the ground and through pain": "Vous pouvez dormir au sol et malgré la douleur",
    "cannot swing a sledgehammer": "Plus de masse",
    "hunger does not rise": "La faim ne monte pas",
    "less body heat generated": "Moins de chaleur corporelle produite",
    "body heat rises": "La température corporelle monte",
    "body heat rises sharply": "La température corporelle monte fortement",
    "thirst and fatigue rise faster": "Soif et fatigue montent plus vite",
    "you lose heat in the cold": "Vous perdez de la chaleur par temps froid",
    "more likely to catch a cold": "Plus de risques d'attraper froid",
    "more likely to fall ill": "Plus de risques de tomber malade",
    "much more likely to fall ill": "Bien plus de risques de tomber malade",
    "narrower vision cone": "Cône de vision réduit",
    "narrower vision and awareness": "Vision et perception réduites",
    "movement, damage and attack speed drop with the wound": "Déplacement, dégâts et vitesse d'attaque baissent selon la blessure",
    "you make noise": "Vous faites du bruit",
    "you complain out loud": "Vous vous plaignez à voix haute",
    "you get up faster": "Vous vous relevez plus vite",
    "you weave as you walk": "Vous titubez en marchant",
    "timed actions take longer": "Les actions prennent plus de temps",
    "unhappiness rises": "Le malheur augmente",
    "unhappiness rises slowly": "Le malheur augmente lentement",
    "unhappiness rises fast": "Le malheur augmente vite",
    "stress rises": "Le stress augmente",
    "boredom is wiped and held down": "L'ennui est effacé et bloqué",
    "the Desensitized trait cancels it": "Le trait Insensible l'annule",
    "no effect until NPCs return": "Sans effet tant qu'il n'y a pas de PNJ",
    "discomfort while in a vehicle": "Inconfort en véhicule",
    "hypothermia is hidden": "L'hypothermie est masquée",
    "it wakes you up": "Cela vous réveille",
    "you sneeze now and then": "Vous éternuez de temps en temps",
    "you sneeze and cough often": "Vous éternuez et toussez souvent",
    "you cough so much that hiding gets hard": "Vous toussez tant qu'il devient dur de se cacher",
    "you cough constantly and draw zombies": "Vous toussez sans arrêt et attirez les zombies",
    "health loss": "Perte de santé",
    "slow health loss": "Perte de santé lente",
    "serious health loss": "Perte de santé importante",
    "health slowly drops": "La santé baisse lentement",
    "health drops if this is infection or poison": "La santé baisse si c'est une infection ou un poison",
    "death without first aid": "Mort sans premiers soins",
    "sickness starts to build": "La maladie commence à monter",
    "sickness builds noticeably": "La maladie monte nettement",
    "many rotting corpses": "Beaucoup de cadavres en décomposition",
    "more rotting corpses": "Davantage de cadavres en décomposition",
    "the worst corpses can do": "Le pire que les cadavres puissent faire",
    "a generator running indoors": "Un générateur allumé à l'intérieur",
    "it will not kill you outright": "Cela ne vous tuera pas sur le coup",
    "a gas mask or SCBA prevents it": "Un masque à gaz ou un ARI l'évite",
    "caused by heavy clothing, bags, bare feet or leg injuries": "Dû aux vêtements lourds, aux sacs, aux pieds nus ou aux jambes blessées",

    # Animals (round 10, block C)
    "Animals: butchering yield, milk, wool and old age":
        "Animaux : rendement en viande, lait, laine et vieillesse",
    "Adds rows to the animal window you get by right-clicking an animal: meat yield, blood, feathers, old age and weight ceiling, which no screen shows, plus health, hunger, thirst, attitude, milk, wool and pregnancy as numbers instead of words.":
        "Ajoute des lignes à la fenêtre de l'animal ouverte par un clic droit : rendement en viande, sang, plumes, vieillesse et poids maximal, qu'aucun écran n'affiche, plus la santé, la faim, la soif, l'attitude, le lait, la laine et la gestation en chiffres au lieu de mots.",
    "Animals: keep vanilla's Animal Care level requirements":
        "Animaux : conserver les niveaux d'Élevage exigés par le jeu",
    "Off by default, so you see everything from level {}. Turn it on and each row reappears at the Animal Care level vanilla itself uses for it: pregnancy at {}, weight at {}, attitude at {}.":
        "Désactivé par défaut, vous voyez donc tout dès le niveau {}. Activez-le et chaque ligne réapparaît au niveau d'Élevage que le jeu utilise lui-même : gestation à {}, poids à {}, attitude à {}.",
    "Meat yield":
        "Rendement en viande",
    "full in %1":
        "plein dans %1",

    # Animal hover descriptions (round 12)
    "Size x meat gene.":
        "Taille x gène de viande.",
    "Multiplies the number of meat pieces and the calories of each one.":
        "Multiplie le nombre de morceaux de viande et les calories de chacun.",
    "Butchering adds x{} every {} levels.":
        "La boucherie ajoute x{} tous les {} niveaux.",
    "Off the ground x{}, on a butcher hook x{}.":
        "Au sol x{}, sur un crochet de boucher x{}.",
    "Litres you can drain into a bucket once it is dead.":
        "Litres que vous pouvez récupérer dans un seau après sa mort.",
    "Grows with weight.":
        "Augmente avec le poids.",
    "Feathers you get for butchering it.":
        "Plumes obtenues en le dépeçant.",
    "Breed maximum x size.":
        "Maximum de la race x taille.",
    "{}%% until {}%% of its life expectancy, then it climbs to {}%%.":
        "{}%% jusqu'à {}%% de son espérance de vie, puis grimpe jusqu'à {}%%.",
    "Over {}%% it loses {}%% health every hour.":
        "Au-delà de {}%%, il perd {}%% de santé par heure.",
    "Current weight and the most this animal can reach.":
        "Poids actuel et maximum que cet animal peut atteindre.",
    "Meat and blood both scale with it.":
        "La viande et le sang suivent cette valeur.",
    "Over {}%% hunger it starts losing weight.":
        "Au-delà de {}%% de faim, il commence à perdre du poids.",
    "{}{}, how much this animal puts up with you.":
        "{}{}, à quel point cet animal vous supporte.",
    "Each point takes {} off the chance it breaks free while being sheared.":
        "Chaque point retire {} au risque qu'il se dégage pendant la tonte.",
    "Every gain is {}, plus {} per Animal Care level.":
        "Chaque gain vaut {}, plus {} par niveau d'Élevage.",
    "Healthy over {}%%, off colour over {}%%, sickly over {}%%, dying below.":
        "En bonne santé au-delà de {}%%, patraque au-delà de {}%%, souffrant au-delà de {}%%, mourant en dessous.",
    "Higher is worse.":
        "Plus c'est haut, plus c'est mauvais.",
    "Well fed under {}%%, underfed under {}%%, starving over it.":
        "Bien nourri sous {}%%, sous-alimenté sous {}%%, affamé au-delà.",
    "Over {}%% it starts losing weight.":
        "Au-delà de {}%%, il commence à perdre du poids.",
    "Fully watered under {}%%, thirsty under {}%%, dying of thirst over it.":
        "Bien hydraté sous {}%%, assoiffé sous {}%%, mourant de soif au-delà.",
    "{}{}. Calm under {}, unnerved under {}, agitated under {}, wild over it.":
        "{}{}. Calme sous {}, nerveux sous {}, agité sous {}, sauvage au-delà.",
    "Over {} milk and wool grow at {} / stress of their rate.":
        "Au-delà de {}, le lait et la laine poussent à {} / stress de leur rythme.",
    "Over {} a pregnancy can be lost.":
        "Au-delà de {}, une gestation peut être perdue.",
    "Milking with stress over {} and Animal Care {} or less always fails and spills the bucket.":
        "Traire avec un stress supérieur à {} et un Élevage de {} ou moins échoue toujours et renverse le seau.",
    "Litres in the udder and what it holds.":
        "Litres dans la mamelle et sa contenance.",
    "It fills by capacity / {} per game hour, times the sandbox milk modifier.":
        "Se remplit de contenance / {} par heure de jeu, multiplié par le modificateur de lait du bac à sable.",
    "Stress over {} slows it down.":
        "Un stress supérieur à {} ralentit tout ça.",
    "Wool grown and the maximum.":
        "Laine poussée et maximum.",
    "It grows by maximum / {} per game hour: {} days for a full fleece.":
        "Pousse de maximum / {} par heure de jeu : {} jours pour une toison complète.",
    "Days left before it gives birth.":
        "Jours restants avant la mise bas.",
    "Stress over {} can end the pregnancy.":
        "Un stress supérieur à {} peut mettre fin à la gestation.",
    "Hours this female stays fertilised.":
        "Heures pendant lesquelles cette femelle reste fécondée.",
    "When it runs out she is no longer fertilised.":
        "Quand elles s'épuisent, elle ne l'est plus.",

    # Wounds and healing
    "Wounds: how long each one still needs":
        "Blessures : le temps qu'il reste à chacune",
    "Adds an Info entry under the treatments you get by clicking a body part in the health panel. Hover it and the box beside it gives the time left on every wound, what bandaging or a poultice would save, how long the bandage lasts and whether the part is mending or getting worse. The game knows all of it and only prints it in debug mode.":
        "Ajoute une entrée Info sous les soins proposés en cliquant sur une partie du corps dans l'écran de santé. Au survol, l'encadré à côté donne le temps restant sur chaque blessure, ce qu'un bandage ou un cataplasme ferait gagner, combien de temps tient le bandage et si la partie guérit ou empire. Le jeu sait tout cela et ne l'affiche qu'en mode débogage.",
    "Wounds: keep vanilla's Doctor level requirements":
        "Blessures : conserver les niveaux de Premiers secours exigés par le jeu",
    "Off by default, so you see everything from level {}. Turn it on and each row reappears at the Doctor level vanilla itself uses for it: scratches and lacerations at {}, deep wounds and splints at {}, fractures and stitches at {}, wound infection at {}.":
        "Désactivé par défaut, vous voyez donc tout dès le niveau {}. Activez-le et chaque ligne réapparaît au niveau de Premiers secours que le jeu utilise lui-même : égratignures et lacérations à {}, plaies profondes et attelles à {}, fractures et points de suture à {}, infection de la plaie à {}.",
    "Full recovery":
        "Guérison complète",
    "Getting worse":
        "S'aggrave",
    "Healing":
        "Guérison",
    "normal":
        "normale",
    "slowed by hunger, thirst or illness":
        "ralentie par la faim, la soif ou la maladie",
    "stopped by hunger or thirst":
        "arrêtée par la faim ou la soif",
    "asleep, ten times faster":
        "pendant le sommeil, dix fois plus vite",
    "wounded parts share it":
        "parties blessées se la partagent",
    "Bandage life":
        "Durée du bandage",
    "ready to remove":
        "prêts à être retirés",

    # Wounds and healing, redesigned tooltip
    "Healing speed":
        "Vitesse de guérison",
    "clean for":
        "propre pendant",
    "Poultice":
        "Cataplasme",
    "Wound infection":
        "Infection de la plaie",
    "won't close, glass inside":
        "ne se referme pas, du verre à l'intérieur",
    "won't close while unbandaged":
        "ne se referme pas sans bandage",
    "rising":
        "en hausse",

    # Wounds: shorter recovery label and infection risk
    "Recovery":
        "Guérison",
    "Infection risk":
        "Risque d'infection",

    # Percentages, ported from the multiplier wording
    "{}%% weapon damage": "{}%% de dégâts de l'arme",
    "{}%% endurance recovery": "{}%% de récupération d'endurance",
    "{}%% melee damage and knockback": "{}%% de dégâts au corps à corps et de recul",
    "{}%% move speed in combat stance": "{}%% de vitesse en posture de combat",
    "{}%% sprint speed": "{}%% de vitesse de sprint",
    "{}%% chance of being spotted": "{}%% de chance d'être repéré",
    "{}%% footstep noise": "{}%% de bruit de pas",
    "{}%% recoil delay": "{}%% de délai de recul",
    "{}%% aim settling speed": "{}%% de vitesse de stabilisation de la visée",
    "{}%% aim penalty for moving (shared with Nimble)":
        "{}%% de malus de visée en mouvement (partagé avec Agilité)",
    "{}%% reload speed": "{}%% de vitesse de rechargement",
    "{}%% racking speed": "{}%% de vitesse d'armement",
    "{}%% XP in every Crafting skill": "{}%% d'XP dans toutes les compétences d'Artisanat",
    "{}%% move speed through trees": "{}%% de vitesse entre les arbres",
    "spotting another player {}%%": "{}%% pour repérer un autre joueur",
    "timed actions {}%%": "actions {}%% plus longues",
    "endurance drain {}%%": "{}%% de perte d'endurance",
    "alcohol hits {}%%, and {}%% over {}%% hunger":
        "L'alcool frappe {0}%%, et {1}%% au-delà de {2}%% de faim",
    "Fitness {}, which is {}%% endurance recovery instead of {}%%":
        "Condition physique {}, soit {}%% de récupération d'endurance au lieu de {}%%",
    "{}%% attack speed": "{}%% de vitesse d'attaque",
    "{}%% crit chance": "{}%% de chance de critique",
    "racking costs {}%% of the aiming time": "armer coûte {}%% du temps de visée",
    "carrying capacity {}": "capacité de charge {}",
    "{} to every weapon's durability roll.": "{} au jet de durabilité de toute arme.",
    "Condition loss (handle)": "Perte d'état (manche)",
    "Condition loss (head)": "Perte d'état (tête)",

    # Ronda 4: medicine, traps, weapon components, skill levels
    '%1 corpses nearby': '%1 cadavres à proximité',
    '%1%% attack time': "%1%% de vitesse d'attaque",
    '%1%% crit chance': '%1%% de chance de coup critique',
    '%1%% muscle strain': '%1%% de fatigue musculaire',
    '%1%% weapon damage': "%1%% de dégâts de l'arme",
    '+%1 to the durability roll': '+%1 au jet de durabilité',
    'Adds an Info entry to a placed trap: the odds of it catching anything in an hour, which animals it can take and the share of the catch each one gets, the bait and its freshness, the zone, the hourly odds of losing bait or trap, and the warning that a trap catches nothing while you stand next to it. Bait foods get a row naming what they attract.': "Ajoute une entrée Info à un piège posé : la chance qu'il prenne quoi que ce soit en une heure, quels animaux il peut prendre et la part de la prise qui revient à chacun, l'appât et sa fraîcheur, la zone, les chances horaires de perdre l'appât ou le piège, et l'avertissement qu'un piège ne prend rien tant que tu restes à côté. Les aliments servant d'appât gagnent une ligne indiquant ce qu'ils attirent.",
    'Bait': 'Appât',
    'Bait lost per hour': 'Appât perdu par heure',
    'In the trap for': 'Dans le piège depuis',
    'Filter left': 'Filtre restant',
    'Hits before it breaks': 'Coups avant de casser',
    'Medicine: duration, delay and effect': 'Médicaments : durée, délai et effet',
    'Medicine: the full list of effects': 'Médicaments : la liste complète des effets',
    'Muscle strain per hit': 'Fatigue musculaire par coup',
    'Off by default, so you see everything from level {}. Turn it on and the trap tooltip only appears from Trapping {}, which is the level vanilla itself uses elsewhere.': "Désactivé par défaut, tu vois donc tout dès le niveau {}. Une fois activé, l'infobulle du piège n'apparaît qu'à partir de Piégeage {}, le niveau que le jeu utilise lui-même ailleurs.",
    'Off by default. Adds everything else each pill does: what cancels it, what intoxication costs it, and the sleeping tablet overdose table.': "Désactivé par défaut. Ajoute tout le reste de ce que fait chaque cachet : ce qui l'annule, ce que l'ivresse lui coûte et la table de surdose des somnifères.",
    'Painkillers, beta blockers, antidepressants, sleeping tablets and antibiotics get how long they last, how long they take to start and what they do per minute. Every figure is recomputed from the sandbox day length.': "Les antidouleurs, bêtabloquants, antidépresseurs, somnifères et antibiotiques indiquent combien de temps ils durent, combien de temps ils mettent à agir et ce qu'ils font par minute. Chaque chiffre est recalculé à partir de la durée du jour de la sandbox.",
    'Prey': 'Proies',
    'Rots once thawed': 'Pourrit une fois décongelé',
    'Stale once thawed': 'Rassis une fois décongelé',
    'Takes effect in': 'Fait effet dans',
    'Trap lost per hour': 'Piège perdu par heure',
    'Traps: catch odds, bait and hours': 'Pièges : chances de capture, appât et horaires',
    "Traps: keep vanilla's Trapping level requirements": 'Pièges : conserver les niveaux de Piégeage exigés par le jeu',
    'Zone': 'Zone',
    'a second dose resets the clock, it does not add': "une deuxième dose remet le compteur à zéro, elle ne s'ajoute pas",
    'a third of the strength above {} intoxication': "un tiers de la force au-delà de {} d'ivresse",
    'fresh for %1': 'frais pendant %1',
    'half the strength above {} intoxication': "la moitié de la force au-delà de {} d'ivresse",
    "each pill counts double above {} intoxication": "chaque cachet compte double au-delà de {} d'ivresse",
    'holds the fever, does not cure it': 'retient la fièvre, ne la soigne pas',
    'incoming panic {}%% per pill, down to nothing': "panique reçue {}%% par cachet, jusqu'à zéro",
    'it catches nothing while you are near it': 'il ne prend rien tant que tu es à côté',
    'only the first dose has to wait': 'seule la première dose doit attendre',
    'overdose: {} pills cost {} health, {} cost {}, {} kill': 'surdose : {} cachets coûtent {} de santé, {} en coûtent {}, {} tuent',
    'sleeping cancels the effect': "dormir annule l'effet",
    'stale, catches nothing': "rassis, n'attire rien",
    'the longer it waits, the likelier it comes out dead': 'plus il attend, plus il risque de sortir mort',
    'to full in %1': 'au maximum dans %1',
    'to zero in %1': 'à zéro dans %1',
    'wound pain stops being recalculated while it lasts': "la douleur des blessures cesse d'être recalculée tant qu'il agit",
    'zombie fever held': 'fièvre zombie retenue',
    '{}%% reading time': '{}%% de temps de lecture',
    'Effect': 'Effet',

    # Ronda 4, segunda pasada
    '%1 s': '%1 s',
    '%1 s per round': '%1 s par balle',
    '%1%% attack speed': "%1%% de vitesse d'attaque",
    'Details': 'Détails',
    'Info': 'Info',
    'Possible prey': 'Proies possibles',
    'Trap breaks per hour': 'Piège cassé par heure',
    'holds the fever': 'retient la fièvre',
    'not being used (%1 corpses nearby)': "ne s'use pas (%1 cadavres à proximité)",
    'Bird': 'Oiseau',
    'Active hours': "Heures d'activité",
    'Possible prey, share of the catch': 'Proies possibles, part de la prise',
    'Catch chance': 'Chance de capture',
    'Bait condition': "État de l'appât",
    'Trap condition': 'État du piège',
    'while you are near it, it neither catches nor breaks': 'tant que tu es à côté, il ne prend rien et ne casse pas',
    'Bait loss risk, per hour': "Risque de perdre l'appât, par heure",
    'Wrecked by an animal, per hour': 'Détruit par un animal, par heure',
    '%1 / h': '%1 / h',
    'Bait loss risk': "Risque de perdre l'appât",
    'Chance of being wrecked': "Risque d'être détruit",
    'Critical damage': 'Dégâts critiques',
    'Effective durability': 'Durabilité effective',
    'Damage with your character': 'Dégâts avec ton personnage',
    'Reach (tiles)': 'Portée (cases)',

    # Bags and the torch beam (0.9.20)
    'All round': 'Tout autour',
    'Beam (degrees)': 'Faisceau (degrés)',
    'Bags: how much they slow you down': 'Sacs : de combien ils vous ralentissent',
    "The run and combat speed a bag costs you, which the game applies and never shows. The run figure is the one you are paying right now: a bag's penalty grows by half again as it fills up, so the same pack goes from {}%% empty to {}%% full. It counts the same in your hands as on your back.": "La vitesse de course et de combat qu'un sac vous coûte, que le jeu applique sans jamais l'afficher. Le chiffre de course est celui que vous payez en ce moment : la pénalité augmente de moitié à mesure que le sac se remplit, donc le même sac passe de {}%% à vide à {}%% plein. Il compte pareil dans les mains que sur le dos.",

    # Trait figures corrected against bytecode (0.9.21)
    "Aiming and Maintenance are not affected":
        "Visée et Entretien ne sont pas affectés",
    "ambient light never drops below {} in the dark":
        "la lumière ambiante ne descend jamais sous {} dans le noir",
    "can tell a poisonous wild plant from a safe one":
        "distingue une plante sauvage vénéneuse d'une plante sûre",
    "lights a fire with a notched plank twice as fast":
        "allume un feu à la planche entaillée deux fois plus vite",
    "no harm at all from tainted water":
        "l'eau souillée ne fait aucun dégât",
    "{} health on every construction":
        "{} points de vie sur chaque construction",
    "{} tiles of perception instead of {}":
        "{} cases de perception au lieu de {}",
    "{}%% XP in the six melee weapon skills":
        "{}%% d'XP dans les six compétences d'arme de mêlée",
    "{}%% chance of tearing your clothes on a tree":
        "{}%% de chances de déchirer vos vêtements sur un arbre",
    "{}%% from any other poison":
        "{}%% de tout autre poison",
    "{}%% from any other poison, bleach aside":
        "{}%% de tout autre poison, sauf l'eau de Javel",
    "{}%% weather penalty in combat":
        "{}%% de pénalité météo en combat",

    # Per-level lines for the twenty craft skills (0.9.21)
    "%1 crop health at planting":
        "%1 de santé de la culture à la plantation",
    "%1%% chance the crop is cursed if planted out of its month":
        "%1%% de chances que la culture soit maudite si plantée hors de son mois",
    "%1%% chance of a bonus harvest planted in its best month":
        "%1%% de chances de récolte bonus si plantée dans son meilleur mois",
    "%1 disease removed per treatment":
        "%1 de maladie retirée par traitement",
    "%1%% chance of harvesting %2 extra vegetables":
        "%1%% de chances de récolter %2 légumes de plus",
    "%1%% back strain planting and harvesting":
        "%1%% de tension dans le dos en plantant et en récoltant",
    "%1 points off the chance a stressed animal breaks off milking or shearing":
        "%1 points sur les chances qu'un animal stressé se débatte à la traite ou à la tonte",
    "a stressed animal never breaks off milking or shearing":
        "un animal stressé ne se débat plus à la traite ni à la tonte",
    "x%1 chance of each extra part off a carcass":
        "x%1 de chances pour chaque pièce supplémentaire d'une carcasse",
    "x%1 of each part":
        "x%1 de chaque pièce",
    "up to %1 blood splatters on you":
        "jusqu'à %1 éclaboussures de sang sur vous",
    "%1 health on everything you build":
        "%1 points de vie sur tout ce que vous construisez",
    "%1%% build time":
        "%1%% de temps de construction",
    "%1%% barricading time":
        "%1%% de temps pour barricader",
    "%1%% chance of recovering material when dismantling":
        "%1%% de chances de récupérer du matériau en démontant",
    "%1%% of the ingredient used per addition":
        "%1%% de l'ingrédient consommé par ajout",
    "x%1 nutrients from each ingredient":
        "x%1 de nutriments par ingrédient",
    "rotten food can go in evolved recipes, worth %1%% of its hunger":
        "vous pouvez mettre un peu de nourriture pourrie dans les recettes évolutives",
    "x%1 fracture healing with a splint":
        "x%1 de guérison des fractures avec une attelle",
    "a bandage lasts %1 to %2 longer":
        "un bandage tient de %1 à %2 fois plus longtemps",
    "%1%% time for every medical action":
        "%1%% de temps pour chaque acte médical",
    "you can judge how bad a wound is":
        "vous savez juger la gravité d'une blessure",
    "you can read pain, and spot the burns that need washing":
        "vous lisez la douleur et repérez les brûlures à laver",
    "you can tell when stitches are ready to come out":
        "vous savez quand les points de suture peuvent être retirés",
    "you spot a wound infection straight away":
        "vous repérez tout de suite une infection de plaie",
    "%1%% chance of getting the patch back":
        "%1%% de chances de récupérer la pièce",
    "%1%% time to add or remove a patch":
        "%1%% de temps pour poser ou retirer une pièce",
    "a hole can be repaired completely, defense and insulation included":
        "un trou se répare entièrement, défense et isolation comprises",
    "+%1%% generator condition per repair":
        "+%1%% d'état du générateur par réparation",
    "%1 points to the chance of hotwiring a car":
        "%1 points sur les chances de démarrer une voiture sans clé",
    "%1%% chance of setting off the car alarm":
        "%1%% de chances de déclencher l'alarme de la voiture",
    "you can salvage and repair a standard engine":
        "vous pouvez récupérer et réparer un moteur standard",
    "you can salvage and repair a heavy-duty engine":
        "vous pouvez récupérer et réparer un moteur lourd",
    "you can salvage and repair a sport engine":
        "vous pouvez récupérer et réparer un moteur sport",
    "you can build the sturdier brick wall":
        "vous pouvez bâtir le mur de briques le plus solide",
    "small %1%%, medium %2%%, large %3%%":
        "petit %1%%, moyen %2%%, gros %3%%",
    "%1 points to the chance a berry or mushroom is poisonous":
        "%1 points sur les chances qu'une baie ou un champignon soit vénéneux",
    "%1%% time to inspect a track":
        "%1%% de temps pour inspecter une trace",
    "no effect of its own, this level only unlocks the recipes below":
        "aucun effet propre, ce niveau ne débloque que les recettes ci-dessous",

    # 0.9.21 follow-up
    "%1 rags when you rip up clothing, capped by the parts it covers":
        "%1 morceaux en déchirant des vêtements, plafonné par ce qu'ils couvrent",
    "rotten food can go in evolved recipes, worth %1%% of its hunger":
        "la nourriture pourrie passe dans les recettes évolutives, elle vaut %1%% de sa satiété",

    # 0.9.21 follow-up 2
    "%1%% time per litre shearing an animal":
        "%1%% de temps par litre en tondant un animal",
    "%1 rags when you rip up clothing, capped by the parts it covers":
        "%1 chiffons en déchirant des vêtements, plafonné par les parties couvertes",
    "%1 to the most aramid thread you can pull out":
        "%1 au maximum de fil d'aramide que vous pouvez tirer",
    "starts at {} weight, becomes Emaciated at {} or less and Low Weight above {}":
        "commence à {} de poids, à {} ou moins devient Émacié et au-dessus de {} devient Maigre",
    "starts at {} weight, becomes High Weight below {}":
        "commence à {} de poids, en dessous de {} devient Surpoids",
    "starts at {} weight, becomes Very High Weight at {} and is lost below {}":
        "commence à {} de poids, à {} devient Obèse et se perd en dessous de {}",
    "starts at {} weight, becomes Very Low Weight at {} or less and is lost above {}":
        "commence à {} de poids, à {} ou moins devient Très maigre et se perd au-dessus de {}",
    "XP awarded":
        "XP accordée",
    "{} chance to trip when a zombie lunges through a window":
        "{} de chance de trébucher quand un zombie se jette par une fenêtre",
    "{} to the roll that keeps you on your feet when a zombie shoves you":
        "{} au jet qui vous garde debout quand un zombie vous bouscule",
    "{}%% muscle strain":
        "{}%% de fatigue musculaire",
    "{}%% axe attack speed, chopping trees included":
        "{}%% de vitesse d'attaque à la hache, abattage des arbres compris",

    # B42.20 trait corrections
    "Another x{} at panic level {}":
        "encore x{} au niveau de panique {}",
    "Can hotwire without Electrical {} and Mechanics {}":
        "peut démarrer sans clé sans Électricité {} ni Mécanique {}",
    "Engine revs three times faster in reverse":
        "le moteur monte trois fois plus vite en marche arrière",
    "Halves your rope climbing bonus":
        "réduit de moitié votre bonus d'escalade à la corde",
    "No unhappiness from looting corpses":
        "fouiller les cadavres ne rend pas malheureux",
    "Stress from handling bloody items":
        "du stress en manipulant des objets ensanglantés",
    "{} move speed at panic level {}, {} at level {}":
        "{} de vitesse au niveau de panique {}, {} au niveau {}",
    "{} to the rope climbing roll":
        "{} au jet d'escalade à la corde",
    "{}%% acceleration, fading out above {}%% of the car's top speed":
        "{}%% d'accélération, qui s'estompe au-dessus de {}%% de la vitesse de pointe de la voiture",
    "{}%% carry capacity":
        "{}%% de capacité de charge",
    "{}%% chance of breaking a window lock instead of {}%%":
        "{}%% de casser le loquet d'une fenêtre au lieu de {}%%",
    "{}%% endurance cost on every exertion":
        "{}%% d'endurance par effort",
    "{}%% reverse acceleration, gone past {} km/h":
        "{}%% d'accélération en marche arrière, nulle au-delà de {} km/h",
    "{}%% unhappiness from looting corpses":
        "{}%% de tristesse en fouillant les cadavres",

    # Repair recipes
    "Repair: +%1 condition, %2 chance of failing":
        "Réparation : +%1 d'état, %2 d'échec",
    "Repair: +%1 condition, %2 chance of failing, repaired %3 times":
        "Réparation : +%1 d'état, %2 d'échec, réparé %3 fois",

    # Corpse count and temperature figures
    "Body temperature: the number on every bar":
        "Température corporelle : le chiffre sur chaque barre",
    "Nauseous: how many corpses are making you ill":
        "Nausée : combien de cadavres vous rendent malade",
    "Rotting corpses nearby raise food sickness, and the game never says how many are close enough. Five or fewer do nothing. The count is read back out of the game, so it follows the sandbox setting.":
        "Les cadavres en décomposition à proximité augmentent l'intoxication alimentaire, et le jeu ne dit jamais combien sont assez près. Cinq ou moins ne font rien. Le compte est relu depuis le jeu, il suit donc le réglage bac à sable.",
    "The temperature view prints its value on Insulation and Wind resistance and leaves the other nine bars as a colour. This sets the same flag on the rest, so skin temperature, body response, heat and wetness read as figures. Vanilla does the drawing, and only for the body part you have selected.":
        "La vue de température écrit sa valeur sur Isolation et Résistance au vent et laisse les neuf autres barres en couleur. Ceci pose le même indicateur sur les autres, donc température de la peau, réponse du corps, chaleur et humidité se lisent en chiffres. C'est le jeu qui dessine, et seulement pour la partie du corps sélectionnée.",

    # Options tab
    "Custom":
        "Personnalisé",
    "Nothing matches that":
        "Aucune correspondance",
    "Moodles: how many corpses are making you ill":
        "Moodles : combien de cadavres vous rendent malade",

    # Option groups
    "Every gun this box or magazine fits, one per row.":
        "Chaque arme dans laquelle cette boîte ou ce chargeur va, une par ligne.",
    "How bloody the garment is, out of a hundred.":
        "À quel point le vêtement est ensanglanté, sur cent.",
    "How brightly it lights what it reaches.":
        "Avec quelle intensité la lumière éclaire ce qu'elle atteint.",
    "How dirty the garment is, out of a hundred.":
        "À quel point le vêtement est sale, sur cent.",
    "How drunk this container will get you.":
        "À quel point ce récipient va vous saouler.",
    "How far the light reaches, in tiles.":
        "Jusqu'où porte la lumière, en cases.",
    "How far the shot is heard, which is how far the horde comes from.":
        "Jusqu'où le tir s'entend, c'est-à-dire d'où vient la horde.",
    "How long before the pill starts working, and only while you have none running.":
        "Combien de temps avant que le cachet fasse effet, et seulement tant qu'aucun n'agit.",
    "How long cooked food can stay on the heat before it burns.":
        "Combien de temps un plat cuit tient sur le feu avant de brûler.",
    "How long the charge lasts with the thing switched on.":
        "Combien de temps la charge dure appareil allumé.",
    "How long the filter lasts at your current exposure, and how many corpses are around you.":
        "Combien de temps le filtre tient à votre exposition actuelle, et combien de cadavres vous entourent.",
    "How long the item burns for as fuel.":
        "Combien de temps l'objet brûle comme combustible.",
    "How long the pages you have not read yet will take.":
        "Combien de temps prendront les pages que vous n'avez pas encore lues.",
    "How long the pill keeps working.":
        "Combien de temps le cachet continue d'agir.",
    "How long the plant takes to be ready, at the current farming speed.":
        "Combien de temps la plante met à être prête, à la vitesse de culture actuelle.",
    "How long until the food goes stale, at the current rot speed.":
        "Combien de temps avant que la nourriture soit rassie, à la vitesse de pourriture actuelle.",
    "How long until the food is rotten, at the current rot speed.":
        "Combien de temps avant que la nourriture soit pourrie, à la vitesse de pourriture actuelle.",
    "How many hits the weapon has left in it, which is the one figure that compares any two weapons.":
        "Combien de coups il reste à l'arme, le seul chiffre qui compare deux armes quelconques.",
    "How much cold the garment keeps out. The game only draws a bar.":
        "Combien de froid le vêtement arrête. Le jeu ne dessine qu'une barre.",
    "How much is left in the filter.":
        "Combien il reste dans le filtre.",
    "How much of it you have already heard.":
        "Quelle part vous en avez déjà écoutée.",
    "How much of the corpse sickness the mask keeps off you. {}%% is immunity.":
        "Quelle part de la maladie des cadavres le masque vous épargne. {}%% est une immunité.",
    "How much of your hunger bar the drink covers.":
        "Quelle part de votre barre de faim la boisson couvre.",
    "How much of your thirst bar the drink covers.":
        "Quelle part de votre barre de soif la boisson couvre.",
    "How much pull the rod takes before the line gives.":
        "Quelle traction la canne encaisse avant que le fil cède.",
    "How much rain the garment keeps out. The game only draws a bar.":
        "Combien de pluie le vêtement arrête. Le jeu ne dessine qu'une barre.",
    "How much the bag slows you down, with its weight and what is inside counted.":
        "À quel point le sac vous ralentit, son poids et son contenu comptés.",
    "How much the bag slows your swing.":
        "À quel point le sac ralentit votre coup.",
    "How much the garment slows you down, as the penalty itself rather than a bar.":
        "À quel point le vêtement vous ralentit, sous forme du malus lui-même plutôt que d'une barre.",
    "How much the garment slows your swing, as the penalty itself rather than a bar.":
        "À quel point le vêtement ralentit votre coup, sous forme du malus lui-même plutôt que d'une barre.",
    "How much tiredness this surface actually clears, your traits included.":
        "Quelle fatigue cette surface enlève vraiment, vos traits compris.",
    "How much wind the garment keeps out. The game only draws a bar.":
        "Combien de vent le vêtement arrête. Le jeu ne dessine qu'une barre.",
    "How often a hit crits, with your level in the weapon's own skill counted.":
        "À quelle fréquence un coup est critique, votre niveau dans la compétence de l'arme compté.",
    "How often a shot crits.":
        "À quelle fréquence un tir est critique.",
    "How wet the garment is, out of a hundred.":
        "À quel point le vêtement est mouillé, sur cent.",
    "In tiles. A swing landed at the edge of your reach does up to twice the damage of one landed close in.":
        "En cases. Un coup porté au bord de votre allonge fait jusqu'au double des dégâts d'un coup porté au corps à corps.",
    "Off by default: the game only reveals this block for packaged food or a Nutritionist.":
        "Désactivé par défaut : le jeu ne montre ce bloc que pour les aliments emballés ou avec Nutritionniste.",
    "Rounds in the magazine right now, out of what it holds.":
        "Balles dans le chargeur en ce moment, sur ce qu'il contient.",
    "The calibre the magazine takes.":
        "Le calibre que prend le chargeur.",
    "The calories in what is actually in the container, mixtures included.":
        "Les calories de ce qu'il y a vraiment dans le récipient, mélanges compris.",
    "The carbohydrates in what is actually in the container.":
        "Les glucides de ce qu'il y a vraiment dans le récipient.",
    "The charge left, as a number instead of a bar.":
        "La charge restante, en chiffre plutôt qu'en barre.",
    "The edge, and the ceiling a worn head puts on it: blunt, the weapon loses the top of its damage range.":
        "Le tranchant, et le plafond qu'une tête usée lui impose : émoussée, l'arme perd le haut de ses dégâts.",
    "The exact minimum and maximum. The game only ever draws it as a bar.":
        "Le minimum et le maximum exacts. Le jeu ne le dessine que comme une barre.",
    "The exact points left, and the head's own count on a weapon that has one.":
        "Les points exacts restants, et le compte propre de la tête sur une arme qui en a une.",
    "The exact points left, where the game only draws a bar.":
        "Les points exacts restants, là où le jeu ne dessine qu'une barre.",
    "The fat in what is actually in the container.":
        "Les lipides de ce qu'il y a vraiment dans le récipient.",
    "The fatigue each swing costs you.":
        "La fatigue que chaque coup vous coûte.",
    "The furthest tile the gun can hit.":
        "La case la plus lointaine que l'arme peut toucher.",
    "The gun's own hit chance, before your aiming skill.":
        "La chance de toucher propre à l'arme, avant votre visée.",
    "The hook fitted, and what it does to your odds of a bite.":
        "L'hameçon monté, et ce qu'il fait à vos chances de touche.",
    "The line fitted, and how much of it each tug wears away.":
        "Le fil monté, et combien chaque traction en use.",
    "The months it can be sown in, one per row.":
        "Les mois où l'on peut semer, un par ligne.",
    "The multiplier your shoes put on stomping a downed zombie. Footwear only.":
        "Le multiplicateur que vos chaussures donnent au piétinement d'un zombie à terre. Chaussures uniquement.",
    "The multiplier your skill puts on this weapon's swing.":
        "Le multiplicateur que votre compétence donne au coup de cette arme.",
    "The net pace of the pill, which is what compares two of them at a glance.":
        "Le rythme net du cachet, ce qui compare deux d'entre eux d'un coup d'œil.",
    "The odds of losing a point of condition on a hit, with Maintenance and the weapon's skill counted.":
        "La chance de perdre un point d'état sur un coup, Entretien et compétence de l'arme comptés.",
    "The odds of losing a point of condition per shot.":
        "La chance de perdre un point d'état par tir.",
    "The poison the drink carries, and only while the game is willing to tell you.":
        "La vraie chance d'enrayage, usure et prise faible comprises.",
    "The proteins in what is actually in the container.":
        "Les protéines de ce qu'il y a vraiment dans le récipient.",
    "The real odds of a jam, wear and a weak grip included.":
        "Le poison que porte la boisson, et seulement tant que le jeu veut bien vous le dire.",
    "The real seconds a reload takes, with your reloading skill and your panic counted.":
        "Les secondes réelles que prend un rechargement, votre compétence de rechargement et la panique comptées.",
    "The real seconds spent lining up the shot, with your aiming skill and your traits counted.":
        "Les secondes réelles passées à aligner le tir, votre visée et vos traits comptés.",
    "The recipes it teaches that you do not know yet, one per row.":
        "Les recettes qu'il enseigne et que vous ne connaissez pas encore, une par ligne.",
    "The swing animation, which is what really separates a slow weapon from a fast one.":
        "L'animation du coup, ce qui sépare vraiment une arme lente d'une arme rapide.",
    "What a critical is worth, from {}%% to {}%% depending on the weapon. The game shows it nowhere.":
        "Ce que vaut un critique, de {}%% à {}%% selon l'arme. Le jeu ne le montre nulle part.",
    "What feeds the Uncomfortable moodle. The game never shows it on the garment at all.":
        "Ce qui alimente le moodle d'inconfort. Le jeu ne le montre jamais sur le vêtement.",
    "What is left in your hands when the rod breaks.":
        "Ce qu'il vous reste dans les mains quand la canne casse.",
    "What sleeping here costs you in comfort.":
        "Ce que dormir ici vous coûte en confort.",
    "What the drink does to boredom and unhappiness, which move together here.":
        "Ce que la boisson fait à l'ennui et au mal-être, qui vont ensemble ici.",
    "What the drink does to your fatigue bar.":
        "Ce que la boisson fait à votre barre de fatigue.",
    "What the drink does to your stress.":
        "Ce que la boisson fait à votre stress.",
    "What the food still needs, and the temperature the figure assumes.":
        "Ce qu'il manque encore à la nourriture, et la température que le chiffre suppose.",
    "Whether it is a cone you aim or a lamp that lights all around, and how wide the cone is.":
        "S'il s'agit d'un cône que vous dirigez ou d'une lampe qui éclaire tout autour, et l'ouverture du cône.",
    "Which fish this bait brings in.":
        "Quels poissons cet appât attire.",
    "Which skill the tape or disc trains and how much experience is left in it.":
        "Quelle compétence la cassette ou le disque entraîne et combien d'expérience il lui reste.",
    "Which skill the weapon trains, and therefore which one drives its damage and its speed.":
        "Quelle compétence l'arme entraîne, et donc laquelle pilote ses dégâts et sa vitesse.",
    "Your own reading speed, traits, glasses and sitting down included.":
        "Votre propre vitesse de lecture, traits, lunettes et position assise compris.",
    "Nutrition":
        "Nutrition",
    "Sleep":
        "Sommeil",
    "How much the bag slows your attack. It multiplies the weapon's own swing speed, not your walking.":
        "À quel point le sac ralentit votre attaque. Il multiplie la vitesse de frappe de l'arme elle-même, pas votre marche.",
    "How much the garment slows your attack. It multiplies the weapon's own swing speed, not your walking.":
        "À quel point le vêtement ralentit votre attaque. Il multiplie la vitesse de frappe de l'arme elle-même, pas votre marche.",
    "Best baits":
        "Meilleurs appâts",
    "Every animal this trap can catch and its share of the catch.":
        "Chaque animal que ce piège peut prendre et sa part dans les prises.",
    "Feathers":
        "Plumes",
    "Fog on a line of its own, because the game lumps it into weather and then reports neither.":
        "Le brouillard sur sa propre ligne, parce que le jeu le range dans la météo et ne rapporte ensuite ni l'un ni l'autre.",
    "Glass or a bullet still in the wound, which stops it healing until it is out.":
        "Du verre ou une balle encore dans la plaie, qui l'empêche de cicatriser tant qu'ils y sont.",
    "How far the disease has gone, out of a hundred.":
        "Jusqu'où la maladie est allée, sur cent.",
    "How far the generator is heard, halved when it stands indoors.":
        "Jusqu'où le générateur s'entend, moitié moins à l'intérieur.",
    "How full the udder is and whether it can be milked yet.":
        "À quel point le pis est plein et si la traite est déjà possible.",
    "How hungry the animal is, and how long its feed will last.":
        "La faim de l'animal, et combien de temps sa ration va durer.",
    "How long before old age starts costing the animal its yield.":
        "Combien de temps avant que la vieillesse commence à lui coûter son rendement.",
    "How long each cut, scratch, burn or bite still needs.":
        "Combien de temps il faut encore à chaque coupure, égratignure, brûlure ou morsure.",
    "How long is left of a pregnancy, or of an egg being fertilised.":
        "Ce qu'il reste d'une gestation, ou avant qu'un œuf soit fécondé.",
    "How long since the last watering. The game works it out to pick a colour and then never shows it.":
        "Depuis combien de temps le dernier arrosage. Le jeu le calcule pour choisir une couleur et ne le montre jamais.",
    "How long the bandage lasts before it is dirty and worth changing.":
        "Combien de temps le bandage tient avant d'être sale et de mériter un changement.",
    "How long the catch has been waiting in there.":
        "Depuis combien de temps la prise attend là-dedans.",
    "How long the fracture needs, and what the splint on it is worth.":
        "Combien de temps il faut à la fracture, et ce que vaut l'attelle qui est dessus.",
    "How long the fuel in the tank lasts at the current draw.":
        "Combien de temps le carburant du réservoir dure à la consommation actuelle.",
    "How long the part needs to be whole again, and how fast it is healing.":
        "Combien de temps il faut à la partie pour être entière, et à quelle vitesse elle guérit.",
    "How long the stiffness in that limb takes to pass.":
        "Combien de temps la raideur de ce membre met à passer.",
    "How long the stitches need, and when they can come out.":
        "Combien de temps il faut aux points de suture, et quand ils peuvent être retirés.",
    "How long until it breaks down for good, on average.":
        "Combien de temps avant qu'il ne casse pour de bon, en moyenne.",
    "How long until it wears down to the point where it can catch fire.":
        "Combien de temps avant qu'il ne s'use au point de pouvoir prendre feu.",
    "How long until the crop moves to its next stage.":
        "Combien de temps avant que la culture passe à son stade suivant.",
    "How long you will wait compared with the best possible spot.":
        "Combien vous allez attendre par rapport au meilleur endroit possible.",
    "How many feathers butchering will give.":
        "Combien de plumes la découpe va donner.",
    "How many fish this spot still holds, and what that is worth.":
        "Combien de poissons cet endroit contient encore, et ce que cela vaut.",
    "How much blood butchering will give.":
        "Combien de sang la découpe va donner.",
    "How much fertiliser the plot holds. Above one is the too much case in the game's own code.":
        "Combien d'engrais la parcelle contient. Au-dessus de un, c'est le cas de trop dans le code du jeu lui-même.",
    "How much meat butchering will give, which is what answers whether it is worth killing yet.":
        "Combien de viande la découpe va donner, ce qui répond à la question de savoir s'il vaut déjà la peine de l'abattre.",
    "How much of the bait is still good.":
        "Quelle part de l'appât est encore bonne.",
    "How much the animal trusts you, which is what lets you handle it.":
        "À quel point l'animal vous fait confiance, ce qui est ce qui permet de le manipuler.",
    "How much wool has grown back and whether it can be sheared yet.":
        "Combien de laine a repoussé et si la tonte est déjà possible.",
    "How stressed the animal is, out of a hundred.":
        "À quel point l'animal est stressé, sur cent.",
    "How the wound infection is going, and whether it is still rising.":
        "Où en est l'infection de la plaie, et si elle monte encore.",
    "How thirsty the animal is, and how long its water will last.":
        "La soif de l'animal, et combien de temps son eau va durer.",
    "Level needed":
        "Niveau requis",
    "Lodged objects":
        "Objets fichés",
    "Odds with your bait":
        "Chances avec votre appât",
    "Predator":
        "Prédateur",
    "Size and weight":
        "Taille et poids",
    "Strength at the top skill level":
        "Solidité au niveau maximum",
    "The Fishing level this species needs before it will bite.":
        "Le niveau de Pêche que cette espèce exige avant de mordre.",
    "The animal's health as a number.":
        "La santé de l'animal en chiffre.",
    "The animal's weight, and how far it still has to grow.":
        "Le poids de l'animal, et ce qu'il lui reste à grandir.",
    "The chance of this exact species with the bait you are using.":
        "La chance d'avoir exactement cette espèce avec l'appât que vous utilisez.",
    "The crop's health out of a hundred. The game only prints it with debug on.":
        "La santé de la culture sur cent. Le jeu ne l'écrit qu'avec le débogage activé.",
    "The fuel still in the tank. The game knows the number and only prints it as a debug option.":
        "Le carburant encore dans la cuve. Le jeu connaît le chiffre et ne l'affiche qu'en option de débogage.",
    "The health the wall or door will have when you build it at your current level.":
        "La solidité qu'aura le mur ou la porte si vous le construisez à votre niveau actuel.",
    "The hourly odds of a bang loud enough to pull zombies in.":
        "Les chances par heure d'une détonation assez forte pour attirer les zombies.",
    "The hourly odds of a fire or an explosion, which set the generator to zero outright.":
        "Les chances par heure d'un incendie ou d'une explosion, qui mettent le générateur à zéro d'un coup.",
    "The hourly odds of the bait being taken without a catch.":
        "Les chances par heure que l'appât soit emporté sans prise.",
    "The hourly odds of the trap being wrecked.":
        "Les chances par heure que le piège soit détruit.",
    "The hourly odds of the wound becoming infected.":
        "Les chances par heure que la plaie s'infecte.",
    "The hours of the day the trap actually works.":
        "Les heures de la journée où le piège fonctionne vraiment.",
    "The kind of ground the trap is standing on, which decides what can come.":
        "Le type de terrain sur lequel le piège est posé, qui décide de ce qui peut venir.",
    "The odds of a bite once every factor is put together.":
        "Les chances de touche une fois tous les facteurs mis ensemble.",
    "The odds of catching anything at all in an hour.":
        "Les chances d'attraper quoi que ce soit en une heure.",
    "The range of lengths and weights this species comes in.":
        "L'éventail de longueurs et de poids dans lequel cette espèce se présente.",
    "The share of your catches that will be junk here.":
        "La part de vos prises qui sera des déchets ici.",
    "The two things the game never says: a long wait kills the catch, and standing nearby stops the trap.":
        "Les deux choses que le jeu ne dit jamais : une longue attente tue la prise, et rester à côté arrête le piège.",
    "The water level as a number, and the amount this seed actually needs.":
        "Le niveau d'eau en chiffre, et la quantité dont cette graine a réellement besoin.",
    "Time to the danger threshold":
        "Temps jusqu'au seuil de danger",
    "Trophy size":
        "Taille trophée",
    "Warnings":
        "Avertissements",
    "Warns that the species only bites while you reel in.":
        "Prévient que l'espèce ne mord que pendant que vous ramenez la ligne.",
    "What a catch has to beat to count as a trophy.":
        "Ce qu'une prise doit dépasser pour compter comme trophée.",
    "What the herbs in the bandage are adding.":
        "Ce que les herbes du bandage apportent.",
    "What the same build would have at level {}, which is the reason to know the figure before building.":
        "Ce que la même construction aurait au niveau {}, ce qui est la raison de connaître le chiffre avant de bâtir.",
    "What the time of day is worth, as the multiplier behind the game's own rating.":
        "Ce que vaut l'heure de la journée, sous forme du multiplicateur derrière la note du jeu.",
    "What the water temperature is worth, with the actual reading in degrees.":
        "Ce que vaut la température de l'eau, avec le relevé réel en degrés.",
    "What the weather is worth, as the multiplier behind the game's own rating.":
        "Ce que vaut la météo, sous forme du multiplicateur derrière la note du jeu.",
    "What the wind is worth. Past half strength it costs the same penalty fog does, and the two never stack.":
        "Ce que vaut le vent. Au-delà de la moitié de sa force, il coûte le même malus que le brouillard, et les deux ne se cumulent jamais.",
    "Whether the mains or a generator is keeping the pump running.":
        "Si c'est le réseau ou un générateur qui fait tourner la pompe.",
    "Which animals a bait item brings in.":
        "Quels animaux un objet servant d'appât attire.",
    "Which bait is in the trap, and whether it is still fresh.":
        "Quel appât se trouve dans le piège, et s'il est encore frais.",
    "Which baits work best on this species.":
        "Quels appâts marchent le mieux sur cette espèce.",
    "Which growth stage the crop is on, out of the total.":
        "À quel stade de croissance la culture se trouve, sur le total.",
    "Which hook is fitted and what it does to your odds.":
        "Quel hameçon est monté et ce qu'il fait à vos chances.",
    "Raw eggs never make you ill":
        "Les œufs crus ne vous rendent jamais malade",
    "{}%% wait before another anti-nausea food works":
        "{}%% d'attente avant qu'un autre aliment anti-nausée agisse",
    "{}%% weapon sight range":
        "{}%% de portée des viseurs",
    "At Axe {} you swing as fast as a maxed axe user":
        "Avec Hache à {} vous frappez aussi vite qu'un expert",
    "{}%% from any poisonous food or drink":
        "{}%% de tout aliment ou boisson empoisonné",
    "{}%% chance of illness from rotten food":
        "{}%% de risque de tomber malade avec de la nourriture pourrie",
    "Melee weapons":
        "Armes de mêlée",
    "Firearms":
        "Armes à feu",
    "Drinks":
        "Boissons",
    "Skill XP":
        "XP de compétence",
    "Weapons":
        "Armes",
    "Worn and carried":
        "Vêtements et contenants",
    "Medicine and reading":
        "Médicaments et lecture",
    "Supplies":
        "Fournitures",
    "Comparison":
        "Comparaison",
    "Power and fuel":
        "Électricité et carburant",
    "Animals and traps":
        "Animaux et pièges",
    "Traits and jobs":
        "Traits et métiers",
    "Moodles":
        "Moodles",
}
