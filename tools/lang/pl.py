"""Polish phrase table for AllInfo.

Keys are the English fragment with every number replaced by {} in order.
Numbers are never written here: they ride through untouched. Use {0} {1} ...
instead of {} when the language needs a different order -- and then index every
slot, Python refuses to mix the two forms.

Run `python tools\\i18n.py` after editing: it checks the arity of every line and
refuses to write a language file it cannot fill completely.
"""

T = {
    # Per-level skill descriptions
    "x{} weapon damage (x{} untrained)": "x{} obrażeń broni (x{} bez wprawy)",
    "{} to the durability roll": "{} do rzutu na wytrzymałość",
    "{} chance to trip vaulting a fence": "{} szansy na potknięcie przy przeskakiwaniu płotu",
    "{}%% fall damage": "{}%% obrażeń od upadku",
    "x{} endurance recovery (x{} untrained)": "x{} regeneracji wytrzymałości (x{} bez wprawy)",
    "x{} melee damage and knockback (x{} untrained)": "x{} obrażeń w zwarciu i odrzutu (x{} bez wprawy)",
    "x{} carrying capacity (x{} untrained)": "x{} udźwigu (x{} bez wprawy)",
    "x{} move speed in combat stance (x{} untrained)": "x{} prędkości w postawie bojowej (x{} bez wprawy)",
    "x{} sprint speed (x{} untrained)": "x{} prędkości sprintu (x{} bez wprawy)",
    "x{} chance of being spotted (x{} untrained)": "x{} szansy na zauważenie cię (x{} bez wprawy)",
    "x{} footstep noise (x{} untrained)": "x{} hałasu kroków (x{} bez wprawy)",
    "{} accuracy (the weapon's aiming modifier, {} on nearly every gun)":
        "{} celności (modyfikator celowania broni, {} przy niemal każdej)",
    "{} wind penalty when aiming (of {})": "{} kary za wiatr przy celowaniu (z {})",
    "x{} reload speed (x{} untrained)": "x{} szybkości przeładowania (x{} bez wprawy)",
    "x{} racking speed (x{} untrained)": "x{} szybkości repetowania (x{} bez wprawy)",
    "racking costs {} of the aiming time ({} untrained)": "repetowanie kosztuje {} czasu celowania ({} bez wprawy)",
    "From here on you no longer count as unsteady with a firearm, as long as your Strength is {} or more: jam chance drops by {} percentage points.":
        "Od tego poziomu nie liczysz się już jako niepewny z bronią palną, o ile twoja Siła wynosi {} lub więcej: szansa na zacięcie spada o {} punkty procentowe.",
    "You never count as unsteady with a firearm again, whatever your Strength.":
        "Już nigdy nie liczysz się jako niepewny z bronią palną, niezależnie od Siły.",

    # Moodles
    "{} melee to-hit": "{} celności w zwarciu",
    "{} climb chance": "{} szansy na wspinaczkę",
    "{} trip chance": "{} szansy na potknięcie",
    "{} to break a zombie's grab": "{} do wyrwania się z uchwytu zombie",
    "{}%% strength": "{}%% siły",
    "{}%% healing": "{}%% leczenia",
    "losing health": "tracisz zdrowie",
    "harder to unjam a gun": "trudniej odblokować zacięcie",
    "{} move speed (of {})": "{} prędkości ruchu (z {})",
    "body at {} C": "temperatura ciała {} C",
    "{} carry capacity": "{} udźwigu",
    "x{} attack speed": "x{} szybkości ataku",
    "endurance under {}%%": "wytrzymałość poniżej {}%%",
    "fatigue over {}%%": "zmęczenie powyżej {}%%",
    "hunger over {}%%": "głód powyżej {}%%",
    "thirst over {}%%": "pragnienie powyżej {}%%",
    "panic over {}%%": "panika powyżej {}%%",
    "stress over {}%%": "stres powyżej {}%%",
    "boredom over {}%%": "nuda powyżej {}%%",
    "unhappiness over {}%%": "przygnębienie powyżej {}%%",
    "{}%% action speed": "{}%% szybkości czynności",
    "anger over {}%%": "złość powyżej {}%%",
    "drunkenness over {}%%": "upojenie powyżej {}%%",
    "pain over {}%%": "ból powyżej {}%%",
    "slower rope climbing": "wolniejsza wspinaczka po linie",
    "{}%% total body damage": "{}%% łącznych obrażeń ciała",
    "sickness over {}%%": "choroba powyżej {}%%",
    "cold strength over {}%%": "siła przeziębienia powyżej {}%%",
    "wetness over {}%%": "przemoczenie powyżej {}%%",
    "discomfort over {}%%": "dyskomfort powyżej {}%%",
    "rotting corpses nearby": "gnijące zwłoki w pobliżu",
    "x{} move speed": "x{} prędkości ruchu",
    "{} discomfort per level": "{} dyskomfortu na poziom",
    "{} C on top of the air temperature": "{} C ponad temperaturę powietrza",
    "carrying {}x capacity": "obciążenie {}x udźwigu",
    "{}%% body heat": "{}%% ciepła ciała",
    "no sleep without pills": "nie zaśniesz bez tabletek",
    "erratic movement": "chwiejny chód",
    "raises discomfort": "podnosi dyskomfort",
    "no sprinting": "bez sprintu",
    "no sprinting, no exercise": "bez sprintu i bez ćwiczeń",
    "zombies spot you {} sooner": "zombie zauważają cię o {} wcześniej",
    "muscle stiffness builds up": "narasta sztywność mięśni",
    "cannot eat or open food": "nie możesz jeść ani otwierać jedzenia",
    "{} move speed with Adrenaline Junkie": "{} prędkości z cechą Adrenaline Junkie",
    "nightmares while asleep": "koszmary podczas snu",
    "no sleep below {}%% fatigue without pills": "bez tabletek nie zaśniesz przy zmęczeniu poniżej {}%%",
    "{}%% move speed": "{}%% prędkości ruchu",
    "cannot move": "nie możesz się ruszyć",
    "{} climbing walls and ropes": "{} do wspinaczki po murach i linach",
    "no running, no exercise": "bez biegania i bez ćwiczeń",
    "over {}x capacity": "powyżej {}x udźwigu",
    "no running": "bez biegania",
    "no sprinting until you drop the bulky item": "bez sprintu, dopóki nie odłożysz nieporęcznego przedmiotu",
    "you can sleep through high pain": "zaśniesz nawet przy silnym bólu",
    "no endurance recovery": "wytrzymałość się nie regeneruje",
    "{} vision cone": "{} stożka widzenia",
    "delayed vehicle controls": "opóźnione sterowanie pojazdem",
    "narrowed vision cone": "zwężony stożek widzenia",
    "no exercise": "bez ćwiczeń",
    "{} wound bleeding": "krwawiące rany: {}",
    "Rest in peace.": "Spoczywaj w pokoju.",
    "Infected. There is no cure.": "Zakażenie. Nie ma lekarstwa.",

    # Tooltip labels
    "Stale in": "Zwietrzeje za",
    "Rots in": "Zgnije za",
    "Cooking time": "Czas gotowania",
    "Never": "Nigdy",
    "Critical chance": "Szansa na krytyk",
    "Trains": "Trenuje",
    "Attack speed": "Szybkość ataku",
    "Swing type": "Rodzaj zamachu",
    "Heavy": "Ciężki",
    "Swung": "Zamaszysty",
    "Stabbing": "Kłujący",
    "Spear": "Włócznia",
    "Stone": "Kamienny",
    "Knockback on hit": "Odrzut przy trafieniu",
    "Condition loss": "Utrata stanu",
    "Jam chance": "Szansa na zacięcie",
    "Accuracy": "Celność",
    "Noise radius": "Promień hałasu",
    "Rounds": "Naboje",
    "Reload time": "Czas przeładowania",
    "Aiming time": "Czas celowania",
    "Used by": "Pasuje do",
    "Reading speed": "Szybkość czytania",
    "Reading time left": "Pozostało czytania",
    "Skill too low to learn from it": "Umiejętność za niska, by się z tego uczyć",
    "Nothing left to learn from it": "Nie ma się już z tego czego uczyć",
    "Proteins": "Białko",
    "Sow in": "Siej w",
    "Ready in": "Gotowe za",
    "Burn time": "Czas palenia",
    # Power: charge, autonomy and light
    "Duration": "Czas działania",
    "Light range": "Zasięg światła",
    "Light strength": "Siła światła",
    "Batteries and radios: charge left, how long it lasts and how far a torch lights": "Baterie i radia: pozostały ładunek, czas działania i zasięg światła latarki",
    "Vanilla draws the charge of a drainable as a bar with no number on it, and never says how long a torch lasts or how far it lights. A torch spends its UseDelta once every ten game minutes, and only while it is in a hand or attached to you: left in a bag it switches itself off. Light range and strength are the figures that actually light the ground.":
        "Gra rysuje ładunek przedmiotu zużywalnego jako pasek bez liczby i nigdy nie mówi, jak długo starczy latarka ani jak daleko świeci. Latarka zużywa swoje UseDelta raz na dziesięć minut gry i tylko wtedy, gdy trzymasz ją w ręce lub masz przypiętą: w plecaku wyłącza się sama. Zasięg i siła światła to liczby, które naprawdę oświetlają ziemię.",
    "Rest quality": "Jakość odpoczynku",
    "Discomfort": "Dyskomfort",
    "Stomp damage": "Obrażenia od deptania",
    "Corpse sickness defense": "Ochrona przed chorobą trupią",
    "Filter charge": "Zapas filtra",
    "New recipes": "Nowe przepisy",
    "Listened": "Odsłuchano",
    "Skill too high for this tape": "Umiejętność za wysoka na tę kasetę",

    # Options screen
    "All Info": "All Info",
    "Enable everything": "Włącz wszystko",
    "Items": "Przedmioty",
    "Crafting": "Wytwarzanie",
    "World": "Świat",
    "Character": "Postać",
    "Everything in this section": "Wszystko w tej sekcji",
    "Food: time left before it spoils": "Jedzenie: ile zostało do zepsucia",
    "Adds hours to stale and hours to rotten, at the current rate. Accounts for the fridge, the freezer and the sandbox spoilage speed.":
        "Pokazuje, ile godzin zostało do zwietrzenia i do zgnicia w obecnym tempie. Uwzględnia lodówkę, zamrażarkę i szybkość psucia z ustawień piaskownicy.",
    "Cooking: add the warm-up minutes": "Gotowanie: doliczaj minuty nagrzewania",
    "Off by default. Cooking time is the time at temperature; this adds the four minutes the food spends heating up before it starts to cook, so an oven timer set to the figure rings when the food is done.":
        "Domyślnie wyłączone. Czas gotowania dotyczy jedzenia już nagrzanego; ta opcja dolicza cztery minuty, które jedzenie traci na nagrzanie, zanim zacznie się gotować, żeby minutnik piekarnika zadzwonił dokładnie wtedy, gdy będzie gotowe.",
    "Food: calories, carbs, protein and fat": "Jedzenie: kalorie, węglowodany, białko i tłuszcz",
    "Off by default. Showing macros on every food undoes the Nutritionist trait, which is what normally reveals them.":
        "Domyślnie wyłączone. Pokazywanie makroskładników przy każdym jedzeniu unieważnia cechę Dietetyk, która normalnie je odsłania.",
    "Melee: exact damage, speed and durability": "Zwarcie: dokładne obrażenia, szybkość i wytrzymałość",
    "Puts numbers on the condition and damage bars, and adds crit chance, swing type, attack speed, knockback and the odds of losing a condition point per hit.":
        "Nanosi liczby na paski stanu i obrażeń oraz dodaje szansę na krytyk, rodzaj zamachu, szybkość ataku, odrzut i szansę na utratę punktu stanu przy ciosie.",
    "Firearms: range, jam chance and reload": "Broń palna: zasięg, zacięcia i przeładowanie",
    "Puts numbers on the condition and damage bars, and adds accuracy, effective range, jam odds and magazine size.":
        "Nanosi liczby na paski stanu i obrażeń oraz dodaje celność, zasięg skuteczny, szansę na zacięcie i pojemność magazynka.",
    "Ammo: rounds left and what it fits": "Amunicja: ile zostało i do czego pasuje",
    "No comparison arrows here: the thing in your hands is a gun, not another magazine, so there is no honest pair to compare.":
        "Tu nie ma strzałek porównania: w rękach trzymasz broń, a nie drugi magazynek, więc nie ma uczciwej pary do zestawienia.",
    "Clothing: numbers on every bar, plus discomfort": "Ubrania: liczby na wszystkich paskach oraz dyskomfort",
    "Vanilla draws condition, insulation, wind, water, blood, dirt and wetness as bars with no figures. This writes the figures next to them and adds the discomfort value, which vanilla never shows at all.":
        "Gra rysuje stan, izolację, wiatr, wodę, krew, brud i przemoczenie jako paski bez liczb. Tutaj liczby są wypisane obok, a do tego dyskomfort, którego gra nie pokazuje nigdzie.",
    "Seeds: growing time and yield": "Nasiona: czas wzrostu i plon",
    "Firewood: how long it burns": "Drewno: jak długo się pali",
    "Books: reading time and skill levels covered": "Książki: czas czytania i objęte poziomy",
    "Reading time already accounts for Fast Reader, Slow Reader and reading glasses.":
        "Czas czytania uwzględnia już Szybkiego Czytelnika, Wolnego Czytelnika i okulary do czytania.",
    "Beds: how well you recover on them": "Łóżka: jak dobrze się na nich wypoczywa",
    "Masks: filter life and protection": "Maski: żywotność filtra i ochrona",
    "Tapes and CDs: which skill they teach and how much XP": "Kasety i płyty: jakiej umiejętności uczą i ile dają PD",
    "Show the difference against what you have equipped": "Pokaż różnicę względem tego, co masz założone",
    "Adds a coloured +/- next to weapon and clothing values. Weapons compare against what is in your hands, clothing against the piece worn in the same slot.":
        "Dodaje kolorowe +/- obok wartości broni i ubrań. Broń porównuje się z tym, co trzymasz, a ubranie z częścią noszoną w tym samym miejscu.",
    "Crafting: full item tooltip on the recipe output": "Wytwarzanie: pełna informacja o przedmiocie przy wyniku przepisu",
    "Hovering the result of a recipe shows the same block an item in your inventory would, comparison included, before you craft it.":
        "Najechanie na wynik przepisu pokazuje ten sam blok, co przedmiot w plecaku, wraz z porównaniem, jeszcze przed wytworzeniem.",
    "Generators: fuel time, wear and danger": "Generatory: paliwo, zużycie i zagrożenie",
    "Adds noise radius, hours of fuel left, average time until {}%% condition and until it breaks, and the hourly odds of a backfire or a fire.":
        "Dodaje promień hałasu, godziny pozostałego paliwa, średni czas do {}%% stanu i do awarii oraz godzinną szansę na strzał gaźnika lub pożar.",
    "Generators: also show times in real-world minutes": "Generatory: pokazuj czasy także w minutach rzeczywistych",
    "Off by default. Converts the in-game hours using the current day length, so you know how long you actually have to wait.":
        "Domyślnie wyłączone. Przelicza godziny gry według obecnej długości doby, żebyś wiedział, ile naprawdę czekasz.",
    "Generators: outline the powered area on the floor": "Generatory: obrysuj na podłodze zasilany obszar",
    "Draws the edge of the range while the generator window is open, green when running and red when off. Only the floor you are standing on is computed.":
        "Rysuje krawędź zasięgu, dopóki okno generatora jest otwarte: zielona, gdy pracuje, czerwona, gdy stoi. Liczone jest tylko piętro, na którym stoisz.",
    "Gas pumps: fuel left and power source": "Dystrybutory: pozostałe paliwo i źródło zasilania",
    "Adds an Info entry to the right-click menu of any gas pump, with the fuel still in the tank and whether the mains or a generator is keeping it running. The game knows that number and only prints it as a debug option.":
        "Dodaje wpis Info do menu prawego przycisku myszy na dystrybutorze: ile paliwa zostało w zbiorniku i czy trzyma go przy życiu sieć, czy generator. Gra zna tę liczbę i pokazuje ją tylko jako opcję debugowania.",
    "Fuel Remaining": "Pozostałe paliwo",
    "Mains power": "Sieć elektryczna",
    "Generator": "Generator",
    "Walls and doors: health under the cursor": "Ściany i drzwi: wytrzymałość pod kursorem",
    "Shows current and maximum health as a number at the foot of whatever you point at, no clicking needed.":
        "Pokazuje obecną i maksymalną wytrzymałość jako liczbę u podstawy tego, na co celujesz, bez klikania.",
    "Build menu: health of what you are about to build": "Menu budowy: wytrzymałość tego, co zamierzasz zbudować",
    "Also shows what that health would be with the relevant skill at {}, so you can tell whether it is worth waiting.":
        "Pokazuje też, ile wyniosłaby ta wytrzymałość przy odpowiedniej umiejętności na {}, żebyś wiedział, czy warto poczekać.",
    "Crops: health, growth and water as numbers": "Uprawy: zdrowie, wzrost i woda w liczbach",
    "Adds rows to the crop window you get by right-clicking a plant: health out of {}, current phase, hours to the next one, water level against what the plant needs, time since the last watering and pest levels.":
        "Dodaje wiersze do okna otwieranego prawym przyciskiem na roślinie: zdrowie z {}, obecna faza, godziny do następnej, poziom wody wobec potrzeb rośliny, czas od ostatniego podlania i poziom każdego szkodnika.",
    "Crops: keep vanilla's Farming level requirements": "Uprawy: zachowaj wymagania poziomu Rolnictwa z gry",
    "Off by default, so you see everything from level {}. Turn it on and each row reappears at the Farming level vanilla itself uses for it: phase and health at {}, water at {}, pests at {}, next phase at {}.":
        "Domyślnie wyłączone, więc widzisz wszystko od poziomu {}. Po włączeniu każdy wiersz wraca na ten poziom Rolnictwa, którego używa sama gra: faza i zdrowie na {}, woda na {}, szkodniki na {}, następna faza na {}.",
    "Noise": "Hałas",
    "tiles": "kratek",
    "Down to %1%% (avg)": "Do %1%% (śr.)",
    "Breaks down in (avg)": "Zepsuje się za (śr.)",
    "Backfire, loud (per hour)": "Strzał gaźnika, głośny (na godzinę)",
    "FIRE OR EXPLOSION (per hour)": "POŻAR LUB WYBUCH (na godzinę)",
    "(real time)": "(czas rzeczywisty)",
    "XP Boost: %1": "Premia PD: %1",
    "Skills": "Umiejętności",
    "Also grants": "Daje także",
    "Disabled in multiplayer": "Wyłączone w trybie wieloosobowym",
    "Foraging": "Zbieractwo",
    "search radius": "promień szukania",
    "weather penalty": "kara za pogodę",
    "darkness penalty": "kara za ciemność",
    "Strength when built": "Wytrzymałość po zbudowaniu",
    "With %1 at {}": "Z %1 na {}",
    "Show XP boosts as a multiplier, not a percentage": "Pokazuj premie PD jako mnożnik, a nie procent",
    'Vanilla says "{}%%" for a level {} boost. The real figure is x{}, because a skill with no boost runs at a quarter rate. Fixed on all three screens that show it.':
        'Gra pisze "{}%%" przy premii poziomu {}. Naprawdę jest to x{}, bo umiejętność bez premii idzie na jednej czwartej tempa. Poprawione na wszystkich trzech ekranach.',
    "Character creation: what each trait and job really does": "Tworzenie postaci: co naprawdę robi każda cecha i profesja",
    "Adds starting skill levels with their true XP multiplier, free traits granted, recipes taught and foraging bonuses to the tooltips in the creation screen.":
        "Dodaje do podpowiedzi na ekranie tworzenia początkowe poziomy umiejętności z prawdziwym mnożnikiem PD, darmowe cechy, nauczane przepisy i premie do zbieractwa.",
    "In game: the same block on the info tab": "W grze: ten sam blok na karcie informacji",
    "Hover a trait icon or the job icon in the character info tab to read the same block after the world has started.":
        "Najedź na ikonę cechy lub profesji na karcie informacji postaci, żeby przeczytać ten sam blok już w grze.",
    "Add hand-written trait effects": "Dodaj ręcznie spisane efekty cech",
    "Effects hardcoded in the game's Java that cannot be read at runtime, so they are written by hand and checked against each build.":
        "Efekty zaszyte w Javie gry, których nie da się odczytać w trakcie działania, więc są spisane ręcznie i sprawdzone przy każdej wersji.",
    "Skills: which recipes each level requires": "Umiejętności: jakie przepisy wymagają danego poziomu",
    "Hover a level in the skills panel to see the recipes and builds that ask for it. Read from the game's own recipe list, so modded recipes appear too and nothing goes stale with a patch.":
        "Najedź na poziom w panelu umiejętności, żeby zobaczyć przepisy i budowle, które go wymagają. Odczytane z listy przepisów samej gry, więc pojawiają się też przepisy z innych modów i nic się nie dezaktualizuje po łatce.",
    "Needs this level": "Wymagają tego poziomu",
    "Skill and moodle descriptions are translation files. They cannot be switched off here; disable the mod to remove them.":
        "Opisy umiejętności i wskaźników nastroju to pliki tłumaczeń. Nie da się ich tu wyłączyć; żeby je usunąć, wyłącz moda.",
    "Run self-test": "Uruchom autotest",

    # Trait and profession effects
    "{}%% footstep noise radius": "{}%% promienia hałasu kroków",
    "more likely to fall when bumped": "łatwiej przewracasz się przy zderzeniu",
    "less likely to fall when bumped": "trudniej przewracasz się przy zderzeniu",
    "{}%% run and sprint speed": "{}%% prędkości biegu i sprintu",
    "no Fitness XP from level {} on": "od poziomu {} brak PD Kondycji",
    "double endurance drain when running": "dwa razy większy ubytek wytrzymałości przy bieganiu",
    "{}%% melee damage": "{}%% obrażeń w zwarciu",
    "{} chance to trip from a lunge": "{} szansy na potknięcie przy wypadzie",
    "starts at {} weight, and you lose health below {}": "zaczyna z wagą {}, a poniżej {} tracisz zdrowie",
    "{}%% axe swing time": "{}%% czasu zamachu siekierą",
    "{}%% axe damage to trees": "{}%% obrażeń siekierą wobec drzew",
    "{}%% endurance lost running": "{}%% wytrzymałości traconej przy bieganiu",
    "{}%% grapple effectiveness": "{}%% skuteczności w zwarciu z chwytem",
    "{}%% knockback": "{}%% odrzutu",
    "can be gained by training Strength to {}": "zdobywa się, trenując Siłę do {}",
    "becomes Strong at Strength {}": "przy Sile {} zmienia się w Silny",
    "becomes Feeble at Strength {}": "przy Sile {} zmienia się w Wątły",
    "lost by training Strength to {}": "znika po wytrenowaniu Siły do {}",
    "{}%% panic, night terrors aside": "{}%% paniki, poza lękami nocnymi",
    "{}%% stress from looting corpses": "{}%% stresu przy przeszukiwaniu zwłok",
    "{}%% panic": "{}%% paniki",
    "no panic from a corpse reanimating": "brak paniki, gdy zwłoki się podnoszą",
    "no stress from looting corpses": "przeszukiwanie zwłok nie daje stresu",
    "{} move speed at panic {}": "{} prędkości przy panice {}",
    "still capped by the movement speed limit": "nadal ograniczone górnym limitem prędkości",
    "{}%% wind penalty when aiming": "{}%% kary za wiatr przy celowaniu",
    "{}%% gun accuracy": "{}%% celności broni palnej",
    "{}%% gun crit chance": "{}%% szansy na krytyk z broni palnej",
    "shorter aiming delay": "krótsze opóźnienie celowania",
    "wider field of view": "szersze pole widzenia",
    "{}%% max range on weapon sights": "{}%% maksymalnego zasięgu celowników",
    "blurry vision": "rozmyty obraz",
    "weapon sight range bonus at its minimum": "premia zasięgu celowników na minimum",
    "cancelled by wearing glasses": "znoszone przez noszenie okularów",
    "{}%% perception radius": "{}%% promienia percepcji",
    "zombies behind you become visible sooner": "zombie za tobą stają się widoczne wcześniej",
    "muffled sound effects": "przytłumione dźwięki",
    "zombies behind you become visible later": "zombie za tobą stają się widoczne później",
    "no sound at all": "żadnego dźwięku",
    "you can still watch TV": "telewizję i tak można oglądać",
    "{}%% chance of not being injured by a zombie": "{}%% szansy na uniknięcie rany od zombie",
    "{}%% chance of being scratched by trees": "{}%% szansy na zadrapanie od drzew",
    "{}%% corpse sickness": "{}%% choroby trupiej",
    "{}%% chance of catching a cold": "{}%% szansy na przeziębienie",
    "{}%% cold strength": "{}%% siły przeziębienia",
    "{}%% cold progression": "{}%% postępu przeziębienia",
    "{}%% zombification speed": "{}%% szybkości zombifikacji",
    "{}%% severity of vehicle injuries": "{}%% ciężkości obrażeń z pojazdu",
    "{}%% fracture severity": "{}%% ciężkości złamań",
    "all wounds heal much faster": "wszystkie rany goją się dużo szybciej",
    "all wounds heal much slower": "wszystkie rany goją się dużo wolniej",
    "{}%% XP in every skill except Fitness and Strength": "{}%% PD we wszystkich umiejętnościach poza Kondycją i Siłą",
    "{}%% reading speed": "{}%% szybkości czytania",
    "{}%% XP in every weapon skill and Aiming": "{}%% PD we wszystkich umiejętnościach broni i w Celowaniu",
    "{}%% inventory transfer time": "{}%% czasu przekładania przedmiotów",
    "{}%% aiming delay": "{}%% opóźnienia celowania",
    "guns jam less often": "broń rzadziej się zacina",
    "fewer injuries opening cans": "mniej skaleczeń przy otwieraniu puszek",
    "guns jam more often": "broń częściej się zacina",
    "more injuries opening cans": "więcej skaleczeń przy otwieraniu puszek",
    "{}%% container capacity": "{}%% pojemności pojemników",
    "crafting does not return leftover items": "wytwarzanie nie zwraca resztek",
    "{}%% thirst": "{}%% pragnienia",
    "{}%% hunger": "{}%% głodu",
    "{}%% food illness chance": "{}%% szansy na zatrucie pokarmowe",
    "{}%% food illness duration": "{}%% czasu trwania zatrucia pokarmowego",
    "{}%% harm from tainted water": "{}%% szkody od skażonej wody",
    "{}%% tiredness gained while awake": "{}%% zmęczenia zbieranego na jawie",
    "{}%% recovery while asleep": "{}%% regeneracji podczas snu",
    "{}%% sleep duration": "{}%% długości snu",
    "you do not wake up at {} tiredness, so set an alarm": "nie budzisz się przy zmęczeniu {}, więc nastaw budzik",
    "harder to fall asleep": "trudniej zasnąć",
    "{}%% vision in the dark": "{}%% widzenia w ciemności",
    "smaller vision cone penalty at night": "mniejsza kara do stożka widzenia w nocy",
    "{}%% chance of being spotted (new stealth)": "{}%% szansy na zauważenie cię (nowa skradanka)",
    "{}%% chance of being spotted (old stealth)": "{}%% szansy na zauważenie cię (stara skradanka)",
    "{}%% chance of breaking kindling": "{}%% szansy na złamanie podpałki",
    "{}%% weather penalty when aiming": "{}%% kary za pogodę przy celowaniu",
    "lights fires twice as fast": "rozpala ogień dwa razy szybciej",
    "almost never scratched by trees": "prawie nigdy nie drapią go drzewa",
    "{}%% endurance lost running, sprinting, carrying and dragging":
        "{}%% wytrzymałości traconej przy bieganiu, sprincie, noszeniu i ciągnięciu",
    "{}%% endurance lost swinging a weapon": "{}%% wytrzymałości traconej przy zamachu bronią",
    "{}%% gear change speed": "{}%% szybkości zmiany biegów",
    "{}%% top speed": "{}%% prędkości maksymalnej",
    "{}%% engine noise in reverse": "{}%% hałasu silnika na wstecznym",
    "{}%% acceleration": "{}%% przyspieszenia",
    "{}%% reverse acceleration": "{}%% przyspieszenia na wstecznym",
    "capped at {} max speed": "prędkość maksymalna ograniczona do {}",
    "engine noise unchanged": "hałas silnika bez zmian",
    "less likely to fail any fence climb": "rzadziej nie udaje się przejść przez płot",
    "slightly faster rope climbing": "nieco szybsza wspinaczka po linie",
    "bloody items transfer faster but cause stress": "zakrwawione przedmioty przekłada się szybciej, ale dają stres",
    "cannot read anything, map labels and calorie counts included":
        "nie potrafisz nic przeczytać, w tym opisów na mapie i kalorii",
    "{} panic per tick indoors, scaling down to {} in a {}-tile room":
        "{} paniki na tick w pomieszczeniu, spadając do {} w pokoju o {} kratkach",
    "a vehicle counts as a {}-tile room": "pojazd liczy się jako pokój o {} kratkach",
    "{} panic per tick whenever you are not in a room": "{} paniki na tick, dopóki nie jesteś w pomieszczeniu",
    "faster building": "szybsze budowanie",
    "faster barricading": "szybsze barykadowanie",
    "no bonus health on constructions in B{}": "w B{} nie daje budowlom dodatkowej wytrzymałości",
    "recipes need one level less of their skill": "przepisy wymagają o poziom niższej umiejętności",
    "you gain weight above {} calories a day instead of {}, while under {} weight":
        "tyjesz powyżej {} kalorii dziennie zamiast {}, dopóki waga jest poniżej {}",
    "you need {} calories a day to gain weight instead of {}, while over {} weight":
        "potrzebujesz {} kalorii dziennie, żeby przytyć, zamiast {}, dopóki waga jest powyżej {}",
    "unhappiness and stress rise as nicotine withdrawal builds":
        "przygnębienie i stres rosną wraz z głodem nikotynowym",
    "smoking clears the withdrawal and gives {} hunger": "palenie znosi głód nikotynowy i daje {} głodu",
    "random coughs and sneezes give you away": "przypadkowy kaszel i kichanie cię zdradzają",
    "shows calories, carbohydrates, protein and fat on every food":
        "pokazuje kalorie, węglowodany, białko i tłuszcz przy każdym jedzeniu",
    "no measurable effect in B{}: no XP boost, no recipes, and nothing in the game's code reads it. The recipes come from the profession itself.":
        "w B{} bez mierzalnego efektu: bez premii PD, bez przepisów i żadne miejsce w kodzie gry tego nie czyta. Przepisy daje sama profesja.",
    "x{} move speed through trees (x{} for everyone else)": "x{} prędkości między drzewami (x{} u wszystkich innych)",
    "starts every exercise at {}{} regularity instead of {}{}":
        "każde ćwiczenie zaczyna z regularnością {}{} zamiast {}{}",
    '{} move speed':
        '{} prędkości ruchu',
    '{} wind penalty when aiming':
        '{} kary za wiatr przy celowaniu',
    '%1 °C':
        '%1 °C',
    'Adds rows to the inventory tooltip: how fast a line wears out, how much each hook helps and which fish a bait attracts.':
        'Dodaje wiersze do podpowiedzi w ekwipunku: jak szybko zużywa się żyłka, ile daje każdy haczyk i jakie ryby wabi dana przynęta.',
    'ALLTHEINFO':
        'ALLTHEINFO',
    'Attracts':
        'Wabi',
    "Back to vanilla's rules: Time needs Fishing {}, Temperature {}, Weather {}, Wind {}, and a species tells you nothing until you have caught it.":
        'Powrót do zasad gry: godzina wymaga Wędkarstwa {}, temperatura {}, pogoda {}, wiatr {}, a gatunek nic nie mówi, dopóki go nie złowisz.',
    'Best baits: %1':
        'Najlepsze przynęty: %1',
    'Bite chance':
        'Szansa brania',
    'Breaks into':
        'Łamie się na',
    'Chance that one attempt hooks something: {}%% times temperature, weather, time, hook and abundance, capped at {}%%.':
        'Szansa, że jedna próba coś złapie: {}%% razy temperatura, pogoda, godzina, haczyk i liczebność ryb, maksymalnie {}%%.',
    'Fish bite more at dawn and dusk: x{} from {}:{} to {}:{} and from {}:{} to {}:{}. Any other hour is x{}.':
        'Ryby biorą lepiej o świcie i o zmierzchu: x{} od {}:{} do {}:{} i od {}:{} do {}:{}. Każda inna godzina to x{}.',
    'Fishing gear: rods, lines, hooks and baits':
        'Sprzęt wędkarski: wędki, żyłki, haczyki i przynęty',
    'Fishing panel: what each rating is worth':
        'Panel wędkarski: ile naprawdę znaczy każda ocena',
    "Fishing: keep vanilla's Fishing level requirements":
        'Wędkarstwo: zachowaj wymagania poziomu Wędkarstwa z gry',
    'Hook':
        'Haczyk',
    'How much longer than the best possible case you wait between attempts. Fishing near the shore doubles it, and a bobber less than {} tiles away triples it.':
        'O ile dłużej czekasz między próbami niż w najlepszym możliwym przypadku. Łowienie przy brzegu podwaja czekanie, a spławik bliżej niż {} pól potraja je.',
    'Lake':
        'Jezioro',
    'Line strength':
        'Wytrzymałość żyłki',
    'Moodles: description box that fits its text':
        'Nastroje: ramka opisu dopasowana do tekstu',
    'Needs Fishing %1':
        'Wymaga Wędkarstwa %1',
    'Only bites while you reel in':
        'Bierze tylko podczas zwijania żyłki',
    'Paperclip x{}, nail x{}, fishing hook x{}. With no hook the chance is x{}: nothing will ever bite.':
        'Spinacz x{}, gwóźdź x{}, haczyk wędkarski x{}. Bez haczyka szansa to x{}: nic nigdy nie weźmie.',
    'Rain is x{}. Fog over {} or wind over {} is x{}. Fog and wind are the same x{}: they never stack.':
        'Deszcz to x{}. Mgła powyżej {} lub wiatr powyżej {} to x{}. Mgła i wiatr to ten sam x{}: nigdy się nie sumują.',
    'Right-click water and pick Fishing. Puts the real multiplier next to Time, Temperature, Weather and Wind, adds hook, spot, bite chance and waiting time, and explains each one on hover.':
        'Kliknij wodę prawym przyciskiem i wybierz wędkowanie. Dopisuje prawdziwy mnożnik obok godziny, temperatury, pogody i wiatru, dodaje haczyk, miejscówkę, szansę brania i czas czekania, a po najechaniu wyjaśnia każde z nich.',
    'River':
        'Rzeka',
    'Spot':
        'Miejscówka',
    "The game's own moodle box is two lines tall and cuts off anything longer, which is most of AllTheInfo's descriptions. This draws the moodle column itself so the box grows with the text. Turn it off to go back to the vanilla widget.":
        'Ramka opisu nastroju w grze ma wysokość dwóch wierszy i ucina wszystko dłuższe, czyli niemal każdy opis AllTheInfo. Tutaj kolumnę nastrojów rysuje sam mod, więc ramka rośnie razem z tekstem. Wyłącz, aby wrócić do widgetu gry.',
    'Trophy from %1 cm, Fishing {} and a {} in {} roll on a big catch':
        'Trofeum od %1 cm, przy Wędkarstwie {} i rzucie {} na {} przy dużym połowie',
    'Under {} fish is x{}, up to {} is x{}, over {} is x{}. Trash is what you pull out instead of a fish, and Fishing {} cuts it to {}%%, level {} to {}%% and level {} to {}%%.':
        'Poniżej {} ryb to x{}, do {} to x{}, powyżej {} to x{}. Śmieci to, co wyciągasz zamiast ryby, a Wędkarstwo {} obniża je do {}%%, poziom {} do {}%%, a poziom {} do {}%%.',
    'Up to %1 cm and %2 kg':
        'Do %1 cm i %2 kg',
    'Vanilla draws condition, insulation, wind, water, blood, dirt and wetness as bars with no figures. This writes the figures next to them and adds the discomfort value, which vanilla never shows at all. The run and combat speed modifiers get a signed figure too, which vanilla only ever draws as a bar with no sign.':
        'Gra rysuje stan, izolację, wiatr, wodę, krew, brud i wilgoć jako paski bez liczb. Tutaj liczby stoją obok, plus wartość dyskomfortu, której gra nie pokazuje nigdzie. Modyfikatory prędkości biegu i walki też dostają liczbę ze znakiem, a gra rysuje je tylko jako pasek bez znaku.',
    'Wait':
        'Czekanie',
    'Waters: %1':
        'Wody: %1',
    'Wear per tug':
        'Zużycie na szarpnięcie',
    'Wind has no coefficient of its own. Over {} it sets the weather to x{}, the same penalty fog sets, and the two do not add up.':
        'Wiatr nie ma własnego współczynnika. Powyżej {} ustawia pogodę na x{}, ta sama kara co przy mgle, i oba się nie sumują.',
    'With your bait: %1%%':
        'Z twoją przynętą: %1%%',
    'Your bait does not attract this one':
        'Twoja przynęta nie wabi tego gatunku',
    'best possible':
        'najlepiej jak się da',
    'near shore':
        'przy brzegu',
    'no fish in this spot':
        'tutaj nie ma ryb',
    'none':
        'brak',
    'trash':
        'śmieci',
    '{} to {} °C is x{}. From {} to {} and from {} to {}, x{}. Over {} or below {}, x{}. Below {} °C, x{}.':
        'Od {} do {} °C to x{}. Od {} do {} i od {} do {}, x{}. Powyżej {} lub poniżej {}, x{}. Poniżej {} °C, x{}.',
    'Fish':
        'Ryby',
    'Trash':
        'Śmieci',
    'Trophy from %1 cm':
        'Trofeum od %1 cm',
    'shore':
        'brzeg',
    'Best baits:':
        'Najlepsze przynęty:',
    'Size: %1-%2 cm, %3-%4 kg':
        'Rozmiar: %1-%2 cm, %3-%4 kg',
    'Trophy: >%1 cm / >%2 kg':
        'Trofeum: >%1 cm / >%2 kg',
    'Under {} fish is x{}, up to {} is x{}, over {} is x{}. Fish schools move every day. Trash is what you pull out instead of a fish: it is fixed per spot, and Fishing {} cuts it to {}%%, level {} to {}%% and level {} to {}%%.':
        'Poniżej {} ryb to x{}, do {} to x{}, powyżej {} to x{}. Ławice ryb przemieszczają się codziennie. Śmieci to, co wyciągasz zamiast ryby: są stałe dla danego miejsca, a Wędkarstwo {} obniża je do {}%%, poziom {} do {}%%, a poziom {} do {}%%.',
    'Fishing gear: hide the combat stats':
        'Sprzęt wędkarski: ukryj statystyki bojowe',
    "Fog over {}%% sets the weather to x{}, the same penalty wind sets, and the two never stack. Vanilla's Weather row reports neither: it says Good for rain even in a gale.":
        'Mgła powyżej {}%% ustawia pogodę na x{}, ta sama kara co przy wietrze, i oba nigdy się nie sumują. Wiersz pogody w grze nie pokazuje żadnego z nich: przy deszczu pisze Dobrze nawet podczas wichury.',
    'Rain is x{}. Fog over {}%% or wind over {}%% is x{}. Fog and wind are the same x{}: they never stack.':
        'Deszcz to x{}. Mgła powyżej {}%% lub wiatr powyżej {}%% to x{}. Mgła i wiatr to ten sam x{}: nigdy się nie sumują.',
    "Rods, nets and fishing spears are weapons in the game's own scripts, so they get crit chance, swing type, attack speed and knockback. This drops that block on fishing gear. The condition and damage bars are drawn by the game in one call and cannot be removed by any mod.":
        'Wędki, sieci i oszczepy są w skryptach samej gry bronią, więc dostają szansę na trafienie krytyczne, typ zamachu, szybkość ataku i odrzut. To usuwa ten blok przy sprzęcie wędkarskim. Paski stanu i obrażeń gra rysuje jednym wywołaniem i żaden mod ich nie usunie.',
    'Wind has no coefficient of its own. Over {}%% it sets the weather to x{}, the same penalty fog sets, and the two do not add up.':
        'Wiatr nie ma własnego współczynnika. Powyżej {}%% ustawia pogodę na x{}, ta sama kara co przy mgle, i oba się nie sumują.',
    'Against the best possible case':
        'W porównaniu z najlepszym możliwym przypadkiem',
    'Any other hour: x{}':
        'Każda inna godzina: x{}',
    'Below {} °C: x{}':
        'Poniżej {} °C: x{}',
    'Bobber under {} tiles away: x{}':
        'Spławik bliżej niż {} pola: x{}',
    'Capped at {}%%':
        'Maksymalnie {}%%',
    'Fishing hook: x{}':
        'Haczyk wędkarski: x{}',
    'Fishing {}, {} and {} cut trash to {}%%, {}%% and {}%%':
        'Wędkarstwo {}, {} i {} obniżają śmieci do {}%%, {}%% i {}%%',
    'Fog and wind never stack':
        'Mgła i wiatr nigdy się nie sumują',
    'Fog over {}%% or wind over {}%%: x{}':
        'Mgła powyżej {}%% lub wiatr powyżej {}%%: x{}',
    'Nail: x{}':
        'Gwóźdź: x{}',
    'Near shore: x{}':
        'Przy brzegu: x{}',
    'No hook: x{}, nothing ever bites':
        'Bez haczyka: x{}, nic nigdy nie weźmie',
    'Over {} or below {} °C: x{}':
        'Powyżej {} lub poniżej {} °C: x{}',
    'Over {}%%: x{} on the weather':
        'Powyżej {}%%: x{} do pogody',
    'Over {}: x{}':
        'Powyżej {}: x{}',
    'Paperclip: x{}':
        'Spinacz: x{}',
    'Rain: x{}':
        'Deszcz: x{}',
    'Rolled once per attempt':
        'Losowane raz na próbę',
    'Same penalty as fog, they never stack':
        'Ta sama kara co przy mgle, nigdy się nie sumują',
    'Same penalty as wind, they never stack':
        'Ta sama kara co przy wietrze, nigdy się nie sumują',
    'Schools move every day':
        'Ławice przemieszczają się codziennie',
    'This row reports neither':
        'Ten wiersz nie pokazuje żadnego z nich',
    'Trash is fixed per spot':
        'Śmieci są stałe dla danego miejsca',
    'Under {} fish: x{}':
        'Poniżej {} ryb: x{}',
    '{} to {} and {} to {} °C: x{}':
        'Od {} do {} i od {} do {} °C: x{}',
    '{} to {} °C: x{}':
        'Od {} do {} °C: x{}',
    '{} to {}: x{}':
        'Od {} do {}: x{}',
    '{}%% x temperature x weather x time x hook x fish':
        '{}%% x temperatura x pogoda x godzina x haczyk x ryby',
    '{}:{} to {}:{} and {}:{} to {}:{}: x{}':
        'Od {}:{} do {}:{} i od {}:{} do {}:{}: x{}',
    'Fishing {}, {} and {}: trash x{}, x{}, x{}':
        'Wędkarstwo {}, {} i {}: śmieci x{}, x{}, x{}',
    'x time x hook x fish':
        'x godzina x haczyk x ryby',
    '{}%% x temperature x weather':
        '{}%% x temperatura x pogoda',

    # Round 11: moodles rewritten from bytecode + wiki
    "melee damage {}%%": "{}%% obrażeń w zwarciu",
    "melee damage {}": "{} obrażeń w zwarciu",
    "move speed {}%%": "{}%% prędkości ruchu",
    "move speed {}%% with Adrenaline Junkie": "{}%% prędkości z cechą Adrenalinowiec",
    "attack speed {}%%": "{}%% prędkości ataku",
    "combat speed {}%%": "{}%% prędkości walki",
    "run speed {}%%": "{}%% prędkości biegu",
    "crit chance {}%%": "{}%% szansy na cios krytyczny",
    "firearm accuracy {}%%": "{}%% celności broni palnej",
    "firearm accuracy {}%% at {} tiles": "{0}%% celności broni palnej na {1} kratek",
    "clearing a jam {}%%": "{}%% szansy na usunięcie zacięcia",
    "climbing {}%%": "{}%% wspinaczki",
    "climbing fences {}%%": "{}%% wspinaczki po płotach",
    "climbing walls and ropes {}%%": "{}%% wspinaczki po murach i linach",
    "tripping over fences {}%%": "{}%% szansy na potknięcie o płot",
    "blocking an attack {}%%": "{}%% blokowania ataku",
    "foraging {}%%": "{}%% zbieractwa",
    "carry capacity {}": "{} udźwigu",
    "healing {}%%": "{}%% leczenia",
    "healing x{}": "leczenie x{}",
    "poison wears off {}%% faster": "Trucizna mija {}%% szybciej",
    "heat dissipation {}%%": "{}%% oddawania ciepła",
    "heat loss {}%%": "{}%% utraty ciepła",
    "discomfort {}%%": "{}%% dyskomfortu",
    "medicine {}%% less effective": "Leki {}%% mniej skuteczne",
    "sleep {}{}%% less effective": "Sen {0}{1}%% mniej skuteczny",
    "panic x{} per wound": "panika x{} na ranę",
    "over {}%% of capacity": "Ponad {}%% udźwigu",
    "health under {}%%": "Zdrowie poniżej {}%%",
    "health {}%% per hour": "{}%% zdrowia na godzinę",
    "health drops to {}%%": "Zdrowie spada do {}%%",
    "health drops to {}%%, then to {}%%": "Zdrowie spada do {0}%%, potem do {1}%%",
    "health drops to {}%% when the air is above {} C": "Zdrowie spada do {0}%%, gdy powietrze jest powyżej {1} C",
    "health drops when the air is below {} C": "Zdrowie spada, gdy powietrze jest poniżej {} C",
    "only heals indoors, dry, under {}%% fatigue and under {}%% hunger and thirst": "Leczy się tylko w pomieszczeniu i na suchym, przy zmęczeniu poniżej {}%% oraz głodzie i pragnieniu poniżej {}%%",
    "vision cone narrows, cancelling Eagle Eyed": "Stożek widzenia się zwęża i znosi Sokoli wzrok",
    "{} C colder than the air": "{} C mniej niż powietrze",
    "{} wounds bleeding": "{} krwawiące rany",
    "{} wounds, or a bleeding neck": "{} rany albo rana szyi",
    "no healing": "Brak leczenia",
    "no natural healing": "Brak naturalnego leczenia",
    "slower healing": "Wolniejsze leczenie",
    "much slower healing": "Dużo wolniejsze leczenie",
    "slower endurance recovery": "Wolniejsza regeneracja wytrzymałości",
    "much slower endurance recovery": "Dużo wolniejsza regeneracja wytrzymałości",
    "endurance barely recovers": "Wytrzymałość prawie się nie regeneruje",
    "endurance drains as you move and never recovers": "Wytrzymałość spada w ruchu i się nie regeneruje",
    "no sprinting or running": "Ani sprintu, ani biegu",
    "you cannot run": "Nie możesz biec",
    "you cannot sleep": "Nie możesz spać",
    "you cannot eat any more": "Nie zjesz już nic więcej",
    "you can sleep on the ground and through pain": "Możesz spać na ziemi i mimo bólu",
    "cannot swing a sledgehammer": "Nie podniesiesz młota",
    "hunger does not rise": "Głód nie rośnie",
    "less body heat generated": "Mniej ciepła ciała",
    "body heat rises": "Temperatura ciała rośnie",
    "body heat rises sharply": "Temperatura ciała mocno rośnie",
    "thirst and fatigue rise faster": "Pragnienie i zmęczenie rosną szybciej",
    "you lose heat in the cold": "Tracisz ciepło na zimnie",
    "more likely to catch a cold": "Większa szansa na przeziębienie",
    "more likely to fall ill": "Większa szansa na chorobę",
    "much more likely to fall ill": "Dużo większa szansa na chorobę",
    "narrower vision cone": "Węższy stożek widzenia",
    "narrower vision and awareness": "Mniejsze pole widzenia i czujność",
    "movement, damage and attack speed drop with the wound": "Ruch, obrażenia i prędkość ataku spadają zależnie od rany",
    "you make noise": "Hałasujesz",
    "you complain out loud": "Narzekasz na głos",
    "you get up faster": "Wstajesz szybciej",
    "you weave as you walk": "Zataczasz się przy chodzeniu",
    "timed actions take longer": "Czynności trwają dłużej",
    "unhappiness rises": "Rośnie przygnębienie",
    "unhappiness rises slowly": "Przygnębienie rośnie powoli",
    "unhappiness rises fast": "Przygnębienie rośnie szybko",
    "stress rises": "Rośnie stres",
    "boredom is wiped and held down": "Nuda zeruje się i nie rośnie",
    "the Desensitized trait cancels it": "Cecha Znieczulony to znosi",
    "no effect until NPCs return": "Bez efektu, dopóki nie wrócą NPC",
    "discomfort while in a vehicle": "Dyskomfort w pojeździe",
    "hypothermia is hidden": "Hipotermia jest ukryta",
    "it wakes you up": "To cię budzi",
    "you sneeze now and then": "Od czasu do czasu kichasz",
    "you sneeze and cough often": "Często kichasz i kaszlesz",
    "you cough so much that hiding gets hard": "Kaszlesz tak, że trudno się ukryć",
    "you cough constantly and draw zombies": "Kaszlesz bez przerwy i wabisz zombie",
    "health loss": "Utrata zdrowia",
    "slow health loss": "Powolna utrata zdrowia",
    "serious health loss": "Poważna utrata zdrowia",
    "health slowly drops": "Zdrowie powoli spada",
    "health drops if this is infection or poison": "Zdrowie spada, jeśli to zakażenie albo trucizna",
    "death without first aid": "Śmierć bez pierwszej pomocy",
    "sickness starts to build": "Choroba zaczyna narastać",
    "sickness builds noticeably": "Choroba wyraźnie narasta",
    "many rotting corpses": "Wiele gnijących zwłok",
    "more rotting corpses": "Więcej gnijących zwłok",
    "the worst corpses can do": "Najgorsze, co robią zwłoki",
    "a generator running indoors": "Generator pracuje w budynku",
    "it will not kill you outright": "To cię od razu nie zabije",
    "a gas mask or SCBA prevents it": "Maska gazowa lub aparat oddechowy temu zapobiega",
    "caused by heavy clothing, bags, bare feet or leg injuries": "Przez ciężkie ubranie, torby, bose stopy lub ranne nogi",

    # Animals (round 10, block C)
    "Animals: butchering yield, milk, wool and old age":
        "Zwierzęta: wydajność mięsa, mleko, wełna i starość",
    "Adds rows to the animal window you get by right-clicking an animal: meat yield, blood, feathers, old age and weight ceiling, which no screen shows, plus health, hunger, thirst, attitude, milk, wool and pregnancy as numbers instead of words.":
        "Dodaje wiersze do okna zwierzęcia otwieranego prawym przyciskiem: wydajność mięsa, krew, pióra, starość i maksymalna waga, których nie pokazuje żaden ekran, a także zdrowie, głód, pragnienie, nastawienie, mleko, wełna i ciąża jako liczby zamiast słów.",
    "Animals: keep vanilla's Animal Care level requirements":
        "Zwierzęta: zachowaj wymagania poziomu Opieki nad zwierzętami",
    "Off by default, so you see everything from level {}. Turn it on and each row reappears at the Animal Care level vanilla itself uses for it: pregnancy at {}, weight at {}, attitude at {}.":
        "Domyślnie wyłączone, więc wszystko widzisz od poziomu {}. Włącz, a każdy wiersz wróci na poziom Opieki nad zwierzętami, którego używa sama gra: ciąża na {}, waga na {}, nastawienie na {}.",
    "Meat yield":
        "Wydajność mięsa",
    "full in %1":
        "pełne za %1",

    # Animal hover descriptions (round 12)
    "Size x meat gene.":
        "Rozmiar x gen mięsa.",
    "Multiplies the number of meat pieces and the calories of each one.":
        "Mnoży liczbę kawałków mięsa i kalorie każdego z nich.",
    "Butchering adds x{} every {} levels.":
        "Rzeźnictwo dodaje x{} co {} poziomy.",
    "Off the ground x{}, on a butcher hook x{}.":
        "Z ziemi x{}, na haku rzeźnickim x{}.",
    "Litres you can drain into a bucket once it is dead.":
        "Litry, które można spuścić do wiadra po śmierci.",
    "Grows with weight.":
        "Rośnie razem z wagą.",
    "Feathers you get for butchering it.":
        "Pióra, które dostajesz za oprawienie.",
    "Breed maximum x size.":
        "Maksimum rasy x rozmiar.",
    "{}%% until {}%% of its life expectancy, then it climbs to {}%%.":
        "{}%% do {}%% oczekiwanej długości życia, potem rośnie do {}%%.",
    "Over {}%% it loses {}%% health every hour.":
        "Powyżej {}%% traci {}%% zdrowia na godzinę.",
    "Current weight and the most this animal can reach.":
        "Obecna waga i najwyższa, jaką to zwierzę osiągnie.",
    "Meat and blood both scale with it.":
        "Mięso i krew skalują się razem z nią.",
    "Over {}%% hunger it starts losing weight.":
        "Przy głodzie powyżej {}%% zaczyna tracić wagę.",
    "{}{}, how much this animal puts up with you.":
        "{}{}, jak bardzo to zwierzę cię znosi.",
    "Each point takes {} off the chance it breaks free while being sheared.":
        "Każdy punkt obniża o {} szansę, że wyrwie się przy strzyżeniu.",
    "Every gain is {}, plus {} per Animal Care level.":
        "Każdy przyrost to {}, plus {} na poziom Opieki nad zwierzętami.",
    "Healthy over {}%%, off colour over {}%%, sickly over {}%%, dying below.":
        "Zdrowe powyżej {}%%, osłabione powyżej {}%%, chorowite powyżej {}%%, umierające poniżej.",
    "Higher is worse.":
        "Im wyżej, tym gorzej.",
    "Well fed under {}%%, underfed under {}%%, starving over it.":
        "Dobrze najedzone poniżej {}%%, niedożywione poniżej {}%%, głodujące powyżej.",
    "Over {}%% it starts losing weight.":
        "Powyżej {}%% zaczyna tracić wagę.",
    "Fully watered under {}%%, thirsty under {}%%, dying of thirst over it.":
        "Nawodnione poniżej {}%%, spragnione poniżej {}%%, umierające z pragnienia powyżej.",
    "{}{}. Calm under {}, unnerved under {}, agitated under {}, wild over it.":
        "{}{}. Spokojne poniżej {}, niespokojne poniżej {}, pobudzone poniżej {}, dzikie powyżej.",
    "Over {} milk and wool grow at {} / stress of their rate.":
        "Powyżej {} mleko i wełna rosną w tempie {} / stres normalnego.",
    "Over {} a pregnancy can be lost.":
        "Powyżej {} ciąża może zostać utracona.",
    "Milking with stress over {} and Animal Care {} or less always fails and spills the bucket.":
        "Dojenie przy stresie powyżej {} i Opiece nad zwierzętami {} lub niższej zawsze się nie udaje i rozlewa wiadro.",
    "Litres in the udder and what it holds.":
        "Litry w wymieniu i jego pojemność.",
    "It fills by capacity / {} per game hour, times the sandbox milk modifier.":
        "Napełnia się o pojemność / {} na godzinę gry, razy modyfikator mleka z piaskownicy.",
    "Stress over {} slows it down.":
        "Stres powyżej {} to zwalnia.",
    "Wool grown and the maximum.":
        "Wyrośnięta wełna i maksimum.",
    "It grows by maximum / {} per game hour: {} days for a full fleece.":
        "Rośnie o maksimum / {} na godzinę gry: {} dni na pełne runo.",
    "Days left before it gives birth.":
        "Dni do porodu.",
    "Stress over {} can end the pregnancy.":
        "Stres powyżej {} może zakończyć ciążę.",
    "Hours this female stays fertilised.":
        "Godziny, przez które ta samica pozostaje zapłodniona.",
    "When it runs out she is no longer fertilised.":
        "Gdy się skończą, przestaje być zapłodniona.",

    # Wounds and healing
    "Wounds: how long each one still needs":
        "Rany: ile czasu jeszcze potrzebuje każda",
    "Adds an Info entry under the treatments you get by clicking a body part in the health panel. Hover it and the box beside it gives the time left on every wound, what bandaging or a poultice would save, how long the bandage lasts and whether the part is mending or getting worse. The game knows all of it and only prints it in debug mode.":
        "Dodaje pozycję Informacje pod zabiegami, które pojawiają się po kliknięciu części ciała w oknie zdrowia. Po najechaniu ramka obok podaje czas pozostały każdej ranie, ile dałby bandaż albo okład, jak długo wytrzyma bandaż i czy część ciała się goi, czy pogarsza. Gra to wszystko wie i wypisuje tylko w trybie debugowania.",
    "Wounds: keep vanilla's Doctor level requirements":
        "Rany: zachowaj wymagania poziomu Pierwszej pomocy",
    "Off by default, so you see everything from level {}. Turn it on and each row reappears at the Doctor level vanilla itself uses for it: scratches and lacerations at {}, deep wounds and splints at {}, fractures and stitches at {}, wound infection at {}.":
        "Domyślnie wyłączone, więc wszystko widzisz od poziomu {}. Włącz, a każdy wiersz wróci na poziom Pierwszej pomocy, którego używa sama gra: zadrapania i rozcięcia na {}, głębokie rany i szyny na {}, złamania i szwy na {}, zakażenie rany na {}.",
    "Full recovery":
        "Pełne wyzdrowienie",
    "Getting worse":
        "Pogarsza się",
    "Healing":
        "Gojenie",
    "normal":
        "normalne",
    "slowed by hunger, thirst or illness":
        "spowolnione przez głód, pragnienie lub chorobę",
    "stopped by hunger or thirst":
        "zatrzymane przez głód lub pragnienie",
    "asleep, ten times faster":
        "we śnie, dziesięć razy szybciej",
    "wounded parts share it":
        "rannych części dzieli je między siebie",
    "Bandage life":
        "Trwałość bandaża",
    "ready to remove":
        "gotowe do zdjęcia",

    # Wounds and healing, redesigned tooltip
    "Healing speed":
        "Szybkość gojenia",
    "clean for":
        "czysty przez",
    "Poultice":
        "Okład",
    "Wound infection":
        "Zakażenie rany",
    "won't close, glass inside":
        "nie zamknie się, w środku jest szkło",
    "won't close while unbandaged":
        "nie zamknie się bez bandaża",
    "rising":
        "rośnie",

    # Wounds: shorter recovery label and infection risk
    "Recovery":
        "Wyzdrowienie",
    "Infection risk":
        "Ryzyko zakażenia",

    # Percentages, ported from the multiplier wording
    "{}%% weapon damage": "{}%% obrażeń broni",
    "{}%% endurance recovery": "{}%% regeneracji wytrzymałości",
    "{}%% melee damage and knockback": "{}%% obrażeń w zwarciu i odrzutu",
    "{}%% move speed in combat stance": "{}%% prędkości w postawie bojowej",
    "{}%% sprint speed": "{}%% prędkości sprintu",
    "{}%% chance of being spotted": "{}%% szansy na zauważenie cię",
    "{}%% footstep noise": "{}%% hałasu kroków",
    "{}%% recoil delay": "{}%% opóźnienia po odrzucie",
    "{}%% aim settling speed": "{}%% szybkości stabilizowania celownika",
    "{}%% aim penalty for moving (shared with Nimble)":
        "{}%% kary do celowania w ruchu (wspólna ze Zwinnością)",
    "{}%% reload speed": "{}%% szybkości przeładowania",
    "{}%% racking speed": "{}%% szybkości repetowania",
    "{}%% XP in every Crafting skill": "{}%% PD we wszystkich umiejętnościach Rzemiosła",
    "{}%% move speed through trees": "{}%% prędkości między drzewami",
    "spotting another player {}%%": "{}%% na dostrzeżenie innego gracza",
    "timed actions {}%%": "czynności trwają {}%%",
    "endurance drain {}%%": "{}%% zużycia wytrzymałości",
    "alcohol hits {}%%, and {}%% over {}%% hunger":
        "Alkohol działa {0}%%, a przy głodzie powyżej {2}%% {1}%%",
    "Fitness {}, which is {}%% endurance recovery instead of {}%%":
        "Kondycja {}, czyli {}%% regeneracji wytrzymałości zamiast {}%%",
    "{}%% attack speed": "{}%% szybkości ataku",
    "{}%% crit chance": "{}%% szansy na trafienie krytyczne",
    "racking costs {}%% of the aiming time": "repetowanie kosztuje {}%% czasu celowania",
    "carrying capacity {}": "udźwig {}",
    "{} to every weapon's durability roll.": "{} do rzutu na wytrzymałość każdej broni.",
    "Condition loss (handle)": "Utrata stanu (rękojeści)",
    "Condition loss (head)": "Utrata stanu (głowni)",

    # Ronda 4: medicine, traps, weapon components, skill levels
    '%1 corpses nearby': '%1 zwłok w pobliżu',
    '%1%% attack time': '%1%% czasu ataku',
    '%1%% crit chance': '%1%% szansy na trafienie krytyczne',
    '%1%% muscle strain': '%1%% obciążenia mięśni',
    '%1%% weapon damage': '%1%% obrażeń broni',
    '+%1 to the durability roll': '+%1 do rzutu na wytrzymałość',
    'Adds an Info entry to a placed trap: the odds of it catching anything in an hour, which animals it can take and the share of the catch each one gets, the bait and its freshness, the zone, the hourly odds of losing bait or trap, and the warning that a trap catches nothing while you stand next to it. Bait foods get a row naming what they attract.': 'Dodaje wpis Info do postawionej pułapki: szansę, że w ciągu godziny cokolwiek złapie, jakie zwierzęta może złapać i jaki udział w zdobyczy przypada każdemu, przynętę i jej świeżość, strefę, godzinowe szanse na utratę przynęty lub pułapki oraz ostrzeżenie, że pułapka nic nie złapie, dopóki stoisz obok. Jedzenie służące za przynętę dostaje wiersz z informacją, co przyciąga.',
    'Bait': 'Przynęta',
    'Bait lost per hour': 'Utrata przynęty na godzinę',
    'In the trap for': 'W pułapce od',
    'Filter left': 'Pozostało filtra',
    'Hits before it breaks': 'Uderzeń do zniszczenia',
    'Medicine: duration, delay and effect': 'Leki: czas działania, opóźnienie i efekt',
    'Medicine: the full list of effects': 'Leki: pełna lista efektów',
    'Muscle strain per hit': 'Obciążenie mięśni na uderzenie',
    'Off by default, so you see everything from level {}. Turn it on and the trap tooltip only appears from Trapping {}, which is the level vanilla itself uses elsewhere.': 'Domyślnie wyłączone, więc widzisz wszystko od poziomu {}. Po włączeniu podpowiedź pułapki pojawia się dopiero od Pułapek {}, czyli poziomu, którego gra sama używa gdzie indziej.',
    'Off by default. Adds everything else each pill does: what cancels it, what intoxication costs it, and the sleeping tablet overdose table.': 'Domyślnie wyłączone. Dodaje wszystko inne, co robi każda tabletka: co ją znosi, ile kosztuje ją upojenie i tabelę przedawkowania tabletek nasennych.',
    'Painkillers, beta blockers, antidepressants, sleeping tablets and antibiotics get how long they last, how long they take to start and what they do per minute. Every figure is recomputed from the sandbox day length.': 'Środki przeciwbólowe, beta-blokery, antydepresanty, tabletki nasenne i antybiotyki pokazują, jak długo działają, ile zajmuje im start i co robią na minutę. Każda wartość jest przeliczana na nowo z długości doby w piaskownicy.',
    'Prey': 'Zdobycz',
    'Rots once thawed': 'Gnije po rozmrożeniu',
    'Stale once thawed': 'Czerstwieje po rozmrożeniu',
    'Takes effect in': 'Zaczyna działać za',
    'Trap lost per hour': 'Utrata pułapki na godzinę',
    'Traps: catch odds, bait and hours': 'Pułapki: szanse złapania, przynęta i godziny',
    "Traps: keep vanilla's Trapping level requirements": 'Pułapki: zachowaj wymagania poziomu Pułapek z gry',
    'Zone': 'Strefa',
    'a second dose resets the clock, it does not add': 'druga dawka zeruje zegar, a nie dodaje',
    'a third of the strength above {} intoxication': 'jedna trzecia siły powyżej {} upojenia',
    'fresh for %1': 'świeża jeszcze %1',
    'half the strength above {} intoxication': 'połowa siły powyżej {} upojenia',
    'each pill counts double above {} intoxication': 'każda tabletka liczy się podwójnie powyżej {} upojenia',
    'holds the fever, does not cure it': 'wstrzymuje gorączkę, nie leczy jej',
    'incoming panic {}%% per pill, down to nothing': 'przychodząca panika {}%% na tabletkę, aż do zera',
    'it catches nothing while you are near it': 'nic nie złapie, dopóki jesteś obok',
    'only the first dose has to wait': 'tylko pierwsza dawka musi czekać',
    'overdose: {} pills cost {} health, {} cost {}, {} kill': 'przedawkowanie: {} tabletek kosztuje {} zdrowia, {} kosztuje {}, {} zabija',
    'sleeping cancels the effect': 'sen znosi efekt',
    'stale, catches nothing': 'czerstwa, nic nie przyciąga',
    'the longer it waits, the likelier it comes out dead': 'im dłużej czeka, tym większa szansa, że wyjdzie martwe',
    'to full in %1': 'do pełna za %1',
    'to zero in %1': 'do zera za %1',
    'wound pain stops being recalculated while it lasts': 'ból ran przestaje być przeliczany, dopóki działa',
    'zombie fever held': 'gorączka zombie wstrzymana',
    '{}%% reading time': '{}%% czasu czytania',
    'Effect': 'Efekt',

    # Ronda 4, segunda pasada
    '%1 s': '%1 s',
    '%1 s per round': '%1 s na nabój',
    '%1%% attack speed': '%1%% szybkości ataku',
    'Details': 'Szczegóły',
    'Info': 'Info',
    'Possible prey': 'Możliwa zdobycz',
    'Trap breaks per hour': 'Pułapka pęka na godzinę',
    'holds the fever': 'wstrzymuje gorączkę',
    'not being used (%1 corpses nearby)': 'nie zużywa się (%1 zwłok w pobliżu)',
    'Bird': 'Ptak',
    'Active hours': 'Godziny aktywności',
    'Possible prey, share of the catch': 'Możliwa zdobycz, udział w zdobyczy',
    'Catch chance': 'Szansa na złapanie',
    'Bait condition': 'Stan przynęty',
    'Trap condition': 'Stan pułapki',
    'while you are near it, it neither catches nor breaks': 'dopóki jesteś obok, nic nie złapie ani się nie zepsuje',
    'Bait loss risk, per hour': 'Ryzyko utraty przynęty, na godzinę',
    'Wrecked by an animal, per hour': 'Zniszczona przez zwierzę, na godzinę',
    '%1 / h': '%1 / h',
    'Bait loss risk': 'Ryzyko utraty przynęty',
    'Chance of being wrecked': 'Szansa na zniszczenie',
    'Critical damage': 'Obrażenia krytyczne',
    'Effective durability': 'Efektywna wytrzymałość',
    'Damage with your character': 'Obrażenia z twoją postacią',
    'Reach (tiles)': 'Zasięg (kratki)',

    # Bags and the torch beam (0.9.20)
    'All round': 'Dookoła',
    'Beam (degrees)': 'Stożek światła (stopnie)',
    'Bags: how much they slow you down': 'Torby: jak bardzo cię spowalniają',
    "The run and combat speed a bag costs you, which the game applies and never shows. The run figure is the one you are paying right now: a bag's penalty grows by half again as it fills up, so the same pack goes from {}%% empty to {}%% full. It counts the same in your hands as on your back.": 'Szybkość biegu i walki, którą kosztuje cię torba, gra ją stosuje i nigdy nie pokazuje. Wartość biegu to ta, którą płacisz teraz: kara rośnie o połowę w miarę zapełniania, więc ta sama torba idzie od {}%% pustej do {}%% pełnej. W rękach liczy się tak samo jak na plecach.',

    # Trait figures corrected against bytecode (0.9.21)
    "Aiming and Maintenance are not affected":
        "Celowanie i Konserwacja nie są objęte",
    "ambient light never drops below {} in the dark":
        "światło otoczenia w ciemności nigdy nie spada poniżej {}",
    "can tell a poisonous wild plant from a safe one":
        "rozpoznaje, czy dzika roślina jest trująca",
    "lights a fire with a notched plank twice as fast":
        "rozpala ogień deską z nacięciem dwa razy szybciej",
    "no harm at all from tainted water":
        "brudna woda nie zadaje żadnych obrażeń",
    "{} health on every construction":
        "{} zdrowia każdej konstrukcji",
    "{} tiles of perception instead of {}":
        "{} kratek percepcji zamiast {}",
    "{}%% XP in the six melee weapon skills":
        "{}%% PD w sześciu umiejętnościach broni białej",
    "{}%% chance of tearing your clothes on a tree":
        "{}%% szansy na rozdarcie ubrania o drzewo",
    "{}%% from any other poison":
        "{}%% od każdej innej trucizny",
    "{}%% from any other poison, bleach aside":
        "{}%% od każdej innej trucizny, poza wybielaczem",
    "{}%% weather penalty in combat":
        "{}%% kary za pogodę w walce",

    # Per-level lines for the twenty craft skills (0.9.21)
    "%1 crop health at planting":
        "%1 zdrowia rośliny przy sadzeniu",
    "%1%% chance the crop is cursed if planted out of its month":
        "%1%% szansy, że roślina będzie przeklęta, jeśli posadzisz ją poza jej miesiącem",
    "%1%% chance of a bonus harvest planted in its best month":
        "%1%% szansy na dodatkowe zbiory przy sadzeniu w najlepszym miesiącu",
    "%1 disease removed per treatment":
        "%1 choroby usuwane na zabieg",
    "%1%% chance of harvesting %2 extra vegetables":
        "%1%% szansy na zebranie %2 warzyw więcej",
    "%1%% back strain planting and harvesting":
        "%1%% obciążenia pleców przy sadzeniu i zbiorach",
    "%1 points off the chance a stressed animal breaks off milking or shearing":
        "%1 punktów do szansy, że zestresowane zwierzę wyrwie się przy dojeniu lub strzyżeniu",
    "a stressed animal never breaks off milking or shearing":
        "zestresowane zwierzę nie wyrywa się już przy dojeniu ani strzyżeniu",
    "x%1 chance of each extra part off a carcass":
        "x%1 szansy na każdą dodatkową część z tuszy",
    "x%1 of each part":
        "x%1 każdej części",
    "up to %1 blood splatters on you":
        "do %1 plam krwi na tobie",
    "%1 health on everything you build":
        "%1 zdrowia wszystkiego, co zbudujesz",
    "%1%% build time":
        "%1%% czasu budowy",
    "%1%% barricading time":
        "%1%% czasu barykadowania",
    "%1%% chance of recovering material when dismantling":
        "%1%% szansy na odzyskanie materiału przy rozbiórce",
    "%1%% of the ingredient used per addition":
        "%1%% składnika zużywane na jedno dodanie",
    "x%1 nutrients from each ingredient":
        "x%1 wartości odżywczych z każdego składnika",
    "rotten food can go in evolved recipes, worth %1%% of its hunger":
        "możesz dodać trochę zepsutego jedzenia do rozwiniętych przepisów",
    "x%1 fracture healing with a splint":
        "x%1 gojenia złamania z szyną",
    "a bandage lasts %1 to %2 longer":
        "bandaż trzyma od %1 do %2 razy dłużej",
    "%1%% time for every medical action":
        "%1%% czasu każdej czynności medycznej",
    "you can judge how bad a wound is":
        "potrafisz ocenić, jak poważna jest rana",
    "you can read pain, and spot the burns that need washing":
        "czytasz ból i widzisz, które oparzenia trzeba przemyć",
    "you can tell when stitches are ready to come out":
        "wiesz, kiedy można zdjąć szwy",
    "you spot a wound infection straight away":
        "od razu wykrywasz zakażenie rany",
    "%1%% chance of getting the patch back":
        "%1%% szansy na odzyskanie łaty",
    "%1%% time to add or remove a patch":
        "%1%% czasu na założenie lub zdjęcie łaty",
    "a hole can be repaired completely, defense and insulation included":
        "dziurę da się naprawić całkowicie, razem z ochroną i izolacją",
    "+%1%% generator condition per repair":
        "+%1%% stanu generatora na naprawę",
    "%1 points to the chance of hotwiring a car":
        "%1 punktów do szansy na odpalenie auta na krótko",
    "%1%% chance of setting off the car alarm":
        "%1%% szansy na uruchomienie alarmu w aucie",
    "you can salvage and repair a standard engine":
        "możesz rozebrać i naprawić standardowy silnik",
    "you can salvage and repair a heavy-duty engine":
        "możesz rozebrać i naprawić silnik do dużych obciążeń",
    "you can salvage and repair a sport engine":
        "możesz rozebrać i naprawić silnik sportowy",
    "you can build the sturdier brick wall":
        "możesz zbudować mocniejszy mur z cegły",
    "small %1%%, medium %2%%, large %3%%":
        "mała %1%%, średnia %2%%, duża %3%%",
    "%1 points to the chance a berry or mushroom is poisonous":
        "%1 punktów do szansy, że jagoda lub grzyb są trujące",
    "%1%% time to inspect a track":
        "%1%% czasu na zbadanie tropu",
    "no effect of its own, this level only unlocks the recipes below":
        "brak własnego efektu, ten poziom odblokowuje tylko przepisy poniżej",

    # 0.9.21 follow-up
    "%1 rags when you rip up clothing, capped by the parts it covers":
        "%1 skrawków przy darciu ubrań, ograniczone tym, co zakrywa",
    "rotten food can go in evolved recipes, worth %1%% of its hunger":
        "zepsute jedzenie nadaje się do rozwiniętych przepisów, daje %1%% swojej sytości",

    # 0.9.21 follow-up 2
    "%1%% time per litre shearing an animal":
        "%1%% czasu na litr przy strzyżeniu zwierzęcia",
    "%1 rags when you rip up clothing, capped by the parts it covers":
        "%1 szmat przy darciu ubrań, ograniczone liczbą zakrywanych części",
    "%1 to the most aramid thread you can pull out":
        "%1 do maksimum nici aramidowej, jaką da się wyciągnąć",
    "starts at {} weight, becomes Emaciated at {} or less and Low Weight above {}":
        "zaczyna z wagą {}, przy {} lub mniej zmienia się w Wychudzenie, a powyżej {} w Niedowagę",
    "starts at {} weight, becomes High Weight below {}":
        "zaczyna z wagą {}, poniżej {} zmienia się w Nadwagę",
    "starts at {} weight, becomes Very High Weight at {} and is lost below {}":
        "zaczyna z wagą {}, przy {} zmienia się w Otyłość, a poniżej {} znika",
    "starts at {} weight, becomes Very Low Weight at {} or less and is lost above {}":
        "zaczyna z wagą {}, przy {} lub mniej zmienia się w Znaczną niedowagę, a powyżej {} znika",
    "XP awarded":
        "Przyznane PD",
    "{} chance to trip when a zombie lunges through a window":
        "{} szansy na potknięcie, gdy zombie rzuca się przez okno",
    "{} to the roll that keeps you on your feet when a zombie shoves you":
        "{} do rzutu, który utrzymuje cię na nogach, gdy zombie cię popycha",
    "{}%% muscle strain":
        "{}%% obciążenia mięśni",
    "{}%% axe attack speed, chopping trees included":
        "{}%% szybkości ataku siekierą, w tym ścinanie drzew",

    # B42.20 trait corrections
    "Another x{} at panic level {}":
        "dodatkowe x{} przy panice poziomu {}",
    "Can hotwire without Electrical {} and Mechanics {}":
        "może odpalić bez kluczyka bez Elektryki {} i Mechaniki {}",
    "Engine revs three times faster in reverse":
        "na wstecznym obroty rosną trzy razy szybciej",
    "Halves your rope climbing bonus":
        "zmniejsza o połowę twój bonus do wspinaczki po linie",
    "No unhappiness from looting corpses":
        "przeszukiwanie zwłok nie daje przygnębienia",
    "Stress from handling bloody items":
        "stres przy obchodzeniu się z zakrwawionymi przedmiotami",
    "{} move speed at panic level {}, {} at level {}":
        "{} prędkości przy panice poziomu {}, {} na poziomie {}",
    "{} to the rope climbing roll":
        "{} do rzutu na wspinaczkę po linie",
    "{}%% acceleration, fading out above {}%% of the car's top speed":
        "{}%% przyspieszenia, które zanika powyżej {}%% prędkości maksymalnej auta",
    "{}%% carry capacity":
        "{}%% udźwigu",
    "{}%% chance of breaking a window lock instead of {}%%":
        "{}%% na wyłamanie zamka okna zamiast {}%%",
    "{}%% endurance cost on every exertion":
        "{}%% wytrzymałości na każdy wysiłek",
    "{}%% reverse acceleration, gone past {} km/h":
        "{}%% przyspieszenia na wstecznym, brak powyżej {} km/h",
    "{}%% unhappiness from looting corpses":
        "{}%% przygnębienia przy przeszukiwaniu zwłok",

    # Repair recipes
    "Repair: +%1 condition, %2 chance of failing":
        "Naprawa: +%1 stanu, %2 na niepowodzenie",
    "Repair: +%1 condition, %2 chance of failing, repaired %3 times":
        "Naprawa: +%1 stanu, %2 na niepowodzenie, naprawiano %3 razy",

    # Corpse count and temperature figures
    "Body temperature: the number on every bar":
        "Temperatura ciała: liczba na każdym pasku",
    "Nauseous: how many corpses are making you ill":
        "Mdłości: ile zwłok cię truje",
    "Rotting corpses nearby raise food sickness, and the game never says how many are close enough. Five or fewer do nothing. The count is read back out of the game, so it follows the sandbox setting.":
        "Gnijące zwłoki w pobliżu podnoszą zatrucie pokarmowe, a gra nigdy nie mówi, ile jest wystarczająco blisko. Pięć lub mniej nic nie robi. Liczba jest odczytywana z samej gry, więc podąża za ustawieniem piaskownicy.",
    "The temperature view prints its value on Insulation and Wind resistance and leaves the other nine bars as a colour. This sets the same flag on the rest, so skin temperature, body response, heat and wetness read as figures. Vanilla does the drawing, and only for the body part you have selected.":
        "Widok temperatury wypisuje wartość tylko na Izolacji i Odporności na wiatr, a pozostałe dziewięć pasków zostawia jako kolor. To ustawia tę samą flagę na reszcie, więc temperatura skóry, reakcja ciała, ciepło i wilgoć czytają się jako liczby. Rysuje sama gra, i tylko dla wybranej części ciała.",

    # Options tab
    "Custom":
        "Własne",
    "Nothing matches that":
        "Nic nie pasuje",
    "Moodles: how many corpses are making you ill":
        "Moodle: ile zwłok cię truje",

    # Option groups
    "Every gun this box or magazine fits, one per row.":
        "Każda broń, do której pasuje to pudełko lub magazynek, po jednej w wierszu.",
    "How bloody the garment is, out of a hundred.":
        "Jak bardzo ubranie jest zakrwawione, na sto.",
    "How brightly it lights what it reaches.":
        "Jak jasno oświetla to, co obejmuje.",
    "How dirty the garment is, out of a hundred.":
        "Jak bardzo ubranie jest brudne, na sto.",
    "How drunk this container will get you.":
        "Jak bardzo upije cię ten pojemnik.",
    "How far the light reaches, in tiles.":
        "Jak daleko sięga światło, w kratkach.",
    "How far the shot is heard, which is how far the horde comes from.":
        "Jak daleko słychać strzał, czyli skąd przyjdzie horda.",
    "How long before the pill starts working, and only while you have none running.":
        "Ile czasu, zanim tabletka zacznie działać, i tylko dopóki żadna nie działa.",
    "How long cooked food can stay on the heat before it burns.":
        "Jak długo ugotowane jedzenie wytrzyma na ogniu, zanim się przypali.",
    "How long the charge lasts with the thing switched on.":
        "Jak długo starcza ładunku przy włączonym urządzeniu.",
    "How long the filter lasts at your current exposure, and how many corpses are around you.":
        "Jak długo starcza filtra przy twojej obecnej ekspozycji i ile zwłok jest wokół ciebie.",
    "How long the item burns for as fuel.":
        "Jak długo przedmiot pali się jako paliwo.",
    "How long the pages you have not read yet will take.":
        "Ile zajmą strony, których jeszcze nie przeczytałeś.",
    "How long the pill keeps working.":
        "Jak długo tabletka dalej działa.",
    "How long the plant takes to be ready, at the current farming speed.":
        "Ile roślina potrzebuje, żeby dojrzeć, przy obecnej szybkości uprawy.",
    "How long until the food goes stale, at the current rot speed.":
        "Ile zostało, zanim jedzenie zwietrzeje, przy obecnej szybkości psucia.",
    "How long until the food is rotten, at the current rot speed.":
        "Ile zostało, zanim jedzenie zgnije, przy obecnej szybkości psucia.",
    "How many hits the weapon has left in it, which is the one figure that compares any two weapons.":
        "Ile ciosów zostało w broni, czyli jedyna liczba porównująca dowolne dwie bronie.",
    "How much cold the garment keeps out. The game only draws a bar.":
        "Ile zimna zatrzymuje ubranie. Gra rysuje tylko pasek.",
    "How much is left in the filter.":
        "Ile zostało w filtrze.",
    "How much of it you have already heard.":
        "Ile z tego już przesłuchałeś.",
    "How much of the corpse sickness the mask keeps off you. {}%% is immunity.":
        "Ile choroby ze zwłok maska od ciebie odsuwa. {}%% to pełna odporność.",
    "How much of your hunger bar the drink covers.":
        "Jaką część paska głodu pokrywa napój.",
    "How much of your thirst bar the drink covers.":
        "Jaką część paska pragnienia pokrywa napój.",
    "How much pull the rod takes before the line gives.":
        "Jak mocne szarpnięcie wytrzyma wędka, zanim puści żyłka.",
    "How much rain the garment keeps out. The game only draws a bar.":
        "Ile deszczu zatrzymuje ubranie. Gra rysuje tylko pasek.",
    "How much the bag slows you down, with its weight and what is inside counted.":
        "Jak bardzo plecak cię spowalnia, licząc jego wagę i zawartość.",
    "How much the bag slows your swing.":
        "Jak bardzo plecak spowalnia twój cios.",
    "How much the garment slows you down, as the penalty itself rather than a bar.":
        "Jak bardzo ubranie cię spowalnia, jako sama kara, a nie pasek.",
    "How much the garment slows your swing, as the penalty itself rather than a bar.":
        "Jak bardzo ubranie spowalnia twój cios, jako sama kara, a nie pasek.",
    "How much tiredness this surface actually clears, your traits included.":
        "Ile zmęczenia ta powierzchnia naprawdę zdejmuje, licząc twoje cechy.",
    "How much wind the garment keeps out. The game only draws a bar.":
        "Ile wiatru zatrzymuje ubranie. Gra rysuje tylko pasek.",
    "How often a hit crits, with your level in the weapon's own skill counted.":
        "Jak często cios jest krytyczny, licząc twój poziom w umiejętności tej broni.",
    "How often a shot crits.":
        "Jak często strzał jest krytyczny.",
    "How wet the garment is, out of a hundred.":
        "Jak bardzo ubranie jest mokre, na sto.",
    "In tiles. A swing landed at the edge of your reach does up to twice the damage of one landed close in.":
        "W kratkach. Cios zadany na granicy zasięgu robi nawet dwa razy więcej obrażeń niż zadany z bliska.",
    "Off by default: the game only reveals this block for packaged food or a Nutritionist.":
        "Domyślnie wyłączone: gra pokazuje ten blok tylko przy jedzeniu w opakowaniu lub z Dietetykiem.",
    "Rounds in the magazine right now, out of what it holds.":
        "Naboje w magazynku w tej chwili, z tego, ile się mieści.",
    "The calibre the magazine takes.":
        "Kaliber, który przyjmuje magazynek.",
    "The calories in what is actually in the container, mixtures included.":
        "Kalorie tego, co naprawdę jest w pojemniku, z mieszankami włącznie.",
    "The carbohydrates in what is actually in the container.":
        "Węglowodany tego, co naprawdę jest w pojemniku.",
    "The charge left, as a number instead of a bar.":
        "Pozostały ładunek, liczbą zamiast paska.",
    "The edge, and the ceiling a worn head puts on it: blunt, the weapon loses the top of its damage range.":
        "Ostrze i sufit, jaki nakłada mu zużyta głowica: tępa broń traci górę swojego zakresu obrażeń.",
    "The exact minimum and maximum. The game only ever draws it as a bar.":
        "Dokładne minimum i maksimum. Gra rysuje to wyłącznie jako pasek.",
    "The exact points left, and the head's own count on a weapon that has one.":
        "Dokładne pozostałe punkty, a przy broni z głowicą także jej własne.",
    "The exact points left, where the game only draws a bar.":
        "Dokładne pozostałe punkty tam, gdzie gra rysuje tylko pasek.",
    "The fat in what is actually in the container.":
        "Tłuszcze tego, co naprawdę jest w pojemniku.",
    "The fatigue each swing costs you.":
        "Zmęczenie, które kosztuje cię każdy cios.",
    "The furthest tile the gun can hit.":
        "Najdalsza kratka, w którą broń trafia.",
    "The gun's own hit chance, before your aiming skill.":
        "Własna celność broni, przed twoją umiejętnością strzelania.",
    "The hook fitted, and what it does to your odds of a bite.":
        "Założony haczyk i to, co robi z twoją szansą na branie.",
    "The line fitted, and how much of it each tug wears away.":
        "Założona żyłka i ile jej ściera każde szarpnięcie.",
    "The months it can be sown in, one per row.":
        "Miesiące, w których można siać, po jednym w wierszu.",
    "The multiplier your shoes put on stomping a downed zombie. Footwear only.":
        "Mnożnik, jaki twoje buty dają deptaniu leżącego zombie. Tylko obuwie.",
    "The multiplier your skill puts on this weapon's swing.":
        "Mnożnik, jaki twoja umiejętność daje ciosowi tej broni.",
    "The net pace of the pill, which is what compares two of them at a glance.":
        "Tempo netto tabletki, czyli to, co porównuje dwie z nich na pierwszy rzut oka.",
    "The odds of losing a point of condition on a hit, with Maintenance and the weapon's skill counted.":
        "Szansa na utratę punktu stanu przy trafieniu, licząc Konserwację i umiejętność broni.",
    "The odds of losing a point of condition per shot.":
        "Szansa na utratę punktu stanu na strzał.",
    "The poison the drink carries, and only while the game is willing to tell you.":
        "Prawdziwa szansa na zacięcie, ze zużyciem i słabym chwytem włącznie.",
    "The proteins in what is actually in the container.":
        "Białka tego, co naprawdę jest w pojemniku.",
    "The real odds of a jam, wear and a weak grip included.":
        "Trucizna, którą niesie napój, i tylko dopóki gra chce ci o tym powiedzieć.",
    "The real seconds a reload takes, with your reloading skill and your panic counted.":
        "Prawdziwe sekundy przeładowania, licząc twoją umiejętność przeładowania i panikę.",
    "The real seconds spent lining up the shot, with your aiming skill and your traits counted.":
        "Prawdziwe sekundy na złożenie się do strzału, licząc twoją celność i twoje cechy.",
    "The recipes it teaches that you do not know yet, one per row.":
        "Przepisy, których uczy, a których jeszcze nie znasz, po jednym w wierszu.",
    "The swing animation, which is what really separates a slow weapon from a fast one.":
        "Animacja zamachu, czyli to, co naprawdę dzieli broń wolną od szybkiej.",
    "What a critical is worth, from {}%% to {}%% depending on the weapon. The game shows it nowhere.":
        "Ile wart jest krytyk, od {}%% do {}%% zależnie od broni. Gra nie pokazuje tego nigdzie.",
    "What feeds the Uncomfortable moodle. The game never shows it on the garment at all.":
        "To, co napędza moodle dyskomfortu. Gra w ogóle tego na ubraniu nie pokazuje.",
    "What is left in your hands when the rod breaks.":
        "Co zostaje ci w rękach, gdy wędka pęknie.",
    "What sleeping here costs you in comfort.":
        "Ile kosztuje cię w komforcie spanie tutaj.",
    "What the drink does to boredom and unhappiness, which move together here.":
        "Co napój robi z nudą i przygnębieniem, które idą tu razem.",
    "What the drink does to your fatigue bar.":
        "Co napój robi z twoim paskiem zmęczenia.",
    "What the drink does to your stress.":
        "Co napój robi z twoim stresem.",
    "What the food still needs, and the temperature the figure assumes.":
        "Ile jedzeniu jeszcze brakuje i jaką temperaturę zakłada ta liczba.",
    "Whether it is a cone you aim or a lamp that lights all around, and how wide the cone is.":
        "Czy to stożek, który kierujesz, czy lampa świecąca dookoła, i jak szeroki jest stożek.",
    "Which fish this bait brings in.":
        "Jakie ryby przyciąga ta przynęta.",
    "Which skill the tape or disc trains and how much experience is left in it.":
        "Jakiej umiejętności uczy kaseta lub płyta i ile doświadczenia w niej zostało.",
    "Which skill the weapon trains, and therefore which one drives its damage and its speed.":
        "Jakiej umiejętności uczy broń, a więc która napędza jej obrażenia i szybkość.",
    "Your own reading speed, traits, glasses and sitting down included.":
        "Twoja własna szybkość czytania, z cechami, okularami i siedzeniem włącznie.",
    "Nutrition":
        "Wartości odżywcze",
    "Sleep":
        "Sen",
    "How much the bag slows your attack. It multiplies the weapon's own swing speed, not your walking.":
        "Jak bardzo plecak spowalnia twój atak. Mnoży szybkość zamachu samej broni, a nie twoje chodzenie.",
    "How much the garment slows your attack. It multiplies the weapon's own swing speed, not your walking.":
        "Jak bardzo ubranie spowalnia twój atak. Mnoży szybkość zamachu samej broni, a nie twoje chodzenie.",
    "Best baits":
        "Najlepsze przynęty",
    "Every animal this trap can catch and its share of the catch.":
        "Każde zwierzę, które ta pułapka może złapać, i jego udział w zdobyczy.",
    "Feathers":
        "Pióra",
    "Fog on a line of its own, because the game lumps it into weather and then reports neither.":
        "Mgła w osobnym wierszu, bo gra wrzuca ją do pogody, a potem nie mówi o żadnej z nich.",
    "Glass or a bullet still in the wound, which stops it healing until it is out.":
        "Szkło albo pocisk wciąż w ranie, przez co nie zagoi się, dopóki nie zostaną wyjęte.",
    "How far the disease has gone, out of a hundred.":
        "Jak daleko posunęła się choroba, na sto.",
    "How far the generator is heard, halved when it stands indoors.":
        "Jak daleko słychać generator; pod dachem o połowę mniej.",
    "How full the udder is and whether it can be milked yet.":
        "Jak pełne jest wymię i czy można już doić.",
    "How hungry the animal is, and how long its feed will last.":
        "Jak głodne jest zwierzę i na jak długo starczy mu paszy.",
    "How long before old age starts costing the animal its yield.":
        "Ile zostało, zanim starość zacznie odbierać zwierzęciu wydajność.",
    "How long each cut, scratch, burn or bite still needs.":
        "Ile jeszcze potrzebuje każde skaleczenie, zadrapanie, oparzenie czy ugryzienie.",
    "How long is left of a pregnancy, or of an egg being fertilised.":
        "Ile zostało do końca ciąży albo do zapłodnienia jaja.",
    "How long since the last watering. The game works it out to pick a colour and then never shows it.":
        "Ile minęło od ostatniego podlania. Gra liczy to, żeby dobrać kolor, i nigdy nie pokazuje.",
    "How long the bandage lasts before it is dirty and worth changing.":
        "Jak długo trzyma bandaż, zanim zabrudzi się i będzie wart zmiany.",
    "How long the catch has been waiting in there.":
        "Jak długo zdobycz już tam czeka.",
    "How long the fracture needs, and what the splint on it is worth.":
        "Ile potrzebuje złamanie i ile warta jest założona na nie szyna.",
    "How long the fuel in the tank lasts at the current draw.":
        "Na jak długo starcza paliwa w zbiorniku przy obecnym poborze.",
    "How long the part needs to be whole again, and how fast it is healing.":
        "Ile potrzebuje ta część, żeby znów była cała, i jak szybko się goi.",
    "How long the stiffness in that limb takes to pass.":
        "Ile czasu schodzi sztywność w tej kończynie.",
    "How long the stitches need, and when they can come out.":
        "Ile potrzebują szwy i kiedy można je zdjąć.",
    "How long until it breaks down for good, on average.":
        "Ile zostało, zanim popsuje się na dobre, średnio.",
    "How long until it wears down to the point where it can catch fire.":
        "Ile zostało, zanim zużyje się do punktu, w którym może się zapalić.",
    "How long until the crop moves to its next stage.":
        "Ile zostało, zanim uprawa przejdzie do następnej fazy.",
    "How long you will wait compared with the best possible spot.":
        "Ile będziesz czekać w porównaniu z najlepszym możliwym miejscem.",
    "How many feathers butchering will give.":
        "Ile piór da oprawianie.",
    "How many fish this spot still holds, and what that is worth.":
        "Ile ryb zostało jeszcze w tym miejscu i ile to warte.",
    "How much blood butchering will give.":
        "Ile krwi da oprawianie.",
    "How much fertiliser the plot holds. Above one is the too much case in the game's own code.":
        "Ile nawozu ma grządka. Powyżej jednego to w kodzie samej gry przypadek nadmiaru.",
    "How much meat butchering will give, which is what answers whether it is worth killing yet.":
        "Ile mięsa da oprawianie, czyli odpowiedź na pytanie, czy już warto ubijać.",
    "How much of the bait is still good.":
        "Ile przynęty jest jeszcze dobre.",
    "How much the animal trusts you, which is what lets you handle it.":
        "Jak bardzo zwierzę ci ufa, bo to właśnie pozwala się nim zajmować.",
    "How much wool has grown back and whether it can be sheared yet.":
        "Ile wełny odrosło i czy można już strzyc.",
    "How stressed the animal is, out of a hundred.":
        "Jak zestresowane jest zwierzę, na sto.",
    "How the wound infection is going, and whether it is still rising.":
        "Jak idzie zakażenie rany i czy wciąż rośnie.",
    "How thirsty the animal is, and how long its water will last.":
        "Jak spragnione jest zwierzę i na jak długo starczy mu wody.",
    "Level needed":
        "Wymagany poziom",
    "Lodged objects":
        "Tkwiące przedmioty",
    "Odds with your bait":
        "Szansa z twoją przynętą",
    "Predator":
        "Drapieżnik",
    "Size and weight":
        "Rozmiar i waga",
    "Strength at the top skill level":
        "Wytrzymałość na najwyższym poziomie",
    "The Fishing level this species needs before it will bite.":
        "Poziom Wędkarstwa, jakiego ten gatunek wymaga, żeby wziąć.",
    "The animal's health as a number.":
        "Zdrowie zwierzęcia jako liczba.",
    "The animal's weight, and how far it still has to grow.":
        "Waga zwierzęcia i ile jeszcze ma urosnąć.",
    "The chance of this exact species with the bait you are using.":
        "Szansa na dokładnie ten gatunek przy przynęcie, której używasz.",
    "The crop's health out of a hundred. The game only prints it with debug on.":
        "Zdrowie uprawy na sto. Gra wypisuje je tylko przy włączonym debugowaniu.",
    "The fuel still in the tank. The game knows the number and only prints it as a debug option.":
        "Paliwo, które zostało w zbiorniku. Gra zna tę liczbę i pokazuje ją tylko jako opcję debugowania.",
    "The health the wall or door will have when you build it at your current level.":
        "Wytrzymałość, jaką ta ściana albo drzwi będą miały, gdy zbudujesz je na obecnym poziomie.",
    "The hourly odds of a bang loud enough to pull zombies in.":
        "Szansa na godzinę na huk dość głośny, żeby ściągnąć zombie.",
    "The hourly odds of a fire or an explosion, which set the generator to zero outright.":
        "Szansa na godzinę na pożar albo wybuch, które od razu zerują generator.",
    "The hourly odds of the bait being taken without a catch.":
        "Szansa na godzinę, że przynęta zniknie bez żadnej zdobyczy.",
    "The hourly odds of the trap being wrecked.":
        "Szansa na godzinę, że pułapka zostanie zniszczona.",
    "The hourly odds of the wound becoming infected.":
        "Szansa na godzinę, że rana się zakazi.",
    "The hours of the day the trap actually works.":
        "Godziny doby, w których pułapka faktycznie działa.",
    "The kind of ground the trap is standing on, which decides what can come.":
        "Rodzaj gruntu, na którym stoi pułapka, bo to on decyduje, co może przyjść.",
    "The odds of a bite once every factor is put together.":
        "Szansa na branie, gdy wszystkie czynniki są już zsumowane.",
    "The odds of catching anything at all in an hour.":
        "Szansa na złapanie czegokolwiek w ciągu godziny.",
    "The range of lengths and weights this species comes in.":
        "Zakres długości i wag, w jakim występuje ten gatunek.",
    "The share of your catches that will be junk here.":
        "Jaka część twoich połowów będzie tu śmieciem.",
    "The two things the game never says: a long wait kills the catch, and standing nearby stops the trap.":
        "Dwie rzeczy, których gra nigdy nie mówi: długie czekanie zabija zdobycz, a twoja obecność obok zatrzymuje pułapkę.",
    "The water level as a number, and the amount this seed actually needs.":
        "Poziom wody jako liczba i ilość, której to nasiono naprawdę potrzebuje.",
    "Time to the danger threshold":
        "Czas do progu zagrożenia",
    "Trophy size":
        "Rozmiar trofeum",
    "Warnings":
        "Ostrzeżenia",
    "Warns that the species only bites while you reel in.":
        "Ostrzega, że gatunek bierze tylko wtedy, gdy zwijasz żyłkę.",
    "What a catch has to beat to count as a trophy.":
        "Ile zdobycz musi przekroczyć, żeby liczyła się jako trofeum.",
    "What the herbs in the bandage are adding.":
        "Co dodają zioła w bandażu.",
    "What the same build would have at level {}, which is the reason to know the figure before building.":
        "Ile ta sama budowa miałaby na poziomie {}, i po to właśnie warto znać tę liczbę przed budowaniem.",
    "What the time of day is worth, as the multiplier behind the game's own rating.":
        "Ile warta jest pora dnia, jako mnożnik stojący za oceną samej gry.",
    "What the water temperature is worth, with the actual reading in degrees.":
        "Ile warta jest temperatura wody, wraz z rzeczywistym odczytem w stopniach.",
    "What the weather is worth, as the multiplier behind the game's own rating.":
        "Ile warta jest pogoda, jako mnożnik stojący za oceną samej gry.",
    "What the wind is worth. Past half strength it costs the same penalty fog does, and the two never stack.":
        "Ile wart jest wiatr. Powyżej połowy siły kosztuje tę samą karę co mgła, a te dwie nigdy się nie sumują.",
    "Whether the mains or a generator is keeping the pump running.":
        "Czy pompę utrzymuje w ruchu sieć, czy generator.",
    "Which animals a bait item brings in.":
        "Jakie zwierzęta przyciąga przedmiot użyty jako przynęta.",
    "Which bait is in the trap, and whether it is still fresh.":
        "Jaka przynęta jest w pułapce i czy jest jeszcze świeża.",
    "Which baits work best on this species.":
        "Jakie przynęty działają najlepiej na ten gatunek.",
    "Which growth stage the crop is on, out of the total.":
        "W której fazie wzrostu jest uprawa, z wszystkich.",
    "Which hook is fitted and what it does to your odds.":
        "Jaki haczyk jest założony i co robi z twoimi szansami.",
    "Raw eggs never make you ill":
        "Surowe jajka nigdy ci nie zaszkodzą",
    "{}%% wait before another anti-nausea food works":
        "{}%% czekania, zanim zadziała kolejny środek na mdłości",
    "{}%% weapon sight range":
        "{}%% zasięgu celowników",
    "At Axe {} you swing as fast as a maxed axe user":
        "Przy Siekierze na {} machasz tak szybko jak mistrz",
    "{}%% from any poisonous food or drink":
        "{}%% z każdego trującego jedzenia lub napoju",
    "{}%% chance of illness from rotten food":
        "{}%% szansy na chorobę po zepsutym jedzeniu",
    "Melee weapons":
        "Broń biała",
    "Firearms":
        "Broń palna",
    "Drinks":
        "Napoje",
    "Skill XP":
        "PD umiejętności",
    "Weapons":
        "Broń",
    "Worn and carried":
        "Ubrania i pojemniki",
    "Medicine and reading":
        "Leki i czytanie",
    "Supplies":
        "Zapasy",
    "Comparison":
        "Porównanie",
    "Power and fuel":
        "Prąd i paliwo",
    "Animals and traps":
        "Zwierzęta i pułapki",
    "Traits and jobs":
        "Cechy i zawody",
    "Moodles":
        "Moodle",
}
