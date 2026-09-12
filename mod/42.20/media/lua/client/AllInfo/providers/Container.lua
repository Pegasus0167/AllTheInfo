require "AllInfo/Core"

-- What a bag costs you to carry.
--
-- InventoryContainer.DoTooltip() already prints capacity, weight reduction and
-- max item size, and InventoryItem's own Weight row already gives the equipped
-- and the unequipped figure side by side, so none of that is repeated here.
-- What nothing in the game shows is the speed you pay for the space, which is
-- the whole of the choice between one bag and another.
--
-- IsoGameCharacter.calcRunSpeedModByBag(bag), verified in bytecode:
--
--     float mod = bag.getScriptItem().runSpeedModifier - 1;
--     float fill = bag.getContentsWeight() / bag.getEffectiveCapacity(chr);
--     return mod * (1 + fill / 2);
--
-- calculateBaseSpeed() sums that over every worn bag *and* over a bag in either
-- hand, so one you are only carrying costs exactly what one on your back costs.
-- The fill half is the part players never see: the same bag goes from -3 % empty
-- to -4.5 % full, and a bag stuffed past its capacity keeps going past that.
-- getEffectiveCapacity() is asked with the character because it is the one that
-- knows about Organized and Disorganized.
--
-- combatSpeedModifier is flat, with no fill term, and only counts while worn:
-- updateSpeedModifiers() adds it inside the wornItems loop and the hands are not
-- in that loop. Five vanilla bags carry one.
local FILL_WEIGHT = 2      -- the /2 above: a full bag is 1.5 times its penalty

AllInfo.Container = AllInfo.Container or {}

-- Both modifiers exist only as public *fields* of zombie.scripting.objects.Item.
-- There is no getter for either, and public fields do not reach Lua (trap 3;
-- LuaJavaClassExposer exposes methods and statics, and nothing else). So the
-- value is read from the same place the engine read it: BaseScriptObject
-- .getScriptLines() hands back the loaded script bodies as lines, newest body
-- first, which is also the order in which a mod overriding an item wins. The
-- first match is therefore the effective value. Verified in game on
-- Bag_Schoolbag, where the dump carries "RunSpeedModifier = 0.97,".
--
-- ponytail: text parsing for two numbers. The day TIS adds a getter, delete
-- scriptNumber() and call it instead; nothing else in this file changes.
local cache = {}

function AllInfo.Container.scriptNumber(item, key)
    -- Memoised per item type: getScriptLines() caches on the Java side, but the
    -- sweep over 25 lines does not, and this runs under a moving cursor.
    local id = item:getFullType()
    local byKey = cache[id]
    if not byKey then
        byKey = {}
        cache[id] = byKey
    end

    local hit = byKey[key]
    if hit ~= nil then
        if hit == false then return nil end
        return hit
    end

    local script = item:getScriptItem()
    local lines = script and script:getScriptLines()
    local found

    if lines then
        for i = 0, lines:size() - 1 do
            local v = string.match(lines:get(i),
                "^%s*" .. key .. "%s*=%s*(%-?%d*%.?%d+)")
            if v then
                found = tonumber(v)
                break
            end
        end
    end

    byKey[key] = found or false     -- remember the miss, don't sweep per frame
    return found
end

-- The run penalty this bag would cost, as a percentage, at the load it is
-- carrying right now. nil when the bag has no modifier, which is what a script
-- without the line means.
function AllInfo.Container.runPenalty(bag, chr)
    local base = AllInfo.Container.scriptNumber(bag, "RunSpeedModifier")
    if not base or base == 1 then return nil end

    local capacity = chr and bag:getEffectiveCapacity(chr) or bag:getCapacity()
    local fill = 0
    if capacity and capacity > 0 then
        fill = bag:getContentsWeight() / capacity
    end

    return (base - 1) * (1 + fill / FILL_WEIGHT) * 100
end

-- The bag this one would replace: whatever is already on that slot. Bags are not
-- Clothing, so AllInfo.replacedClothing cannot answer this. A bag in the primary
-- hand is a fair comparison too and AllInfo.compareTo covers it, but the useful
-- one is nearly always the pack already on your back.
local function replaced(item, chr)
    if not chr or not AllInfo.enabled("ShowDeltas") then return nil end

    -- wornItems.contains(), an identity check inside Java, so it beats an ==
    -- between two Lua-wrapped Java objects.
    if chr:isEquippedClothing(item) then return nil end

    local where = item:canBeEquipped()
    local worn = where and chr:getWornItem(where)
    if worn and instanceof(worn, "InventoryContainer") then return worn end

    return AllInfo.compareTo(item, chr)
end

AllInfo.register("Container", 36, nil, function(out, item, chr)
    if not instanceof(item, "InventoryContainer") then return end

    local other = replaced(item, chr)
    if other and not instanceof(other, "InventoryContainer") then other = nil end

    -- Both labels are vanilla's, so this reads right in the 29 languages the
    -- game ships. Printed as the penalty itself, the way Clothing.lua prints
    -- the same two for garments: 0.97 becomes -3 %.
    local run = AllInfo.Container.runPenalty(item, chr)
    if run then
        AllInfo.rowIf(out, "BagRun", getText("Tooltip_RunSpeedModifier"),
            AllInfo.signed(run, 1) .. "%", nil,
            AllInfo.delta(run, other and AllInfo.Container.runPenalty(other, chr),
                true, 1, "%"))
    end

    local combat = AllInfo.Container.scriptNumber(item, "CombatSpeedModifier")
    if combat and combat ~= 1 then
        local otherCombat = other
            and AllInfo.Container.scriptNumber(other, "CombatSpeedModifier")
        AllInfo.rowIf(out, "BagCombat", getText("Tooltip_CombatSpeedModifier"),
            AllInfo.signed((combat - 1) * 100, 1) .. "%", nil,
            AllInfo.delta((combat - 1) * 100,
                otherCombat and (otherCombat - 1) * 100, true, 1, "%"))
    end
end)
