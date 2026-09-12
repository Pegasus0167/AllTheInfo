require "AllInfo/Core"

-- Burn time in a campfire.
--
-- camping_fuel.lua documents the B42 system in its own header: an item is fuel
-- if it carries the IsFireFuel tag, and the hours it adds are weight * ratio.
-- Default ratio 2/3, or 1/4 for clothing, literature and maps; a script can
-- override it with FireFuelRatio (exposed as getFireFuelRatio()).
--
-- The legacy campingFuelType table is still valid as a fallback, and per that
-- same header the game takes "the lower of the value defined here or the
-- procedurally calculated value". It lives in lua/server though, so it can be
-- nil on a multiplayer client: guarded, never required.
local DEFAULT_RATIO = 2 / 3
local LIGHT_RATIO = 1 / 4

AllInfo.register("Fuel", 50, nil, function(out, item, chr)
    local hours

    if item:hasTag(ItemTag.IS_FIRE_FUEL) then
        local ratio = item:getFireFuelRatio()
        if not ratio or ratio <= 0 then
            ratio = (instanceof(item, "Clothing") or instanceof(item, "Literature"))
                and LIGHT_RATIO or DEFAULT_RATIO
        end
        hours = item:getActualWeight() * ratio
    end

    -- Items listed in the old table are fuel even without the tag.
    local listed = campingFuelType and campingFuelType[item:getType()]
    if listed and listed > 0 then
        hours = hours and math.min(hours, listed) or listed
    end

    if not hours or hours <= 0 then return end

    local d = AllInfo.duration(hours * 60)
    if d then AllInfo.rowIf(out, "FuelBurn", getText("Tooltip_AllInfo_BurnTime"), d) end
end)
