"""Turkish phrase table for AllInfo.

Keys are the English fragment with every number replaced by {} in order.
Numbers are never written here: they ride through untouched. Use {0} {1} ...
instead of {} when the language needs a different order -- and then index every
slot, Python refuses to mix the two forms.

Run `python tools\\i18n.py` after editing: it checks the arity of every line and
refuses to write a language file it cannot fill completely.
"""

T = {
    # Per-level skill descriptions
    "x{} weapon damage (x{} untrained)": "x{} silah hasarı (eğitimsizken x{})",
    "{} to the durability roll": "{} dayanıklılık zarına",
    "{} chance to trip vaulting a fence": "{} çitten atlarken tökezleme şansı",
    "{}%% fall damage": "{}%% düşme hasarı",
    "x{} endurance recovery (x{} untrained)": "x{} dayanıklılık yenilenmesi (eğitimsizken x{})",
    "x{} melee damage and knockback (x{} untrained)": "x{} yakın dövüş hasarı ve geri itme (eğitimsizken x{})",
    "x{} carrying capacity (x{} untrained)": "x{} taşıma kapasitesi (eğitimsizken x{})",
    "x{} move speed in combat stance (x{} untrained)": "x{} dövüş duruşunda hareket hızı (eğitimsizken x{})",
    "x{} sprint speed (x{} untrained)": "x{} sprint hızı (eğitimsizken x{})",
    "x{} chance of being spotted (x{} untrained)": "x{} fark edilme şansı (eğitimsizken x{})",
    "x{} footstep noise (x{} untrained)": "x{} ayak sesi (eğitimsizken x{})",
    "{} accuracy (the weapon's aiming modifier, {} on nearly every gun)":
        "{} isabet (silahın nişan çarpanı, neredeyse her silahta {})",
    "{} wind penalty when aiming (of {})": "{} nişan alırken rüzgâr cezası ({} üzerinden)",
    "x{} reload speed (x{} untrained)": "x{} şarjör değiştirme hızı (eğitimsizken x{})",
    "x{} racking speed (x{} untrained)": "x{} kurma hızı (eğitimsizken x{})",
    "racking costs {} of the aiming time ({} untrained)": "kurmak nişan süresinin {} kadarını alır (eğitimsizken {})",
    "From here on you no longer count as unsteady with a firearm, as long as your Strength is {} or more: jam chance drops by {} percentage points.":
        "Bu seviyeden sonra Gücün {} veya üzerindeyse ateşli silahla artık tutuk sayılmazsın: tutukluk şansı {} puan düşer.",
    "You never count as unsteady with a firearm again, whatever your Strength.":
        "Gücün ne olursa olsun ateşli silahla bir daha asla tutuk sayılmazsın.",

    # Moodles
    "{} melee to-hit": "{} yakın dövüş isabeti",
    "{} climb chance": "{} tırmanma şansı",
    "{} trip chance": "{} tökezleme şansı",
    "{} to break a zombie's grab": "{} zombinin kavrayışından kurtulmaya",
    "{}%% strength": "{}%% güç",
    "{}%% healing": "{}%% iyileşme",
    "losing health": "can azalıyor",
    "harder to unjam a gun": "tutukluğu açmak daha zor",
    "{} move speed (of {})": "{} hareket hızı ({} üzerinden)",
    "body at {} C": "vücut sıcaklığı {} C",
    "{} carry capacity": "{} taşıma kapasitesi",
    "x{} attack speed": "x{} saldırı hızı",
    "endurance under {}%%": "dayanıklılık {}%% altında",
    "fatigue over {}%%": "yorgunluk {}%% üstünde",
    "hunger over {}%%": "açlık {}%% üstünde",
    "thirst over {}%%": "susuzluk {}%% üstünde",
    "panic over {}%%": "panik {}%% üstünde",
    "stress over {}%%": "stres {}%% üstünde",
    "boredom over {}%%": "can sıkıntısı {}%% üstünde",
    "unhappiness over {}%%": "mutsuzluk {}%% üstünde",
    "{}%% action speed": "{}%% eylem hızı",
    "anger over {}%%": "öfke {}%% üstünde",
    "drunkenness over {}%%": "sarhoşluk {}%% üstünde",
    "pain over {}%%": "acı {}%% üstünde",
    "slower rope climbing": "ipe tırmanmak daha yavaş",
    "{}%% total body damage": "{}%% toplam vücut hasarı",
    "sickness over {}%%": "hastalık {}%% üstünde",
    "cold strength over {}%%": "soğuk algınlığı şiddeti {}%% üstünde",
    "wetness over {}%%": "ıslaklık {}%% üstünde",
    "discomfort over {}%%": "rahatsızlık {}%% üstünde",
    "rotting corpses nearby": "yakınlarda çürüyen cesetler",
    "x{} move speed": "x{} hareket hızı",
    "{} discomfort per level": "seviye başına {} rahatsızlık",
    "{} C on top of the air temperature": "hava sıcaklığının üstüne {} C",
    "carrying {}x capacity": "kapasitenin {}x katını taşıyorsun",
    "{}%% body heat": "{}%% vücut ısısı",
    "no sleep without pills": "hapsız uyuyamazsın",
    "erratic movement": "düzensiz hareket",
    "raises discomfort": "rahatsızlığı artırır",
    "no sprinting": "sprint yok",
    "no sprinting, no exercise": "sprint yok, egzersiz yok",
    "zombies spot you {} sooner": "zombiler seni {} daha erken fark eder",
    "muscle stiffness builds up": "kas tutulması birikir",
    "cannot eat or open food": "yemek yiyemez ve paket açamazsın",
    "{} move speed with Adrenaline Junkie": "Adrenalin Bağımlısı ile {} hareket hızı",
    "nightmares while asleep": "uykuda kâbuslar",
    "no sleep below {}%% fatigue without pills": "hapsız, yorgunluk {}%% altındayken uyuyamazsın",
    "{}%% move speed": "{}%% hareket hızı",
    "cannot move": "hareket edemezsin",
    "{} climbing walls and ropes": "{} duvar ve ip tırmanışına",
    "no running, no exercise": "koşu yok, egzersiz yok",
    "over {}x capacity": "kapasitenin {}x katının üstünde",
    "no running": "koşu yok",
    "no sprinting until you drop the bulky item": "hantal eşyayı bırakana kadar sprint yok",
    "you can sleep through high pain": "şiddetli acıya rağmen uyuyabilirsin",
    "no endurance recovery": "dayanıklılık yenilenmiyor",
    "{} vision cone": "{} görüş konisi",
    "delayed vehicle controls": "araç kontrolleri gecikmeli",
    "narrowed vision cone": "görüş konisi daralır",
    "no exercise": "egzersiz yok",
    "{} wound bleeding": "{} yara kanıyor",
    "Rest in peace.": "Huzur içinde yat.",
    "Infected. There is no cure.": "Enfekte. Çaresi yok.",

    # Tooltip labels
    "Stale in": "Bayatlamaya",
    "Rots in": "Çürümeye",
    "Cooking time": "Pişme süresi",
    "Never": "Asla",
    "Critical chance": "Kritik şansı",
    "Trains": "Geliştirir",
    "Attack speed": "Saldırı hızı",
    "Swing type": "Vuruş tipi",
    "Heavy": "Ağır",
    "Swung": "Savurma",
    "Stabbing": "Saplama",
    "Spear": "Mızrak",
    "Stone": "Taş",
    "Knockback on hit": "İsabette geri itme",
    "Condition loss": "Durum kaybı",
    "Jam chance": "Tutukluk şansı",
    "Accuracy": "İsabet",
    "Noise radius": "Gürültü yarıçapı",
    "Rounds": "Mermi",
    "Reload time": "Doldurma süresi",
    "Aiming time": "Nişan süresi",
    "Used by": "Kullanan silahlar",
    "Reading speed": "Okuma hızı",
    "Reading time left": "Kalan okuma süresi",
    "Skill too low to learn from it": "Bundan öğrenmek için beceri çok düşük",
    "Nothing left to learn from it": "Bundan öğrenilecek bir şey kalmadı",
    "Proteins": "Protein",
    "Sow in": "Ekim ayları",
    "Ready in": "Hazır olmasına",
    "Burn time": "Yanma süresi",
    # Power: charge, autonomy and light
    "Duration": "Süre",
    "Light range": "Işık menzili",
    "Light strength": "Işık gücü",
    "Batteries and radios: charge left, how long it lasts and how far a torch lights": "Piller ve telsizler: kalan şarj, ne kadar dayandığı ve bir el fenerinin ne kadar aydınlattığı",
    "Vanilla draws the charge of a drainable as a bar with no number on it, and never says how long a torch lasts or how far it lights. A torch spends its UseDelta once every ten game minutes, and only while it is in a hand or attached to you: left in a bag it switches itself off. Light range and strength are the figures that actually light the ground.":
        "Oyun, tükenen bir eşyanın şarjını üzerinde sayı olmayan bir çubuk olarak çizer ve bir el fenerinin ne kadar dayandığını ya da ne kadar uzağı aydınlattığını asla söylemez. El feneri UseDelta değerini her on oyun dakikasında bir harcar ve yalnızca elinde ya da üzerine takılıyken: çantada kendi kendine kapanır. Işık menzili ve gücü, zemini gerçekten aydınlatan sayılardır.",
    "Rest quality": "Dinlenme kalitesi",
    "Discomfort": "Rahatsızlık",
    "Stomp damage": "Ezme hasarı",
    "Corpse sickness defense": "Ceset hastalığına karşı koruma",
    "Filter charge": "Filtre doluluğu",
    "New recipes": "Yeni tarifler",
    "Listened": "Dinlenen",
    "Skill too high for this tape": "Bu kaset için beceri çok yüksek",

    # Options screen
    "All Info": "All Info",
    "Enable everything": "Hepsini aç",
    "Items": "Eşyalar",
    "Crafting": "Üretim",
    "World": "Dünya",
    "Character": "Karakter",
    "Everything in this section": "Bu bölümdeki her şey",
    "Food: time left before it spoils": "Yiyecek: bozulmasına ne kadar kaldı",
    "Adds hours to stale and hours to rotten, at the current rate. Accounts for the fridge, the freezer and the sandbox spoilage speed.":
        "Şu anki hızla bayatlamaya ve çürümeye kaç saat kaldığını gösterir. Buzdolabını, derin dondurucuyu ve sandbox bozulma hızını hesaba katar.",
    "Cooking: add the warm-up minutes": "Pişirme: ısınma dakikalarını ekle",
    "Off by default. Cooking time is the time at temperature; this adds the four minutes the food spends heating up before it starts to cook, so an oven timer set to the figure rings when the food is done.":
        "Varsayılan olarak kapalı. Pişme süresi, yiyecek sıcaklığa ulaştıktan sonrası içindir; bu seçenek yiyeceğin pişmeye başlamadan önce ısınmak için harcadığı dört dakikayı ekler, böylece fırın zamanlayıcısı tam yemek hazır olduğunda çalar.",
    "Food: calories, carbs, protein and fat": "Yiyecek: kalori, karbonhidrat, protein ve yağ",
    "Off by default. Showing macros on every food undoes the Nutritionist trait, which is what normally reveals them.":
        "Varsayılan olarak kapalı. Her yiyecekte besin değerlerini göstermek, normalde bunları açan Beslenme Uzmanı özelliğini anlamsız kılar.",
    "Melee: exact damage, speed and durability": "Yakın dövüş: tam hasar, hız ve dayanıklılık",
    "Puts numbers on the condition and damage bars, and adds crit chance, swing type, attack speed, knockback and the odds of losing a condition point per hit.":
        "Durum ve hasar çubuklarına sayı koyar; kritik şansı, vuruş tipi, saldırı hızı, geri itme ve darbe başına bir durum puanı kaybetme olasılığını ekler.",
    "Firearms: range, jam chance and reload": "Ateşli silahlar: menzil, tutukluk ve doldurma",
    "Puts numbers on the condition and damage bars, and adds accuracy, effective range, jam odds and magazine size.":
        "Durum ve hasar çubuklarına sayı koyar; isabet, etkili menzil, tutukluk olasılığı ve şarjör kapasitesini ekler.",
    "Ammo: rounds left and what it fits": "Mermi: kaç tane kaldı ve nereye uyar",
    "No comparison arrows here: the thing in your hands is a gun, not another magazine, so there is no honest pair to compare.":
        "Burada karşılaştırma oku yok: elindeki bir silah, başka bir şarjör değil, yani karşılaştırılacak dürüst bir çift yok.",
    "Clothing: numbers on every bar, plus discomfort": "Kıyafet: tüm çubuklarda sayılar ve rahatsızlık",
    "Vanilla draws condition, insulation, wind, water, blood, dirt and wetness as bars with no figures. This writes the figures next to them and adds the discomfort value, which vanilla never shows at all.":
        "Oyun; durum, yalıtım, rüzgâr, su, kan, kir ve ıslaklığı sayısız çubuklar olarak çizer. Burada sayılar yanlarına yazılır, ayrıca oyunun hiçbir yerde göstermediği rahatsızlık değeri eklenir.",
    "Seeds: growing time and yield": "Tohum: yetişme süresi ve verim",
    "Firewood: how long it burns": "Odun: ne kadar yanar",
    "Books: reading time and skill levels covered": "Kitaplar: okuma süresi ve kapsadığı seviyeler",
    "Reading time already accounts for Fast Reader, Slow Reader and reading glasses.":
        "Okuma süresi Hızlı Okur, Yavaş Okur ve okuma gözlüğünü zaten hesaba katar.",
    "Beds: how well you recover on them": "Yataklar: üzerlerinde ne kadar iyi dinlenirsin",
    "Masks: filter life and protection": "Maskeler: filtre ömrü ve koruma",
    "Tapes and CDs: which skill they teach and how much XP": "Kaset ve CD'ler: hangi beceriyi öğretir ve ne kadar XP verir",
    "Show the difference against what you have equipped": "Kuşandığınla arasındaki farkı göster",
    "Adds a coloured +/- next to weapon and clothing values. Weapons compare against what is in your hands, clothing against the piece worn in the same slot.":
        "Silah ve kıyafet değerlerinin yanına renkli bir +/- ekler. Silahlar elindekiyle, kıyafetler aynı yerde giyilen parçayla karşılaştırılır.",
    "Crafting: full item tooltip on the recipe output": "Üretim: tarif sonucunda tam eşya bilgisi",
    "Hovering the result of a recipe shows the same block an item in your inventory would, comparison included, before you craft it.":
        "Bir tarifin sonucunun üzerine gelmek, üretmeden önce envanterindeki bir eşyanın göstereceği bloğun aynısını, karşılaştırmasıyla birlikte gösterir.",
    "Generators: fuel time, wear and danger": "Jeneratörler: yakıt süresi, aşınma ve tehlike",
    "Adds noise radius, hours of fuel left, average time until {}%% condition and until it breaks, and the hourly odds of a backfire or a fire.":
        "Gürültü yarıçapını, kalan yakıt saatini, {}%% duruma ve bozulmaya kadar geçen ortalama süreyi ve saatlik geri tepme veya yangın olasılığını ekler.",
    "Generators: also show times in real-world minutes": "Jeneratörler: süreleri gerçek dakika olarak da göster",
    "Off by default. Converts the in-game hours using the current day length, so you know how long you actually have to wait.":
        "Varsayılan olarak kapalı. Oyun içi saatleri şu anki gün uzunluğuna göre çevirir, böylece gerçekte ne kadar bekleyeceğini bilirsin.",
    "Generators: outline the powered area on the floor": "Jeneratörler: beslenen alanı yere çiz",
    "Draws the edge of the range while the generator window is open, green when running and red when off. Only the floor you are standing on is computed.":
        "Jeneratör penceresi açıkken menzilin kenarını çizer: çalışırken yeşil, dururken kırmızı. Yalnızca üzerinde durduğun kat hesaplanır.",
    "Gas pumps: fuel left and power source": "Yakıt pompaları: kalan yakıt ve güç kaynağı",
    "Adds an Info entry to the right-click menu of any gas pump, with the fuel still in the tank and whether the mains or a generator is keeping it running. The game knows that number and only prints it as a debug option.":
        "Herhangi bir yakıt pompasının sağ tık menüsüne bir Bilgi girdisi ekler: depoda kalan yakıt ve pompayı ayakta tutanın şebeke mi yoksa jeneratör mü olduğu. Oyun bu sayıyı biliyor ve yalnızca hata ayıklama seçeneği olarak gösteriyor.",
    "Fuel Remaining": "Kalan yakıt",
    "Mains power": "Şebeke elektriği",
    "Generator": "Jeneratör",
    "Walls and doors: health under the cursor": "Duvar ve kapılar: imlecin altındaki dayanıklılık",
    "Shows current and maximum health as a number at the foot of whatever you point at, no clicking needed.":
        "İşaret ettiğin şeyin dibinde mevcut ve azami dayanıklılığı sayı olarak gösterir, tıklamaya gerek yok.",
    "Build menu: health of what you are about to build": "İnşa menüsü: yapacağın şeyin dayanıklılığı",
    "Also shows what that health would be with the relevant skill at {}, so you can tell whether it is worth waiting.":
        "İlgili beceri {} seviyedeyken bu dayanıklılığın ne olacağını da gösterir, beklemeye değer mi anlarsın.",
    "Crops: health, growth and water as numbers": "Ekinler: sağlık, büyüme ve su sayı olarak",
    "Adds rows to the crop window you get by right-clicking a plant: health out of {}, current phase, hours to the next one, water level against what the plant needs, time since the last watering and pest levels.":
        "Bir bitkiye sağ tıklayınca açılan pencereye satır ekler: {} üzerinden sağlık, mevcut evre, bir sonrakine kalan saat, bitkinin ihtiyacına karşı su seviyesi, son sulamadan bu yana geçen süre ve her zararlının seviyesi.",
    "Crops: keep vanilla's Farming level requirements": "Ekinler: oyunun Tarım seviye şartlarını koru",
    "Off by default, so you see everything from level {}. Turn it on and each row reappears at the Farming level vanilla itself uses for it: phase and health at {}, water at {}, pests at {}, next phase at {}.":
        "Varsayılan olarak kapalı, yani her şeyi {} seviyeden itibaren görürsün. Açarsan her satır oyunun kendi kullandığı Tarım seviyesinde geri gelir: evre ve sağlık {}, su {}, zararlılar {}, sonraki evre {}.",
    "Noise": "Gürültü",
    "tiles": "kare",
    "Down to %1%% (avg)": "%1%% seviyesine (ort.)",
    "Breaks down in (avg)": "Bozulmasına (ort.)",
    "Backfire, loud (per hour)": "Geri tepme, gürültülü (saatlik)",
    "FIRE OR EXPLOSION (per hour)": "YANGIN VEYA PATLAMA (saatlik)",
    "(real time)": "(gerçek zaman)",
    "XP Boost: %1": "XP Katsayısı: %1",
    "Skills": "Beceriler",
    "Also grants": "Ayrıca verir",
    "Disabled in multiplayer": "Çok oyuncuda devre dışı",
    "Foraging": "Toplayıcılık",
    "search radius": "arama yarıçapı",
    "weather penalty": "hava cezası",
    "darkness penalty": "karanlık cezası",
    "Strength when built": "İnşa edildiğindeki dayanıklılık",
    "With %1 at {}": "%1 {} seviyedeyken",
    "Show XP boosts as a multiplier, not a percentage": "XP katsayılarını yüzde değil çarpan olarak göster",
    'Vanilla says "{}%%" for a level {} boost. The real figure is x{}, because a skill with no boost runs at a quarter rate. Fixed on all three screens that show it.':
        'Oyun {} seviyelik bir katsayı için "{}%%" yazar. Gerçek değer x{}, çünkü katsayısı olmayan bir beceri çeyrek hızla ilerler. Bunu gösteren üç ekranda da düzeltildi.',
    "Character creation: what each trait and job really does": "Karakter oluşturma: her özellik ve meslek gerçekte ne yapar",
    "Adds starting skill levels with their true XP multiplier, free traits granted, recipes taught and foraging bonuses to the tooltips in the creation screen.":
        "Oluşturma ekranındaki ipuçlarına başlangıç beceri seviyelerini gerçek XP çarpanıyla, bedava verilen özellikleri, öğretilen tarifleri ve toplayıcılık bonuslarını ekler.",
    "In game: the same block on the info tab": "Oyunda: bilgi sekmesinde aynı blok",
    "Hover a trait icon or the job icon in the character info tab to read the same block after the world has started.":
        "Dünya başladıktan sonra aynı bloğu okumak için karakter bilgi sekmesindeki bir özellik veya meslek simgesinin üzerine gel.",
    "Add hand-written trait effects": "Elle yazılmış özellik etkilerini ekle",
    "Effects hardcoded in the game's Java that cannot be read at runtime, so they are written by hand and checked against each build.":
        "Oyunun Java kodunda sabitlenmiş, çalışma anında okunamayan etkiler; bu yüzden elle yazılır ve her sürüme karşı denetlenir.",
    "Skills: which recipes each level requires": "Beceriler: her seviye hangi tarifler için gerekli",
    "Hover a level in the skills panel to see the recipes and builds that ask for it. Read from the game's own recipe list, so modded recipes appear too and nothing goes stale with a patch.":
        "Beceriler panelinde bir seviyenin üzerine gelerek onu isteyen tarifleri ve yapıları gör. Oyunun kendi tarif listesinden okunur, bu yüzden diğer modların tarifleri de görünür ve hiçbir şey yamayla eskimez.",
    "Needs this level": "Bu seviyeyi ister",
    "Skill and moodle descriptions are translation files. They cannot be switched off here; disable the mod to remove them.":
        "Beceri ve moodle açıklamaları çeviri dosyalarıdır. Buradan kapatılamaz; kaldırmak için modu devre dışı bırak.",
    "Run self-test": "Otomatik testi çalıştır",

    # Trait and profession effects
    "{}%% footstep noise radius": "{}%% ayak sesi yarıçapı",
    "more likely to fall when bumped": "çarpıldığında daha kolay düşersin",
    "less likely to fall when bumped": "çarpıldığında daha zor düşersin",
    "{}%% run and sprint speed": "{}%% koşu ve sprint hızı",
    "no Fitness XP from level {} on": "{} seviyeden itibaren Kondisyon XP'si yok",
    "double endurance drain when running": "koşarken iki katı dayanıklılık harcar",
    "{}%% melee damage": "{}%% yakın dövüş hasarı",
    "{} chance to trip from a lunge": "{} hamlede tökezleme şansı",
    "starts at {} weight, and you lose health below {}": "{} kiloyla başlar ve {} altında can kaybedersin",
    "{}%% axe swing time": "{}%% balta vuruş süresi",
    "{}%% axe damage to trees": "ağaçlara {}%% balta hasarı",
    "{}%% endurance lost running": "koşarken {}%% dayanıklılık kaybı",
    "{}%% grapple effectiveness": "{}%% boğuşma etkinliği",
    "{}%% knockback": "{}%% geri itme",
    "can be gained by training Strength to {}": "Gücü {} seviyeye çıkararak kazanılır",
    "becomes Strong at Strength {}": "Güç {} olunca Güçlü'ye dönüşür",
    "becomes Feeble at Strength {}": "Güç {} olunca Cılız'a dönüşür",
    "lost by training Strength to {}": "Gücü {} seviyeye çıkarınca kaybolur",
    "{}%% panic, night terrors aside": "{}%% panik, gece korkuları hariç",
    "{}%% stress from looting corpses": "ceset aramaktan {}%% stres",
    "{}%% panic": "{}%% panik",
    "no panic from a corpse reanimating": "bir ceset canlandığında panik yok",
    "no stress from looting corpses": "ceset aramak stres vermez",
    "{} move speed at panic {}": "panik {1} iken {0} hareket hızı",
    "still capped by the movement speed limit": "yine de hareket hızı üst sınırıyla kısıtlı",
    "{}%% wind penalty when aiming": "nişan alırken {}%% rüzgâr cezası",
    "{}%% gun accuracy": "{}%% ateşli silah isabeti",
    "{}%% gun crit chance": "{}%% ateşli silah kritik şansı",
    "shorter aiming delay": "daha kısa nişan gecikmesi",
    "wider field of view": "daha geniş görüş alanı",
    "{}%% max range on weapon sights": "dürbünlerde {}%% azami menzil",
    "blurry vision": "bulanık görüş",
    "weapon sight range bonus at its minimum": "dürbün menzil bonusu asgaride",
    "cancelled by wearing glasses": "gözlük takınca ortadan kalkar",
    "{}%% perception radius": "{}%% algı yarıçapı",
    "zombies behind you become visible sooner": "arkandaki zombiler daha erken görünür",
    "muffled sound effects": "boğuk sesler",
    "zombies behind you become visible later": "arkandaki zombiler daha geç görünür",
    "no sound at all": "hiç ses yok",
    "you can still watch TV": "yine de televizyon izleyebilirsin",
    "{}%% chance of not being injured by a zombie": "bir zombiden yaralanmama şansı {}%%",
    "{}%% chance of being scratched by trees": "ağaçlarda çizilme şansı {}%%",
    "{}%% corpse sickness": "{}%% ceset hastalığı",
    "{}%% chance of catching a cold": "{}%% soğuk algınlığına yakalanma şansı",
    "{}%% cold strength": "{}%% soğuk algınlığı şiddeti",
    "{}%% cold progression": "{}%% soğuk algınlığı ilerlemesi",
    "{}%% zombification speed": "{}%% zombileşme hızı",
    "{}%% severity of vehicle injuries": "{}%% araç yaralanmalarının şiddeti",
    "{}%% fracture severity": "{}%% kırık şiddeti",
    "all wounds heal much faster": "tüm yaralar çok daha hızlı iyileşir",
    "all wounds heal much slower": "tüm yaralar çok daha yavaş iyileşir",
    "{}%% XP in every skill except Fitness and Strength": "Kondisyon ve Güç dışındaki tüm becerilerde {}%% XP",
    "{}%% reading speed": "{}%% okuma hızı",
    "{}%% XP in every weapon skill and Aiming": "tüm silah becerilerinde ve Nişancılıkta {}%% XP",
    "{}%% inventory transfer time": "{}%% eşya taşıma süresi",
    "{}%% aiming delay": "{}%% nişan gecikmesi",
    "guns jam less often": "silahlar daha az tutukluk yapar",
    "fewer injuries opening cans": "konserve açarken daha az yaralanma",
    "guns jam more often": "silahlar daha sık tutukluk yapar",
    "more injuries opening cans": "konserve açarken daha çok yaralanma",
    "{}%% container capacity": "{}%% kap kapasitesi",
    "crafting does not return leftover items": "üretim artan malzemeleri geri vermez",
    "{}%% thirst": "{}%% susuzluk",
    "{}%% hunger": "{}%% açlık",
    "{}%% food illness chance": "{}%% gıda zehirlenmesi şansı",
    "{}%% food illness duration": "{}%% gıda zehirlenmesi süresi",
    "{}%% harm from tainted water": "kirli sudan {}%% zarar",
    "{}%% tiredness gained while awake": "uyanıkken biriken {}%% yorgunluk",
    "{}%% recovery while asleep": "uykuda {}%% dinlenme",
    "{}%% sleep duration": "{}%% uyku süresi",
    "you do not wake up at {} tiredness, so set an alarm": "{} yorgunlukta uyanmazsın, o yüzden alarm kur",
    "harder to fall asleep": "uykuya dalmak daha zor",
    "{}%% vision in the dark": "karanlıkta {}%% görüş",
    "smaller vision cone penalty at night": "geceleri görüş konisi cezası daha küçük",
    "{}%% chance of being spotted (new stealth)": "{}%% fark edilme şansı (yeni gizlilik)",
    "{}%% chance of being spotted (old stealth)": "{}%% fark edilme şansı (eski gizlilik)",
    "{}%% chance of breaking kindling": "çıra kırma şansı {}%%",
    "{}%% weather penalty when aiming": "nişan alırken {}%% hava cezası",
    "lights fires twice as fast": "ateşi iki kat hızlı yakar",
    "almost never scratched by trees": "ağaçlar neredeyse hiç çizmez",
    "{}%% endurance lost running, sprinting, carrying and dragging":
        "koşarken, sprint atarken, taşırken ve sürüklerken {}%% dayanıklılık kaybı",
    "{}%% endurance lost swinging a weapon": "silah savururken {}%% dayanıklılık kaybı",
    "{}%% gear change speed": "{}%% vites değiştirme hızı",
    "{}%% top speed": "{}%% azami hız",
    "{}%% engine noise in reverse": "geri viteste {}%% motor gürültüsü",
    "{}%% acceleration": "{}%% hızlanma",
    "{}%% reverse acceleration": "geri viteste {}%% hızlanma",
    "capped at {} max speed": "azami hız {} ile sınırlı",
    "engine noise unchanged": "motor gürültüsü değişmez",
    "less likely to fail any fence climb": "herhangi bir çiti aşarken daha az başarısız olur",
    "slightly faster rope climbing": "ipe tırmanmak biraz daha hızlı",
    "bloody items transfer faster but cause stress": "kanlı eşyalar daha hızlı taşınır ama stres verir",
    "cannot read anything, map labels and calorie counts included":
        "hiçbir şey okuyamazsın, harita etiketleri ve kalori değerleri dâhil",
    "{} panic per tick indoors, scaling down to {} in a {}-tile room":
        "kapalı alanda tick başına {0} panik, {2} kare büyüklüğünde bir odada {1} seviyesine iner",
    "a vehicle counts as a {}-tile room": "bir araç {} karelik bir oda sayılır",
    "{} panic per tick whenever you are not in a room": "bir odada değilken tick başına {} panik",
    "faster building": "daha hızlı inşa",
    "faster barricading": "daha hızlı barikatlama",
    "no bonus health on constructions in B{}": "B{} sürümünde yapılara ek dayanıklılık vermez",
    "recipes need one level less of their skill": "tarifler becerilerinin bir seviye altını ister",
    "you gain weight above {} calories a day instead of {}, while under {} weight":
        "kilon {2} altındayken günde {1} yerine {0} kalorinin üstünde kilo alırsın",
    "you need {} calories a day to gain weight instead of {}, while over {} weight":
        "kilon {2} üstündeyken kilo almak için günde {1} yerine {0} kalori gerekir",
    "unhappiness and stress rise as nicotine withdrawal builds":
        "nikotin yoksunluğu arttıkça mutsuzluk ve stres yükselir",
    "smoking clears the withdrawal and gives {} hunger": "sigara yoksunluğu giderir ve {} açlık verir",
    "random coughs and sneezes give you away": "rastgele öksürük ve hapşırıklar seni ele verir",
    "shows calories, carbohydrates, protein and fat on every food":
        "her yiyecekte kalori, karbonhidrat, protein ve yağı gösterir",
    "no measurable effect in B{}: no XP boost, no recipes, and nothing in the game's code reads it. The recipes come from the profession itself.":
        "B{} sürümünde ölçülebilir bir etkisi yok: XP katsayısı yok, tarif yok ve oyunun kodunda onu okuyan hiçbir yer yok. Tarifler mesleğin kendisinden gelir.",
    "x{} move speed through trees (x{} for everyone else)": "ağaçların arasında x{} hareket hızı (herkes için x{})",
    "starts every exercise at {}{} regularity instead of {}{}":
        "her egzersize {}{} düzenlilikle başlar, {}{} yerine",
    '{} move speed':
        '{} hareket hızı',
    '{} wind penalty when aiming':
        '{} nişan alırken rüzgâr cezası',
    '%1 °C':
        '%1 °C',
    'Adds rows to the inventory tooltip: how fast a line wears out, how much each hook helps and which fish a bait attracts.':
        'Envanter ipucuna satırlar ekler: misina ne kadar hızlı yıpranır, her olta iğnesi ne kadar yardım eder ve bir yem hangi balıkları çeker.',
    'ALLTHEINFO':
        'ALLTHEINFO',
    'Attracts':
        'Çeker',
    "Back to vanilla's rules: Time needs Fishing {}, Temperature {}, Weather {}, Wind {}, and a species tells you nothing until you have caught it.":
        'Oyunun kurallarına dönüş: saat Balıkçılık {}, sıcaklık {}, hava {}, rüzgar {} ister ve bir türü yakalayana kadar hiçbir şey söylemez.',
    'Best baits: %1':
        'En iyi yemler: %1',
    'Bite chance':
        'Vurma şansı',
    'Breaks into':
        'Kırılınca olur',
    'Chance that one attempt hooks something: {}%% times temperature, weather, time, hook and abundance, capped at {}%%.':
        'Bir denemenin bir şey yakalama şansı: {}%% çarpı sıcaklık, hava, saat, iğne ve balık bolluğu, en fazla {}%%.',
    'Fish bite more at dawn and dusk: x{} from {}:{} to {}:{} and from {}:{} to {}:{}. Any other hour is x{}.':
        'Balıklar şafakta ve gün batımında daha çok vurur: {}:{} - {}:{} ve {}:{} - {}:{} arası x{}. Diğer her saat x{}.',
    'Fishing gear: rods, lines, hooks and baits':
        'Balıkçılık takımı: oltalar, misinalar, iğneler ve yemler',
    'Fishing panel: what each rating is worth':
        'Balıkçılık paneli: her değerlendirme ne demek',
    "Fishing: keep vanilla's Fishing level requirements":
        'Balıkçılık: oyunun Balıkçılık seviye şartlarını koru',
    'Hook':
        'İğne',
    'How much longer than the best possible case you wait between attempts. Fishing near the shore doubles it, and a bobber less than {} tiles away triples it.':
        'Denemeler arasında mümkün olan en iyi duruma göre ne kadar fazla beklediğin. Kıyıya yakın balık tutmak bunu ikiye katlar, {} kareden yakın bir şamındıra ise üçe.',
    'Lake':
        'Göl',
    'Line strength':
        'Misina dayanımı',
    'Moodles: description box that fits its text':
        'Moodle: metne sığan açıklama kutusu',
    'Needs Fishing %1':
        'Balıkçılık %1 ister',
    'Only bites while you reel in':
        'Sadece misinayı sararken vurur',
    'Paperclip x{}, nail x{}, fishing hook x{}. With no hook the chance is x{}: nothing will ever bite.':
        'Ataş x{}, çivi x{}, olta iğnesi x{}. İğne yoksa şans x{}: hiçbir şey vurmaz.',
    'Rain is x{}. Fog over {} or wind over {} is x{}. Fog and wind are the same x{}: they never stack.':
        'Yağmur x{}. {} üzeri sis ya da {} üzeri rüzgar x{}. Sis ve rüzgar aynı x{}: asla toplanmazlar.',
    'Right-click water and pick Fishing. Puts the real multiplier next to Time, Temperature, Weather and Wind, adds hook, spot, bite chance and waiting time, and explains each one on hover.':
        "Suya sağ tıklayıp Balık Tut'u seç. Saat, sıcaklık, hava ve rüzgarın yanına gerçek çarpanı yazar; iğne, mevki, vurma şansı ve bekleme süresi ekler ve üzerine gelince her birini açıklar.",
    'River':
        'Nehir',
    'Spot':
        'Mevki',
    "The game's own moodle box is two lines tall and cuts off anything longer, which is most of AllTheInfo's descriptions. This draws the moodle column itself so the box grows with the text. Turn it off to go back to the vanilla widget.":
        "Oyunun moodle kutusu iki satır yüksekliğinde ve daha uzun olan her şeyi keser, ki bu AllTheInfo açıklamalarının neredeyse tamamıdır. Burada moodle sütununu mod çizer, böylece kutu metinle birlikte büyür. Kapatırsan oyunun kendi widget'ı geri gelir.",
    'Trophy from %1 cm, Fishing {} and a {} in {} roll on a big catch':
        "%1 cm'den itibaren kupalık, Balıkçılık {} ve büyük bir avda {} zarda {} atışıyla",
    'Under {} fish is x{}, up to {} is x{}, over {} is x{}. Trash is what you pull out instead of a fish, and Fishing {} cuts it to {}%%, level {} to {}%% and level {} to {}%%.':
        '{} balıktan az x{}, {} kadar x{}, {} üzeri x{}. Çöp, balık yerine çıkardığın şeydir ve Balıkçılık {} bunu {}%% seviyesine, {} seviyesi {}%% seviyesine ve {} seviyesi {}%% seviyesine düşürür.',
    'Up to %1 cm and %2 kg':
        "%1 cm ve %2 kg'a kadar",
    'Vanilla draws condition, insulation, wind, water, blood, dirt and wetness as bars with no figures. This writes the figures next to them and adds the discomfort value, which vanilla never shows at all. The run and combat speed modifiers get a signed figure too, which vanilla only ever draws as a bar with no sign.':
        'Oyun durumu, yalıtımı, rüzgarı, suyu, kanı, kiri ve ıslaklığı rakamsız çubuklar olarak çizer. Burada rakamlar yanlarına yazılır, artı oyunun hiç göstermediği rahatsızlık değeri. Koşma ve dövüş hızı değiştiricileri de işaretli bir rakam alır; oyun onları yalnızca işaretsiz bir çubuk olarak çizer.',
    'Wait':
        'Bekleme',
    'Waters: %1':
        'Sular: %1',
    'Wear per tug':
        'Çekiş başına aşınma',
    'Wind has no coefficient of its own. Over {} it sets the weather to x{}, the same penalty fog sets, and the two do not add up.':
        'Rüzgarın kendi katsayısı yoktur. {} üzerinde havayı x{} yapar, sisin verdiği cezanın aynısı, ve ikisi toplanmaz.',
    'With your bait: %1%%':
        'Yeminle: %1%%',
    'Your bait does not attract this one':
        'Yemin bu türü çekmiyor',
    'best possible':
        'mümkün olan en iyisi',
    'near shore':
        'kıyıya yakın',
    'no fish in this spot':
        'burada balık yok',
    'none':
        'yok',
    'trash':
        'çöp',
    '{} to {} °C is x{}. From {} to {} and from {} to {}, x{}. Over {} or below {}, x{}. Below {} °C, x{}.':
        '{} ile {} °C arası x{}. {} ile {} arası ve {} ile {} arası x{}. {} üzeri ya da {} altı x{}. {} °C altı x{}.',
    'Fish':
        'Balık',
    'Trash':
        'Çöp',
    'Trophy from %1 cm':
        "%1 cm'den itibaren kupalık",
    'shore':
        'kıyı',
    'Best baits:':
        'En iyi yemler:',
    'Size: %1-%2 cm, %3-%4 kg':
        'Boyut: %1-%2 cm, %3-%4 kg',
    'Trophy: >%1 cm / >%2 kg':
        'Kupalık: >%1 cm / >%2 kg',
    'Under {} fish is x{}, up to {} is x{}, over {} is x{}. Fish schools move every day. Trash is what you pull out instead of a fish: it is fixed per spot, and Fishing {} cuts it to {}%%, level {} to {}%% and level {} to {}%%.':
        '{} balıktan az x{}, {} kadar x{}, {} üzeri x{}. Balık sürüleri her gün yer değiştirir. Çöp, balık yerine çıkardığın şeydir: her mevkide sabittir ve Balıkçılık {} bunu {}%% seviyesine, {} seviyesi {}%% seviyesine ve {} seviyesi {}%% seviyesine düşürür.',
    'Fishing gear: hide the combat stats':
        'Balıkçılık takımı: dövüş verilerini gizle',
    "Fog over {}%% sets the weather to x{}, the same penalty wind sets, and the two never stack. Vanilla's Weather row reports neither: it says Good for rain even in a gale.":
        '{}%% üzeri sis havayı x{} yapar, rüzgarın verdiği cezanın aynısı, ve ikisi asla toplanmaz. Oyunun hava satırı ikisini de bildirmez: fırtınada bile yağmur için İyi yazar.',
    'Rain is x{}. Fog over {}%% or wind over {}%% is x{}. Fog and wind are the same x{}: they never stack.':
        'Yağmur x{}. {}%% üzeri sis ya da {}%% üzeri rüzgar x{}. Sis ve rüzgar aynı x{}: asla toplanmazlar.',
    "Rods, nets and fishing spears are weapons in the game's own scripts, so they get crit chance, swing type, attack speed and knockback. This drops that block on fishing gear. The condition and damage bars are drawn by the game in one call and cannot be removed by any mod.":
        'Oltalar, ağlar ve zıpkınlar oyunun kendi betiklerinde silahtır, bu yüzden kritik şansı, vuruş tipi, saldırı hızı ve itme değeri alırlar. Bu seçenek balıkçılık takımında o bölümü kaldırır. Durum ve hasar çubuklarını oyun tek seferde çizer; hiçbir mod onları kaldıramaz.',
    'Wind has no coefficient of its own. Over {}%% it sets the weather to x{}, the same penalty fog sets, and the two do not add up.':
        'Rüzgarın kendi katsayısı yoktur. {}%% üzerinde havayı x{} yapar, sisin verdiği cezanın aynısı, ve ikisi toplanmaz.',
    'Against the best possible case':
        'Mümkün olan en iyi duruma göre',
    'Any other hour: x{}':
        'Diğer her saat: x{}',
    'Below {} °C: x{}':
        '{} °C altı: x{}',
    'Bobber under {} tiles away: x{}':
        'Şamandıra {} kareden yakın: x{}',
    'Capped at {}%%':
        'En fazla {}%%',
    'Fishing hook: x{}':
        'Olta iğnesi: x{}',
    'Fishing {}, {} and {} cut trash to {}%%, {}%% and {}%%':
        'Balıkçılık {}, {} ve {} çöpü {}%%, {}%% ve {}%% seviyesine düşürür',
    'Fog and wind never stack':
        'Sis ve rüzgar asla toplanmaz',
    'Fog over {}%% or wind over {}%%: x{}':
        '{}%% üzeri sis ya da {}%% üzeri rüzgar: x{}',
    'Nail: x{}':
        'Çivi: x{}',
    'Near shore: x{}':
        'Kıyıya yakın: x{}',
    'No hook: x{}, nothing ever bites':
        'İğne yok: x{}, hiçbir şey vurmaz',
    'Over {} or below {} °C: x{}':
        '{} üzeri ya da {} °C altı: x{}',
    'Over {}%%: x{} on the weather':
        '{}%% üzeri: havaya x{}',
    'Over {}: x{}':
        '{} üzeri: x{}',
    'Paperclip: x{}':
        'Ataş: x{}',
    'Rain: x{}':
        'Yağmur: x{}',
    'Rolled once per attempt':
        'Her denemede bir kez atılır',
    'Same penalty as fog, they never stack':
        'Sisle aynı ceza, asla toplanmazlar',
    'Same penalty as wind, they never stack':
        'Rüzgarla aynı ceza, asla toplanmazlar',
    'Schools move every day':
        'Sürüler her gün yer değiştirir',
    'This row reports neither':
        'Bu satır ikisini de bildirmez',
    'Trash is fixed per spot':
        'Çöp her mevkide sabittir',
    'Under {} fish: x{}':
        '{} balıktan az: x{}',
    '{} to {} and {} to {} °C: x{}':
        '{} ile {} arası ve {} ile {} arası °C: x{}',
    '{} to {} °C: x{}':
        '{} ile {} °C arası: x{}',
    '{} to {}: x{}':
        '{} ile {} arası: x{}',
    '{}%% x temperature x weather x time x hook x fish':
        '{}%% x sıcaklık x hava x saat x iğne x balık',
    '{}:{} to {}:{} and {}:{} to {}:{}: x{}':
        '{}:{} - {}:{} ve {}:{} - {}:{} arası: x{}',
    'Fishing {}, {} and {}: trash x{}, x{}, x{}':
        'Balıkçılık {}, {} ve {}: çöp x{}, x{}, x{}',
    'x time x hook x fish':
        'x saat x iğne x balık',
    '{}%% x temperature x weather':
        '{}%% x sıcaklık x hava',

    # Round 11: moodles rewritten from bytecode + wiki
    "melee damage {}%%": "{}%% yakın dövüş hasarı",
    "melee damage {}": "{} yakın dövüş hasarı",
    "move speed {}%%": "{}%% hareket hızı",
    "move speed {}%% with Adrenaline Junkie": "Adrenalin Bağımlısı ile {}%% hareket hızı",
    "attack speed {}%%": "{}%% saldırı hızı",
    "combat speed {}%%": "{}%% çatışma hızı",
    "run speed {}%%": "{}%% koşu hızı",
    "crit chance {}%%": "{}%% kritik şansı",
    "firearm accuracy {}%%": "{}%% ateşli silah isabeti",
    "firearm accuracy {}%% at {} tiles": "{0}%% kare mesafede {1} ateşli silah isabeti",
    "clearing a jam {}%%": "{}%% tutukluk giderme şansı",
    "climbing {}%%": "{}%% tırmanma",
    "climbing fences {}%%": "{}%% çit tırmanma",
    "climbing walls and ropes {}%%": "{}%% duvar ve ip tırmanma",
    "tripping over fences {}%%": "{}%% çitte tökezleme şansı",
    "blocking an attack {}%%": "{}%% saldırı bloklama",
    "foraging {}%%": "{}%% yiyecek arama",
    "carry capacity {}": "{} taşıma kapasitesi",
    "healing {}%%": "{}%% iyileşme",
    "healing x{}": "x{} iyileşme",
    "poison wears off {}%% faster": "Zehir {}%% daha hızlı geçer",
    "heat dissipation {}%%": "{}%% ısı atımı",
    "heat loss {}%%": "{}%% ısı kaybı",
    "discomfort {}%%": "{}%% rahatsızlık",
    "medicine {}%% less effective": "İlaçlar {}%% daha az etkili",
    "sleep {}{}%% less effective": "Uyku {0}{1}%% daha az etkili",
    "panic x{} per wound": "yara başına x{} panik",
    "over {}%% of capacity": "Kapasitenin {}%% üzerinde",
    "health under {}%%": "Can {}%% altında",
    "health {}%% per hour": "Saatte {}%% can",
    "health drops to {}%%": "Can {}%% seviyesine düşer",
    "health drops to {}%%, then to {}%%": "Can {0}%% seviyesine, sonra {1}%% seviyesine düşer",
    "health drops to {}%% when the air is above {} C": "Hava {1} C üzerinde olduğunda can {0}%% seviyesine düşer",
    "health drops when the air is below {} C": "Hava {} C altında olduğunda can düşer",
    "only heals indoors, dry, under {}%% fatigue and under {}%% hunger and thirst": "Sadece kapalı alanda, kuru, {}%% altında yorgunluk ve {}%% altında açlık ve susuzlukla geçer",
    "vision cone narrows, cancelling Eagle Eyed": "Görüş konisi daralir ve Kartal Görüşlü özelliğini iptal eder",
    "{} C colder than the air": "Havadan {} C daha soğuk",
    "{} wounds bleeding": "{} yara kanıyor",
    "{} wounds, or a bleeding neck": "{} yara veya boyunda kanama",
    "no healing": "İyileşme yok",
    "no natural healing": "Doğal iyileşme yok",
    "slower healing": "Daha yavaş iyileşme",
    "much slower healing": "Çok daha yavaş iyileşme",
    "slower endurance recovery": "Dayanıklılık daha yavaş dolar",
    "much slower endurance recovery": "Dayanıklılık çok daha yavaş dolar",
    "endurance barely recovers": "Dayanıklılık neredeyse dolmuyor",
    "endurance drains as you move and never recovers": "Hareket ettikçe dayanıklılık düşer ve dolmaz",
    "no sprinting or running": "Ne sprint ne koşu",
    "you cannot run": "Koşamazsın",
    "you cannot sleep": "Uyuyamazsın",
    "you cannot eat any more": "Daha fazla yiyemezsin",
    "you can sleep on the ground and through pain": "Yerde ve ağrıya rağmen uyuyabilirsin",
    "cannot swing a sledgehammer": "Balyoz sallayamazsın",
    "hunger does not rise": "Açlık artmaz",
    "less body heat generated": "Daha az vücut ısısı üretilir",
    "body heat rises": "Vücut ısısı yükselir",
    "body heat rises sharply": "Vücut ısısı hızla yükselir",
    "thirst and fatigue rise faster": "Susuzluk ve yorgunluk daha hızlı artar",
    "you lose heat in the cold": "Soğukta ısı kaybedersin",
    "more likely to catch a cold": "Soğuk algınlığı riski artar",
    "more likely to fall ill": "Hastalanma riski artar",
    "much more likely to fall ill": "Hastalanma riski çok artar",
    "narrower vision cone": "Görüş konisi daralır",
    "narrower vision and awareness": "Görüş ve farkındalık azalır",
    "movement, damage and attack speed drop with the wound": "Hareket, hasar ve saldırı hızı yaraya göre düşer",
    "you make noise": "Ses çıkarırsın",
    "you complain out loud": "Yüksek sesle yakınırsın",
    "you get up faster": "Daha hızlı kalkarsın",
    "you weave as you walk": "Yürürken yalpalarsın",
    "timed actions take longer": "İşlemler daha uzun sürer",
    "unhappiness rises": "Mutsuzluk artar",
    "unhappiness rises slowly": "Mutsuzluk yavaşça artar",
    "unhappiness rises fast": "Mutsuzluk hızla artar",
    "stress rises": "Stres artar",
    "boredom is wiped and held down": "Sıkıntı sıfırlanır ve artmaz",
    "the Desensitized trait cancels it": "Duyarsız özelliği bunu iptal eder",
    "no effect until NPCs return": "NPC'ler dönene kadar etkisiz",
    "discomfort while in a vehicle": "Araçtayken rahatsızlık",
    "hypothermia is hidden": "Hipotermi gizlenir",
    "it wakes you up": "Seni uyandırır",
    "you sneeze now and then": "Ara sıra hapşırırsın",
    "you sneeze and cough often": "Sık sık hapşırır ve öksürürsün",
    "you cough so much that hiding gets hard": "O kadar öksürürsün ki saklanmak zorlaşır",
    "you cough constantly and draw zombies": "Sürekli öksürür ve zombileri çekersin",
    "health loss": "Can kaybı",
    "slow health loss": "Yavaş can kaybı",
    "serious health loss": "Ciddi can kaybı",
    "health slowly drops": "Can yavaşça düşer",
    "health drops if this is infection or poison": "Enfeksiyon veya zehirse can düşer",
    "death without first aid": "İlk yardım olmadan ölüm",
    "sickness starts to build": "Hastalık birikmeye başlar",
    "sickness builds noticeably": "Hastalık gözle görülür şekilde birikir",
    "many rotting corpses": "Çok sayıda çürüyen ceset",
    "more rotting corpses": "Daha fazla çürüyen ceset",
    "the worst corpses can do": "Cesetlerin yapabileceği en kötüsü",
    "a generator running indoors": "İçeride çalışan bir jeneratör",
    "it will not kill you outright": "Seni doğrudan öldürmez",
    "a gas mask or SCBA prevents it": "Gaz maskesi veya solunum cihazı bunu önler",
    "caused by heavy clothing, bags, bare feet or leg injuries": "Ağır kıyafet, çanta, çıplak ayak veya bacak yarası yüzünden",

    # Animals (round 10, block C)
    "Animals: butchering yield, milk, wool and old age":
        "Hayvanlar: et verimi, süt, yün ve yaşlılık",
    "Adds rows to the animal window you get by right-clicking an animal: meat yield, blood, feathers, old age and weight ceiling, which no screen shows, plus health, hunger, thirst, attitude, milk, wool and pregnancy as numbers instead of words.":
        "Bir hayvana sağ tıklayınca açılan pencereye satırlar ekler: hiçbir ekranda görünmeyen et verimi, kan, tüy, yaşlılık ve azami ağırlık; ayrıca sağlık, açlık, susuzluk, tavır, süt, yün ve gebelik kelime yerine sayı olarak.",
    "Animals: keep vanilla's Animal Care level requirements":
        "Hayvanlar: oyunun Hayvan Bakımı seviye koşullarını koru",
    "Off by default, so you see everything from level {}. Turn it on and each row reappears at the Animal Care level vanilla itself uses for it: pregnancy at {}, weight at {}, attitude at {}.":
        "Varsayılan olarak kapalı, yani her şeyi {} seviyesinden itibaren görürsün. Açtığında her satır oyunun kendi kullandığı Hayvan Bakımı seviyesinde geri gelir: gebelik {}, ağırlık {}, tavır {}.",
    "Meat yield":
        "Et verimi",
    "full in %1":
        "%1 içinde dolar",

    # Animal hover descriptions (round 12)
    "Size x meat gene.":
        "Boyut x et geni.",
    "Multiplies the number of meat pieces and the calories of each one.":
        "Hem et parçası sayısını hem de her parçanın kalorisini çarpar.",
    "Butchering adds x{} every {} levels.":
        "Kasaplık her {} seviyede x{} ekler.",
    "Off the ground x{}, on a butcher hook x{}.":
        "Yerde x{}, kasap kancasında x{}.",
    "Litres you can drain into a bucket once it is dead.":
        "Öldükten sonra kovaya boşaltabileceğin litre.",
    "Grows with weight.":
        "Ağırlıkla birlikte artar.",
    "Feathers you get for butchering it.":
        "Onu kesip parçalayınca aldığın tüyler.",
    "Breed maximum x size.":
        "Irk azamisi x boyut.",
    "{}%% until {}%% of its life expectancy, then it climbs to {}%%.":
        "Ömrünün {}%% ine kadar {}%%, sonra {}%% e kadar tırmanır.",
    "Over {}%% it loses {}%% health every hour.":
        "{}%% üzerinde her saat {}%% sağlık kaybeder.",
    "Current weight and the most this animal can reach.":
        "Mevcut ağırlık ve bu hayvanın ulaşabileceği en fazlası.",
    "Meat and blood both scale with it.":
        "Et de kan da buna göre ölçeklenir.",
    "Over {}%% hunger it starts losing weight.":
        "Açlık {}%% üzerindeyse ağırlık kaybetmeye başlar.",
    "{}{}, how much this animal puts up with you.":
        "{}{}, bu hayvanın sana ne kadar tahammül ettiği.",
    "Each point takes {} off the chance it breaks free while being sheared.":
        "Her puan, kırkım sırasında kurtulma şansını {} düşürür.",
    "Every gain is {}, plus {} per Animal Care level.":
        "Her artış {}, artı Hayvan Bakımı seviyesi başına {}.",
    "Healthy over {}%%, off colour over {}%%, sickly over {}%%, dying below.":
        "{}%% üzeri sağlıklı, {}%% üzeri kırgın, {}%% üzeri hastalıklı, altı ölmekte.",
    "Higher is worse.":
        "Yüksek olması kötü.",
    "Well fed under {}%%, underfed under {}%%, starving over it.":
        "{}%% altı iyi beslenmiş, {}%% altı yetersiz beslenmiş, üstü aç.",
    "Over {}%% it starts losing weight.":
        "{}%% üzerinde ağırlık kaybetmeye başlar.",
    "Fully watered under {}%%, thirsty under {}%%, dying of thirst over it.":
        "{}%% altı suya doymuş, {}%% altı susamış, üstü susuzluktan ölmekte.",
    "{}{}. Calm under {}, unnerved under {}, agitated under {}, wild over it.":
        "{}{}. {} altı sakin, {} altı huzursuz, {} altı tedirgin, üstü vahşi.",
    "Over {} milk and wool grow at {} / stress of their rate.":
        "{} üzerinde süt ve yün normal hızının {} / stres kadarıyla artar.",
    "Over {} a pregnancy can be lost.":
        "{} üzerinde gebelik kaybedilebilir.",
    "Milking with stress over {} and Animal Care {} or less always fails and spills the bucket.":
        "Stres {} üzerindeyken ve Hayvan Bakımı {} veya altındayken sağmak her zaman başarısız olur ve kova devrilir.",
    "Litres in the udder and what it holds.":
        "Memedeki litre ve kapasitesi.",
    "It fills by capacity / {} per game hour, times the sandbox milk modifier.":
        "Oyun saati başına kapasite / {} dolar, sandbox süt çarpanıyla.",
    "Stress over {} slows it down.":
        "{} üzerindeki stres bunu yavaşlatır.",
    "Wool grown and the maximum.":
        "Biriken yün ve azamisi.",
    "It grows by maximum / {} per game hour: {} days for a full fleece.":
        "Oyun saati başına azami / {} artar: tam bir yapağı için {} gün.",
    "Days left before it gives birth.":
        "Doğuma kalan gün.",
    "Stress over {} can end the pregnancy.":
        "{} üzerindeki stres gebeliği bitirebilir.",
    "Hours this female stays fertilised.":
        "Bu dişinin döllenmiş kalacağı saat.",
    "When it runs out she is no longer fertilised.":
        "Süre bitince artık döllenmiş olmaz.",

    # Wounds and healing
    "Wounds: how long each one still needs":
        "Yaralar: her birine daha ne kadar gerekiyor",
    "Adds an Info entry under the treatments you get by clicking a body part in the health panel. Hover it and the box beside it gives the time left on every wound, what bandaging or a poultice would save, how long the bandage lasts and whether the part is mending or getting worse. The game knows all of it and only prints it in debug mode.":
        "Sağlık ekranında bir vücut bölgesine tıklayınca çıkan tedavilerin altına bir Bilgi girdisi ekler. Üzerine gelince yanındaki kutu her yaranın kalan süresini, sargı ya da lapa uygulamanın ne kadar kazandıracağını, sargının ne kadar dayanacağını ve bölgenin iyileşip iyileşmediğini gösterir. Oyun bunların hepsini biliyor ve yalnızca hata ayıklama modunda yazdırıyor.",
    "Wounds: keep vanilla's Doctor level requirements":
        "Yaralar: oyunun İlk Yardım seviye koşullarını koru",
    "Off by default, so you see everything from level {}. Turn it on and each row reappears at the Doctor level vanilla itself uses for it: scratches and lacerations at {}, deep wounds and splints at {}, fractures and stitches at {}, wound infection at {}.":
        "Varsayılan olarak kapalı, yani her şeyi {} seviyesinden itibaren görürsün. Açtığında her satır oyunun kendi kullandığı İlk Yardım seviyesinde geri gelir: sıyrık ve kesikler {}, derin yaralar ve atel {}, kırıklar ve dikişler {}, yara enfeksiyonu {}.",
    "Full recovery":
        "Tam iyileşme",
    "Getting worse":
        "Kötüleşiyor",
    "Healing":
        "İyileşme",
    "normal":
        "normal",
    "slowed by hunger, thirst or illness":
        "açlık, susuzluk veya hastalık yüzünden yavaş",
    "stopped by hunger or thirst":
        "açlık veya susuzluk yüzünden durdu",
    "asleep, ten times faster":
        "uykuda, on kat hızlı",
    "wounded parts share it":
        "yaralı bölge paylaşıyor",
    "Bandage life":
        "Sargı ömrü",
    "ready to remove":
        "çıkarılmaya hazır",

    # Wounds and healing, redesigned tooltip
    "Healing speed":
        "İyileşme hızı",
    "clean for":
        "temiz kalma süresi",
    "Poultice":
        "Lapa",
    "Wound infection":
        "Yara enfeksiyonu",
    "won't close, glass inside":
        "kapanmaz, içinde cam var",
    "won't close while unbandaged":
        "sargısız kapanmaz",
    "rising":
        "yükseliyor",

    # Wounds: shorter recovery label and infection risk
    "Recovery":
        "İyileşme",
    "Infection risk":
        "Enfeksiyon riski",

    # Percentages, ported from the multiplier wording
    "{}%% weapon damage": "{}%% silah hasarı",
    "{}%% endurance recovery": "{}%% dayanıklılık yenilenmesi",
    "{}%% melee damage and knockback": "{}%% yakın dövüş hasarı ve geri itme",
    "{}%% move speed in combat stance": "{}%% dövüş duruşunda hareket hızı",
    "{}%% sprint speed": "{}%% sprint hızı",
    "{}%% chance of being spotted": "{}%% fark edilme şansı",
    "{}%% footstep noise": "{}%% ayak sesi",
    "{}%% recoil delay": "{}%% geri tepme gecikmesi",
    "{}%% aim settling speed": "{}%% nişanı sabitleme hızı",
    "{}%% aim penalty for moving (shared with Nimble)":
        "{}%% hareket hâlinde nişan cezası (Çeviklik ile ortak)",
    "{}%% reload speed": "{}%% şarjör değiştirme hızı",
    "{}%% racking speed": "{}%% kurma hızı",
    "{}%% XP in every Crafting skill": "tüm Üretim becerilerinde {}%% XP",
    "{}%% move speed through trees": "ağaçların arasında {}%% hareket hızı",
    "spotting another player {}%%": "başka bir oyuncuyu fark etme {}%%",
    "timed actions {}%%": "işlemler {}%% sürer",
    "endurance drain {}%%": "{}%% dayanıklılık tüketimi",
    "alcohol hits {}%%, and {}%% over {}%% hunger": "Alkol {0}%% etki eder, {2}%% üstü açlıkta {1}%%",
    "Fitness {}, which is {}%% endurance recovery instead of {}%%":
        "Kondisyon {0}, yani {2}%% yerine {1}%% dayanıklılık yenilenmesi",
    "{}%% attack speed": "{}%% saldırı hızı",
    "{}%% crit chance": "{}%% kritik şansı",
    "racking costs {}%% of the aiming time": "kurmak nişan süresinin {}%% kadarını alır",
    "carrying capacity {}": "taşıma kapasitesi {}",
    "{} to every weapon's durability roll.": "{} her silahın dayanıklılık zarına.",
    "Condition loss (handle)": "Durum kaybı (sap)",
    "Condition loss (head)": "Durum kaybı (uç)",

    # Ronda 4: medicine, traps, weapon components, skill levels
    '%1 corpses nearby': 'Yakında %1 ceset',
    '%1%% attack time': '%1%% saldırı hızı',
    '%1%% crit chance': '%1%% kritik şansı',
    '%1%% muscle strain': '%1%% kas yorgunluğu',
    '%1%% weapon damage': '%1%% silah hasarı',
    '+%1 to the durability roll': 'Dayanıklılık zarına +%1',
    'Adds an Info entry to a placed trap: the odds of it catching anything in an hour, which animals it can take and the share of the catch each one gets, the bait and its freshness, the zone, the hourly odds of losing bait or trap, and the warning that a trap catches nothing while you stand next to it. Bait foods get a row naming what they attract.': 'Kurulmuş bir tuzağa bir Bilgi girdisi ekler: bir saatte herhangi bir şey yakalama olasılığı, hangi hayvanları yakalayabileceği ve her birine düşen av payı, yem ve tazeliği, bölge, yemi veya tuzağı kaybetmenin saatlik olasılıkları ve yanında durduğun sürece tuzağın hiçbir şey yakalamadığı uyarısı. Yem olan yiyecekler, neyi çektiklerini söyleyen bir satır kazanır.',
    'Bait': 'Yem',
    'Bait lost per hour': 'Saat başına yem kaybı',
    'In the trap for': 'Tuzakta kaldığı süre',
    'Filter left': 'Kalan filtre',
    'Hits before it breaks': 'Kırılmadan önceki vuruş',
    'Medicine: duration, delay and effect': 'İlaçlar: süre, gecikme ve etki',
    'Medicine: the full list of effects': 'İlaçlar: etkilerin tam listesi',
    'Muscle strain per hit': 'Vuruş başına kas yorgunluğu',
    'Off by default, so you see everything from level {}. Turn it on and the trap tooltip only appears from Trapping {}, which is the level vanilla itself uses elsewhere.': 'Varsayılan olarak kapalı, bu yüzden her şeyi {} seviyesinden itibaren görürsün. Açtığında tuzak ipucu yalnızca Tuzakçılık {} seviyesinden itibaren görünür; oyunun kendisi de başka yerlerde bu seviyeyi kullanır.',
    'Off by default. Adds everything else each pill does: what cancels it, what intoxication costs it, and the sleeping tablet overdose table.': 'Varsayılan olarak kapalı. Her hapın yaptığı diğer her şeyi ekler: onu neyin iptal ettiğini, sarhoşluğun ona neye mal olduğunu ve uyku hapı aşırı doz tablosunu.',
    'Painkillers, beta blockers, antidepressants, sleeping tablets and antibiotics get how long they last, how long they take to start and what they do per minute. Every figure is recomputed from the sandbox day length.': 'Ağrı kesiciler, beta blokerler, antidepresanlar, uyku hapları ve antibiyotikler ne kadar sürdüklerini, etkilerinin ne zaman başladığını ve dakikada ne yaptıklarını gösterir. Her değer, korumalı alanın gün uzunluğundan yeniden hesaplanır.',
    'Prey': 'Av',
    'Rots once thawed': 'Çözülünce çürür',
    'Stale once thawed': 'Çözülünce bayatlar',
    'Takes effect in': 'Etkisi şu sürede başlar',
    'Trap lost per hour': 'Saat başına tuzak kaybı',
    'Traps: catch odds, bait and hours': 'Tuzaklar: yakalama olasılıkları, yem ve saatler',
    "Traps: keep vanilla's Trapping level requirements": 'Tuzaklar: oyunun Tuzakçılık seviye gereksinimlerini koru',
    'Zone': 'Bölge',
    'a second dose resets the clock, it does not add': 'ikinci doz sayacı sıfırlar, üstüne eklemez',
    'a third of the strength above {} intoxication': '{} sarhoşluğun üzerinde gücün üçte biri',
    'fresh for %1': '%1 daha taze',
    'half the strength above {} intoxication': '{} sarhoşluğun üzerinde gücün yarısı',
    'each pill counts double above {} intoxication': '{} sarhoşluk üzerinde her hap iki sayılır',
    'holds the fever, does not cure it': 'ateşi tutar, iyileştirmez',
    'incoming panic {}%% per pill, down to nothing': 'hap başına gelen panik {}%%, sıfıra kadar',
    'it catches nothing while you are near it': 'sen yanındayken hiçbir şey yakalamaz',
    'only the first dose has to wait': 'yalnızca ilk dozun beklemesi gerekir',
    'overdose: {} pills cost {} health, {} cost {}, {} kill': 'aşırı doz: {} hap {} can götürür, {} hap {} götürür, {} hap öldürür',
    'sleeping cancels the effect': 'uyumak etkiyi iptal eder',
    'stale, catches nothing': 'bayat, hiçbir şeyi çekmez',
    'the longer it waits, the likelier it comes out dead': 'ne kadar beklerse, ölü çıkma olasılığı o kadar artar',
    'to full in %1': '%1 içinde tam dolar',
    'to zero in %1': '%1 içinde sıfırlanır',
    'wound pain stops being recalculated while it lasts': 'etkisi sürerken yara ağrısı yeniden hesaplanmaz',
    'zombie fever held': 'zombi ateşi durduruldu',
    '{}%% reading time': '{}%% okuma süresi',
    'Effect': 'Etki',

    # Ronda 4, segunda pasada
    '%1 s': '%1 sn',
    '%1 s per round': 'mermi başına %1 sn',
    '%1%% attack speed': '%1%% saldırı hızı',
    'Details': 'Ayrıntılar',
    'Info': 'Bilgi',
    'Possible prey': 'Olası av',
    'Trap breaks per hour': 'Saat başına tuzak kırılması',
    'holds the fever': 'ateşi tutar',
    'not being used (%1 corpses nearby)': 'harcanmıyor (yakında %1 ceset)',
    'Bird': 'Kuş',
    'Active hours': 'Etkin saatler',
    'Possible prey, share of the catch': 'Olası av, av payı',
    'Catch chance': 'Yakalama şansı',
    'Bait condition': 'Yem durumu',
    'Trap condition': 'Tuzak durumu',
    'while you are near it, it neither catches nor breaks': 'sen yanındayken ne bir şey yakalar ne de kırılır',
    'Bait loss risk, per hour': 'Saat başına yemi kaybetme riski',
    'Wrecked by an animal, per hour': 'Saat başına bir hayvan tarafından parçalanma',
    '%1 / h': '%1 / sa',
    'Bait loss risk': 'Yemi kaybetme riski',
    'Chance of being wrecked': 'Parçalanma olasılığı',
    'Critical damage': 'Kritik hasar',
    'Effective durability': 'Etkin dayanıklılık',
    'Damage with your character': 'Karakterinle hasar',
    'Reach (tiles)': 'Menzil (kare)',

    # Bags and the torch beam (0.9.20)
    'All round': 'Her yöne',
    'Beam (degrees)': 'Işık huzmesi (derece)',
    'Bags: how much they slow you down': 'Çantalar: seni ne kadar yavaşlatıyorlar',
    "The run and combat speed a bag costs you, which the game applies and never shows. The run figure is the one you are paying right now: a bag's penalty grows by half again as it fills up, so the same pack goes from {}%% empty to {}%% full. It counts the same in your hands as on your back.": 'Bir çantanın sana mal olduğu koşu ve dövüş hızı: oyunun uyguladığı ama hiç göstermediği değer. Koşu değeri şu anda ödediğin değerdir; çanta doldukça ceza yarısı kadar daha artar, yani aynı çanta boşken {}%%, doluyken {}%% olur. Elinde de sırtında da aynı sayılır.',

    # Trait figures corrected against bytecode (0.9.21)
    "Aiming and Maintenance are not affected":
        "Nişan Alma ve Bakım etkilenmez",
    "ambient light never drops below {} in the dark":
        "karanlıkta ortam ışığı asla {} altına düşmez",
    "can tell a poisonous wild plant from a safe one":
        "zehirli bir yabani bitkiyi güvenli olandan ayırt eder",
    "lights a fire with a notched plank twice as fast":
        "çentikli tahtayla ateşi iki kat hızlı yakar",
    "no harm at all from tainted water":
        "kirli su hiç zarar vermez",
    "{} health on every construction":
        "her yapıya {} can",
    "{} tiles of perception instead of {}":
        "{1} yerine {0} karelik algı",
    "{}%% XP in the six melee weapon skills":
        "altı yakın dövüş silah becerisinde {}%% XP",
    "{}%% chance of tearing your clothes on a tree":
        "ağaca takılıp kıyafetini yırtma ihtimali {}%%",
    "{}%% from any other poison":
        "diğer herhangi bir zehirden {}%%",
    "{}%% from any other poison, bleach aside":
        "çamaşır suyu hariç diğer herhangi bir zehirden {}%%",
    "{}%% weather penalty in combat":
        "savaşta {}%% hava cezası",

    # Per-level lines for the twenty craft skills (0.9.21)
    "%1 crop health at planting":
        "ekerken ürün sağlığı %1",
    "%1%% chance the crop is cursed if planted out of its month":
        "kendi ayı dışında ekilirse ürünün lanetlenme ihtimali %1%%",
    "%1%% chance of a bonus harvest planted in its best month":
        "en iyi ayında ekilirse fazladan hasat ihtimali %1%%",
    "%1 disease removed per treatment":
        "her tedavide %1 hastalık giderilir",
    "%1%% chance of harvesting %2 extra vegetables":
        "%2 fazla sebze toplama ihtimali %1%%",
    "%1%% back strain planting and harvesting":
        "ekim ve hasatta bel yükü %1%%",
    "%1 points off the chance a stressed animal breaks off milking or shearing":
        "stresli bir hayvanın sağım veya kırkımda kaçma ihtimaline %1 puan",
    "a stressed animal never breaks off milking or shearing":
        "stresli bir hayvan artık sağımda veya kırkımda kaçmaz",
    "x%1 chance of each extra part off a carcass":
        "leşten çıkan her ek parçanın ihtimali x%1",
    "x%1 of each part":
        "her parçadan x%1",
    "up to %1 blood splatters on you":
        "üzerinizde en fazla %1 kan lekesi",
    "%1 health on everything you build":
        "inşa ettiğiniz her şeye %1 can",
    "%1%% build time":
        "%1%% inşa süresi",
    "%1%% barricading time":
        "%1%% barikat kurma süresi",
    "%1%% chance of recovering material when dismantling":
        "sökerken malzeme geri alma ihtimali %1%%",
    "%1%% of the ingredient used per addition":
        "her eklemede malzemenin %1%% kadarı harcanır",
    "x%1 nutrients from each ingredient":
        "her malzemeden x%1 besin",
    "rotten food can go in evolved recipes, worth %1%% of its hunger":
        "gelişmiş tariflere az miktarda çürük yiyecek koyabilirsiniz",
    "x%1 fracture healing with a splint":
        "atelle kırık iyileşmesi x%1",
    "a bandage lasts %1 to %2 longer":
        "bir bandaj %1 ile %2 kat daha uzun dayanır",
    "%1%% time for every medical action":
        "her tıbbi işlem için %1%% süre",
    "you can judge how bad a wound is":
        "bir yaranın ne kadar kötü olduğunu değerlendirebilirsiniz",
    "you can read pain, and spot the burns that need washing":
        "acıyı okuyabilir, hangi yanıkların yıkanması gerektiğini görebilirsiniz",
    "you can tell when stitches are ready to come out":
        "dikişlerin ne zaman alınabileceğini anlarsınız",
    "you spot a wound infection straight away":
        "yara enfeksiyonunu anında fark edersiniz",
    "%1%% chance of getting the patch back":
        "yamayı geri alma ihtimali %1%%",
    "%1%% time to add or remove a patch":
        "yama takma veya çıkarma süresi %1%%",
    "a hole can be repaired completely, defense and insulation included":
        "bir delik tamamen onarılabilir, koruma ve yalıtım dahil",
    "+%1%% generator condition per repair":
        "her onarımda +%1%% jeneratör durumu",
    "%1 points to the chance of hotwiring a car":
        "bir arabayı kontak kablosuyla çalıştırma ihtimaline %1 puan",
    "%1%% chance of setting off the car alarm":
        "araba alarmını tetikleme ihtimali %1%%",
    "you can salvage and repair a standard engine":
        "standart bir motoru sökebilir ve onarabilirsiniz",
    "you can salvage and repair a heavy-duty engine":
        "ağır hizmet motorunu sökebilir ve onarabilirsiniz",
    "you can salvage and repair a sport engine":
        "spor bir motoru sökebilir ve onarabilirsiniz",
    "you can build the sturdier brick wall":
        "daha sağlam tuğla duvarı inşa edebilirsiniz",
    "small %1%%, medium %2%%, large %3%%":
        "küçük %1%%, orta %2%%, büyük %3%%",
    "%1 points to the chance a berry or mushroom is poisonous":
        "bir meyvenin veya mantarın zehirli olma ihtimaline %1 puan",
    "%1%% time to inspect a track":
        "bir izi incelemek için %1%% süre",
    "no effect of its own, this level only unlocks the recipes below":
        "kendine ait etkisi yok, bu seviye yalnızca aşağıdaki tarifleri açar",

    # 0.9.21 follow-up
    "%1 rags when you rip up clothing, capped by the parts it covers":
        "kıyafet yırtarken %1 parça, giysinin kapladığı yer kadar",
    "rotten food can go in evolved recipes, worth %1%% of its hunger":
        "çürük yiyecek gelişmiş tariflerde kullanılabilir, doyuruculuğunun %1%% kadarını verir",

    # 0.9.21 follow-up 2
    "%1%% time per litre shearing an animal":
        "bir hayvanı kırkarken litre başına %1%% süre",
    "%1 rags when you rip up clothing, capped by the parts it covers":
        "kıyafet yırtarken %1 paçavra, giysinin kapladığı bölge sayısı kadar",
    "%1 to the most aramid thread you can pull out":
        "çıkarabileceğin aramid ipliğin üst sınırına %1",
    "starts at {} weight, becomes Emaciated at {} or less and Low Weight above {}":
        "{} kiloyla başlar, {} veya altında Sıska olur, {} üstünde Düşük Kilo olur",
    "starts at {} weight, becomes High Weight below {}":
        "{} kiloyla başlar, {} altında Şişman olur",
    "starts at {} weight, becomes Very High Weight at {} and is lost below {}":
        "{} kiloyla başlar, {} kiloda Obez olur ve {} altında kaybolur",
    "starts at {} weight, becomes Very Low Weight at {} or less and is lost above {}":
        "{} kiloyla başlar, {} veya altında Çok Zayıf olur ve {} üstünde kaybolur",
    "XP awarded":
        "Verilen XP",
    "{} chance to trip when a zombie lunges through a window":
        "{} pencereden atılan bir zombide tökezleme şansı",
    "{} to the roll that keeps you on your feet when a zombie shoves you":
        "{} bir zombi seni ittiğinde ayakta kalma zarına",
    "{}%% muscle strain":
        "{}%% kas yorgunluğu",
    "{}%% axe attack speed, chopping trees included":
        "{}%% balta saldırı hızı, ağaç kesmek dahil",

    # B42.20 trait corrections
    "Another x{} at panic level {}":
        "panik seviyesi {1} iken ayrıca x{0}",
    "Can hotwire without Electrical {} and Mechanics {}":
        "Elektrik {} ve Mekanik {} olmadan kontak kablolayabilir",
    "Engine revs three times faster in reverse":
        "geri viteste motor devri üç kat hızlı yükselir",
    "Halves your rope climbing bonus":
        "ip tırmanma bonusunu yarıya indirir",
    "No unhappiness from looting corpses":
        "ceset aramak mutsuzluk vermez",
    "Stress from handling bloody items":
        "kanlı eşyaları taşımak stres verir",
    "{} move speed at panic level {}, {} at level {}":
        "panik seviyesi {1} iken {0} hareket hızı, seviye {3} iken {2}",
    "{} to the rope climbing roll":
        "{} ip tırmanma zarına",
    "{}%% acceleration, fading out above {}%% of the car's top speed":
        "{0}%% hızlanma, aracın azami hızının {1}%% üstünde sönümlenir",
    "{}%% carry capacity":
        "{}%% taşıma kapasitesi",
    "{}%% chance of breaking a window lock instead of {}%%":
        "{1}%% yerine {0}%% pencere kilidini kırma şansı",
    "{}%% endurance cost on every exertion":
        "her eforda {}%% dayanıklılık maliyeti",
    "{}%% reverse acceleration, gone past {} km/h":
        "geri viteste {0}%% hızlanma, {1} km/h sonrası yok",
    "{}%% unhappiness from looting corpses":
        "ceset aramaktan {}%% mutsuzluk",

    # Repair recipes
    "Repair: +%1 condition, %2 chance of failing":
        "Onarım: +%1 durum, %2 başarısız olma",
    "Repair: +%1 condition, %2 chance of failing, repaired %3 times":
        "Onarım: +%1 durum, %2 başarısız olma, %3 kez onarıldı",

    # Corpse count and temperature figures
    "Body temperature: the number on every bar":
        "Vücut sıcaklığı: her çubuktaki sayı",
    "Nauseous: how many corpses are making you ill":
        "Mide bulantısı: kaç ceset seni hasta ediyor",
    "Rotting corpses nearby raise food sickness, and the game never says how many are close enough. Five or fewer do nothing. The count is read back out of the game, so it follows the sandbox setting.":
        "Yakındaki çürüyen cesetler gıda zehirlenmesini artırır ve oyun kaç tanesinin yeterince yakın olduğunu asla söylemez. Beş veya daha azı hiçbir şey yapmaz. Sayı oyunun kendisinden okunur, yani sandbox ayarını izler.",
    "The temperature view prints its value on Insulation and Wind resistance and leaves the other nine bars as a colour. This sets the same flag on the rest, so skin temperature, body response, heat and wetness read as figures. Vanilla does the drawing, and only for the body part you have selected.":
        "Sıcaklık görünümü değerini yalnızca Yalıtım ve Rüzgar direncine yazar, diğer dokuz çubuğu renk olarak bırakır. Bu, aynı işareti geri kalanına da koyar, böylece deri sıcaklığı, vücut tepkisi, ısı ve ıslaklık sayı olarak okunur. Çizimi oyunun kendisi yapar ve yalnızca seçtiğin vücut bölgesi için.",

    # Options tab
    "Custom":
        "Özel",
    "Nothing matches that":
        "Eşleşen bir şey yok",
    "Moodles: how many corpses are making you ill":
        "Moodle'lar: kaç ceset seni hasta ediyor",

    # Option groups
    "Every gun this box or magazine fits, one per row.":
        "Bu kutunun ya da şarjörün uyduğu her silah, satır başına bir tane.",
    "How bloody the garment is, out of a hundred.":
        "Giysinin ne kadar kanlı olduğu, yüz üzerinden.",
    "How brightly it lights what it reaches.":
        "Ulaştığı yeri ne kadar parlak aydınlattığı.",
    "How dirty the garment is, out of a hundred.":
        "Giysinin ne kadar kirli olduğu, yüz üzerinden.",
    "How drunk this container will get you.":
        "Bu kabın seni ne kadar sarhoş edeceği.",
    "How far the light reaches, in tiles.":
        "Işığın ne kadar uzağa ulaştığı, kare cinsinden.",
    "How far the shot is heard, which is how far the horde comes from.":
        "Atışın ne kadar uzaktan duyulduğu, yani sürünün nereden geleceği.",
    "How long before the pill starts working, and only while you have none running.":
        "Hapın etki etmeye başlaması ne kadar sürer, ve yalnızca üzerinde etkili bir hap yokken.",
    "How long cooked food can stay on the heat before it burns.":
        "Pişmiş yemeğin yanmadan önce ateşte ne kadar durabileceği.",
    "How long the charge lasts with the thing switched on.":
        "Cihaz açıkken şarjın ne kadar dayandığı.",
    "How long the filter lasts at your current exposure, and how many corpses are around you.":
        "Mevcut maruziyetinde filtrenin ne kadar dayandığı ve çevrende kaç ceset olduğu.",
    "How long the item burns for as fuel.":
        "Eşyanın yakıt olarak ne kadar yandığı.",
    "How long the pages you have not read yet will take.":
        "Henüz okumadığın sayfaların ne kadar süreceği.",
    "How long the pill keeps working.":
        "Hapın ne kadar süre etki etmeye devam ettiği.",
    "How long the plant takes to be ready, at the current farming speed.":
        "Mevcut tarım hızında bitkinin hazır olması ne kadar sürer.",
    "How long until the food goes stale, at the current rot speed.":
        "Mevcut çürüme hızında yemeğin bayatlamasına ne kadar kaldığı.",
    "How long until the food is rotten, at the current rot speed.":
        "Mevcut çürüme hızında yemeğin çürümesine ne kadar kaldığı.",
    "How many hits the weapon has left in it, which is the one figure that compares any two weapons.":
        "Silahta kaç vuruş kaldığı, ki bu herhangi iki silahı karşılaştıran tek rakamdır.",
    "How much cold the garment keeps out. The game only draws a bar.":
        "Giysinin ne kadar soğuk tuttuğu. Oyun yalnızca bir çubuk çizer.",
    "How much is left in the filter.":
        "Filtrede ne kadar kaldığı.",
    "How much of it you have already heard.":
        "Bunun ne kadarını zaten dinlediğin.",
    "How much of the corpse sickness the mask keeps off you. {}%% is immunity.":
        "Maskenin ceset hastalığının ne kadarını senden uzak tuttuğu. {}%% tam bağışıklıktır.",
    "How much of your hunger bar the drink covers.":
        "İçeceğin açlık çubuğunun ne kadarını doldurduğu.",
    "How much of your thirst bar the drink covers.":
        "İçeceğin susuzluk çubuğunun ne kadarını doldurduğu.",
    "How much pull the rod takes before the line gives.":
        "Misina kopmadan önce kamışın ne kadar çekmeye dayandığı.",
    "How much rain the garment keeps out. The game only draws a bar.":
        "Giysinin ne kadar yağmur tuttuğu. Oyun yalnızca bir çubuk çizer.",
    "How much the bag slows you down, with its weight and what is inside counted.":
        "Çantanın seni ne kadar yavaşlattığı, kendi ağırlığı ve içindekiler hesaba katılarak.",
    "How much the bag slows your swing.":
        "Çantanın vuruşunu ne kadar yavaşlattığı.",
    "How much the garment slows you down, as the penalty itself rather than a bar.":
        "Giysinin seni ne kadar yavaşlattığı, çubuk yerine cezanın kendisi olarak.",
    "How much the garment slows your swing, as the penalty itself rather than a bar.":
        "Giysinin vuruşunu ne kadar yavaşlattığı, çubuk yerine cezanın kendisi olarak.",
    "How much tiredness this surface actually clears, your traits included.":
        "Bu yüzeyin yorgunluğunun ne kadarını gerçekten giderdiği, özelliklerin dahil.",
    "How much wind the garment keeps out. The game only draws a bar.":
        "Giysinin ne kadar rüzgâr tuttuğu. Oyun yalnızca bir çubuk çizer.",
    "How often a hit crits, with your level in the weapon's own skill counted.":
        "Bir vuruşun ne sıklıkla kritik olduğu, silahın kendi yeteneğindeki seviyen hesaba katılarak.",
    "How often a shot crits.":
        "Bir atışın ne sıklıkla kritik olduğu.",
    "How wet the garment is, out of a hundred.":
        "Giysinin ne kadar ıslak olduğu, yüz üzerinden.",
    "In tiles. A swing landed at the edge of your reach does up to twice the damage of one landed close in.":
        "Kare cinsinden. Menzilinin ucunda inen bir vuruş, yakından inene göre iki katına kadar hasar verir.",
    "Off by default: the game only reveals this block for packaged food or a Nutritionist.":
        "Varsayılan olarak kapalı: oyun bu bölümü yalnızca paketli yiyecekte ya da Beslenme Uzmanı ile gösterir.",
    "Rounds in the magazine right now, out of what it holds.":
        "Şarjörde şu anda kaç mermi olduğu ve toplam kaç aldığı.",
    "The calibre the magazine takes.":
        "Şarjörün aldığı kalibre.",
    "The calories in what is actually in the container, mixtures included.":
        "Kapta gerçekten ne varsa onun kalorisi, karışımlar dahil.",
    "The carbohydrates in what is actually in the container.":
        "Kapta gerçekten ne varsa onun karbonhidratı.",
    "The charge left, as a number instead of a bar.":
        "Kalan şarj, çubuk yerine sayı olarak.",
    "The edge, and the ceiling a worn head puts on it: blunt, the weapon loses the top of its damage range.":
        "Keskinlik ve yıpranmış bir başlığın ona koyduğu tavan: kör bir ağız silahın hasar aralığının üstünü alır.",
    "The exact minimum and maximum. The game only ever draws it as a bar.":
        "Tam olarak en düşük ve en yüksek değer. Oyun bunu yalnızca çubuk olarak çizer.",
    "The exact points left, and the head's own count on a weapon that has one.":
        "Kalan tam puan, ve başlığı olan bir silahta başlığın kendi puanı.",
    "The exact points left, where the game only draws a bar.":
        "Kalan tam puan, oyunun yalnızca çubuk çizdiği yerde.",
    "The fat in what is actually in the container.":
        "Kapta gerçekten ne varsa onun yağı.",
    "The fatigue each swing costs you.":
        "Her vuruşun sana mal olduğu yorgunluk.",
    "The furthest tile the gun can hit.":
        "Silahın vurabildiği en uzak kare.",
    "The gun's own hit chance, before your aiming skill.":
        "Silahın kendi isabet şansı, senin nişancılığından önce.",
    "The hook fitted, and what it does to your odds of a bite.":
        "Takılı olan iğne ve balığın vurma ihtimaline ne yaptığı.",
    "The line fitted, and how much of it each tug wears away.":
        "Takılı olan misina ve her çekişte ne kadarının aşındığı.",
    "The months it can be sown in, one per row.":
        "Ekilebileceği aylar, satır başına bir tane.",
    "The multiplier your shoes put on stomping a downed zombie. Footwear only.":
        "Ayakkabılarının yerdeki bir zombiyi ezmeye verdiği çarpan. Yalnızca ayakkabı.",
    "The multiplier your skill puts on this weapon's swing.":
        "Yeteneğinin bu silahın vuruşuna verdiği çarpan.",
    "The net pace of the pill, which is what compares two of them at a glance.":
        "Hapın net hızı, ki iki hapı bir bakışta karşılaştıran şey budur.",
    "The odds of losing a point of condition on a hit, with Maintenance and the weapon's skill counted.":
        "Bir vuruşta bir durum puanı kaybetme ihtimali, Bakım ve silahın yeteneği hesaba katılarak.",
    "The odds of losing a point of condition per shot.":
        "Atış başına bir durum puanı kaybetme ihtimali.",
    "The poison the drink carries, and only while the game is willing to tell you.":
        "Tutukluk yapmanın gerçek ihtimali, yıpranma ve zayıf kavrayış dahil.",
    "The proteins in what is actually in the container.":
        "Kapta gerçekten ne varsa onun proteini.",
    "The real odds of a jam, wear and a weak grip included.":
        "İçeceğin taşıdığı zehir, ve yalnızca oyun bunu sana söylemeye razıyken.",
    "The real seconds a reload takes, with your reloading skill and your panic counted.":
        "Bir doldurmanın gerçekte kaç saniye sürdüğü, doldurma yeteneğin ve paniğin hesaba katılarak.",
    "The real seconds spent lining up the shot, with your aiming skill and your traits counted.":
        "Atışı hizalamanın gerçekte kaç saniye sürdüğü, nişancılığın ve özelliklerin hesaba katılarak.",
    "The recipes it teaches that you do not know yet, one per row.":
        "Öğrettiği ve senin henüz bilmediğin tarifler, satır başına bir tane.",
    "The swing animation, which is what really separates a slow weapon from a fast one.":
        "Vuruş animasyonu, yavaş bir silahı hızlı olandan gerçekten ayıran şey.",
    "What a critical is worth, from {}%% to {}%% depending on the weapon. The game shows it nowhere.":
        "Bir kritiğin ne değdiği, silaha göre {}%% ile {}%% arası. Oyun bunu hiçbir yerde göstermez.",
    "What feeds the Uncomfortable moodle. The game never shows it on the garment at all.":
        "Rahatsızlık moodle'ını besleyen şey. Oyun bunu giysinin üzerinde hiç göstermez.",
    "What is left in your hands when the rod breaks.":
        "Kamış kırıldığında elinde ne kaldığı.",
    "What sleeping here costs you in comfort.":
        "Burada uyumanın sana konfor olarak neye mal olduğu.",
    "What the drink does to boredom and unhappiness, which move together here.":
        "İçeceğin can sıkıntısı ve mutsuzluğa ne yaptığı, ki burada ikisi birlikte hareket eder.",
    "What the drink does to your fatigue bar.":
        "İçeceğin yorgunluk çubuğuna ne yaptığı.",
    "What the drink does to your stress.":
        "İçeceğin stresine ne yaptığı.",
    "What the food still needs, and the temperature the figure assumes.":
        "Yemeğe daha ne gerektiği, ve rakamın varsaydığı sıcaklık.",
    "Whether it is a cone you aim or a lamp that lights all around, and how wide the cone is.":
        "Doğrulttuğun bir koni mi yoksa çevreyi aydınlatan bir lamba mı olduğu, ve koninin ne kadar açıldığı.",
    "Which fish this bait brings in.":
        "Bu yemin hangi balıkları çektiği.",
    "Which skill the tape or disc trains and how much experience is left in it.":
        "Kasetin ya da diskin hangi yeteneği çalıştırdığı ve içinde ne kadar deneyim kaldığı.",
    "Which skill the weapon trains, and therefore which one drives its damage and its speed.":
        "Silahın hangi yeteneği geliştirdiği, dolayısıyla hasarını ve hızını hangisinin sürüklediği.",
    "Your own reading speed, traits, glasses and sitting down included.":
        "Kendi okuma hızın, özellikler, gözlük ve oturuyor olmak dahil.",
    "Nutrition":
        "Besin değerleri",
    "Sleep":
        "Uyku",
    "How much the bag slows your attack. It multiplies the weapon's own swing speed, not your walking.":
        "Çantanın saldırını ne kadar yavaşlattığı. Silahın kendi vuruş hızını çarpar, yürüyüşünü değil.",
    "How much the garment slows your attack. It multiplies the weapon's own swing speed, not your walking.":
        "Giysinin saldırını ne kadar yavaşlattığı. Silahın kendi vuruş hızını çarpar, yürüyüşünü değil.",
    "Best baits":
        "En iyi yemler",
    "Every animal this trap can catch and its share of the catch.":
        "Bu tuzağın yakalayabileceği her hayvan ve avdaki payı.",
    "Feathers":
        "Tüyler",
    "Fog on a line of its own, because the game lumps it into weather and then reports neither.":
        "Sis kendi satırında, çünkü oyun onu havanın içine atıp sonra ikisini de bildirmiyor.",
    "Glass or a bullet still in the wound, which stops it healing until it is out.":
        "Yarada hâlâ duran cam ya da kurşun; çıkmadan yara iyileşmiyor.",
    "How far the disease has gone, out of a hundred.":
        "Hastalığın ne kadar ilerlediği, yüz üzerinden.",
    "How far the generator is heard, halved when it stands indoors.":
        "Jeneratörün ne kadar uzaktan duyulduğu; kapalı alanda yarısı.",
    "How full the udder is and whether it can be milked yet.":
        "Memenin ne kadar dolu olduğu ve artık sağılıp sağılamayacağı.",
    "How hungry the animal is, and how long its feed will last.":
        "Hayvanın ne kadar aç olduğu ve yeminin ne kadar dayanacağı.",
    "How long before old age starts costing the animal its yield.":
        "Yaşlılığın hayvanın verimini düşürmeye başlamasına ne kadar kaldığı.",
    "How long each cut, scratch, burn or bite still needs.":
        "Her kesiğin, sıyrığın, yanığın ya da ısırığın daha ne kadar süreceği.",
    "How long is left of a pregnancy, or of an egg being fertilised.":
        "Gebelikten ya da bir yumurtanın döllenmesinden ne kadar kaldığı.",
    "How long since the last watering. The game works it out to pick a colour and then never shows it.":
        "Son sulamanın üzerinden ne kadar geçtiği. Oyun bunu bir renk seçmek için hesaplar ve asla göstermez.",
    "How long the bandage lasts before it is dirty and worth changing.":
        "Bandajın kirlenip değiştirmeye değer hale gelmesine ne kadar dayandığı.",
    "How long the catch has been waiting in there.":
        "Avın orada ne kadar süredir beklediği.",
    "How long the fracture needs, and what the splint on it is worth.":
        "Kırığın ne kadar süreye ihtiyacı olduğu ve üzerindeki atelin ne değdiği.",
    "How long the fuel in the tank lasts at the current draw.":
        "Depodaki yakıtın mevcut tüketimle ne kadar dayandığı.",
    "How long the part needs to be whole again, and how fast it is healing.":
        "Uzvun yeniden bütün olması için ne kadar gerektiği ve ne hızla iyileştiği.",
    "How long the stiffness in that limb takes to pass.":
        "O uzuvdaki tutulmanın geçmesinin ne kadar sürdüğü.",
    "How long the stitches need, and when they can come out.":
        "Dikişlerin ne kadar süreye ihtiyacı olduğu ve ne zaman alınabileceği.",
    "How long until it breaks down for good, on average.":
        "Ortalama olarak tamamen bozulmasına ne kadar kaldığı.",
    "How long until it wears down to the point where it can catch fire.":
        "Alev alabileceği noktaya kadar yıpranmasına ne kadar kaldığı.",
    "How long until the crop moves to its next stage.":
        "Ekinin bir sonraki aşamaya geçmesine ne kadar kaldığı.",
    "How long you will wait compared with the best possible spot.":
        "Mümkün olan en iyi noktaya kıyasla ne kadar bekleyeceğin.",
    "How many feathers butchering will give.":
        "Kesimin ne kadar tüy vereceği.",
    "How many fish this spot still holds, and what that is worth.":
        "Bu noktada kaç balık kaldığı ve bunun ne değdiği.",
    "How much blood butchering will give.":
        "Kesimin ne kadar kan vereceği.",
    "How much fertiliser the plot holds. Above one is the too much case in the game's own code.":
        "Tarlada ne kadar gübre olduğu. Birin üzeri, oyunun kendi kodunda fazla kaçmış demektir.",
    "How much meat butchering will give, which is what answers whether it is worth killing yet.":
        "Kesimin ne kadar et vereceği; artık kesmeye değer mi sorusunun cevabı tam olarak budur.",
    "How much of the bait is still good.":
        "Yemin ne kadarının hâlâ iyi olduğu.",
    "How much the animal trusts you, which is what lets you handle it.":
        "Hayvanın sana ne kadar güvendiği; onu elleyebilmeni sağlayan şey budur.",
    "How much wool has grown back and whether it can be sheared yet.":
        "Ne kadar yün çıktığı ve artık kırkılıp kırkılamayacağı.",
    "How stressed the animal is, out of a hundred.":
        "Hayvanın ne kadar stresli olduğu, yüz üzerinden.",
    "How the wound infection is going, and whether it is still rising.":
        "Yara enfeksiyonunun nasıl gittiği ve hâlâ yükselip yükselmediği.",
    "How thirsty the animal is, and how long its water will last.":
        "Hayvanın ne kadar susuz olduğu ve suyunun ne kadar dayanacağı.",
    "Level needed":
        "Gereken seviye",
    "Lodged objects":
        "Saplanmış cisimler",
    "Odds with your bait":
        "Yeminle şans",
    "Predator":
        "Yırtıcı",
    "Size and weight":
        "Boy ve ağırlık",
    "Strength at the top skill level":
        "En üst seviyedeki dayanıklılık",
    "The Fishing level this species needs before it will bite.":
        "Bu türün oltaya vurması için gereken Balıkçılık seviyesi.",
    "The animal's health as a number.":
        "Hayvanın canı, sayı olarak.",
    "The animal's weight, and how far it still has to grow.":
        "Hayvanın ağırlığı ve daha ne kadar büyüyeceği.",
    "The chance of this exact species with the bait you are using.":
        "Kullandığın yemle tam olarak bu türün çıkma ihtimali.",
    "The crop's health out of a hundred. The game only prints it with debug on.":
        "Ekinin canı, yüz üzerinden. Oyun bunu yalnızca hata ayıklama açıkken yazar.",
    "The fuel still in the tank. The game knows the number and only prints it as a debug option.":
        "Depoda kalan yakıt. Oyun bu sayıyı bilir ve yalnızca hata ayıklama seçeneği olarak gösterir.",
    "The health the wall or door will have when you build it at your current level.":
        "Duvarın ya da kapının, mevcut seviyende inşa edersen sahip olacağı dayanıklılık.",
    "The hourly odds of a bang loud enough to pull zombies in.":
        "Saat başına, zombileri çekecek kadar yüksek bir patlama sesi ihtimali.",
    "The hourly odds of a fire or an explosion, which set the generator to zero outright.":
        "Saat başına yangın ya da patlama ihtimali; ikisi de jeneratörü doğrudan sıfırlar.",
    "The hourly odds of the bait being taken without a catch.":
        "Saat başına, hiçbir şey yakalanmadan yemin götürülme ihtimali.",
    "The hourly odds of the trap being wrecked.":
        "Saat başına tuzağın parçalanma ihtimali.",
    "The hourly odds of the wound becoming infected.":
        "Saat başına yaranın enfeksiyon kapma ihtimali.",
    "The hours of the day the trap actually works.":
        "Günün, tuzağın gerçekten çalıştığı saatleri.",
    "The kind of ground the trap is standing on, which decides what can come.":
        "Tuzağın üzerinde durduğu zemin türü; neyin gelebileceğine o karar verir.",
    "The odds of a bite once every factor is put together.":
        "Bütün etkenler bir araya geldikten sonraki vurma ihtimali.",
    "The odds of catching anything at all in an hour.":
        "Bir saat içinde herhangi bir şey yakalama ihtimali.",
    "The range of lengths and weights this species comes in.":
        "Bu türün çıktığı boy ve ağırlık aralığı.",
    "The share of your catches that will be junk here.":
        "Burada avının ne kadarının çöp olacağı.",
    "The two things the game never says: a long wait kills the catch, and standing nearby stops the trap.":
        "Oyunun asla söylemediği iki şey: uzun bekleyiş avı öldürür ve sen yakındayken tuzak durur.",
    "The water level as a number, and the amount this seed actually needs.":
        "Su seviyesi sayı olarak ve bu tohumun gerçekten ihtiyaç duyduğu miktar.",
    "Time to the danger threshold":
        "Tehlike eşiğine kalan süre",
    "Trophy size":
        "Kupa boyutu",
    "Warnings":
        "Uyarılar",
    "Warns that the species only bites while you reel in.":
        "Türün yalnızca sen misinayı toplarken vurduğunu hatırlatır.",
    "What a catch has to beat to count as a trophy.":
        "Bir avın kupa sayılması için neyi geçmesi gerektiği.",
    "What the herbs in the bandage are adding.":
        "Bandajdaki bitkilerin ne kattığı.",
    "What the same build would have at level {}, which is the reason to know the figure before building.":
        "Aynı yapının {}. seviyede ne olacağı; inşa etmeden önce bu sayıyı bilmenin sebebi budur.",
    "What the time of day is worth, as the multiplier behind the game's own rating.":
        "Günün saatinin ne değdiği; oyunun kendi değerlendirmesinin arkasındaki çarpan.",
    "What the water temperature is worth, with the actual reading in degrees.":
        "Su sıcaklığının ne değdiği, gerçek derece okumasıyla birlikte.",
    "What the weather is worth, as the multiplier behind the game's own rating.":
        "Havanın ne değdiği; oyunun kendi değerlendirmesinin arkasındaki çarpan.",
    "What the wind is worth. Past half strength it costs the same penalty fog does, and the two never stack.":
        "Rüzgârın ne değdiği. Gücün yarısını geçince sisle aynı cezayı getirir ve ikisi asla üst üste binmez.",
    "Whether the mains or a generator is keeping the pump running.":
        "Pompayı şebekenin mi yoksa bir jeneratörün mü çalıştırdığı.",
    "Which animals a bait item brings in.":
        "Yem olarak kullanılan bir eşyanın hangi hayvanları çektiği.",
    "Which bait is in the trap, and whether it is still fresh.":
        "Tuzakta hangi yemin olduğu ve hâlâ taze olup olmadığı.",
    "Which baits work best on this species.":
        "Bu türde en iyi işe yarayan yemler.",
    "Which growth stage the crop is on, out of the total.":
        "Ekinin toplam içinde hangi büyüme aşamasında olduğu.",
    "Which hook is fitted and what it does to your odds.":
        "Hangi iğnenin takılı olduğu ve şansını nasıl değiştirdiği.",
    "Raw eggs never make you ill":
        "Çiğ yumurta sana asla dokunmaz",
    "{}%% wait before another anti-nausea food works":
        "Bir sonraki bulantı gidericinin etki etmesi için {}%% bekleme",
    "{}%% weapon sight range":
        "{}%% nişangâh menzili",
    "At Axe {} you swing as fast as a maxed axe user":
        "Balta {} iken ustası kadar hızlı vurursun",
    "{}%% from any poisonous food or drink":
        "Zehirli her yiyecek ve içecekten {}%%",
    "{}%% chance of illness from rotten food":
        "Bozuk yiyecekten hastalanma ihtimali {}%%",
    "Melee weapons":
        "Yakın dövüş silahları",
    "Firearms":
        "Ateşli silahlar",
    "Drinks":
        "İçecekler",
    "Skill XP":
        "Yetenek XP",
    "Weapons":
        "Silahlar",
    "Worn and carried":
        "Giysi ve çantalar",
    "Medicine and reading":
        "İlaç ve okuma",
    "Supplies":
        "Malzemeler",
    "Comparison":
        "Karşılaştırma",
    "Power and fuel":
        "Elektrik ve yakıt",
    "Animals and traps":
        "Hayvanlar ve tuzaklar",
    "Traits and jobs":
        "Özellikler ve meslekler",
    "Moodles":
        "Moodle'lar",
}
