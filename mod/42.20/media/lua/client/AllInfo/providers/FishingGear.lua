require "AllInfo/Core"
require "Fishing/fishing_properties"

-- Rods, lines, hooks and baits. None of these numbers is anywhere in the game:
-- the rod's coefficient scales how long you can hold high tension before the
-- line snaps (FishingRod:updateLine -> tensionLimit), the line's is how much
-- condition each tug costs (damageLine), and the hook's multiplies the bite
-- chance directly (Bobber:attractFish).
--
-- Read live from Fishing.rods / line / hook / fishes, so a fishing mod that adds
-- its own gear gets described too.

local function bestFishFor(lure)
    local sorted = {}
    for _, cfg in ipairs(Fishing.fishes) do
        local weight = cfg.lure and cfg.lure[lure]
        if weight and weight > 0 then
            sorted[#sorted + 1] = { item = cfg.itemType, weight = weight }
        end
    end
    table.sort(sorted, function(a, b)
        if a.weight == b.weight then return a.item < b.item end
        return a.weight > b.weight
    end)

    local names = {}
    for i = 1, math.min(#sorted, 3) do
        names[#names + 1] = getItemNameFromFullType(sorted[i].item)
    end
    if #names == 0 then return nil end
    return table.concat(names, " | ")   -- ASCII: the tooltip font has no U+00B7
end

AllInfo.register("FishingGear", 45, nil, function(out, item, chr)
    local fullType = item:getFullType()

    local rod = Fishing.rods[fullType]
    if rod then
        AllInfo.rowIf(out, "RodTension", getText("Tooltip_AllInfo_fish_RodTension"), "x" .. AllInfo.num(rod, 2))

        local into = Fishing.breakRodReplacement[fullType]
        if into then
            AllInfo.rowIf(out, "RodBreaks", getText("Tooltip_AllInfo_fish_Breaks"), getItemNameFromFullType(into))
        end

        -- The line and hook actually fitted to this rod, which live in its mod
        -- data and are rolled per item by Fishing.onCreateFishingRod.
        local mod = item:getModData()
        local hookType = mod.fishing_HookType
        if hookType then
            AllInfo.rowIf(out, "GearHook", getText("Tooltip_AllInfo_fish_HookChance"),
                getItemNameFromFullType(hookType)
                    .. "  x" .. AllInfo.num(Fishing.hook[hookType] or 0, 2))
        end

        local lineType = mod.fishing_LineType
        if lineType and Fishing.line[lineType] then
            AllInfo.rowIf(out, "GearLine", getText("Tooltip_AllInfo_fish_LineWear"),
                getItemNameFromFullType(lineType)
                    .. "  " .. AllInfo.pct(Fishing.line[lineType], 1))
        end
    end

    local line = Fishing.line[fullType]
    if line then
        AllInfo.rowIf(out, "GearLine", getText("Tooltip_AllInfo_fish_LineWear"), AllInfo.pct(line, 1))
    end

    local hook = Fishing.hook[fullType]
    if hook then
        AllInfo.rowIf(out, "GearHook", getText("Tooltip_AllInfo_fish_HookChance"), "x" .. AllInfo.num(hook, 2))
    end

    -- Fishing.lure.All is built on OnGameStart from every bait family.
    if Fishing.lure and Fishing.lure.All and Fishing.lure.All[fullType] then
        local fish = bestFishFor(fullType)
        if fish then
            AllInfo.rowIf(out, "BaitFor", getText("Tooltip_AllInfo_fish_BaitFor"), fish)
        end
    end
end)
