require "AllInfo/Core"
require "ISUI/ISGeneratorInfoWindow"

AllInfo.Generator = AllInfo.Generator or {}

-- Extra lines under vanilla's generator info window.
--
-- Vanilla (ISGeneratorInfoWindow.getRichText) already shows the fuel
-- percentage, the condition, every powered appliance *with its own draw*, the
-- generator's base draw and the total. Plan 2 §1.4 asked for per-appliance
-- consumption: B42.20 already has it, so there is nothing to add there.
--
-- What vanilla never says is how long the tank lasts, how long the machine
-- lasts, how likely it is to set the place on fire, and how far it can be
-- heard. The reach is drawn on the ground instead, in GeneratorRange.lua.

-- Everything below is per generator model, read from its own script item, so
-- the four vanilla ones (30 / 36 / 24 / 25 wear, 20 / 20 / 23 / 25 noise) and
-- any modded one work without a table of names.
local function script(object)
    local itemType = object:getGeneratorItemType()
    return itemType and getScriptManager():getItem(itemType)
end

-- Fuel drain, straight out of IsoGenerator.update(): once per in-game hour,
--     fuel -= totalPowerUsing * SandboxOptions.generatorFuelConsumption
--
-- Two traps in there, both of which plan 2 §1.3 got wrong:
--   * getTotalPowerUsing() *already* multiplies by generatorFuelConsumption,
--     so applying the sandbox multiplier again would halve or tenth the
--     answer. (getTotalPowerUsingString(), which vanilla prints, does not.)
--   * getMaxFuel() is a hardcoded 10.0 and getFuel() is on that same 0..10
--     scale. getFuelPercentage() is the 0..100 one. Treating getFuel() as a
--     percentage overstates the time by 10x.
local function fuelHours(object)
    local perHour = object:getTotalPowerUsing()
    if not perHour or perHour <= 0 then return nil end   -- never divide by zero

    local fuel = object:getFuel()
    if not fuel or fuel <= 0 then return nil end

    return fuel / perHour
end

-- Wear, from the same hourly loop:
--     if Rand.Next(conditionLowerChance) == 0 then condition -= Rand.Next(2)+1
-- so it loses 1 or 2 points, 1 hour in N. That averages 1.5/N per hour, and an
-- average is all this can ever be: the roll is random, so the row is labelled
-- as one and never dressed up as a countdown.
-- conditionLowerChance comes from the generator's script item, or 30 when
-- there is none -- the same fallback Java uses.
local AVG_LOSS = 1.5

local function hoursToCondition(object, target)
    local condition = object:getCondition()
    if condition <= target then return nil end

    local item = script(object)
    local chance = item and item:getConditionLowerChance() or 30
    if chance <= 0 then return nil end

    return (condition - target) * chance / AVG_LOSS
end

-- Danger bands, read off IsoGenerator.update(). All of it fires once per
-- in-game hour, and only while the generator is running.
--   backfire (a loud 40-tile, volume-60 world sound, nothing else):
--       condition <= 20 -> 1 in 5, <= 30 -> 1 in 10, <= 40 -> 1 in 15
--   at condition <= 20, and only there:
--       1 in 10  -> StartFire, condition = 0, generator off
--       else 1 in 20 -> explode(), condition = 0
--   so the catastrophic odds are 1/10 + 9/10 * 1/20 = 14.5% per hour.
-- ponytail: these five numbers are private static finals inlined by the
-- compiler, so they cannot be read at runtime. Re-check them on each PZ
-- update; everything else in this file is derived.
local DANGER_CONDITION = 20

local function backfireChance(condition)
    if condition <= DANGER_CONDITION then return 1 / 5 end
    if condition <= 30 then return 1 / 10 end
    if condition <= 40 then return 1 / 15 end
    return nil
end

local function disasterChance(condition)
    if condition > DANGER_CONDITION then return nil end
    return 1 / 10 + (9 / 10) * (1 / 20)
end

-- An in-game day is not 24 real hours unless the sandbox says so.
local function toRealMinutes(gameHours)
    local dayMinutes = getSandboxOptions():getDayLengthMinutes()
    if not dayMinutes or dayMinutes <= 0 then return nil end
    return gameHours / 24 * dayMinutes
end

-- Takes an already translated label: the threshold one needs an argument, and
-- '%%' in a json only survives Translator on the getText(key, arg) path that
-- vanilla itself uses for IGUI_Generator_FuelAmount.
local function timeLine(out, opt, label, gameHours)
    if not gameHours or not AllInfo.enabled(opt) then return end

    local realTime = AllInfo.enabled("GeneratorRealTime")
    local minutes = realTime and toRealMinutes(gameHours) or gameHours * 60
    local text = minutes and AllInfo.duration(minutes)
    if not text then return end

    if realTime then text = text .. " " .. getText("UI_AllInfo_GeneratorRealTimeMark") end
    out[#out + 1] = label .. ": " .. text
end

-- Noise: update() reads SoundRadius from the script (20 if unset or <= 0) and
-- halves it when the generator stands in a room. SoundVolume is 1 on all four
-- vanilla models, so it tells you nothing and is left out.
local function noiseTiles(object)
    local item = script(object)
    local radius = item and item:getSoundRadius() or 0
    if radius <= 0 then radius = 20 end

    local square = object:getSquare()
    if square and square:getRoom() then radius = math.floor(radius / 2) end

    return radius
end

function AllInfo.Generator.extraRichText(object)
    local lines = {}

    if AllInfo.enabled("GenNoise") then
        lines[#lines + 1] = getText("UI_AllInfo_GeneratorNoise") .. ": "
            .. noiseTiles(object) .. " " .. getText("UI_AllInfo_GeneratorTiles")
    end

    -- A generator that is off burns no fuel and suffers no wear: update()
    -- returns immediately. Every countdown below would be infinite.
    if not object:isActivated() then
        if #lines == 0 then return "" end
        return " <LINE> " .. table.concat(lines, " <LINE> ")
    end

    timeLine(lines, "GenFuel", getText("IGUI_invpanel_Remaining"), fuelHours(object))
    timeLine(lines, "GenToWarn", getText("UI_AllInfo_GeneratorToWarn", DANGER_CONDITION),
        hoursToCondition(object, DANGER_CONDITION))
    timeLine(lines, "GenToDead", getText("UI_AllInfo_GeneratorToDead"),
        hoursToCondition(object, 0))

    local condition = object:getCondition()

    local backfire = AllInfo.enabled("GenBackfire") and backfireChance(condition)
    if backfire then
        lines[#lines + 1] = getText("UI_AllInfo_GeneratorBackfire") .. ": " .. AllInfo.pct(backfire, 1)
    end

    -- The one line worth shouting about: below 20% it can burn the building
    -- down or blow up, and both set the condition to 0 outright.
    local disaster = AllInfo.enabled("GenDanger") and disasterChance(condition)
    if disaster then
        lines[#lines + 1] = " <RED> " .. getText("UI_AllInfo_GeneratorDanger")
            .. ": " .. AllInfo.pct(disaster, 1) .. " <RGB:1,1,1> "
    end

    if #lines == 0 then return "" end
    return " <LINE> " .. table.concat(lines, " <LINE> ")
end

-- Generator Time Remaining replaces this function outright, which is why it
-- breaks on every patch. Wrapping composes with whatever else is installed.
local base = ISGeneratorInfoWindow.getRichText

function ISGeneratorInfoWindow.getRichText(object, displayStats)
    local text = base(object, displayStats)
    if not displayStats then return text end

    -- Same isolation policy as the item providers: a window you cannot read is
    -- worse than a window without our lines.
    local ok, extra = pcall(AllInfo.Generator.extraRichText, object)
    if not ok then
        print("[AllInfo] generator info disabled: " .. tostring(extra))
        AllInfo.Generator.extraRichText = function() return "" end
        return text
    end

    return text .. (extra or "")
end

AllInfo.hooks = AllInfo.hooks or {}
AllInfo.hooks.GeneratorRichText = ISGeneratorInfoWindow.getRichText
