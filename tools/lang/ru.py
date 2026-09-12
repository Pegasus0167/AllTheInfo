"""Russian phrase table for AllInfo.

Keys are the English fragment with every number replaced by {} in order.
Numbers are never written here: they ride through untouched. Use {0} {1} ...
instead of {} when the language needs a different order -- and then index every
slot, Python refuses to mix the two forms.

Run `python tools\i18n.py` after editing: it checks the arity of every line and
refuses to write a language file it cannot fill completely.
"""

T = {
    'x{} weapon damage (x{} untrained)':
        'x{} урона оружия (x{} без навыка)',
    '{} to the durability roll':
        '{} к броску износа',
    '{} chance to trip vaulting a fence':
        '{} к шансу споткнуться при перелезании забора',
    '{}%% fall damage':
        '{}%% урона при падении',
    'x{} endurance recovery (x{} untrained)':
        'x{} к восстановлению выносливости (x{} без навыка)',
    'x{} melee damage and knockback (x{} untrained)':
        'x{} урона в ближнем бою и отбрасывания (x{} без навыка)',
    'x{} carrying capacity (x{} untrained)':
        'x{} к грузоподъёмности (x{} без навыка)',
    'x{} move speed in combat stance (x{} untrained)':
        'x{} к скорости движения в боевой стойке (x{} без навыка)',
    'x{} sprint speed (x{} untrained)':
        'x{} к скорости спринта (x{} без навыка)',
    'x{} chance of being spotted (x{} untrained)':
        'x{} к шансу быть замеченным (x{} без навыка)',
    'x{} footstep noise (x{} untrained)':
        'x{} к шуму шагов (x{} без навыка)',
    "{} accuracy (the weapon's aiming modifier, {} on nearly every gun)":
        '{} к точности (модификатор прицеливания оружия, {} почти у всех стволов)',
    '{} wind penalty when aiming (of {})':
        '{} к штрафу за ветер при прицеливании (из {})',
    'x{} reload speed (x{} untrained)':
        'x{} к скорости перезарядки (x{} без навыка)',
    'x{} racking speed (x{} untrained)':
        'x{} к скорости передёргивания затвора (x{} без навыка)',
    'racking costs {} of the aiming time ({} untrained)':
        'передёргивание затвора стоит {} от времени прицеливания ({} без навыка)',
    'From here on you no longer count as unsteady with a firearm, as long as your Strength is {} or more: jam chance drops by {} percentage points.':
        'С этого уровня вы больше не считаетесь неуверенным стрелком, если Сила {} или выше: шанс заклинивания падает на {} процентных пункта.',
    'You never count as unsteady with a firearm again, whatever your Strength.':
        'Вы больше никогда не считаетесь неуверенным стрелком, какой бы ни была Сила.',
    '{} melee to-hit':
        '{} к точности в ближнем бою',
    '{} climb chance':
        '{} к шансу перелезть',
    '{} trip chance':
        '{} к шансу споткнуться',
    "{} to break a zombie's grab":
        '{} к попытке вырваться из захвата зомби',
    '{}%% strength':
        '{}%% силы',
    '{}%% healing':
        '{}%% к скорости лечения',
    'losing health':
        'здоровье падает',
    'harder to unjam a gun':
        'сложнее устранить заклинивание',
    '{} move speed (of {})':
        '{} к скорости движения (из {})',
    'body at {} C':
        'температура тела {} C',
    '{} carry capacity':
        '{} к грузоподъёмности',
    'x{} attack speed':
        'x{} к скорости атаки',
    'endurance under {}%%':
        'выносливость ниже {}%%',
    'fatigue over {}%%':
        'усталость выше {}%%',
    'hunger over {}%%':
        'голод выше {}%%',
    'thirst over {}%%':
        'жажда выше {}%%',
    'panic over {}%%':
        'паника выше {}%%',
    'stress over {}%%':
        'стресс выше {}%%',
    'boredom over {}%%':
        'скука выше {}%%',
    'unhappiness over {}%%':
        'уныние выше {}%%',
    '{}%% action speed':
        '{}%% к скорости действий',
    'anger over {}%%':
        'злость выше {}%%',
    'drunkenness over {}%%':
        'опьянение выше {}%%',
    'pain over {}%%':
        'боль выше {}%%',
    'slower rope climbing':
        'медленнее подъём по верёвке',
    '{}%% total body damage':
        '{}%% общего урона телу',
    'sickness over {}%%':
        'болезнь выше {}%%',
    'cold strength over {}%%':
        'сила простуды выше {}%%',
    'wetness over {}%%':
        'промокание выше {}%%',
    'discomfort over {}%%':
        'дискомфорт выше {}%%',
    'rotting corpses nearby':
        'рядом гниющие трупы',
    'x{} move speed':
        'x{} к скорости движения',
    '{} discomfort per level':
        '{} дискомфорта за уровень',
    '{} C on top of the air temperature':
        '{} C сверх температуры воздуха',
    'carrying {}x capacity':
        'нагрузка {}x от предела',
    '{}%% body heat':
        '{}%% тепла тела',
    'no sleep without pills':
        'не уснуть без снотворного',
    'erratic movement':
        'движение шатает',
    'raises discomfort':
        'повышает дискомфорт',
    'no sprinting':
        'нельзя спринтовать',
    'no sprinting, no exercise':
        'нельзя спринтовать и заниматься',
    'zombies spot you {} sooner':
        'зомби замечают вас на {} раньше',
    'muscle stiffness builds up':
        'накапливается мышечная скованность',
    'cannot eat or open food':
        'нельзя есть и открывать еду',
    '{} move speed with Adrenaline Junkie':
        '{} к скорости с чертой «Адреналиновый наркоман»',
    'nightmares while asleep':
        'кошмары во сне',
    'no sleep below {}%% fatigue without pills':
        'без снотворного не уснуть при усталости ниже {}%%',
    '{}%% move speed':
        '{}%% к скорости движения',
    'cannot move':
        'нельзя двигаться',
    '{} climbing walls and ropes':
        '{} к подъёму по стенам и верёвкам',
    'no running, no exercise':
        'нельзя бегать и заниматься',
    'over {}x capacity':
        'выше {}x от предела',
    'no running':
        'нельзя бегать',
    'no sprinting until you drop the bulky item':
        'нельзя спринтовать, пока не бросите громоздкий предмет',
    'you can sleep through high pain':
        'можно уснуть даже при сильной боли',
    'no endurance recovery':
        'выносливость не восстанавливается',
    '{} vision cone':
        '{} к конусу обзора',
    'delayed vehicle controls':
        'запаздывает управление машиной',
    'narrowed vision cone':
        'сужается конус обзора',
    'no exercise':
        'нельзя заниматься',
    '{} wound bleeding':
        'кровоточащих ран: {}',
    'Rest in peace.':
        'Покойся с миром.',
    'Infected. There is no cure.':
        'Заражение. Лекарства нет.',
    'Stale in':
        'Испортится через',
    'Rots in':
        'Сгниёт через',
    'Cooking time':
        'Время готовки',
    'Never':
        'Никогда',
    'Trains':
        'Прокачивает',
    'Critical chance':
        'Шанс крита',
    'Attack speed':
        'Скорость атаки',
    'Swing type':
        'Тип замаха',
    'Heavy':
        'Тяжёлый',
    'Swung':
        'Размашистый',
    'Stabbing':
        'Колющий',
    'Spear':
        'Копейный',
    'Stone':
        'Каменный',
    'Knockback on hit':
        'Отбрасывание при ударе',
    'Condition loss':
        'Потеря состояния',
    'Jam chance':
        'Шанс заклинивания',
    'Accuracy':
        'Точность',
    'Noise radius':
        'Радиус шума',
    'Rounds':
        'Патроны',
    'Reload time':
        'Время перезарядки',
    'Aiming time':
        'Время прицеливания',
    'Used by':
        'Подходит к',
    'Reading speed':
        'Скорость чтения',
    'Reading time left':
        'Осталось читать',
    'Skill too low to learn from it':
        'Навык слишком низкий, чтобы учиться по ней',
    'Nothing left to learn from it':
        'Больше нечему научиться',
    'Proteins':
        'Белки',
    'Sow in':
        'Сеять в',
    'Ready in':
        'Созреет через',
    'Burn time':
        'Время горения',
    # Power: charge, autonomy and light
    "Duration": "Длительность",
    "Light range": "Дальность света",
    "Light strength": "Яркость света",
    "Batteries and radios: charge left, how long it lasts and how far a torch lights": "Батарейки и радио: остаток заряда, время работы и дальность света фонарика",
    "Vanilla draws the charge of a drainable as a bar with no number on it, and never says how long a torch lasts or how far it lights. A torch spends its UseDelta once every ten game minutes, and only while it is in a hand or attached to you: left in a bag it switches itself off. Light range and strength are the figures that actually light the ground.":
        "Игра рисует заряд расходуемого предмета полоской без цифр и никогда не говорит, насколько хватит фонарика и как далеко он светит. Фонарик тратит свой UseDelta раз в десять игровых минут и только пока он в руке или закреплён на вас: в рюкзаке он выключается сам. Дальность и яркость света — это те цифры, которые действительно освещают землю.",
    'Rest quality':
        'Качество отдыха',
    'Discomfort':
        'Дискомфорт',
    'Stomp damage':
        'Урон от топтания',
    'Corpse sickness defense':
        'Защита от трупной болезни',
    'Filter charge':
        'Заряд фильтра',
    'New recipes':
        'Новые рецепты',
    'Listened':
        'Прослушано',
    'Skill too high for this tape':
        'Навык слишком высок для этой записи',
    'All Info':
        'All Info',
    'Enable everything':
        'Включить всё',
    'Items':
        'Предметы',
    'Crafting':
        'Крафт',
    'World':
        'Мир',
    'Character':
        'Персонаж',
    'Everything in this section':
        'Всё в этом разделе',
    'Food: time left before it spoils':
        'Еда: сколько осталось до порчи',
    'Adds hours to stale and hours to rotten, at the current rate. Accounts for the fridge, the freezer and the sandbox spoilage speed.':
        'Показывает, сколько часов до «несвежего» и до «гнилого» при нынешней скорости. Учитывает холодильник, морозильник и скорость порчи из настроек песочницы.',
    'Cooking: add the warm-up minutes':
        'Готовка: добавлять минуты на прогрев',
    'Off by default. Cooking time is the time at temperature; this adds the four minutes the food spends heating up before it starts to cook, so an oven timer set to the figure rings when the food is done.':
        'По умолчанию выключено. Время готовки указано для еды, уже прогретой до нужной температуры; эта настройка добавляет четыре минуты, которые еда тратит на прогрев перед началом готовки, чтобы таймер духовки прозвонил ровно тогда, когда всё готово.',
    'Food: calories, carbs, protein and fat':
        'Еда: калории, углеводы, белки и жиры',
    'Off by default. Showing macros on every food undoes the Nutritionist trait, which is what normally reveals them.':
        'По умолчанию выключено. Показ БЖУ на любой еде обесценивает черту «Диетолог», которая обычно их и открывает.',
    'Melee: exact damage, speed and durability':
        'Ближний бой: точный урон, скорость и прочность',
    'Puts numbers on the condition and damage bars, and adds crit chance, swing type, attack speed, knockback and the odds of losing a condition point per hit.':
        'Ставит числа на полоски состояния и урона и добавляет шанс крита, тип замаха, скорость атаки, отбрасывание и вероятность потерять очко состояния за удар.',
    'Firearms: range, jam chance and reload':
        'Огнестрел: дальность, заклинивание и перезарядка',
    'Puts numbers on the condition and damage bars, and adds accuracy, effective range, jam odds and magazine size.':
        'Ставит числа на полоски состояния и урона и добавляет точность, эффективную дальность, шанс заклинивания и ёмкость магазина.',
    'Ammo: rounds left and what it fits':
        'Патроны: сколько осталось и к чему подходят',
    'No comparison arrows here: the thing in your hands is a gun, not another magazine, so there is no honest pair to compare.':
        'Здесь нет стрелок сравнения: в руках у вас ствол, а не другой магазин, так что честной пары для сравнения просто нет.',
    'Clothing: numbers on every bar, plus discomfort':
        'Одежда: числа на всех полосках плюс дискомфорт',
    'Vanilla draws condition, insulation, wind, water, blood, dirt and wetness as bars with no figures. This writes the figures next to them and adds the discomfort value, which vanilla never shows at all.':
        'Игра рисует состояние, утепление, ветро- и водозащиту, кровь, грязь и промокание полосками без цифр. Здесь цифры пишутся рядом, плюс дискомфорт, который игра не показывает нигде.',
    'Seeds: growing time and yield':
        'Семена: время роста и урожай',
    'Firewood: how long it burns':
        'Дрова: сколько горят',
    'Books: reading time and skill levels covered':
        'Книги: время чтения и охваченные уровни навыка',
    'Reading time already accounts for Fast Reader, Slow Reader and reading glasses.':
        'Время чтения уже учитывает «Быстрое чтение», «Медленное чтение» и очки для чтения.',
    'Beds: how well you recover on them':
        'Кровати: насколько хорошо на них отдыхаешь',
    'Masks: filter life and protection':
        'Маски: ресурс фильтра и защита',
    'Tapes and CDs: which skill they teach and how much XP':
        'Кассеты и диски: какому навыку учат и сколько опыта дают',
    'Show the difference against what you have equipped':
        'Показывать разницу с тем, что надето и в руках',
    'Adds a coloured +/- next to weapon and clothing values. Weapons compare against what is in your hands, clothing against the piece worn in the same slot.':
        'Добавляет цветной +/- к значениям оружия и одежды. Оружие сравнивается с тем, что в руках, одежда — с вещью в том же слоте.',
    'Crafting: full item tooltip on the recipe output':
        'Крафт: полная подсказка предмета на результате рецепта',
    'Hovering the result of a recipe shows the same block an item in your inventory would, comparison included, before you craft it.':
        'Наведите на результат рецепта — увидите тот же блок, что и у предмета в инвентаре, вместе со сравнением, ещё до крафта.',
    'Generators: fuel time, wear and danger':
        'Генераторы: топливо, износ и опасность',
    'Adds noise radius, hours of fuel left, average time until {}%% condition and until it breaks, and the hourly odds of a backfire or a fire.':
        'Добавляет радиус шума, часы оставшегося топлива, среднее время до {}%% состояния и до поломки, а также почасовой шанс хлопка или пожара.',
    'Generators: also show times in real-world minutes':
        'Генераторы: показывать время и в реальных минутах',
    'Off by default. Converts the in-game hours using the current day length, so you know how long you actually have to wait.':
        'По умолчанию выключено. Переводит игровые часы по текущей длине суток, чтобы знать, сколько ждать на самом деле.',
    'Generators: outline the powered area on the floor':
        'Генераторы: очерчивать зону питания на полу',
    'Draws the edge of the range while the generator window is open, green when running and red when off. Only the floor you are standing on is computed.':
        'Рисует границу зоны, пока открыто окно генератора: зелёная, если он работает, красная, если нет. Считается только тот этаж, на котором вы стоите.',
    'Gas pumps: fuel left and power source':
        'Бензоколонки: остаток топлива и источник питания',
    'Adds an Info entry to the right-click menu of any gas pump, with the fuel still in the tank and whether the mains or a generator is keeping it running. The game knows that number and only prints it as a debug option.':
        'Добавляет пункт «Инфо» в меню правой кнопки на любой бензоколонке: сколько топлива осталось в баке и что её питает — сеть или ваш генератор. Игра знает это число и показывает его только как отладочный пункт.',
    'Fuel Remaining':
        'Остаток топлива',
    'Mains power':
        'Электросеть',
    'Generator':
        'Генератор',
    'Walls and doors: health under the cursor':
        'Стены и двери: прочность под курсором',
    'Shows current and maximum health as a number at the foot of whatever you point at, no clicking needed.':
        'Показывает текущую и максимальную прочность числом у основания того, на что вы наводите, без единого клика.',
    'Build menu: health of what you are about to build':
        'Меню строительства: прочность того, что собираетесь построить',
    'Also shows what that health would be with the relevant skill at {}, so you can tell whether it is worth waiting.':
        'Ещё показывает, какой была бы эта прочность при нужном навыке на {}, чтобы понять, стоит ли подождать.',
    'Crops: health, growth and water as numbers':
        'Грядки: здоровье, рост и полив числами',
    'Adds rows to the crop window you get by right-clicking a plant: health out of {}, current phase, hours to the next one, water level against what the plant needs, time since the last watering and pest levels.':
        'Добавляет строки в окно растения по правому клику: здоровье из {}, текущая фаза, часы до следующей, уровень воды против того, что растению нужно, время с последнего полива и уровень каждого вредителя.',
    "Crops: keep vanilla's Farming level requirements":
        'Грядки: сохранить требования по уровню Земледелия',
    'Off by default, so you see everything from level {}. Turn it on and each row reappears at the Farming level vanilla itself uses for it: phase and health at {}, water at {}, pests at {}, next phase at {}.':
        'По умолчанию выключено, так что всё видно с {} уровня. Включите — и каждая строка вернётся на тот уровень Земледелия, который использует сама игра: фаза и здоровье на {}, вода на {}, вредители на {}, следующая фаза на {}.',
    'Noise':
        'Шум',
    'tiles':
        'клеток',
    'Down to %1%% (avg)':
        'До %1%% (в среднем)',
    'Breaks down in (avg)':
        'Сломается через (в среднем)',
    'Backfire, loud (per hour)':
        'Хлопок, громко (за час)',
    'FIRE OR EXPLOSION (per hour)':
        'ПОЖАР ИЛИ ВЗРЫВ (за час)',
    '(real time)':
        '(реальное время)',
    'XP Boost: %1':
        'Бонус опыта: %1',
    'Skills':
        'Навыки',
    'Also grants':
        'Также даёт',
    'Disabled in multiplayer':
        'Отключено в мультиплеере',
    'Foraging':
        'Собирательство',
    'search radius':
        'радиус поиска',
    'weather penalty':
        'штраф за погоду',
    'darkness penalty':
        'штраф за темноту',
    'Strength when built':
        'Прочность при постройке',
    'With %1 at {}':
        'С %1 на {}',
    'Show XP boosts as a multiplier, not a percentage':
        'Показывать бонусы опыта множителем, а не процентом',
    'Vanilla says "{}%%" for a level {} boost. The real figure is x{}, because a skill with no boost runs at a quarter rate. Fixed on all three screens that show it.':
        'Игра пишет «{}%%» для бонуса {} уровня. На деле это x{}, потому что навык без бонуса идёт вчетверо медленнее. Исправлено на всех трёх экранах, где это показывается.',
    'Character creation: what each trait and job really does':
        'Создание персонажа: что на самом деле делает каждая черта и профессия',
    'Adds starting skill levels with their true XP multiplier, free traits granted, recipes taught and foraging bonuses to the tooltips in the creation screen.':
        'Добавляет в подсказки на экране создания стартовые уровни навыков с настоящим множителем опыта, бесплатные черты, изучаемые рецепты и бонусы собирательства.',
    'In game: the same block on the info tab':
        'В игре: тот же блок на вкладке информации',
    'Hover a trait icon or the job icon in the character info tab to read the same block after the world has started.':
        'Наведите на значок черты или профессии на вкладке информации, чтобы прочитать тот же блок уже в игре.',
    'Add hand-written trait effects':
        'Добавить эффекты черт, вписанные вручную',
    "Effects hardcoded in the game's Java that cannot be read at runtime, so they are written by hand and checked against each build.":
        'Эффекты зашиты в Java игры и не читаются на лету, поэтому вписаны вручную и сверены с этой сборкой.',
    'Skills: which recipes each level requires':
        'Навыки: какие рецепты требуют этого уровня',
    "Hover a level in the skills panel to see the recipes and builds that ask for it. Read from the game's own recipe list, so modded recipes appear too and nothing goes stale with a patch.":
        'Наведите на уровень в панели навыков, чтобы увидеть рецепты и постройки, которым он нужен. Читается из списка рецептов самой игры, так что рецепты из модов тоже попадают, и ничто не устаревает после патча.',
    'Needs this level':
        'Требуют этого уровня',
    'Skill and moodle descriptions are translation files. They cannot be switched off here; disable the mod to remove them.':
        'Описания навыков и моудлов — это файлы перевода. Отключить их здесь нельзя; чтобы убрать, выключите мод.',
    'Run self-test':
        'Запустить самопроверку',
    '{}%% footstep noise radius':
        '{}%% к радиусу шума шагов',
    'more likely to fall when bumped':
        'чаще падаете от толчка',
    'less likely to fall when bumped':
        'реже падаете от толчка',
    '{}%% run and sprint speed':
        '{}%% к скорости бега и спринта',
    'no Fitness XP from level {} on':
        'с {} уровня опыт Физподготовки больше не идёт',
    'double endurance drain when running':
        'вдвое быстрее тратится выносливость при беге',
    '{}%% melee damage':
        '{}%% урона в ближнем бою',
    '{} chance to trip from a lunge':
        '{} к шансу споткнуться при выпаде',
    'starts at {} weight, and you lose health below {}':
        'начинается с веса {}, ниже {} здоровье начинает падать',
    '{}%% axe swing time':
        '{}%% к времени замаха топором',
    '{}%% axe damage to trees':
        '{}%% урона топором по деревьям',
    '{}%% endurance lost running':
        '{}%% выносливости тратится на бег',
    '{}%% grapple effectiveness':
        '{}%% к эффективности в захвате',
    '{}%% knockback':
        '{}%% к отбрасыванию',
    'can be gained by training Strength to {}':
        'получается прокачкой Силы до {}',
    'becomes Strong at Strength {}':
        'на Силе {} переходит в «Сильный»',
    'becomes Feeble at Strength {}':
        'на Силе {} переходит в «Немощный»',
    'lost by training Strength to {}':
        'теряется при прокачке Силы до {}',
    '{}%% panic, night terrors aside':
        '{}%% паники, кроме ночных кошмаров',
    '{}%% stress from looting corpses':
        '{}%% стресса от обыска трупов',
    '{}%% panic':
        '{}%% паники',
    'no panic from a corpse reanimating':
        'нет паники, когда труп оживает',
    'no stress from looting corpses':
        'обыск трупов не даёт стресса',
    '{} move speed at panic {}':
        '{} к скорости при панике {}',
    'still capped by the movement speed limit':
        'всё равно упирается в предел скорости',
    '{}%% wind penalty when aiming':
        '{}%% к штрафу за ветер при прицеливании',
    '{}%% gun accuracy':
        '{}%% к точности огнестрела',
    '{}%% gun crit chance':
        '{}%% к шансу крита из огнестрела',
    'shorter aiming delay':
        'короче задержка прицеливания',
    'wider field of view':
        'шире поле зрения',
    '{}%% max range on weapon sights':
        '{}%% к максимальной дальности прицелов',
    'blurry vision':
        'размытое зрение',
    'weapon sight range bonus at its minimum':
        'бонус дальности прицела на минимуме',
    'cancelled by wearing glasses':
        'снимается очками',
    '{}%% perception radius':
        '{}%% к радиусу восприятия',
    'zombies behind you become visible sooner':
        'зомби за спиной становятся видны раньше',
    'muffled sound effects':
        'приглушённые звуки',
    'zombies behind you become visible later':
        'зомби за спиной становятся видны позже',
    'no sound at all':
        'звука нет вообще',
    'you can still watch TV':
        'телевизор смотреть всё равно можно',
    '{}%% chance of not being injured by a zombie':
        '{}%% к шансу не получить рану от зомби',
    '{}%% chance of being scratched by trees':
        '{}%% к шансу оцарапаться о деревья',
    '{}%% corpse sickness':
        '{}%% трупной болезни',
    '{}%% chance of catching a cold':
        '{}%% к шансу простудиться',
    '{}%% cold strength':
        '{}%% к силе простуды',
    '{}%% cold progression':
        '{}%% к развитию простуды',
    '{}%% zombification speed':
        '{}%% к скорости зомбификации',
    '{}%% severity of vehicle injuries':
        '{}%% к тяжести автомобильных травм',
    '{}%% fracture severity':
        '{}%% к тяжести переломов',
    'all wounds heal much faster':
        'все раны заживают гораздо быстрее',
    'all wounds heal much slower':
        'все раны заживают гораздо медленнее',
    '{}%% XP in every skill except Fitness and Strength':
        '{}%% опыта во всех навыках, кроме Физподготовки и Силы',
    '{}%% reading speed':
        '{}%% к скорости чтения',
    '{}%% XP in every weapon skill and Aiming':
        '{}%% опыта во всех оружейных навыках и Меткости',
    '{}%% inventory transfer time':
        '{}%% к времени перекладывания вещей',
    '{}%% aiming delay':
        '{}%% к задержке прицеливания',
    'guns jam less often':
        'оружие реже клинит',
    'fewer injuries opening cans':
        'реже режетесь, открывая консервы',
    'guns jam more often':
        'оружие чаще клинит',
    'more injuries opening cans':
        'чаще режетесь, открывая консервы',
    '{}%% container capacity':
        '{}%% к вместимости контейнеров',
    'crafting does not return leftover items':
        'крафт не возвращает остатки',
    '{}%% thirst':
        '{}%% жажды',
    '{}%% hunger':
        '{}%% голода',
    '{}%% food illness chance':
        '{}%% к шансу пищевого отравления',
    '{}%% food illness duration':
        '{}%% к длительности пищевого отравления',
    '{}%% harm from tainted water':
        '{}%% вреда от грязной воды',
    '{}%% tiredness gained while awake':
        '{}%% усталости, накопленной за день',
    '{}%% recovery while asleep':
        '{}%% восстановления во сне',
    '{}%% sleep duration':
        '{}%% к длительности сна',
    'you do not wake up at {} tiredness, so set an alarm':
        'вы не просыпаетесь при усталости {}, так что заводите будильник',
    'harder to fall asleep':
        'тяжелее заснуть',
    '{}%% vision in the dark':
        '{}%% к зрению в темноте',
    'smaller vision cone penalty at night':
        'меньше штраф к конусу обзора ночью',
    '{}%% chance of being spotted (new stealth)':
        '{}%% к шансу быть замеченным (новый стелс)',
    '{}%% chance of being spotted (old stealth)':
        '{}%% к шансу быть замеченным (старый стелс)',
    '{}%% chance of breaking kindling':
        '{}%% к шансу сломать растопку',
    '{}%% weather penalty when aiming':
        '{}%% к штрафу за погоду при прицеливании',
    'lights fires twice as fast':
        'разводит огонь вдвое быстрее',
    'almost never scratched by trees':
        'деревья почти никогда не царапают',
    '{}%% endurance lost running, sprinting, carrying and dragging':
        '{}%% выносливости тратится на бег, спринт, переноску и волочение',
    '{}%% endurance lost swinging a weapon':
        '{}%% выносливости тратится на замах оружием',
    '{}%% gear change speed':
        '{}%% к скорости переключения передач',
    '{}%% top speed':
        '{}%% к максимальной скорости',
    '{}%% engine noise in reverse':
        '{}%% шума двигателя на задней передаче',
    '{}%% acceleration':
        '{}%% к разгону',
    '{}%% reverse acceleration':
        '{}%% к разгону задним ходом',
    'capped at {} max speed':
        'максимальная скорость ограничена {}',
    'engine noise unchanged':
        'шум двигателя не меняется',
    'less likely to fail any fence climb':
        'реже срываетесь при перелезании любого забора',
    'slightly faster rope climbing':
        'чуть быстрее подъём по верёвке',
    'bloody items transfer faster but cause stress':
        'окровавленные вещи перекладываются быстрее, но дают стресс',
    'cannot read anything, map labels and calorie counts included':
        'нельзя читать вообще ничего, включая подписи на карте и калории',
    '{} panic per tick indoors, scaling down to {} in a {}-tile room':
        '{} паники за тик в помещении, снижаясь до {} в комнате на {} клеток',
    'a vehicle counts as a {}-tile room':
        'машина считается комнатой на {} клеток',
    '{} panic per tick whenever you are not in a room':
        '{} паники за тик, пока вы не в помещении',
    'faster building':
        'быстрее строительство',
    'faster barricading':
        'быстрее забаррикадирование',
    'no bonus health on constructions in B{}':
        'в B{} не даёт постройкам дополнительной прочности',
    'recipes need one level less of their skill':
        'рецепты требуют на уровень меньше своего навыка',
    'you gain weight above {} calories a day instead of {}, while under {} weight':
        'вес растёт выше {} калорий в день вместо {}, пока вес ниже {}',
    'you need {} calories a day to gain weight instead of {}, while over {} weight':
        'чтобы набрать вес, нужно {} калорий в день вместо {}, пока вес выше {}',
    'unhappiness and stress rise as nicotine withdrawal builds':
        'уныние и стресс растут по мере никотиновой ломки',
    'smoking clears the withdrawal and gives {} hunger':
        'курение снимает ломку и даёт {} голода',
    'random coughs and sneezes give you away':
        'случайный кашель и чихание выдают вас',
    'shows calories, carbohydrates, protein and fat on every food':
        'показывает калории, углеводы, белки и жиры у любой еды',
    "no measurable effect in B{}: no XP boost, no recipes, and nothing in the game's code reads it. The recipes come from the profession itself.":
        'в B{} никакого измеримого эффекта: ни бонуса опыта, ни рецептов, и ни одна строка кода игры её не читает. Рецепты даёт сама профессия.',
    'x{} move speed through trees (x{} for everyone else)':
        'x{} к скорости движения среди деревьев (x{} у всех остальных)',
    'starts every exercise at {}{} regularity instead of {}{}':
        'каждое упражнение начинается с регулярностью {}{} вместо {}{}',
    '{} move speed':
        '{} к скорости движения',
    '{} wind penalty when aiming':
        '{} к штрафу за ветер при прицеливании',
    '%1 °C':
        '%1 °C',
    'Adds rows to the inventory tooltip: how fast a line wears out, how much each hook helps and which fish a bait attracts.':
        'Добавляет строки в подсказку инвентаря: как быстро изнашивается леска, насколько помогает каждый крючок и какую рыбу приманивает наживка.',
    'ALLTHEINFO':
        'ALLTHEINFO',
    'Attracts':
        'Приманивает',
    "Back to vanilla's rules: Time needs Fishing {}, Temperature {}, Weather {}, Wind {}, and a species tells you nothing until you have caught it.":
        'Назад к правилам игры: время требует Рыбалку {}, температура {}, погода {}, ветер {}, а вид рыбы молчит, пока вы его не поймали.',
    'Best baits: %1':
        'Лучшие наживки: %1',
    'Bite chance':
        'Шанс поклёвки',
    'Breaks into':
        'Ломается в',
    'Chance that one attempt hooks something: {}%% times temperature, weather, time, hook and abundance, capped at {}%%.':
        'Шанс, что попытка зацепит добычу: {}%% умножить на температуру, погоду, время, крючок и обилие рыбы, но не больше {}%%.',
    'Fish bite more at dawn and dusk: x{} from {}:{} to {}:{} and from {}:{} to {}:{}. Any other hour is x{}.':
        'Рыба клюёт лучше на рассвете и на закате: x{} с {}:{} до {}:{} и с {}:{} до {}:{}. В любой другой час x{}.',
    'Fishing gear: rods, lines, hooks and baits':
        'Рыболовные снасти: удочки, лески, крючки и наживки',
    'Fishing panel: what each rating is worth':
        'Панель рыбалки: сколько стоит каждая оценка',
    "Fishing: keep vanilla's Fishing level requirements":
        'Рыбалка: сохранить требования игры к уровню Рыбалки',
    'Hook':
        'Крючок',
    'How much longer than the best possible case you wait between attempts. Fishing near the shore doubles it, and a bobber less than {} tiles away triples it.':
        'Насколько дольше вы ждёте между попытками по сравнению с лучшим случаем. Рыбалка у берега удваивает ожидание, а поплавок ближе {} клеток утраивает.',
    'Lake':
        'Озеро',
    'Line strength':
        'Прочность лески',
    'Moodles: description box that fits its text':
        'Мудлы: окно описания по размеру текста',
    'Needs Fishing %1':
        'Нужна Рыбалка %1',
    'Only bites while you reel in':
        'Клюёт только когда вы подматываете',
    'Paperclip x{}, nail x{}, fishing hook x{}. With no hook the chance is x{}: nothing will ever bite.':
        'Скрепка x{}, гвоздь x{}, рыболовный крючок x{}. Без крючка шанс x{}: не клюнет никогда.',
    'Rain is x{}. Fog over {} or wind over {} is x{}. Fog and wind are the same x{}: they never stack.':
        'Дождь x{}. Туман выше {} или ветер выше {} дают x{}. Туман и ветер — это один и тот же x{}: они не складываются.',
    'Right-click water and pick Fishing. Puts the real multiplier next to Time, Temperature, Weather and Wind, adds hook, spot, bite chance and waiting time, and explains each one on hover.':
        'Щёлкните правой кнопкой по воде и выберите рыбалку. Ставит настоящий множитель рядом со временем, температурой, погодой и ветром, добавляет крючок, место, шанс поклёвки и ожидание и поясняет каждое при наведении.',
    'River':
        'Река',
    'Spot':
        'Место',
    "The game's own moodle box is two lines tall and cuts off anything longer, which is most of AllTheInfo's descriptions. This draws the moodle column itself so the box grows with the text. Turn it off to go back to the vanilla widget.":
        'Окно мудла в игре высотой в две строки и обрезает всё, что длиннее, а это почти все описания AllTheInfo. Здесь колонка мудлов рисуется сама, поэтому окно растёт вместе с текстом. Выключите, чтобы вернуть виджет игры.',
    'Trophy from %1 cm, Fishing {} and a {} in {} roll on a big catch':
        'Трофей от %1 см, при Рыбалке {} и броске {} из {} на крупной добыче',
    'Under {} fish is x{}, up to {} is x{}, over {} is x{}. Trash is what you pull out instead of a fish, and Fishing {} cuts it to {}%%, level {} to {}%% and level {} to {}%%.':
        'Меньше {} рыб — x{}, до {} — x{}, больше {} — x{}. Мусор — это то, что вы вытаскиваете вместо рыбы, и Рыбалка {} снижает его до {}%%, уровень {} до {}%%, уровень {} до {}%%.',
    'Up to %1 cm and %2 kg':
        'До %1 см и %2 кг',
    'Vanilla draws condition, insulation, wind, water, blood, dirt and wetness as bars with no figures. This writes the figures next to them and adds the discomfort value, which vanilla never shows at all. The run and combat speed modifiers get a signed figure too, which vanilla only ever draws as a bar with no sign.':
        'В игре состояние, утепление, защита от ветра и воды, кровь, грязь и влага показаны полосками без цифр. Здесь цифры пишутся рядом, плюс значение дискомфорта, которого игра не показывает вовсе. Модификаторы скорости бега и боя тоже получают цифру со знаком, а игра рисует их полоской без знака.',
    'Wait':
        'Ожидание',
    'Waters: %1':
        'Воды: %1',
    'Wear per tug':
        'Износ за рывок',
    'Wind has no coefficient of its own. Over {} it sets the weather to x{}, the same penalty fog sets, and the two do not add up.':
        'У ветра нет своего коэффициента. Выше {} он ставит погоде x{}, тот же штраф, что и туман, и они не складываются.',
    'With your bait: %1%%':
        'С вашей наживкой: %1%%',
    'Your bait does not attract this one':
        'Ваша наживка не привлекает этот вид',
    'best possible':
        'лучшее возможное',
    'near shore':
        'у берега',
    'no fish in this spot':
        'здесь нет рыбы',
    'none':
        'нет',
    'trash':
        'мусор',
    '{} to {} °C is x{}. From {} to {} and from {} to {}, x{}. Over {} or below {}, x{}. Below {} °C, x{}.':
        'От {} до {} °C — x{}. От {} до {} и от {} до {}, x{}. Выше {} или ниже {}, x{}. Ниже {} °C, x{}.',
    'Fish':
        'Рыба',
    'Trash':
        'Мусор',
    'Trophy from %1 cm':
        'Трофей от %1 см',
    'shore':
        'берег',
    'Best baits:':
        'Лучшие наживки:',
    'Size: %1-%2 cm, %3-%4 kg':
        'Размер: %1-%2 см, %3-%4 кг',
    'Trophy: >%1 cm / >%2 kg':
        'Трофей: >%1 см / >%2 кг',
    'Under {} fish is x{}, up to {} is x{}, over {} is x{}. Fish schools move every day. Trash is what you pull out instead of a fish: it is fixed per spot, and Fishing {} cuts it to {}%%, level {} to {}%% and level {} to {}%%.':
        'Меньше {} рыб — x{}, до {} — x{}, больше {} — x{}. Косяки рыбы каждый день перемещаются. Мусор — это то, что вы вытаскиваете вместо рыбы: он постоянен для каждого места, и Рыбалка {} снижает его до {}%%, уровень {} до {}%%, уровень {} до {}%%.',
    'Fishing gear: hide the combat stats':
        'Рыболовные снасти: скрыть боевые характеристики',
    "Fog over {}%% sets the weather to x{}, the same penalty wind sets, and the two never stack. Vanilla's Weather row reports neither: it says Good for rain even in a gale.":
        'Туман выше {}%% ставит погоде x{}, тот же штраф, что и ветер, и они никогда не складываются. Строка погоды в игре не сообщает ни о том, ни о другом: при дожде она пишет «хорошо» даже в шторм.',
    'Rain is x{}. Fog over {}%% or wind over {}%% is x{}. Fog and wind are the same x{}: they never stack.':
        'Дождь x{}. Туман выше {}%% или ветер выше {}%% дают x{}. Туман и ветер — это один и тот же x{}: они не складываются.',
    "Rods, nets and fishing spears are weapons in the game's own scripts, so they get crit chance, swing type, attack speed and knockback. This drops that block on fishing gear. The condition and damage bars are drawn by the game in one call and cannot be removed by any mod.":
        'Удочки, сети и остроги в скриптах самой игры являются оружием, поэтому получают шанс крита, тип удара, скорость атаки и отбрасывание. Это убирает такой блок у рыболовных снастей. Полоски состояния и урона игра рисует одним вызовом, и убрать их не может ни один мод.',
    'Wind has no coefficient of its own. Over {}%% it sets the weather to x{}, the same penalty fog sets, and the two do not add up.':
        'У ветра нет своего коэффициента. Выше {}%% он ставит погоде x{}, тот же штраф, что и туман, и они не складываются.',
    'Against the best possible case':
        'по сравнению с лучшим возможным случаем',
    'Any other hour: x{}':
        'Любой другой час: x{}',
    'Below {} °C: x{}':
        'Ниже {} °C: x{}',
    'Bobber under {} tiles away: x{}':
        'Поплавок ближе {} клеток: x{}',
    'Capped at {}%%':
        'Не больше {}%%',
    'Fishing hook: x{}':
        'Рыболовный крючок: x{}',
    'Fishing {}, {} and {} cut trash to {}%%, {}%% and {}%%':
        'Рыбалка {}, {} и {} снижают мусор до {}%%, {}%% и {}%%',
    'Fog and wind never stack':
        'Туман и ветер не складываются',
    'Fog over {}%% or wind over {}%%: x{}':
        'Туман выше {}%% или ветер выше {}%%: x{}',
    'Nail: x{}':
        'Гвоздь: x{}',
    'Near shore: x{}':
        'У берега: x{}',
    'No hook: x{}, nothing ever bites':
        'Без крючка: x{}, не клюнет никогда',
    'Over {} or below {} °C: x{}':
        'Выше {} или ниже {} °C: x{}',
    'Over {}%%: x{} on the weather':
        'Выше {}%%: x{} к погоде',
    'Over {}: x{}':
        'Больше {}: x{}',
    'Paperclip: x{}':
        'Скрепка: x{}',
    'Rain: x{}':
        'Дождь: x{}',
    'Rolled once per attempt':
        'Бросок на каждую попытку',
    'Same penalty as fog, they never stack':
        'Тот же штраф, что и у тумана, они не складываются',
    'Same penalty as wind, they never stack':
        'Тот же штраф, что и у ветра, они не складываются',
    'Schools move every day':
        'Косяки перемещаются каждый день',
    'This row reports neither':
        'Эта строка не сообщает ни о том, ни о другом',
    'Trash is fixed per spot':
        'Мусор постоянен для каждого места',
    'Under {} fish: x{}':
        'Меньше {} рыб: x{}',
    '{} to {} and {} to {} °C: x{}':
        'От {} до {} и от {} до {} °C: x{}',
    '{} to {} °C: x{}':
        'От {} до {} °C: x{}',
    '{} to {}: x{}':
        'От {} до {}: x{}',
    '{}%% x temperature x weather x time x hook x fish':
        '{}%% x температура x погода x время x крючок x рыба',
    '{}:{} to {}:{} and {}:{} to {}:{}: x{}':
        'С {}:{} до {}:{} и с {}:{} до {}:{}: x{}',
    'Fishing {}, {} and {}: trash x{}, x{}, x{}':
        'Рыбалка {}, {} и {}: мусор x{}, x{}, x{}',
    'x time x hook x fish':
        'x время x крючок x рыба',
    '{}%% x temperature x weather':
        '{}%% x температура x погода',

    # Round 11: moodles rewritten from bytecode + wiki
    "melee damage {}%%": "{}%% к урону в ближнем бою",
    "melee damage {}": "{} к урону в ближнем бою",
    "move speed {}%%": "{}%% к скорости передвижения",
    "move speed {}%% with Adrenaline Junkie": "{}%% к скорости с чертой «Адреналиновый наркоман»",
    "attack speed {}%%": "{}%% к скорости атаки",
    "combat speed {}%%": "{}%% к скорости боя",
    "run speed {}%%": "{}%% к скорости бега",
    "crit chance {}%%": "{}%% к шансу крита",
    "firearm accuracy {}%%": "{}%% к точности огнестрела",
    "firearm accuracy {}%% at {} tiles": "{0}%% к точности огнестрела на {1} клеток",
    "clearing a jam {}%%": "{}%% к шансу устранить перекос",
    "climbing {}%%": "{}%% к лазанию",
    "climbing fences {}%%": "{}%% к перелезанию через забор",
    "climbing walls and ropes {}%%": "{}%% к лазанию по стенам и верёвкам",
    "tripping over fences {}%%": "{}%% к шансу споткнуться о забор",
    "blocking an attack {}%%": "{}%% к блоку атаки",
    "foraging {}%%": "{}%% к собирательству",
    "carry capacity {}": "{} к грузоподъёмности",
    "healing {}%%": "{}%% к скорости лечения",
    "healing x{}": "лечение x{}",
    "poison wears off {}%% faster": "Яд выводится на {}%% быстрее",
    "heat dissipation {}%%": "{}%% к отводу тепла",
    "heat loss {}%%": "{}%% к потере тепла",
    "discomfort {}%%": "{}%% к дискомфорту",
    "medicine {}%% less effective": "Лекарства слабее на {}%%",
    "sleep {}{}%% less effective": "Сон слабее на {0}{1}%%",
    "panic x{} per wound": "паника x{} за рану",
    "over {}%% of capacity": "Более {}%% грузоподъёмности",
    "health under {}%%": "Здоровье ниже {}%%",
    "health {}%% per hour": "{}%% здоровья в час",
    "health drops to {}%%": "Здоровье падает до {}%%",
    "health drops to {}%%, then to {}%%": "Здоровье падает до {0}%%, затем до {1}%%",
    "health drops to {}%% when the air is above {} C": "Здоровье падает до {0}%%, когда воздух выше {1} C",
    "health drops when the air is below {} C": "Здоровье падает, когда воздух ниже {} C",
    "only heals indoors, dry, under {}%% fatigue and under {}%% hunger and thirst": "Проходит только в помещении, всухую, при усталости ниже {}%% и голоде и жажде ниже {}%%",
    "vision cone narrows, cancelling Eagle Eyed": "Конус обзора сужается и отменяет Орлиный глаз",
    "{} C colder than the air": "На {} C холоднее воздуха",
    "{} wounds bleeding": "{} кровоточащие раны",
    "{} wounds, or a bleeding neck": "{} раны или рана на шее",
    "no healing": "Лечение не идёт",
    "no natural healing": "Естественное лечение не идёт",
    "slower healing": "Лечение медленнее",
    "much slower healing": "Лечение намного медленнее",
    "slower endurance recovery": "Выносливость восстанавливается медленнее",
    "much slower endurance recovery": "Выносливость восстанавливается намного медленнее",
    "endurance barely recovers": "Выносливость почти не восстанавливается",
    "endurance drains as you move and never recovers": "Выносливость тратится при движении и не восстанавливается",
    "no sprinting or running": "Ни спринта, ни бега",
    "you cannot run": "Вы не можете бежать",
    "you cannot sleep": "Вы не можете спать",
    "you cannot eat any more": "Вы больше не можете есть",
    "you can sleep on the ground and through pain": "Вы можете спать на земле и сквозь боль",
    "cannot swing a sledgehammer": "Кувалда больше не поднимается",
    "hunger does not rise": "Голод не растёт",
    "less body heat generated": "Меньше тепла вырабатывается",
    "body heat rises": "Температура тела растёт",
    "body heat rises sharply": "Температура тела резко растёт",
    "thirst and fatigue rise faster": "Жажда и усталость растут быстрее",
    "you lose heat in the cold": "Вы теряете тепло на холоде",
    "more likely to catch a cold": "Выше шанс простудиться",
    "more likely to fall ill": "Выше шанс заболеть",
    "much more likely to fall ill": "Намного выше шанс заболеть",
    "narrower vision cone": "Конус обзора уже",
    "narrower vision and awareness": "Обзор и внимание снижены",
    "movement, damage and attack speed drop with the wound": "Скорость, урон и скорость атаки падают в зависимости от раны",
    "you make noise": "Вы издаёте шум",
    "you complain out loud": "Вы жалуетесь вслух",
    "you get up faster": "Вы встаёте быстрее",
    "you weave as you walk": "Вас шатает при ходьбе",
    "timed actions take longer": "Действия занимают больше времени",
    "unhappiness rises": "Уныние растёт",
    "unhappiness rises slowly": "Уныние растёт медленно",
    "unhappiness rises fast": "Уныние растёт быстро",
    "stress rises": "Стресс растёт",
    "boredom is wiped and held down": "Скука обнуляется и не растёт",
    "the Desensitized trait cancels it": "Черта «Толстокожий» это отменяет",
    "no effect until NPCs return": "Без эффекта, пока не вернутся NPC",
    "discomfort while in a vehicle": "Дискомфорт в транспорте",
    "hypothermia is hidden": "Переохлаждение скрыто",
    "it wakes you up": "Это вас будит",
    "you sneeze now and then": "Вы иногда чихаете",
    "you sneeze and cough often": "Вы часто чихаете и кашляете",
    "you cough so much that hiding gets hard": "Вы кашляете так, что прятаться трудно",
    "you cough constantly and draw zombies": "Вы кашляете без остановки и привлекаете зомби",
    "health loss": "Потеря здоровья",
    "slow health loss": "Медленная потеря здоровья",
    "serious health loss": "Серьёзная потеря здоровья",
    "health slowly drops": "Здоровье медленно падает",
    "health drops if this is infection or poison": "Здоровье падает, если это заражение или яд",
    "death without first aid": "Смерть без первой помощи",
    "sickness starts to build": "Болезнь начинает нарастать",
    "sickness builds noticeably": "Болезнь заметно нарастает",
    "many rotting corpses": "Много гниющих трупов",
    "more rotting corpses": "Больше гниющих трупов",
    "the worst corpses can do": "Худшее, что дают трупы",
    "a generator running indoors": "Генератор работает в помещении",
    "it will not kill you outright": "Это не убьёт вас сразу",
    "a gas mask or SCBA prevents it": "Противогаз или дыхательный аппарат это предотвращает",
    "caused by heavy clothing, bags, bare feet or leg injuries": "Из-за тяжёлой одежды, сумок, босых ног или ран на ногах",

    # Animals (round 10, block C)
    "Animals: butchering yield, milk, wool and old age":
        "Животные: выход мяса, молоко, шерсть и старость",
    "Adds rows to the animal window you get by right-clicking an animal: meat yield, blood, feathers, old age and weight ceiling, which no screen shows, plus health, hunger, thirst, attitude, milk, wool and pregnancy as numbers instead of words.":
        "Добавляет строки в окно животного по правому клику: выход мяса, кровь, перья, старость и предельный вес, которых нет ни на одном экране, плюс здоровье, голод, жажда, нрав, молоко, шерсть и беременность числами вместо слов.",
    "Animals: keep vanilla's Animal Care level requirements":
        "Животные: сохранить требования по уровню Ухода за животными",
    "Off by default, so you see everything from level {}. Turn it on and each row reappears at the Animal Care level vanilla itself uses for it: pregnancy at {}, weight at {}, attitude at {}.":
        "По умолчанию выключено, так что всё видно с {} уровня. Включите — и каждая строка вернётся на тот уровень Ухода за животными, который использует сама игра: беременность на {}, вес на {}, нрав на {}.",
    "Meat yield":
        "Выход мяса",
    "full in %1":
        "заполнится через %1",

    # Animal hover descriptions (round 12)
    "Size x meat gene.":
        "Размер x ген мяса.",
    "Multiplies the number of meat pieces and the calories of each one.":
        "Умножает число куском мяса и калории каждого из них.",
    "Butchering adds x{} every {} levels.":
        "Разделка добавляет x{} каждые {} уровня.",
    "Off the ground x{}, on a butcher hook x{}.":
        "С земли x{}, на крюке мясника x{}.",
    "Litres you can drain into a bucket once it is dead.":
        "Литры, которые можно слить в ведро после смерти.",
    "Grows with weight.":
        "Растёт вместе с весом.",
    "Feathers you get for butchering it.":
        "Перья, которые дают за разделку.",
    "Breed maximum x size.":
        "Максимум породы x размер.",
    "{}%% until {}%% of its life expectancy, then it climbs to {}%%.":
        "{}%% до {}%% ожидаемой продолжительности жизни, затем растёт до {}%%.",
    "Over {}%% it loses {}%% health every hour.":
        "Выше {}%% теряет {}%% здоровья каждый час.",
    "Current weight and the most this animal can reach.":
        "Текущий вес и максимум, которого это животное может достичь.",
    "Meat and blood both scale with it.":
        "Мясо и кровь зависят от него.",
    "Over {}%% hunger it starts losing weight.":
        "При голоде выше {}%% начинает терять вес.",
    "{}{}, how much this animal puts up with you.":
        "{}{}, насколько животное вас терпит.",
    "Each point takes {} off the chance it breaks free while being sheared.":
        "Каждый пункт снижает на {} шанс, что оно вырвется при стрижке.",
    "Every gain is {}, plus {} per Animal Care level.":
        "Каждая прибавка — {}, плюс {} за уровень Ухода за животными.",
    "Healthy over {}%%, off colour over {}%%, sickly over {}%%, dying below.":
        "Здоровое выше {}%%, недомогает выше {}%%, болеет выше {}%%, умирает ниже.",
    "Higher is worse.":
        "Чем выше, тем хуже.",
    "Well fed under {}%%, underfed under {}%%, starving over it.":
        "Сыто ниже {}%%, недокормлено ниже {}%%, голодает выше.",
    "Over {}%% it starts losing weight.":
        "Выше {}%% начинает терять вес.",
    "Fully watered under {}%%, thirsty under {}%%, dying of thirst over it.":
        "Напоено ниже {}%%, хочет пить ниже {}%%, умирает от жажды выше.",
    "{}{}. Calm under {}, unnerved under {}, agitated under {}, wild over it.":
        "{}{}. Спокойно ниже {}, встревожено ниже {}, взволновано ниже {}, буйно выше.",
    "Over {} milk and wool grow at {} / stress of their rate.":
        "Выше {} молоко и шерсть растут со скоростью {} / стресс от обычной.",
    "Over {} a pregnancy can be lost.":
        "Выше {} беременность может прерваться.",
    "Milking with stress over {} and Animal Care {} or less always fails and spills the bucket.":
        "Доение при стрессе выше {} и Уходе за животными {} или ниже всегда срывается и опрокидывает ведро.",
    "Litres in the udder and what it holds.":
        "Литры в вымени и его вместимость.",
    "It fills by capacity / {} per game hour, times the sandbox milk modifier.":
        "Наполняется на вместимость / {} за игровой час, умножая на модификатор молока из песочницы.",
    "Stress over {} slows it down.":
        "Стресс выше {} это замедляет.",
    "Wool grown and the maximum.":
        "Накопленная шерсть и максимум.",
    "It grows by maximum / {} per game hour: {} days for a full fleece.":
        "Растёт на максимум / {} за игровой час: {} дней до полного руна.",
    "Days left before it gives birth.":
        "Дней до родов.",
    "Stress over {} can end the pregnancy.":
        "Стресс выше {} может прервать беременность.",
    "Hours this female stays fertilised.":
        "Часов, пока эта самка остаётся оплодотворённой.",
    "When it runs out she is no longer fertilised.":
        "Когда они кончатся, она перестанет быть оплодотворённой.",

    # Wounds and healing
    "Wounds: how long each one still needs":
        "Раны: сколько ещё нужно каждой",
    "Adds an Info entry under the treatments you get by clicking a body part in the health panel. Hover it and the box beside it gives the time left on every wound, what bandaging or a poultice would save, how long the bandage lasts and whether the part is mending or getting worse. The game knows all of it and only prints it in debug mode.":
        "Добавляет пункт «Информация» под способами лечения, которые открываются щелчком по части тела в окне здоровья. При наведении рамка рядом показывает, сколько осталось каждой ране, что дало бы бинтование или припарка, насколько хватит бинта и заживает ли часть тела или ей становится хуже. Игра всё это знает и печатает только в режиме отладки.",
    "Wounds: keep vanilla's Doctor level requirements":
        "Раны: сохранить требования к уровню Медицины",
    "Off by default, so you see everything from level {}. Turn it on and each row reappears at the Doctor level vanilla itself uses for it: scratches and lacerations at {}, deep wounds and splints at {}, fractures and stitches at {}, wound infection at {}.":
        "По умолчанию выключено, так что всё видно с уровня {}. Включите — и каждая строка вернётся на тот уровень Медицины, который использует сама игра: царапины и порезы на {}, глубокие раны и шины на {}, переломы и швы на {}, заражение раны на {}.",
    "Full recovery":
        "Полное восстановление",
    "Getting worse":
        "Ухудшается",
    "Healing":
        "Заживление",
    "normal":
        "обычное",
    "slowed by hunger, thirst or illness":
        "замедлено голодом, жаждой или болезнью",
    "stopped by hunger or thirst":
        "остановлено голодом или жаждой",
    "asleep, ten times faster":
        "во сне, в десять раз быстрее",
    "wounded parts share it":
        "раненых частей делят его между собой",
    "Bandage life":
        "Срок бинта",
    "ready to remove":
        "можно снимать",

    # Wounds and healing, redesigned tooltip
    "Healing speed":
        "Скорость заживления",
    "clean for":
        "чистый ещё",
    "Poultice":
        "Припарка",
    "Wound infection":
        "Заражение раны",
    "won't close, glass inside":
        "не затянется, внутри стекло",
    "won't close while unbandaged":
        "не затянется без бинта",
    "rising":
        "растёт",

    # Wounds: shorter recovery label and infection risk
    "Recovery":
        "Восстановление",
    "Infection risk":
        "Риск заражения",

    # Percentages, ported from the multiplier wording
    "{}%% weapon damage": "{}%% урона оружия",
    "{}%% endurance recovery": "{}%% к восстановлению выносливости",
    "{}%% melee damage and knockback": "{}%% урона в ближнем бою и отбрасывания",
    "{}%% move speed in combat stance": "{}%% к скорости движения в боевой стойке",
    "{}%% sprint speed": "{}%% к скорости спринта",
    "{}%% chance of being spotted": "{}%% к шансу быть замеченным",
    "{}%% footstep noise": "{}%% к шуму шагов",
    "{}%% recoil delay": "{}%% к задержке отдачи",
    "{}%% aim settling speed": "{}%% к скорости стабилизации прицела",
    "{}%% aim penalty for moving (shared with Nimble)":
        "{}%% к штрафу прицеливания за движение (общий с Ловкостью)",
    "{}%% reload speed": "{}%% к скорости перезарядки",
    "{}%% racking speed": "{}%% к скорости передёргивания затвора",
    "{}%% XP in every Crafting skill": "{}%% опыта во всех навыках Ремесла",
    "{}%% move speed through trees": "{}%% к скорости движения среди деревьев",
    "spotting another player {}%%": "{}%% к обнаружению другого игрока",
    "timed actions {}%%": "действия дольше в {} раза",
    "endurance drain {}%%": "{}%% к расходу выносливости",
    "alcohol hits {}%%, and {}%% over {}%% hunger":
        "Алкоголь бьёт {0}%%, а при голоде выше {2}%% — {1}%%",
    "Fitness {}, which is {}%% endurance recovery instead of {}%%":
        "Физподготовка {}, то есть {}%% восстановления выносливости вместо {}%%",
    "{}%% attack speed": "{}%% к скорости атаки",
    "{}%% crit chance": "{}%% к шансу крита",
    "racking costs {}%% of the aiming time":
        "передёргивание затвора стоит {}%% от времени прицеливания",
    "carrying capacity {}": "грузоподъёмность {}",
    "{} to every weapon's durability roll.": "{} к броску износа любого оружия.",
    "Condition loss (handle)": "Потеря состояния (рукояти)",
    "Condition loss (head)": "Потеря состояния (головы)",

    # Ronda 4: medicine, traps, weapon components, skill levels
    '%1 corpses nearby': '%1 трупов поблизости',
    '%1%% attack time': '%1%% времени атаки',
    '%1%% crit chance': '%1%% шанса крит. удара',
    '%1%% muscle strain': '%1%% мышечного напряжения',
    '%1%% weapon damage': '%1%% урона оружия',
    '+%1 to the durability roll': '+%1 к броску прочности',
    'Adds an Info entry to a placed trap: the odds of it catching anything in an hour, which animals it can take and the share of the catch each one gets, the bait and its freshness, the zone, the hourly odds of losing bait or trap, and the warning that a trap catches nothing while you stand next to it. Bait foods get a row naming what they attract.': 'Добавляет пункт Инфо к установленной ловушке: с каким шансом она вообще что-нибудь поймает за час, каких животных она может поймать и какая доля улова достаётся каждому, приманку и её свежесть, зону, почасовые шансы потерять приманку или ловушку, и предупреждение, что ловушка ничего не ловит, пока вы стоите рядом. У продуктов-приманок появляется строка с тем, кого они привлекают.',
    'Bait': 'Приманка',
    'Bait lost per hour': 'Потеря приманки в час',
    'In the trap for': 'В ловушке уже',
    'Filter left': 'Остаток фильтра',
    'Hits before it breaks': 'Ударов до поломки',
    'Medicine: duration, delay and effect': 'Лекарства: длительность, задержка и эффект',
    'Medicine: the full list of effects': 'Лекарства: полный список эффектов',
    'Muscle strain per hit': 'Мышечное напряжение за удар',
    'Off by default, so you see everything from level {}. Turn it on and the trap tooltip only appears from Trapping {}, which is the level vanilla itself uses elsewhere.': 'По умолчанию выключено, поэтому вы видите всё с уровня {}. При включении подсказка ловушки появляется только с уровня Ловушки {}, который игра сама использует в других местах.',
    'Off by default. Adds everything else each pill does: what cancels it, what intoxication costs it, and the sleeping tablet overdose table.': 'По умолчанию выключено. Добавляет всё остальное, что делает каждая таблетка: что её отменяет, чего стоит опьянение и таблицу передозировки снотворного.',
    'Painkillers, beta blockers, antidepressants, sleeping tablets and antibiotics get how long they last, how long they take to start and what they do per minute. Every figure is recomputed from the sandbox day length.': 'Обезболивающие, бета-блокаторы, антидепрессанты, снотворное и антибиотики показывают, сколько они действуют, сколько занимает начало действия и что они делают за минуту. Каждое значение пересчитывается по длине дня в песочнице.',
    'Prey': 'Добыча',
    'Rots once thawed': 'Портится после разморозки',
    'Stale once thawed': 'Черствеет после разморозки',
    'Takes effect in': 'Начинает действовать через',
    'Trap lost per hour': 'Потеря ловушки в час',
    'Traps: catch odds, bait and hours': 'Ловушки: шансы поимки, приманка и часы',
    "Traps: keep vanilla's Trapping level requirements": 'Ловушки: сохранить требования игры к уровню Ловушек',
    'Zone': 'Зона',
    'a second dose resets the clock, it does not add': 'вторая доза сбрасывает таймер, а не складывается',
    'a third of the strength above {} intoxication': 'треть силы при опьянении выше {}',
    'fresh for %1': 'свежая ещё %1',
    'half the strength above {} intoxication': 'половина силы при опьянении выше {}',
    'each pill counts double above {} intoxication': 'каждая таблетка считается за две при опьянении выше {}',
    'holds the fever, does not cure it': 'сдерживает лихорадку, но не лечит её',
    'incoming panic {}%% per pill, down to nothing': 'входящая паника {}%% за таблетку, вплоть до нуля',
    'it catches nothing while you are near it': 'она ничего не ловит, пока вы рядом',
    'only the first dose has to wait': 'ждать нужно только первой дозе',
    'overdose: {} pills cost {} health, {} cost {}, {} kill': 'передозировка: {} таблеток отнимают {} здоровья, {} отнимают {}, {} убивают',
    'sleeping cancels the effect': 'сон отменяет эффект',
    'stale, catches nothing': 'несвежая, никого не привлекает',
    'the longer it waits, the likelier it comes out dead': 'чем дольше ждёт, тем вероятнее выйдет мёртвым',
    'to full in %1': 'до максимума за %1',
    'to zero in %1': 'до нуля за %1',
    'wound pain stops being recalculated while it lasts': 'боль от ран перестаёт пересчитываться, пока действует',
    'zombie fever held': 'зомби-лихорадка сдержана',
    '{}%% reading time': '{}%% времени чтения',
    'Effect': 'Эффект',

    # Ronda 4, segunda pasada
    '%1 s': '%1 с',
    '%1 s per round': '%1 с на патрон',
    '%1%% attack speed': '%1%% скорости атаки',
    'Details': 'Подробности',
    'Info': 'Инфо',
    'Possible prey': 'Возможная добыча',
    'Trap breaks per hour': 'Поломка ловушки в час',
    'holds the fever': 'сдерживает лихорадку',
    'not being used (%1 corpses nearby)': 'не расходуется (%1 трупов поблизости)',
    'Bird': 'Птица',
    'Active hours': 'Часы активности',
    'Possible prey, share of the catch': 'Возможная добыча, доля улова',
    'Catch chance': 'Шанс поимки',
    'Bait condition': 'Состояние приманки',
    'Trap condition': 'Состояние ловушки',
    'while you are near it, it neither catches nor breaks': 'пока вы рядом, она ничего не ловит и не ломается',
    'Bait loss risk, per hour': 'Риск потерять приманку, в час',
    'Wrecked by an animal, per hour': 'Разрушена зверем, в час',
    '%1 / h': '%1 / ч',
    'Bait loss risk': 'Риск потерять приманку',
    'Chance of being wrecked': 'Шанс быть разрушенной',
    'Critical damage': 'Критический урон',
    'Effective durability': 'Эффективная прочность',
    'Damage with your character': 'Урон с вашим персонажем',
    'Reach (tiles)': 'Дальность (клетки)',

    # Bags and the torch beam (0.9.20)
    'All round': 'Во все стороны',
    'Beam (degrees)': 'Луч (градусы)',
    'Bags: how much they slow you down': 'Сумки: насколько они вас замедляют',
    "The run and combat speed a bag costs you, which the game applies and never shows. The run figure is the one you are paying right now: a bag's penalty grows by half again as it fills up, so the same pack goes from {}%% empty to {}%% full. It counts the same in your hands as on your back.": 'Скорость бега и боя, которой обходится сумка: игра её применяет и никогда не показывает. Значение бега это то, которое вы платите прямо сейчас: штраф растёт в полтора раза по мере наполнения, поэтому одна и та же сумка идёт от {}%% пустой до {}%% полной. В руках она считается так же, как за спиной.',

    # Trait figures corrected against bytecode (0.9.21)
    "Aiming and Maintenance are not affected":
        "Меткость и Обслуживание не затрагиваются",
    "ambient light never drops below {} in the dark":
        "фоновое освещение в темноте не опускается ниже {}",
    "can tell a poisonous wild plant from a safe one":
        "отличает ядовитое дикорастущее растение от безопасного",
    "lights a fire with a notched plank twice as fast":
        "разжигает огонь дощечкой с зарубкой вдвое быстрее",
    "no harm at all from tainted water":
        "грязная вода не наносит никакого вреда",
    "{} health on every construction":
        "{} к прочности каждой постройки",
    "{} tiles of perception instead of {}":
        "{} клетки восприятия вместо {}",
    "{}%% XP in the six melee weapon skills":
        "{}%% опыта в шести навыках ближнего боя",
    "{}%% chance of tearing your clothes on a tree":
        "{}%% к шансу порвать одежду о дерево",
    "{}%% from any other poison":
        "{}%% от любого другого яда",
    "{}%% from any other poison, bleach aside":
        "{}%% от любого другого яда, кроме отбеливателя",
    "{}%% weather penalty in combat":
        "{}%% к штрафу за погоду в бою",

    # Per-level lines for the twenty craft skills (0.9.21)
    "%1 crop health at planting":
        "%1 к здоровью растения при посадке",
    "%1%% chance the crop is cursed if planted out of its month":
        "%1%% что растение будет проклятым, если посадить его не в свой месяц",
    "%1%% chance of a bonus harvest planted in its best month":
        "%1%% на дополнительный урожай при посадке в лучший месяц",
    "%1 disease removed per treatment":
        "%1 болезни снимается за обработку",
    "%1%% chance of harvesting %2 extra vegetables":
        "%1%% собрать на %2 овощей больше",
    "%1%% back strain planting and harvesting":
        "%1%% нагрузки на спину при посадке и сборе урожая",
    "%1 points off the chance a stressed animal breaks off milking or shearing":
        "%1 к шансу, что стрессующее животное вырвется при дойке или стрижке",
    "a stressed animal never breaks off milking or shearing":
        "стрессующее животное больше не вырывается при дойке и стрижке",
    "x%1 chance of each extra part off a carcass":
        "x%1 к шансу каждой дополнительной части туши",
    "x%1 of each part":
        "x%1 от каждой части",
    "up to %1 blood splatters on you":
        "до %1 брызг крови на вас",
    "%1 health on everything you build":
        "%1 к прочности всего, что вы строите",
    "%1%% build time":
        "%1%% времени на строительство",
    "%1%% barricading time":
        "%1%% времени на баррикадирование",
    "%1%% chance of recovering material when dismantling":
        "%1%% вернуть материалы при разборке",
    "%1%% of the ingredient used per addition":
        "%1%% ингредиента расходуется за добавление",
    "x%1 nutrients from each ingredient":
        "x%1 питательности от каждого ингредиента",
    "rotten food can go in evolved recipes, worth %1%% of its hunger":
        "можно класть немного испорченной еды в развивающиеся рецепты",
    "x%1 fracture healing with a splint":
        "x%1 к скорости заживления перелома с шиной",
    "a bandage lasts %1 to %2 longer":
        "бинт держится от %1 до %2 дольше",
    "%1%% time for every medical action":
        "%1%% времени на любое медицинское действие",
    "you can judge how bad a wound is":
        "вы можете оценить тяжесть раны",
    "you can read pain, and spot the burns that need washing":
        "вы читаете боль и видите, какие ожоги надо промыть",
    "you can tell when stitches are ready to come out":
        "вы понимаете, когда швы можно снимать",
    "you spot a wound infection straight away":
        "вы сразу замечаете заражение раны",
    "%1%% chance of getting the patch back":
        "%1%% вернуть заплату обратно",
    "%1%% time to add or remove a patch":
        "%1%% времени на установку или снятие заплаты",
    "a hole can be repaired completely, defense and insulation included":
        "дыру можно залатать полностью, вместе с защитой и утеплением",
    "+%1%% generator condition per repair":
        "+%1%% состояния генератора за ремонт",
    "%1 points to the chance of hotwiring a car":
        "%1 к шансу завести машину без ключа",
    "%1%% chance of setting off the car alarm":
        "%1%% что сработает автосигнализация",
    "you can salvage and repair a standard engine":
        "можно разобрать и починить обычный двигатель",
    "you can salvage and repair a heavy-duty engine":
        "можно разобрать и починить тяжёлый двигатель",
    "you can salvage and repair a sport engine":
        "можно разобрать и починить спортивный двигатель",
    "you can build the sturdier brick wall":
        "можно строить более прочную кирпичную стену",
    "small %1%%, medium %2%%, large %3%%":
        "мелкая %1%%, средняя %2%%, крупная %3%%",
    "%1 points to the chance a berry or mushroom is poisonous":
        "%1 к шансу, что ягода или гриб окажутся ядовитыми",
    "%1%% time to inspect a track":
        "%1%% времени на осмотр следа",
    "no effect of its own, this level only unlocks the recipes below":
        "своего эффекта нет, этот уровень лишь открывает рецепты ниже",

    # 0.9.21 follow-up
    "%1 rags when you rip up clothing, capped by the parts it covers":
        "%1 лоскута при разрывании одежды, не больше числа закрытых частей тела",
    "rotten food can go in evolved recipes, worth %1%% of its hunger":
        "испорченную еду можно класть в развивающиеся рецепты, она даёт %1%% своей сытости",

    # 0.9.21 follow-up 2
    "%1%% time per litre shearing an animal":
        "%1%% времени на литр при стрижке животного",
    "%1 rags when you rip up clothing, capped by the parts it covers":
        "%1 лоскута при разрывании одежды, не больше числа закрытых частей тела",
    "%1 to the most aramid thread you can pull out":
        "%1 к максимуму арамидной нити, которую можно вытянуть",
    "starts at {} weight, becomes Emaciated at {} or less and Low Weight above {}":
        "начинается с веса {}, при {} и ниже переходит в «Крайне недостаточный вес», выше {} — в «Недостаточный вес»",
    "starts at {} weight, becomes High Weight below {}":
        "начинается с веса {}, ниже {} переходит в «Избыточный вес»",
    "starts at {} weight, becomes Very High Weight at {} and is lost below {}":
        "начинается с веса {}, на {} переходит в «Очень избыточный вес», ниже {} теряется",
    "starts at {} weight, becomes Very Low Weight at {} or less and is lost above {}":
        "начинается с веса {}, при {} и ниже переходит в «Очень низкий вес», выше {} теряется",
    "XP awarded":
        "Начисляемый опыт",
    "{} chance to trip when a zombie lunges through a window":
        "{} к шансу споткнуться, когда зомби бросается через окно",
    "{} to the roll that keeps you on your feet when a zombie shoves you":
        "{} к броску, который удерживает вас на ногах при толчке зомби",
    "{}%% muscle strain":
        "{}%% мышечного напряжения",
    "{}%% axe attack speed, chopping trees included":
        "{}%% скорости атаки топором, рубка деревьев в том числе",

    # B42.20 trait corrections
    "Another x{} at panic level {}":
        "ещё x{} при панике уровня {}",
    "Can hotwire without Electrical {} and Mechanics {}":
        "можно завести без ключа без Электрики {} и Механики {}",
    "Engine revs three times faster in reverse":
        "обороты растут втрое быстрее задним ходом",
    "Halves your rope climbing bonus":
        "бонус к подъёму по верёвке уменьшается вдвое",
    "No unhappiness from looting corpses":
        "обыск трупов не даёт уныния",
    "Stress from handling bloody items":
        "стресс от обращения с окровавленными вещами",
    "{} move speed at panic level {}, {} at level {}":
        "{} к скорости при панике уровня {}, {} на уровне {}",
    "{} to the rope climbing roll":
        "{} к броску на подъём по верёвке",
    "{}%% acceleration, fading out above {}%% of the car's top speed":
        "{}%% к разгону, и он угасает выше {}%% максимальной скорости машины",
    "{}%% carry capacity":
        "{}%% к грузоподъёмности",
    "{}%% chance of breaking a window lock instead of {}%%":
        "{}%% сломать шпингалет окна вместо {}%%",
    "{}%% endurance cost on every exertion":
        "{}%% выносливости на каждое усилие",
    "{}%% reverse acceleration, gone past {} km/h":
        "{}%% к разгону задним ходом, и его нет после {} км/ч",
    "{}%% unhappiness from looting corpses":
        "{}%% уныния от обыска трупов",

    # Repair recipes
    "Repair: +%1 condition, %2 chance of failing":
        "Ремонт: +%1 к состоянию, %2 провалить",
    "Repair: +%1 condition, %2 chance of failing, repaired %3 times":
        "Ремонт: +%1 к состоянию, %2 провалить, ремонтов уже %3",

    # Corpse count and temperature figures
    "Body temperature: the number on every bar":
        "Температура тела: число в каждой полосе",
    "Nauseous: how many corpses are making you ill":
        "Тошнота: сколько трупов вас отравляет",
    "Rotting corpses nearby raise food sickness, and the game never says how many are close enough. Five or fewer do nothing. The count is read back out of the game, so it follows the sandbox setting.":
        "Гниющие трупы рядом повышают пищевое отравление, и игра нигде не говорит, сколько их достаточно близко. Пять и меньше не делают ничего. Счёт считывается из самой игры, так что он следует настройке песочницы.",
    "The temperature view prints its value on Insulation and Wind resistance and leaves the other nine bars as a colour. This sets the same flag on the rest, so skin temperature, body response, heat and wetness read as figures. Vanilla does the drawing, and only for the body part you have selected.":
        "Вид температуры пишет значение на «Изоляции» и «Защите от ветра», а остальные девять полос оставляет цветом. Здесь тот же флаг ставится на остальные, так что температура кожи, отклик тела, тепло и влажность читаются числами. Рисует их сама игра, и только для выбранной части тела.",

    # Options tab
    "Custom":
        "Свой",
    "Nothing matches that":
        "Ничего не найдено",
    "Moodles: how many corpses are making you ill":
        "Моудлы: сколько трупов вас отравляет",

    # Option groups
    "Every gun this box or magazine fits, one per row.":
        "Каждое оружие, к которому подходит эта коробка или магазин, по одному в строке.",
    "How bloody the garment is, out of a hundred.":
        "Насколько одежда в крови, из ста.",
    "How brightly it lights what it reaches.":
        "Насколько ярко освещает то, до чего достаёт.",
    "How dirty the garment is, out of a hundred.":
        "Насколько одежда грязная, из ста.",
    "How drunk this container will get you.":
        "Насколько пьяным вас сделает эта ёмкость.",
    "How far the light reaches, in tiles.":
        "Насколько далеко достаёт свет, в клетках.",
    "How far the shot is heard, which is how far the horde comes from.":
        "Насколько далеко слышен выстрел, то есть откуда придёт орда.",
    "How long before the pill starts working, and only while you have none running.":
        "Через сколько таблетка начнёт действовать, и только пока ни одна не действует.",
    "How long cooked food can stay on the heat before it burns.":
        "Сколько готовая еда продержится на огне, прежде чем сгорит.",
    "How long the charge lasts with the thing switched on.":
        "На сколько хватает заряда при включённом устройстве.",
    "How long the filter lasts at your current exposure, and how many corpses are around you.":
        "На сколько хватит фильтра при текущем воздействии и сколько трупов вокруг вас.",
    "How long the item burns for as fuel.":
        "Сколько предмет горит в качестве топлива.",
    "How long the pages you have not read yet will take.":
        "Сколько времени займут ещё не прочитанные страницы.",
    "How long the pill keeps working.":
        "Сколько таблетка продолжает действовать.",
    "How long the plant takes to be ready, at the current farming speed.":
        "Сколько растение растёт до готовности, при текущей скорости земледелия.",
    "How long until the food goes stale, at the current rot speed.":
        "Через сколько еда станет несвежей, при текущей скорости порчи.",
    "How long until the food is rotten, at the current rot speed.":
        "Через сколько еда испортится, при текущей скорости порчи.",
    "How many hits the weapon has left in it, which is the one figure that compares any two weapons.":
        "Сколько ударов в оружии ещё осталось: единственная величина, сравнивающая любые два оружия.",
    "How much cold the garment keeps out. The game only draws a bar.":
        "Сколько холода не пропускает одежда. Игра рисует только полоску.",
    "How much is left in the filter.":
        "Сколько осталось в фильтре.",
    "How much of it you have already heard.":
        "Сколько из этого вы уже прослушали.",
    "How much of the corpse sickness the mask keeps off you. {}%% is immunity.":
        "Сколько трупной болезни маска с вас снимает. {}%% это полный иммунитет.",
    "How much of your hunger bar the drink covers.":
        "Какую часть шкалы голода закрывает напиток.",
    "How much of your thirst bar the drink covers.":
        "Какую часть шкалы жажды закрывает напиток.",
    "How much pull the rod takes before the line gives.":
        "Какое натяжение выдержит удочка, прежде чем леска сдаст.",
    "How much rain the garment keeps out. The game only draws a bar.":
        "Сколько дождя не пропускает одежда. Игра рисует только полоску.",
    "How much the bag slows you down, with its weight and what is inside counted.":
        "Насколько сумка вас замедляет, с учётом её веса и содержимого.",
    "How much the bag slows your swing.":
        "Насколько сумка замедляет ваш удар.",
    "How much the garment slows you down, as the penalty itself rather than a bar.":
        "Насколько одежда вас замедляет, самим штрафом, а не полоской.",
    "How much the garment slows your swing, as the penalty itself rather than a bar.":
        "Насколько одежда замедляет ваш удар, самим штрафом, а не полоской.",
    "How much tiredness this surface actually clears, your traits included.":
        "Сколько усталости эта поверхность на самом деле снимает, с учётом ваших черт.",
    "How much wind the garment keeps out. The game only draws a bar.":
        "Сколько ветра не пропускает одежда. Игра рисует только полоску.",
    "How often a hit crits, with your level in the weapon's own skill counted.":
        "Как часто удар критический, с учётом вашего уровня в навыке этого оружия.",
    "How often a shot crits.":
        "Как часто выстрел критический.",
    "How wet the garment is, out of a hundred.":
        "Насколько одежда мокрая, из ста.",
    "In tiles. A swing landed at the edge of your reach does up to twice the damage of one landed close in.":
        "В клетках. Удар на краю досягаемости наносит до двух раз больше урона, чем удар вплотную.",
    "Off by default: the game only reveals this block for packaged food or a Nutritionist.":
        "Выключено по умолчанию: игра показывает этот блок только для упакованной еды или Диетолога.",
    "Rounds in the magazine right now, out of what it holds.":
        "Патронов в магазине сейчас, из того, сколько в него влезает.",
    "The calibre the magazine takes.":
        "Калибр, который принимает магазин.",
    "The calories in what is actually in the container, mixtures included.":
        "Калории того, что реально налито в ёмкость, включая смеси.",
    "The carbohydrates in what is actually in the container.":
        "Углеводы того, что реально налито в ёмкость.",
    "The charge left, as a number instead of a bar.":
        "Оставшийся заряд, числом, а не полоской.",
    "The edge, and the ceiling a worn head puts on it: blunt, the weapon loses the top of its damage range.":
        "Заточка и потолок, который ставит изношенная головка: без заточки оружие теряет верх своего урона.",
    "The exact minimum and maximum. The game only ever draws it as a bar.":
        "Точные минимум и максимум. Игра рисует это только полоской.",
    "The exact points left, and the head's own count on a weapon that has one.":
        "Точные оставшиеся очки, и отдельный счёт головки у оружия, где она есть.",
    "The exact points left, where the game only draws a bar.":
        "Точные оставшиеся очки там, где игра рисует только полоску.",
    "The fat in what is actually in the container.":
        "Жиры того, что реально налито в ёмкость.",
    "The fatigue each swing costs you.":
        "Усталость, которую стоит каждый удар.",
    "The furthest tile the gun can hit.":
        "Самая дальняя клетка, куда достаёт выстрел.",
    "The gun's own hit chance, before your aiming skill.":
        "Собственный шанс попадания оружия, до вашего навыка стрельбы.",
    "The hook fitted, and what it does to your odds of a bite.":
        "Установленный крючок и что он делает с вашими шансами на поклёвку.",
    "The line fitted, and how much of it each tug wears away.":
        "Установленная леска и сколько её стирает каждый рывок.",
    "The months it can be sown in, one per row.":
        "Месяцы, в которые можно сеять, по одному в строке.",
    "The multiplier your shoes put on stomping a downed zombie. Footwear only.":
        "Множитель, который ваша обувь даёт добиванию лежачего зомби. Только обувь.",
    "The multiplier your skill puts on this weapon's swing.":
        "Множитель, который ваш навык даёт удару этого оружия.",
    "The net pace of the pill, which is what compares two of them at a glance.":
        "Чистый темп таблетки: то, что сравнивает две из них с одного взгляда.",
    "The odds of losing a point of condition on a hit, with Maintenance and the weapon's skill counted.":
        "Шанс потерять очко состояния при ударе, с учётом Ремонта и навыка этого оружия.",
    "The odds of losing a point of condition per shot.":
        "Шанс потерять очко состояния за выстрел.",
    "The poison the drink carries, and only while the game is willing to tell you.":
        "Настоящий шанс осечки, включая износ и слабый хват.",
    "The proteins in what is actually in the container.":
        "Белки того, что реально налито в ёмкость.",
    "The real odds of a jam, wear and a weak grip included.":
        "Яд, который несёт напиток, и только пока игра готова вам об этом сказать.",
    "The real seconds a reload takes, with your reloading skill and your panic counted.":
        "Реальные секунды перезарядки, с учётом вашего навыка перезарядки и паники.",
    "The real seconds spent lining up the shot, with your aiming skill and your traits counted.":
        "Реальные секунды на прицеливание, с учётом вашего навыка стрельбы и ваших черт.",
    "The recipes it teaches that you do not know yet, one per row.":
        "Рецепты, которым это учит и которых вы ещё не знаете, по одному в строке.",
    "The swing animation, which is what really separates a slow weapon from a fast one.":
        "Анимация замаха: именно она отличает медленное оружие от быстрого.",
    "What a critical is worth, from {}%% to {}%% depending on the weapon. The game shows it nowhere.":
        "Сколько стоит критический удар, от {}%% до {}%% в зависимости от оружия. Игра не показывает это нигде.",
    "What feeds the Uncomfortable moodle. The game never shows it on the garment at all.":
        "То, что питает моудл дискомфорта. Игра вообще не показывает это на одежде.",
    "What is left in your hands when the rod breaks.":
        "Что останется у вас в руках, когда удочка сломается.",
    "What sleeping here costs you in comfort.":
        "Во что вам обходится сон здесь по комфорту.",
    "What the drink does to boredom and unhappiness, which move together here.":
        "Что напиток делает со скукой и несчастьем, которые здесь идут вместе.",
    "What the drink does to your fatigue bar.":
        "Что напиток делает с вашей шкалой усталости.",
    "What the drink does to your stress.":
        "Что напиток делает с вашим стрессом.",
    "What the food still needs, and the temperature the figure assumes.":
        "Сколько еде ещё нужно и при какой температуре считается цифра.",
    "Whether it is a cone you aim or a lamp that lights all around, and how wide the cone is.":
        "Конус, который вы наводите, или лампа, светящая вокруг, и насколько широк конус.",
    "Which fish this bait brings in.":
        "Какую рыбу приманивает эта наживка.",
    "Which skill the tape or disc trains and how much experience is left in it.":
        "Какому навыку учит кассета или диск и сколько опыта в ней осталось.",
    "Which skill the weapon trains, and therefore which one drives its damage and its speed.":
        "Какой навык тренирует оружие, а значит и какой двигает его урон и скорость.",
    "Your own reading speed, traits, glasses and sitting down included.":
        "Ваша собственная скорость чтения, включая черты, очки и то, что вы сидите.",
    "Nutrition":
        "Питание",
    "Sleep":
        "Сон",
    "How much the bag slows your attack. It multiplies the weapon's own swing speed, not your walking.":
        "Насколько сумка замедляет вашу атаку. Она умножает скорость замаха самого оружия, а не вашу ходьбу.",
    "How much the garment slows your attack. It multiplies the weapon's own swing speed, not your walking.":
        "Насколько одежда замедляет вашу атаку. Она умножает скорость замаха самого оружия, а не вашу ходьбу.",
    "Best baits":
        "Лучшие наживки",
    "Every animal this trap can catch and its share of the catch.":
        "Каждое животное, которое может попасть в эту ловушку, и его доля в добыче.",
    "Feathers":
        "Перья",
    "Fog on a line of its own, because the game lumps it into weather and then reports neither.":
        "Туман отдельной строкой, потому что игра сваливает его в погоду и потом не сообщает ни о том, ни о другом.",
    "Glass or a bullet still in the wound, which stops it healing until it is out.":
        "Стекло или пуля, всё ещё сидящие в ране: пока их не вынуть, она не заживает.",
    "How far the disease has gone, out of a hundred.":
        "Насколько далеко зашла болезнь, из ста.",
    "How far the generator is heard, halved when it stands indoors.":
        "Насколько далеко слышно генератор; под крышей вдвое меньше.",
    "How full the udder is and whether it can be milked yet.":
        "Насколько полно вымя и можно ли уже доить.",
    "How hungry the animal is, and how long its feed will last.":
        "Насколько животное голодно и на сколько хватит его корма.",
    "How long before old age starts costing the animal its yield.":
        "Через сколько старость начнёт отнимать у животного продуктивность.",
    "How long each cut, scratch, burn or bite still needs.":
        "Сколько ещё нужно каждому порезу, царапине, ожогу или укусу.",
    "How long is left of a pregnancy, or of an egg being fertilised.":
        "Сколько осталось до конца беременности или до оплодотворения яйца.",
    "How long since the last watering. The game works it out to pick a colour and then never shows it.":
        "Сколько прошло с последнего полива. Игра считает это, чтобы выбрать цвет, и никогда не показывает.",
    "How long the bandage lasts before it is dirty and worth changing.":
        "На сколько хватает бинта, прежде чем он загрязнится и его стоит сменить.",
    "How long the catch has been waiting in there.":
        "Сколько добыча уже там сидит.",
    "How long the fracture needs, and what the splint on it is worth.":
        "Сколько нужно перелому и чего стоит наложенная шина.",
    "How long the fuel in the tank lasts at the current draw.":
        "На сколько хватает топлива в баке при текущем расходе.",
    "How long the part needs to be whole again, and how fast it is healing.":
        "Сколько нужно части тела, чтобы снова стать целой, и с какой скоростью она заживает.",
    "How long the stiffness in that limb takes to pass.":
        "Сколько времени проходит скованность в этой конечности.",
    "How long the stitches need, and when they can come out.":
        "Сколько нужно швам и когда их можно снять.",
    "How long until it breaks down for good, on average.":
        "Через сколько он окончательно сломается, в среднем.",
    "How long until it wears down to the point where it can catch fire.":
        "Через сколько он износится до состояния, в котором может загореться.",
    "How long until the crop moves to its next stage.":
        "Через сколько посадка перейдёт в следующую стадию.",
    "How long you will wait compared with the best possible spot.":
        "Сколько вы будете ждать по сравнению с лучшим возможным местом.",
    "How many feathers butchering will give.":
        "Сколько перьев даст разделка.",
    "How many fish this spot still holds, and what that is worth.":
        "Сколько рыбы ещё осталось в этом месте и чего это стоит.",
    "How much blood butchering will give.":
        "Сколько крови даст разделка.",
    "How much fertiliser the plot holds. Above one is the too much case in the game's own code.":
        "Сколько удобрения на грядке. Больше единицы, по коду самой игры, это уже перебор.",
    "How much meat butchering will give, which is what answers whether it is worth killing yet.":
        "Сколько мяса даст разделка: именно это отвечает на вопрос, стоит ли уже забивать.",
    "How much of the bait is still good.":
        "Сколько наживки ещё годится.",
    "How much the animal trusts you, which is what lets you handle it.":
        "Насколько животное вам доверяет: именно это позволяет с ним обращаться.",
    "How much wool has grown back and whether it can be sheared yet.":
        "Сколько шерсти отросло и можно ли уже стричь.",
    "How stressed the animal is, out of a hundred.":
        "Насколько животное в стрессе, из ста.",
    "How the wound infection is going, and whether it is still rising.":
        "Как идёт заражение раны и растёт ли оно ещё.",
    "How thirsty the animal is, and how long its water will last.":
        "Насколько животное хочет пить и на сколько хватит его воды.",
    "Level needed":
        "Нужный уровень",
    "Lodged objects":
        "Застрявшие предметы",
    "Odds with your bait":
        "Шанс с вашей наживкой",
    "Predator":
        "Хищник",
    "Size and weight":
        "Размер и вес",
    "Strength at the top skill level":
        "Прочность на максимальном уровне",
    "The Fishing level this species needs before it will bite.":
        "Уровень Рыбалки, который нужен этому виду, чтобы клюнуть.",
    "The animal's health as a number.":
        "Здоровье животного числом.",
    "The animal's weight, and how far it still has to grow.":
        "Вес животного и сколько ему ещё расти.",
    "The chance of this exact species with the bait you are using.":
        "Шанс именно этого вида с той наживкой, которой вы ловите.",
    "The crop's health out of a hundred. The game only prints it with debug on.":
        "Здоровье посадки из ста. Игра пишет его только с включённой отладкой.",
    "The fuel still in the tank. The game knows the number and only prints it as a debug option.":
        "Топливо, оставшееся в баке. Игра знает это число и выводит его только как отладочную опцию.",
    "The health the wall or door will have when you build it at your current level.":
        "Прочность стены или двери, если построить её на вашем текущем уровне.",
    "The hourly odds of a bang loud enough to pull zombies in.":
        "Почасовой шанс хлопка, достаточно громкого, чтобы притянуть зомби.",
    "The hourly odds of a fire or an explosion, which set the generator to zero outright.":
        "Почасовой шанс пожара или взрыва, которые сразу обнуляют генератор.",
    "The hourly odds of the bait being taken without a catch.":
        "Почасовой шанс того, что наживку унесут без улова.",
    "The hourly odds of the trap being wrecked.":
        "Почасовой шанс того, что ловушку разломают.",
    "The hourly odds of the wound becoming infected.":
        "Почасовой шанс того, что рана заразится.",
    "The hours of the day the trap actually works.":
        "Часы суток, в которые ловушка действительно работает.",
    "The kind of ground the trap is standing on, which decides what can come.":
        "Тип земли, на которой стоит ловушка: он решает, кто может прийти.",
    "The odds of a bite once every factor is put together.":
        "Шанс поклёвки, когда все факторы уже сложены вместе.",
    "The odds of catching anything at all in an hour.":
        "Шанс поймать хоть что-нибудь за час.",
    "The range of lengths and weights this species comes in.":
        "Диапазон длин и весов, в котором встречается этот вид.",
    "The share of your catches that will be junk here.":
        "Какая доля вашего улова здесь будет мусором.",
    "The two things the game never says: a long wait kills the catch, and standing nearby stops the trap.":
        "Две вещи, о которых игра молчит: долгое ожидание убивает добычу, а ваше присутствие рядом останавливает ловушку.",
    "The water level as a number, and the amount this seed actually needs.":
        "Уровень воды числом и то, сколько на самом деле нужно этим семенам.",
    "Time to the danger threshold":
        "Время до порога опасности",
    "Trophy size":
        "Трофейный размер",
    "Warnings":
        "Предупреждения",
    "Warns that the species only bites while you reel in.":
        "Предупреждает, что вид клюёт только во время подмотки.",
    "What a catch has to beat to count as a trophy.":
        "Что улову нужно превысить, чтобы считаться трофеем.",
    "What the herbs in the bandage are adding.":
        "Что добавляют травы в повязке.",
    "What the same build would have at level {}, which is the reason to know the figure before building.":
        "Что та же постройка имела бы на уровне {}: ради этого и стоит знать цифру до начала стройки.",
    "What the time of day is worth, as the multiplier behind the game's own rating.":
        "Чего стоит время суток, как множитель за оценкой самой игры.",
    "What the water temperature is worth, with the actual reading in degrees.":
        "Чего стоит температура воды, с реальным показанием в градусах.",
    "What the weather is worth, as the multiplier behind the game's own rating.":
        "Чего стоит погода, как множитель за оценкой самой игры.",
    "What the wind is worth. Past half strength it costs the same penalty fog does, and the two never stack.":
        "Чего стоит ветер. За половиной силы он стоит того же штрафа, что и туман, и они никогда не складываются.",
    "Whether the mains or a generator is keeping the pump running.":
        "Что питает насос: сеть или генератор.",
    "Which animals a bait item brings in.":
        "Каких животных приманивает предмет, используемый как наживка.",
    "Which bait is in the trap, and whether it is still fresh.":
        "Какая наживка лежит в ловушке и свежая ли она ещё.",
    "Which baits work best on this species.":
        "Какие наживки лучше всего работают на этом виде.",
    "Which growth stage the crop is on, out of the total.":
        "На какой стадии роста находится посадка, из общего числа.",
    "Which hook is fitted and what it does to your odds.":
        "Какой крючок стоит и что он делает с вашими шансами.",
    "Raw eggs never make you ill":
        "Сырые яйца никогда не вызывают недомогания",
    "{}%% wait before another anti-nausea food works":
        "{}%% ожидания, прежде чем подействует следующая еда от тошноты",
    "{}%% weapon sight range":
        "{}%% дальности прицелов",
    "At Axe {} you swing as fast as a maxed axe user":
        "С Топором на {} вы бьёте так же быстро, как мастер топора",
    "{}%% from any poisonous food or drink":
        "{}%% от любой ядовитой еды или питья",
    "{}%% chance of illness from rotten food":
        "{}%% вероятности заболеть от испорченной еды",
    "Melee weapons":
        "Ближний бой",
    "Firearms":
        "Огнестрельное",
    "Drinks":
        "Напитки",
    "Skill XP":
        "Опыт навыков",
    "Weapons":
        "Оружие",
    "Worn and carried":
        "Одежда и сумки",
    "Medicine and reading":
        "Лекарства и чтение",
    "Supplies":
        "Припасы",
    "Comparison":
        "Сравнение",
    "Power and fuel":
        "Электричество и топливо",
    "Animals and traps":
        "Животные и ловушки",
    "Traits and jobs":
        "Черты и профессии",
    "Moodles":
        "Моудлы",
}
