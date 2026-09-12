require "AllInfo/Core"

-- Clothing.DoTooltip() paints nine values as bars only (setProgress, no number
-- on them): condition, insulation, wind, water, blood, dirt, wetness and the
-- run and combat speed modifiers. Same situation as Condition and Damage on a
-- weapon, so the same answer: the figure goes next to the bar. Bite/scratch/
-- bullet defense already come out as numbers *and* compared, so they are left
-- alone.
--
-- getDiscomfortModifier() is the one value vanilla never shows on the item at
-- all. Every piece of clothing has one (0.02 to 0.75 across the scripts) and it
-- is what feeds the Uncomfortable moodle.
--
-- Scales are read off the bytecode, not guessed: insulation, wind and water go
-- into setProgress() raw, so they are 0..1; blood, dirt and wetness are divided
-- by 100 on the way in, so they are 0..100.
--
-- Every label already exists in vanilla, so this provider adds no translation
-- keys and inherits all 29 languages. Getters are wrapped in closures because
-- Java methods cannot be indexed as fields from Lua (they come back nil).

-- { label, getter, higher is better }, all 0..1 ratios shown as percentages.
local RATIOS = {
    { "Tooltip_item_Insulation",  function(c) return c:getInsulation() end,      true, "ClothInsulation" },
    { "Tooltip_item_Windresist",  function(c) return c:getWindresistance() end,  true, "ClothWind" },
    { "Tooltip_item_Waterresist", function(c) return c:getWaterResistance() end, true, "ClothWater" },
}

-- Run and combat speed are multipliers around 1 that vanilla paints as a bar of
-- "how far from 1", with no number and no sign, so a bar can mean -3% or +3%.
-- Printed as the penalty itself: 0.97 becomes -3%. The row only exists when
-- there is a modifier, which is also the only time vanilla draws its bar.
local SPEEDS = {
    { "Tooltip_RunSpeedModifier",    function(c) return c:getRunSpeedModifier() end, "ClothRun" },
    { "Tooltip_CombatSpeedModifier", function(c) return c:getCombatSpeedModifier() end, "ClothCombat" },
}

-- 0..100, and only worth a row once there is something to report: a clean dry
-- shirt would otherwise add three rows of zero.
local STATES = {
    { "Tooltip_clothing_bloody", function(c) return c:getBloodLevel() end, "ClothBlood" },
    { "Tooltip_clothing_dirty",  function(c) return c:getDirtiness() end, "ClothDirt" },
    { "Tooltip_clothing_wet",    function(c) return c:getWetness() end, "ClothWet" },
}

AllInfo.register("Clothing", 35, nil, function(out, item, chr)
    if not instanceof(item, "Clothing") then return end

    -- Shared with Mask.lua, which compares the same way.
    local other = AllInfo.replacedClothing(item, chr)

    -- Compares what each garment has left, same as every other condition row.
    if AllInfo.enabled("ClothCondition") then AllInfo.conditionRow(out, item, other) end

    for i = 1, #RATIOS do
        local label, get, higherIsBetter = RATIOS[i][1], RATIOS[i][2], RATIOS[i][3]
        AllInfo.rowIf(out, RATIOS[i][4], getText(label), AllInfo.pct(get(item), 1),
            nil, AllInfo.deltaPct(get(item), other and get(other), higherIsBetter, 1))
    end

    for i = 1, #SPEEDS do
        local label, get = SPEEDS[i][1], SPEEDS[i][2]
        local v = get(item)
        if v ~= 1 then
            AllInfo.rowIf(out, SPEEDS[i][3], getText(label), AllInfo.signed((v - 1) * 100, 1) .. "%",
                nil, AllInfo.deltaPct(v, other and get(other), true, 1))
        end
    end

    -- A 0..1 ratio like the three above, and for the same verified reason:
    -- InventoryItem's tooltip feeds it to setProgress() raw. Vanilla draws a
    -- negative one as a bar of the same length in the good colour, so a comfy
    -- piece is worth a row too.
    local discomfort = item:getDiscomfortModifier()
    if discomfort ~= 0 then
        AllInfo.rowIf(out, "ClothDiscomfort", getText("Tooltip_item_Discomfort"), AllInfo.pct(discomfort, 1),
            nil, AllInfo.deltaPct(discomfort, other and other:getDiscomfortModifier(), false, 1))
    end

    -- Stomping a downed zombie is CombatManager: Rand(0.7, 1) + Strength * 0.2,
    -- and then *= the shoes' StompPower, or *= 0.5 with nothing on. It only ever
    -- reads getWornItem(SHOES), so the row belongs to footwear and nowhere else.
    -- Clothing defaults the field to 1, which is what the six crafted wraps get.
    -- A multiplier around 1, so it reads as a percentage: 2.5 is 250%.
    if item:getBodyLocation() == ItemBodyLocation.SHOES then
        AllInfo.rowIf(out, "ClothStomp", getText("Tooltip_AllInfo_StompPower"),
            AllInfo.pct(item:getStompPower(), 0), nil,
            AllInfo.deltaPct(item:getStompPower(), other and other:getStompPower(), true, 0))
    end

    for i = 1, #STATES do
        local label, get = STATES[i][1], STATES[i][2]
        local v = get(item)
        if v > 0 then
            AllInfo.rowIf(out, STATES[i][3], getText(label), AllInfo.num(v, 0) .. " / 100")
        end
    end
end)
