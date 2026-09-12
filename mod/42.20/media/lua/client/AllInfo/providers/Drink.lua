require "AllInfo/Core"

-- What a drink actually does to you. Vanilla shows none of it: FluidContainer
-- .DoTooltip() paints the fluid's name, the mixture if there is one, and the
-- "Tainted" label, and stops there. A beer, a canteen and a carton of juice all
-- look the same.
--
-- Every label here is a vanilla key -- Fluid_Prop_* and Fluid_Poison* are a
-- complete set shipped for the fluid transfer panel -- so this file adds no
-- translation keys of its own and is right in all 29 languages.

-- The container has already done the arithmetic. getProperties() accumulates
--     addFromMultiplied(fluid.getProperties(), litres * share)
-- over every fluid inside, so it *is* what you get for drinking what is in
-- there right now, mixtures included. Nothing to scale by hand.
--
-- ⚠️ The script numbers are not in the units they look like. Water declares
-- ThirstChange = -50 and a full 1 L bottle measures -0.5, because
-- CharacterStat registers Thirst on a 0..1 bar: that -50 is fifty hundredths of
-- the bar, i.e. half your thirst. Measured in game 02-09-2026, three
-- containers, exact to the last decimal. The ranges, from CharacterStat:
--
--     Thirst, Hunger, Fatigue, Stress, Endurance   0..1    -> x100 for a %
--     Boredom, Unhappiness, Poison, Intoxication   0..100  -> already a %
--
-- Hence two lists below instead of one.

-- { label key, getter, higher is better }. Fractions of their own bar.
local BAR = {
    { "Fluid_Prop_Thirst",  function(p) return p:getThirstChange() end,  false, "DrinkThirst" },
    { "Fluid_Prop_Hunger",  function(p) return p:getHungerChange() end,  false, "DrinkHunger" },
    { "Fluid_Prop_Fatigue", function(p) return p:getFatigueChange() end, false, "DrinkFatigue" },
    { "Fluid_Prop_Stress",  function(p) return p:getStressChange() end,  false, "DrinkStress" },
}

-- Already points out of a hundred. getUnhappyChange() feeds BOREDOM *and*
-- UNHAPPINESS with the same figure in DrinkFluid, so it is one row, not two.
local POINTS = {
    { "Fluid_Prop_Unhappy", function(p) return p:getUnhappyChange() end, "DrinkUnhappy" },
}

-- Absolute amounts, not bars.
local NUTRIENTS = {
    { "Fluid_Prop_Calories",      function(p) return p:getCalories() end,      0, "DrinkCalories" },
    { "Fluid_Prop_Carbohydrates", function(p) return p:getCarbohydrates() end, 1, "DrinkCarbs" },
    { "Fluid_Prop_Proteins",      function(p) return p:getProteins() end,      1, "DrinkProteins" },
    { "Fluid_Prop_Lipids",        function(p) return p:getLipids() end,        1, "DrinkFat" },
}

-- No rows for painReduction, fluReduction, enduranceChange or
-- foodSicknessChange: all 31 vanilla fluids declare them as zero, so they would
-- never draw. The guards below are per-value anyway, so a mod that uses one
-- only needs its line adding here.

-- BodyDamage.JustDrankBoozeFluid(): stats.add(INTOXICATION, drunkIncrease *
-- alcohol), on a 0..100 bar, with drunkIncrease defaulting to 400. So a 0.3 L
-- beer at alcohol 0.015 is six points of drunk, and a litre of brandy is 160,
-- which is the bar and then some.
--
-- ponytail: the hunger multiplier is left out. The same method scales the
-- result by 1.25 on a fairly empty stomach and 1.1 on a full one, and that is a
-- property of the moment you drink, not of the bottle.
local DRUNK_DEFAULT = 400

local function drunkPoints(chr, alcohol)
    local rate = DRUNK_DEFAULT
    if chr then
        local bd = chr:getBodyDamage()
        local v = bd and bd:getDrunkIncreaseValue()
        if type(v) == "number" and v > 0 then rate = v end
    end
    return alcohol * rate
end

-- IsoGameCharacter.DrinkFluid(), poison branch, in this exact order. Iron Gut
-- does not halve tainted water, it cancels it outright; the halving is for
-- every other poison except bleach. Weak Stomach is x1.2 tainted and x2
-- otherwise. Both of ours said -50% / +50% and both were wrong.
local function poisonFor(chr, container, poison)
    if poison <= 0 then return 0 end

    local tainted = container:isTainted()
    if tainted then poison = poison * 0.75 end
    if not chr then return poison end

    -- DrinkFluid tests getPrimaryFluid().getFluidType() == FluidType.Bleach,
    -- and isPrimaryFluidType is that same test with a null check in it.
    local bleach = FluidType and container:isPrimaryFluidType(FluidType.Bleach)

    if chr:hasTrait(CharacterTrait.IRON_GUT) then
        if tainted then return 0 end
        if not bleach then poison = poison / 2 end
    elseif chr:hasTrait(CharacterTrait.WEAK_STOMACH) then
        poison = poison * (tainted and 1.2 or 2)
    end

    return poison
end

AllInfo.register("Drink", 12, nil, function(out, item, chr)
    -- getFluidContainerFromSelfOrWorldItem, not getFluidContainer: an item lying
    -- on the ground keeps its fluid on the IsoWorldInventoryObject, so the plain
    -- getter comes back empty and the block silently vanished when you looked at
    -- a bottle at your feet. The world-aware getter answers for both.
    local container = item:getFluidContainerFromSelfOrWorldItem()
        or item:getFluidContainer()
    if not container or container:isEmpty() then return end

    local props = container:getProperties()
    if not props then return end

    for i = 1, #BAR do
        local label, get, higherIsBetter = BAR[i][1], BAR[i][2], BAR[i][3]
        local v = get(props)
        if v and v ~= 0 then
            AllInfo.rowIf(out, BAR[i][4], getText(label), AllInfo.signed(v * 100, 1) .. "%",
                AllInfo.color(higherIsBetter == (v > 0)))
        end
    end

    for i = 1, #POINTS do
        local v = POINTS[i][2](props)
        if v and v ~= 0 then
            AllInfo.rowIf(out, POINTS[i][3], getText(POINTS[i][1]), AllInfo.signed(v, 1) .. "%",
                AllInfo.color(v < 0))
        end
    end

    for i = 1, #NUTRIENTS do
        local v = NUTRIENTS[i][2](props)
        if v and v ~= 0 then
            AllInfo.rowIf(out, NUTRIENTS[i][4], getText(NUTRIENTS[i][1]), AllInfo.num(v, NUTRIENTS[i][3]))
        end
    end

    local alcohol = props:getAlcohol()
    if alcohol and alcohol > 0 then
        AllInfo.rowIf(out, "DrinkAlcohol", getText("Fluid_Prop_Alcohol"),
            AllInfo.num(drunkPoints(chr, alcohol), 1) .. "%", AllInfo.color(false))
    end

    -- Poison stays quiet when the game is hiding it. isTaintedStatusKnown() is
    -- false with the enableTaintedWaterText sandbox option off, which is a
    -- server deliberately not telling you the water is bad, and vanilla's own
    -- inventory pane gates on the same call. Bleach is always known.
    local poison = props:getPoison()
    if poison and poison > 0 and container:isTaintedStatusKnown() then
        -- The figure only. PoisonEffect.getLevel() used to be appended as a
        -- "(Medium)" band next to it, and every drinkable fluid in the game
        -- lands on the same band, so the word carried no information and read
        -- like a second, vaguer opinion about the number beside it.
        local value = poisonFor(chr, container, poison)
        local text = AllInfo.num(value, 1) .. "%"

        AllInfo.rowIf(out, "DrinkPoison", getText("Fluid_Poison"), text, AllInfo.color(value <= 0))
    end
end)
