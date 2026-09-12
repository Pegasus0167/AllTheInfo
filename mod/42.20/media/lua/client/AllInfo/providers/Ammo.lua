require "AllInfo/Core"

-- Magazines carry their own AmmoType, but loose ammo declares nothing at all:
-- 556Bullets is just a weight, a count and a "base:ammo" tag. The weapon is the
-- side that knows which ammo it eats, so build the reverse index once from the
-- scripts. Derived from the game's own data, so modded guns show up for free.
local gunsByAmmo

local function compatibleGuns(fullType)
    if not gunsByAmmo then
        gunsByAmmo = {}

        local all = getScriptManager():getAllItems()
        for i = 0, all:size() - 1 do
            local script = all:get(i)
            if script:isRanged() then
                local ammo = script:getAmmoType()
                local key = ammo and ammo:getItemKey()
                if key then
                    local list = gunsByAmmo[key]
                    if not list then
                        list = {}
                        gunsByAmmo[key] = list
                    end
                    list[#list + 1] = script:getDisplayName()
                end
            end
        end

        -- Sorted once here, not on every hover: the index never changes.
        for _, list in pairs(gunsByAmmo) do table.sort(list) end
    end

    return gunsByAmmo[fullType]
end

AllInfo.register("Ammo", 30, nil, function(out, item, chr)
    if instanceof(item, "HandWeapon") then return end   -- Firearm.lua covers guns

    local ammoType = item:getAmmoType()
    local maxAmmo = item:getMaxAmmo()

    if ammoType and maxAmmo > 0 then
        AllInfo.rowIf(out, "AmmoCount", getText("Tooltip_AllInfo_Capacity"),
            item:getCurrentAmmoCount() .. " / " .. maxAmmo)

        local name = ammoType:getTranslationName()
        if name and name ~= "" then
            AllInfo.rowIf(out, "AmmoType", getText("Tooltip_weapon_Ammo"), getText(name))
        end
    end

    local guns = compatibleGuns(item:getFullType())
    if guns and #guns > 0 then
        -- One weapon per row: a comma-joined list would stretch the tooltip
        -- off-screen on a calibre shared by a dozen guns. Only the first row
        -- carries the label, so the names line up in a column.
        for i = 1, #guns do
            AllInfo.rowIf(out, "AmmoGuns", i == 1 and getText("Tooltip_AllInfo_UsedBy") or "", guns[i])
        end
    end
end)
