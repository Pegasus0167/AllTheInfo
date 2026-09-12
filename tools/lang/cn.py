"""Chinese (Simplified) phrase table for AllInfo.

Keys are the English fragment with every number replaced by {} in order.
Numbers are never written here: they ride through untouched. Use {0} {1} ...
instead of {} when the language needs a different order -- and then index every
slot, Python refuses to mix the two forms.

Run `python tools\i18n.py` after editing: it checks the arity of every line and
refuses to write a language file it cannot fill completely.
"""

T = {
    'x{} weapon damage (x{} untrained)':
        'x{} 武器伤害（未训练 x{}）',
    '{} to the durability roll':
        '{} 耐久判定',
    '{} chance to trip vaulting a fence':
        '{} 翻越围栏的绊倒几率',
    '{}%% fall damage':
        '{}%% 坠落伤害',
    'x{} endurance recovery (x{} untrained)':
        'x{} 耐力恢复（未训练 x{}）',
    'x{} melee damage and knockback (x{} untrained)':
        'x{} 近战伤害与击退（未训练 x{}）',
    'x{} carrying capacity (x{} untrained)':
        'x{} 负重上限（未训练 x{}）',
    'x{} move speed in combat stance (x{} untrained)':
        'x{} 战斗姿态移动速度（未训练 x{}）',
    'x{} sprint speed (x{} untrained)':
        'x{} 冲刺速度（未训练 x{}）',
    'x{} chance of being spotted (x{} untrained)':
        'x{} 被发现的几率（未训练 x{}）',
    'x{} footstep noise (x{} untrained)':
        'x{} 脚步声（未训练 x{}）',
    "{} accuracy (the weapon's aiming modifier, {} on nearly every gun)":
        '{} 精准度（武器的瞄准修正，几乎所有枪都是 {}）',
    '{} wind penalty when aiming (of {})':
        '瞄准时的风力惩罚 {}（满值 {}）',
    'x{} reload speed (x{} untrained)':
        'x{} 装填速度（未训练 x{}）',
    'x{} racking speed (x{} untrained)':
        'x{} 上膛速度（未训练 x{}）',
    'racking costs {} of the aiming time ({} untrained)':
        '上膛消耗 {} 的瞄准时间（未训练 {}）',
    'From here on you no longer count as unsteady with a firearm, as long as your Strength is {} or more: jam chance drops by {} percentage points.':
        '从此以后，只要力量达到 {} 或更高，你不再被视为持枪不稳：卡壳几率下降 {} 个百分点。',
    'You never count as unsteady with a firearm again, whatever your Strength.':
        '无论力量多少，你都不再被视为持枪不稳。',
    '{} melee to-hit':
        '{} 近战命中',
    '{} climb chance':
        '{} 攀爬成功率',
    '{} trip chance':
        '{} 绊倒几率',
    "{} to break a zombie's grab":
        '{} 挣脱丧尸抓取',
    '{}%% strength':
        '{}%% 力量',
    '{}%% healing':
        '{}%% 治疗速度',
    'losing health':
        '生命值持续下降',
    'harder to unjam a gun':
        '更难排除卡壳',
    '{} move speed (of {})':
        '{} 移动速度（满值 {}）',
    'body at {} C':
        '体温 {} C',
    '{} carry capacity':
        '{} 负重',
    'x{} attack speed':
        'x{} 攻击速度',
    'endurance under {}%%':
        '耐力低于 {}%%',
    'fatigue over {}%%':
        '疲劳高于 {}%%',
    'hunger over {}%%':
        '饥饿高于 {}%%',
    'thirst over {}%%':
        '口渴高于 {}%%',
    'panic over {}%%':
        '恐慌高于 {}%%',
    'stress over {}%%':
        '压力高于 {}%%',
    'boredom over {}%%':
        '无聊高于 {}%%',
    'unhappiness over {}%%':
        '不快高于 {}%%',
    '{}%% action speed':
        '{}%% 动作速度',
    'anger over {}%%':
        '愤怒高于 {}%%',
    'drunkenness over {}%%':
        '醉酒高于 {}%%',
    'pain over {}%%':
        '疼痛高于 {}%%',
    'slower rope climbing':
        '爬绳更慢',
    '{}%% total body damage':
        '全身受伤 {}%%',
    'sickness over {}%%':
        '患病高于 {}%%',
    'cold strength over {}%%':
        '感冒强度高于 {}%%',
    'wetness over {}%%':
        '潮湿高于 {}%%',
    'discomfort over {}%%':
        '不适高于 {}%%',
    'rotting corpses nearby':
        '附近有腐烂的尸体',
    'x{} move speed':
        'x{} 移动速度',
    '{} discomfort per level':
        '每级 {} 不适',
    '{} C on top of the air temperature':
        '在气温基础上再 {} C',
    'carrying {}x capacity':
        '负重达到上限的 {} 倍',
    '{}%% body heat':
        '{}%% 体温',
    'no sleep without pills':
        '没有安眠药就睡不着',
    'erratic movement':
        '移动摇晃不稳',
    'raises discomfort':
        '增加不适',
    'no sprinting':
        '无法冲刺',
    'no sprinting, no exercise':
        '无法冲刺，无法锻炼',
    'zombies spot you {} sooner':
        '丧尸提前 {} 发现你',
    'muscle stiffness builds up':
        '肌肉僵硬逐渐累积',
    'cannot eat or open food':
        '无法进食或开启食物',
    '{} move speed with Adrenaline Junkie':
        '拥有肾上腺瘾君子时 {} 移动速度',
    'nightmares while asleep':
        '睡眠中做噩梦',
    'no sleep below {}%% fatigue without pills':
        '疲劳低于 {}%% 时没有安眠药就睡不着',
    '{}%% move speed':
        '{}%% 移动速度',
    'cannot move':
        '无法移动',
    '{} climbing walls and ropes':
        '{} 攀爬墙壁与绳索',
    'no running, no exercise':
        '无法奔跑，无法锻炼',
    'over {}x capacity':
        '超过上限的 {} 倍',
    'no running':
        '无法奔跑',
    'no sprinting until you drop the bulky item':
        '放下笨重物品前无法冲刺',
    'you can sleep through high pain':
        '剧痛时也能入睡',
    'no endurance recovery':
        '耐力不再恢复',
    '{} vision cone':
        '{} 视野锥',
    'delayed vehicle controls':
        '车辆操作延迟',
    'narrowed vision cone':
        '视野锥变窄',
    'no exercise':
        '无法锻炼',
    '{} wound bleeding':
        '{} 处伤口在流血',
    'Rest in peace.':
        '安息吧。',
    'Infected. There is no cure.':
        '已感染。无药可医。',
    'Stale in':
        '变质剩余',
    'Rots in':
        '腐烂剩余',
    'Cooking time':
        '烹饪时间',
    'Never':
        '永不',
    'Trains':
        '训练',
    'Critical chance':
        '暴击率',
    'Attack speed':
        '攻击速度',
    'Swing type':
        '挥击类型',
    'Heavy':
        '重型',
    'Swung':
        '挥砍',
    'Stabbing':
        '刺击',
    'Spear':
        '长矛',
    'Stone':
        '石制',
    'Knockback on hit':
        '命中击退',
    'Condition loss':
        '耐久损失',
    'Jam chance':
        '卡壳几率',
    'Accuracy':
        '精准度',
    'Noise radius':
        '噪音半径',
    'Rounds':
        '弹药',
    'Reload time':
        '装填时间',
    'Aiming time':
        '瞄准时间',
    'Used by':
        '适用武器',
    'Reading speed':
        '阅读速度',
    'Reading time left':
        '剩余阅读时间',
    'Skill too low to learn from it':
        '技能太低，无法从中学习',
    'Nothing left to learn from it':
        '已无可学',
    'Proteins':
        '蛋白质',
    'Sow in':
        '播种月份',
    'Ready in':
        '成熟剩余',
    'Burn time':
        '燃烧时间',
    # Power: charge, autonomy and light
    "Duration": "持续时间",
    "Light range": "光照范围",
    "Light strength": "光照强度",
    "Batteries and radios: charge left, how long it lasts and how far a torch lights": "电池与无线电：剩余电量、可用时长和手电筒的光照范围",
    "Vanilla draws the charge of a drainable as a bar with no number on it, and never says how long a torch lasts or how far it lights. A torch spends its UseDelta once every ten game minutes, and only while it is in a hand or attached to you: left in a bag it switches itself off. Light range and strength are the figures that actually light the ground.":
        "游戏只用一根没有数字的进度条显示消耗品的电量，也从不告诉你手电筒能用多久、能照多远。手电筒每十个游戏分钟消耗一次 UseDelta，而且只有拿在手上或挂在身上时才消耗：放进背包它会自动关闭。光照范围和强度才是真正照亮地面的数字。",
    'Rest quality':
        '休息质量',
    'Discomfort':
        '不适',
    'Stomp damage':
        '踩踏伤害',
    'Corpse sickness defense':
        '尸毒防护',
    'Filter charge':
        '滤芯余量',
    'New recipes':
        '新配方',
    'Listened':
        '已收听',
    'Skill too high for this tape':
        '技能太高，此录像无效',
    'All Info':
        'All Info',
    'Enable everything':
        '全部启用',
    'Items':
        '物品',
    'Crafting':
        '制作',
    'World':
        '世界',
    'Character':
        '角色',
    'Everything in this section':
        '本节全部',
    'Food: time left before it spoils':
        '食物：变质剩余时间',
    'Adds hours to stale and hours to rotten, at the current rate. Accounts for the fridge, the freezer and the sandbox spoilage speed.':
        '按当前速度显示距离变质和腐烂还有多少小时。已计入冰箱、冷冻柜和沙盒的腐坏速度设置。',
    'Cooking: add the warm-up minutes':
        '烹饪：加上预热时间',
    'Off by default. Cooking time is the time at temperature; this adds the four minutes the food spends heating up before it starts to cook, so an oven timer set to the figure rings when the food is done.':
        '默认关闭。烹饪时间是食物已达温度后的用时；开启后会加上食物开始烹饪前升温所需的4分钟，这样把烤箱定时器设成这个数字，铃响时食物正好做好。',
    'Food: calories, carbs, protein and fat':
        '食物：热量、碳水、蛋白质和脂肪',
    'Off by default. Showing macros on every food undoes the Nutritionist trait, which is what normally reveals them.':
        '默认关闭。在所有食物上显示营养成分会让「营养学家」特性失去意义，那本来才是解锁这些数值的途径。',
    'Melee: exact damage, speed and durability':
        '近战：精确伤害、速度与耐久',
    'Puts numbers on the condition and damage bars, and adds crit chance, swing type, attack speed, knockback and the odds of losing a condition point per hit.':
        '在耐久条和伤害条上标出数字，并补充暴击率、挥击类型、攻击速度、击退，以及每次命中损失一点耐久的概率。',
    'Firearms: range, jam chance and reload':
        '枪械：射程、卡壳几率与装填',
    'Puts numbers on the condition and damage bars, and adds accuracy, effective range, jam odds and magazine size.':
        '在耐久条和伤害条上标出数字，并补充精准度、有效射程、卡壳几率和弹匣容量。',
    'Ammo: rounds left and what it fits':
        '弹药：剩余数量与适配武器',
    'No comparison arrows here: the thing in your hands is a gun, not another magazine, so there is no honest pair to compare.':
        '这里没有比较箭头：你手里拿的是枪，不是另一个弹匣，没有诚实的对比对象。',
    'Clothing: numbers on every bar, plus discomfort':
        '衣物：所有条形图的数字，外加不适值',
    'Vanilla draws condition, insulation, wind, water, blood, dirt and wetness as bars with no figures. This writes the figures next to them and adds the discomfort value, which vanilla never shows at all.':
        '原版把耐久、保暖、防风、防水、血污、脏污和潮湿画成没有数字的条形图。这里把数字写在旁边，还加上原版从不显示的不适值。',
    'Seeds: growing time and yield':
        '种子：生长时间与产量',
    'Firewood: how long it burns':
        '柴火：燃烧时长',
    'Books: reading time and skill levels covered':
        '书籍：阅读时间与覆盖的技能等级',
    'Reading time already accounts for Fast Reader, Slow Reader and reading glasses.':
        '阅读时间已计入速读、慢读特性和老花镜。',
    'Beds: how well you recover on them':
        '床铺：恢复效果如何',
    'Masks: filter life and protection':
        '面具：滤芯寿命与防护',
    'Tapes and CDs: which skill they teach and how much XP':
        '录像带与光盘：教授什么技能、给多少经验',
    'Show the difference against what you have equipped':
        '显示与当前装备的差值',
    'Adds a coloured +/- next to weapon and clothing values. Weapons compare against what is in your hands, clothing against the piece worn in the same slot.':
        '在武器和衣物数值旁添加彩色的 +/-。武器与手上的对比，衣物与同一部位穿着的对比。',
    'Crafting: full item tooltip on the recipe output':
        '制作：配方产物显示完整物品信息',
    'Hovering the result of a recipe shows the same block an item in your inventory would, comparison included, before you craft it.':
        '把鼠标移到配方产物上，就能在制作之前看到与背包中物品相同的信息块，含对比。',
    'Generators: fuel time, wear and danger':
        '发电机：燃料时间、磨损与危险',
    'Adds noise radius, hours of fuel left, average time until {}%% condition and until it breaks, and the hourly odds of a backfire or a fire.':
        '补充噪音半径、剩余燃料小时数、降到 {}%% 耐久与彻底损坏的平均时间，以及每小时回火或起火的概率。',
    'Generators: also show times in real-world minutes':
        '发电机：同时以现实分钟显示时间',
    'Off by default. Converts the in-game hours using the current day length, so you know how long you actually have to wait.':
        '默认关闭。按当前的一天时长把游戏内小时换算过来，让你知道实际要等多久。',
    'Generators: outline the powered area on the floor':
        '发电机：在地面上勾出供电范围',
    'Draws the edge of the range while the generator window is open, green when running and red when off. Only the floor you are standing on is computed.':
        '在发电机窗口打开时描出范围边缘，运行中为绿色、停机时为红色。只计算你所在的这一层。',
    'Gas pumps: fuel left and power source':
        '加油泵：剩余油量与供电来源',
    'Adds an Info entry to the right-click menu of any gas pump, with the fuel still in the tank and whether the mains or a generator is keeping it running. The game knows that number and only prints it as a debug option.':
        '在任意加油泵的右键菜单中加入「信息」项，显示油罐中剩余的燃料，以及维持它运转的是电网还是你的发电机。游戏知道这个数字，却只在调试选项里显示。',
    'Fuel Remaining':
        '剩余燃料',
    'Mains power':
        '电网',
    'Generator':
        '发电机',
    'Walls and doors: health under the cursor':
        '墙与门：光标下的耐久',
    'Shows current and maximum health as a number at the foot of whatever you point at, no clicking needed.':
        '在你指向的物体脚下以数字显示当前与最大耐久，无需点击。',
    'Build menu: health of what you are about to build':
        '建造菜单：即将建造物的耐久',
    'Also shows what that health would be with the relevant skill at {}, so you can tell whether it is worth waiting.':
        '还会显示相关技能达到 {} 级时的耐久，让你判断值不值得再等等。',
    'Crops: health, growth and water as numbers':
        '作物：以数字显示健康、生长与水分',
    'Adds rows to the crop window you get by right-clicking a plant: health out of {}, current phase, hours to the next one, water level against what the plant needs, time since the last watering and pest levels.':
        '在右键点击作物弹出的窗口里增加数行：健康值（满 {}）、当前生长阶段、距下一阶段的小时数、当前水分与植物所需水分的对比、距上次浇水的时间，以及各类虫害等级。',
    "Crops: keep vanilla's Farming level requirements":
        '作物：保留原版的农业等级门槛',
    'Off by default, so you see everything from level {}. Turn it on and each row reappears at the Farming level vanilla itself uses for it: phase and health at {}, water at {}, pests at {}, next phase at {}.':
        '默认关闭，因此从 {} 级起就能看到全部内容。开启后，每一行会回到原版自己使用的农业等级：阶段与健康 {} 级、水分 {} 级、虫害 {} 级、下一阶段 {} 级。',
    'Noise':
        '噪音',
    'tiles':
        '格',
    'Down to %1%% (avg)':
        '降至 %1%%（平均）',
    'Breaks down in (avg)':
        '损坏剩余（平均）',
    'Backfire, loud (per hour)':
        '回火，很响（每小时）',
    'FIRE OR EXPLOSION (per hour)':
        '起火或爆炸（每小时）',
    '(real time)':
        '（现实时间）',
    'XP Boost: %1':
        '经验加成：%1',
    'Skills':
        '技能',
    'Also grants':
        '额外获得',
    'Disabled in multiplayer':
        '多人模式下禁用',
    'Foraging':
        '搜寻',
    'search radius':
        '搜寻半径',
    'weather penalty':
        '天气惩罚',
    'darkness penalty':
        '黑暗惩罚',
    'Strength when built':
        '建成时的耐久',
    'With %1 at {}':
        '%1 达到 {} 级时',
    'Show XP boosts as a multiplier, not a percentage':
        '以倍率而非百分比显示经验加成',
    'Vanilla says "{}%%" for a level {} boost. The real figure is x{}, because a skill with no boost runs at a quarter rate. Fixed on all three screens that show it.':
        '原版对 {1} 级加成显示「{0}%%」。真实数值是 x{2}，因为没有加成的技能只按四分之一速率成长。三个显示它的界面都已修正。',
    'Character creation: what each trait and job really does':
        '角色创建：每个特性和职业的真实作用',
    'Adds starting skill levels with their true XP multiplier, free traits granted, recipes taught and foraging bonuses to the tooltips in the creation screen.':
        '在创建界面的提示中加入初始技能等级及其真实经验倍率、附赠的特性、教授的配方和搜寻加成。',
    'In game: the same block on the info tab':
        '游戏中：信息页显示同样的内容块',
    'Hover a trait icon or the job icon in the character info tab to read the same block after the world has started.':
        '世界开始后，把鼠标移到角色信息页的特性图标或职业图标上，即可读到同样的内容块。',
    'Add hand-written trait effects':
        '加入手写的特性效果',
    "Effects hardcoded in the game's Java that cannot be read at runtime, so they are written by hand and checked against each build.":
        '这些效果硬编码在游戏的 Java 里，无法在运行时读取，因此由人工写出并对照每个版本核对。',
    'Skills: which recipes each level requires':
        '技能：每一级都被哪些配方要求',
    "Hover a level in the skills panel to see the recipes and builds that ask for it. Read from the game's own recipe list, so modded recipes appear too and nothing goes stale with a patch.":
        '把鼠标移到技能面板中的某一级，即可看到要求该等级的配方与建造项。数据来自游戏自身的配方表，因此其他模组的配方也会出现，且不会因为更新而过时。',
    'Needs this level':
        '需要此等级',
    'Skill and moodle descriptions are translation files. They cannot be switched off here; disable the mod to remove them.':
        '技能与状态图标的描述是翻译文件，无法在此关闭；要移除请停用模组。',
    'Run self-test':
        '运行自检',
    '{}%% footstep noise radius':
        '{}%% 脚步声半径',
    'more likely to fall when bumped':
        '被撞时更容易摔倒',
    'less likely to fall when bumped':
        '被撞时更不容易摔倒',
    '{}%% run and sprint speed':
        '{}%% 奔跑与冲刺速度',
    'no Fitness XP from level {} on':
        '从 {} 级起不再获得体能经验',
    'double endurance drain when running':
        '奔跑时耐力消耗翻倍',
    '{}%% melee damage':
        '{}%% 近战伤害',
    '{} chance to trip from a lunge':
        '{} 突刺时的绊倒几率',
    'starts at {} weight, and you lose health below {}':
        '初始体重 {}，低于 {} 开始掉血',
    '{}%% axe swing time':
        '{}%% 斧类挥击时间',
    '{}%% axe damage to trees':
        '{}%% 斧头对树木的伤害',
    '{}%% endurance lost running':
        '{}%% 奔跑耐力消耗',
    '{}%% grapple effectiveness':
        '{}%% 擒抱效果',
    '{}%% knockback':
        '{}%% 击退',
    'can be gained by training Strength to {}':
        '把力量练到 {} 级即可获得',
    'becomes Strong at Strength {}':
        '力量 {} 级时变为强壮',
    'becomes Feeble at Strength {}':
        '力量 {} 级时变为孱弱',
    'lost by training Strength to {}':
        '把力量练到 {} 级即可摆脱',
    '{}%% panic, night terrors aside':
        '{}%% 恐慌，夜惊除外',
    '{}%% stress from looting corpses':
        '{}%% 搜刮尸体带来的压力',
    '{}%% panic':
        '{}%% 恐慌',
    'no panic from a corpse reanimating':
        '尸体复活时不会恐慌',
    'no stress from looting corpses':
        '搜刮尸体不产生压力',
    '{} move speed at panic {}':
        '恐慌达到 {1} 时 {0} 移动速度',
    'still capped by the movement speed limit':
        '仍受移动速度上限限制',
    '{}%% wind penalty when aiming':
        '{}%% 瞄准时的风力惩罚',
    '{}%% gun accuracy':
        '{}%% 枪械精准度',
    '{}%% gun crit chance':
        '{}%% 枪械暴击率',
    'shorter aiming delay':
        '瞄准延迟更短',
    'wider field of view':
        '视野更广',
    '{}%% max range on weapon sights':
        '{}%% 瞄具最大射程',
    'blurry vision':
        '视线模糊',
    'weapon sight range bonus at its minimum':
        '瞄具射程加成降至最低',
    'cancelled by wearing glasses':
        '戴上眼镜即可抵消',
    '{}%% perception radius':
        '{}%% 感知半径',
    'zombies behind you become visible sooner':
        '更早看到身后的丧尸',
    'muffled sound effects':
        '声音变得沉闷',
    'zombies behind you become visible later':
        '更晚才看到身后的丧尸',
    'no sound at all':
        '完全听不到声音',
    'you can still watch TV':
        '仍然可以看电视',
    '{}%% chance of not being injured by a zombie':
        '{}%% 不被丧尸弄伤的几率',
    '{}%% chance of being scratched by trees':
        '{}%% 被树木划伤的几率',
    '{}%% corpse sickness':
        '{}%% 尸毒',
    '{}%% chance of catching a cold':
        '{}%% 感冒几率',
    '{}%% cold strength':
        '{}%% 感冒强度',
    '{}%% cold progression':
        '{}%% 感冒发展速度',
    '{}%% zombification speed':
        '{}%% 尸变速度',
    '{}%% severity of vehicle injuries':
        '{}%% 车祸伤势严重度',
    '{}%% fracture severity':
        '{}%% 骨折严重度',
    'all wounds heal much faster':
        '所有伤口愈合快得多',
    'all wounds heal much slower':
        '所有伤口愈合慢得多',
    '{}%% XP in every skill except Fitness and Strength':
        '除体能和力量外所有技能 {}%% 经验',
    '{}%% reading speed':
        '{}%% 阅读速度',
    '{}%% XP in every weapon skill and Aiming':
        '所有武器技能与枪法 {}%% 经验',
    '{}%% inventory transfer time':
        '{}%% 物品搬运时间',
    '{}%% aiming delay':
        '{}%% 瞄准延迟',
    'guns jam less often':
        '枪械更少卡壳',
    'fewer injuries opening cans':
        '开罐头时更少受伤',
    'guns jam more often':
        '枪械更常卡壳',
    'more injuries opening cans':
        '开罐头时更常受伤',
    '{}%% container capacity':
        '{}%% 容器容量',
    'crafting does not return leftover items':
        '制作不返还剩余材料',
    '{}%% thirst':
        '{}%% 口渴',
    '{}%% hunger':
        '{}%% 饥饿',
    '{}%% food illness chance':
        '{}%% 食物中毒几率',
    '{}%% food illness duration':
        '{}%% 食物中毒持续时间',
    '{}%% harm from tainted water':
        '{}%% 脏水造成的伤害',
    '{}%% tiredness gained while awake':
        '{}%% 清醒时累积的疲劳',
    '{}%% recovery while asleep':
        '{}%% 睡眠恢复',
    '{}%% sleep duration':
        '{}%% 睡眠时长',
    'you do not wake up at {} tiredness, so set an alarm':
        '疲劳降到 {} 也不会自己醒，记得上闹钟',
    'harder to fall asleep':
        '更难入睡',
    '{}%% vision in the dark':
        '{}%% 夜间视力',
    'smaller vision cone penalty at night':
        '夜间视野锥惩罚更小',
    '{}%% chance of being spotted (new stealth)':
        '{}%% 被发现几率（新潜行）',
    '{}%% chance of being spotted (old stealth)':
        '{}%% 被发现几率（旧潜行）',
    '{}%% chance of breaking kindling':
        '{}%% 弄断引火物的几率',
    '{}%% weather penalty when aiming':
        '{}%% 瞄准时的天气惩罚',
    'lights fires twice as fast':
        '生火速度快一倍',
    'almost never scratched by trees':
        '几乎不会被树木划伤',
    '{}%% endurance lost running, sprinting, carrying and dragging':
        '{}%% 奔跑、冲刺、搬运和拖拽的耐力消耗',
    '{}%% endurance lost swinging a weapon':
        '{}%% 挥击武器的耐力消耗',
    '{}%% gear change speed':
        '{}%% 换挡速度',
    '{}%% top speed':
        '{}%% 极速',
    '{}%% engine noise in reverse':
        '{}%% 倒车时的引擎噪音',
    '{}%% acceleration':
        '{}%% 加速',
    '{}%% reverse acceleration':
        '{}%% 倒车加速',
    'capped at {} max speed':
        '极速被限制在 {}',
    'engine noise unchanged':
        '引擎噪音不变',
    'less likely to fail any fence climb':
        '翻越任何围栏都更少失手',
    'slightly faster rope climbing':
        '爬绳略快',
    'bloody items transfer faster but cause stress':
        '沾血物品搬运更快，但会带来压力',
    'cannot read anything, map labels and calorie counts included':
        '什么都读不了，包括地图标注和热量数值',
    '{} panic per tick indoors, scaling down to {} in a {}-tile room':
        '室内每 tick {0} 恐慌，在 {2} 格大的房间里降至 {1}',
    'a vehicle counts as a {}-tile room':
        '车辆算作 {} 格的房间',
    '{} panic per tick whenever you are not in a room':
        '只要不在房间里，每 tick {} 恐慌',
    'faster building':
        '建造更快',
    'faster barricading':
        '加固更快',
    'no bonus health on constructions in B{}':
        '在 B{} 中不再为建筑提供额外耐久',
    'recipes need one level less of their skill':
        '配方所需的技能等级降低一级',
    'you gain weight above {} calories a day instead of {}, while under {} weight':
        '每天超过 {} 卡路里就长胖，而不是 {}，只要体重低于 {}',
    'you need {} calories a day to gain weight instead of {}, while over {} weight':
        '体重高于 {2} 时，需要每天 {0} 卡路里才会长胖，而不是 {1}',
    'unhappiness and stress rise as nicotine withdrawal builds':
        '随着尼古丁戒断加剧，不快与压力上升',
    'smoking clears the withdrawal and gives {} hunger':
        '抽烟可解除戒断，并带来 {} 饥饿',
    'random coughs and sneezes give you away':
        '随机的咳嗽和喷嚏会暴露你',
    'shows calories, carbohydrates, protein and fat on every food':
        '在所有食物上显示热量、碳水、蛋白质和脂肪',
    "no measurable effect in B{}: no XP boost, no recipes, and nothing in the game's code reads it. The recipes come from the profession itself.":
        '在 B{} 中没有可测量的效果：没有经验加成、没有配方，游戏代码里也没有任何地方读取它。配方来自职业本身。',
    'x{} move speed through trees (x{} for everyone else)':
        'x{} 穿越树林的移动速度（其他人 x{}）',
    'starts every exercise at {}{} regularity instead of {}{}':
        '每项锻炼的规律度初始为 {}{}，而不是 {}{}',
    '{} move speed':
        '{} 移动速度',
    '{} wind penalty when aiming':
        '瞄准时的风力惩罚 {}',
    '%1 °C':
        '%1 °C',
    'Adds rows to the inventory tooltip: how fast a line wears out, how much each hook helps and which fish a bait attracts.':
        '在物品提示中增加行：鱼线磨损多快、每种鱼钩有多大帮助，以及饵料会引来哪些鱼。',
    'ALLTHEINFO':
        'ALLTHEINFO',
    'Attracts':
        '引来',
    "Back to vanilla's rules: Time needs Fishing {}, Temperature {}, Weather {}, Wind {}, and a species tells you nothing until you have caught it.":
        '回到原版规则：时间需要钓鱼 {}，温度 {}，天气 {}，风 {}，而鱼种在你钓到之前什么都不会告诉你。',
    'Best baits: %1':
        '最佳饵料：%1',
    'Bite chance':
        '上钩机率',
    'Breaks into':
        '损坏后变成',
    'Chance that one attempt hooks something: {}%% times temperature, weather, time, hook and abundance, capped at {}%%.':
        '一次尝试上钩的机率：{}%% 乘以温度、天气、时间、鱼钩和鱼群密度，上限 {}%%。',
    'Fish bite more at dawn and dusk: x{} from {}:{} to {}:{} and from {}:{} to {}:{}. Any other hour is x{}.':
        '鱼在黄昏和黎明更容易咬钩：{}:{} 到 {}:{} 以及 {}:{} 到 {}:{} 为 x{}。其他时段为 x{}。',
    'Fishing gear: rods, lines, hooks and baits':
        '钓鱼装备：鱼竿、鱼线、鱼钩和饵料',
    'Fishing panel: what each rating is worth':
        '钓鱼面板：每个评价到底值多少',
    "Fishing: keep vanilla's Fishing level requirements":
        '钓鱼：保留原版的钓鱼等级限制',
    'Hook':
        '鱼钩',
    'How much longer than the best possible case you wait between attempts. Fishing near the shore doubles it, and a bobber less than {} tiles away triples it.':
        '与最佳情况相比，每次尝试之间要多等多久。靠岸边钓鱼会翻倍，浮标距离不足 {} 格则变为三倍。',
    'Lake':
        '湖',
    'Line strength':
        '鱼线强度',
    'Moodles: description box that fits its text':
        '情绪图标：随文字伸缩的说明框',
    'Needs Fishing %1':
        '需要钓鱼 %1',
    'Only bites while you reel in':
        '只有收线时才会咬钩',
    'Paperclip x{}, nail x{}, fishing hook x{}. With no hook the chance is x{}: nothing will ever bite.':
        '回形针 x{}，钉子 x{}，鱼钩 x{}。没有鱼钩时机率为 x{}：永远不会上鱼。',
    'Rain is x{}. Fog over {} or wind over {} is x{}. Fog and wind are the same x{}: they never stack.':
        '雨天为 x{}。雾超过 {} 或风超过 {} 为 x{}。雾和风是同一个 x{}：两者不会叠加。',
    'Right-click water and pick Fishing. Puts the real multiplier next to Time, Temperature, Weather and Wind, adds hook, spot, bite chance and waiting time, and explains each one on hover.':
        '右键点击水面并选择钓鱼。在时间、温度、天气和风旁边写出真实倍率，并增加鱼钩、钓点、上钩机率和等待时间，鼠标悬停时逐一说明。',
    'River':
        '河',
    'Spot':
        '钓点',
    "The game's own moodle box is two lines tall and cuts off anything longer, which is most of AllTheInfo's descriptions. This draws the moodle column itself so the box grows with the text. Turn it off to go back to the vanilla widget.":
        '游戏自带的情绪说明框只有两行高，更长的文字会被截断，而 AllTheInfo 的说明几乎都更长。这里由模组自己绘制情绪列，所以说明框会随文字变高。关闭则恢复游戏原本的控件。',
    'Trophy from %1 cm, Fishing {} and a {} in {} roll on a big catch':
        '%1 厘米起为奖杯鱼，需要钓鱼 {}，并在大鱼上钩时掷出 {}/{} 的概率',
    'Under {} fish is x{}, up to {} is x{}, over {} is x{}. Trash is what you pull out instead of a fish, and Fishing {} cuts it to {}%%, level {} to {}%% and level {} to {}%%.':
        '鱼群不足 {} 为 x{}，不超过 {} 为 x{}，超过 {} 为 x{}。垃圾就是你代替鱼拉上来的东西，钓鱼 {} 会将其降到 {}%%，{} 级降到 {}%%，{} 级降到 {}%%。',
    'Up to %1 cm and %2 kg':
        '最大 %1 厘米、%2 公斤',
    'Vanilla draws condition, insulation, wind, water, blood, dirt and wetness as bars with no figures. This writes the figures next to them and adds the discomfort value, which vanilla never shows at all. The run and combat speed modifiers get a signed figure too, which vanilla only ever draws as a bar with no sign.':
        '游戏把耐久度、保暖、防风、防水、血迹、脏污和潮湿都画成没有数字的进度条。这里在旁边写出数字，并加上游戏从不显示的不适值。跑速和战斗速度修正也会写成带符号的数字，而游戏只画成不带符号的进度条。',
    'Wait':
        '等待',
    'Waters: %1':
        '水域：%1',
    'Wear per tug':
        '每次拉扯的磨损',
    'Wind has no coefficient of its own. Over {} it sets the weather to x{}, the same penalty fog sets, and the two do not add up.':
        '风没有自己的系数。超过 {} 时它把天气变成 x{}，与雾的惩罚完全相同，且两者不相加。',
    'With your bait: %1%%':
        '用你的饵料：%1%%',
    'Your bait does not attract this one':
        '你的饵料引不来这个鱼种',
    'best possible':
        '已是最佳',
    'near shore':
        '靠近岸边',
    'no fish in this spot':
        '这里没有鱼',
    'none':
        '无',
    'trash':
        '垃圾',
    '{} to {} °C is x{}. From {} to {} and from {} to {}, x{}. Over {} or below {}, x{}. Below {} °C, x{}.':
        '{} 到 {} °C 为 x{}。{} 到 {} 以及 {} 到 {} 为 x{}。超过 {} 或低于 {} 为 x{}。低于 {} °C 为 x{}。',
    'Fish':
        '鱼群',
    'Trash':
        '垃圾',
    'Trophy from %1 cm':
        '%1 厘米起为奖杯鱼',
    'shore':
        '岸边',
    'Best baits:':
        '最佳饵料：',
    'Size: %1-%2 cm, %3-%4 kg':
        '体型：%1-%2 厘米，%3-%4 公斤',
    'Trophy: >%1 cm / >%2 kg':
        '奖杯鱼：>%1 厘米 / >%2 公斤',
    'Under {} fish is x{}, up to {} is x{}, over {} is x{}. Fish schools move every day. Trash is what you pull out instead of a fish: it is fixed per spot, and Fishing {} cuts it to {}%%, level {} to {}%% and level {} to {}%%.':
        '鱼群不足 {} 为 x{}，不超过 {} 为 x{}，超过 {} 为 x{}。鱼群每天都会移动。垃圾就是你代替鱼拉上来的东西：每个钓点的垃圾是固定的，钓鱼 {} 会将其降到 {}%%，{} 级降到 {}%%，{} 级降到 {}%%。',
    'Fishing gear: hide the combat stats':
        '钓鱼装备：隐藏战斗数据',
    "Fog over {}%% sets the weather to x{}, the same penalty wind sets, and the two never stack. Vanilla's Weather row reports neither: it says Good for rain even in a gale.":
        '雾超过 {}%% 会把天气变成 x{}，与风的惩罚完全相同，且两者从不叠加。游戏的天气那一行两者都不反映：即使刮着大风，下雨时它依然写“好”。',
    'Rain is x{}. Fog over {}%% or wind over {}%% is x{}. Fog and wind are the same x{}: they never stack.':
        '雨天为 x{}。雾超过 {}%% 或风超过 {}%% 为 x{}。雾和风是同一个 x{}：两者不会叠加。',
    "Rods, nets and fishing spears are weapons in the game's own scripts, so they get crit chance, swing type, attack speed and knockback. This drops that block on fishing gear. The condition and damage bars are drawn by the game in one call and cannot be removed by any mod.":
        '鱼竿、渔网和鱼叉在游戏自己的脚本里都算武器，所以会显示暴击率、挥击类型、攻击速度和击退。此选项会去掉钓鱼装备上的这一段。耐久度和伤害进度条由游戏一次性绘制，任何模组都无法移除。',
    'Wind has no coefficient of its own. Over {}%% it sets the weather to x{}, the same penalty fog sets, and the two do not add up.':
        '风没有自己的系数。超过 {}%% 时它把天气变成 x{}，与雾的惩罚相同，且两者不相加。',
    'Against the best possible case':
        '与最佳情况相比',
    'Any other hour: x{}':
        '其他时段：x{}',
    'Below {} °C: x{}':
        '低于 {} °C：x{}',
    'Bobber under {} tiles away: x{}':
        '浮标距离不足 {} 格：x{}',
    'Capped at {}%%':
        '上限 {}%%',
    'Fishing hook: x{}':
        '鱼钩：x{}',
    'Fishing {}, {} and {} cut trash to {}%%, {}%% and {}%%':
        '钓鱼 {}、{} 和 {} 将垃圾降到 {}%%、{}%% 和 {}%%',
    'Fog and wind never stack':
        '雾和风不会叠加',
    'Fog over {}%% or wind over {}%%: x{}':
        '雾超过 {}%% 或风超过 {}%%：x{}',
    'Nail: x{}':
        '钉子：x{}',
    'Near shore: x{}':
        '靠近岸边：x{}',
    'No hook: x{}, nothing ever bites':
        '没有鱼钩：x{}，永远不会上鱼',
    'Over {} or below {} °C: x{}':
        '超过 {} 或低于 {} °C：x{}',
    'Over {}%%: x{} on the weather':
        '超过 {}%%：天气 x{}',
    'Over {}: x{}':
        '超过 {}：x{}',
    'Paperclip: x{}':
        '回形针：x{}',
    'Rain: x{}':
        '雨天：x{}',
    'Rolled once per attempt':
        '每次尝试掷一次',
    'Same penalty as fog, they never stack':
        '与雾相同的惩罚，两者不叠加',
    'Same penalty as wind, they never stack':
        '与风相同的惩罚，两者不叠加',
    'Schools move every day':
        '鱼群每天移动',
    'This row reports neither':
        '这一行两者都不反映',
    'Trash is fixed per spot':
        '垃圾在每个钓点是固定的',
    'Under {} fish: x{}':
        '鱼群不足 {}：x{}',
    '{} to {} and {} to {} °C: x{}':
        '{} 到 {} 以及 {} 到 {} °C：x{}',
    '{} to {} °C: x{}':
        '{} 到 {} °C：x{}',
    '{} to {}: x{}':
        '{} 到 {}：x{}',
    '{}%% x temperature x weather x time x hook x fish':
        '{}%% x 温度 x 天气 x 时间 x 鱼钩 x 鱼群',
    '{}:{} to {}:{} and {}:{} to {}:{}: x{}':
        '{}:{} 到 {}:{} 以及 {}:{} 到 {}:{}：x{}',
    'Fishing {}, {} and {}: trash x{}, x{}, x{}':
        '钓鱼 {}、{} 和 {}：垃圾 x{}、x{}、x{}',
    'x time x hook x fish':
        'x 时间 x 鱼钩 x 鱼群',
    '{}%% x temperature x weather':
        '{}%% x 温度 x 天气',

    # Round 11: moodles rewritten from bytecode + wiki
    "melee damage {}%%": "近战伤害 {}%%",
    "melee damage {}": "近战伤害 {}",
    "move speed {}%%": "移动速度 {}%%",
    "move speed {}%% with Adrenaline Junkie": "肾上腺素狂人时移动速度 {}%%",
    "attack speed {}%%": "攻击速度 {}%%",
    "combat speed {}%%": "战斗速度 {}%%",
    "run speed {}%%": "奔跑速度 {}%%",
    "crit chance {}%%": "暴击率 {}%%",
    "firearm accuracy {}%%": "枪械精准度 {}%%",
    "firearm accuracy {}%% at {} tiles": "{1} 格外枪械精准度 {0}%%",
    "clearing a jam {}%%": "排除卡壳几率 {}%%",
    "climbing {}%%": "攀爬 {}%%",
    "climbing fences {}%%": "翻越栅栏 {}%%",
    "climbing walls and ropes {}%%": "攀爬墙壁与绳索 {}%%",
    "tripping over fences {}%%": "翻栅栏摔倒几率 {}%%",
    "blocking an attack {}%%": "格挡攻击 {}%%",
    "foraging {}%%": "搜寻 {}%%",
    "carry capacity {}": "负重上限 {}",
    "healing {}%%": "治疗速度 {}%%",
    "healing x{}": "治疗速度 x{}",
    "poison wears off {}%% faster": "中毒消退快 {}%%",
    "heat dissipation {}%%": "散热 {}%%",
    "heat loss {}%%": "热量流失 {}%%",
    "discomfort {}%%": "不适 {}%%",
    "medicine {}%% less effective": "药物效果降低 {}%%",
    "sleep {}{}%% less effective": "睡眠效果降低 {0}{1}%%",
    "panic x{} per wound": "每处伤口恐慌 x{}",
    "over {}%% of capacity": "超过负重上限的 {}%%",
    "health under {}%%": "生命值低于 {}%%",
    "health {}%% per hour": "每小时生命值 {}%%",
    "health drops to {}%%": "生命值降至 {}%%",
    "health drops to {}%%, then to {}%%": "生命值降至 {0}%%，随后降至 {1}%%",
    "health drops to {}%% when the air is above {} C": "气温高于 {1} C 时生命值降至 {0}%%",
    "health drops when the air is below {} C": "气温低于 {} C 时生命值下降",
    "only heals indoors, dry, under {}%% fatigue and under {}%% hunger and thirst": "仅在室内、身体干燥、疲劳低于 {}%% 且饥饿与口渴低于 {}%% 时才会痊愈",
    "vision cone narrows, cancelling Eagle Eyed": "视野锥变窄，抵消「目光锐利」",
    "{} C colder than the air": "比气温低 {} C",
    "{} wounds bleeding": "{} 处伤口流血",
    "{} wounds, or a bleeding neck": "{} 处伤口，或颈部流血",
    "no healing": "无法恢复生命",
    "no natural healing": "无法自然恢复",
    "slower healing": "恢复变慢",
    "much slower healing": "恢复慢得多",
    "slower endurance recovery": "耐力恢复变慢",
    "much slower endurance recovery": "耐力恢复慢得多",
    "endurance barely recovers": "耐力几乎不恢复",
    "endurance drains as you move and never recovers": "移动时耐力下降且不再恢复",
    "no sprinting or running": "无法冲刺与奔跑",
    "you cannot run": "无法奔跑",
    "you cannot sleep": "无法入睡",
    "you cannot eat any more": "吃不下了",
    "you can sleep on the ground and through pain": "可在地上入睡，也可忍痛入睡",
    "cannot swing a sledgehammer": "挥不动大锤",
    "hunger does not rise": "饥饿不再上升",
    "less body heat generated": "产生的体热更少",
    "body heat rises": "体温上升",
    "body heat rises sharply": "体温大幅上升",
    "thirst and fatigue rise faster": "口渴与疲劳上升更快",
    "you lose heat in the cold": "寒冷中流失体温",
    "more likely to catch a cold": "更容易感冒",
    "more likely to fall ill": "更容易生病",
    "much more likely to fall ill": "非常容易生病",
    "narrower vision cone": "视野锥变窄",
    "narrower vision and awareness": "视野与警觉下降",
    "movement, damage and attack speed drop with the wound": "移动、伤害与攻速随伤势下降",
    "you make noise": "你会发出声响",
    "you complain out loud": "你会出声抱怨",
    "you get up faster": "起身更快",
    "you weave as you walk": "走路东倒西歪",
    "timed actions take longer": "动作耗时更长",
    "unhappiness rises": "不悦上升",
    "unhappiness rises slowly": "不悦缓慢上升",
    "unhappiness rises fast": "不悦快速上升",
    "stress rises": "压力上升",
    "boredom is wiped and held down": "无聊被清空且不再上升",
    "the Desensitized trait cancels it": "麻木特质可抵消",
    "no effect until NPCs return": "在 NPC 回归前没有效果",
    "discomfort while in a vehicle": "在载具中产生不适",
    "hypothermia is hidden": "体温过低被掩盖",
    "it wakes you up": "会把你惊醒",
    "you sneeze now and then": "偶尔打喷嚏",
    "you sneeze and cough often": "经常打喷嚏与咳嗽",
    "you cough so much that hiding gets hard": "咳得难以藏身",
    "you cough constantly and draw zombies": "不停咳嗽并引来丧尸",
    "health loss": "生命流失",
    "slow health loss": "缓慢流失生命",
    "serious health loss": "严重流失生命",
    "health slowly drops": "生命缓慢下降",
    "health drops if this is infection or poison": "若为感染或中毒则生命下降",
    "death without first aid": "不急救则死亡",
    "sickness starts to build": "病情开始累积",
    "sickness builds noticeably": "病情明显累积",
    "many rotting corpses": "大量腐烂尸体",
    "more rotting corpses": "更多腐烂尸体",
    "the worst corpses can do": "尸体所能造成的极限",
    "a generator running indoors": "室内运转的发电机",
    "it will not kill you outright": "不会直接致死",
    "a gas mask or SCBA prevents it": "防毒面具或空气呼吸器可避免",
    "caused by heavy clothing, bags, bare feet or leg injuries": "由厚重衣物、背包、赤脚或腿伤引起",

    # Animals (round 10, block C)
    "Animals: butchering yield, milk, wool and old age":
        "动物：出肉量、产奶、产毛与衰老",
    "Adds rows to the animal window you get by right-clicking an animal: meat yield, blood, feathers, old age and weight ceiling, which no screen shows, plus health, hunger, thirst, attitude, milk, wool and pregnancy as numbers instead of words.":
        "在右键点击动物弹出的窗口里增加数行：任何界面都不显示的出肉量、血液、羽毛、衰老与体重上限，以及以数字而非文字显示的健康、饥饿、口渴、态度、产奶、羊毛与怀孕。",
    "Animals: keep vanilla's Animal Care level requirements":
        "动物：保留原版的畜牧等级门槛",
    "Off by default, so you see everything from level {}. Turn it on and each row reappears at the Animal Care level vanilla itself uses for it: pregnancy at {}, weight at {}, attitude at {}.":
        "默认关闭，因此从 {} 级起就能看到全部内容。开启后，每一行会回到原版自己使用的畜牧等级：怀孕 {} 级、体重 {} 级、态度 {} 级。",
    "Meat yield":
        "出肉量",
    "full in %1":
        "%1 后装满",

    # Animal hover descriptions (round 12)
    "Size x meat gene.":
        "体型 x 出肉基因。",
    "Multiplies the number of meat pieces and the calories of each one.":
        "同时乘以肉块数量和每块肉的热量。",
    "Butchering adds x{} every {} levels.":
        "屠宰每 {} 级增加 x{}。",
    "Off the ground x{}, on a butcher hook x{}.":
        "从地面上处理 x{}，挂在屠宰钩上 x{}。",
    "Litres you can drain into a bucket once it is dead.":
        "死后可以放进桶里的升数。",
    "Grows with weight.":
        "随体重增长。",
    "Feathers you get for butchering it.":
        "屠宰它能得到的羽毛。",
    "Breed maximum x size.":
        "品种上限 x 体型。",
    "{}%% until {}%% of its life expectancy, then it climbs to {}%%.":
        "在预期寿命的 {}%% 之前为 {}%%，之后一路升到 {}%%。",
    "Over {}%% it loses {}%% health every hour.":
        "超过 {}%% 每小时损失 {}%% 生命。",
    "Current weight and the most this animal can reach.":
        "当前体重与这只动物能达到的上限。",
    "Meat and blood both scale with it.":
        "出肉量和血量都随它变化。",
    "Over {}%% hunger it starts losing weight.":
        "饥饿超过 {}%% 就开始掉体重。",
    "{}{}, how much this animal puts up with you.":
        "{}{}，这只动物对你的容忍度。",
    "Each point takes {} off the chance it breaks free while being sheared.":
        "每 1 点让剪毛时挣脱的几率降低 {}。",
    "Every gain is {}, plus {} per Animal Care level.":
        "每次提升为 {}，每级畜牧再加 {}。",
    "Healthy over {}%%, off colour over {}%%, sickly over {}%%, dying below.":
        "高于 {}%% 健康，高于 {}%% 略有不适，高于 {}%% 病弱，更低则濒死。",
    "Higher is worse.":
        "数值越高越糟。",
    "Well fed under {}%%, underfed under {}%%, starving over it.":
        "低于 {}%% 吃得饱，低于 {}%% 吃不饱，更高则饥饿。",
    "Over {}%% it starts losing weight.":
        "超过 {}%% 开始掉体重。",
    "Fully watered under {}%%, thirsty under {}%%, dying of thirst over it.":
        "低于 {}%% 不渴，低于 {}%% 口渴，更高则渴到濒死。",
    "{}{}. Calm under {}, unnerved under {}, agitated under {}, wild over it.":
        "{}{}。低于 {} 平静，低于 {} 不安，低于 {} 焦躁，更高则狂躁。",
    "Over {} milk and wool grow at {} / stress of their rate.":
        "超过 {} 时，产奶与产毛的速度只有 {} / 压力 倍。",
    "Over {} a pregnancy can be lost.":
        "超过 {} 可能导致流产。",
    "Milking with stress over {} and Animal Care {} or less always fails and spills the bucket.":
        "压力超过 {} 且畜牧 {} 级或更低时，挤奶必定失败并打翻桶。",
    "Litres in the udder and what it holds.":
        "乳房里的升数与容量。",
    "It fills by capacity / {} per game hour, times the sandbox milk modifier.":
        "每游戏小时按 容量 / {} 增加，再乘以沙盒的产奶修正。",
    "Stress over {} slows it down.":
        "压力超过 {} 会拖慢它。",
    "Wool grown and the maximum.":
        "已长出的羊毛与上限。",
    "It grows by maximum / {} per game hour: {} days for a full fleece.":
        "每游戏小时按 上限 / {} 增长：{} 天长满一身。",
    "Days left before it gives birth.":
        "距离生产还有几天。",
    "Stress over {} can end the pregnancy.":
        "压力超过 {} 可能导致流产。",
    "Hours this female stays fertilised.":
        "这只雌性还能保持受精状态的小时数。",
    "When it runs out she is no longer fertilised.":
        "时间耗尽后就不再是受精状态。",

    # Wounds and healing
    "Wounds: how long each one still needs":
        "伤口：每处还需要多久",
    "Adds an Info entry under the treatments you get by clicking a body part in the health panel. Hover it and the box beside it gives the time left on every wound, what bandaging or a poultice would save, how long the bandage lasts and whether the part is mending or getting worse. The game knows all of it and only prints it in debug mode.":
        "在健康面板点击身体部位后出现的治疗选项下方添加一个「信息」条目。将光标移上去，旁边的方框会显示每处伤口的剩余时间、包扎或敷药能省下多少、绷带还能撑多久，以及该部位是在愈合还是在恶化。游戏本身知道这一切，却只在调试模式下打印。",
    "Wounds: keep vanilla's Doctor level requirements":
        "伤口：保留原版的急救等级要求",
    "Off by default, so you see everything from level {}. Turn it on and each row reappears at the Doctor level vanilla itself uses for it: scratches and lacerations at {}, deep wounds and splints at {}, fractures and stitches at {}, wound infection at {}.":
        "默认关闭，所以从等级 {} 起就能看到全部。打开后，每一行会回到游戏自己使用的急救等级：抓伤和撕裂伤在 {}，深伤口和夹板在 {}，骨折和缝合在 {}，伤口感染在 {}。",
    "Full recovery":
        "完全康复",
    "Getting worse":
        "正在恶化",
    "Healing":
        "愈合",
    "normal":
        "正常",
    "slowed by hunger, thirst or illness":
        "因饥饿、口渴或生病而减慢",
    "stopped by hunger or thirst":
        "因饥饿或口渴而停止",
    "asleep, ten times faster":
        "睡眠中，快十倍",
    "wounded parts share it":
        "处受伤部位共享",
    "Bandage life":
        "绷带寿命",
    "ready to remove":
        "可以拆线",

    # Wounds and healing, redesigned tooltip
    "Healing speed":
        "愈合速度",
    "clean for":
        "保持干净",
    "Poultice":
        "敷药",
    "Wound infection":
        "伤口感染",
    "won't close, glass inside":
        "无法愈合，里面有玻璃",
    "won't close while unbandaged":
        "不包扎就无法愈合",
    "rising":
        "上升中",

    # Wounds: shorter recovery label and infection risk
    "Recovery":
        "恢复",
    "Infection risk":
        "感染风险",

    # Percentages, ported from the multiplier wording
    "{}%% weapon damage": "{}%% 武器伤害",
    "{}%% endurance recovery": "{}%% 耐力恢复",
    "{}%% melee damage and knockback": "{}%% 近战伤害与击退",
    "{}%% move speed in combat stance": "{}%% 战斗姿态移动速度",
    "{}%% sprint speed": "{}%% 冲刺速度",
    "{}%% chance of being spotted": "{}%% 被发现的几率",
    "{}%% footstep noise": "{}%% 脚步声",
    "{}%% recoil delay": "{}%% 后坐力延迟",
    "{}%% aim settling speed": "{}%% 瞄准稳定速度",
    "{}%% aim penalty for moving (shared with Nimble)": "{}%% 移动时的瞄准惩罚（与敏捷共享）",
    "{}%% reload speed": "{}%% 装填速度",
    "{}%% racking speed": "{}%% 上膛速度",
    "{}%% XP in every Crafting skill": "所有制作类技能 {}%% 经验",
    "{}%% move speed through trees": "{}%% 穿越树林的移动速度",
    "spotting another player {}%%": "发现其他玩家 {}%%",
    "timed actions {}%%": "动作耗时 {}%%",
    "endurance drain {}%%": "耐力消耗 {}%%",
    "alcohol hits {}%%, and {}%% over {}%% hunger": "酒精效果 {0}%%，饥饿超过 {2}%% 时 {1}%%",
    "Fitness {}, which is {}%% endurance recovery instead of {}%%": "体能 {}，即耐力恢复为 {}%% 而非 {}%%",
    "{}%% attack speed": "{}%% 攻击速度",
    "{}%% crit chance": "{}%% 暴击率",
    "racking costs {}%% of the aiming time": "上膛消耗 {}%% 的瞄准时间",
    "carrying capacity {}": "负重上限 {}",
    "{} to every weapon's durability roll.": "所有武器的耐久判定 {}。",
    "Condition loss (handle)": "耐久损失 (握柄)",
    "Condition loss (head)": "耐久损失 (头部)",

    # Ronda 4: medicine, traps, weapon components, skill levels
    '%1 corpses nearby': '附近有 %1 具尸体',
    '%1%% attack time': '%1%% 攻击速度',
    '%1%% crit chance': '%1%% 暴击几率',
    '%1%% muscle strain': '%1%% 肌肉劳损',
    '%1%% weapon damage': '%1%% 武器伤害',
    '+%1 to the durability roll': '耐久判定 +%1',
    'Adds an Info entry to a placed trap: the odds of it catching anything in an hour, which animals it can take and the share of the catch each one gets, the bait and its freshness, the zone, the hourly odds of losing bait or trap, and the warning that a trap catches nothing while you stand next to it. Bait foods get a row naming what they attract.': '为放置好的陷阱添加一个信息条目：它每小时捕到东西的几率、它能捕到哪些动物以及各自占捕获量的比例、诱饵及其新鲜度、区域、每小时丢失诱饵或陷阱的几率，以及只要你站在旁边陷阱就什么都捕不到的提示。作为诱饵的食物会多出一行，说明它们能吸引什么。',
    'Bait': '诱饵',
    'Bait lost per hour': '每小时诱饵损失',
    'In the trap for': '已被困',
    'Filter left': '滤芯剩余',
    'Hits before it breaks': '损坏前可用次数',
    'Medicine: duration, delay and effect': '药品：持续时间、生效延迟与效果',
    'Medicine: the full list of effects': '药品：完整的效果列表',
    'Muscle strain per hit': '每次挥击的肌肉劳损',
    'Off by default, so you see everything from level {}. Turn it on and the trap tooltip only appears from Trapping {}, which is the level vanilla itself uses elsewhere.': '默认关闭，所以你从 {} 级起就能看到全部内容。开启后，陷阱提示只在陷阱学 {} 级起显示，这是游戏自身在别处使用的等级。',
    'Off by default. Adds everything else each pill does: what cancels it, what intoxication costs it, and the sleeping tablet overdose table.': '默认关闭。补全每种药片的其余作用：什么会取消它、醉酒会削弱多少，以及安眠药的过量服用表。',
    'Painkillers, beta blockers, antidepressants, sleeping tablets and antibiotics get how long they last, how long they take to start and what they do per minute. Every figure is recomputed from the sandbox day length.': '止痛药、β受体阻滞剂、抗抑郁药、安眠药和抗生素会显示它们持续多久、多久开始生效，以及每分钟的作用。所有数值都会根据沙盒的白昼长度重新计算。',
    'Prey': '猎物',
    'Rots once thawed': '解冻后腐烂',
    'Stale once thawed': '解冻后变质',
    'Takes effect in': '生效于',
    'Trap lost per hour': '每小时陷阱损失',
    'Traps: catch odds, bait and hours': '陷阱：捕获几率、诱饵与时段',
    "Traps: keep vanilla's Trapping level requirements": '陷阱：保留游戏原版的陷阱学等级要求',
    'Zone': '区域',
    'a second dose resets the clock, it does not add': '第二剂会重置计时，而不是累加',
    'a third of the strength above {} intoxication': '醉酒超过 {} 时只有三分之一的强度',
    'fresh for %1': '新鲜可保 %1',
    'half the strength above {} intoxication': '醉酒超过 {} 时只有一半的强度',
    'each pill counts double above {} intoxication': '醉酒超过 {} 时每颗药按两颗计',
    'holds the fever, does not cure it': '抑制发热，但不治愈',
    'incoming panic {}%% per pill, down to nothing': '每片使受到的恐慌 {}%%，直至归零',
    'it catches nothing while you are near it': '只要你在附近，它就什么都捕不到',
    'only the first dose has to wait': '只有第一剂需要等待',
    'overdose: {} pills cost {} health, {} cost {}, {} kill': '过量服用：{} 片扣 {} 点生命，{} 片扣 {} 点，{} 片致死',
    'sleeping cancels the effect': '睡眠会取消效果',
    'stale, catches nothing': '不新鲜，吸引不到任何东西',
    'the longer it waits, the likelier it comes out dead': '等得越久，出来时死亡的可能性越大',
    'to full in %1': '%1 后达到上限',
    'to zero in %1': '%1 后归零',
    'wound pain stops being recalculated while it lasts': '生效期间伤口疼痛不再重新计算',
    'zombie fever held': '丧尸热已被抑制',
    '{}%% reading time': '{}%% 阅读时间',
    'Effect': '效果',

    # Ronda 4, segunda pasada
    '%1 s': '%1 秒',
    '%1 s per round': '每发 %1 秒',
    '%1%% attack speed': '%1%% 攻击速度',
    'Details': '详情',
    'Info': '信息',
    'Possible prey': '可能的猎物',
    'Trap breaks per hour': '每小时陷阱损坏',
    'holds the fever': '抑制发热',
    'not being used (%1 corpses nearby)': '未在消耗（附近有 %1 具尸体）',
    'Bird': '鸟',
    'Active hours': '活动时段',
    'Possible prey, share of the catch': '可能的猎物，捕获占比',
    'Catch chance': '捕获几率',
    'Bait condition': '诱饵状态',
    'Trap condition': '陷阱状态',
    'while you are near it, it neither catches nor breaks': '只要你在附近，它既不会捕获也不会损坏',
    'Bait loss risk, per hour': '每小时丢失诱饵的风险',
    'Wrecked by an animal, per hour': '每小时被动物毁坏的风险',
    '%1 / h': '%1 / 小时',
    'Bait loss risk': '丢失诱饵的风险',
    'Chance of being wrecked': '被毁坏的几率',
    'Critical damage': '暴击伤害',
    'Effective durability': '有效耐久',
    'Damage with your character': '你的角色造成的伤害',
    'Reach (tiles)': '攻击距离（格）',

    # Bags and the torch beam (0.9.20)
    'All round': '全方向',
    'Beam (degrees)': '光束（度）',
    'Bags: how much they slow you down': '背包：会让你慢多少',
    "The run and combat speed a bag costs you, which the game applies and never shows. The run figure is the one you are paying right now: a bag's penalty grows by half again as it fills up, so the same pack goes from {}%% empty to {}%% full. It counts the same in your hands as on your back.": '背包让你在奔跑和战斗中损失的速度，游戏会算却从不显示。奔跑那一项就是你此刻正在承受的：背包越满惩罚越重，最多再加一半，所以同一个背包空着是 {}%%，装满是 {}%%。拿在手上和背在背上算得一样。',

    # Trait figures corrected against bytecode (0.9.21)
    "Aiming and Maintenance are not affected":
        "瞄准和维护不受影响",
    "ambient light never drops below {} in the dark":
        "黑暗中的环境光不会低于 {}",
    "can tell a poisonous wild plant from a safe one":
        "能分辨野生植物是否有毒",
    "lights a fire with a notched plank twice as fast":
        "用刻痕木板生火速度快一倍",
    "no harm at all from tainted water":
        "脏水完全不造成伤害",
    "{} health on every construction":
        "每个建筑 {} 生命值",
    "{} tiles of perception instead of {}":
        "感知范围 {} 格，而不是 {} 格",
    "{}%% XP in the six melee weapon skills":
        "六项近战武器技能 {}%% 经验",
    "{}%% chance of tearing your clothes on a tree":
        "{}%% 被树木刮破衣服的几率",
    "{}%% from any other poison":
        "{}%% 其他任何毒物的伤害",
    "{}%% from any other poison, bleach aside":
        "{}%% 其他任何毒物的伤害，漂白剂除外",
    "{}%% weather penalty in combat":
        "{}%% 战斗中的天气惩罚",

    # Per-level lines for the twenty craft skills (0.9.21)
    "%1 crop health at planting":
        "种植时作物生命 %1",
    "%1%% chance the crop is cursed if planted out of its month":
        "%1%% 在非本月份种植时作物变异的几率",
    "%1%% chance of a bonus harvest planted in its best month":
        "%1%% 在最佳月份种植时额外收成的几率",
    "%1 disease removed per treatment":
        "每次处理清除 %1 点病害",
    "%1%% chance of harvesting %2 extra vegetables":
        "%1%% 多收获 %2 个蔬菜的几率",
    "%1%% back strain planting and harvesting":
        "%1%% 种植和收获时的腰部劳损",
    "%1 points off the chance a stressed animal breaks off milking or shearing":
        "牲畜受惊时挣脱挤奶或剪毛的几率 %1 点",
    "a stressed animal never breaks off milking or shearing":
        "受惊的牲畜再也不会在挤奶或剪毛时挣脱",
    "x%1 chance of each extra part off a carcass":
        "从尸体获得每个额外部位的几率 x%1",
    "x%1 of each part":
        "每个部位的数量 x%1",
    "up to %1 blood splatters on you":
        "身上最多 %1 处血迹",
    "%1 health on everything you build":
        "你建造的所有东西 %1 生命值",
    "%1%% build time":
        "%1%% 建造时间",
    "%1%% barricading time":
        "%1%% 加固时间",
    "%1%% chance of recovering material when dismantling":
        "%1%% 拆解时回收材料的几率",
    "%1%% of the ingredient used per addition":
        "每次添加消耗 %1%% 的食材",
    "x%1 nutrients from each ingredient":
        "每份食材提供 x%1 营养",
    "rotten food can go in evolved recipes, worth %1%% of its hunger":
        "可以在进阶食谱中加入少量腐烂食物",
    "x%1 fracture healing with a splint":
        "使用夹板时骨折愈合速度 x%1",
    "a bandage lasts %1 to %2 longer":
        "绷带持续时间延长 %1 到 %2 倍",
    "%1%% time for every medical action":
        "%1%% 所有医疗动作的时间",
    "you can judge how bad a wound is":
        "你能判断伤口有多严重",
    "you can read pain, and spot the burns that need washing":
        "你能读出疼痛，并看出哪些烧伤需要清洗",
    "you can tell when stitches are ready to come out":
        "你知道什么时候可以拆线",
    "you spot a wound infection straight away":
        "你能立刻发现伤口感染",
    "%1%% chance of getting the patch back":
        "%1%% 取回补丁的几率",
    "%1%% time to add or remove a patch":
        "%1%% 添加或移除补丁的时间",
    "a hole can be repaired completely, defense and insulation included":
        "破洞可以完全修复，包括防护和保暖",
    "+%1%% generator condition per repair":
        "每次维修 +%1%% 发电机状态",
    "%1 points to the chance of hotwiring a car":
        "热接汽车成功率 %1 点",
    "%1%% chance of setting off the car alarm":
        "%1%% 触发汽车警报的几率",
    "you can salvage and repair a standard engine":
        "可以拆解和维修普通引擎",
    "you can salvage and repair a heavy-duty engine":
        "可以拆解和维修重型引擎",
    "you can salvage and repair a sport engine":
        "可以拆解和维修跑车引擎",
    "you can build the sturdier brick wall":
        "可以建造更坚固的砖墙",
    "small %1%%, medium %2%%, large %3%%":
        "小型 %1%%，中型 %2%%，大型 %3%%",
    "%1 points to the chance a berry or mushroom is poisonous":
        "浆果或蘑菇有毒的几率 %1 点",
    "%1%% time to inspect a track":
        "%1%% 检查足迹的时间",
    "no effect of its own, this level only unlocks the recipes below":
        "本身没有效果，这一级只解锁下面的配方",

    # 0.9.21 follow-up
    "%1 rags when you rip up clothing, capped by the parts it covers":
        "撕开衣物时多 %1 块布，上限为该衣物覆盖的部位数",
    "rotten food can go in evolved recipes, worth %1%% of its hunger":
        "腐烂食物可以用于进阶食谱，提供其饱食度的 %1%%",

    # 0.9.21 follow-up 2
    "%1%% time per litre shearing an animal":
        "给动物剪毛时每升 %1%% 时间",
    "%1 rags when you rip up clothing, capped by the parts it covers":
        "撕开衣物时多 %1 块破布，上限为该衣物覆盖的部位数",
    "%1 to the most aramid thread you can pull out":
        "可抽出芳纶线的上限 %1",
    "starts at {} weight, becomes Emaciated at {} or less and Low Weight above {}":
        "初始体重 {}，{} 或更低变为瘦骨嶙峥，高于 {} 变为体重过轻",
    "starts at {} weight, becomes High Weight below {}":
        "初始体重 {}，低于 {} 变为体重过重",
    "starts at {} weight, becomes Very High Weight at {} and is lost below {}":
        "初始体重 {}，达到 {} 变为身肥体胖，低于 {} 则失去",
    "starts at {} weight, becomes Very Low Weight at {} or less and is lost above {}":
        "初始体重 {}，{} 或更低变为身形消瘦，高于 {} 则失去",
    "XP awarded":
        "获得经验",
    "{} chance to trip when a zombie lunges through a window":
        "{} 僵尸从窗户扑来时的牐倒几率",
    "{} to the roll that keeps you on your feet when a zombie shoves you":
        "{} 僵尸推撞时保持站立的判定",
    "{}%% muscle strain":
        "{}%% 肌肉劳损",
    "{}%% axe attack speed, chopping trees included":
        "斧类攻击速度 {}%%，含伐木",

    # B42.20 trait corrections
    "Another x{} at panic level {}":
        "恐慌 {1} 级时额外 x{0}",
    "Can hotwire without Electrical {} and Mechanics {}":
        "无需电工 {} 和机械 {} 即可接线打火",
    "Engine revs three times faster in reverse":
        "倒车时转速上升快三倍",
    "Halves your rope climbing bonus":
        "爬绳加成减半",
    "No unhappiness from looting corpses":
        "搜刮尸体不产生不快",
    "Stress from handling bloody items":
        "处理沾血物品会产生压力",
    "{} move speed at panic level {}, {} at level {}":
        "恐慌 {1} 级时移动速度 {0}，{3} 级时 {2}",
    "{} to the rope climbing roll":
        "{} 爬绳判定",
    "{}%% acceleration, fading out above {}%% of the car's top speed":
        "{}%% 加速，超过车辆极速的 {}%% 后逐渐消失",
    "{}%% carry capacity":
        "{}%% 负重上限",
    "{}%% chance of breaking a window lock instead of {}%%":
        "{0}%% 弄坏窗户插销，而非 {1}%%",
    "{}%% endurance cost on every exertion":
        "每次用力消耗 {}%% 耐力",
    "{}%% reverse acceleration, gone past {} km/h":
        "{}%% 倒车加速，超过 {} km/h 后消失",
    "{}%% unhappiness from looting corpses":
        "{}%% 搜刮尸体带来的不快",

    # Repair recipes
    "Repair: +%1 condition, %2 chance of failing":
        "修理：+%1 耐久，%2 失败",
    "Repair: +%1 condition, %2 chance of failing, repaired %3 times":
        "修理：+%1 耐久，%2 失败，已修理 %3 次",

    # Corpse count and temperature figures
    "Body temperature: the number on every bar":
        "体温：每条进度条上的数字",
    "Nauseous: how many corpses are making you ill":
        "恶心：有多少尸体在让你生病",
    "Rotting corpses nearby raise food sickness, and the game never says how many are close enough. Five or fewer do nothing. The count is read back out of the game, so it follows the sandbox setting.":
        "附近腐烂的尸体会提高食物中毒，而游戏从不告诉你有多少具足够近。五具或更少不起作用。数量是从游戏本身读回的，所以会跟随沙盒设置。",
    "The temperature view prints its value on Insulation and Wind resistance and leaves the other nine bars as a colour. This sets the same flag on the rest, so skin temperature, body response, heat and wetness read as figures. Vanilla does the drawing, and only for the body part you have selected.":
        "温度视图只在「保暖」和「防风」上写出数值，其余九条只是颜色。这里给其余的加上同一个标记，于是皮肤温度、身体反应、热量和湿度都变成数字。绘制由游戏本身完成，且只针对你选中的身体部位。",

    # Options tab
    "Custom":
        "自定义",
    "Nothing matches that":
        "没有匹配的项",
    "Moodles: how many corpses are making you ill":
        "状态图标：有多少尸体在让你生病",

    # Option groups
    "Every gun this box or magazine fits, one per row.":
        "这盒子或弹匣适配的每一把枪，一行一把。",
    "How bloody the garment is, out of a hundred.":
        "衣物沾血的程度，满分一百。",
    "How brightly it lights what it reaches.":
        "照到的地方有多亮。",
    "How dirty the garment is, out of a hundred.":
        "衣物脏污的程度，满分一百。",
    "How drunk this container will get you.":
        "这一容器会让你醉到什么程度。",
    "How far the light reaches, in tiles.":
        "光能照多远，以格为单位。",
    "How far the shot is heard, which is how far the horde comes from.":
        "枪声能传多远，也就是尸潮会从多远赶来。",
    "How long before the pill starts working, and only while you have none running.":
        "药片多久才开始起效，只在你身上没有药效时显示。",
    "How long cooked food can stay on the heat before it burns.":
        "煮好的食物还能在火上放多久才烧焦。",
    "How long the charge lasts with the thing switched on.":
        "开着的时候这些电量能撑多久。",
    "How long the filter lasts at your current exposure, and how many corpses are around you.":
        "按你当前的暴露程度滤芯还能撑多久，以及你周围有多少尸体。",
    "How long the item burns for as fuel.":
        "这件物品当作燃料能烧多久。",
    "How long the pages you have not read yet will take.":
        "你还没读的页数要花多久。",
    "How long the pill keeps working.":
        "药片的效果持续多久。",
    "How long the plant takes to be ready, at the current farming speed.":
        "按当前的耕种速度，作物多久才长好。",
    "How long until the food goes stale, at the current rot speed.":
        "按当前的腐坏速度，食物多久会变得不新鲜。",
    "How long until the food is rotten, at the current rot speed.":
        "按当前的腐坏速度，食物多久会腐烂。",
    "How many hits the weapon has left in it, which is the one figure that compares any two weapons.":
        "这把武器还能打多少下，这是唯一能比较任意两把武器的数字。",
    "How much cold the garment keeps out. The game only draws a bar.":
        "衣物能挡住多少寒冷。游戏只画一条进度条。",
    "How much is left in the filter.":
        "滤芯还剩多少。",
    "How much of it you have already heard.":
        "你已经听过多少了。",
    "How much of the corpse sickness the mask keeps off you. {}%% is immunity.":
        "面具能替你挡掉多少尸臭病。{}%% 就是完全免疫。",
    "How much of your hunger bar the drink covers.":
        "这份饮料能补上多少饥饿条。",
    "How much of your thirst bar the drink covers.":
        "这份饮料能补上多少口渴条。",
    "How much pull the rod takes before the line gives.":
        "鱼竿能承受多大的拉力才断线。",
    "How much rain the garment keeps out. The game only draws a bar.":
        "衣物能挡住多少雨水。游戏只画一条进度条。",
    "How much the bag slows you down, with its weight and what is inside counted.":
        "背包让你慢多少，已算上它的重量和里面装的东西。",
    "How much the bag slows your swing.":
        "背包让你的挥击慢多少。",
    "How much the garment slows you down, as the penalty itself rather than a bar.":
        "衣物让你慢多少，直接给出惩罚本身，而不是一条进度条。",
    "How much the garment slows your swing, as the penalty itself rather than a bar.":
        "衣物让你的挥击慢多少，直接给出惩罚本身，而不是一条进度条。",
    "How much tiredness this surface actually clears, your traits included.":
        "睡在这个表面实际能消掉多少疲劳，已算上你的特性。",
    "How much wind the garment keeps out. The game only draws a bar.":
        "衣物能挡住多少风。游戏只画一条进度条。",
    "How often a hit crits, with your level in the weapon's own skill counted.":
        "命中出暴击的频率，已算上你在该武器技能上的等级。",
    "How often a shot crits.":
        "开枪出暴击的频率。",
    "How wet the garment is, out of a hundred.":
        "衣物潮湿的程度，满分一百。",
    "In tiles. A swing landed at the edge of your reach does up to twice the damage of one landed close in.":
        "以格为单位。在攻击距离边缘打中，伤害最高可达贴身打中的两倍。",
    "Off by default: the game only reveals this block for packaged food or a Nutritionist.":
        "默认关闭：游戏只对包装食品或营养师显示这一段。",
    "Rounds in the magazine right now, out of what it holds.":
        "弹匣里现在有多少发，以及总共装得下多少发。",
    "The calibre the magazine takes.":
        "弹匣使用的口径。",
    "The calories in what is actually in the container, mixtures included.":
        "容器里实际装的东西含有多少热量，包含混合液。",
    "The carbohydrates in what is actually in the container.":
        "容器里实际装的东西含有多少碳水化合物。",
    "The charge left, as a number instead of a bar.":
        "剩余电量，以数字而不是进度条呈现。",
    "The edge, and the ceiling a worn head puts on it: blunt, the weapon loses the top of its damage range.":
        "锋利度，以及磨损的头部给它设的上限：不锋利，武器就失去伤害区间的上半段。",
    "The exact minimum and maximum. The game only ever draws it as a bar.":
        "精确的最小值和最大值。游戏只把它画成一条进度条。",
    "The exact points left, and the head's own count on a weapon that has one.":
        "精确的剩余耐久点数，有头部的武器还单独算头部。",
    "The exact points left, where the game only draws a bar.":
        "精确的剩余点数，而游戏只画一条进度条。",
    "The fat in what is actually in the container.":
        "容器里实际装的东西含有多少脂肪。",
    "The fatigue each swing costs you.":
        "每一次挥击消耗你多少体力。",
    "The furthest tile the gun can hit.":
        "枪能打到的最远一格。",
    "The gun's own hit chance, before your aiming skill.":
        "武器本身的命中率，还没算上你的枪法技能。",
    "The hook fitted, and what it does to your odds of a bite.":
        "装着的鱼钩，以及它如何改变你上钩的几率。",
    "The line fitted, and how much of it each tug wears away.":
        "装着的鱼线，以及每次拉扯磨损多少。",
    "The months it can be sown in, one per row.":
        "可以播种的月份，一行一个。",
    "The multiplier your shoes put on stomping a downed zombie. Footwear only.":
        "你的鞋子给踩踏倒地丧尸带来的倍率。仅限鞋类。",
    "The multiplier your skill puts on this weapon's swing.":
        "你的技能给这把武器挥击带来的倍率。",
    "The net pace of the pill, which is what compares two of them at a glance.":
        "药片的净速率，这是一眼比较两种药片的依据。",
    "The odds of losing a point of condition on a hit, with Maintenance and the weapon's skill counted.":
        "一次命中掉一点耐久的几率，已算上维修技能和该武器的技能。",
    "The odds of losing a point of condition per shot.":
        "每开一枪掉一点耐久的几率。",
    "The poison the drink carries, and only while the game is willing to tell you.":
        "真实的卡壳几率，包含磨损和握持不稳。",
    "The proteins in what is actually in the container.":
        "容器里实际装的东西含有多少蛋白质。",
    "The real odds of a jam, wear and a weak grip included.":
        "饮料里带的毒，且只在游戏愿意告诉你的时候显示。",
    "The real seconds a reload takes, with your reloading skill and your panic counted.":
        "一次换弹实际要几秒，已算上你的换弹技能和恐慌。",
    "The real seconds spent lining up the shot, with your aiming skill and your traits counted.":
        "举枪瞄准实际要几秒，已算上你的枪法技能和特性。",
    "The recipes it teaches that you do not know yet, one per row.":
        "它能教而你还不会的配方，一行一个。",
    "The swing animation, which is what really separates a slow weapon from a fast one.":
        "挥击动作，这才是慢武器和快武器真正的区别。",
    "What a critical is worth, from {}%% to {}%% depending on the weapon. The game shows it nowhere.":
        "一次暴击值多少，视武器从 {}%% 到 {}%%。游戏在任何地方都不显示。",
    "What feeds the Uncomfortable moodle. The game never shows it on the garment at all.":
        "驱动“不适”心情的数值。游戏在衣物上完全不显示它。",
    "What is left in your hands when the rod breaks.":
        "鱼竿断掉后你手上还剩什么。",
    "What sleeping here costs you in comfort.":
        "睡在这里在舒适度上要付出什么代价。",
    "What the drink does to boredom and unhappiness, which move together here.":
        "饮料对无聊和不快的影响，这里两者一起变动。",
    "What the drink does to your fatigue bar.":
        "饮料对你疲劳条的影响。",
    "What the drink does to your stress.":
        "饮料对你压力的影响。",
    "What the food still needs, and the temperature the figure assumes.":
        "食物还差多少，以及这个数字假定的温度。",
    "Whether it is a cone you aim or a lamp that lights all around, and how wide the cone is.":
        "是你要瞄准的光锥，还是照亮四周的灯，以及光锥有多宽。",
    "Which fish this bait brings in.":
        "这种鱼饵能引来哪些鱼。",
    "Which skill the tape or disc trains and how much experience is left in it.":
        "这盘带子或碟片训练哪项技能，以及里面还剩多少经验。",
    "Which skill the weapon trains, and therefore which one drives its damage and its speed.":
        "武器训练哪项技能，也就是哪项技能带动它的伤害和速度。",
    "Your own reading speed, traits, glasses and sitting down included.":
        "你自己的阅读速度，包含特性、眼镜和坐下。",
    "Nutrition":
        "营养",
    "Sleep":
        "睡眠",
    "How much the bag slows your attack. It multiplies the weapon's own swing speed, not your walking.":
        "那个背包让你的攻击慢多少。它乘的是武器本身的挥击速度，不是你的走路速度。",
    "How much the garment slows your attack. It multiplies the weapon's own swing speed, not your walking.":
        "那件衣服让你的攻击慢多少。它乘的是武器本身的挥击速度，不是你的走路速度。",
    "Best baits":
        "最佳鱼饵",
    "Every animal this trap can catch and its share of the catch.":
        "这个陷阱能抓到的每种动物，以及各自在捕获中的占比。",
    "Feathers":
        "羽毛",
    "Fog on a line of its own, because the game lumps it into weather and then reports neither.":
        "雾单独占一行，因为游戏把它并进天气里，然后两者都不报。",
    "Glass or a bullet still in the wound, which stops it healing until it is out.":
        "还留在伤口里的玻璃或子弹，不取出来伤口就不会愈合。",
    "How far the disease has gone, out of a hundred.":
        "病害发展到什么程度，满分一百。",
    "How far the generator is heard, halved when it stands indoors.":
        "发电机能被听到多远，放在室内时减半。",
    "How full the udder is and whether it can be milked yet.":
        "乳房有多满，以及现在能不能挤奶。",
    "How hungry the animal is, and how long its feed will last.":
        "这只动物有多饿，以及它的饲料还能撑多久。",
    "How long before old age starts costing the animal its yield.":
        "还有多久衰老会开始削减这只动物的产出。",
    "How long each cut, scratch, burn or bite still needs.":
        "每一处割伤、抓伤、烧伤或咬伤还需要多久。",
    "How long is left of a pregnancy, or of an egg being fertilised.":
        "怀孕还剩多久，或者蛋还有多久受精完成。",
    "How long since the last watering. The game works it out to pick a colour and then never shows it.":
        "距离上次浇水过了多久。游戏算出它只为了挑颜色，然后从不显示。",
    "How long the bandage lasts before it is dirty and worth changing.":
        "绷带能撑多久才会变脏、值得更换。",
    "How long the catch has been waiting in there.":
        "猎物已经在里面等了多久。",
    "How long the fracture needs, and what the splint on it is worth.":
        "骨折还需要多久，以及上面的夹板值多少。",
    "How long the fuel in the tank lasts at the current draw.":
        "按当前消耗，油箱里的燃料还能撑多久。",
    "How long the part needs to be whole again, and how fast it is healing.":
        "这个部位恢复完整还需要多久，以及愈合有多快。",
    "How long the stiffness in that limb takes to pass.":
        "那条肢体的僵硬要多久才会消。",
    "How long the stitches need, and when they can come out.":
        "缝线还需要多久，以及什么时候可以拆。",
    "How long until it breaks down for good, on average.":
        "平均还有多久它会彻底损坏。",
    "How long until it wears down to the point where it can catch fire.":
        "还有多久它会磨损到可能起火的程度。",
    "How long until the crop moves to its next stage.":
        "作物还有多久进入下一个生长阶段。",
    "How long you will wait compared with the best possible spot.":
        "和最好的钓点相比，你要多等多久。",
    "How many feathers butchering will give.":
        "宰杀能得到多少羽毛。",
    "How many fish this spot still holds, and what that is worth.":
        "这个钓点还剩多少鱼，以及那值多少。",
    "How much blood butchering will give.":
        "宰杀能得到多少血。",
    "How much fertiliser the plot holds. Above one is the too much case in the game's own code.":
        "这块地里有多少肥料。按游戏自己的代码，超过一就是过量。",
    "How much meat butchering will give, which is what answers whether it is worth killing yet.":
        "宰杀能得到多少肉，这正是“现在杀值不值”的答案。",
    "How much of the bait is still good.":
        "鱼饵还有多少是好的。",
    "How much the animal trusts you, which is what lets you handle it.":
        "这只动物有多信任你，这正是你能不能摆弄它的关键。",
    "How much wool has grown back and whether it can be sheared yet.":
        "羊毛长回来多少，以及现在能不能剪。",
    "How stressed the animal is, out of a hundred.":
        "这只动物压力有多大，满分一百。",
    "How the wound infection is going, and whether it is still rising.":
        "伤口感染进展如何，以及还在不在上升。",
    "How thirsty the animal is, and how long its water will last.":
        "这只动物有多渴，以及它的水还能撑多久。",
    "Level needed":
        "所需等级",
    "Lodged objects":
        "嵌入的异物",
    "Odds with your bait":
        "用你的饵时的几率",
    "Predator":
        "掠食性",
    "Size and weight":
        "体型与重量",
    "Strength at the top skill level":
        "满级时的强度",
    "The Fishing level this species needs before it will bite.":
        "这个鱼种要咬钩所需要的钓鱼等级。",
    "The animal's health as a number.":
        "以数字呈现的动物健康。",
    "The animal's weight, and how far it still has to grow.":
        "这只动物的体重，以及它还能长多少。",
    "The chance of this exact species with the bait you are using.":
        "用你正在使用的鱼饵，钓到这个鱼种的几率。",
    "The crop's health out of a hundred. The game only prints it with debug on.":
        "作物的健康，满分一百。游戏只在开启调试时才写出来。",
    "The fuel still in the tank. The game knows the number and only prints it as a debug option.":
        "油箱里还剩的燃料。游戏知道这个数字，却只把它当调试选项显示。",
    "The health the wall or door will have when you build it at your current level.":
        "以你当前的等级建造时，这面墙或这扇门会有的耐久。",
    "The hourly odds of a bang loud enough to pull zombies in.":
        "每小时发生一次足以把丧尸引过来的爆响的几率。",
    "The hourly odds of a fire or an explosion, which set the generator to zero outright.":
        "每小时起火或爆炸的几率，这两者会直接把发电机打到零。",
    "The hourly odds of the bait being taken without a catch.":
        "每小时鱼饵被叼走却什么也没抓到的几率。",
    "The hourly odds of the trap being wrecked.":
        "每小时陷阱被破坏的几率。",
    "The hourly odds of the wound becoming infected.":
        "每小时伤口被感染的几率。",
    "The hours of the day the trap actually works.":
        "一天当中陷阱真正起作用的时段。",
    "The kind of ground the trap is standing on, which decides what can come.":
        "陷阱所在的地形类型，它决定什么动物会来。",
    "The odds of a bite once every factor is put together.":
        "把所有因素都算进去之后的上钩几率。",
    "The odds of catching anything at all in an hour.":
        "一小时内抓到任何东西的几率。",
    "The range of lengths and weights this species comes in.":
        "这个鱼种的体长和体重范围。",
    "The share of your catches that will be junk here.":
        "你在这里的渔获中会有多大比例是垃圾。",
    "The two things the game never says: a long wait kills the catch, and standing nearby stops the trap.":
        "游戏从不说的两件事：等太久猎物会死，而你站在旁边陷阱就不工作。",
    "The water level as a number, and the amount this seed actually needs.":
        "以数字呈现的水分，以及这种种子真正需要的量。",
    "Time to the danger threshold":
        "距危险阈值的时间",
    "Trophy size":
        "奖杯尺寸",
    "Warnings":
        "提示",
    "Warns that the species only bites while you reel in.":
        "提醒该鱼种只在你收线时才咬钩。",
    "What a catch has to beat to count as a trophy.":
        "一条鱼要超过多少才算奖杯。",
    "What the herbs in the bandage are adding.":
        "绷带里的草药带来了什么。",
    "What the same build would have at level {}, which is the reason to know the figure before building.":
        "同样的建造在 {} 级时会是多少，这正是开工前该知道这个数字的理由。",
    "What the time of day is worth, as the multiplier behind the game's own rating.":
        "一天中的时辰值多少，也就是游戏那个评级背后的倍率。",
    "What the water temperature is worth, with the actual reading in degrees.":
        "水温值多少，并附上实际的度数读数。",
    "What the weather is worth, as the multiplier behind the game's own rating.":
        "天气值多少，也就是游戏那个评级背后的倍率。",
    "What the wind is worth. Past half strength it costs the same penalty fog does, and the two never stack.":
        "风值多少。超过一半强度时它的惩罚和雾相同，而且两者从不叠加。",
    "Whether the mains or a generator is keeping the pump running.":
        "是市电还是发电机在维持这台油泵运转。",
    "Which animals a bait item brings in.":
        "作为鱼饵的物品会引来哪些动物。",
    "Which bait is in the trap, and whether it is still fresh.":
        "陷阱里放的是什么饵，以及它是否还新鲜。",
    "Which baits work best on this species.":
        "哪些鱼饵对这个鱼种最有效。",
    "Which growth stage the crop is on, out of the total.":
        "作物处于第几个生长阶段，以及总共有几个。",
    "Which hook is fitted and what it does to your odds.":
        "装的是哪种鱼钩，以及它如何改变你的几率。",
    "Raw eggs never make you ill":
        "生鸡蛋永远不会让你不适",
    "{}%% wait before another anti-nausea food works":
        "再吃一次止吐食物的等待时间 {}%%",
    "{}%% weapon sight range":
        "瞄准镜射程 {}%%",
    "At Axe {} you swing as fast as a maxed axe user":
        "斧头技能 {} 级时，你的挥砍速度等同满级斧手",
    "{}%% from any poisonous food or drink":
        "任何有毒食物或饮料的影响 {}%%",
    "{}%% chance of illness from rotten food":
        "因腐烂食物患病的几率 {}%%",
    "Melee weapons":
        "近战武器",
    "Firearms":
        "枪械",
    "Drinks":
        "饮品",
    "Skill XP":
        "技能经验",
    "Weapons":
        "武器",
    "Worn and carried":
        "衣物与容器",
    "Medicine and reading":
        "药品与阅读",
    "Supplies":
        "物资",
    "Comparison":
        "对比",
    "Power and fuel":
        "电力与燃料",
    "Animals and traps":
        "动物与陷阱",
    "Traits and jobs":
        "特质与职业",
    "Moodles":
        "状态图标",
}
