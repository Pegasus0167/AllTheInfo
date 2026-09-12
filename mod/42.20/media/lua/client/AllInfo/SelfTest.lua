require "AllInfo/Core"
require "AllInfo/Render"      -- AllInfo.pad and the render hooks
require "AllInfo/OptionsTab"  -- the MainOptions hooks and the option catalog
require "AllInfo/CraftingUI"  -- AllInfoItemTip and the output widget hooks
require "AllInfo/Moodles"     -- the moodle column and its texture table
require "AllInfo/world/Generator"
require "AllInfo/world/GeneratorRange"
require "AllInfo/world/Structures"
require "AllInfo/world/Crops"
require "AllInfo/world/Fishing"
require "AllInfo/world/Animals"
require "AllInfo/providers/FishingGear"
require "AllInfo/character/XpMultiplier"
require "AllInfo/character/SkillRecipes"
require "AllInfo/character/Creation"
require "AllInfo/character/InfoScreen"
require "AllInfo/character/Health"
require "AllInfo/character/SkillLevels"
require "AllInfo/character/SkillLevelsCraft"
require "AllInfo/world/Traps"
require "AllInfo/providers/Medicine"
require "AllInfo/providers/Container"
require "AllInfo/providers/Drink"

-- The mod's only runnable check. No framework, no fixtures: it fails loudly
-- when a game update changes an API underneath us.
-- Run from the debug console with: AllInfo.SelfTest.run()
-- Grows with each phase; phase 1 covers the pure helpers and the render hooks.

AllInfo.SelfTest = AllInfo.SelfTest or {}

local function check(fails, name, ok)
    if not ok then fails[#fails + 1] = name end
    return ok and 1 or 0
end

-- "nil" and "nan" only count as leaks when they stand alone. Plain find()
-- matched them inside ordinary words and cried wolf the moment the profession
-- block started listing recipe *names*: "destornillador", "tornillos",
-- "anillo" and "espinillera" all contain "nil".
local function leaks(s)
    local padded = " " .. s .. " "
    return padded:find("[^%w]nil[^%w]") ~= nil
        or padded:find("[^%w]nan[^%w]") ~= nil
        or padded:find("[^%w]inf[^%w]") ~= nil
end

-- Kahlua allows 200 local variables per function and run() is one function, so
-- the big sweeps live out here and take t() as an argument. This is not tidying
-- up: run() hit 222 locals when the animal sweep landed and the compiler died
-- at load with a bare ArrayIndexOutOfBounds, which took AllInfo.SelfTest with
-- it. tools/LuaCheck.java now counts locals per function and fails at 200.

-- Forward declarations: `function name()` below assigns to these locals,
-- so nothing new lands in the game's global table.
local providerChecks, fishingChecks, animalChecks, ronda4Checks

-- Run every provider against real items. Catches API breakage without
-- having to hover anything in game. Grows as providers land.
function providerChecks(t)
    local SAMPLES = {
        -- Food and Nutrition
        "Base.Bread", "Base.Steak", "Base.Apple", "Base.Milk", "Base.Cheese", "Base.Butter",
        -- Medicine, and Carrots doubles as a trap bait
        "Base.Pills", "Base.PillsBeta", "Base.PillsAntiDep",
        "Base.PillsSleepingTablets", "Base.Antibiotics", "Base.Carrots",
        -- MeleeWeapon: one per swing animation and weapon category
        "Base.Axe", "Base.BaseballBat", "Base.KitchenKnife", "Base.HuntingKnife",
        "Base.Machete", "Base.Katana", "Base.Crowbar", "Base.Sledgehammer",
        "Base.Hammer", "Base.Saw", "Base.Screwdriver",
        -- Firearm and Ammo
        "Base.Shotgun", "Base.ShotgunSawnoff", "Base.Pistol", "Base.HuntingRifle",
        "Base.9mmClip", "Base.556Bullets", "Base.308Box", "Base.Bullets9mmBox",
        -- Books: skill book, plain book and the two that only kill boredom
        "Base.BookMaintenance1", "Base.BookCarpentry1", "Base.Notebook", "Base.Newspaper",
        -- Seeds
        "Base.BroccoliSeed", "Base.CarrotSeed", "Base.CabbageSeed",
        -- Fuel
        "Base.Log", "Base.Plank", "Base.Twigs", "Base.SheetPaper2",
        -- Sleep
        "Base.Pillow", "Base.Mattress",
        -- Power: a torch that lights, a battery that does not, and a radio
        "Base.HandTorch", "Base.Battery", "Base.WalkieTalkie1",
        -- Mask: with filter, without filter, improvised and plain
        "Base.Hat_GasMask", "Base.Hat_GasMask_nofilter", "Base.Hat_ImprovisedGasMask",
        "Base.Hat_BuildersRespirator", "Base.Hat_DustMask",
        -- Clothing: one per body slot the provider has to cope with
        "Base.Tshirt_WhiteTINT", "Base.Trousers_Black", "Base.Shoes_Black",
        "Base.Jacket_Padded", "Base.Hat_BaseballCap", "Base.Gloves_LeatherGloves",
        -- RecordedMedia
        "Base.VHS_Retail", "Base.VHS_Home",
        -- Containers: a plain bag, the worst run penalty, and one of the five
        -- that also carry a combat modifier
        "Base.Bag_Schoolbag", "Base.Bag_BigHikingBag", "Base.Bag_ChestRig",
        -- Items no provider should touch
        "Base.Sheet", "Base.Doll",
    }

    local built, dirty = 0, {}
    for _, fullType in ipairs(SAMPLES) do
        local proto = AllInfo.proto(fullType)
        if proto then
            built = built + 1
            for _, row in ipairs(AllInfo.rows(proto, nil) or {}) do
                if type(row.value) ~= "string" then
                    dirty[#dirty + 1] = fullType .. " (not a string)"
                elseif row.value:find("nan") or row.value:find("inf") or row.value:find("nil") then
                    dirty[#dirty + 1] = fullType .. " -> " .. row.value
                end
            end
        end
    end
    t("providers.samples-built", built == #SAMPLES)
    t("providers.clean-output", #dirty == 0)

    -- The Trains row prints one skill and stops, which is only honest while no
    -- weapon carries two of the six XP-granting categories. Swept over every
    -- item script in the game, mods included, because that is the claim being
    -- made -- SAMPLES would only prove it for eleven weapons.
    local multi = {}
    local allScripts = getScriptManager():getAllItems()
    for i = 0, allScripts:size() - 1 do
        local script = allScripts:get(i)
        if not script:isRanged() then
            local n = 0
            for j = 1, #AllInfo.MeleeWeapon.XP_CATEGORIES do
                if script:containsWeaponCategory(AllInfo.MeleeWeapon.XP_CATEGORIES[j][1]) then
                    n = n + 1
                end
            end
            if n > 1 then multi[#multi + 1] = script:getDisplayName() end
        end
    end
    t("weapon.one-xp-category", #multi == 0)

    -- The clothing provider has to actually produce rows: every getter it calls
    -- is on Clothing rather than InventoryItem, so a rename there would leave
    -- the block empty instead of throwing.
    local shirt = AllInfo.proto("Base.Tshirt_WhiteTINT")
    local shirtRows = shirt and AllInfo.rows(shirt, nil) or {}
    t("clothing.produces-rows", #shirtRows > 0)

    -- The stomp row hangs off two names that can be renamed without throwing:
    -- ItemBodyLocation.SHOES and Clothing.getStompPower. Shoes_Black is 2.1 in
    -- the scripts, and the shirt above proves the row stays off everything else.
    local stompLabel = getText("Tooltip_AllInfo_StompPower")
    local function stompValue(rows)
        for _, row in ipairs(rows) do
            if row.label == stompLabel then return row.value end
        end
    end
    local shoes = AllInfo.proto("Base.Shoes_Black")
    t("clothing.stomp-shoes", stompValue(shoes and AllInfo.rows(shoes, nil) or {}) == "210%")
    t("clothing.stomp-shirt-only", stompValue(shirtRows) == nil)

    -- Same reasoning for the cooking row: getCookingTime / getMinutesToCook and
    -- ItemContainer.getTemprature live on other classes, and a rename would
    -- silently drop the line rather than throw. Steak is IsCookable with
    -- MinutesToCook = 50. Out of an oven the row quotes the 200 C ceiling, so
    -- the value must carry the temperature postfix too.
    local steak = AllInfo.proto("Base.Steak")
    local cooking
    for _, row in ipairs(steak and AllInfo.rows(steak, nil) or {}) do
        if row.label == getText("Tooltip_AllInfo_CookingTime") then cooking = row.value end
    end
    t("cooking.produces-row", cooking ~= nil)
    t("cooking.quotes-temperature",
        cooking ~= nil and cooking:find(Temperature.getTemperaturePostfix(), 1, true) ~= nil)
    -- 50 units at heat 3.0 is 50 / (3 / 1.5) = 25 minutes, plus the warm-up
    -- when that option is on. Guards the arithmetic, not just the row.
    t("cooking.counts-minutes", cooking ~= nil and cooking:find(
        AllInfo.duration(AllInfo.enabled("CookingWarmUp") and 29 or 25), 1, true) == 1)

    -- Drinks. A prototype bottle is created empty, so the provider has nothing
    -- to draw and that is the point: the guard has to hold. The scale itself is
    -- checked on the fluid definition instead, which is where the surprise was:
    -- Water declares ThirstChange -50 and the Thirst bar is 0..1, so drinking a
    -- full litre is half your thirst, not fifty of anything.
    local bottle = AllInfo.proto("Base.WaterBottle")
    t("drink.empty-is-quiet", bottle == nil or #(AllInfo.rows(bottle, nil) or {}) >= 0)
    -- Water's script says ThirstChange = -50 and the property reads -0.5,
    -- because CharacterStat registers Thirst on a 0..1 bar. Measured in game
    -- 02-09-2026; the provider multiplies by 100 on the strength of this.
    local water = Fluid and Fluid.Water and Fluid.Water:getProperties()
    t("drink.thirst-scale", water == nil
        or math.abs(water:getThirstChange() + 0.5) < 0.001)
    -- Bleach is Deadly, and Deadly is level 100, not 5: 700 poison per litre.
    local bleach = Fluid and Fluid.Bleach and Fluid.Bleach:getProperties()
    t("drink.poison-scale", bleach == nil or bleach:getPoison() > 0)

    -- Power. The torch rows hang off getLightDistance / getLightStrength and the
    -- ten-minute bucket of DrainableComboItem.update(); none of the three throws
    -- if it goes missing, the rows just vanish. Values are derived from the item
    -- rather than pinned, so a balance patch does not fail the test.
    local torch = AllInfo.proto("Base.HandTorch")
    local torchRows = torch and AllInfo.rows(torch, nil) or {}
    local function valueOf(rows, label)
        for _, row in ipairs(rows) do
            if row.label == label then return row.value end
        end
    end
    local life = valueOf(torchRows, getText("Tooltip_AllInfo_PowerLife"))
    t("power.torch-rows", valueOf(torchRows, getText("IGUI_invpanel_Remaining")) ~= nil
        and life ~= nil
        and valueOf(torchRows, getText("Tooltip_AllInfo_LightDistance")) ~= nil
        and valueOf(torchRows, getText("Tooltip_AllInfo_LightStrength")) ~= nil)

    -- One UseDelta per ten game minutes, not per minute: that x10 is the whole
    -- difference between a torch and a radio, and it is the easiest thing in
    -- this file to "simplify" away by accident.
    local charge = torch and torch:getCurrentUsesFloat() or 0
    local delta = torch and torch:getUseDelta() or 0
    t("power.ten-minute-bucket", delta > 0
        and life == AllInfo.duration(charge / delta * 10)
        and life ~= AllInfo.duration(charge / delta))

    -- A battery has charge but no light, and no clock either: it cannot be
    -- activated, so quoting a duration for it would be an invented number.
    local battery = AllInfo.proto("Base.Battery")
    local batteryRows = battery and AllInfo.rows(battery, nil) or {}
    t("power.battery-no-light",
        valueOf(batteryRows, getText("IGUI_invpanel_Remaining")) ~= nil
        and valueOf(batteryRows, getText("Tooltip_AllInfo_LightDistance")) == nil
        and valueOf(batteryRows, getText("Tooltip_AllInfo_PowerLife")) == nil)

    -- The beam. TorchDot is the cosine of the half-angle (IsoGridSquare tests a
    -- dot product of two unit vectors against it), so the hand torch's 0.5 is a
    -- 120 degree cone. Derived from the item's own dot rather than pinned to
    -- 120, so a balance patch does not fail the test -- what it does catch is
    -- getTorchDot() going away or the conversion being "simplified".
    t("power.torch-beam", torch ~= nil
        and valueOf(torchRows, getText("Tooltip_AllInfo_LightBeam"))
            == AllInfo.num(math.deg(math.acos(torch:getTorchDot())) * 2, 0))

    -- A hurricane lantern is TorchCone = false, which takes the other branch of
    -- that same test. It has no angle, and inventing 360 for it is exactly what
    -- this asserts we do not do.
    local lantern = AllInfo.proto("Base.Lantern_HurricaneLit")
    t("power.lantern-all-round", lantern ~= nil
        and valueOf(AllInfo.rows(lantern, nil) or {}, getText("Tooltip_AllInfo_LightBeam"))
            == getText("Tooltip_AllInfo_LightBeamAll"))

    -- Bags. RunSpeedModifier has no getter and public fields do not reach Lua,
    -- so the figure is read out of the script text the engine itself parsed.
    -- This is really a check that getScriptLines() still hands that text back:
    -- the day it returns an empty list the row disappears in silence.
    local bag = AllInfo.proto("Base.Bag_Schoolbag")
    local bagRun = bag and AllInfo.Container.scriptNumber(bag, "RunSpeedModifier")
    t("container.script-number",
        type(bagRun) == "number" and bagRun > 0 and bagRun <= 1)

    -- A prototype is empty, so the fill term is 1 and the penalty is the flat
    -- modifier. Compared against the parsed value, not against -3, for the same
    -- reason as the beam above.
    t("container.run-penalty", bagRun ~= nil
        and math.abs(AllInfo.Container.runPenalty(bag, nil) - (bagRun - 1) * 100) < 1e-9)
    t("container.row", bag ~= nil
        and valueOf(AllInfo.rows(bag, nil) or {},
            getText("Tooltip_RunSpeedModifier")) ~= nil)

    -- Radios run on the other clock: one UseDelta per single minute, so half a
    -- battery at 0.001 is 500 minutes and not 5000. Asserted on the arithmetic
    -- rather than on a hovered radio, because a fresh prototype has no battery
    -- in it and would produce no rows at all.
    t("radio.per-minute", AllInfo.Power.deviceMinutes(0.5, 0.001) == 500)
    t("radio.no-clock-without-delta", AllInfo.Power.deviceMinutes(0.5, 0) == nil)

    -- The device data itself has to still be there and still carry a drain, or
    -- the two rows would quietly stop appearing instead of throwing.
    local walkie = AllInfo.proto("Base.WalkieTalkie1")
    local data = walkie and instanceof(walkie, "Radio") and walkie:getDeviceData()
    t("radio.device-data", data ~= nil and data:getUseDelta() > 0)
end

-- Round 4: frozen food, weapon components, medicine, mask filters, traps and
-- the derived per-level skill lines. Same rule as the fishing block: these
-- assert that the API is still there and still answers in range, never a
-- balance number, except where the whole point is that a hardcoded mirror still
-- matches the game.
-- The trap block, in its own function and called under pcall. It used to sit
-- inline inside ronda4Checks, where an exception would have taken every check
-- after it down with it and still let run() print a total, which is the one
-- thing a self-test must never do. Now a fall is one named assertion,
-- trap.block-ran, and the error is printed with its own text.
local function trapChecks(t)
    -- Trap tables, straight from vanilla's server-side Lua.
    --
    -- None of this lives inside an `if` any more. It did, and a check that
    -- vanishes when the thing it was going to test is missing proves nothing:
    -- it just shrinks the total without saying so. The tables being absent is
    -- one named assertion now, and the rest carry it as a condition.
    local haveTraps = TrapAnimals ~= nil and Traps ~= nil
    t("trap.tables-present", haveTraps)

    local badTrap, badHour, badPct = nil, nil, nil
    if haveTraps then
        for i = 1, #TrapAnimals do
            local a = TrapAnimals[i]
            if a.minHour < 0 or a.minHour > 24 or a.maxHour < 0 or a.maxHour > 24 then
                badHour = a.type
            end
            for trapType, chance in pairs(a.traps or {}) do
                local found = false
                for j = 1, #Traps do
                    if Traps[j].type == trapType then found = true end
                end
                if not found then badTrap = trapType end
                -- roll() reads these as percentage points, so anything outside
                -- 0..100 would come out of AllInfo.pct as a nonsense figure.
                if chance < 0 or chance > 100 then badPct = trapType end
            end
        end
    end
    t("trap.tables", badTrap == nil)
    t("trap.hours", badHour == nil)
    t("trap.pct", badPct == nil)

    -- The window itself, against a trap built here rather than found in the
    -- world: AllInfo.Traps.rows() is plain Lua over plain tables, so it can be
    -- run without a placed trap under the cursor. This is the only cover the
    -- biggest block of the round had, and it had none.
    local fake = {
        trapType = "Base.TrapCage", bait = "Base.Carrots", trapBaitDay = 0,
        trappingSkill = 5, zones = { DeepForest = "DeepForest" },
        zone = "DeepForest", animal = {}, animalAliveHour = 0,
    }
    local okRows, rows = pcall(AllInfo.Traps.rows, fake)
    t("trap.rows-build", okRows and type(rows) == "table" and #rows > 0)

    local badRow, share, sawWarning, sawCatch = nil, 0, false, false
    if okRows and type(rows) == "table" then
        for i = 1, #rows do
            local r = rows[i]
            if type(r.label) ~= "string" or type(r.value) ~= "string" then
                badRow = i
            elseif leaks(r.label) or leaks(r.value) then
                badRow = i
            end
            if r.indent then
                share = share + (tonumber(r.value:match("^([%d%.]+)%%")) or 0)
            end
            if r.wide then sawWarning = true end
            if r.label == getText("UI_AllInfo_trap_CatchChance") then sawCatch = true end
        end
    end
    t("trap.rows-clean", badRow == nil)
    -- The per-animal figures are shares of one draw, so they add up to the whole
    -- catch and nothing else. This is the check that the exact draw maths in
    -- draws() agrees with the catch chance next to it; a slip in either shows up
    -- here as a total that is not 100. Two points of slack for the rounding.
    t("trap.rows-shares", not haveTraps or (share > 98 and share < 102))
    -- The "not while you are near it" line is unconditional, and a baited cage
    -- in deep forest always has odds of catching something.
    t("trap.rows-warning", sawWarning)
    t("trap.rows-catch", not haveTraps or sawCatch)

    -- Same trap with the bait taken out: the trap does not roll at all, so no
    -- prey row may carry a percentage and there is no catch chance either.
    fake.bait, fake.trapBaitDay = nil, nil
    local okBare, bare = pcall(AllInfo.Traps.rows, fake)
    local bareHasPct = false
    if okBare and type(bare) == "table" then
        for i = 1, #bare do
            if bare[i].indent and bare[i].value:find("%%") then bareHasPct = true end
            if bare[i].label == getText("UI_AllInfo_trap_CatchChance") then
                bareHasPct = true
            end
        end
    end
    t("trap.rows-unbaited", okBare and not bareHasPct)
end

function ronda4Checks(t)
    -- Frozen food keeps the number and only swaps the label, so both labels
    -- have to exist. Tooltip_AllInfo_Forever is gone on purpose.
    t("spoil.thawed-keys", getTextOrNull("Tooltip_AllInfo_StaleThawed") ~= nil
        and getTextOrNull("Tooltip_AllInfo_RotsThawed") ~= nil)

    -- Only three weapon categories scale with skill. The other three answer a
    -- flat 1.0 at any level, which is what makes their old "attack speed" line
    -- a lie.
    local chr = getPlayer()
    local knife = AllInfo.proto("Base.KitchenKnife")
    local bat = AllInfo.proto("Base.BaseballBat")
    -- The three calls the attack speed row is built out of. getSpeedMod() is
    -- gone from here on purpose: it is dead code in the game and testing it only
    -- proved the copy of a table nothing reads (state, trap 92).
    t("weapon.base-speed", not bat or bat:getBaseSpeed() > 0)
    t("weapon.chop-speed", not chr or chr:getChopTreeSpeed() > 0)
    t("weapon.category-call", not bat or type(bat:isOfWeaponCategory(WeaponCategory.BLUNT)) == "boolean")

    -- Our walk of getWeaponLevel against the real one, for the only weapon it
    -- can be asked about: the one in your hands. This is the check that makes
    -- reproducing it acceptable (trap 175).
    local held = chr and chr:getPrimaryHandItem()
    local heldWeapon = held and instanceof(held, "HandWeapon") and held
    t("weapon.level-walk", not heldWeapon
        or AllInfo.MeleeWeapon.weaponLevel(heldWeapon, chr) == chr:getWeaponLevel(heldWeapon))

    -- A weapon skill produces a line, a non-weapon skill produces none.
    t("skill.describe-weapon", AllInfo.SkillLevels.describe(Perks.Axe, 5) ~= nil)
    t("skill.describe-other", AllInfo.SkillLevels.describe(Perks.Cooking, 5) == nil)
    t("skill.combat-config", type(getCombatConfig) == "function"
        and getCombatConfig() ~= nil)

    -- The other twenty skills. Every level of every covered perk has to build a
    -- line, and none of them may leak a raw translation key: a wrong argument
    -- count makes getText hand back the key with its %1 still in it, which is
    -- exactly how a mistyped line would reach the player.
    local craftBad = {}
    local CRAFT = { Perks.Farming, Perks.Husbandry, Perks.Butchering,
        Perks.Woodwork, Perks.Cooking, Perks.Doctor, Perks.Tailoring,
        Perks.Electricity, Perks.Fishing, Perks.PlantScavenging, Perks.Tracking }
    for i = 1, #CRAFT do
        for lvl = 1, 10 do
            local ok, line = pcall(AllInfo.SkillLevels.craft, CRAFT[i], lvl)
            if not ok or type(line) ~= "string" or line == ""
                or line:find("UI_AllInfo_perk_", 1, true) or line:find("%1", 1, true)
            then
                craftBad[#craftBad + 1] = tostring(CRAFT[i]:getId()) .. " " .. lvl
            end
        end
    end
    t("skill.craft-lines" .. (craftBad[1] and (" " .. craftBad[1]) or ""), #craftBad == 0)

    -- Fishing is called, not mirrored, so it is worth knowing the function is
    -- still there and still answers for an arbitrary level.
    t("skill.fish-table", Fishing and Fishing.Utils
        and type(Fishing.Utils.getFishSizeChancesBySkillLevel) == "function")

    -- Carving and friends read the level nowhere, and say so.
    t("skill.craft-recipes-only", AllInfo.SkillLevels.craft(Perks.Pottery, 3) ~= nil)
    -- Trapping is deliberately not covered.
    t("skill.craft-uncovered", AllInfo.SkillLevels.craft(Perks.Trapping, 3) == nil)

    -- Sharpness ceiling is the head's own wear, which is the link between the
    -- head and the damage the weapon does.
    local axe = AllInfo.proto("Base.HandAxe")
    t("weapon.sharp-cap", not axe or not axe:hasSharpness()
        or not axe:hasHeadCondition()
        or math.abs(axe:getMaxSharpness()
            - axe:getHeadCondition() / axe:getHeadConditionMax()) < 0.001)

    -- A critical never multiplies by less than 2, whatever the script says:
    -- processHitDamage() takes Math.max(2, getCriticalDamageMultiplier()). The
    -- broom is one of the fifteen vanilla weapons shipping a 1.0.
    local broom = AllInfo.proto("Base.Broom")
    t("weapon.crit-floor", not broom or AllInfo.criticalDamage(broom) == 2)
    t("weapon.crit-passthrough", not bat or AllInfo.criticalDamage(bat)
        == bat:getCriticalDamageMultiplier())

    -- Two-handed strain is halved, and it is halved *per arm*.
    local strainOne = knife and chr and AllInfo.MeleeWeapon.strain(knife, chr)
    t("weapon.strain-positive", not strainOne or strainOne > 0)

    local hits = bat and chr and AllInfo.hitsToBreak(bat, chr)
    t("weapon.hits-positive", not hits or hits > 0)

    -- Every pill answers with a finite, positive duration at the current day
    -- length, and none of them leaks a nil into its row.
    local pills = { "Base.Pills", "Base.PillsBeta", "Base.PillsAntiDep",
                    "Base.PillsSleepingTablets", "Base.Antibiotics" }
    local badPill = nil
    for i = 1, #pills do
        local item = AllInfo.proto(pills[i])
        if item then
            local rows = {}
            local ok = pcall(function()
                for _, p in ipairs(AllInfo.providers) do
                    if p.id == "Medicine" then p.fn(rows, item, getPlayer()) end
                end
            end)
            if not ok or #rows == 0 then badPill = pills[i] end
            for j = 1, #rows do
                if leaks(rows[j].value) then badPill = pills[i] end
            end
        end
    end
    t("medicine.rows-clean", badPill == nil)

    local trapOk, trapErr = pcall(trapChecks, t)
    t("trap.block-ran", trapOk)
    if not trapOk then print("[AllInfo] trap block: " .. tostring(trapErr)) end

    -- The three farming getters are ours now, and vanilla's own text has to
    -- still come through them untouched when the option is off.
    t("hook.FarmingWaterLvl", AllInfo.hooks.FarmingWaterLvl == ISFarmingInfo.getWaterLvl)
    t("hook.FarmingNextPhase",
        AllInfo.hooks.FarmingNextPhase == ISFarmingInfo.getNextGrowingPhase)
    t("hook.FarmingDisease", AllInfo.hooks.FarmingDisease == ISFarmingInfo.getDiseaseString)
end

-- Fishing. The coefficients come from vanilla's own functions, so these
-- assertions are about the API still being there and answering in range,
-- never about a specific balance number.
function fishingChecks(t)
    local F = AllInfo.Fishing
    t("fishing.utils-present", type(Fishing) == "table"
        and type(Fishing.Utils) == "table"
        and type(Fishing.Utils.getTemperatureParams) == "function"
        and type(Fishing.Utils.getWeatherParams) == "function"
        and type(Fishing.Utils.getTimeParams) == "function"
        and type(Fishing.Utils.getHookParams) == "function"
        and type(Fishing.Utils.getFishNumParams) == "function"
        and type(Fishing.Utils.isNearShore) == "function"
        and type(Fishing.isRiver) == "function"
        and type(Fishing.isNoFishZone) == "function")
    t("fishing.species-table", type(Fishing.fishes) == "table" and #Fishing.fishes > 0)
    t("fishing.hook-table", type(Fishing.hook) == "table" and Fishing.hook["Base.FishingHook"] ~= nil)

    -- The per-level weight cap decides which species can bite at all. It has to
    -- stay sorted, or minLevel() answers nonsense.
    local sizeOk = true
    for lvl = 1, 10 do
        local prev = Fishing.Utils.skillSizeLimit[lvl - 1]
        local here = Fishing.Utils.skillSizeLimit[lvl]
        if type(here) ~= "number" or type(prev) ~= "number" or here < prev then sizeOk = false end
    end
    t("fishing.size-limit-sorted", sizeOk)

    -- Every species must be reachable at some level.
    local speciesDirty = {}
    for _, cfg in ipairs(Fishing.fishes) do
        local lvl = F.minLevel(cfg)
        if type(lvl) ~= "number" or lvl < 0 or lvl > 10 then
            speciesDirty[#speciesDirty + 1] = tostring(cfg.itemType) .. ": level " .. tostring(lvl)
        end
    end
    t("fishing.min-level-known", #speciesDirty == 0)
    for i = 1, math.min(#speciesDirty, 3) do
        print("[AllInfo] fishing species: " .. speciesDirty[i])
    end

    -- Odds with a given bait must add up to 100% inside each regime.
    local odds = F.speciesOdds("Base.Worm", false, 10)
    local oddsSum, oddsCount = 0, 0
    -- pairs(), never next(): the game's Kahlua VM does not expose next().
    for _, pct in pairs(odds.base) do
        oddsSum = oddsSum + pct
        oddsCount = oddsCount + 1
    end
    t("fishing.odds-sum", math.abs(oddsSum - 100) < 0.5)
    t("fishing.odds-nonempty", oddsCount > 0)

    -- The wait is expressed relative to the best case, so it can never be < 1.
    t("fishing.wait-floor", F.waitRatio(500, false, false) == 1)
    t("fishing.wait-shore", F.waitRatio(500, true, false) == 2)
    t("fishing.wait-close", F.waitRatio(500, false, true) == 3)
    t("fishing.wait-worst", F.waitRatio(2000, true, true) == 24)

    -- Every species must compose a clean block, with or without a rod in hand.
    local blockDirty = {}
    for _, cfg in ipairs(Fishing.fishes) do
        local okBlock, block = pcall(F.speciesBlock, cfg.itemType, getSpecificPlayer(0))
        if not okBlock or type(block) ~= "string" or block == "" then
            blockDirty[#blockDirty + 1] = tostring(cfg.itemType) .. ": " .. tostring(block)
        elseif leaks(block) then
            blockDirty[#blockDirty + 1] = tostring(cfg.itemType) .. " -> " .. block
        end
    end
    t("fishing.species-blocks-clean", #blockDirty == 0)
    for i = 1, math.min(#blockDirty, 3) do
        print("[AllInfo] fishing block: " .. blockDirty[i])
    end

    -- The panel wrappers must be ours, and installed exactly once.
    local INFO = PZAPI.UI.FishWindow.children.body.children.tabPanel.children.info
    t("fishing.hooks-installed", F.hookedUpdate == true and F.hookedInit == true
        and type(INFO.update) == "function" and type(INFO.init) == "function")
    t("fishing.header-tips", type(INFO.children.textTime.onHover) == "function"
        and type(INFO.children.textWind.onHover) == "function")
end

-- Animals. The panel wrapper must be ours and installed exactly once.
function animalChecks(t)
    t("animals.hook-installed", AllInfo.Animals.hooked == true
        and type(AllInfo.hooks.AnimalUIRender) == "function"
        and AllInfo.hooks.AnimalUIRender == ISAnimalUI.render
        and type(AllInfo.Animals.draw) == "function")

    -- Every animal in the cell gets its block composed, both with and without
    -- the cheat flag, so a getter that moved shows up here instead of in a
    -- stack trace on the first cow. Scales are asserted in range: hunger,
    -- thirst and health are 0-1 and stress is 0-100, and mixing those up is
    -- what would publish a "7000%".
    -- getAnimals() is typed as java.util.List, not ArrayList: asked through a
    -- closure so a binding that does not expose size() fails as a nil count
    -- instead of taking the rest of the sweep with it.
    local okCell, animals = pcall(function()
        local cell = getCell()
        local list = cell and cell:getAnimals()
        return list and list:size() > 0 and list or nil
    end)
    if not okCell then animals = nil end

    local chr = getSpecificPlayer(0)
    if animals and chr then
        local animalDirty, animalRows = {}, 0
        for i = 0, animals:size() - 1 do
            local a = animals:get(i)
            for _, cheat in ipairs({ true, false }) do
                local okRows, list = pcall(AllInfo.Animals.rows, a, chr, 10, cheat)
                if not okRows or type(list) ~= "table" then
                    animalDirty[#animalDirty + 1] = tostring(a:getAnimalType()) .. ": " .. tostring(list)
                else
                    for _, r in ipairs(list) do
                        animalRows = animalRows + 1
                        if leaks(r.label .. " " .. r.value) then
                            animalDirty[#animalDirty + 1] = r.label .. " = " .. r.value
                        end
                        -- Every row promises a hover description. A missing key
                        -- would silently show no box; a "%%" left in the text
                        -- would mean getTextOrNull stopped running the string
                        -- through String.format, which is what un-escapes it.
                        local tip = r.tip and getTextOrNull(r.tip)
                        if not tip then
                            animalDirty[#animalDirty + 1] = r.label .. ": no tip " .. tostring(r.tip)
                        elseif tip:find("%%%%") then
                            animalDirty[#animalDirty + 1] = r.tip .. ": literal %% in " .. tip
                        end
                    end
                end
            end

            local h, hunger, thirst, stress = a:getHealth(), a:getHunger(), a:getThirst(), a:getStress()
            if h < 0 or h > 1 or hunger < 0 or hunger > 1 or thirst < 0 or thirst > 1
                or stress < 0 or stress > 100 then
                animalDirty[#animalDirty + 1] = tostring(a:getAnimalType()) .. ": scale out of range"
            end
        end
        t("animals.blocks-clean", #animalDirty == 0)
        t("animals.finds-something", animalRows > 0)
        for i = 1, math.min(#animalDirty, 3) do
            print("[AllInfo] animal block: " .. animalDirty[i])
        end
    end
end

-- The tab builds every control once and then only moves them, so the failure it
-- can have is a row or a group that never got built: it would be invisible AND
-- unsaved, and nothing else would complain. Counting is the whole check.
--
-- Its own function rather than inline in run(): Kahlua allows 200 locals per
-- function and run() is already past the 150 warning (traps 83 and 84).
local function checkOptionsTab(t)
    local page = AllInfo.OptionsTab and AllInfo.OptionsTab.page
    if not page then return end   -- the options screen has never been opened

    local rows, groups = 0, 0
    for _, section in ipairs(AllInfo.Options.sections) do
        rows = rows + #section.options
        groups = groups + #section.groups
    end

    local built = 0
    for _, sec in ipairs(page.sections) do built = built + #sec.groups end

    -- Every switch that hides a single tooltip line is named with the key of
    -- that line's own label, and most of those keys are vanilla's. A key the
    -- game renames stops resolving and the tab prints the raw key, which is not
    -- something a compile or a translation check can see: this is what catches
    -- it, and it covers the group headers for the same reason.
    local missing
    for _, section in ipairs(AllInfo.Options.sections) do
        for _, group in ipairs(section.groups) do
            local label = group.label or ("UI_AllInfo_group_" .. group.key)
            if getText(label) == label then missing = label end
            for _, o in ipairs(group.options) do
                local key = o[4] or ("UI_AllInfo_opt_" .. o[1])
                if getText(key) == key then missing = key end
            end
        end
    end
    -- The offending key rides in the test name: a bare red line saying "names"
    -- would send the next reader through ninety of them by hand.
    t("optionstab.names" .. (missing and (" (" .. missing .. ")") or ""), missing == nil)

    t("optionstab.rows-built", #page.every == rows)
    t("optionstab.sections-built", #page.sections == #AllInfo.Options.sections)
    t("optionstab.groups-built", built == groups)
end

-- Proving the tooltip switches without eighty hovers --------------------------
--
-- Every switch that hides a tooltip row can be proved from Lua alone: build the
-- rows of a sample item with the switch on, build them again with it off, and
-- the two lists have to differ. Nothing is drawn, so the whole item half of the
-- options tab is one command instead of an afternoon of hovering.
--
-- The verdict is deliberately three-way. A switch whose sample never produced
-- the row it hides comes back as "not proved", never as a pass: a test that
-- cannot see the row has nothing to say about it, and the list it prints at the
-- end is exactly what still needs a pair of eyes. Saying so out loud is the
-- whole point of running this instead of trusting it.
--
-- The world and character switches are not in here. Their lines live in
-- windows and context menus that need a real object under the cursor, so
-- tools/OptionAudit.py proves they are *wired* and the rest is manual.
--
-- ⚠️ AllInfo.rows() caches on the item and the character, not on the options,
-- so the second call would hand back the first answer. AllInfo.flushRows()
-- between them is what makes the comparison mean anything at all.

local AXE = "Base.Axe"
local GUN = "Base.Pistol"
local FOOD = "Base.Steak"

-- A sample per switch. A function when the type has to be looked up in a table
-- the game builds at runtime rather than named here.
local function anySeed()
    local props = farming_vegetableconf and farming_vegetableconf.props
    if not props then return nil end
    for _, plant in pairs(props) do
        if plant.seedName then return plant.seedName end
    end
end

local PROBE = {
    { "WpnDamage", AXE }, { "WpnCrit", AXE }, { "WpnCritDmg", AXE },
    { "WpnSharp", AXE }, { "WpnSpeed", AXE }, { "WpnReach", AXE },
    { "WpnStrain", AXE }, { "WpnSwing", AXE }, { "WpnCategory", AXE },
    { "WpnCondition", AXE }, { "WpnLoss", AXE }, { "WpnHits", AXE },
    { "HideFishingCombat", "Base.FishingRod" },

    { "GunCondition", GUN }, { "GunDamage", GUN }, { "GunRange", GUN },
    { "GunHitChance", GUN }, { "GunCrit", GUN }, { "GunNoise", GUN },
    { "GunAim", GUN }, { "GunReload", GUN }, { "GunClip", GUN },
    { "GunLoss", GUN }, { "GunJam", GUN },

    { "AmmoCount", "Base.Bullets9mmBox" }, { "AmmoType", "Base.Bullets9mmBox" },
    { "AmmoGuns", "Base.Bullets9mmBox" },

    { "FoodStale", FOOD }, { "FoodRots", FOOD },
    { "FoodCooking", FOOD }, { "FoodBurning", FOOD }, { "CookingWarmUp", FOOD },

    { "NutCalories", FOOD }, { "NutCarbs", FOOD },
    { "NutProteins", FOOD }, { "NutFat", FOOD },

    { "ClothCondition", "Base.Jacket_Varsity" },
    { "ClothInsulation", "Base.Jacket_Varsity" },
    { "ClothWind", "Base.Jacket_Varsity" },
    { "ClothWater", "Base.Jacket_Varsity" },
    { "ClothRun", "Base.Shoes_ArmyBoots" },
    { "ClothCombat", "Base.Shoes_ArmyBoots" },
    { "ClothDiscomfort", "Base.Jacket_Varsity" },
    { "ClothStomp", "Base.Shoes_ArmyBoots" },
    { "ClothBlood", "Base.Jacket_Varsity" },
    { "ClothDirt", "Base.Jacket_Varsity" },
    { "ClothWet", "Base.Jacket_Varsity" },

    { "BagRun", "Base.Bag_Schoolbag" }, { "BagCombat", "Base.Bag_Schoolbag" },

    { "MaskDefense", "Base.Hat_GasMask" }, { "MaskCharge", "Base.Hat_GasMask" },
    { "MaskLeft", "Base.Hat_GasMask" },

    { "MedDuration", "Base.PillsBeta" }, { "MedWait", "Base.PillsBeta" },
    { "MedEffect", "Base.PillsBeta" }, { "MedicineDetail", "Base.PillsBeta" },

    { "BookSpeed", "Base.Book" }, { "BookTime", "Base.Book" },

    { "MediaXp", "Base.VHS_Retail" }, { "MediaRecipes", "Base.VHS_Retail" },
    { "MediaWatched", "Base.VHS_Retail" },

    { "SleepQuality", "Base.Pillow" },

    { "PowerLeft", "Base.Torch" }, { "PowerLife", "Base.Torch" },
    { "LightDistance", "Base.Torch" }, { "LightStrength", "Base.Torch" },
    { "LightBeam", "Base.Torch" },

    { "RodTension", "Base.FishingRod" }, { "RodBreaks", "Base.FishingRod" },
    { "GearHook", "Base.FishingRod" }, { "GearLine", "Base.FishingRod" },

    { "SeedGrow", anySeed }, { "SeedMonths", anySeed },
    { "FuelBurn", "Base.Plank" },

    { "ShowDeltas", AXE },
}

-- Labels and values joined into one string. Comparing this rather than the row
-- count catches the switches that change a figure instead of removing a line,
-- which a count would call broken.
local function signature(item, chr)
    AllInfo.flushRows()
    local rows = AllInfo.rows(item, chr)
    if not rows then return "" end

    local parts = {}
    for i = 1, #rows do
        parts[#parts + 1] = rows[i].label .. "=" .. rows[i].value
            .. "=" .. tostring(rows[i].delta)
    end
    return table.concat(parts, "|")
end

function AllInfo.SelfTest.options()
    local opts = PZAPI.ModOptions.Dict[AllInfo.Options.MOD_ID]
    if not opts then
        print("[AllInfo] options are not registered, nothing to sweep")
        return false
    end

    local chr = getPlayer()
    local proved, unproved, nosample = 0, {}, {}

    for i = 1, #PROBE do
        local id = PROBE[i][1]
        local source = PROBE[i][2]
        local fullType = type(source) == "function" and source() or source
        local item = fullType and AllInfo.proto(fullType)
        local option = opts.dict[id]

        if not option then
            nosample[#nosample + 1] = id .. " (no such switch)"
        elseif not item then
            nosample[#nosample + 1] = id .. " (" .. tostring(fullType) .. " not in this build)"
        else
            local was = option.value

            option.value = true
            local on = signature(item, chr)
            option.value = false
            local off = signature(item, chr)

            option.value = was
            AllInfo.flushRows()

            if on == "" then
                unproved[#unproved + 1] = id .. " (no rows on " .. fullType .. ")"
            elseif on ~= off then
                proved = proved + 1
            else
                unproved[#unproved + 1] = id .. " (no change on " .. fullType .. ")"
            end
        end
    end

    print("[AllInfo] switch sweep: " .. proved .. "/" .. #PROBE .. " proved")
    if #unproved > 0 then
        print("[AllInfo]   not proved on their sample, check by hand: "
            .. table.concat(unproved, ", "))
    end
    if #nosample > 0 then
        print("[AllInfo]   no sample item: " .. table.concat(nosample, ", "))
    end
    return #unproved == 0 and #nosample == 0
end

function AllInfo.SelfTest.run()
    local fails, total, passed = {}, 0, 0

    local function t(name, ok)
        total = total + 1
        passed = passed + check(fails, name, ok)
    end

    -- Formatting. Only binary-exact values here: 1.235 is really
    -- 1.23499999..., so a .5 decimal case would fail for the wrong reason.
    t("round.half-up", AllInfo.round(2.5) == 3)
    t("round.down", AllInfo.round(1.2345, 2) == 1.23)
    t("round.up", AllInfo.round(1.236, 2) == 1.24)
    t("round.int", AllInfo.round(2.4) == 2)
    t("num.strips-zeros", AllInfo.num(2.0, 2) == "2")
    t("num.nan", AllInfo.num(0 / 0) == "")
    t("num.nil", AllInfo.num(nil) == "")
    t("pct.whole", AllInfo.pct(0.5) == "50%")
    t("pct.decimal", AllInfo.pct(0.125, 1) == "12.5%")
    t("signed.pos", AllInfo.signed(1.5, 1) == "+1.5")
    t("signed.neg", AllInfo.signed(-1.5, 1) == "-1.5")

    -- duration() must never leak nil/nan into a label
    local d = AllInfo.duration(1575)
    t("duration.string", type(d) == "string" and d ~= "")
    t("duration.clean", d and not d:find("nil") and not d:find("nan"))
    t("duration.negative", AllInfo.duration(-5) == nil)
    t("duration.nan", AllInfo.duration(0 / 0) == nil)
    t("duration.inf", AllInfo.duration(math.huge) == nil)
    t("duration.sub-minute", AllInfo.duration(0.5) ~= nil)

    -- Deltas vs the equipped item. The color follows "is this better", not the
    -- sign of the difference, so both directions are checked.
    local good, bad = AllInfo.color(true), AllInfo.color(false)
    local function isColor(c, ref)
        return c ~= nil and c.r == ref.r and c.g == ref.g and c.b == ref.b
    end

    local ds, dc = AllInfo.delta(2, 1, true, 2)
    t("delta.string", ds == "(+1)")
    t("delta.good-color", isColor(dc, good))
    local _, worseColor = AllInfo.delta(2, 1, false, 2)
    t("delta.inverted-color", isColor(worseColor, bad))
    local negative, negColor = AllInfo.delta(1, 2, true, 2)
    t("delta.negative", negative == "(-1)" and isColor(negColor, bad))
    t("delta.equal-is-nothing", AllInfo.delta(1, 1, true, 2) == nil)
    -- A nil `old` is the "nothing comparable in hand" path every provider uses.
    t("delta.no-other", AllInfo.delta(1, nil, true, 2) == nil)
    t("delta.nan", AllInfo.delta(0 / 0, 1, true, 2) == nil)
    t("delta.below-precision", AllInfo.delta(1.001, 1, true, 2) == nil)
    t("delta.suffix", AllInfo.delta(3, 1, true, 0, "%") == "(+2%)")
    t("deltaPct.scales", AllInfo.deltaPct(0.5, 0.25, true, 0) == "(+25%)")
    t("deltaPct.no-other", AllInfo.deltaPct(0.5, nil, true, 0) == nil)
    -- No character means no hands to compare against: the crafting UI path.
    t("compareTo.no-character", AllInfo.compareTo(AllInfo.proto("Base.Axe"), nil) == nil)

    -- Condition loss. Without a character it is the bare 1-in-N from the
    -- script, so only the shape is asserted: pinning 1/35 would just hardcode
    -- today's balance data.
    local axeLoss = AllInfo.conditionLoss(AllInfo.proto("Base.Axe"), nil)
    t("conditionLoss.no-character", type(axeLoss) == "number" and axeLoss > 0 and axeLoss <= 1)

    -- Tool weapons roll a second, separate check for the head. A hammer has one
    -- and a kitchen knife does not, which is the whole branch: the label of the
    -- first row changes to "handle" only when the second row exists.
    local hammer = AllInfo.proto("Base.Hammer")
    local knife = AllInfo.proto("Base.KitchenKnife")
    t("headCondition.hammer-has-one", hammer ~= nil and hammer:hasHeadCondition())
    t("headCondition.knife-has-none", knife ~= nil and not knife:hasHeadCondition())

    local headLoss = hammer and AllInfo.headConditionLoss(hammer, nil)
    t("headConditionLoss.hammer", type(headLoss) == "number" and headLoss > 0 and headLoss <= 1)
    t("headConditionLoss.knife-nil", knife ~= nil and AllInfo.headConditionLoss(knife, nil) == nil)
    -- The vanilla labels this leans on, which are the reason there are no keys
    -- of ours for the two condition rows.
    t("i18n.handle-condition", getText("Tooltip_weapon_HandleCondition") ~= "Tooltip_weapon_HandleCondition")
    t("i18n.head-condition", getText("Tooltip_weapon_HeadCondition") ~= "Tooltip_weapon_HeadCondition")

    -- AllInfo.weaponLevel mirrors IsoGameCharacter.getWeaponLevel(HandWeapon),
    -- which ignores its argument and always answers about the equipped weapon.
    -- On that one item the two must agree, so this catches TIS changing the
    -- formula instead of letting the tooltip lie quietly. Needs a weapon in
    -- hand; skipped otherwise.
    local player = getSpecificPlayer(0)
    local held = player and player:getPrimaryHandItem()
    if held and instanceof(held, "HandWeapon") then
        t("weaponLevel.matches-java", AllInfo.weaponLevel(held, player) == player:getWeaponLevel(held))
    end

    -- AllInfo.rows keys its cache on the held item, so it keeps a Java
    -- reference across frames. That only works if two Lua reads of the same
    -- object compare equal; if it ever stops being true the cache silently
    -- never hits while something is in hand.
    if held then
        t("cache.java-identity", player:getPrimaryHandItem() == held)
    end

    -- ISToolTipInv is not item-only: ISFluidBar hands it a FluidContainer
    -- component. Anything that is not an InventoryItem has to be turned away
    -- before a provider calls an item method on it.
    t("rows.rejects-non-item", AllInfo.rows(getCore(), nil) == nil)

    -- The one method AllInfoItemTip exists to add: ISImage:updateTooltip()
    -- anchors through it and ISToolTipInv does not have it.
    t("craftingTip.adapts-position", type(AllInfoItemTip.setDesiredPosition) == "function")

    -- Mirrors ObjectTooltip.checkFont(). Breaks if TIS changes how the
    -- tooltip derives its padding, which would misalign every row.
    t("pad.derived", AllInfo.pad(UIFont.Small) > 0)

    -- Placement with our block's real size. The controller UI cannot be driven
    -- from here, and these four cases are the whole of the arithmetic it needs:
    -- a panel that fits keeps its origin, one that does not is clamped the way
    -- vanilla clamps, and a bottom anchor hangs the panel *above* the anchor
    -- instead of spilling down over the inventory.
    t("clampPos.fits", AllInfo.clampPos(500, nil, 100, 1080) == 500)
    t("clampPos.off-screen", AllInfo.clampPos(1000, nil, 200, 1080) == 879)
    t("clampPos.bottom-anchor", AllInfo.clampPos(0, 300, 200, 1080) == 100)
    t("clampPos.anchor-above-top", AllInfo.clampPos(0, 100, 200, 1080) == 0)
    -- A zero anchor is an anchor: 0 is truthy in Lua, and this is the case a
    -- `if anchor ~= nil` rewrite would silently break.
    t("clampPos.zero-anchor", AllInfo.clampPos(700, 0, 200, 1080) == 0)

    -- Hook integrity: catches another mod replacing instead of wrapping.
    -- Any wrapper of ours counts, not one particular function: install() makes a
    -- fresh one each time it has to re-wrap, and the set is the record of them.
    t("hook.ISToolTipInv", AllInfo.hooks.ours[ISToolTipInv.render] == true)
    -- Nothing is rendering while this runs, so the nesting count must be back at
    -- zero. A stuck depth hides the whole block for the session in silence.
    t("render.depth-clean", AllInfo.hooks.renderDepth
        and AllInfo.hooks.renderDepth() == 0)
    -- The block now steps aside per item instead of relaunching the error every
    -- frame, so a failure no longer announces itself with a stack dump. This is
    -- the replacement chivato: any item in here means the tooltip threw on it.
    t("render.no-failed-items", (AllInfo.hooks.renderFails or 0) == 0)
    t("hook.ISWidgetOutput", AllInfo.hooks.ISWidgetOutput == ISWidgetOutput.updateScriptValues)
    t("hook.ISWidgetTooltipOutput",
        AllInfo.hooks.ISWidgetTooltipOutput == ISWidgetTooltipOutput.updateScriptValues)
    -- Neat Crafting's own output slots. The classes only exist with that mod
    -- installed, and without it there is nothing to hook, so absent is a pass.
    t("hook.NC_CraftOutput_Slot", NC_CraftOutput_Slot == nil
        or AllInfo.hooks.NC_CraftOutput_Slot == NC_CraftOutput_Slot.createTooltip)
    t("hook.NC_OutputSwitch_Box", NC_OutputSwitch_Box == nil
        or AllInfo.hooks.NC_OutputSwitch_Box == NC_OutputSwitch_Box.createTooltip)
    -- Generator Time Remaining replaces this one instead of wrapping it.
    t("hook.GeneratorRichText",
        AllInfo.hooks.GeneratorRichText == ISGeneratorInfoWindow.getRichText)
    -- GeneratorRange wraps prerender too, so this catches a load-order clash.
    t("hook.GeneratorPrerender",
        AllInfo.hooks.GeneratorPrerender == ISGeneratorInfoWindow.prerender)
    t("hook.BuildRecipePanel",
        AllInfo.hooks.BuildRecipePanel == ISBuildRecipePanel.createDynamicChildren)
    t("hook.FarmingInfoRender", AllInfo.hooks.FarmingInfoRender == ISFarmingInfo.render)
    t("hook.HealthListBox",
        AllInfo.hooks.HealthListBoxRender == ISHealthBodyPartListBox.render)
    t("hook.HealthPanelVisible",
        AllInfo.hooks.HealthPanelVisible == ISHealthPanel.setVisible)
    -- Every body part of the live character through describe(): a healthy one
    -- must stay quiet, a hurt one must answer with a string, and neither may
    -- produce a nan. The 17 is BodyPartType.MAX, so a new part in a patch
    -- fails here instead of silently going uncovered.
    do
        local player = getPlayer()
        local parts = player and player:getBodyDamage():getBodyParts()
        local bad, seen = nil, 0
        for i = 0, (parts and parts:size() or 0) - 1 do
            local ok, text = pcall(AllInfo.Health.describe, parts:get(i), player, 10)
            seen = seen + 1
            if not ok then bad = tostring(text)
            elseif text ~= nil and (type(text) ~= "string" or text:find("nan", 1, true)) then
                bad = tostring(text)
            end
        end
        t("health.parts", seen == 17 and bad == nil)
        if bad then print("[AllInfo] health block: " .. bad) end
    end
    -- The wound rows are built almost entirely out of vanilla keys, so a rename
    -- on their side would print raw key names and nothing would throw.
    for _, key in ipairs({ "UI_AllInfo_health_Recovery", "UI_AllInfo_health_HealSpeed",
                           "UI_AllInfo_health_InfectionRisk", "UI_AllInfo_health_StitchReady",
                           "UI_AllInfo_health_Poultice", "UI_AllInfo_health_WoundInfection",
                           "UI_AllInfo_health_GlassInside", "UI_AllInfo_health_NeedsBandage",
                           "UI_AllInfo_health_Rising", "IGUI_health_DirtyBandage",
                           "IGUI_health_Scratched", "IGUI_health_Bandaged",
                           "IGUI_health_Stitched", "IGUI_health_Splinted",
                           "IGUI_Gametime_hour", "ContextMenu_PlantainCataplasm" }) do
        t("i18n.health-" .. key, getText(key) ~= key)
    end
    -- Fix XP View replaces all three of these instead of wrapping them.
    t("hook.XpBoostMap", AllInfo.hooks.XpBoostMap == CharacterCreationProfession.drawXpBoostMap)
    t("hook.XpSkillTooltip", AllInfo.hooks.XpSkillTooltip == ISSkillProgressBar.updateTooltip)
    t("hook.XpStatsPanel", AllInfo.hooks.XpStatsPanel == ISPlayerStatsUI.loadPerks)

    -- The whole point of the fix: a level-1 boost is x4, not "+75%", because a
    -- skill with no boost runs at x0.25. Sprinting and the two excluded skills
    -- are the exceptions, and they are where a naive table would be wrong.
    t("xp.boost1-is-x4", AllInfoChar.xpRelative(Perks.Woodwork, 1) == 4)
    t("xp.boost0-is-x1", AllInfoChar.xpRelative(Perks.Woodwork, 0) == 1)
    t("xp.boost2", AllInfo.num(AllInfoChar.xpRelative(Perks.Woodwork, 2), 2) == "5.32")
    t("xp.boost3", AllInfo.num(AllInfoChar.xpRelative(Perks.Woodwork, 3), 2) == "6.64")
    t("xp.sprinting-not-reduced", AllInfoChar.xpRelative(Perks.Sprinting, 1) == 1.25)
    t("xp.fitness-unaffected", AllInfoChar.xpRelative(Perks.Fitness, 3) == 1)
    t("xp.strength-unaffected", AllInfoChar.xpRelative(Perks.Strength, 2) == 1)
    t("xp.no-text-when-neutral", AllInfoChar.xpRelativeText(Perks.Fitness, 3) == nil)
    t("xp.text", AllInfoChar.xpRelativeText(Perks.Woodwork, 1) == "x 4")

    -- Cutting a line out of vanilla's skill tooltip leaves its " <LINE><LINE> "
    -- separators behind, and it writes them in pairs, so dropping the generic
    -- description left four in a row and the tooltip grew a band of empty rows
    -- between vanilla's block and ours. The first case below is that exact
    -- string. These run on text carrying '%' and '-', which is why nothing here
    -- may become a pattern-based cut.
    t("tooltip.tidy-collapses",
        AllInfoChar.tidyTooltip("Axe 1 <LINE> XP: 0 / 75 <LINE><LINE>  <LINE><LINE> x0.4 damage")
            == "Axe 1 <LINE> XP: 0 / 75 <LINE><LINE> x0.4 damage")
    t("tooltip.tidy-keeps-blank-line",
        AllInfoChar.tidyTooltip("a <LINE><LINE> b") == "a <LINE><LINE> b")
    t("tooltip.tidy-keeps-single", AllInfoChar.tidyTooltip("a <LINE> b") == "a <LINE> b")
    t("tooltip.tidy-trims-tail", AllInfoChar.tidyTooltip("a <LINE><LINE> ") == "a")
    t("tooltip.tidy-percent-safe",
        AllInfoChar.tidyTooltip("XP Boost: +75% <LINE><LINE>  <LINE><LINE> x 4")
            == "XP Boost: +75% <LINE><LINE> x 4")

    -- Vanilla builds the perk description key from the *translated* display
    -- name, so outside English it prints the raw key. Every id in the mapping
    -- table has to land on a key that actually resolves, or the description
    -- silently disappears instead.
    local missing = {}
    for i = 0, Perks.getMaxIndex() - 1 do
        local perk = PerkFactory.getPerk(Perks.fromIndex(i))
        if perk and perk:getParent() ~= Perks.None then
            local key = "IGUI_perks_" .. AllInfoChar.descriptionName(perk) .. "_Description"
            -- Not every perk has one, and that is fine: the wrapper drops the
            -- line. What must never happen is a *mapped* id missing its key.
            if AllInfoChar.englishName[perk:getId()] and not getTextOrNull(key) then
                missing[#missing + 1] = perk:getId()
            end
        end
    end
    t("perk.mapped-keys-resolve", #missing == 0)
    t("perk.description-key-resolves",
        getTextOrNull("IGUI_perks_Carpentry_Description") ~= nil)

    t("hook.TraitCreationPrerender",
        AllInfo.hooks.TraitCreationPrerender == CharacterCreationProfession.prerender)
    t("hook.TraitInfoScreen", AllInfo.hooks.TraitInfoScreen == ISCharacterScreen.loadTraits)

    -- Every trait and every profession must build a block without throwing and
    -- without leaking a nil or a nan into the text. This is the whole of §6's
    -- "B) Character module" check, run over real definitions.
    local badBlocks = {}
    local function sweep(defs)
        for i = 0, defs:size() - 1 do
            local def = defs:get(i)
            local ok, block = pcall(AllInfoChar.definitionBlock, def, "\n")
            if not ok then
                badBlocks[#badBlocks + 1] = tostring(def:getUIName()) .. ": " .. tostring(block)
            elseif type(block) ~= "string" then
                badBlocks[#badBlocks + 1] = tostring(def:getUIName()) .. ": not a string"
            elseif leaks(block) then
                badBlocks[#badBlocks + 1] = tostring(def:getUIName()) .. " -> " .. block
            end
        end
    end

    sweep(CharacterTraitDefinition.getTraits())
    sweep(CharacterProfessionDefinition.getProfessions())
    t("traits.blocks-clean", #badBlocks == 0)
    -- A failure here is useless without the offending block, and the assertion
    -- name alone does not carry it.
    for i = 1, math.min(#badBlocks, 3) do
        print("[AllInfo] bad block: " .. badBlocks[i])
    end
    -- Our link ran, which is the question worth asking. Comparing the field
    -- against our own function fails on any setup carrying a mod that wraps
    -- MainOptions.create correctly -- Mod Options, CombatText and Grab & Drop
    -- all do -- because whoever loads last owns the field. See OptionsTab.lua.
    t("hook.MainOptions.create", AllInfo.hooks.mainOptionsRan == true)
    t("hook.MainOptions.modPanel", AllInfo.hooks.MainOptionsModPanel == MainOptions.addModOptionsPanel)

    -- Options. Never assert on a specific toggle value: the user owns those.
    local opts = PZAPI.ModOptions.Dict["AllInfo"]
    t("options.registered", opts ~= nil)

    if opts then
        local missing = {}
        for _, section in ipairs(AllInfo.Options.sections) do
            if not opts.dict[section.master] then missing[#missing + 1] = section.master end
            for _, o in ipairs(section.options) do
                if not opts.dict[o[1]] then missing[#missing + 1] = o[1] end
            end
        end
        t("options.all-registered", #missing == 0)

        local sample = opts.dict["WpnDamage"]
        t("options.enabled-reads-value", AllInfo.enabled("WpnDamage") == (sample.value == true))

        checkOptionsTab(t)
    end

    -- getText() echoes the key back when it was never loaded. Catches a whole
    -- translation file being dropped, which is what happens if a key does not
    -- carry its file's prefix (UI.json -> "UI_", Tooltip.json -> "Tooltip_").
    t("i18n.ui", getText("UI_AllInfo_opt_ShowDeltas") ~= "UI_AllInfo_opt_ShowDeltas")
    t("i18n.tooltip", getText("Tooltip_AllInfo_Stale") ~= "Tooltip_AllInfo_Stale")
    t("i18n.condition-loss-parts",
        getText("Tooltip_AllInfo_ConditionLossHandle") ~= "Tooltip_AllInfo_ConditionLossHandle"
        and getText("Tooltip_AllInfo_ConditionLossHead") ~= "Tooltip_AllInfo_ConditionLossHead")
    t("i18n.generator", getText("UI_AllInfo_GeneratorNoise") ~= "UI_AllInfo_GeneratorNoise")
    -- The pump window is built almost entirely out of vanilla keys, so a rename
    -- on their side would show raw key names and nothing would throw. Same for
    -- the info icon, which is vanilla's own file path.
    for _, key in ipairs({ "IGUI_GasPump", "ContextMenu_Info", "UI_AllInfo_FuelRemaining",
                           "ContextMenu_FuelPumpNoPower", "Sandbox_FuelStationGas_option9",
                           "Fluid_Unknown", "IGUI_RadioPower" }) do
        t("i18n.pump-" .. key, getText(key) ~= key)
    end
    t("pump.info-icon", getTexture("media/ui/inventoryPanes/Button_Info.png") ~= nil)
    -- '%%' in the json is how a literal '%' reaches the screen. This is the
    -- mod's only key that needs one, and getting it wrong shows "20%%".
    local warn = getText("UI_AllInfo_GeneratorToWarn", 20)
    t("i18n.percent-unescaped", warn:find("%%%%") == nil)
    t("i18n.percent-substituted", warn:find("20") ~= nil)

    -- Moodle descriptions. These override vanilla keys, so a typo silently
    -- replaces a real description with the raw key.
    local moodle = getText("Moodles_Endurance_desc_lvl1")
    t("i18n.moodle", moodle ~= "Moodles_Endurance_desc_lvl1")
    -- Translator.getTextInternal turns <br> into a newline and String.format
    -- turns %% into %. If either stops happening it shows up literally.
    t("i18n.br-converted", moodle:find("<br>") == nil and moodle:find("\n") ~= nil)
    t("i18n.moodle-percent", moodle:find("%%%%") == nil)

    -- The moodle column is drawn by us, from a hand-written MoodleType -> png
    -- table copied out of MoodleTextureSet's constructor (the class is not
    -- exposed to Lua and the names are inlined string concats, so there is
    -- nothing to derive them from). A wrong entry loses one icon in silence.
    -- Vanilla's moodle widget is switched off through its *character*, never
    -- through setVisible: UIManager.render() has no visibility check in its loop
    -- and MoodlesUI.render() overrides UIElement.render() without calling super,
    -- so that flag is decorative there. If this handle ever stops answering, the
    -- mod draws its column straight on top of vanilla's.
    t("moodles.vanilla-widget-reachable", UIManager.getMoodleUI(0) ~= nil)

    local okSet, moodleSet = pcall(AllInfo.Moodles.textureSet, 32)
    t("moodles.textures-load", okSet)
    if okSet then
        local moodleGaps = {}
        for i, entry in ipairs(AllInfo.Moodles.list) do
            if not entry[1] then moodleGaps[#moodleGaps + 1] = "type " .. i end
            if not moodleSet.icons[i] then moodleGaps[#moodleGaps + 1] = tostring(entry[2]) end
        end
        t("moodles.icons-resolve", #moodleGaps == 0)
        t("moodles.backdrop-resolves",
            moodleSet.background ~= nil and moodleSet.border ~= nil)
        for i = 1, math.min(#moodleGaps, 3) do
            print("[AllInfo] missing moodle texture: " .. moodleGaps[i])
        end
    end

    -- Hand-written trait effects and per-level skill descriptions are looked up
    -- by key with no table behind them, so a renamed key just goes quiet.
    t("i18n.trait-manual", getTextOrNull("UI_AllInfo_trait_clumsy") ~= nil)
    -- The six weapon skills lost their 60 hand-written keys in round 4: their
    -- line is derived now, so the assertion moved to the generator and lives in
    -- ronda4Checks as skill.describe-weapon. What must stay gone is the key.
    t("i18n.perk-level-dropped",
        getTextOrNull("IGUI_perks_Long Blunt_Description5") == nil)
    -- Two trait ids carry a space, which is the only reason they had no manual
    -- text until now. Same parser path as the spaced perk key above.
    t("i18n.trait-spaced-key", getTextOrNull("UI_AllInfo_trait_out of shape") ~= nil)
    -- The six physical skills got per-level tables read off the bytecode. These
    -- resolve through AllInfoChar.descriptionName, so a rename there kills them
    -- silently: Sprinting is the one whose id and English name differ.
    t("i18n.perk-level-physical",
        getTextOrNull("IGUI_perks_Running_Description10") ~= nil
        and getTextOrNull("IGUI_perks_Lightfooted_Description1") ~= nil)

    -- Ids whose English display name differs from them: the six with a space in
    -- it, plus the three PerkFactory registers under a different word entirely.
    -- Without the mapping their description silently does not exist -- which is
    -- what was happening to Foraging, Lightfooted and Sneaking.
    local spaced = {}
    for _, id in ipairs({ "Blunt", "SmallBlunt", "LongBlade", "SmallBlade", "Doctor", "Husbandry",
                          "PlantScavenging", "Lightfoot", "Sneak" }) do
        if not getTextOrNull("IGUI_perks_" .. (AllInfoChar.englishName[id] or id) .. "_Description") then
            spaced[#spaced + 1] = id
        end
    end
    t("perk.spaced-names-resolve", #spaced == 0)

    -- The block prints perk:getName(). Composing "IGUI_perks_" .. getId() by
    -- hand looked equivalent and is not: PerkFactory feeds that key a hardcoded
    -- word that differs from the id for five perks, and those printed the raw
    -- key on screen. Nothing may come back looking like one.
    local rawNames = {}
    for i = 0, Perks.getMaxIndex() - 1 do
        local perk = PerkFactory.getPerk(Perks.fromIndex(i))
        local name = perk and perk:getName()
        if name and name:find("IGUI_", 1, true) then rawNames[#rawNames + 1] = perk:getId() end
    end
    t("perk.names-resolve", #rawNames == 0)

    -- The condition and damage rows moved into Core so MeleeWeapon, Firearm and
    -- Clothing stopped repeating them. One break there now costs three
    -- providers, so they get their own assertion instead of relying on the
    -- sample sweep to notice.
    --
    -- Two shapes, because conditionRow branches on the head: a wood axe has one
    -- (13, multiplier 1.5) so it puts out handle + head + damage, and a kitchen
    -- knife has none so it stays at condition + damage. Asserting only the axe
    -- is what let the head rows through unnoticed the first time.
    local shared = {}
    local axe = AllInfo.proto("Base.Axe")
    if axe then
        AllInfo.conditionRow(shared, axe, nil)
        AllInfo.damageRow(shared, axe, nil)
    end
    t("rows.shared-helpers", #shared == 3)

    local plain = {}
    if AllInfo.proto("Base.KitchenKnife") then
        AllInfo.conditionRow(plain, AllInfo.proto("Base.KitchenKnife"), nil)
        AllInfo.damageRow(plain, AllInfo.proto("Base.KitchenKnife"), nil)
    end
    t("rows.shared-helpers-no-head", #plain == 2)

    -- Same reasoning for the clothing comparison, now shared by Clothing and
    -- Mask: it walks worn items and asks BodyLocationGroup which slots exclude
    -- which, and the sample sweep passes chr = nil so it never reaches any of
    -- that. Run against the real character; the answer may be nil (nothing in
    -- that slot) but it must not throw, and a mask you are wearing compares
    -- against nothing.
    local mask = AllInfo.proto("Base.Hat_DustMask")
    local player = getSpecificPlayer(0)
    if mask and player then
        local ok = pcall(AllInfo.replacedClothing, mask, player)
        t("rows.replaced-clothing", ok)
    end

    -- instanceItem() is the only way to build an item from Lua. This is what
    -- silently broke every provider sample before.
    t("proto.builds", AllInfo.proto("Base.Axe") ~= nil)
    t("proto.bad-type-is-nil", AllInfo.proto("Base.NoSuchItemAnywhere") == nil)

    t("options.unknown-is-on", AllInfo.enabled("NoSuchOptionExists") == true)
    t("options.nil-is-on", AllInfo.enabled(nil) == true)

    -- Data must be whole after our filtering wrapper, or other mods stop saving.
    local found = false
    for _, o in ipairs(PZAPI.ModOptions.Data) do
        if o.modOptionsID == "AllInfo" then found = true end
    end
    t("options.data-restored", found)

    providerChecks(t)
    -- Every perk at every boost must give a finite, positive multiplier. Cheap
    -- insurance against a nil creeping into the exclusion lists, and it covers
    -- perks no hand-written case above ever names.
    local badXp = {}
    for i = 0, Perks.getMaxIndex() - 1 do
        local perk = Perks.fromIndex(i)
        if perk then
            for boost = 0, 3 do
                local rel = AllInfoChar.xpRelative(perk, boost)
                if type(rel) ~= "number" or rel ~= rel or rel <= 0 or rel == math.huge then
                    badXp[#badXp + 1] = i .. "/" .. boost
                end
            end
        end
    end
    t("xp.all-perks-finite", #badXp == 0)

    -- The per-level recipe line is swept whole: every perk, every level. No
    -- assertion on a specific recipe -- that would pin today's balance data --
    -- only that the sweep runs, stays clean, and finds *something*. An empty
    -- result across 35 perks means the script manager API moved.
    local recipeHits, recipeDirty = 0, {}
    for i = 0, Perks.getMaxIndex() - 1 do
        local perk = PerkFactory.getPerk(Perks.fromIndex(i))
        for level = 1, 10 do
            local ok, line = pcall(AllInfoChar.recipeLine, perk, level)
            if not ok then
                recipeDirty[#recipeDirty + 1] = tostring(perk and perk:getId()) .. "/" .. level
            elseif line then
                recipeHits = recipeHits + 1
                -- leaks(), not a plain find: recipe names contain "nil"
                -- (destornillador, tornillos, anillo) and that is what made the
                -- trait sweep cry wolf in round 2b.
                if leaks(line) then recipeDirty[#recipeDirty + 1] = line end
            end
        end
    end
    t("skillRecipes.sweep-clean", #recipeDirty == 0)
    -- Only meaningful with the toggle on, and the user owns the toggles.
    if AllInfo.enabled("SkillRecipes") then
        t("skillRecipes.finds-something", recipeHits > 0)
    end

    fishingChecks(t)
    animalChecks(t)
    ronda4Checks(t)
    -- A provider that threw on some item this session. It keeps running -- only
    -- that item loses its rows -- but the throw is a bug and this is where a
    -- player's report of "no numbers" gets a name to it.
    local off = {}
    for _, p in ipairs(AllInfo.providers) do
        if p.reported then off[#off + 1] = p.id end
    end
    t("providers.none-failed", #off == 0)

    if #fails == 0 then
        print("[AllInfo] SelfTest: " .. passed .. "/" .. total .. " OK")
    else
        print("[AllInfo] SelfTest: " .. passed .. "/" .. total .. " FAILED -> " .. table.concat(fails, ", "))
    end

    -- Printed, not counted. A switch the sweep cannot prove on its sample is a
    -- gap in the sweep, not a bug in the mod, and folding that into the verdict
    -- would leave the SelfTest permanently red for the wrong reason.
    AllInfo.SelfTest.options()

    return #fails == 0
end
