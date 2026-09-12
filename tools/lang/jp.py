"""Japanese phrase table for AllInfo.

Keys are the English fragment with every number replaced by {} in order.
Numbers are never written here: they ride through untouched. Use {0} {1} ...
instead of {} when the language needs a different order -- and then index every
slot, Python refuses to mix the two forms.

Run `python tools\\i18n.py` after editing: it checks the arity of every line and
refuses to write a language file it cannot fill completely.
"""

T = {
    # Per-level skill descriptions
    "x{} weapon damage (x{} untrained)": "武器ダメージ x{}（未修得は x{}）",
    "{} to the durability roll": "耐久判定に {}",
    "{} chance to trip vaulting a fence": "柵を乗り越えるときの転倒率 {}",
    "{}%% fall damage": "落下ダメージ {}%%",
    "x{} endurance recovery (x{} untrained)": "スタミナ回復 x{}（未修得は x{}）",
    "x{} melee damage and knockback (x{} untrained)": "近接ダメージとノックバック x{}（未修得は x{}）",
    "x{} carrying capacity (x{} untrained)": "所持重量 x{}（未修得は x{}）",
    "x{} move speed in combat stance (x{} untrained)": "戦闘姿勢での移動速度 x{}（未修得は x{}）",
    "x{} sprint speed (x{} untrained)": "疾走速度 x{}（未修得は x{}）",
    "x{} chance of being spotted (x{} untrained)": "発見される確率 x{}（未修得は x{}）",
    "x{} footstep noise (x{} untrained)": "足音の大きさ x{}（未修得は x{}）",
    "{} accuracy (the weapon's aiming modifier, {} on nearly every gun)":
        "命中 {}（武器の照準補正。ほぼすべての銃で {}）",
    "{} wind penalty when aiming (of {})": "照準時の風ペナルティ {}（最大 {}）",
    "x{} reload speed (x{} untrained)": "リロード速度 x{}（未修得は x{}）",
    "x{} racking speed (x{} untrained)": "装填動作の速度 x{}（未修得は x{}）",
    "racking costs {} of the aiming time ({} untrained)": "装填動作で照準時間の {} を消費（未修得は {}）",
    "From here on you no longer count as unsteady with a firearm, as long as your Strength is {} or more: jam chance drops by {} percentage points.":
        "このレベル以降、筋力が {} 以上なら銃の扱いが不安定とはみなされなくなり、ジャム率が {} ポイント下がる。",
    "You never count as unsteady with a firearm again, whatever your Strength.":
        "筋力にかかわらず、以後は銃の扱いが不安定とみなされることはない。",

    # Moodles
    "{} melee to-hit": "近接命中 {}",
    "{} climb chance": "よじ登り成功率 {}",
    "{} trip chance": "転倒率 {}",
    "{} to break a zombie's grab": "ゾンビの拘束を振りほどく判定に {}",
    "{}%% strength": "筋力 {}%%",
    "{}%% healing": "治癒速度 {}%%",
    "losing health": "体力が減っていく",
    "harder to unjam a gun": "ジャムの解除が難しくなる",
    "{} move speed (of {})": "移動速度 {}（最大 {}）",
    "body at {} C": "体温 {} C",
    "{} carry capacity": "所持重量 {}",
    "x{} attack speed": "攻撃速度 x{}",
    "endurance under {}%%": "スタミナ {}%% 未満",
    "fatigue over {}%%": "疲労 {}%% 超",
    "hunger over {}%%": "空腹 {}%% 超",
    "thirst over {}%%": "喉の渇き {}%% 超",
    "panic over {}%%": "パニック {}%% 超",
    "stress over {}%%": "ストレス {}%% 超",
    "boredom over {}%%": "退屈 {}%% 超",
    "unhappiness over {}%%": "不幸 {}%% 超",
    "{}%% action speed": "行動速度 {}%%",
    "anger over {}%%": "怒り {}%% 超",
    "drunkenness over {}%%": "酩酊 {}%% 超",
    "pain over {}%%": "痛み {}%% 超",
    "slower rope climbing": "ロープの上り下りが遅くなる",
    "{}%% total body damage": "全身のダメージ {}%%",
    "sickness over {}%%": "病気 {}%% 超",
    "cold strength over {}%%": "風邪の強さ {}%% 超",
    "wetness over {}%%": "濡れ {}%% 超",
    "discomfort over {}%%": "不快 {}%% 超",
    "rotting corpses nearby": "近くに腐乱死体がある",
    "x{} move speed": "移動速度 x{}",
    "{} discomfort per level": "レベルごとに不快 {}",
    "{} C on top of the air temperature": "気温にさらに {} C",
    "carrying {}x capacity": "所持重量の {} 倍を運搬中",
    "{}%% body heat": "体温 {}%%",
    "no sleep without pills": "睡眠薬なしでは眠れない",
    "erratic movement": "足元がふらつく",
    "raises discomfort": "不快が上がる",
    "no sprinting": "疾走できない",
    "no sprinting, no exercise": "疾走も運動もできない",
    "zombies spot you {} sooner": "ゾンビに {} 早く気づかれる",
    "muscle stiffness builds up": "筋肉のこわばりが蓄積する",
    "cannot eat or open food": "食事も食品の開封もできない",
    "{} move speed with Adrenaline Junkie": "アドレナリン中毒があると移動速度 {}",
    "nightmares while asleep": "睡眠中に悪夢を見る",
    "no sleep below {}%% fatigue without pills": "睡眠薬なしでは疲労 {}%% 未満で眠れない",
    "{}%% move speed": "移動速度 {}%%",
    "cannot move": "移動できない",
    "{} climbing walls and ropes": "壁とロープのよじ登りに {}",
    "no running, no exercise": "走ることも運動もできない",
    "over {}x capacity": "所持重量の {} 倍超",
    "no running": "走れない",
    "no sprinting until you drop the bulky item": "かさばる物を下ろすまで疾走できない",
    "you can sleep through high pain": "強い痛みがあっても眠れる",
    "no endurance recovery": "スタミナが回復しない",
    "{} vision cone": "視界の角度 {}",
    "delayed vehicle controls": "車の操作が遅れる",
    "narrowed vision cone": "視界の角度が狭まる",
    "no exercise": "運動できない",
    "{} wound bleeding": "出血中の傷 {} 箇所",
    "Rest in peace.": "安らかに。",
    "Infected. There is no cure.": "感染。治療法はない。",

    # Tooltip labels
    "Stale in": "劣化まで",
    "Rots in": "腐敗まで",
    "Cooking time": "調理時間",
    "Never": "しない",
    "Critical chance": "クリティカル率",
    "Trains": "鍛える技能",
    "Attack speed": "攻撃速度",
    "Swing type": "振り方",
    "Heavy": "重量",
    "Swung": "薙ぎ払い",
    "Stabbing": "刺突",
    "Spear": "槍",
    "Stone": "石器",
    "Knockback on hit": "命中時のノックバック",
    "Condition loss": "耐久の減少率",
    "Jam chance": "ジャム率",
    "Accuracy": "命中",
    "Noise radius": "騒音半径",
    "Rounds": "装弾",
    "Reload time": "リロード時間",
    "Aiming time": "照準時間",
    "Used by": "使用する銃",
    "Reading speed": "読書速度",
    "Reading time left": "残りの読書時間",
    "Skill too low to learn from it": "スキルが低すぎて学べない",
    "Nothing left to learn from it": "これ以上学ぶことはない",
    "Proteins": "タンパク質",
    "Sow in": "種まきの月",
    "Ready in": "収穫まで",
    "Burn time": "燃焼時間",
    # Power: charge, autonomy and light
    "Duration": "持続時間",
    "Light range": "光の範囲",
    "Light strength": "光の強さ",
    "Batteries and radios: charge left, how long it lasts and how far a torch lights": "電池と無線機：残量、持続時間、懐中電灯の光の範囲",
    "Vanilla draws the charge of a drainable as a bar with no number on it, and never says how long a torch lasts or how far it lights. A torch spends its UseDelta once every ten game minutes, and only while it is in a hand or attached to you: left in a bag it switches itself off. Light range and strength are the figures that actually light the ground.":
        "ゲームは消耗品の残量を数字のないバーで描くだけで、懐中電灯が何時間もつのか、どこまで照らすのかは決して教えない。懐中電灯はゲーム内で10分ごとに UseDelta を1回消費し、しかも手に持っているか身に着けている間だけで、バッグに入れると自動的に消える。光の範囲と強さこそが、実際に地面を照らしている数値だ。",
    "Rest quality": "休息の質",
    "Discomfort": "不快",
    "Stomp damage": "踏みつけダメージ",
    "Corpse sickness defense": "死体病への防御",
    "Filter charge": "フィルターの残量",
    "New recipes": "新しいレシピ",
    "Listened": "視聴済み",
    "Skill too high for this tape": "このテープにはスキルが高すぎる",

    # Options screen
    "All Info": "All Info",
    "Enable everything": "すべて有効にする",
    "Items": "アイテム",
    "Crafting": "クラフト",
    "World": "ワールド",
    "Character": "キャラクター",
    "Everything in this section": "このセクションのすべて",
    "Food: time left before it spoils": "食料：傷むまでの残り時間",
    "Adds hours to stale and hours to rotten, at the current rate. Accounts for the fridge, the freezer and the sandbox spoilage speed.":
        "現在の速度で劣化までと腐敗までの時間を表示します。冷蔵庫、冷凍庫、サンドボックスの腐敗速度を考慮します。",
    "Cooking: add the warm-up minutes": "調理：予熱の分数を加算する",
    "Off by default. Cooking time is the time at temperature; this adds the four minutes the food spends heating up before it starts to cook, so an oven timer set to the figure rings when the food is done.":
        "既定ではオフ。調理時間は食材が温まったあとの時間です。オンにすると、調理が始まるまでに食材が温まるのにかかる4分を加算するので、オーブンのタイマーをその数字に合わせればちょうど焼き上がりに鳴ります。",
    "Food: calories, carbs, protein and fat": "食料：カロリー、炭水化物、タンパク質、脂質",
    "Off by default. Showing macros on every food undoes the Nutritionist trait, which is what normally reveals them.":
        "既定ではオフ。すべての食料に栄養値を出すと、本来それを明かす特性「栄養士」の意味がなくなります。",
    "Melee: exact damage, speed and durability": "近接：正確なダメージ、速度、耐久",
    "Puts numbers on the condition and damage bars, and adds crit chance, swing type, attack speed, knockback and the odds of losing a condition point per hit.":
        "耐久とダメージのバーに数値を書き入れ、クリティカル率、振り方、攻撃速度、ノックバック、一撃で耐久が 1 減る確率を追加します。",
    "Firearms: range, jam chance and reload": "銃：射程、ジャム率、リロード",
    "Puts numbers on the condition and damage bars, and adds accuracy, effective range, jam odds and magazine size.":
        "耐久とダメージのバーに数値を書き入れ、命中、有効射程、ジャム率、装弾数を追加します。",
    "Ammo: rounds left and what it fits": "弾薬：残弾と対応する銃",
    "No comparison arrows here: the thing in your hands is a gun, not another magazine, so there is no honest pair to compare.":
        "ここに比較の矢印はありません。手にしているのは銃であって別のマガジンではないので、正直に比べられる相手がいないためです。",
    "Clothing: numbers on every bar, plus discomfort": "衣服：すべてのバーに数値、さらに不快値",
    "Vanilla draws condition, insulation, wind, water, blood, dirt and wetness as bars with no figures. This writes the figures next to them and adds the discomfort value, which vanilla never shows at all.":
        "本編は耐久、断熱、防風、防水、血、汚れ、濡れを数値なしのバーで描きます。ここではその横に数値を書き、本編がどこにも出さない不快値も加えます。",
    "Seeds: growing time and yield": "種：生育時間と収穫",
    "Firewood: how long it burns": "薪：燃える時間",
    "Books: reading time and skill levels covered": "本：読書時間と対応レベル",
    "Reading time already accounts for Fast Reader, Slow Reader and reading glasses.":
        "読書時間には「速読」「遅読」と老眼鏡がすでに反映されています。",
    "Beds: how well you recover on them": "ベッド：どれだけよく休めるか",
    "Masks: filter life and protection": "マスク：フィルター寿命と防御",
    "Tapes and CDs: which skill they teach and how much XP": "テープと CD：どのスキルをどれだけの経験値で教えるか",
    "Show the difference against what you have equipped": "装備中のものとの差を表示する",
    "Adds a coloured +/- next to weapon and clothing values. Weapons compare against what is in your hands, clothing against the piece worn in the same slot.":
        "武器と衣服の数値の横に色付きの +/- を付けます。武器は手に持っているものと、衣服は同じ部位に着ているものと比較します。",
    "Crafting: full item tooltip on the recipe output": "クラフト：レシピの成果物に完全なアイテム情報",
    "Hovering the result of a recipe shows the same block an item in your inventory would, comparison included, before you craft it.":
        "レシピの成果物にカーソルを合わせると、作る前でも所持品と同じ情報ブロックが比較付きで表示されます。",
    "Generators: fuel time, wear and danger": "発電機：燃料、摩耗、危険",
    "Adds noise radius, hours of fuel left, average time until {}%% condition and until it breaks, and the hourly odds of a backfire or a fire.":
        "騒音半径、残り燃料の時間、耐久 {}%% までと故障までの平均時間、1 時間あたりのバックファイアや火災の確率を追加します。",
    "Generators: also show times in real-world minutes": "発電機：現実の分でも時間を表示する",
    "Off by default. Converts the in-game hours using the current day length, so you know how long you actually have to wait.":
        "既定ではオフ。現在の 1 日の長さでゲーム内の時間を換算し、実際にどれだけ待つのかがわかります。",
    "Generators: outline the powered area on the floor": "発電機：給電範囲を床に描く",
    "Draws the edge of the range while the generator window is open, green when running and red when off. Only the floor you are standing on is computed.":
        "発電機のウィンドウが開いている間、範囲の外周を描きます。稼働中は緑、停止中は赤。計算するのは自分が立っている階だけです。",
    "Gas pumps: fuel left and power source": "給油ポンプ：残量と電源",
    "Adds an Info entry to the right-click menu of any gas pump, with the fuel still in the tank and whether the mains or a generator is keeping it running. The game knows that number and only prints it as a debug option.":
        "給油ポンプの右クリックメニューに「情報」を追加し、タンクに残っている燃料と、電力網と発電機のどちらが動かしているかを表示します。ゲームはこの数値を持っていますが、デバッグ項目でしか表示しません。",
    "Fuel Remaining": "残りの燃料",
    "Mains power": "電力網",
    "Generator": "発電機",
    "Walls and doors: health under the cursor": "壁とドア：カーソル下の耐久",
    "Shows current and maximum health as a number at the foot of whatever you point at, no clicking needed.":
        "指したものの足元に現在と最大の耐久を数値で表示します。クリックは不要です。",
    "Build menu: health of what you are about to build": "建築メニュー：これから建てるものの耐久",
    "Also shows what that health would be with the relevant skill at {}, so you can tell whether it is worth waiting.":
        "対応スキルが {} のときの耐久も表示するので、待つ価値があるか判断できます。",
    "Crops: health, growth and water as numbers": "作物：健康、生育、水分を数値で",
    "Adds rows to the crop window you get by right-clicking a plant: health out of {}, current phase, hours to the next one, water level against what the plant needs, time since the last watering and pest levels.":
        "作物を右クリックして開くウィンドウに行を追加します。{} 満点の健康、現在の生育段階、次の段階までの時間、必要量に対する水分、最後の水やりからの時間、各害虫のレベル。",
    "Crops: keep vanilla's Farming level requirements": "作物：本編の農業レベル条件を残す",
    "Off by default, so you see everything from level {}. Turn it on and each row reappears at the Farming level vanilla itself uses for it: phase and health at {}, water at {}, pests at {}, next phase at {}.":
        "既定ではオフなので、レベル {} からすべて見えます。オンにすると各行は本編が使う農業レベルで再び現れます。生育段階と健康は {}、水分は {}、害虫は {}、次の段階は {}。",
    "Noise": "騒音",
    "tiles": "タイル",
    "Down to %1%% (avg)": "%1%% まで（平均）",
    "Breaks down in (avg)": "故障まで（平均）",
    "Backfire, loud (per hour)": "バックファイア、大音量（1 時間あたり）",
    "FIRE OR EXPLOSION (per hour)": "火災または爆発（1 時間あたり）",
    "(real time)": "（現実時間）",
    "XP Boost: %1": "経験値ブースト：%1",
    "Skills": "スキル",
    "Also grants": "さらに付与",
    "Disabled in multiplayer": "マルチプレイでは無効",
    "Foraging": "採集",
    "search radius": "探索半径",
    "weather penalty": "天候ペナルティ",
    "darkness penalty": "暗闇ペナルティ",
    "Strength when built": "建築時の耐久",
    "With %1 at {}": "%1 が {} のとき",
    "Show XP boosts as a multiplier, not a percentage": "経験値ブーストを百分率ではなく倍率で表示する",
    'Vanilla says "{}%%" for a level {} boost. The real figure is x{}, because a skill with no boost runs at a quarter rate. Fixed on all three screens that show it.':
        '本編はレベル {1} のブーストを "{0}%%" と表示します。実際は x{2} です。ブーストのないスキルは 4 分の 1 の速度で伸びるためです。表示される 3 つの画面すべてで修正します。',
    "Character creation: what each trait and job really does": "キャラクター作成：各特性と職業の実際の効果",
    "Adds starting skill levels with their true XP multiplier, free traits granted, recipes taught and foraging bonuses to the tooltips in the creation screen.":
        "作成画面のツールチップに、初期スキルレベルと本当の経験値倍率、無料で付く特性、習得できるレシピ、採集ボーナスを追加します。",
    "In game: the same block on the info tab": "ゲーム中：情報タブに同じブロック",
    "Hover a trait icon or the job icon in the character info tab to read the same block after the world has started.":
        "キャラクター情報タブで特性か職業のアイコンにカーソルを合わせると、ワールド開始後も同じブロックを読めます。",
    "Add hand-written trait effects": "手書きの特性効果を追加する",
    "Effects hardcoded in the game's Java that cannot be read at runtime, so they are written by hand and checked against each build.":
        "ゲームの Java に直接書かれていて実行時には読めない効果です。そのため手作業で書き、各ビルドで照合しています。",
    "Skills: which recipes each level requires": "スキル：各レベルを必要とするレシピ",
    "Hover a level in the skills panel to see the recipes and builds that ask for it. Read from the game's own recipe list, so modded recipes appear too and nothing goes stale with a patch.":
        "スキル画面でレベルにカーソルを合わせると、そのレベルを要求するレシピと建築が表示されます。ゲーム自身のレシピ一覧から読むので、他の MOD のレシピも出ますし、アップデートで古くなることもありません。",
    "Needs this level": "このレベルが必要",
    "Skill and moodle descriptions are translation files. They cannot be switched off here; disable the mod to remove them.":
        "スキルとムードルの説明は翻訳ファイルです。ここでは無効にできません。消すには MOD 自体を無効にしてください。",
    "Run self-test": "セルフテストを実行",

    # Trait and profession effects
    "{}%% footstep noise radius": "足音の半径 {}%%",
    "more likely to fall when bumped": "ぶつかられると転びやすい",
    "less likely to fall when bumped": "ぶつかられても転びにくい",
    "{}%% run and sprint speed": "走行と疾走の速度 {}%%",
    "no Fitness XP from level {} on": "レベル {} 以降は体力の経験値が入らない",
    "double endurance drain when running": "走行時のスタミナ消費が 2 倍",
    "{}%% melee damage": "近接ダメージ {}%%",
    "{} chance to trip from a lunge": "踏み込みでの転倒率 {}",
    "starts at {} weight, and you lose health below {}": "体重 {} で始まり、{} を下回ると体力が減る",
    "{}%% axe swing time": "斧の振り時間 {}%%",
    "{}%% axe damage to trees": "樹木への斧のダメージ {}%%",
    "{}%% endurance lost running": "走行時のスタミナ消費 {}%%",
    "{}%% grapple effectiveness": "組み合いの有効度 {}%%",
    "{}%% knockback": "ノックバック {}%%",
    "can be gained by training Strength to {}": "筋力を {} まで鍛えると得られる",
    "becomes Strong at Strength {}": "筋力 {} で「強靭」になる",
    "becomes Feeble at Strength {}": "筋力 {} で「虚弱」になる",
    "lost by training Strength to {}": "筋力を {} まで鍛えると失われる",
    "{}%% panic, night terrors aside": "パニック {}%%（夜驚を除く）",
    "{}%% stress from looting corpses": "死体を漁るときのストレス {}%%",
    "{}%% panic": "パニック {}%%",
    "no panic from a corpse reanimating": "死体が起き上がってもパニックにならない",
    "no stress from looting corpses": "死体を漁ってもストレスにならない",
    "{} move speed at panic {}": "パニック {1} で移動速度 {0}",
    "still capped by the movement speed limit": "それでも移動速度の上限は超えられない",
    "{}%% wind penalty when aiming": "照準時の風ペナルティ {}%%",
    "{}%% gun accuracy": "銃の命中 {}%%",
    "{}%% gun crit chance": "銃のクリティカル率 {}%%",
    "shorter aiming delay": "照準の遅延が短くなる",
    "wider field of view": "視野が広がる",
    "{}%% max range on weapon sights": "照準器の最大射程 {}%%",
    "blurry vision": "視界がぼやける",
    "weapon sight range bonus at its minimum": "照準器の射程ボーナスが最小になる",
    "cancelled by wearing glasses": "眼鏡をかければ打ち消せる",
    "{}%% perception radius": "知覚半径 {}%%",
    "zombies behind you become visible sooner": "背後のゾンビが早く見えるようになる",
    "muffled sound effects": "音がこもる",
    "zombies behind you become visible later": "背後のゾンビが見えるのが遅くなる",
    "no sound at all": "音がまったく聞こえない",
    "you can still watch TV": "テレビは見られる",
    "{}%% chance of not being injured by a zombie": "ゾンビに傷つけられない確率 {}%%",
    "{}%% chance of being scratched by trees": "木で擦り傷を負う確率 {}%%",
    "{}%% corpse sickness": "死体病 {}%%",
    "{}%% chance of catching a cold": "風邪をひく確率 {}%%",
    "{}%% cold strength": "風邪の強さ {}%%",
    "{}%% cold progression": "風邪の進行 {}%%",
    "{}%% zombification speed": "ゾンビ化の速度 {}%%",
    "{}%% severity of vehicle injuries": "車両による負傷の重さ {}%%",
    "{}%% fracture severity": "骨折の重さ {}%%",
    "all wounds heal much faster": "あらゆる傷がずっと早く治る",
    "all wounds heal much slower": "あらゆる傷がずっと遅く治る",
    "{}%% XP in every skill except Fitness and Strength": "体力と筋力を除く全スキルの経験値 {}%%",
    "{}%% reading speed": "読書速度 {}%%",
    "{}%% XP in every weapon skill and Aiming": "全武器スキルと射撃の経験値 {}%%",
    "{}%% inventory transfer time": "アイテムの移動時間 {}%%",
    "{}%% aiming delay": "照準の遅延 {}%%",
    "guns jam less often": "銃がジャムしにくくなる",
    "fewer injuries opening cans": "缶を開けるときの怪我が減る",
    "guns jam more often": "銃がジャムしやすくなる",
    "more injuries opening cans": "缶を開けるときの怪我が増える",
    "{}%% container capacity": "コンテナの容量 {}%%",
    "crafting does not return leftover items": "クラフトで余った材料が戻らない",
    "{}%% thirst": "喉の渇き {}%%",
    "{}%% hunger": "空腹 {}%%",
    "{}%% food illness chance": "食中毒になる確率 {}%%",
    "{}%% food illness duration": "食中毒の持続時間 {}%%",
    "{}%% harm from tainted water": "汚れた水による害 {}%%",
    "{}%% tiredness gained while awake": "起きている間にたまる疲労 {}%%",
    "{}%% recovery while asleep": "睡眠中の回復 {}%%",
    "{}%% sleep duration": "睡眠時間 {}%%",
    "you do not wake up at {} tiredness, so set an alarm": "疲労 {} でも目が覚めないので、目覚ましをかけること",
    "harder to fall asleep": "寝つきが悪くなる",
    "{}%% vision in the dark": "暗闇での視界 {}%%",
    "smaller vision cone penalty at night": "夜間の視界角ペナルティが小さい",
    "{}%% chance of being spotted (new stealth)": "発見される確率 {}%%（新ステルス）",
    "{}%% chance of being spotted (old stealth)": "発見される確率 {}%%（旧ステルス）",
    "{}%% chance of breaking kindling": "焚きつけを折る確率 {}%%",
    "{}%% weather penalty when aiming": "照準時の天候ペナルティ {}%%",
    "lights fires twice as fast": "火起こしが 2 倍速い",
    "almost never scratched by trees": "木でほとんど傷つかない",
    "{}%% endurance lost running, sprinting, carrying and dragging":
        "走行、疾走、運搬、牽引でのスタミナ消費 {}%%",
    "{}%% endurance lost swinging a weapon": "武器を振るときのスタミナ消費 {}%%",
    "{}%% gear change speed": "ギアチェンジの速度 {}%%",
    "{}%% top speed": "最高速度 {}%%",
    "{}%% engine noise in reverse": "後退時のエンジン音 {}%%",
    "{}%% acceleration": "加速 {}%%",
    "{}%% reverse acceleration": "後退時の加速 {}%%",
    "capped at {} max speed": "最高速度が {} に制限される",
    "engine noise unchanged": "エンジン音は変わらない",
    "less likely to fail any fence climb": "どの柵でも乗り越えに失敗しにくい",
    "slightly faster rope climbing": "ロープの上り下りが少し速い",
    "bloody items transfer faster but cause stress": "血まみれの物は速く運べるがストレスになる",
    "cannot read anything, map labels and calorie counts included":
        "地図のラベルもカロリー表示も含め、何も読めない",
    "{} panic per tick indoors, scaling down to {} in a {}-tile room":
        "屋内では 1 ティックあたりパニック {0}。{2} タイルの部屋では {1} まで下がる",
    "a vehicle counts as a {}-tile room": "車両は {} タイルの部屋として扱われる",
    "{} panic per tick whenever you are not in a room": "部屋の外にいる間、1 ティックあたりパニック {}",
    "faster building": "建築が速い",
    "faster barricading": "バリケード作業が速い",
    "no bonus health on constructions in B{}": "B{} では建築物の耐久が上乗せされない",
    "recipes need one level less of their skill": "レシピが要求するスキルレベルが 1 下がる",
    "you gain weight above {} calories a day instead of {}, while under {} weight":
        "体重が {2} を下回っている間、1 日 {1} ではなく {0} キロカロリーを超えると太る",
    "you need {} calories a day to gain weight instead of {}, while over {} weight":
        "体重が {2} を上回っている間、太るのに 1 日 {1} ではなく {0} キロカロリー必要になる",
    "unhappiness and stress rise as nicotine withdrawal builds":
        "ニコチン切れが進むにつれて不幸とストレスが上がる",
    "smoking clears the withdrawal and gives {} hunger": "喫煙でニコチン切れが解消し、空腹が {} される",
    "random coughs and sneezes give you away": "不意の咳やくしゃみで居場所がばれる",
    "shows calories, carbohydrates, protein and fat on every food":
        "あらゆる食料のカロリー、炭水化物、タンパク質、脂質を表示する",
    "no measurable effect in B{}: no XP boost, no recipes, and nothing in the game's code reads it. The recipes come from the profession itself.":
        "B{} では測定できる効果がありません。経験値ブーストもレシピもなく、ゲームのコードのどこからも参照されていません。レシピは職業そのものが与えます。",
    "x{} move speed through trees (x{} for everyone else)": "樹木の間の移動速度 x{}（他の全員は x{}）",
    "starts every exercise at {}{} regularity instead of {}{}":
        "各運動の規則性が {}{} から始まる（通常は {}{}）",
    '{} move speed':
        '移動速度 {}',
    '{} wind penalty when aiming':
        '照準時の風ペナルティ {}',
    '%1 °C':
        '%1 °C',
    'Adds rows to the inventory tooltip: how fast a line wears out, how much each hook helps and which fish a bait attracts.':
        '持ち物のツールチップに行を追加します。道糸の消耗の速さ、釣り針ごとの効果、そして餌がどの魚を寄せるか。',
    'ALLTHEINFO':
        'ALLTHEINFO',
    'Attracts':
        '寄せる魚',
    "Back to vanilla's rules: Time needs Fishing {}, Temperature {}, Weather {}, Wind {}, and a species tells you nothing until you have caught it.":
        'バニラの規則に戻します。時間は釣り{}、気温は{}、天候は{}、風は{}が必要で、釣ったことのない魚種は何も表示されません。',
    'Best baits: %1':
        '最適な餌: %1',
    'Bite chance':
        'アタリ率',
    'Breaks into':
        '壊れると',
    'Chance that one attempt hooks something: {}%% times temperature, weather, time, hook and abundance, capped at {}%%.':
        '1回の試行で何かが掛かる確率: {}%% × 気温 × 天候 × 時間 × 釣り針 × 魚の多さ、上限は{}%%。',
    'Fish bite more at dawn and dusk: x{} from {}:{} to {}:{} and from {}:{} to {}:{}. Any other hour is x{}.':
        '魚は夕方と早朝によく釣れます: {}:{}から{}:{}と{}:{}から{}:{}は×{}。それ以外の時間は×{}。',
    'Fishing gear: rods, lines, hooks and baits':
        '釣具: 竿、道糸、釣り針、餌',
    'Fishing panel: what each rating is worth':
        '釣りパネル: 各評価の実際の値',
    "Fishing: keep vanilla's Fishing level requirements":
        '釣り: バニラの釣りレベル制限を維持',
    'Hook':
        '釣り針',
    'How much longer than the best possible case you wait between attempts. Fishing near the shore doubles it, and a bobber less than {} tiles away triples it.':
        '最良の場合と比べて、アタリの間隔がどれだけ長いか。岸辺での釣りは2倍、ウキが{}タイル未満の距離なら3倍になります。',
    'Lake':
        '湖',
    'Line strength':
        '道糸の強さ',
    'Moodles: description box that fits its text':
        'ムードル: 文量に合う説明枠',
    'Needs Fishing %1':
        '釣り%1が必要',
    'Only bites while you reel in':
        'リールを巻いている間だけ掛かる',
    'Paperclip x{}, nail x{}, fishing hook x{}. With no hook the chance is x{}: nothing will ever bite.':
        'クリップ×{}、釘×{}、釣り針×{}。針がなければ確率は×{}で、何も掛かりません。',
    'Rain is x{}. Fog over {} or wind over {} is x{}. Fog and wind are the same x{}: they never stack.':
        '雨は×{}。{}を超える霧、または{}を超える風は×{}。霧と風は同じ×{}で、重なることはありません。',
    'Right-click water and pick Fishing. Puts the real multiplier next to Time, Temperature, Weather and Wind, adds hook, spot, bite chance and waiting time, and explains each one on hover.':
        '水面を右クリックして釣りを選びます。時間・気温・天候・風の隣に実際の倍率を表示し、釣り針、場所、アタリ率、待ち時間を加え、カーソルを合わせるとそれぞれを説明します。',
    'River':
        '川',
    'Spot':
        '場所',
    "The game's own moodle box is two lines tall and cuts off anything longer, which is most of AllTheInfo's descriptions. This draws the moodle column itself so the box grows with the text. Turn it off to go back to the vanilla widget.":
        'ゲームのムードル枠は2行分しかなく、それより長い文は切り捨てられます。AllTheInfoの説明はほぼそうです。ここではムードル列を自前で描画するので、枠が文量に合わせて伸びます。オフにすればバニラの表示に戻ります。',
    'Trophy from %1 cm, Fishing {} and a {} in {} roll on a big catch':
        '%1cmからトロフィー。釣り{}で、大物を掛けたときに{}分の{}の抽選。',
    'Under {} fish is x{}, up to {} is x{}, over {} is x{}. Trash is what you pull out instead of a fish, and Fishing {} cuts it to {}%%, level {} to {}%% and level {} to {}%%.':
        '魚が{}未満なら×{}、{}までなら×{}、{}を超えるなら×{}。ゴミは魚の代わりに釣れるもので、釣り{}で{}%%、レベル{}で{}%%、レベル{}で{}%%まで下がります。',
    'Up to %1 cm and %2 kg':
        '最大%1cm、%2kg',
    'Vanilla draws condition, insulation, wind, water, blood, dirt and wetness as bars with no figures. This writes the figures next to them and adds the discomfort value, which vanilla never shows at all. The run and combat speed modifiers get a signed figure too, which vanilla only ever draws as a bar with no sign.':
        'バニラは耐久度、断熱、防風、防水、血、汚れ、濡れを数値なしのバーで描きます。ここではその隣に数値を書き、バニラが一切見せない不快度も追加します。走行速度と戦闘速度の修正値も符号付きの数値になります。バニラは符号のないバーしか描きません。',
    'Wait':
        '待ち時間',
    'Waters: %1':
        '水域: %1',
    'Wear per tug':
        '1回の引きあたりの消耗',
    'Wind has no coefficient of its own. Over {} it sets the weather to x{}, the same penalty fog sets, and the two do not add up.':
        '風に固有の係数はありません。{}を超えると天候を×{}にします。霧と同じペナルティで、両方が重なることはありません。',
    'With your bait: %1%%':
        'この餌で: %1%%',
    'Your bait does not attract this one':
        'この餌ではこの魚種は寄ってこない',
    'best possible':
        '最良',
    'near shore':
        '岸辺',
    'no fish in this spot':
        'ここに魚はいない',
    'none':
        'なし',
    'trash':
        'ゴミ',
    '{} to {} °C is x{}. From {} to {} and from {} to {}, x{}. Over {} or below {}, x{}. Below {} °C, x{}.':
        '{}～{} °Cは×{}。{}～{}と{}～{}は×{}。{}以上または{}未満は×{}。{} °C未満は×{}。',
    'Fish':
        '魚影',
    'Trash':
        'ゴミ',
    'Trophy from %1 cm':
        '%1cmからトロフィー',
    'shore':
        '岸辺',
    'Best baits:':
        '最適な餌:',
    'Size: %1-%2 cm, %3-%4 kg':
        'サイズ: %1-%2 cm、%3-%4 kg',
    'Trophy: >%1 cm / >%2 kg':
        'トロフィー: >%1 cm / >%2 kg',
    'Under {} fish is x{}, up to {} is x{}, over {} is x{}. Fish schools move every day. Trash is what you pull out instead of a fish: it is fixed per spot, and Fishing {} cuts it to {}%%, level {} to {}%% and level {} to {}%%.':
        '魚が{}未満なら×{}、{}までなら×{}、{}を超えるなら×{}。魚群は毎日移動します。ゴミは魚の代わりに釣れるもので、場所ごとに固定です。釣り{}で{}%%、レベル{}で{}%%、レベル{}で{}%%まで下がります。',
    'Fishing gear: hide the combat stats':
        '釣具: 戦闘ステータスを隠す',
    "Fog over {}%% sets the weather to x{}, the same penalty wind sets, and the two never stack. Vanilla's Weather row reports neither: it says Good for rain even in a gale.":
        '霧が{}%%を超えると天候が×{}になります。風と同じペナルティで、両方が重なることはありません。ゲームの天候欄はどちらも反映せず、強風でも雨なら「良い」と表示します。',
    'Rain is x{}. Fog over {}%% or wind over {}%% is x{}. Fog and wind are the same x{}: they never stack.':
        '雨は×{}。{}%%を超える霧、または{}%%を超える風は×{}。霧と風は同じ×{}で、重なることはありません。',
    "Rods, nets and fishing spears are weapons in the game's own scripts, so they get crit chance, swing type, attack speed and knockback. This drops that block on fishing gear. The condition and damage bars are drawn by the game in one call and cannot be removed by any mod.":
        '竿、網、ヤスはゲームのスクリプト上は武器なので、クリティカル率、振りの種類、攻撃速度、ノックバックが表示されます。この設定は釣具のその部分を消します。耐久度と与ダメージのバーはゲームが一度の呼び出しで描くため、どのMODでも消せません。',
    'Wind has no coefficient of its own. Over {}%% it sets the weather to x{}, the same penalty fog sets, and the two do not add up.':
        '風に固有の係数はありません。{}%%を超えると天候を×{}にします。霧と同じペナルティで、両方が重なることはありません。',
    'Against the best possible case':
        '最良の場合と比べて',
    'Any other hour: x{}':
        'それ以外の時間: ×{}',
    'Below {} °C: x{}':
        '{} °C未満: ×{}',
    'Bobber under {} tiles away: x{}':
        'ウキが{}タイル未満: ×{}',
    'Capped at {}%%':
        '上限{}%%',
    'Fishing hook: x{}':
        '釣り針: ×{}',
    'Fishing {}, {} and {} cut trash to {}%%, {}%% and {}%%':
        '釣り{}、{}、{}でゴミが{}%%、{}%%、{}%%に下がる',
    'Fog and wind never stack':
        '霧と風は重ならない',
    'Fog over {}%% or wind over {}%%: x{}':
        '{}%%を超える霧、または{}%%を超える風: ×{}',
    'Nail: x{}':
        '釘: ×{}',
    'Near shore: x{}':
        '岸辺: ×{}',
    'No hook: x{}, nothing ever bites':
        '針なし: ×{}、何も掛からない',
    'Over {} or below {} °C: x{}':
        '{}を超える、または{} °C未満: ×{}',
    'Over {}%%: x{} on the weather':
        '{}%%超: 天候に×{}',
    'Over {}: x{}':
        '{}超: ×{}',
    'Paperclip: x{}':
        'クリップ: ×{}',
    'Rain: x{}':
        '雨: ×{}',
    'Rolled once per attempt':
        '1回の試行ごとに抽選',
    'Same penalty as fog, they never stack':
        '霧と同じペナルティで、重なることはない',
    'Same penalty as wind, they never stack':
        '風と同じペナルティで、重なることはない',
    'Schools move every day':
        '魚群は毎日移動する',
    'This row reports neither':
        'この行はどちらも反映しない',
    'Trash is fixed per spot':
        'ゴミは場所ごとに固定',
    'Under {} fish: x{}':
        '魚が{}未満: ×{}',
    '{} to {} and {} to {} °C: x{}':
        '{}～{}および{}～{} °C: ×{}',
    '{} to {} °C: x{}':
        '{}～{} °C: ×{}',
    '{} to {}: x{}':
        '{}～{}: ×{}',
    '{}%% x temperature x weather x time x hook x fish':
        '{}%% × 気温 × 天候 × 時間 × 釣り針 × 魚の多さ',
    '{}:{} to {}:{} and {}:{} to {}:{}: x{}':
        '{}:{}～{}:{}および{}:{}～{}:{}: ×{}',
    'Fishing {}, {} and {}: trash x{}, x{}, x{}':
        '釣り{}、{}、{}: ゴミ ×{}、×{}、×{}',
    'x time x hook x fish':
        '× 時間 × 釣り針 × 魚の多さ',
    '{}%% x temperature x weather':
        '{}%% × 気温 × 天候',

    # Round 11: moodles rewritten from bytecode + wiki
    "melee damage {}%%": "近接ダメージ {}%%",
    "melee damage {}": "近接ダメージ {}",
    "move speed {}%%": "移動速度 {}%%",
    "move speed {}%% with Adrenaline Junkie": "アドレナリン中毒時の移動速度 {}%%",
    "attack speed {}%%": "攻撃速度 {}%%",
    "combat speed {}%%": "戦闘速度 {}%%",
    "run speed {}%%": "走行速度 {}%%",
    "crit chance {}%%": "クリティカル率 {}%%",
    "firearm accuracy {}%%": "銃の命中率 {}%%",
    "firearm accuracy {}%% at {} tiles": "{1} マスで銃の命中率 {0}%%",
    "clearing a jam {}%%": "ジャム解除の成功率 {}%%",
    "climbing {}%%": "よじ登り {}%%",
    "climbing fences {}%%": "柵越え {}%%",
    "climbing walls and ropes {}%%": "壁とロープの登攀 {}%%",
    "tripping over fences {}%%": "柵でつまずく確率 {}%%",
    "blocking an attack {}%%": "攻撃の受け {}%%",
    "foraging {}%%": "採集 {}%%",
    "carry capacity {}": "所持重量 {}",
    "healing {}%%": "回復速度 {}%%",
    "healing x{}": "回復速度 x{}",
    "poison wears off {}%% faster": "毒の抜けが {}%% 速い",
    "heat dissipation {}%%": "放熱 {}%%",
    "heat loss {}%%": "熱損失 {}%%",
    "discomfort {}%%": "不快感 {}%%",
    "medicine {}%% less effective": "薬の効果が {}%% 低下",
    "sleep {}{}%% less effective": "睡眠の効果が {0}{1}%% 低下",
    "panic x{} per wound": "傷1つにつきパニック x{}",
    "over {}%% of capacity": "所持重量の {}%% 超過",
    "health under {}%%": "体力 {}%% 未満",
    "health {}%% per hour": "1時間あたり体力 {}%%",
    "health drops to {}%%": "体力が {}%% まで低下",
    "health drops to {}%%, then to {}%%": "体力が {0}%% まで、その後 {1}%% まで低下",
    "health drops to {}%% when the air is above {} C": "気温が {1} C を超えると体力が {0}%% まで低下",
    "health drops when the air is below {} C": "気温が {} C を下回ると体力が低下",
    "only heals indoors, dry, under {}%% fatigue and under {}%% hunger and thirst": "屋内で乾いた状態、疲労 {}%% 未満、空腹と渇き {}%% 未満のときだけ回復",
    "vision cone narrows, cancelling Eagle Eyed": "視野角が狭くなり、鷹の目を打ち消す",
    "{} C colder than the air": "気温より {} C 低く感じる",
    "{} wounds bleeding": "{} 箇所が出血",
    "{} wounds, or a bleeding neck": "{} 箇所、または首の出血",
    "no healing": "回復しない",
    "no natural healing": "自然回復しない",
    "slower healing": "回復が遅い",
    "much slower healing": "回復がかなり遅い",
    "slower endurance recovery": "スタミナ回復が遅い",
    "much slower endurance recovery": "スタミナ回復がかなり遅い",
    "endurance barely recovers": "スタミナがほとんど回復しない",
    "endurance drains as you move and never recovers": "移動でスタミナが減り回復しない",
    "no sprinting or running": "全力疾走も走行も不可",
    "you cannot run": "走れない",
    "you cannot sleep": "眠れない",
    "you cannot eat any more": "もう食べられない",
    "you can sleep on the ground and through pain": "地面でも痛みがあっても眠れる",
    "cannot swing a sledgehammer": "大ハンマーを振れない",
    "hunger does not rise": "空腹が進まない",
    "less body heat generated": "体熱の産生が減る",
    "body heat rises": "体温が上がる",
    "body heat rises sharply": "体温が大きく上がる",
    "thirst and fatigue rise faster": "喉の渇きと疲労が早く進む",
    "you lose heat in the cold": "寒さで体温を失う",
    "more likely to catch a cold": "風邪をひきやすくなる",
    "more likely to fall ill": "病気になりやすくなる",
    "much more likely to fall ill": "病気になる危険が大きい",
    "narrower vision cone": "視野角が狭まる",
    "narrower vision and awareness": "視野と警戒が落ちる",
    "movement, damage and attack speed drop with the wound": "傷の場所に応じて移動・ダメージ・攻撃速度が落ちる",
    "you make noise": "音を立てる",
    "you complain out loud": "声に出して不平を言う",
    "you get up faster": "早く立ち上がれる",
    "you weave as you walk": "歩くとふらつく",
    "timed actions take longer": "作業に時間がかかる",
    "unhappiness rises": "不幸が上がる",
    "unhappiness rises slowly": "不幸がゆっくり上がる",
    "unhappiness rises fast": "不幸が速く上がる",
    "stress rises": "ストレスが上がる",
    "boredom is wiped and held down": "退屈が消え、上がらなくなる",
    "the Desensitized trait cancels it": "「無感覚」特性で打ち消される",
    "no effect until NPCs return": "NPC が戻るまで効果なし",
    "discomfort while in a vehicle": "車内では不快感が溜まる",
    "hypothermia is hidden": "低体温症が隠れる",
    "it wakes you up": "目が覚めてしまう",
    "you sneeze now and then": "ときどきくしゃみが出る",
    "you sneeze and cough often": "くしゃみと咳が頻繁に出る",
    "you cough so much that hiding gets hard": "咳がひどく隠れにくい",
    "you cough constantly and draw zombies": "咳が止まらずゾンビを引き寄せる",
    "health loss": "体力の低下",
    "slow health loss": "体力がゆっくり減る",
    "serious health loss": "体力が大きく減る",
    "health slowly drops": "体力がじわじわ減る",
    "health drops if this is infection or poison": "感染か毒なら体力が減る",
    "death without first aid": "手当てをしないと死ぬ",
    "sickness starts to build": "病気が溜まり始める",
    "sickness builds noticeably": "病気がはっきり溜まる",
    "many rotting corpses": "腐乱死体が多い",
    "more rotting corpses": "腐乱死体が増えた",
    "the worst corpses can do": "死体で到達する最大値",
    "a generator running indoors": "屋内で稼働中の発電機",
    "it will not kill you outright": "直接死ぬことはない",
    "a gas mask or SCBA prevents it": "ガスマスクか空気呼吸器で防げる",
    "caused by heavy clothing, bags, bare feet or leg injuries": "重い衣類・バッグ・裸足・脚の負傷が原因",

    # Animals (round 10, block C)
    "Animals: butchering yield, milk, wool and old age":
        "動物：肉の取れ高、ミルク、羊毛、老い",
    "Adds rows to the animal window you get by right-clicking an animal: meat yield, blood, feathers, old age and weight ceiling, which no screen shows, plus health, hunger, thirst, attitude, milk, wool and pregnancy as numbers instead of words.":
        "動物を右クリックして開く画面に行を追加：どの画面にも出ない肉の取れ高・血・羽根・老い・体重の上限に加え、健康・空腹・喉の渇き・態度・ミルク・羊毛・妊娠を言葉ではなく数字で表示。",
    "Animals: keep vanilla's Animal Care level requirements":
        "動物：バニラの動物福祉レベル条件を残す",
    "Off by default, so you see everything from level {}. Turn it on and each row reappears at the Animal Care level vanilla itself uses for it: pregnancy at {}, weight at {}, attitude at {}.":
        "既定ではオフなので、レベル {} からすべて見える。オンにすると、各行はゲーム自身が使う動物福祉レベルに戻る：妊娠 {}、体重 {}、態度 {}。",
    "Meat yield":
        "肉の取れ高",
    "full in %1":
        "%1 で満タン",

    # Animal hover descriptions (round 12)
    "Size x meat gene.":
        "サイズ x 肉の遺伝子。",
    "Multiplies the number of meat pieces and the calories of each one.":
        "肉の個数と 1 個あたりのカロリーの両方に掛かる。",
    "Butchering adds x{} every {} levels.":
        "解体は {} レベルごとに x{} 加算。",
    "Off the ground x{}, on a butcher hook x{}.":
        "地面では x{}、精肉フックでは x{}。",
    "Litres you can drain into a bucket once it is dead.":
        "死んだあとバケツに取れるリットル数。",
    "Grows with weight.":
        "体重とともに増える。",
    "Feathers you get for butchering it.":
        "解体で手に入る羽根。",
    "Breed maximum x size.":
        "品種の上限 x サイズ。",
    "{}%% until {}%% of its life expectancy, then it climbs to {}%%.":
        "寿命の {}%% までは {}%%、その後 {}%% まで上がる。",
    "Over {}%% it loses {}%% health every hour.":
        "{}%% を超えると毎時 {}%% の体力を失う。",
    "Current weight and the most this animal can reach.":
        "現在の体重と、この動物が届く上限。",
    "Meat and blood both scale with it.":
        "肉も血もこの値に比例する。",
    "Over {}%% hunger it starts losing weight.":
        "空腹が {}%% を超えると体重が減りはじめる。",
    "{}{}, how much this animal puts up with you.":
        "{}{}。この動物がどれだけ我慢してくれるか。",
    "Each point takes {} off the chance it breaks free while being sheared.":
        "1 ポイントごとに、毛刈り中に暴れる確率が {} 下がる。",
    "Every gain is {}, plus {} per Animal Care level.":
        "上昇は 1 回 {}、動物福祉レベルごとに {} 追加。",
    "Healthy over {}%%, off colour over {}%%, sickly over {}%%, dying below.":
        "{}%% 超で健康、{}%% 超で不調、{}%% 超で病弱、それ未満は死にかけ。",
    "Higher is worse.":
        "高いほど悪い。",
    "Well fed under {}%%, underfed under {}%%, starving over it.":
        "{}%% 未満で満腹、{}%% 未満で栄養不足、それ以上は飢餓。",
    "Over {}%% it starts losing weight.":
        "{}%% を超えると体重が減りはじめる。",
    "Fully watered under {}%%, thirsty under {}%%, dying of thirst over it.":
        "{}%% 未満で水分充分、{}%% 未満で渇き、それ以上は渇きで死にかけ。",
    "{}{}. Calm under {}, unnerved under {}, agitated under {}, wild over it.":
        "{}{}。{} 未満で穏やか、{} 未満で不安、{} 未満で興奮、それ以上は荒れている。",
    "Over {} milk and wool grow at {} / stress of their rate.":
        "{} を超えると、ミルクと羊毛の増加量が本来の {} / ストレス になる。",
    "Over {} a pregnancy can be lost.":
        "{} を超えると妊娠が失われることがある。",
    "Milking with stress over {} and Animal Care {} or less always fails and spills the bucket.":
        "ストレス {} 超かつ動物福祉 {} 以下での搾乳は必ず失敗し、バケツをこぼす。",
    "Litres in the udder and what it holds.":
        "乳房のリットル数と容量。",
    "It fills by capacity / {} per game hour, times the sandbox milk modifier.":
        "ゲーム内 1 時間ごとに 容量 / {} ずつ溜まり、サンドボックスのミルク補正が掛かる。",
    "Stress over {} slows it down.":
        "ストレス {} 超で遅くなる。",
    "Wool grown and the maximum.":
        "伸びた羊毛と上限。",
    "It grows by maximum / {} per game hour: {} days for a full fleece.":
        "ゲーム内 1 時間ごとに 上限 / {} 伸びる。フリース 1 枚分で {} 日。",
    "Days left before it gives birth.":
        "出産まであと何日か。",
    "Stress over {} can end the pregnancy.":
        "ストレス {} 超で妊娠が終わることがある。",
    "Hours this female stays fertilised.":
        "このメスが受精状態を保つ時間。",
    "When it runs out she is no longer fertilised.":
        "尽きると受精状態ではなくなる。",

    # Wounds and healing
    "Wounds: how long each one still needs":
        "傷：それぞれあとどれくらいかかるか",
    "Adds an Info entry under the treatments you get by clicking a body part in the health panel. Hover it and the box beside it gives the time left on every wound, what bandaging or a poultice would save, how long the bandage lasts and whether the part is mending or getting worse. The game knows all of it and only prints it in debug mode.":
        "健康画面で体の部位をクリックすると出る処置の下に「情報」の項目を追加。カーソルを合わせると、隣の枠に各傷の残り時間、包帯や湿布でどれだけ短縮できるか、包帯がどれだけ持つか、その部位が治りつつあるか悪化しているかが出る。ゲームはすべて把握していて、デバッグモードでしか表示しない。",
    "Wounds: keep vanilla's Doctor level requirements":
        "傷：バニラの応急医療レベル条件を残す",
    "Off by default, so you see everything from level {}. Turn it on and each row reappears at the Doctor level vanilla itself uses for it: scratches and lacerations at {}, deep wounds and splints at {}, fractures and stitches at {}, wound infection at {}.":
        "既定ではオフなので、レベル {} からすべて見える。オンにすると、各行はゲーム自身が使う応急医療レベルに戻る：引っかき傷と裂傷 {}、深い傷と添え木 {}、骨折と縫合 {}、傷の感染 {}。",
    "Full recovery":
        "完全回復",
    "Getting worse":
        "悪化中",
    "Healing":
        "治癒",
    "normal":
        "通常",
    "slowed by hunger, thirst or illness":
        "空腹・喉の渇き・病気で遅い",
    "stopped by hunger or thirst":
        "空腹か喉の渇きで停止",
    "asleep, ten times faster":
        "睡眠中、10倍速",
    "wounded parts share it":
        "か所の負傷部位で分け合う",
    "Bandage life":
        "包帯の持ち",
    "ready to remove":
        "抜糸できる",

    # Wounds and healing, redesigned tooltip
    "Healing speed":
        "治癒速度",
    "clean for":
        "清潔なまま",
    "Poultice":
        "湿布",
    "Wound infection":
        "傷の感染",
    "won't close, glass inside":
        "ガラスが残っていて塞がらない",
    "won't close while unbandaged":
        "包帯なしでは塞がらない",
    "rising":
        "悪化中",

    # Wounds: shorter recovery label and infection risk
    "Recovery":
        "回復",
    "Infection risk":
        "感染リスク",

    # Percentages, ported from the multiplier wording
    "{}%% weapon damage": "武器ダメージ {}%%",
    "{}%% endurance recovery": "スタミナ回復 {}%%",
    "{}%% melee damage and knockback": "近接ダメージとノックバック {}%%",
    "{}%% move speed in combat stance": "戦闘姿勢での移動速度 {}%%",
    "{}%% sprint speed": "疾走速度 {}%%",
    "{}%% chance of being spotted": "発見される確率 {}%%",
    "{}%% footstep noise": "足音の大きさ {}%%",
    "{}%% recoil delay": "反動による遅延 {}%%",
    "{}%% aim settling speed": "照準が安定する速さ {}%%",
    "{}%% aim penalty for moving (shared with Nimble)": "移動中の照準ペナルティ {}%%（機敏と共通）",
    "{}%% reload speed": "リロード速度 {}%%",
    "{}%% racking speed": "装填動作の速度 {}%%",
    "{}%% XP in every Crafting skill": "全クラフトスキルの経験値 {}%%",
    "{}%% move speed through trees": "樹木の間の移動速度 {}%%",
    "spotting another player {}%%": "他プレイヤーの発見 {}%%",
    "timed actions {}%%": "作業時間 {}%%",
    "endurance drain {}%%": "スタミナ消費 {}%%",
    "alcohol hits {}%%, and {}%% over {}%% hunger": "酔いが {0}%%、空腹 {2}%% 超で {1}%%",
    "Fitness {}, which is {}%% endurance recovery instead of {}%%":
        "体力 {0}、つまりスタミナ回復が {2}%% ではなく {1}%%",
    "{}%% attack speed": "攻撃速度 {}%%",
    "{}%% crit chance": "クリティカル率 {}%%",
    "racking costs {}%% of the aiming time": "装填動作で照準時間の {}%% を消費",
    "carrying capacity {}": "所持重量 {}",
    "{} to every weapon's durability roll.": "すべての武器の耐久判定に {}。",
    "Condition loss (handle)": "耐久の減少率 (柄)",
    "Condition loss (head)": "耐久の減少率 (頭)",

    # Ronda 4: medicine, traps, weapon components, skill levels
    '%1 corpses nearby': '近くに死体 %1 体',
    '%1%% attack time': '攻撃速度 %1%%',
    '%1%% crit chance': 'クリティカル率 %1%%',
    '%1%% muscle strain': '筋肉疲労 %1%%',
    '%1%% weapon damage': '武器ダメージ %1%%',
    '+%1 to the durability roll': '耐久判定 +%1',
    'Adds an Info entry to a placed trap: the odds of it catching anything in an hour, which animals it can take and the share of the catch each one gets, the bait and its freshness, the zone, the hourly odds of losing bait or trap, and the warning that a trap catches nothing while you stand next to it. Bait foods get a row naming what they attract.': '設置したトラップに情報の項目を追加します。1時間あたりに何かを捕まえる確率、捕まえられる動物とそれぞれの捕獲割合、餌とその鮮度、ゾーン、餌やトラップを失う1時間あたりの確率、そしてそばに立っている間はトラップが何も捕まえないという警告です。餌になる食料には、何を引き寄せるかを示す行が付きます。',
    'Bait': '餌',
    'Bait lost per hour': '1時間あたりの餌の損失',
    'In the trap for': '捕獲からの経過',
    'Filter left': 'フィルター残量',
    'Hits before it breaks': '壊れるまでの打撃回数',
    'Medicine: duration, delay and effect': '薬品: 持続時間、効果が出るまで、効果',
    'Medicine: the full list of effects': '薬品: 効果の全一覧',
    'Muscle strain per hit': '1撃あたりの筋肉疲労',
    'Off by default, so you see everything from level {}. Turn it on and the trap tooltip only appears from Trapping {}, which is the level vanilla itself uses elsewhere.': '既定ではオフなので、レベル {} からすべて見えます。オンにすると、トラップのツールチップはトラップ {} からのみ表示されます。ゲーム自身が他の場所で使っているレベルです。',
    'Off by default. Adds everything else each pill does: what cancels it, what intoxication costs it, and the sleeping tablet overdose table.': '既定ではオフ。各錠剤のその他の作用をすべて追加します。何が効果を打ち消すか、酩酊でどれだけ弱まるか、睡眠薬の過剰摂取表です。',
    'Painkillers, beta blockers, antidepressants, sleeping tablets and antibiotics get how long they last, how long they take to start and what they do per minute. Every figure is recomputed from the sandbox day length.': '鎮痛剤、ベータ遮断薬、抗うつ薬、睡眠薬、抗生物質に、持続時間、効果が出るまでの時間、1分あたりの作用が付きます。どの数値もサンドボックスの1日の長さから計算し直されます。',
    'Prey': '獲物',
    'Rots once thawed': '解凍後に腐る',
    'Stale once thawed': '解凍後に古くなる',
    'Takes effect in': '効果が出るまで',
    'Trap lost per hour': '1時間あたりのトラップの損失',
    'Traps: catch odds, bait and hours': 'トラップ: 捕獲確率、餌、時間帯',
    "Traps: keep vanilla's Trapping level requirements": 'トラップ: ゲーム本来のトラップレベル条件を維持する',
    'Zone': 'ゾーン',
    'a second dose resets the clock, it does not add': '2錠目は時間を加算せずリセットする',
    'a third of the strength above {} intoxication': '酩酊 {} を超えると強さは3分の1',
    'fresh for %1': 'あと %1 は新鮮',
    'half the strength above {} intoxication': '酩酊 {} を超えると強さは半分',
    'each pill counts double above {} intoxication': '酩酊 {} を超えると錠剤は2錠分として数える',
    'holds the fever, does not cure it': '熱を抑えるが、治しはしない',
    'incoming panic {}%% per pill, down to nothing': '受けるパニックが1錠につき {}%%、ゼロまで',
    'it catches nothing while you are near it': 'そばにいる間は何も捕まえない',
    'only the first dose has to wait': '待つ必要があるのは最初の1錠だけ',
    'overdose: {} pills cost {} health, {} cost {}, {} kill': '過剰摂取: {} 錠で体力 {}、{} 錠で {}、{} 錠で死亡',
    'sleeping cancels the effect': '眠ると効果が消える',
    'stale, catches nothing': '古くなり、何も引き寄せない',
    'the longer it waits, the likelier it comes out dead': '待たせるほど、死んで出てくる可能性が高くなる',
    'to full in %1': '%1 で最大',
    'to zero in %1': '%1 でゼロ',
    'wound pain stops being recalculated while it lasts': '効いている間は傷の痛みが再計算されない',
    'zombie fever held': 'ゾンビ熱を抑制中',
    '{}%% reading time': '読書時間 {}%%',
    'Effect': '効果',

    # Ronda 4, segunda pasada
    '%1 s': '%1 秒',
    '%1 s per round': '1発あたり %1 秒',
    '%1%% attack speed': '攻撃速度 %1%%',
    'Details': '詳細',
    'Info': '情報',
    'Possible prey': '捕まえられる獲物',
    'Trap breaks per hour': '1時間あたりのトラップ破損',
    'holds the fever': '熱を抑える',
    'not being used (%1 corpses nearby)': '消費されていません（近くに死体 %1 体）',
    'Bird': '鳥',
    'Active hours': '活動時間帯',
    'Possible prey, share of the catch': '捕まえられる獲物、捕獲割合',
    'Catch chance': '捕獲確率',
    'Bait condition': '餌の状態',
    'Trap condition': 'トラップの状態',
    'while you are near it, it neither catches nor breaks': 'そばにいる間は、何も捕まえず壊れもしない',
    'Bait loss risk, per hour': '1時間あたりの餌を失う危険',
    'Wrecked by an animal, per hour': '1時間あたりに動物に壊される確率',
    '%1 / h': '%1 / 時',
    'Bait loss risk': '餌を失う危険',
    'Chance of being wrecked': '壊される確率',
    'Critical damage': 'クリティカルダメージ',
    'Effective durability': '実質耐久',
    'Damage with your character': 'あなたのキャラクターでのダメージ',
    'Reach (tiles)': '間合い（タイル）',

    # Bags and the torch beam (0.9.20)
    'All round': '全方向',
    'Beam (degrees)': '光の広がり（度）',
    'Bags: how much they slow you down': 'バッグ：どれだけ遅くなるか',
    "The run and combat speed a bag costs you, which the game applies and never shows. The run figure is the one you are paying right now: a bag's penalty grows by half again as it fills up, so the same pack goes from {}%% empty to {}%% full. It counts the same in your hands as on your back.": 'バッグが奪う移動速度と戦闘速度で、ゲームは適用しているのに表示しません。移動の数値は今まさに払っている分です。中身が増えるとペナルティは 1.5 倍まで重くなり、同じバッグでも空なら {}%%、満杯なら {}%% になります。手に持っていても背負っていても同じように計算されます。',

    # Trait figures corrected against bytecode (0.9.21)
    "Aiming and Maintenance are not affected":
        "照準と整備は影響を受けない",
    "ambient light never drops below {} in the dark":
        "暗闇での環境光が {} を下回らない",
    "can tell a poisonous wild plant from a safe one":
        "野生植物が有毒かどうか見分けられる",
    "lights a fire with a notched plank twice as fast":
        "切り込み板での火起こしが 2 倍速い",
    "no harm at all from tainted water":
        "汚れた水による害を一切受けない",
    "{} health on every construction":
        "すべての建造物に耐久 {}",
    "{} tiles of perception instead of {}":
        "知覚範囲 {} マス（{} から）",
    "{}%% XP in the six melee weapon skills":
        "近接武器 6 種のスキル経験値 {}%%",
    "{}%% chance of tearing your clothes on a tree":
        "木で服が破れる確率 {}%%",
    "{}%% from any other poison":
        "その他の毒による害 {}%%",
    "{}%% from any other poison, bleach aside":
        "漂白剤を除くその他の毒による害 {}%%",
    "{}%% weather penalty in combat":
        "戦闘中の天候ペナルティ {}%%",

    # Per-level lines for the twenty craft skills (0.9.21)
    "%1 crop health at planting":
        "植えたときの作物の健康 %1",
    "%1%% chance the crop is cursed if planted out of its month":
        "本来の月以外に植えた場合に作物が呪われる確率 %1%%",
    "%1%% chance of a bonus harvest planted in its best month":
        "最適な月に植えた場合のボーナス収穫の確率 %1%%",
    "%1 disease removed per treatment":
        "処置 1 回あたり病害を %1 除去",
    "%1%% chance of harvesting %2 extra vegetables":
        "野菜を %2 個多く収穫する確率 %1%%",
    "%1%% back strain planting and harvesting":
        "植え付けと収穫での腰への負担 %1%%",
    "%1 points off the chance a stressed animal breaks off milking or shearing":
        "ストレス状態の家畜が搾乳や毛刈りで暴れる確率に %1 ポイント",
    "a stressed animal never breaks off milking or shearing":
        "ストレス状態の家畜が搾乳や毛刈りで暴れなくなる",
    "x%1 chance of each extra part off a carcass":
        "死体から追加部位が得られる確率 x%1",
    "x%1 of each part":
        "各部位の量 x%1",
    "up to %1 blood splatters on you":
        "身体に付く血しぶきは最大 %1 か所",
    "%1 health on everything you build":
        "建てたものすべてに耐久 %1",
    "%1%% build time":
        "建築時間 %1%%",
    "%1%% barricading time":
        "バリケード時間 %1%%",
    "%1%% chance of recovering material when dismantling":
        "解体時に素材を回収できる確率 %1%%",
    "%1%% of the ingredient used per addition":
        "追加 1 回あたりに消費する食材 %1%%",
    "x%1 nutrients from each ingredient":
        "食材 1 つあたりの栄養 x%1",
    "rotten food can go in evolved recipes, worth %1%% of its hunger":
        "発展レシピに少量の腐った食材を入れられる",
    "x%1 fracture healing with a splint":
        "添え木での骨折治癒 x%1",
    "a bandage lasts %1 to %2 longer":
        "包帯の持続が %1 から %2 倍長い",
    "%1%% time for every medical action":
        "すべての医療行為の所要時間 %1%%",
    "you can judge how bad a wound is":
        "傷の重さを判断できる",
    "you can read pain, and spot the burns that need washing":
        "痛みを読み取り、洗浄が必要な火傷を見分けられる",
    "you can tell when stitches are ready to come out":
        "縫合を抜いてよい時期がわかる",
    "you spot a wound infection straight away":
        "傷の感染をすぐに見抜ける",
    "%1%% chance of getting the patch back":
        "当て布を回収できる確率 %1%%",
    "%1%% time to add or remove a patch":
        "当て布の着脱にかかる時間 %1%%",
    "a hole can be repaired completely, defense and insulation included":
        "穴を完全に修復できる、防御と断熱を含めて",
    "+%1%% generator condition per repair":
        "修理 1 回あたり発電機の状態 +%1%%",
    "%1 points to the chance of hotwiring a car":
        "車の直結始動の成功率に %1 ポイント",
    "%1%% chance of setting off the car alarm":
        "車の警報が鳴る確率 %1%%",
    "you can salvage and repair a standard engine":
        "標準エンジンを回収して修理できる",
    "you can salvage and repair a heavy-duty engine":
        "大型エンジンを回収して修理できる",
    "you can salvage and repair a sport engine":
        "スポーツエンジンを回収して修理できる",
    "you can build the sturdier brick wall":
        "より頑丈なれんが壁を建てられる",
    "small %1%%, medium %2%%, large %3%%":
        "小 %1%%、中 %2%%、大 %3%%",
    "%1 points to the chance a berry or mushroom is poisonous":
        "ベリーやキノコが有毒である確率に %1 ポイント",
    "%1%% time to inspect a track":
        "足跡を調べる時間 %1%%",
    "no effect of its own, this level only unlocks the recipes below":
        "固有の効果はなく、このレベルは下のレシピを解放するだけ",

    # 0.9.21 follow-up
    "%1 rags when you rip up clothing, capped by the parts it covers":
        "衣類を裂いたとき %1 枚、その衣類が覆う部位数が上限",
    "rotten food can go in evolved recipes, worth %1%% of its hunger":
        "腐った食材も発展レシピに使える、満腹度の %1%% 分になる",

    # 0.9.21 follow-up 2
    "%1%% time per litre shearing an animal":
        "動物の毛刈り 1 リットルあたりの時間 %1%%",
    "%1 rags when you rip up clothing, capped by the parts it covers":
        "衣類を裂いたとき %1 枚のぼろ布、その衣類が覆う部位数が上限",
    "%1 to the most aramid thread you can pull out":
        "取り出せるアラミド糸の上限 %1",
    "starts at {} weight, becomes Emaciated at {} or less and Low Weight above {}":
        "体重 {} で始まり、{} 以下で「やせ衷え」に、{} を超えると「体重不足」になる",
    "starts at {} weight, becomes High Weight below {}":
        "体重 {} で始まり、{} を下回ると「太り過ぎ」になる",
    "starts at {} weight, becomes Very High Weight at {} and is lost below {}":
        "体重 {} で始まり、{} で「肥満」になり、{} を下回ると失われる",
    "starts at {} weight, becomes Very Low Weight at {} or less and is lost above {}":
        "体重 {} で始まり、{} 以下で「痩せ過ぎ」になり、{} を超えると失われる",
    "XP awarded":
        "獲得経験値",
    "{} chance to trip when a zombie lunges through a window":
        "ゾンビが窓から飛びかかってきたときの転倒率 {}",
    "{} to the roll that keeps you on your feet when a zombie shoves you":
        "ゾンビに突き飛ばされたとき踏みとどまる判定 {}",
    "{}%% muscle strain":
        "筋肉疲労 {}%%",
    "{}%% axe attack speed, chopping trees included":
        "斧の攻撃速度 {}%%（伐採も含む）",

    # B42.20 trait corrections
    "Another x{} at panic level {}":
        "パニック {1} でさらに x{0}",
    "Can hotwire without Electrical {} and Mechanics {}":
        "電気 {} と整備 {} なしで直結できる",
    "Engine revs three times faster in reverse":
        "後退時はエンジン回転が3倍速く上がる",
    "Halves your rope climbing bonus":
        "ロープ登りのボーナスが半減",
    "No unhappiness from looting corpses":
        "死体を漁っても不幸にならない",
    "Stress from handling bloody items":
        "血まみれの物を扱うとストレス",
    "{} move speed at panic level {}, {} at level {}":
        "パニック {1} で移動速度 {0}、{3} で {2}",
    "{} to the rope climbing roll":
        "ロープ登り判定 {}",
    "{}%% acceleration, fading out above {}%% of the car's top speed":
        "加速 {0}%%、車の最高速度の {1}%% を超えると弱まる",
    "{}%% carry capacity":
        "所持重量 {}%%",
    "{}%% chance of breaking a window lock instead of {}%%":
        "窓の鍵を壊す確率が {1}%% ではなく {0}%%",
    "{}%% endurance cost on every exertion":
        "動作ごとのスタミナ消費 {}%%",
    "{}%% reverse acceleration, gone past {} km/h":
        "後退時の加速 {0}%%、{1} km/h を超えると効かない",
    "{}%% unhappiness from looting corpses":
        "死体を漁るときの不幸 {}%%",

    # Repair recipes
    "Repair: +%1 condition, %2 chance of failing":
        "修理：耐久 +%1、失敗 %2",
    "Repair: +%1 condition, %2 chance of failing, repaired %3 times":
        "修理：耐久 +%1、失敗 %2、修理済み %3 回",

    # Corpse count and temperature figures
    "Body temperature: the number on every bar":
        "体温：各バーの数値",
    "Nauseous: how many corpses are making you ill":
        "吐き気：何体の死体が体調を崩させているか",
    "Rotting corpses nearby raise food sickness, and the game never says how many are close enough. Five or fewer do nothing. The count is read back out of the game, so it follows the sandbox setting.":
        "近くの腐乱死体は食中毒を高めるが、何体が十分に近いのかをゲームは決して教えない。5体以下では何も起きない。数はゲーム自体から読み戻すので、サンドボックス設定にそのまま従う。",
    "The temperature view prints its value on Insulation and Wind resistance and leaves the other nine bars as a colour. This sets the same flag on the rest, so skin temperature, body response, heat and wetness read as figures. Vanilla does the drawing, and only for the body part you have selected.":
        "温度ビューは「断熱」と「防風」にだけ数値を書き、残り9本のバーは色のままにしている。ここでは残りにも同じフラグを立てるので、皮膚温度、身体反応、熱、濡れが数字で読める。描画はゲーム自身が行い、選択した部位のみ。",

    # Options tab
    "Custom":
        "カスタム",
    "Nothing matches that":
        "一致するものがない",
    "Moodles: how many corpses are making you ill":
        "ムードル：何体の死体が体調を崩させているか",

    # Option groups
    "Every gun this box or magazine fits, one per row.":
        "この箱や弾倉が合う銃を、1行に1つずつ。",
    "How bloody the garment is, out of a hundred.":
        "衣服の血の付き具合、100点満点。",
    "How brightly it lights what it reaches.":
        "届いた範囲をどれだけ明るく照らすか。",
    "How dirty the garment is, out of a hundred.":
        "衣服の汚れ具合、100点満点。",
    "How drunk this container will get you.":
        "この容器でどれだけ酔うか。",
    "How far the light reaches, in tiles.":
        "光が届く距離、タイル単位。",
    "How far the shot is heard, which is how far the horde comes from.":
        "銃声が届く距離、つまり群れが寄ってくる距離。",
    "How long before the pill starts working, and only while you have none running.":
        "薬が効き始めるまでの時間。効いている薬がないときだけ表示。",
    "How long cooked food can stay on the heat before it burns.":
        "火にかけたままの調理済みの食べ物が焦げるまでの時間。",
    "How long the charge lasts with the thing switched on.":
        "電源を入れたままで充電が持つ時間。",
    "How long the filter lasts at your current exposure, and how many corpses are around you.":
        "今の曝露でフィルターが持つ時間と、周囲の死体の数。",
    "How long the item burns for as fuel.":
        "そのアイテムが燃料として燃える時間。",
    "How long the pages you have not read yet will take.":
        "まだ読んでいないページにかかる時間。",
    "How long the pill keeps working.":
        "薬の効果が続く時間。",
    "How long the plant takes to be ready, at the current farming speed.":
        "現在の栽培速度で作物が育ちきるまでの時間。",
    "How long until the food goes stale, at the current rot speed.":
        "現在の腐敗速度で食べ物が古くなるまでの時間。",
    "How long until the food is rotten, at the current rot speed.":
        "現在の腐敗速度で食べ物が腐るまでの時間。",
    "How many hits the weapon has left in it, which is the one figure that compares any two weapons.":
        "その武器にあと何回分の殴りが残っているか。任意の2本を比べられる唯一の数字。",
    "How much cold the garment keeps out. The game only draws a bar.":
        "衣服がどれだけ寒さを防ぐか。ゲームはバーしか描かない。",
    "How much is left in the filter.":
        "フィルターの残量。",
    "How much of it you have already heard.":
        "そのうちどれだけ聴き終えたか。",
    "How much of the corpse sickness the mask keeps off you. {}%% is immunity.":
        "死体病をマスクがどれだけ防いでくれるか。{}%% で完全な免疫。",
    "How much of your hunger bar the drink covers.":
        "その飲み物が空腹ゲージをどれだけ埋めるか。",
    "How much of your thirst bar the drink covers.":
        "その飲み物が喉の渇きゲージをどれだけ埋めるか。",
    "How much pull the rod takes before the line gives.":
        "糸が切れるまで竿が耐える引きの強さ。",
    "How much rain the garment keeps out. The game only draws a bar.":
        "衣服がどれだけ雨を防ぐか。ゲームはバーしか描かない。",
    "How much the bag slows you down, with its weight and what is inside counted.":
        "そのバッグがどれだけ足を遅くするか。重さと中身も計算済み。",
    "How much the bag slows your swing.":
        "そのバッグがどれだけ攻撃を遅くするか。",
    "How much the garment slows you down, as the penalty itself rather than a bar.":
        "その衣服がどれだけ足を遅くするか。バーではなくペナルティそのもので。",
    "How much the garment slows your swing, as the penalty itself rather than a bar.":
        "その衣服がどれだけ攻撃を遅くするか。バーではなくペナルティそのもので。",
    "How much tiredness this surface actually clears, your traits included.":
        "この寝床で実際にどれだけ疲労が抜けるか。特性も計算済み。",
    "How much wind the garment keeps out. The game only draws a bar.":
        "衣服がどれだけ風を防ぐか。ゲームはバーしか描かない。",
    "How often a hit crits, with your level in the weapon's own skill counted.":
        "攻撃がクリティカルになる頻度。その武器のスキルレベルも計算済み。",
    "How often a shot crits.":
        "射撃がクリティカルになる頻度。",
    "How wet the garment is, out of a hundred.":
        "衣服の濡れ具合、100点満点。",
    "In tiles. A swing landed at the edge of your reach does up to twice the damage of one landed close in.":
        "タイル単位。間合いのぎりぎり端で当てた一撃は、密着で当てた一撃の最大2倍のダメージになる。",
    "Off by default: the game only reveals this block for packaged food or a Nutritionist.":
        "初期状態はオフ。ゲームはこの欄を包装食品か栄養士のときしか出さない。",
    "Rounds in the magazine right now, out of what it holds.":
        "今、弾倉に入っている弾数と、入る上限。",
    "The calibre the magazine takes.":
        "その弾倉が受け付ける口径。",
    "The calories in what is actually in the container, mixtures included.":
        "容器に実際に入っているもののカロリー。混合物も含む。",
    "The carbohydrates in what is actually in the container.":
        "容器に実際に入っているものの炭水化物。",
    "The charge left, as a number instead of a bar.":
        "残りの充電量を、バーではなく数字で。",
    "The edge, and the ceiling a worn head puts on it: blunt, the weapon loses the top of its damage range.":
        "切れ味と、摩耗したヘッドがそれに課す上限。切れ味が落ちると武器はダメージ上限を失う。",
    "The exact minimum and maximum. The game only ever draws it as a bar.":
        "正確な最小値と最大値。ゲームはバーでしか描かない。",
    "The exact points left, and the head's own count on a weapon that has one.":
        "正確な残り耐久値。ヘッドのある武器はヘッドの分も別に。",
    "The exact points left, where the game only draws a bar.":
        "ゲームがバーしか描かないところに、正確な残り耐久値を。",
    "The fat in what is actually in the container.":
        "容器に実際に入っているものの脂質。",
    "The fatigue each swing costs you.":
        "一振りごとにかかる疲労。",
    "The furthest tile the gun can hit.":
        "その銃が届く一番遠いタイル。",
    "The gun's own hit chance, before your aiming skill.":
        "射撃スキルを除いた、その銃自体の命中率。",
    "The hook fitted, and what it does to your odds of a bite.":
        "付いている針と、それが食いつく確率に与える影響。",
    "The line fitted, and how much of it each tug wears away.":
        "付いている糸と、一回の引きで減る量。",
    "The months it can be sown in, one per row.":
        "種をまける月を、1行に1つずつ。",
    "The multiplier your shoes put on stomping a downed zombie. Footwear only.":
        "倒れたゾンビを踏みつけるときに靴がかける倍率。履物のみ。",
    "The multiplier your skill puts on this weapon's swing.":
        "この武器の一振りにスキルがかける倍率。",
    "The net pace of the pill, which is what compares two of them at a glance.":
        "薬の正味の速さ。2種類を一目で比べられる数字。",
    "The odds of losing a point of condition on a hit, with Maintenance and the weapon's skill counted.":
        "一撃で耐久を1失う確率。整備スキルとその武器のスキルも計算済み。",
    "The odds of losing a point of condition per shot.":
        "1発ごとに耐久を1失う確率。",
    "The poison the drink carries, and only while the game is willing to tell you.":
        "実際のジャム率。摩耗と握りの弱さも含む。",
    "The proteins in what is actually in the container.":
        "容器に実際に入っているもののタンパク質。",
    "The real odds of a jam, wear and a weak grip included.":
        "その飲み物が含む毒。ゲームが教えてくれる場合のみ。",
    "The real seconds a reload takes, with your reloading skill and your panic counted.":
        "リロードに実際にかかる秒数。リロードスキルとパニックも計算済み。",
    "The real seconds spent lining up the shot, with your aiming skill and your traits counted.":
        "構えて狙うのに実際にかかる秒数。射撃スキルと特性も計算済み。",
    "The recipes it teaches that you do not know yet, one per row.":
        "それが教えてくれる、まだ知らないレシピを1行に1つずつ。",
    "The swing animation, which is what really separates a slow weapon from a fast one.":
        "振りのアニメーション。遅い武器と速い武器を実際に分けているもの。",
    "What a critical is worth, from {}%% to {}%% depending on the weapon. The game shows it nowhere.":
        "クリティカルの威力。武器によって {}%% から {}%% まで。ゲームはどこにも表示しない。",
    "What feeds the Uncomfortable moodle. The game never shows it on the garment at all.":
        "不快ムードルの元になる値。ゲームは衣服の上でまったく表示しない。",
    "What is left in your hands when the rod breaks.":
        "竿が折れたとき手に残るもの。",
    "What sleeping here costs you in comfort.":
        "ここで寝ると快適さの面で何を失うか。",
    "What the drink does to boredom and unhappiness, which move together here.":
        "その飲み物が退屈と不満に与える影響。ここでは両方が一緒に動く。",
    "What the drink does to your fatigue bar.":
        "その飲み物が疲労ゲージに与える影響。",
    "What the drink does to your stress.":
        "その飲み物がストレスに与える影響。",
    "What the food still needs, and the temperature the figure assumes.":
        "食べ物にあとどれだけ必要か、そしてその数字が前提にしている温度。",
    "Whether it is a cone you aim or a lamp that lights all around, and how wide the cone is.":
        "向ける円錐なのか周囲を照らすランプなのか、そして円錐の広さ。",
    "Which fish this bait brings in.":
        "この餌が寄せてくる魚。",
    "Which skill the tape or disc trains and how much experience is left in it.":
        "そのテープやディスクが鍛えるスキルと、残っている経験値。",
    "Which skill the weapon trains, and therefore which one drives its damage and its speed.":
        "その武器が鍛えるスキル。つまりダメージと速度を動かしているスキル。",
    "Your own reading speed, traits, glasses and sitting down included.":
        "あなた自身の読書速度。特性、眼鏡、座っていることも含む。",
    "Nutrition":
        "栄養",
    "Sleep":
        "睡眠",
    "How much the bag slows your attack. It multiplies the weapon's own swing speed, not your walking.":
        "そのバッグが攻撃をどれだけ遅くするか。かかるのは武器自体の振りの速さで、歩く速さではない。",
    "How much the garment slows your attack. It multiplies the weapon's own swing speed, not your walking.":
        "その衣服が攻撃をどれだけ遅くするか。かかるのは武器自体の振りの速さで、歩く速さではない。",
    "Best baits":
        "最適な餌",
    "Every animal this trap can catch and its share of the catch.":
        "この罠にかかりうる動物と、それぞれの捕獲の割合。",
    "Feathers":
        "羽根",
    "Fog on a line of its own, because the game lumps it into weather and then reports neither.":
        "霧を独立した行に。ゲームは霧を天候にまとめてしまい、結局どちらも伝えないため。",
    "Glass or a bullet still in the wound, which stops it healing until it is out.":
        "傷口に残ったガラスや弾丸。抜くまで傷は治らない。",
    "How far the disease has gone, out of a hundred.":
        "病気がどこまで進んでいるか、100点満点。",
    "How far the generator is heard, halved when it stands indoors.":
        "発電機の音が届く距離。屋内では半分になる。",
    "How full the udder is and whether it can be milked yet.":
        "乳房の張り具合と、もう搾れるかどうか。",
    "How hungry the animal is, and how long its feed will last.":
        "その動物の空腹度と、餌がどれだけ持つか。",
    "How long before old age starts costing the animal its yield.":
        "老いが動物の産出を削り始めるまでの時間。",
    "How long each cut, scratch, burn or bite still needs.":
        "切り傷、擦り傷、火傷、噛み傷それぞれにあと必要な時間。",
    "How long is left of a pregnancy, or of an egg being fertilised.":
        "妊娠の残り、または卵が受精するまでの残り。",
    "How long since the last watering. The game works it out to pick a colour and then never shows it.":
        "最後に水をやってからの時間。ゲームは色を決めるために計算しておきながら、決して表示しない。",
    "How long the bandage lasts before it is dirty and worth changing.":
        "包帯が汚れて交換に値するまでの時間。",
    "How long the catch has been waiting in there.":
        "獲物が中で待たされている時間。",
    "How long the fracture needs, and what the splint on it is worth.":
        "骨折に必要な時間と、当てられた添え木の価値。",
    "How long the fuel in the tank lasts at the current draw.":
        "現在の消費でタンクの燃料が持つ時間。",
    "How long the part needs to be whole again, and how fast it is healing.":
        "その部位が元通りになるまでの時間と、治りの速さ。",
    "How long the stiffness in that limb takes to pass.":
        "その手足のこわばりが取れるまでの時間。",
    "How long the stitches need, and when they can come out.":
        "縫合に必要な時間と、抜糸できる時期。",
    "How long until it breaks down for good, on average.":
        "平均して、完全に壊れるまでの時間。",
    "How long until it wears down to the point where it can catch fire.":
        "発火しうる状態まで摩耗するまでの時間。",
    "How long until the crop moves to its next stage.":
        "作物が次の段階に進むまでの時間。",
    "How long you will wait compared with the best possible spot.":
        "最良の場所と比べてどれだけ待つことになるか。",
    "How many feathers butchering will give.":
        "解体で得られる羽根の量。",
    "How many fish this spot still holds, and what that is worth.":
        "この場所に残っている魚の数と、その価値。",
    "How much blood butchering will give.":
        "解体で得られる血の量。",
    "How much fertiliser the plot holds. Above one is the too much case in the game's own code.":
        "その区画の肥料の量。1を超えるとゲーム自身のコードで過剰の扱いになる。",
    "How much meat butchering will give, which is what answers whether it is worth killing yet.":
        "解体で得られる肉の量。「まだ仕留める価値があるか」への答えはこれ。",
    "How much of the bait is still good.":
        "餌のうちまだ使える割合。",
    "How much the animal trusts you, which is what lets you handle it.":
        "その動物がどれだけ懐いているか。世話ができるかどうかを決めるのがこれ。",
    "How much wool has grown back and whether it can be sheared yet.":
        "羊毛がどれだけ生え戻ったかと、もう刈れるかどうか。",
    "How stressed the animal is, out of a hundred.":
        "その動物のストレス度、100点満点。",
    "How the wound infection is going, and whether it is still rising.":
        "傷口の感染の進み具合と、まだ悪化しているかどうか。",
    "How thirsty the animal is, and how long its water will last.":
        "その動物の喉の渇きと、水がどれだけ持つか。",
    "Level needed":
        "必要レベル",
    "Lodged objects":
        "刺さったままの異物",
    "Odds with your bait":
        "手持ちの餌での確率",
    "Predator":
        "捕食魚",
    "Size and weight":
        "大きさと重さ",
    "Strength at the top skill level":
        "最高レベルでの強度",
    "The Fishing level this species needs before it will bite.":
        "この魚種が食いつくのに必要な釣りレベル。",
    "The animal's health as a number.":
        "動物の体力を数値で。",
    "The animal's weight, and how far it still has to grow.":
        "動物の体重と、あとどれだけ育つか。",
    "The chance of this exact species with the bait you are using.":
        "今使っている餌で、まさにこの魚種が釣れる確率。",
    "The crop's health out of a hundred. The game only prints it with debug on.":
        "作物の健康度、100点満点。ゲームはデバッグ時にしか表示しない。",
    "The fuel still in the tank. The game knows the number and only prints it as a debug option.":
        "タンクに残る燃料。ゲームはこの数値を持っていながら、デバッグ用の項目としてしか出さない。",
    "The health the wall or door will have when you build it at your current level.":
        "今のレベルで建てた場合に、その壁や扉が持つ耐久。",
    "The hourly odds of a bang loud enough to pull zombies in.":
        "ゾンビを引き寄せるほどの大きな破裂音が起きる1時間あたりの確率。",
    "The hourly odds of a fire or an explosion, which set the generator to zero outright.":
        "火災や爆発が起きる1時間あたりの確率。どちらも発電機を一気にゼロにする。",
    "The hourly odds of the bait being taken without a catch.":
        "獲物がかからないまま餌だけ持っていかれる1時間あたりの確率。",
    "The hourly odds of the trap being wrecked.":
        "罠が壊される1時間あたりの確率。",
    "The hourly odds of the wound becoming infected.":
        "傷口が感染する1時間あたりの確率。",
    "The hours of the day the trap actually works.":
        "その罠が実際に機能する時間帯。",
    "The kind of ground the trap is standing on, which decides what can come.":
        "罠が置かれている地形の種類。何が来るかを決めるのはこれ。",
    "The odds of a bite once every factor is put together.":
        "すべての要因を合わせたうえでの、食いつく確率。",
    "The odds of catching anything at all in an hour.":
        "1時間のうちに何かしら獲れる確率。",
    "The range of lengths and weights this species comes in.":
        "この魚種が取りうる体長と体重の幅。",
    "The share of your catches that will be junk here.":
        "ここでの釣果のうちゴミになる割合。",
    "The two things the game never says: a long wait kills the catch, and standing nearby stops the trap.":
        "ゲームが決して言わない2つのこと。待たせすぎると獲物は死に、そばにいる間は罠が働かない。",
    "The water level as a number, and the amount this seed actually needs.":
        "水分量の数値と、この種が実際に必要とする量。",
    "Time to the danger threshold":
        "危険域までの時間",
    "Trophy size":
        "トロフィーの基準",
    "Warnings":
        "警告",
    "Warns that the species only bites while you reel in.":
        "その魚種は糸を巻いている間しか食いつかないことを知らせる。",
    "What a catch has to beat to count as a trophy.":
        "トロフィー扱いになるために釣果が超えるべき値。",
    "What the herbs in the bandage are adding.":
        "包帯に入った薬草が加えているもの。",
    "What the same build would have at level {}, which is the reason to know the figure before building.":
        "同じ建築物がレベル {} だといくつになるか。建てる前にこの数値を知る意味はここにある。",
    "What the time of day is worth, as the multiplier behind the game's own rating.":
        "時間帯の価値。ゲーム自身の評価の裏にある倍率として。",
    "What the water temperature is worth, with the actual reading in degrees.":
        "水温の価値。実際の温度も添えて。",
    "What the weather is worth, as the multiplier behind the game's own rating.":
        "天候の価値。ゲーム自身の評価の裏にある倍率として。",
    "What the wind is worth. Past half strength it costs the same penalty fog does, and the two never stack.":
        "風の価値。強さが半分を超えると霧と同じ penalty がかかり、両者が重なることはない。",
    "Whether the mains or a generator is keeping the pump running.":
        "そのポンプを動かしているのが送電網か発電機か。",
    "Which animals a bait item brings in.":
        "餌として使う品物がどの動物を引き寄せるか。",
    "Which bait is in the trap, and whether it is still fresh.":
        "罠に入っている餌と、それがまだ新鮮かどうか。",
    "Which baits work best on this species.":
        "その魚種に最もよく効く餌。",
    "Which growth stage the crop is on, out of the total.":
        "作物が全体のうち第何段階にあるか。",
    "Which hook is fitted and what it does to your odds.":
        "付いている釣り針と、それが確率に与える影響。",
    "Raw eggs never make you ill":
        "生卵で体調を崩すことはない",
    "{}%% wait before another anti-nausea food works":
        "次の吐き気止めが効くまでの待ち時間 {}%%",
    "{}%% weapon sight range":
        "照準器の射程 {}%%",
    "At Axe {} you swing as fast as a maxed axe user":
        "斧スキル{}でも、熟練者と同じ速さで振れる",
    "{}%% from any poisonous food or drink":
        "毒のある food や飲み物から {}%%",
    "{}%% chance of illness from rotten food":
        "腐った食べ物で病気になる確率 {}%%",
    "Melee weapons":
        "近接武器",
    "Firearms":
        "銃器",
    "Drinks":
        "飲み物",
    "Skill XP":
        "スキル経験値",
    "Weapons":
        "武器",
    "Worn and carried":
        "衣服と収納",
    "Medicine and reading":
        "薬と読み物",
    "Supplies":
        "物資",
    "Comparison":
        "比較",
    "Power and fuel":
        "電力と燃料",
    "Animals and traps":
        "動物と罠",
    "Traits and jobs":
        "特性と職業",
    "Moodles":
        "ムードル",
}
