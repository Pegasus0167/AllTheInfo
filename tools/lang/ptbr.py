"""Portuguese (Brazilian) phrase table for AllInfo.

Keys are the English fragment with every number replaced by {} in order.
Numbers are never written here: they ride through untouched. Use {0} {1} ...
instead of {} when the language needs a different order -- and then index every
slot, Python refuses to mix the two forms.

Run `python tools\\i18n.py` after editing: it checks the arity of every line and
refuses to write a language file it cannot fill completely.
"""

T = {
    # Per-level skill descriptions
    "x{} weapon damage (x{} untrained)": "x{} de dano da arma (x{} sem treino)",
    "{} to the durability roll": "{} na rolagem de durabilidade",
    "{} chance to trip vaulting a fence": "{} de chance de tropeçar ao pular uma cerca",
    "{}%% fall damage": "{}%% de dano de queda",
    "x{} endurance recovery (x{} untrained)": "x{} de recuperação de energia (x{} sem treino)",
    "x{} melee damage and knockback (x{} untrained)": "x{} de dano corpo a corpo e empurrão (x{} sem treino)",
    "x{} carrying capacity (x{} untrained)": "x{} de capacidade de carga (x{} sem treino)",
    "x{} move speed in combat stance (x{} untrained)": "x{} de velocidade em postura de combate (x{} sem treino)",
    "x{} sprint speed (x{} untrained)": "x{} de velocidade de corrida rápida (x{} sem treino)",
    "x{} chance of being spotted (x{} untrained)": "x{} de chance de ser notado (x{} sem treino)",
    "x{} footstep noise (x{} untrained)": "x{} de barulho dos passos (x{} sem treino)",
    "{} accuracy (the weapon's aiming modifier, {} on nearly every gun)":
        "{} de precisão (o modificador de mira da arma, {} em quase todas)",
    "{} wind penalty when aiming (of {})": "{} de penalidade de vento ao mirar (de {})",
    "x{} reload speed (x{} untrained)": "x{} de velocidade de recarga (x{} sem treino)",
    "x{} racking speed (x{} untrained)": "x{} de velocidade para engatilhar (x{} sem treino)",
    "racking costs {} of the aiming time ({} untrained)": "engatilhar custa {} do tempo de mira ({} sem treino)",
    "From here on you no longer count as unsteady with a firearm, as long as your Strength is {} or more: jam chance drops by {} percentage points.":
        "A partir daqui você deixa de contar como instável com armas de fogo, desde que sua Força seja {} ou mais: a chance de emperrar cai {} pontos percentuais.",
    "You never count as unsteady with a firearm again, whatever your Strength.":
        "Você nunca mais conta como instável com armas de fogo, seja qual for sua Força.",

    # Moodles
    "{} melee to-hit": "{} de acerto corpo a corpo",
    "{} climb chance": "{} de chance de escalar",
    "{} trip chance": "{} de chance de tropeçar",
    "{} to break a zombie's grab": "{} para escapar do agarrão de um zumbi",
    "{}%% strength": "{}%% de força",
    "{}%% healing": "{}%% de cura",
    "losing health": "perdendo vida",
    "harder to unjam a gun": "mais difícil desemperrar a arma",
    "{} move speed (of {})": "{} de velocidade de movimento (de {})",
    "body at {} C": "corpo a {} C",
    "{} carry capacity": "{} de capacidade de carga",
    "x{} attack speed": "x{} de velocidade de ataque",
    "endurance under {}%%": "energia abaixo de {}%%",
    "fatigue over {}%%": "fadiga acima de {}%%",
    "hunger over {}%%": "fome acima de {}%%",
    "thirst over {}%%": "sede acima de {}%%",
    "panic over {}%%": "pânico acima de {}%%",
    "stress over {}%%": "estresse acima de {}%%",
    "boredom over {}%%": "tédio acima de {}%%",
    "unhappiness over {}%%": "infelicidade acima de {}%%",
    "{}%% action speed": "{}%% de velocidade das ações",
    "anger over {}%%": "raiva acima de {}%%",
    "drunkenness over {}%%": "embriaguez acima de {}%%",
    "pain over {}%%": "dor acima de {}%%",
    "slower rope climbing": "sobe cordas mais devagar",
    "{}%% total body damage": "{}%% de dano corporal total",
    "sickness over {}%%": "doença acima de {}%%",
    "cold strength over {}%%": "intensidade do resfriado acima de {}%%",
    "wetness over {}%%": "umidade acima de {}%%",
    "discomfort over {}%%": "desconforto acima de {}%%",
    "rotting corpses nearby": "corpos apodrecendo por perto",
    "x{} move speed": "x{} de velocidade de movimento",
    "{} discomfort per level": "{} de desconforto por nível",
    "{} C on top of the air temperature": "{} C além da temperatura do ar",
    "carrying {}x capacity": "carregando {}x a capacidade",
    "{}%% body heat": "{}%% de calor corporal",
    "no sleep without pills": "não dorme sem comprimidos",
    "erratic movement": "movimento errático",
    "raises discomfort": "aumenta o desconforto",
    "no sprinting": "não pode correr rápido",
    "no sprinting, no exercise": "não pode correr rápido nem se exercitar",
    "zombies spot you {} sooner": "zumbis te notam {} antes",
    "muscle stiffness builds up": "a rigidez muscular se acumula",
    "cannot eat or open food": "não consegue comer nem abrir comida",
    "{} move speed with Adrenaline Junkie": "{} de velocidade com Viciado em Adrenalina",
    "nightmares while asleep": "pesadelos durante o sono",
    "no sleep below {}%% fatigue without pills": "sem comprimidos não dorme com fadiga abaixo de {}%%",
    "{}%% move speed": "{}%% de velocidade de movimento",
    "cannot move": "não consegue se mover",
    "{} climbing walls and ropes": "{} ao escalar muros e cordas",
    "no running, no exercise": "não pode correr nem se exercitar",
    "over {}x capacity": "acima de {}x a capacidade",
    "no running": "não pode correr",
    "no sprinting until you drop the bulky item": "não pode correr rápido até largar o item volumoso",
    "you can sleep through high pain": "consegue dormir mesmo com muita dor",
    "no endurance recovery": "a energia não se recupera",
    "{} vision cone": "{} no cone de visão",
    "delayed vehicle controls": "controles do veículo atrasados",
    "narrowed vision cone": "cone de visão estreitado",
    "no exercise": "não pode se exercitar",
    "{} wound bleeding": "{} ferimento sangrando",
    "Rest in peace.": "Descanse em paz.",
    "Infected. There is no cure.": "Infectado. Não há cura.",

    # Tooltip labels
    "Stale in": "Estraga em",
    "Rots in": "Apodrece em",
    "Cooking time": "Tempo de cozimento",
    "Never": "Nunca",
    "Critical chance": "Chance de crítico",
    "Trains": "Treina",
    "Attack speed": "Velocidade de ataque",
    "Swing type": "Tipo de golpe",
    "Heavy": "Pesado",
    "Swung": "Balançado",
    "Stabbing": "Perfurante",
    "Spear": "Lança",
    "Stone": "Pedra",
    "Knockback on hit": "Empurrão no acerto",
    "Condition loss": "Perda de condição",
    "Jam chance": "Chance de emperrar",
    "Accuracy": "Precisão",
    "Noise radius": "Raio do ruído",
    "Rounds": "Munição",
    "Reload time": "Tempo de recarga",
    "Aiming time": "Tempo de mira",
    "Used by": "Usada por",
    "Reading speed": "Velocidade de leitura",
    "Reading time left": "Leitura restante",
    "Skill too low to learn from it": "Habilidade baixa demais para aprender com ele",
    "Nothing left to learn from it": "Não há mais nada a aprender com ele",
    "Proteins": "Proteínas",
    "Sow in": "Plantar em",
    "Ready in": "Pronto em",
    "Burn time": "Tempo de queima",
    # Power: charge, autonomy and light
    "Duration": "Duração",
    "Light range": "Alcance da luz",
    "Light strength": "Intensidade da luz",
    "Batteries and radios: charge left, how long it lasts and how far a torch lights": "Pilhas e rádios: carga restante, duração e alcance da luz de uma lanterna",
    "Vanilla draws the charge of a drainable as a bar with no number on it, and never says how long a torch lasts or how far it lights. A torch spends its UseDelta once every ten game minutes, and only while it is in a hand or attached to you: left in a bag it switches itself off. Light range and strength are the figures that actually light the ground.":
        "O jogo desenha a carga de um item consumível como uma barra sem número e nunca diz quanto tempo dura uma lanterna nem até onde ela ilumina. Uma lanterna gasta seu UseDelta uma vez a cada dez minutos de jogo, e só enquanto está na mão ou presa a você: guardada na mochila, ela se apaga sozinha. Alcance e intensidade da luz são os números que de fato iluminam o chão.",
    "Rest quality": "Qualidade do descanso",
    "Discomfort": "Desconforto",
    "Stomp damage": "Dano ao pisotear",
    "Corpse sickness defense": "Defesa contra doença de cadáver",
    "Filter charge": "Carga do filtro",
    "New recipes": "Novas receitas",
    "Listened": "Ouvido",
    "Skill too high for this tape": "Habilidade alta demais para esta fita",

    # Options screen
    "All Info": "All Info",
    "Enable everything": "Ativar tudo",
    "Items": "Itens",
    "Crafting": "Fabricação",
    "World": "Mundo",
    "Character": "Personagem",
    "Everything in this section": "Tudo desta seção",
    "Food: time left before it spoils": "Comida: quanto falta para estragar",
    "Adds hours to stale and hours to rotten, at the current rate. Accounts for the fridge, the freezer and the sandbox spoilage speed.":
        "Mostra quantas horas faltam para estragar e para apodrecer, no ritmo atual. Considera a geladeira, o freezer e a velocidade de deterioração do sandbox.",
    "Cooking: add the warm-up minutes": "Cozimento: somar os minutos de aquecimento",
    "Off by default. Cooking time is the time at temperature; this adds the four minutes the food spends heating up before it starts to cook, so an oven timer set to the figure rings when the food is done.":
        "Desativado por padrão. O tempo de cozimento vale para o alimento já na temperatura; isto soma os quatro minutos que ele leva para esquentar antes de começar a cozinhar, para que o timer do forno toque quando estiver pronto.",
    "Food: calories, carbs, protein and fat": "Comida: calorias, carboidratos, proteínas e gorduras",
    "Off by default. Showing macros on every food undoes the Nutritionist trait, which is what normally reveals them.":
        "Desligado por padrão. Mostrar os macros em toda comida anula o traço Nutricionista, que é o que normalmente os revela.",
    "Melee: exact damage, speed and durability": "Corpo a corpo: dano, velocidade e durabilidade exatos",
    "Puts numbers on the condition and damage bars, and adds crit chance, swing type, attack speed, knockback and the odds of losing a condition point per hit.":
        "Põe números nas barras de condição e dano e acrescenta chance de crítico, tipo de golpe, velocidade de ataque, empurrão e a chance de perder um ponto de condição por golpe.",
    "Firearms: range, jam chance and reload": "Armas de fogo: alcance, chance de emperrar e recarga",
    "Puts numbers on the condition and damage bars, and adds accuracy, effective range, jam odds and magazine size.":
        "Põe números nas barras de condição e dano e acrescenta precisão, alcance efetivo, chance de emperrar e tamanho do carregador.",
    "Ammo: rounds left and what it fits": "Munição: quanto resta e em que serve",
    "No comparison arrows here: the thing in your hands is a gun, not another magazine, so there is no honest pair to compare.":
        "Aqui não há setas de comparação: o que está na sua mão é uma arma, não outro carregador, então não existe par honesto para comparar.",
    "Clothing: numbers on every bar, plus discomfort": "Roupas: números em todas as barras, mais o desconforto",
    "Vanilla draws condition, insulation, wind, water, blood, dirt and wetness as bars with no figures. This writes the figures next to them and adds the discomfort value, which vanilla never shows at all.":
        "O jogo desenha condição, isolamento, vento, água, sangue, sujeira e umidade como barras sem números. Isto escreve os números ao lado e acrescenta o desconforto, que o jogo não mostra em lugar nenhum.",
    "Seeds: growing time and yield": "Sementes: tempo de cultivo e colheita",
    "Firewood: how long it burns": "Lenha: quanto tempo queima",
    "Books: reading time and skill levels covered": "Livros: tempo de leitura e níveis cobertos",
    "Reading time already accounts for Fast Reader, Slow Reader and reading glasses.":
        "O tempo de leitura já considera Leitor Rápido, Leitor Lento e os óculos de leitura.",
    "Beds: how well you recover on them": "Camas: o quanto você descansa nelas",
    "Masks: filter life and protection": "Máscaras: vida do filtro e proteção",
    "Tapes and CDs: which skill they teach and how much XP": "Fitas e CDs: que habilidade ensinam e quanta XP dão",
    "Show the difference against what you have equipped": "Mostrar a diferença em relação ao que está equipado",
    "Adds a coloured +/- next to weapon and clothing values. Weapons compare against what is in your hands, clothing against the piece worn in the same slot.":
        "Acrescenta um +/- colorido junto aos valores de armas e roupas. Armas comparam com o que está na sua mão; roupas, com a peça usada no mesmo lugar.",
    "Crafting: full item tooltip on the recipe output": "Fabricação: informação completa do item no resultado da receita",
    "Hovering the result of a recipe shows the same block an item in your inventory would, comparison included, before you craft it.":
        "Passar o mouse sobre o resultado de uma receita mostra o mesmo bloco que o item teria no inventário, com comparação, antes de fabricar.",
    "Generators: fuel time, wear and danger": "Geradores: combustível, desgaste e perigo",
    "Adds noise radius, hours of fuel left, average time until {}%% condition and until it breaks, and the hourly odds of a backfire or a fire.":
        "Acrescenta raio de ruído, horas de combustível restantes, tempo médio até {}%% de condição e até quebrar, e a chance por hora de estouro ou incêndio.",
    "Generators: also show times in real-world minutes": "Geradores: mostrar os tempos também em minutos reais",
    "Off by default. Converts the in-game hours using the current day length, so you know how long you actually have to wait.":
        "Desligado por padrão. Converte as horas do jogo usando a duração atual do dia, para você saber quanto realmente vai esperar.",
    "Generators: outline the powered area on the floor": "Geradores: marcar no chão a área energizada",
    "Draws the edge of the range while the generator window is open, green when running and red when off. Only the floor you are standing on is computed.":
        "Desenha a borda do alcance enquanto a janela do gerador está aberta, verde se ligado e vermelho se desligado. Só o andar em que você está é calculado.",
    "Gas pumps: fuel left and power source": "Bombas de combustível: quanto resta e de onde vem a energia",
    "Adds an Info entry to the right-click menu of any gas pump, with the fuel still in the tank and whether the mains or a generator is keeping it running. The game knows that number and only prints it as a debug option.":
        "Adiciona uma entrada Info ao menu do botão direito de qualquer bomba de combustível, com o combustível que resta no tanque e se quem a mantém ligada é a rede elétrica ou um gerador. O jogo sabe esse número e só o mostra como opção de depuração.",
    "Fuel Remaining": "Combustível restante",
    "Mains power": "Rede elétrica",
    "Generator": "Gerador",
    "Walls and doors: health under the cursor": "Paredes e portas: resistência sob o cursor",
    "Shows current and maximum health as a number at the foot of whatever you point at, no clicking needed.":
        "Mostra a resistência atual e a máxima como número ao pé do que você apontar, sem precisar clicar.",
    "Build menu: health of what you are about to build": "Menu de construção: resistência do que você vai construir",
    "Also shows what that health would be with the relevant skill at {}, so you can tell whether it is worth waiting.":
        "Mostra também qual seria essa resistência com a habilidade correspondente em {}, para saber se vale a pena esperar.",
    "Crops: health, growth and water as numbers": "Plantações: saúde, crescimento e água em números",
    "Adds rows to the crop window you get by right-clicking a plant: health out of {}, current phase, hours to the next one, water level against what the plant needs, time since the last watering and pest levels.":
        "Acrescenta linhas à janela que aparece ao clicar com o botão direito numa planta: saúde de {}, fase atual, horas até a próxima, nível de água contra o que a planta precisa, tempo desde a última rega e o nível de cada praga.",
    "Crops: keep vanilla's Farming level requirements": "Plantações: manter as exigências de nível de Agricultura do jogo",
    "Off by default, so you see everything from level {}. Turn it on and each row reappears at the Farming level vanilla itself uses for it: phase and health at {}, water at {}, pests at {}, next phase at {}.":
        "Desligado por padrão, então você vê tudo desde o nível {}. Se ligar, cada linha volta ao nível de Agricultura que o próprio jogo usa: fase e saúde no {}, água no {}, pragas no {}, próxima fase no {}.",
    "Noise": "Ruído",
    "tiles": "blocos",
    "Down to %1%% (avg)": "Até %1%% (média)",
    "Breaks down in (avg)": "Quebra em (média)",
    "Backfire, loud (per hour)": "Estouro, alto (por hora)",
    "FIRE OR EXPLOSION (per hour)": "INCÊNDIO OU EXPLOSÃO (por hora)",
    "(real time)": "(tempo real)",
    "XP Boost: %1": "Bônus de XP: %1",
    "Skills": "Habilidades",
    "Also grants": "Também concede",
    "Disabled in multiplayer": "Desativado no multijogador",
    "Foraging": "Coleta",
    "search radius": "raio de busca",
    "weather penalty": "penalidade do clima",
    "darkness penalty": "penalidade da escuridão",
    "Strength when built": "Resistência ao construir",
    "With %1 at {}": "Com %1 em {}",
    "Show XP boosts as a multiplier, not a percentage": "Mostrar os bônus de XP como multiplicador, não como porcentagem",
    'Vanilla says "{}%%" for a level {} boost. The real figure is x{}, because a skill with no boost runs at a quarter rate. Fixed on all three screens that show it.':
        'O jogo diz "{}%%" para um bônus de nível {}. O número real é x{}, porque uma habilidade sem bônus rende um quarto. Corrigido nas três telas que mostram isso.',
    "Character creation: what each trait and job really does": "Criação de personagem: o que cada traço e profissão faz de verdade",
    "Adds starting skill levels with their true XP multiplier, free traits granted, recipes taught and foraging bonuses to the tooltips in the creation screen.":
        "Acrescenta às dicas da tela de criação os níveis iniciais de habilidade com o multiplicador real de XP, os traços gratuitos, as receitas ensinadas e os bônus de coleta.",
    "In game: the same block on the info tab": "No jogo: o mesmo bloco na aba de informações",
    "Hover a trait icon or the job icon in the character info tab to read the same block after the world has started.":
        "Passe o mouse sobre o ícone de um traço ou da profissão na aba de informações para ler o mesmo bloco com o mundo já iniciado.",
    "Add hand-written trait effects": "Acrescentar efeitos de traços escritos à mão",
    "Effects hardcoded in the game's Java that cannot be read at runtime, so they are written by hand and checked against each build.":
        "Efeitos fixos no Java do jogo que não podem ser lidos em tempo de execução, por isso são escritos à mão e conferidos a cada versão.",
    "Skills: which recipes each level requires": "Habilidades: que receitas cada nível exige",
    "Hover a level in the skills panel to see the recipes and builds that ask for it. Read from the game's own recipe list, so modded recipes appear too and nothing goes stale with a patch.":
        "Passe o mouse sobre um nível no painel de habilidades para ver as receitas e construções que o exigem. Lido da própria lista de receitas do jogo, então receitas de outros mods também aparecem e nada fica desatualizado após um patch.",
    "Needs this level": "Exigem este nível",
    "Skill and moodle descriptions are translation files. They cannot be switched off here; disable the mod to remove them.":
        "As descrições de habilidades e moodles são arquivos de tradução. Não dá para desligá-las aqui; desative o mod para removê-las.",
    "Run self-test": "Executar autoteste",

    # Trait and profession effects
    "{}%% footstep noise radius": "{}%% no raio de ruído dos passos",
    "more likely to fall when bumped": "cai mais facilmente ao ser empurrado",
    "less likely to fall when bumped": "cai menos facilmente ao ser empurrado",
    "{}%% run and sprint speed": "{}%% de velocidade de corrida e corrida rápida",
    "no Fitness XP from level {} on": "sem XP de Preparo Físico a partir do nível {}",
    "double endurance drain when running": "gasta o dobro de energia ao correr",
    "{}%% melee damage": "{}%% de dano corpo a corpo",
    "{} chance to trip from a lunge": "{} de chance de tropeçar num avanço",
    "starts at {} weight, and you lose health below {}": "começa com {} de peso, e abaixo de {} você perde vida",
    "{}%% axe swing time": "{}%% no tempo de golpe com machado",
    "{}%% axe damage to trees": "{}%% de dano de machado em árvores",
    "{}%% endurance lost running": "{}%% de energia gasta ao correr",
    "{}%% grapple effectiveness": "{}%% de eficácia no agarrão",
    "{}%% knockback": "{}%% de empurrão",
    "can be gained by training Strength to {}": "obtido treinando Força até {}",
    "becomes Strong at Strength {}": "vira Forte com Força {}",
    "becomes Feeble at Strength {}": "vira Frágil com Força {}",
    "lost by training Strength to {}": "perdido ao treinar Força até {}",
    "{}%% panic, night terrors aside": "{}%% de pânico, exceto terrores noturnos",
    "{}%% stress from looting corpses": "{}%% de estresse ao revistar corpos",
    "{}%% panic": "{}%% de pânico",
    "no panic from a corpse reanimating": "não entra em pânico quando um corpo reanima",
    "no stress from looting corpses": "revistar corpos não causa estresse",
    "{} move speed at panic {}": "{} de velocidade com pânico em {}",
    "still capped by the movement speed limit": "ainda limitado pelo teto de velocidade",
    "{}%% wind penalty when aiming": "{}%% de penalidade de vento ao mirar",
    "{}%% gun accuracy": "{}%% de precisão com armas de fogo",
    "{}%% gun crit chance": "{}%% de chance de crítico com armas de fogo",
    "shorter aiming delay": "atraso de mira menor",
    "wider field of view": "campo de visão mais amplo",
    "{}%% max range on weapon sights": "{}%% de alcance máximo das miras",
    "blurry vision": "visão embaçada",
    "weapon sight range bonus at its minimum": "bônus de alcance das miras no mínimo",
    "cancelled by wearing glasses": "anulado ao usar óculos",
    "{}%% perception radius": "{}%% de raio de percepção",
    "zombies behind you become visible sooner": "zumbis atrás de você ficam visíveis antes",
    "muffled sound effects": "sons abafados",
    "zombies behind you become visible later": "zumbis atrás de você ficam visíveis depois",
    "no sound at all": "nenhum som",
    "you can still watch TV": "ainda dá para assistir TV",
    "{}%% chance of not being injured by a zombie": "{}%% de chance de não se ferir com um zumbi",
    "{}%% chance of being scratched by trees": "{}%% de chance de se arranhar em árvores",
    "{}%% corpse sickness": "{}%% de doença de cadáver",
    "{}%% chance of catching a cold": "{}%% de chance de pegar um resfriado",
    "{}%% cold strength": "{}%% de intensidade do resfriado",
    "{}%% cold progression": "{}%% de avanço do resfriado",
    "{}%% zombification speed": "{}%% de velocidade de zumbificação",
    "{}%% severity of vehicle injuries": "{}%% de gravidade dos ferimentos de veículo",
    "{}%% fracture severity": "{}%% de gravidade das fraturas",
    "all wounds heal much faster": "todos os ferimentos curam muito mais rápido",
    "all wounds heal much slower": "todos os ferimentos curam muito mais devagar",
    "{}%% XP in every skill except Fitness and Strength": "{}%% de XP em todas as habilidades exceto Preparo Físico e Força",
    "{}%% reading speed": "{}%% de velocidade de leitura",
    "{}%% XP in every weapon skill and Aiming": "{}%% de XP em todas as habilidades de arma e em Mira",
    "{}%% inventory transfer time": "{}%% no tempo para mover itens",
    "{}%% aiming delay": "{}%% no atraso de mira",
    "guns jam less often": "as armas emperram menos",
    "fewer injuries opening cans": "menos ferimentos ao abrir latas",
    "guns jam more often": "as armas emperram mais",
    "more injuries opening cans": "mais ferimentos ao abrir latas",
    "{}%% container capacity": "{}%% de capacidade dos recipientes",
    "crafting does not return leftover items": "a fabricação não devolve o material que sobra",
    "{}%% thirst": "{}%% de sede",
    "{}%% hunger": "{}%% de fome",
    "{}%% food illness chance": "{}%% de chance de intoxicação alimentar",
    "{}%% food illness duration": "{}%% de duração da intoxicação alimentar",
    "{}%% harm from tainted water": "{}%% de dano da água contaminada",
    "{}%% tiredness gained while awake": "{}%% de cansaço acumulado acordado",
    "{}%% recovery while asleep": "{}%% de recuperação dormindo",
    "{}%% sleep duration": "{}%% de duração do sono",
    "you do not wake up at {} tiredness, so set an alarm": "você não acorda com {} de cansaço, então use um despertador",
    "harder to fall asleep": "mais difícil pegar no sono",
    "{}%% vision in the dark": "{}%% de visão no escuro",
    "smaller vision cone penalty at night": "menos penalidade no cone de visão à noite",
    "{}%% chance of being spotted (new stealth)": "{}%% de chance de ser notado (furtividade nova)",
    "{}%% chance of being spotted (old stealth)": "{}%% de chance de ser notado (furtividade antiga)",
    "{}%% chance of breaking kindling": "{}%% de chance de quebrar a isca de fogo",
    "{}%% weather penalty when aiming": "{}%% de penalidade do clima ao mirar",
    "lights fires twice as fast": "acende fogueiras duas vezes mais rápido",
    "almost never scratched by trees": "quase nunca se arranha em árvores",
    "{}%% endurance lost running, sprinting, carrying and dragging":
        "{}%% de energia gasta ao correr, correr rápido, carregar e arrastar",
    "{}%% endurance lost swinging a weapon": "{}%% de energia gasta ao golpear com uma arma",
    "{}%% gear change speed": "{}%% de velocidade para trocar marcha",
    "{}%% top speed": "{}%% de velocidade máxima",
    "{}%% engine noise in reverse": "{}%% de ruído do motor em marcha à ré",
    "{}%% acceleration": "{}%% de aceleração",
    "{}%% reverse acceleration": "{}%% de aceleração em marcha à ré",
    "capped at {} max speed": "velocidade máxima limitada a {}",
    "engine noise unchanged": "o ruído do motor não muda",
    "less likely to fail any fence climb": "erra menos ao escalar qualquer cerca",
    "slightly faster rope climbing": "sobe cordas um pouco mais rápido",
    "bloody items transfer faster but cause stress": "move itens ensanguentados mais rápido, mas isso causa estresse",
    "cannot read anything, map labels and calorie counts included":
        "não consegue ler nada, nem rótulos do mapa nem calorias",
    "{} panic per tick indoors, scaling down to {} in a {}-tile room":
        "{} de pânico por tick em ambientes fechados, caindo até {} numa sala de {} blocos",
    "a vehicle counts as a {}-tile room": "um veículo conta como uma sala de {} blocos",
    "{} panic per tick whenever you are not in a room": "{} de pânico por tick sempre que você não estiver numa sala",
    "faster building": "constrói mais rápido",
    "faster barricading": "barrica mais rápido",
    "no bonus health on constructions in B{}": "no B{} não dá resistência extra às construções",
    "recipes need one level less of their skill": "as receitas pedem um nível a menos da habilidade",
    "you gain weight above {} calories a day instead of {}, while under {} weight":
        "você engorda acima de {} calorias por dia em vez de {}, enquanto estiver abaixo de {} de peso",
    "you need {} calories a day to gain weight instead of {}, while over {} weight":
        "você precisa de {} calorias por dia para engordar em vez de {}, enquanto estiver acima de {} de peso",
    "unhappiness and stress rise as nicotine withdrawal builds":
        "a infelicidade e o estresse sobem conforme a abstinência de nicotina cresce",
    "smoking clears the withdrawal and gives {} hunger": "fumar corta a abstinência e dá {} de fome",
    "random coughs and sneezes give you away": "tosses e espirros aleatórios te entregam",
    "shows calories, carbohydrates, protein and fat on every food":
        "mostra calorias, carboidratos, proteínas e gorduras em qualquer comida",
    "no measurable effect in B{}: no XP boost, no recipes, and nothing in the game's code reads it. The recipes come from the profession itself.":
        "sem efeito mensurável no B{}: sem bônus de XP, sem receitas, e nenhum ponto do código do jogo o consulta. As receitas vêm da própria profissão.",
    "x{} move speed through trees (x{} for everyone else)": "x{} de velocidade entre árvores (x{} para todos os outros)",
    "starts every exercise at {}{} regularity instead of {}{}":
        "começa cada exercício com regularidade {}{} em vez de {}{}",
    '{} move speed':
        '{} de velocidade de movimento',
    '{} wind penalty when aiming':
        '{} de penalidade de vento ao mirar',
    '%1 °C':
        '%1 °C',
    'Adds rows to the inventory tooltip: how fast a line wears out, how much each hook helps and which fish a bait attracts.':
        'Adiciona linhas ao tooltip do inventário: com que rapidez a linha se desgasta, quanto cada anzol ajuda e quais peixes cada isca atrai.',
    'ALLTHEINFO':
        'ALLTHEINFO',
    'Attracts':
        'Atrai',
    "Back to vanilla's rules: Time needs Fishing {}, Temperature {}, Weather {}, Wind {}, and a species tells you nothing until you have caught it.":
        'De volta às regras do jogo: a hora exige Pesca {}, a temperatura {}, o clima {}, o vento {}, e uma espécie não diz nada até você tê-la pescado.',
    'Best baits: %1':
        'Melhores iscas: %1',
    'Bite chance':
        'Chance de fisgada',
    'Breaks into':
        'Quebra em',
    'Chance that one attempt hooks something: {}%% times temperature, weather, time, hook and abundance, capped at {}%%.':
        'Chance de uma tentativa fisgar algo: {}%% vezes temperatura, clima, hora, anzol e abundância, limitado a {}%%.',
    'Fish bite more at dawn and dusk: x{} from {}:{} to {}:{} and from {}:{} to {}:{}. Any other hour is x{}.':
        'Os peixes mordem mais ao amanhecer e ao anoitecer: x{} das {}:{} às {}:{} e das {}:{} às {}:{}. Em qualquer outra hora é x{}.',
    'Fishing gear: rods, lines, hooks and baits':
        'Equipamento de pesca: varas, linhas, anzóis e iscas',
    'Fishing panel: what each rating is worth':
        'Painel de pesca: quanto vale cada avaliação',
    "Fishing: keep vanilla's Fishing level requirements":
        'Pesca: manter as exigências de nível de Pesca do jogo',
    'Hook':
        'Anzol',
    'How much longer than the best possible case you wait between attempts. Fishing near the shore doubles it, and a bobber less than {} tiles away triples it.':
        'Quanto mais você espera entre tentativas em comparação com o melhor caso possível. Pescar perto da margem dobra a espera, e uma boia a menos de {} tiles a triplica.',
    'Lake':
        'Lago',
    'Line strength':
        'Resistência da linha',
    'Moodles: description box that fits its text':
        'Moodles: caixa de descrição do tamanho do texto',
    'Needs Fishing %1':
        'Exige Pesca %1',
    'Only bites while you reel in':
        'Só morde enquanto você recolhe a linha',
    'Paperclip x{}, nail x{}, fishing hook x{}. With no hook the chance is x{}: nothing will ever bite.':
        'Clipe de papel x{}, prego x{}, anzol de pesca x{}. Sem anzol a chance é x{}: nada morde nunca.',
    'Rain is x{}. Fog over {} or wind over {} is x{}. Fog and wind are the same x{}: they never stack.':
        'Chuva é x{}. Névoa acima de {} ou vento acima de {} é x{}. Névoa e vento são o mesmo x{}: nunca se somam.',
    'Right-click water and pick Fishing. Puts the real multiplier next to Time, Temperature, Weather and Wind, adds hook, spot, bite chance and waiting time, and explains each one on hover.':
        'Clique com o botão direito na água e escolha Pescar. Põe o multiplicador real ao lado de hora, temperatura, clima e vento, adiciona anzol, local, chance de fisgada e espera, e explica cada um ao passar o mouse.',
    'River':
        'Rio',
    'Spot':
        'Local',
    "The game's own moodle box is two lines tall and cuts off anything longer, which is most of AllTheInfo's descriptions. This draws the moodle column itself so the box grows with the text. Turn it off to go back to the vanilla widget.":
        'A caixa de moodle do jogo tem duas linhas de altura e corta tudo que for maior, que é quase toda descrição do AllTheInfo. Aqui a coluna de moodles é desenhada pelo mod, então a caixa cresce com o texto. Desligue para voltar ao widget do jogo.',
    'Trophy from %1 cm, Fishing {} and a {} in {} roll on a big catch':
        'Troféu a partir de %1 cm, com Pesca {} e uma rolagem de {} em {} numa captura grande',
    'Under {} fish is x{}, up to {} is x{}, over {} is x{}. Trash is what you pull out instead of a fish, and Fishing {} cuts it to {}%%, level {} to {}%% and level {} to {}%%.':
        'Menos de {} peixes é x{}, até {} é x{}, mais de {} é x{}. Lixo é o que você puxa no lugar de um peixe, e Pesca {} reduz para {}%%, nível {} para {}%% e nível {} para {}%%.',
    'Up to %1 cm and %2 kg':
        'Até %1 cm e %2 kg',
    'Vanilla draws condition, insulation, wind, water, blood, dirt and wetness as bars with no figures. This writes the figures next to them and adds the discomfort value, which vanilla never shows at all. The run and combat speed modifiers get a signed figure too, which vanilla only ever draws as a bar with no sign.':
        'O jogo desenha condição, isolamento, vento, água, sangue, sujeira e umidade como barras sem números. Aqui os números vão ao lado, mais o valor de desconforto, que o jogo nunca mostra. Os modificadores de velocidade de corrida e de combate também ganham número com sinal, que o jogo só desenha como barra sem sinal.',
    'Wait':
        'Espera',
    'Waters: %1':
        'Águas: %1',
    'Wear per tug':
        'Desgaste por puxada',
    'Wind has no coefficient of its own. Over {} it sets the weather to x{}, the same penalty fog sets, and the two do not add up.':
        'O vento não tem coeficiente próprio. Acima de {} ele deixa o clima em x{}, a mesma penalidade da névoa, e os dois não se somam.',
    'With your bait: %1%%':
        'Com sua isca: %1%%',
    'Your bait does not attract this one':
        'Sua isca não atrai esta espécie',
    'best possible':
        'o melhor possível',
    'near shore':
        'perto da margem',
    'no fish in this spot':
        'aqui não há peixes',
    'none':
        'nenhum',
    'trash':
        'lixo',
    '{} to {} °C is x{}. From {} to {} and from {} to {}, x{}. Over {} or below {}, x{}. Below {} °C, x{}.':
        'De {} a {} °C é x{}. De {} a {} e de {} a {}, x{}. Acima de {} ou abaixo de {}, x{}. Abaixo de {} °C, x{}.',
    'Fish':
        'Peixes',
    'Trash':
        'Lixo',
    'Trophy from %1 cm':
        'Troféu a partir de %1 cm',
    'shore':
        'margem',
    'Best baits:':
        'Melhores iscas:',
    'Size: %1-%2 cm, %3-%4 kg':
        'Tamanho: %1-%2 cm, %3-%4 kg',
    'Trophy: >%1 cm / >%2 kg':
        'Troféu: >%1 cm / >%2 kg',
    'Under {} fish is x{}, up to {} is x{}, over {} is x{}. Fish schools move every day. Trash is what you pull out instead of a fish: it is fixed per spot, and Fishing {} cuts it to {}%%, level {} to {}%% and level {} to {}%%.':
        'Menos de {} peixes é x{}, até {} é x{}, mais de {} é x{}. Os cardumes mudam de lugar todo dia. Lixo é o que você puxa no lugar de um peixe: é fixo por local, e Pesca {} reduz para {}%%, nível {} para {}%% e nível {} para {}%%.',
    'Fishing gear: hide the combat stats':
        'Equipamento de pesca: esconder os dados de combate',
    "Fog over {}%% sets the weather to x{}, the same penalty wind sets, and the two never stack. Vanilla's Weather row reports neither: it says Good for rain even in a gale.":
        'Névoa acima de {}%% deixa o clima em x{}, a mesma penalidade do vento, e os dois nunca se somam. A linha de clima do jogo não informa nenhum dos dois: diz Bom pela chuva mesmo com vendaval.',
    'Rain is x{}. Fog over {}%% or wind over {}%% is x{}. Fog and wind are the same x{}: they never stack.':
        'Chuva é x{}. Névoa acima de {}%% ou vento acima de {}%% é x{}. Névoa e vento são o mesmo x{}: nunca se somam.',
    "Rods, nets and fishing spears are weapons in the game's own scripts, so they get crit chance, swing type, attack speed and knockback. This drops that block on fishing gear. The condition and damage bars are drawn by the game in one call and cannot be removed by any mod.":
        'Varas, redes e lanças de pesca são armas nos próprios scripts do jogo, então recebem chance de crítico, tipo de golpe, velocidade de ataque e empurrão. Isto remove esse bloco no equipamento de pesca. As barras de condição e dano são desenhadas pelo jogo em uma única chamada e nenhum mod consegue removê-las.',
    'Wind has no coefficient of its own. Over {}%% it sets the weather to x{}, the same penalty fog sets, and the two do not add up.':
        'O vento não tem coeficiente próprio. Acima de {}%% ele deixa o clima em x{}, a mesma penalidade da névoa, e os dois não se somam.',
    'Against the best possible case':
        'Em relação ao melhor caso possível',
    'Any other hour: x{}':
        'Qualquer outra hora: x{}',
    'Below {} °C: x{}':
        'Abaixo de {} °C: x{}',
    'Bobber under {} tiles away: x{}':
        'Boia a menos de {} tiles: x{}',
    'Capped at {}%%':
        'Limitado a {}%%',
    'Fishing hook: x{}':
        'Anzol de pesca: x{}',
    'Fishing {}, {} and {} cut trash to {}%%, {}%% and {}%%':
        'Pesca {}, {} e {} reduzem o lixo para {}%%, {}%% e {}%%',
    'Fog and wind never stack':
        'Névoa e vento nunca se somam',
    'Fog over {}%% or wind over {}%%: x{}':
        'Névoa acima de {}%% ou vento acima de {}%%: x{}',
    'Nail: x{}':
        'Prego: x{}',
    'Near shore: x{}':
        'Perto da margem: x{}',
    'No hook: x{}, nothing ever bites':
        'Sem anzol: x{}, nada morde nunca',
    'Over {} or below {} °C: x{}':
        'Acima de {} ou abaixo de {} °C: x{}',
    'Over {}%%: x{} on the weather':
        'Acima de {}%%: x{} no clima',
    'Over {}: x{}':
        'Acima de {}: x{}',
    'Paperclip: x{}':
        'Clipe de papel: x{}',
    'Rain: x{}':
        'Chuva: x{}',
    'Rolled once per attempt':
        'Rolado uma vez por tentativa',
    'Same penalty as fog, they never stack':
        'A mesma penalidade da névoa, nunca se somam',
    'Same penalty as wind, they never stack':
        'A mesma penalidade do vento, nunca se somam',
    'Schools move every day':
        'Os cardumes mudam de lugar todo dia',
    'This row reports neither':
        'Esta linha não informa nenhum dos dois',
    'Trash is fixed per spot':
        'O lixo é fixo por local',
    'Under {} fish: x{}':
        'Menos de {} peixes: x{}',
    '{} to {} and {} to {} °C: x{}':
        'De {} a {} e de {} a {} °C: x{}',
    '{} to {} °C: x{}':
        'De {} a {} °C: x{}',
    '{} to {}: x{}':
        'De {} a {}: x{}',
    '{}%% x temperature x weather x time x hook x fish':
        '{}%% x temperatura x clima x hora x anzol x peixes',
    '{}:{} to {}:{} and {}:{} to {}:{}: x{}':
        'Das {}:{} às {}:{} e das {}:{} às {}:{}: x{}',
    'Fishing {}, {} and {}: trash x{}, x{}, x{}':
        'Pesca {}, {} e {}: lixo x{}, x{}, x{}',
    'x time x hook x fish':
        'x hora x anzol x peixes',
    '{}%% x temperature x weather':
        '{}%% x temperatura x clima',

    # Round 11: moodles rewritten from bytecode + wiki
    "melee damage {}%%": "{}%% de dano corpo a corpo",
    "melee damage {}": "{} de dano corpo a corpo",
    "move speed {}%%": "{}%% de velocidade de movimento",
    "move speed {}%% with Adrenaline Junkie": "{}%% de velocidade com Viciado em Adrenalina",
    "attack speed {}%%": "{}%% de velocidade de ataque",
    "combat speed {}%%": "{}%% de velocidade em combate",
    "run speed {}%%": "{}%% de velocidade de corrida",
    "crit chance {}%%": "{}%% de chance de crítico",
    "firearm accuracy {}%%": "{}%% de precisão com arma de fogo",
    "firearm accuracy {}%% at {} tiles": "{0}%% de precisão com arma de fogo a {1} blocos",
    "clearing a jam {}%%": "{}%% de chance de destravar a arma",
    "climbing {}%%": "{}%% para escalar",
    "climbing fences {}%%": "{}%% para pular cercas",
    "climbing walls and ropes {}%%": "{}%% para escalar muros e cordas",
    "tripping over fences {}%%": "{}%% de chance de tropeçar em cercas",
    "blocking an attack {}%%": "{}%% para bloquear um ataque",
    "foraging {}%%": "{}%% de coleta",
    "carry capacity {}": "{} de capacidade de carga",
    "healing {}%%": "{}%% de cura",
    "healing x{}": "cura x{}",
    "poison wears off {}%% faster": "O veneno passa {}%% mais rápido",
    "heat dissipation {}%%": "{}%% de dissipação de calor",
    "heat loss {}%%": "{}%% de perda de calor",
    "discomfort {}%%": "{}%% de desconforto",
    "medicine {}%% less effective": "Remédios {}%% menos eficazes",
    "sleep {}{}%% less effective": "Sono {0}{1}%% menos eficaz",
    "panic x{} per wound": "pânico x{} por ferimento",
    "over {}%% of capacity": "Acima de {}%% da sua capacidade",
    "health under {}%%": "Vida abaixo de {}%%",
    "health {}%% per hour": "{}%% de vida por hora",
    "health drops to {}%%": "A vida cai para {}%%",
    "health drops to {}%%, then to {}%%": "A vida cai para {0}%% e depois para {1}%%",
    "health drops to {}%% when the air is above {} C": "A vida cai para {0}%% quando o ar está acima de {1} C",
    "health drops when the air is below {} C": "A vida cai quando o ar está abaixo de {} C",
    "only heals indoors, dry, under {}%% fatigue and under {}%% hunger and thirst": "Só sara em ambiente fechado, seco, com fadiga abaixo de {}%% e fome e sede abaixo de {}%%",
    "vision cone narrows, cancelling Eagle Eyed": "O cone de visão estreita e cancela Olhos de Águia",
    "{} C colder than the air": "{} C mais frio que o ar",
    "{} wounds bleeding": "{} ferimentos sangrando",
    "{} wounds, or a bleeding neck": "{} ferimentos, ou um no pescoço",
    "no healing": "Sem cura",
    "no natural healing": "Sem cura natural",
    "slower healing": "Cura mais lenta",
    "much slower healing": "Cura muito mais lenta",
    "slower endurance recovery": "Estamina se recupera mais devagar",
    "much slower endurance recovery": "Estamina se recupera muito mais devagar",
    "endurance barely recovers": "A estamina quase não se recupera",
    "endurance drains as you move and never recovers": "A estamina cai ao se mover e não se recupera",
    "no sprinting or running": "Sem sprint e sem corrida",
    "you cannot run": "Você não consegue correr",
    "you cannot sleep": "Você não consegue dormir",
    "you cannot eat any more": "Você não consegue comer mais",
    "you can sleep on the ground and through pain": "Você consegue dormir no chão e com dor",
    "cannot swing a sledgehammer": "Sem marreta",
    "hunger does not rise": "A fome não sobe",
    "less body heat generated": "Menos calor corporal gerado",
    "body heat rises": "A temperatura corporal sobe",
    "body heat rises sharply": "A temperatura corporal sobe muito",
    "thirst and fatigue rise faster": "Sede e fadiga sobem mais rápido",
    "you lose heat in the cold": "Você perde calor no frio",
    "more likely to catch a cold": "Mais chance de pegar um resfriado",
    "more likely to fall ill": "Mais chance de ficar doente",
    "much more likely to fall ill": "Muito mais chance de ficar doente",
    "narrower vision cone": "Cone de visão mais estreito",
    "narrower vision and awareness": "Visão e percepção reduzidas",
    "movement, damage and attack speed drop with the wound": "Movimento, dano e velocidade de ataque caem conforme o ferimento",
    "you make noise": "Você faz barulho",
    "you complain out loud": "Você reclama em voz alta",
    "you get up faster": "Você se levanta mais rápido",
    "you weave as you walk": "Você anda cambaleando",
    "timed actions take longer": "As ações demoram mais",
    "unhappiness rises": "A infelicidade sobe",
    "unhappiness rises slowly": "A infelicidade sobe devagar",
    "unhappiness rises fast": "A infelicidade sobe rápido",
    "stress rises": "O estresse sobe",
    "boredom is wiped and held down": "O tédio é zerado e não sobe",
    "the Desensitized trait cancels it": "O traço Insensível anula isso",
    "no effect until NPCs return": "Sem efeito até os NPCs voltarem",
    "discomfort while in a vehicle": "Desconforto dentro de um veículo",
    "hypothermia is hidden": "A hipotermia fica escondida",
    "it wakes you up": "Isso te acorda",
    "you sneeze now and then": "Você espirra de vez em quando",
    "you sneeze and cough often": "Você espirra e tosse com frequência",
    "you cough so much that hiding gets hard": "Você tosse tanto que fica difícil se esconder",
    "you cough constantly and draw zombies": "Você tosse sem parar e atrai zumbis",
    "health loss": "Perda de vida",
    "slow health loss": "Perda de vida lenta",
    "serious health loss": "Perda de vida séria",
    "health slowly drops": "A vida cai devagar",
    "health drops if this is infection or poison": "A vida cai se for infecção ou veneno",
    "death without first aid": "Morte sem primeiros socorros",
    "sickness starts to build": "A doença começa a subir",
    "sickness builds noticeably": "A doença sobe de forma perceptível",
    "many rotting corpses": "Muitos cadáveres apodrecendo",
    "more rotting corpses": "Mais cadáveres apodrecendo",
    "the worst corpses can do": "O pior que cadáveres causam",
    "a generator running indoors": "Um gerador ligado dentro de casa",
    "it will not kill you outright": "Isso não te mata na hora",
    "a gas mask or SCBA prevents it": "Uma máscara de gás ou SCBA evita isso",
    "caused by heavy clothing, bags, bare feet or leg injuries": "Causado por roupas pesadas, bolsas, pés descalços ou pernas feridas",

    # Animals (round 10, block C)
    "Animals: butchering yield, milk, wool and old age":
        "Animais: rendimento de carne, leite, lã e velhice",
    "Adds rows to the animal window you get by right-clicking an animal: meat yield, blood, feathers, old age and weight ceiling, which no screen shows, plus health, hunger, thirst, attitude, milk, wool and pregnancy as numbers instead of words.":
        "Adiciona linhas à janela do animal que aparece ao clicar com o botão direito: rendimento de carne, sangue, penas, velhice e peso máximo, que nenhuma tela mostra, além de saúde, fome, sede, atitude, leite, lã e gravidez como números em vez de palavras.",
    "Animals: keep vanilla's Animal Care level requirements":
        "Animais: manter as exigências de nível de Cuidados com Animais do jogo",
    "Off by default, so you see everything from level {}. Turn it on and each row reappears at the Animal Care level vanilla itself uses for it: pregnancy at {}, weight at {}, attitude at {}.":
        "Desligado por padrão, então você vê tudo desde o nível {}. Ligue e cada linha volta a aparecer no nível de Cuidados com Animais que o próprio jogo usa: gravidez em {}, peso em {}, atitude em {}.",
    "Meat yield":
        "Rendimento de carne",
    "full in %1":
        "cheio em %1",

    # Animal hover descriptions (round 12)
    "Size x meat gene.":
        "Tamanho x gene de carne.",
    "Multiplies the number of meat pieces and the calories of each one.":
        "Multiplica o número de pedaços de carne e as calorias de cada um.",
    "Butchering adds x{} every {} levels.":
        "Açougue soma x{} a cada {} níveis.",
    "Off the ground x{}, on a butcher hook x{}.":
        "No chão x{}, no gancho de açougueiro x{}.",
    "Litres you can drain into a bucket once it is dead.":
        "Litros que você pode tirar num balde depois de morto.",
    "Grows with weight.":
        "Cresce com o peso.",
    "Feathers you get for butchering it.":
        "Penas que você recebe ao esquartejá-lo.",
    "Breed maximum x size.":
        "Máximo da raça x tamanho.",
    "{}%% until {}%% of its life expectancy, then it climbs to {}%%.":
        "{}%% até {}%% da expectativa de vida, depois sobe até {}%%.",
    "Over {}%% it loses {}%% health every hour.":
        "Acima de {}%% perde {}%% de saúde por hora.",
    "Current weight and the most this animal can reach.":
        "Peso atual e o máximo que este animal alcança.",
    "Meat and blood both scale with it.":
        "A carne e o sangue acompanham esse valor.",
    "Over {}%% hunger it starts losing weight.":
        "Com fome acima de {}%% começa a perder peso.",
    "{}{}, how much this animal puts up with you.":
        "{}{}, quanto este animal te tolera.",
    "Each point takes {} off the chance it breaks free while being sheared.":
        "Cada ponto reduz em {} a chance de ele se soltar na tosquia.",
    "Every gain is {}, plus {} per Animal Care level.":
        "Cada ganho vale {}, mais {} por nível de Cuidados com Animais.",
    "Healthy over {}%%, off colour over {}%%, sickly over {}%%, dying below.":
        "Saudável acima de {}%%, indisposto acima de {}%%, doente acima de {}%%, morrendo abaixo.",
    "Higher is worse.":
        "Quanto mais alto, pior.",
    "Well fed under {}%%, underfed under {}%%, starving over it.":
        "Bem alimentado abaixo de {}%%, mal alimentado abaixo de {}%%, faminto acima.",
    "Over {}%% it starts losing weight.":
        "Acima de {}%% começa a perder peso.",
    "Fully watered under {}%%, thirsty under {}%%, dying of thirst over it.":
        "Hidratado abaixo de {}%%, com sede abaixo de {}%%, morrendo de sede acima.",
    "{}{}. Calm under {}, unnerved under {}, agitated under {}, wild over it.":
        "{}{}. Calmo abaixo de {}, inquieto abaixo de {}, agitado abaixo de {}, selvagem acima.",
    "Over {} milk and wool grow at {} / stress of their rate.":
        "Acima de {}, leite e lã crescem a {} / estresse do ritmo normal.",
    "Over {} a pregnancy can be lost.":
        "Acima de {} a gravidez pode se perder.",
    "Milking with stress over {} and Animal Care {} or less always fails and spills the bucket.":
        "Ordenhar com estresse acima de {} e Cuidados com Animais {} ou menos falha sempre e derruba o balde.",
    "Litres in the udder and what it holds.":
        "Litros na teta e quanto ela cabe.",
    "It fills by capacity / {} per game hour, times the sandbox milk modifier.":
        "Enche em capacidade / {} por hora de jogo, vezes o modificador de leite do sandbox.",
    "Stress over {} slows it down.":
        "Estresse acima de {} deixa isso mais lento.",
    "Wool grown and the maximum.":
        "Lã acumulada e o máximo.",
    "It grows by maximum / {} per game hour: {} days for a full fleece.":
        "Cresce em máximo / {} por hora de jogo: {} dias para um velo completo.",
    "Days left before it gives birth.":
        "Dias que faltam para o parto.",
    "Stress over {} can end the pregnancy.":
        "Estresse acima de {} pode acabar com a gravidez.",
    "Hours this female stays fertilised.":
        "Horas que esta fêmea continua fertilizada.",
    "When it runs out she is no longer fertilised.":
        "Quando acabam, ela deixa de estar fertilizada.",

    # Wounds and healing
    "Wounds: how long each one still needs":
        "Ferimentos: quanto falta para cada um",
    "Adds an Info entry under the treatments you get by clicking a body part in the health panel. Hover it and the box beside it gives the time left on every wound, what bandaging or a poultice would save, how long the bandage lasts and whether the part is mending or getting worse. The game knows all of it and only prints it in debug mode.":
        "Adiciona uma entrada Informações abaixo dos tratamentos que aparecem ao clicar em uma parte do corpo na tela de saúde. Ao passar o cursor, o quadro ao lado dá o tempo restante de cada ferimento, o que um curativo ou uma cataplasma economizaria, quanto dura o curativo e se a parte está sarando ou piorando. O jogo sabe tudo isso e só imprime no modo de depuração.",
    "Wounds: keep vanilla's Doctor level requirements":
        "Ferimentos: manter as exigências de nível de Primeiros Socorros do jogo",
    "Off by default, so you see everything from level {}. Turn it on and each row reappears at the Doctor level vanilla itself uses for it: scratches and lacerations at {}, deep wounds and splints at {}, fractures and stitches at {}, wound infection at {}.":
        "Desligado por padrão, então você vê tudo desde o nível {}. Ligue e cada linha volta a aparecer no nível de Primeiros Socorros que o próprio jogo usa: arranhões e lacerações em {}, ferimentos profundos e talas em {}, fraturas e pontos em {}, infecção do ferimento em {}.",
    "Full recovery":
        "Recuperação completa",
    "Getting worse":
        "Piorando",
    "Healing":
        "Cura",
    "normal":
        "normal",
    "slowed by hunger, thirst or illness":
        "reduzida por fome, sede ou doença",
    "stopped by hunger or thirst":
        "parada por fome ou sede",
    "asleep, ten times faster":
        "dormindo, dez vezes mais rápida",
    "wounded parts share it":
        "partes feridas dividem entre si",
    "Bandage life":
        "Duração do curativo",
    "ready to remove":
        "prontos para remover",

    # Wounds and healing, redesigned tooltip
    "Healing speed":
        "Velocidade de cura",
    "clean for":
        "limpo por",
    "Poultice":
        "Cataplasma",
    "Wound infection":
        "Infecção do ferimento",
    "won't close, glass inside":
        "não fecha, há vidro dentro",
    "won't close while unbandaged":
        "não fecha sem curativo",
    "rising":
        "subindo",

    # Wounds: shorter recovery label and infection risk
    "Recovery":
        "Recuperação",
    "Infection risk":
        "Risco de infecção",

    # Percentages, ported from the multiplier wording
    "{}%% weapon damage": "{}%% de dano da arma",
    "{}%% endurance recovery": "{}%% de recuperação de energia",
    "{}%% melee damage and knockback": "{}%% de dano corpo a corpo e empurrão",
    "{}%% move speed in combat stance": "{}%% de velocidade em postura de combate",
    "{}%% sprint speed": "{}%% de velocidade de corrida rápida",
    "{}%% chance of being spotted": "{}%% de chance de ser notado",
    "{}%% footstep noise": "{}%% de barulho dos passos",
    "{}%% recoil delay": "{}%% de atraso do recuo",
    "{}%% aim settling speed": "{}%% de velocidade para estabilizar a mira",
    "{}%% aim penalty for moving (shared with Nimble)":
        "{}%% de penalidade de mira por se mover (dividida com Agilidade)",
    "{}%% reload speed": "{}%% de velocidade de recarga",
    "{}%% racking speed": "{}%% de velocidade para engatilhar",
    "{}%% XP in every Crafting skill": "{}%% de XP em todas as habilidades de Fabricação",
    "{}%% move speed through trees": "{}%% de velocidade entre árvores",
    "spotting another player {}%%": "{}%% para avistar outro jogador",
    "timed actions {}%%": "ações levam {}%%",
    "endurance drain {}%%": "{}%% de gasto de estamina",
    "alcohol hits {}%%, and {}%% over {}%% hunger":
        "O álcool bate {0}%%, e {1}%% acima de {2}%% de fome",
    "Fitness {}, which is {}%% endurance recovery instead of {}%%":
        "Preparo Físico {}, ou seja {}%% de recuperação de energia em vez de {}%%",
    "{}%% attack speed": "{}%% de velocidade de ataque",
    "{}%% crit chance": "{}%% de chance de crítico",
    "racking costs {}%% of the aiming time": "engatilhar custa {}%% do tempo de mira",
    "carrying capacity {}": "capacidade de carga {}",
    "{} to every weapon's durability roll.": "{} na rolagem de durabilidade de qualquer arma.",
    "Condition loss (handle)": "Perda de condição (cabo)",
    "Condition loss (head)": "Perda de condição (cabeça)",

    # Ronda 4: medicine, traps, weapon components, skill levels
    '%1 corpses nearby': '%1 cadáveres por perto',
    '%1%% attack time': '%1%% de velocidade de ataque',
    '%1%% crit chance': '%1%% de chance de crítico',
    '%1%% muscle strain': '%1%% de fadiga muscular',
    '%1%% weapon damage': '%1%% de dano da arma',
    '+%1 to the durability roll': '+%1 na rolagem de durabilidade',
    'Adds an Info entry to a placed trap: the odds of it catching anything in an hour, which animals it can take and the share of the catch each one gets, the bait and its freshness, the zone, the hourly odds of losing bait or trap, and the warning that a trap catches nothing while you stand next to it. Bait foods get a row naming what they attract.': 'Adiciona uma entrada Info a uma armadilha colocada: a chance de ela pegar alguma coisa em uma hora, quais animais ela pode pegar e a parcela da captura que cabe a cada um, a isca e seu frescor, a zona, as chances por hora de perder a isca ou a armadilha, e o aviso de que uma armadilha não pega nada enquanto você está ao lado. Alimentos que servem de isca ganham uma linha dizendo o que atraem.',
    'Bait': 'Isca',
    'Bait lost per hour': 'Isca perdida por hora',
    'In the trap for': 'Na armadilha há',
    'Filter left': 'Filtro restante',
    'Hits before it breaks': 'Golpes até quebrar',
    'Medicine: duration, delay and effect': 'Remédios: duração, espera e efeito',
    'Medicine: the full list of effects': 'Remédios: a lista completa de efeitos',
    'Muscle strain per hit': 'Fadiga muscular por golpe',
    'Off by default, so you see everything from level {}. Turn it on and the trap tooltip only appears from Trapping {}, which is the level vanilla itself uses elsewhere.': 'Desligado por padrão, então você vê tudo a partir do nível {}. Ao ligar, a dica da armadilha só aparece a partir de Armadilhas {}, que é o nível que o próprio jogo usa em outros lugares.',
    'Off by default. Adds everything else each pill does: what cancels it, what intoxication costs it, and the sleeping tablet overdose table.': 'Desligado por padrão. Adiciona tudo o mais que cada comprimido faz: o que o cancela, quanto a embriaguez lhe custa e a tabela de overdose dos soníferos.',
    'Painkillers, beta blockers, antidepressants, sleeping tablets and antibiotics get how long they last, how long they take to start and what they do per minute. Every figure is recomputed from the sandbox day length.': 'Analgésicos, betabloqueadores, antidepressivos, soníferos e antibióticos mostram quanto duram, quanto demoram para agir e o que fazem por minuto. Cada valor é recalculado a partir da duração do dia do sandbox.',
    'Prey': 'Presas',
    'Rots once thawed': 'Apodrece ao descongelar',
    'Stale once thawed': 'Fica velho ao descongelar',
    'Takes effect in': 'Faz efeito em',
    'Trap lost per hour': 'Armadilha perdida por hora',
    'Traps: catch odds, bait and hours': 'Armadilhas: chances de captura, isca e horários',
    "Traps: keep vanilla's Trapping level requirements": 'Armadilhas: manter as exigências de nível de Armadilhas do jogo',
    'Zone': 'Zona',
    'a second dose resets the clock, it does not add': 'uma segunda dose reinicia o relógio, ela não soma',
    'a third of the strength above {} intoxication': 'um terço da força acima de {} de embriaguez',
    'fresh for %1': 'fresca por %1',
    'half the strength above {} intoxication': 'metade da força acima de {} de embriaguez',
    'each pill counts double above {} intoxication': 'cada comprimido conta em dobro acima de {} de embriaguez',
    'holds the fever, does not cure it': 'segura a febre, não a cura',
    'incoming panic {}%% per pill, down to nothing': 'pânico recebido {}%% por comprimido, até zerar',
    'it catches nothing while you are near it': 'ela não pega nada enquanto você estiver perto',
    'only the first dose has to wait': 'só a primeira dose precisa esperar',
    'overdose: {} pills cost {} health, {} cost {}, {} kill': 'overdose: {} comprimidos custam {} de vida, {} custam {}, {} matam',
    'sleeping cancels the effect': 'dormir cancela o efeito',
    'stale, catches nothing': 'velha, não atrai nada',
    'the longer it waits, the likelier it comes out dead': 'quanto mais esperar, mais provável que saia morto',
    'to full in %1': 'ao máximo em %1',
    'to zero in %1': 'a zero em %1',
    'wound pain stops being recalculated while it lasts': 'a dor das feridas deixa de ser recalculada enquanto dura',
    'zombie fever held': 'febre zumbi contida',
    '{}%% reading time': '{}%% de tempo de leitura',
    'Effect': 'Efeito',

    # Ronda 4, segunda pasada
    '%1 s': '%1 s',
    '%1 s per round': '%1 s por bala',
    '%1%% attack speed': '%1%% de velocidade de ataque',
    'Details': 'Detalhes',
    'Info': 'Info',
    'Possible prey': 'Presas possíveis',
    'Trap breaks per hour': 'Armadilha quebra por hora',
    'holds the fever': 'segura a febre',
    'not being used (%1 corpses nearby)': 'não está sendo gasto (%1 cadáveres por perto)',
    'Bird': 'Pássaro',
    'Active hours': 'Horário de atividade',
    'Possible prey, share of the catch': 'Presas possíveis, parcela da captura',
    'Catch chance': 'Chance de captura',
    'Bait condition': 'Estado da isca',
    'Trap condition': 'Estado da armadilha',
    'while you are near it, it neither catches nor breaks': 'enquanto você estiver perto, ela não pega nada nem quebra',
    'Bait loss risk, per hour': 'Risco de perder a isca, por hora',
    'Wrecked by an animal, per hour': 'Destruída por um animal, por hora',
    '%1 / h': '%1 / h',
    'Bait loss risk': 'Risco de perder a isca',
    'Chance of being wrecked': 'Chance de ser destruída',
    'Critical damage': 'Dano crítico',
    'Effective durability': 'Durabilidade efetiva',
    'Damage with your character': 'Dano com seu personagem',
    'Reach (tiles)': 'Alcance (blocos)',

    # Bags and the torch beam (0.9.20)
    'All round': 'Em todas as direções',
    'Beam (degrees)': 'Feixe (graus)',
    'Bags: how much they slow you down': 'Bolsas: o quanto te deixam mais lento',
    "The run and combat speed a bag costs you, which the game applies and never shows. The run figure is the one you are paying right now: a bag's penalty grows by half again as it fills up, so the same pack goes from {}%% empty to {}%% full. It counts the same in your hands as on your back.": 'A velocidade de corrida e de combate que uma bolsa te custa, que o jogo aplica e nunca mostra. O número de corrida é o que você está pagando agora: a penalidade cresce metade de novo conforme a bolsa enche, então a mesma bolsa vai de {}%% vazia a {}%% cheia. Conta igual nas mãos e nas costas.',

    # Trait figures corrected against bytecode (0.9.21)
    "Aiming and Maintenance are not affected":
        "Pontaria e Manutenção não são afetadas",
    "ambient light never drops below {} in the dark":
        "a luz ambiente nunca cai abaixo de {} no escuro",
    "can tell a poisonous wild plant from a safe one":
        "distingue uma planta silvestre venenosa de uma segura",
    "lights a fire with a notched plank twice as fast":
        "acende uma fogueira com tábua entalhada duas vezes mais rápido",
    "no harm at all from tainted water":
        "a água contaminada não causa dano nenhum",
    "{} health on every construction":
        "{} de vida em cada construção",
    "{} tiles of perception instead of {}":
        "{} tiles de percepção em vez de {}",
    "{}%% XP in the six melee weapon skills":
        "{}%% de XP nas seis habilidades de arma corpo a corpo",
    "{}%% chance of tearing your clothes on a tree":
        "{}%% de rasgar a roupa numa árvore",
    "{}%% from any other poison":
        "{}%% de qualquer outro veneno",
    "{}%% from any other poison, bleach aside":
        "{}%% de qualquer outro veneno, exceto água sanitária",
    "{}%% weather penalty in combat":
        "{}%% de penalidade de clima em combate",

    # Per-level lines for the twenty craft skills (0.9.21)
    "%1 crop health at planting":
        "%1 de vida da plantação ao plantar",
    "%1%% chance the crop is cursed if planted out of its month":
        "%1%% de a plantação sair amaldiçoada se plantada fora do mês dela",
    "%1%% chance of a bonus harvest planted in its best month":
        "%1%% de colheita extra se plantada no melhor mês dela",
    "%1 disease removed per treatment":
        "%1 de doença removida por tratamento",
    "%1%% chance of harvesting %2 extra vegetables":
        "%1%% de colher %2 vegetais a mais",
    "%1%% back strain planting and harvesting":
        "%1%% de esforço nas costas ao plantar e colher",
    "%1 points off the chance a stressed animal breaks off milking or shearing":
        "%1 pontos na chance de um animal estressado escapar ao ordenhar ou tosquiar",
    "a stressed animal never breaks off milking or shearing":
        "um animal estressado nunca mais escapa ao ordenhar ou tosquiar",
    "x%1 chance of each extra part off a carcass":
        "x%1 de chance de cada parte extra de uma carcaça",
    "x%1 of each part":
        "x%1 de cada parte",
    "up to %1 blood splatters on you":
        "até %1 respingos de sangue em você",
    "%1 health on everything you build":
        "%1 de vida em tudo o que você construir",
    "%1%% build time":
        "%1%% de tempo de construção",
    "%1%% barricading time":
        "%1%% de tempo para barricar",
    "%1%% chance of recovering material when dismantling":
        "%1%% de recuperar material ao desmontar",
    "%1%% of the ingredient used per addition":
        "%1%% do ingrediente gasto por adição",
    "x%1 nutrients from each ingredient":
        "x%1 de nutrientes de cada ingrediente",
    "rotten food can go in evolved recipes, worth %1%% of its hunger":
        "você pode pôr um pouco de comida podre em receitas evoluídas",
    "x%1 fracture healing with a splint":
        "x%1 de cura de fratura com tala",
    "a bandage lasts %1 to %2 longer":
        "uma bandagem dura de %1 a %2 mais",
    "%1%% time for every medical action":
        "%1%% de tempo em cada ação médica",
    "you can judge how bad a wound is":
        "você sabe avaliar a gravidade de um ferimento",
    "you can read pain, and spot the burns that need washing":
        "você sabe ler a dor e ver quais queimaduras precisam ser lavadas",
    "you can tell when stitches are ready to come out":
        "você sabe quando os pontos podem ser retirados",
    "you spot a wound infection straight away":
        "você percebe na hora que um ferimento está infeccionado",
    "%1%% chance of getting the patch back":
        "%1%% de recuperar o remendo",
    "%1%% time to add or remove a patch":
        "%1%% de tempo para pôr ou tirar um remendo",
    "a hole can be repaired completely, defense and insulation included":
        "um buraco pode ser consertado por completo, defesa e isolamento inclusos",
    "+%1%% generator condition per repair":
        "+%1%% de condição do gerador por reparo",
    "%1 points to the chance of hotwiring a car":
        "%1 pontos na chance de ligar um carro na ignição direta",
    "%1%% chance of setting off the car alarm":
        "%1%% de disparar o alarme do carro",
    "you can salvage and repair a standard engine":
        "você pode desmontar e consertar um motor comum",
    "you can salvage and repair a heavy-duty engine":
        "você pode desmontar e consertar um motor pesado",
    "you can salvage and repair a sport engine":
        "você pode desmontar e consertar um motor esportivo",
    "you can build the sturdier brick wall":
        "você pode construir o muro de tijolos mais resistente",
    "small %1%%, medium %2%%, large %3%%":
        "pequeno %1%%, médio %2%%, grande %3%%",
    "%1 points to the chance a berry or mushroom is poisonous":
        "%1 pontos na chance de uma fruta ou cogumelo ser venenoso",
    "%1%% time to inspect a track":
        "%1%% de tempo para inspecionar um rastro",
    "no effect of its own, this level only unlocks the recipes below":
        "sem efeito próprio, este nível só desbloqueia as receitas abaixo",

    # 0.9.21 follow-up
    "%1 rags when you rip up clothing, capped by the parts it covers":
        "%1 retalhos ao rasgar roupas, limitado pelo que a peça cobre",
    "rotten food can go in evolved recipes, worth %1%% of its hunger":
        "comida podre serve em receitas evoluídas, vale %1%% da fome dela",

    # 0.9.21 follow-up 2
    "%1%% time per litre shearing an animal":
        "%1%% de tempo por litro ao tosquiar um animal",
    "%1 rags when you rip up clothing, capped by the parts it covers":
        "%1 trapos ao rasgar roupas, limitado pelas partes que a peça cobre",
    "%1 to the most aramid thread you can pull out":
        "%1 no máximo de linha de aramida que dá para tirar",
    "starts at {} weight, becomes Emaciated at {} or less and Low Weight above {}":
        "começa com {} de peso, em {} ou menos vira Emaciação e acima de {} vira Abaixo do Peso",
    "starts at {} weight, becomes High Weight below {}":
        "começa com {} de peso, abaixo de {} vira Acima do Peso",
    "starts at {} weight, becomes Very High Weight at {} and is lost below {}":
        "começa com {} de peso, em {} vira Muito Acima do Peso e abaixo de {} se perde",
    "starts at {} weight, becomes Very Low Weight at {} or less and is lost above {}":
        "começa com {} de peso, em {} ou menos vira Muito Abaixo do Peso e acima de {} se perde",
    "XP awarded":
        "XP concedido",
    "{} chance to trip when a zombie lunges through a window":
        "{} de chance de tropeçar quando um zumbi avança por uma janela",
    "{} to the roll that keeps you on your feet when a zombie shoves you":
        "{} na rolagem que te mantém de pé quando um zumbi te empurra",
    "{}%% muscle strain":
        "{}%% de fadiga muscular",
    "{}%% axe attack speed, chopping trees included":
        "{}%% de velocidade de ataque com machado, cortar árvores incluído",

    # B42.20 trait corrections
    "Another x{} at panic level {}":
        "outro x{} com pânico de nível {}",
    "Can hotwire without Electrical {} and Mechanics {}":
        "pode fazer ligação direta sem Eletricidade {} e Mecânica {}",
    "Engine revs three times faster in reverse":
        "o motor sobe de giro três vezes mais rápido em marcha à ré",
    "Halves your rope climbing bonus":
        "reduz à metade seu bônus de escalada em corda",
    "No unhappiness from looting corpses":
        "revistar corpos não causa infelicidade",
    "Stress from handling bloody items":
        "estresse ao manusear itens ensanguentados",
    "{} move speed at panic level {}, {} at level {}":
        "{} de velocidade com pânico de nível {}, {} no nível {}",
    "{} to the rope climbing roll":
        "{} na rolagem de escalada em corda",
    "{}%% acceleration, fading out above {}%% of the car's top speed":
        "{}%% de aceleração, que some acima de {}%% da velocidade máxima do carro",
    "{}%% carry capacity":
        "{}%% de capacidade de carga",
    "{}%% chance of breaking a window lock instead of {}%%":
        "{}%% de quebrar a tranca da janela em vez de {}%%",
    "{}%% endurance cost on every exertion":
        "{}%% da energia que cada esforço custa",
    "{}%% reverse acceleration, gone past {} km/h":
        "{}%% de aceleração em marcha à ré, nula acima de {} km/h",
    "{}%% unhappiness from looting corpses":
        "{}%% de infelicidade ao revistar corpos",

    # Repair recipes
    "Repair: +%1 condition, %2 chance of failing":
        "Reparo: +%1 de condição, %2 de falhar",
    "Repair: +%1 condition, %2 chance of failing, repaired %3 times":
        "Reparo: +%1 de condição, %2 de falhar, reparado %3 vezes",

    # Corpse count and temperature figures
    "Body temperature: the number on every bar":
        "Temperatura corporal: o número em cada barra",
    "Nauseous: how many corpses are making you ill":
        "Náusea: quantos corpos estão te deixando doente",
    "Rotting corpses nearby raise food sickness, and the game never says how many are close enough. Five or fewer do nothing. The count is read back out of the game, so it follows the sandbox setting.":
        "Corpos apodrecendo por perto aumentam a intoxicação alimentar, e o jogo nunca diz quantos estão perto o bastante. Cinco ou menos não fazem nada. A contagem é lida do próprio jogo, então acompanha a opção do sandbox.",
    "The temperature view prints its value on Insulation and Wind resistance and leaves the other nine bars as a colour. This sets the same flag on the rest, so skin temperature, body response, heat and wetness read as figures. Vanilla does the drawing, and only for the body part you have selected.":
        "A vista de temperatura escreve o valor em Isolamento e Resistência ao vento e deixa as outras nove barras como cor. Isto põe a mesma marca no resto, então temperatura da pele, resposta corporal, calor e umidade passam a ser cifras. Quem desenha é o próprio jogo, e só na parte do corpo que você selecionou.",

    # Options tab
    "Custom":
        "Personalizado",
    "Nothing matches that":
        "Nada corresponde a isso",
    "Moodles: how many corpses are making you ill":
        "Moodles: quantos corpos estão te deixando doente",

    # Option groups
    "Every gun this box or magazine fits, one per row.":
        "Cada arma em que esta caixa ou carregador serve, uma por linha.",
    "How bloody the garment is, out of a hundred.":
        "O quanto a peça está ensanguentada, de cem.",
    "How brightly it lights what it reaches.":
        "Com que intensidade ilumina o que alcança.",
    "How dirty the garment is, out of a hundred.":
        "O quanto a peça está suja, de cem.",
    "How drunk this container will get you.":
        "O quanto este recipiente vai te deixar bêbado.",
    "How far the light reaches, in tiles.":
        "Até onde a luz chega, em tiles.",
    "How far the shot is heard, which is how far the horde comes from.":
        "Até onde o tiro é ouvido, ou seja, de onde vem a horda.",
    "How long before the pill starts working, and only while you have none running.":
        "Quanto falta para o comprimido começar a agir, e só enquanto você não tem nenhum agindo.",
    "How long cooked food can stay on the heat before it burns.":
        "Quanto a comida pronta aguenta no fogo antes de queimar.",
    "How long the charge lasts with the thing switched on.":
        "Quanto a carga dura com a coisa ligada.",
    "How long the filter lasts at your current exposure, and how many corpses are around you.":
        "Quanto o filtro dura na sua exposição atual, e quantos cadáveres há em volta de você.",
    "How long the item burns for as fuel.":
        "Quanto tempo o item queima como combustível.",
    "How long the pages you have not read yet will take.":
        "Quanto vão levar as páginas que você ainda não leu.",
    "How long the pill keeps working.":
        "Quanto tempo o comprimido continua fazendo efeito.",
    "How long the plant takes to be ready, at the current farming speed.":
        "Quanto a planta leva para ficar pronta, na velocidade de plantio atual.",
    "How long until the food goes stale, at the current rot speed.":
        "Quanto falta para a comida ficar velha, na velocidade de apodrecimento atual.",
    "How long until the food is rotten, at the current rot speed.":
        "Quanto falta para a comida apodrecer, na velocidade de apodrecimento atual.",
    "How many hits the weapon has left in it, which is the one figure that compares any two weapons.":
        "Quantos golpes a arma ainda tem, que é o único número que compara duas armas quaisquer.",
    "How much cold the garment keeps out. The game only draws a bar.":
        "Quanto frio a peça segura. O jogo só desenha uma barra.",
    "How much is left in the filter.":
        "Quanto resta no filtro.",
    "How much of it you have already heard.":
        "Quanto disso você já ouviu.",
    "How much of the corpse sickness the mask keeps off you. {}%% is immunity.":
        "Quanto da doença de cadáveres a máscara tira de você. {}%% é imunidade.",
    "How much of your hunger bar the drink covers.":
        "Quanto da sua barra de fome a bebida cobre.",
    "How much of your thirst bar the drink covers.":
        "Quanto da sua barra de sede a bebida cobre.",
    "How much pull the rod takes before the line gives.":
        "Quanta força a vara aguenta antes de a linha ceder.",
    "How much rain the garment keeps out. The game only draws a bar.":
        "Quanta chuva a peça segura. O jogo só desenha uma barra.",
    "How much the bag slows you down, with its weight and what is inside counted.":
        "O quanto a mochila te atrasa, contando o peso dela e o que está dentro.",
    "How much the bag slows your swing.":
        "O quanto a mochila atrasa o seu golpe.",
    "How much the garment slows you down, as the penalty itself rather than a bar.":
        "O quanto a peça te atrasa, como a própria penalidade em vez de uma barra.",
    "How much the garment slows your swing, as the penalty itself rather than a bar.":
        "O quanto a peça atrasa o seu golpe, como a própria penalidade em vez de uma barra.",
    "How much tiredness this surface actually clears, your traits included.":
        "Quanto cansaço esta superfície realmente tira, contando as suas características.",
    "How much wind the garment keeps out. The game only draws a bar.":
        "Quanto vento a peça segura. O jogo só desenha uma barra.",
    "How often a hit crits, with your level in the weapon's own skill counted.":
        "Com que frequência um golpe é crítico, contando o seu nível na perícia da própria arma.",
    "How often a shot crits.":
        "Com que frequência um tiro é crítico.",
    "How wet the garment is, out of a hundred.":
        "O quanto a peça está molhada, de cem.",
    "In tiles. A swing landed at the edge of your reach does up to twice the damage of one landed close in.":
        "Em tiles. Um golpe na borda do seu alcance causa até o dobro do dano de um golpe colado.",
    "Off by default: the game only reveals this block for packaged food or a Nutritionist.":
        "Desligado por padrão: o jogo só mostra este bloco em comida embalada ou com Nutricionista.",
    "Rounds in the magazine right now, out of what it holds.":
        "Balas no carregador agora, do total que ele leva.",
    "The calibre the magazine takes.":
        "O calibre que o carregador aceita.",
    "The calories in what is actually in the container, mixtures included.":
        "As calorias do que está de fato no recipiente, misturas incluídas.",
    "The carbohydrates in what is actually in the container.":
        "Os carboidratos do que está de fato no recipiente.",
    "The charge left, as a number instead of a bar.":
        "A carga que resta, como número em vez de barra.",
    "The edge, and the ceiling a worn head puts on it: blunt, the weapon loses the top of its damage range.":
        "O fio, e o teto que uma cabeça gasta impõe: sem fio, a arma perde a parte alta do seu dano.",
    "The exact minimum and maximum. The game only ever draws it as a bar.":
        "O mínimo e o máximo exatos. O jogo só desenha isso como uma barra.",
    "The exact points left, and the head's own count on a weapon that has one.":
        "Os pontos exatos que restam, e a conta separada da cabeça numa arma que tenha uma.",
    "The exact points left, where the game only draws a bar.":
        "Os pontos exatos que restam, onde o jogo só desenha uma barra.",
    "The fat in what is actually in the container.":
        "As gorduras do que está de fato no recipiente.",
    "The fatigue each swing costs you.":
        "A fadiga que cada golpe te custa.",
    "The furthest tile the gun can hit.":
        "O tile mais distante que a arma alcança.",
    "The gun's own hit chance, before your aiming skill.":
        "A chance de acerto da própria arma, antes da sua pontaria.",
    "The hook fitted, and what it does to your odds of a bite.":
        "O anzol montado, e o que ele faz com a sua chance de fisgada.",
    "The line fitted, and how much of it each tug wears away.":
        "A linha montada, e quanto dela cada puxão gasta.",
    "The months it can be sown in, one per row.":
        "Os meses em que dá para semear, um por linha.",
    "The multiplier your shoes put on stomping a downed zombie. Footwear only.":
        "O multiplicador que os seus sapatos dão ao pisotear um zumbi caído. Só calçados.",
    "The multiplier your skill puts on this weapon's swing.":
        "O multiplicador que a sua perícia dá ao golpe desta arma.",
    "The net pace of the pill, which is what compares two of them at a glance.":
        "O ritmo líquido do comprimido, que é o que compara dois deles de relance.",
    "The odds of losing a point of condition on a hit, with Maintenance and the weapon's skill counted.":
        "A chance de perder um ponto de condição por golpe, contando Manutenção e a perícia da arma.",
    "The odds of losing a point of condition per shot.":
        "A chance de perder um ponto de condição por tiro.",
    "The poison the drink carries, and only while the game is willing to tell you.":
        "A chance real de emperrar, desgaste e empunhadura fraca incluídos.",
    "The proteins in what is actually in the container.":
        "As proteínas do que está de fato no recipiente.",
    "The real odds of a jam, wear and a weak grip included.":
        "O veneno que a bebida carrega, e só enquanto o jogo estiver disposto a te contar.",
    "The real seconds a reload takes, with your reloading skill and your panic counted.":
        "Os segundos reais que uma recarga leva, contando a sua perícia de recarga e o pânico.",
    "The real seconds spent lining up the shot, with your aiming skill and your traits counted.":
        "Os segundos reais gastos alinhando o tiro, contando a sua pontaria e as suas características.",
    "The recipes it teaches that you do not know yet, one per row.":
        "As receitas que ele ensina e que você ainda não sabe, uma por linha.",
    "The swing animation, which is what really separates a slow weapon from a fast one.":
        "A animação do golpe, que é o que de fato separa uma arma lenta de uma rápida.",
    "What a critical is worth, from {}%% to {}%% depending on the weapon. The game shows it nowhere.":
        "Quanto vale um crítico, de {}%% a {}%% conforme a arma. O jogo não mostra isso em lugar nenhum.",
    "What feeds the Uncomfortable moodle. The game never shows it on the garment at all.":
        "O que alimenta o moodle de desconforto. O jogo nunca mostra isso na peça.",
    "What is left in your hands when the rod breaks.":
        "O que sobra nas suas mãos quando a vara quebra.",
    "What sleeping here costs you in comfort.":
        "O que dormir aqui te custa em conforto.",
    "What the drink does to boredom and unhappiness, which move together here.":
        "O que a bebida faz com o tédio e a infelicidade, que aqui andam juntos.",
    "What the drink does to your fatigue bar.":
        "O que a bebida faz com a sua barra de fadiga.",
    "What the drink does to your stress.":
        "O que a bebida faz com o seu estresse.",
    "What the food still needs, and the temperature the figure assumes.":
        "O que ainda falta para a comida, e a temperatura que o número assume.",
    "Whether it is a cone you aim or a lamp that lights all around, and how wide the cone is.":
        "Se é um cone que você aponta ou uma lâmpada que ilumina em volta, e quão aberto é o cone.",
    "Which fish this bait brings in.":
        "Quais peixes esta isca atrai.",
    "Which skill the tape or disc trains and how much experience is left in it.":
        "Qual perícia a fita ou o disco treina e quanta experiência ainda resta nele.",
    "Which skill the weapon trains, and therefore which one drives its damage and its speed.":
        "Qual perícia a arma treina, e portanto qual delas move o dano e a velocidade dela.",
    "Your own reading speed, traits, glasses and sitting down included.":
        "A sua própria velocidade de leitura, com características, óculos e estar sentado incluídos.",
    "Nutrition":
        "Nutrição",
    "Sleep":
        "Dormir",
    "How much the bag slows your attack. It multiplies the weapon's own swing speed, not your walking.":
        "O quanto a mochila atrasa o seu ataque. Ela multiplica a velocidade do golpe da própria arma, não o seu andar.",
    "How much the garment slows your attack. It multiplies the weapon's own swing speed, not your walking.":
        "O quanto a peça atrasa o seu ataque. Ela multiplica a velocidade do golpe da própria arma, não o seu andar.",
    "Best baits":
        "Melhores iscas",
    "Every animal this trap can catch and its share of the catch.":
        "Cada animal que esta armadilha pode pegar e a sua fatia da captura.",
    "Feathers":
        "Penas",
    "Fog on a line of its own, because the game lumps it into weather and then reports neither.":
        "A névoa em linha própria, porque o jogo a joga dentro do clima e depois não informa nenhum dos dois.",
    "Glass or a bullet still in the wound, which stops it healing until it is out.":
        "Vidro ou bala ainda dentro do ferimento, que o impede de cicatrizar até sair.",
    "How far the disease has gone, out of a hundred.":
        "O quanto a doença avançou, de cem.",
    "How far the generator is heard, halved when it stands indoors.":
        "Até onde o gerador é ouvido, pela metade quando está sob um teto.",
    "How full the udder is and whether it can be milked yet.":
        "O quanto o úbere está cheio e se já dá para ordenhar.",
    "How hungry the animal is, and how long its feed will last.":
        "A fome do animal, e quanto tempo a ração dele vai durar.",
    "How long before old age starts costing the animal its yield.":
        "Quanto falta para a velhice começar a custar rendimento ao animal.",
    "How long each cut, scratch, burn or bite still needs.":
        "Quanto ainda falta para cada corte, arranhão, queimadura ou mordida.",
    "How long is left of a pregnancy, or of an egg being fertilised.":
        "Quanto falta de uma gestação, ou de um ovo ser fecundado.",
    "How long since the last watering. The game works it out to pick a colour and then never shows it.":
        "Quanto tempo desde a última rega. O jogo calcula isso para escolher uma cor e depois nunca mostra.",
    "How long the bandage lasts before it is dirty and worth changing.":
        "Quanto a bandagem dura antes de ficar suja e valer a troca.",
    "How long the catch has been waiting in there.":
        "Há quanto tempo a captura está esperando ali dentro.",
    "How long the fracture needs, and what the splint on it is worth.":
        "Quanto a fratura precisa, e quanto vale a tala que está nela.",
    "How long the fuel in the tank lasts at the current draw.":
        "Quanto o combustível do tanque dura no consumo atual.",
    "How long the part needs to be whole again, and how fast it is healing.":
        "Quanto a parte precisa para ficar inteira de novo, e a que ritmo está cicatrizando.",
    "How long the stiffness in that limb takes to pass.":
        "Quanto tempo a rigidez naquele membro leva para passar.",
    "How long the stitches need, and when they can come out.":
        "Quanto os pontos precisam, e quando podem sair.",
    "How long until it breaks down for good, on average.":
        "Quanto falta para ele quebrar de vez, em média.",
    "How long until it wears down to the point where it can catch fire.":
        "Quanto falta para ele se desgastar até o ponto em que pode pegar fogo.",
    "How long until the crop moves to its next stage.":
        "Quanto falta para a plantação passar para o próximo estágio.",
    "How long you will wait compared with the best possible spot.":
        "Quanto você vai esperar comparado com o melhor ponto possível.",
    "How many feathers butchering will give.":
        "Quantas penas o abate vai dar.",
    "How many fish this spot still holds, and what that is worth.":
        "Quantos peixes este ponto ainda tem, e quanto isso vale.",
    "How much blood butchering will give.":
        "Quanto sangue o abate vai dar.",
    "How much fertiliser the plot holds. Above one is the too much case in the game's own code.":
        "Quanto fertilizante o canteiro tem. Acima de um é o caso de excesso no código do próprio jogo.",
    "How much meat butchering will give, which is what answers whether it is worth killing yet.":
        "Quanta carne o abate vai dar, que é o que responde se já vale a pena matar.",
    "How much of the bait is still good.":
        "Quanto da isca ainda está boa.",
    "How much the animal trusts you, which is what lets you handle it.":
        "O quanto o animal confia em você, que é o que permite manejá-lo.",
    "How much wool has grown back and whether it can be sheared yet.":
        "Quanta lã voltou a crescer e se já dá para tosquiar.",
    "How stressed the animal is, out of a hundred.":
        "O quanto o animal está estressado, de cem.",
    "How the wound infection is going, and whether it is still rising.":
        "Como vai a infecção do ferimento, e se ainda está subindo.",
    "How thirsty the animal is, and how long its water will last.":
        "A sede do animal, e quanto tempo a água dele vai durar.",
    "Level needed":
        "Nível necessário",
    "Lodged objects":
        "Objetos alojados",
    "Odds with your bait":
        "Chance com a sua isca",
    "Predator":
        "Predador",
    "Size and weight":
        "Tamanho e peso",
    "Strength at the top skill level":
        "Resistência no nível máximo",
    "The Fishing level this species needs before it will bite.":
        "O nível de Pesca que esta espécie exige para morder.",
    "The animal's health as a number.":
        "A saúde do animal como número.",
    "The animal's weight, and how far it still has to grow.":
        "O peso do animal, e o quanto ele ainda tem para crescer.",
    "The chance of this exact species with the bait you are using.":
        "A chance desta espécie exata com a isca que você está usando.",
    "The crop's health out of a hundred. The game only prints it with debug on.":
        "A saúde da plantação de cem. O jogo só escreve isso com a depuração ligada.",
    "The fuel still in the tank. The game knows the number and only prints it as a debug option.":
        "O combustível que resta no tanque. O jogo sabe o número e só o mostra como opção de depuração.",
    "The health the wall or door will have when you build it at your current level.":
        "A resistência que a parede ou a porta vai ter quando você construí-la no seu nível atual.",
    "The hourly odds of a bang loud enough to pull zombies in.":
        "A chance por hora de um estouro alto o bastante para atrair zumbis.",
    "The hourly odds of a fire or an explosion, which set the generator to zero outright.":
        "A chance por hora de incêndio ou explosão, que zeram o gerador de uma vez.",
    "The hourly odds of the bait being taken without a catch.":
        "A chance por hora de a isca ser levada sem nenhuma captura.",
    "The hourly odds of the trap being wrecked.":
        "A chance por hora de a armadilha ser destruída.",
    "The hourly odds of the wound becoming infected.":
        "A chance por hora de o ferimento infeccionar.",
    "The hours of the day the trap actually works.":
        "As horas do dia em que a armadilha realmente funciona.",
    "The kind of ground the trap is standing on, which decides what can come.":
        "O tipo de terreno em que a armadilha está, que decide o que pode aparecer.",
    "The odds of a bite once every factor is put together.":
        "A chance de fisgada depois que todos os fatores são somados.",
    "The odds of catching anything at all in an hour.":
        "A chance de pegar qualquer coisa em uma hora.",
    "The range of lengths and weights this species comes in.":
        "A faixa de comprimentos e pesos em que esta espécie aparece.",
    "The share of your catches that will be junk here.":
        "A fatia das suas capturas que aqui vai ser lixo.",
    "The two things the game never says: a long wait kills the catch, and standing nearby stops the trap.":
        "As duas coisas que o jogo nunca diz: uma espera longa mata a captura, e ficar por perto trava a armadilha.",
    "The water level as a number, and the amount this seed actually needs.":
        "O nível de água como número, e a quantidade que esta semente realmente precisa.",
    "Time to the danger threshold":
        "Tempo até o limiar de perigo",
    "Trophy size":
        "Tamanho de troféu",
    "Warnings":
        "Avisos",
    "Warns that the species only bites while you reel in.":
        "Avisa que a espécie só morde enquanto você recolhe a linha.",
    "What a catch has to beat to count as a trophy.":
        "O que uma captura precisa superar para contar como troféu.",
    "What the herbs in the bandage are adding.":
        "O que as ervas na bandagem estão acrescentando.",
    "What the same build would have at level {}, which is the reason to know the figure before building.":
        "O que a mesma construção teria no nível {}, que é o motivo de saber o número antes de construir.",
    "What the time of day is worth, as the multiplier behind the game's own rating.":
        "Quanto vale a hora do dia, como o multiplicador por trás da avaliação do próprio jogo.",
    "What the water temperature is worth, with the actual reading in degrees.":
        "Quanto vale a temperatura da água, com a leitura real em graus.",
    "What the weather is worth, as the multiplier behind the game's own rating.":
        "Quanto vale o clima, como o multiplicador por trás da avaliação do próprio jogo.",
    "What the wind is worth. Past half strength it costs the same penalty fog does, and the two never stack.":
        "Quanto vale o vento. Passada a metade da força ele custa a mesma penalidade da névoa, e as duas nunca somam.",
    "Whether the mains or a generator is keeping the pump running.":
        "Se é a rede elétrica ou um gerador que mantém a bomba funcionando.",
    "Which animals a bait item brings in.":
        "Quais animais um item usado como isca atrai.",
    "Which bait is in the trap, and whether it is still fresh.":
        "Qual isca está na armadilha, e se ela ainda está fresca.",
    "Which baits work best on this species.":
        "Quais iscas funcionam melhor nesta espécie.",
    "Which growth stage the crop is on, out of the total.":
        "Em qual estágio de crescimento a plantação está, do total.",
    "Which hook is fitted and what it does to your odds.":
        "Qual anzol está montado e o que ele faz com as suas chances.",
    "Raw eggs never make you ill":
        "Ovos crus nunca te fazem mal",
    "{}%% wait before another anti-nausea food works":
        "{}%% de espera até outra comida contra náusea fazer efeito",
    "{}%% weapon sight range":
        "{}%% de alcance das miras",
    "At Axe {} you swing as fast as a maxed axe user":
        "Com Machado em {} você golpeia tão rápido quanto quem o tem no máximo",
    "{}%% from any poisonous food or drink":
        "{}%% de qualquer comida ou bebida venenosa",
    "{}%% chance of illness from rotten food":
        "{}%% de chance de adoecer por comida estragada",
    "Melee weapons":
        "Armas corpo a corpo",
    "Firearms":
        "Armas de fogo",
    "Drinks":
        "Bebidas",
    "Skill XP":
        "XP de habilidade",
    "Weapons":
        "Armas",
    "Worn and carried":
        "Roupas e recipientes",
    "Medicine and reading":
        "Remédios e leitura",
    "Supplies":
        "Suprimentos",
    "Comparison":
        "Comparação",
    "Power and fuel":
        "Energia e combustível",
    "Animals and traps":
        "Animais e armadilhas",
    "Traits and jobs":
        "Traços e profissões",
    "Moodles":
        "Moodles",
}
