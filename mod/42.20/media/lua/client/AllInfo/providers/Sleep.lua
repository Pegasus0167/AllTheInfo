require "AllInfo/Core"
require "ISUI/ISWorldObjectContextMenu"

-- Rest quality. Two surfaces: pillows in the tooltip, and the "Sleep" context
-- menu option on a bed.
--
-- IsoPlayer.updateStats_Sleeping() multiplies fatigue recovery by these.
-- Shown as an absolute percentage: vanilla already says "Good"/"Average", what
-- it never gives is the number behind that word.
-- ponytail: hardcoded in Java, re-check on each PZ update.
local RECOVERY = {
    goodBedPillow = 1.15, goodBed = 1.10,
    averageBedPillow = 1.05, averageBed = 1.00,
    badBedPillow = 0.95, badBed = 0.90,
    floorPillow = 0.75, floor = 0.60,
}

-- BodyDamage.UpdateDiscomfort
local DISCOMFORT = {
    badBed = 0.3, badBedPillow = 0.2,
    floor = 0.5, floorPillow = 0.4,
}

-- Sleep length is deliberately not shown. The game rolls
-- ZombRand(fatigue*10, fatigue*13) every time, so any single figure is one
-- sample of a range the player never sees, and the [3,16] clamp flattens every
-- surface to the same number on a rested character.

-- IsoPlayer.updateStats_Sleeping() scales fatigue recovery by these in the same
-- chain as the bed multiplier, so they belong in the same percentage.
-- ponytail: hardcoded in Java, re-check on each PZ update.
local TRAIT_RECOVERY = {
    { trait = CharacterTrait.INSOMNIAC, factor = 0.5 },
    { trait = CharacterTrait.NIGHT_OWL, factor = 1.4 },
}

local function traitRecovery(playerObj)
    local factor = 1.0
    for i = 1, #TRAIT_RECOVERY do
        local entry = TRAIT_RECOVERY[i]
        if entry.trait and playerObj:hasTrait(entry.trait) then
            factor = factor * entry.factor
        end
    end
    return factor
end

-- A pillow adds a flat +0.05 on any bed (1.00 -> 1.05) and +0.15 on the floor
-- (0.60 -> 0.75). We quote the bed figure: that is where players actually sleep.
local PILLOW_BONUS = 0.05

local function describe(bedType, playerObj)
    local rows = {}

    -- Surface and traits multiply together, so the figure is what this
    -- character actually recovers here, not just what the bed is worth.
    local surface = RECOVERY[bedType] or 1.00   -- chairs and anything unknown
    local traits = traitRecovery(playerObj)
    local recovery = surface * traits

    local value = AllInfo.pct(recovery, 0)
    if traits ~= 1.0 then
        value = value .. "  (" .. AllInfo.pct(surface, 0) .. " x" .. AllInfo.num(traits, 2) .. ")"
    end
    AllInfo.rowIf(rows, "SleepQuality", getText("Tooltip_AllInfo_RestQuality"), value, AllInfo.color(recovery >= 1))

    local discomfort = DISCOMFORT[bedType]
    if discomfort then
        AllInfo.rowIf(rows, "SleepDiscomfort", getText("Tooltip_AllInfo_Discomfort"),
            AllInfo.num(discomfort, 2), AllInfo.color(false))
    end

    return rows
end

-- 1) Items: a pillow upgrades whatever you sleep on.
AllInfo.register("Sleep", 90, nil, function(out, item, chr)
    if item:hasTag(ItemTag.PILLOW) then
        AllInfo.rowIf(out, "SleepQuality", getText("Tooltip_AllInfo_RestQuality"),
            "+" .. AllInfo.pct(PILLOW_BONUS, 0), AllInfo.color(true))
    end
end)

-- 2) The "Sleep" option. Vanilla nests it in a per-furniture submenu ("Modern
-- bed" > "Sleep"), so a flat scan of the root menu never finds it.
local function findOption(menu, name, depth)
    if not menu or not menu.options or depth > 3 then return nil end

    for i = 1, #menu.options do
        local option = menu.options[i]
        if option.name == name then return option end
        if option.subOption then
            local found = findOption(menu:getSubMenu(option.subOption), name, depth + 1)
            if found then return found end
        end
    end

    return nil
end

local function onFillWorldObjectContextMenu(playerNum, context, worldObjects, test)
    if test then return end

    local option = findOption(context, getText("ContextMenu_Sleep"), 1)
    if not option then return end

    local playerObj = getSpecificPlayer(playerNum)
    if not playerObj then return end

    -- Find the bed the way vanilla does, then reuse its own classifier so our
    -- percentage and its "Good"/"Average" label can never disagree.
    local bed = nil
    for i = 1, #worldObjects do
        local props = worldObjects[i]:getProperties()
        if props and props:get("BedType") then
            bed = worldObjects[i]
            break
        end
    end

    local ok, bedType = pcall(ISWorldObjectContextMenu.getBedQuality, playerObj, bed)
    if not ok or not bedType then return end

    local rows = describe(bedType, playerObj)
    if #rows == 0 then return end

    local tooltip = option.toolTip or ISWorldObjectContextMenu.addToolTip()
    tooltip:setName(option.name)

    local text = tooltip.description or ""
    for i = 1, #rows do
        if text ~= "" then text = text .. " <LINE> " end
        text = text .. rows[i].label .. ": " .. rows[i].value
    end

    tooltip.description = text
    option.toolTip = tooltip
end

-- Added last so vanilla has already built its submenus by the time we look.
Events.OnFillWorldObjectContextMenu.Add(onFillWorldObjectContextMenu)
