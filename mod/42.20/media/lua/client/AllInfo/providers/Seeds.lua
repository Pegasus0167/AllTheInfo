require "AllInfo/Core"

-- Growth time and sowing months for seed packets.
--
-- farming_vegetableconf.props is keyed by plant name and each entry carries
-- seedName / sowMonth / timeToGrow. We need the reverse lookup, so the
-- seed -> plant index is built once.
--
-- That table lives in lua/server, so it can be missing on a multiplayer
-- client. Every access is guarded and the provider shows nothing rather than
-- guessing.
local seedIndex

local function plantForSeed(fullType)
    if seedIndex == nil then
        seedIndex = {}
        local props = farming_vegetableconf and farming_vegetableconf.props
        if props then
            for _, plant in pairs(props) do
                if plant.seedName then seedIndex[plant.seedName] = plant end
            end
        end
    end
    return seedIndex[fullType]
end

AllInfo.register("Seeds", 40, nil, function(out, item, chr)
    local plant = plantForSeed(item:getFullType())
    if not plant then return end

    if plant.timeToGrow and plant.timeToGrow > 0 then
        local hours = plant.timeToGrow
        local speed = AllInfo.gameSandbox("FarmingSpeedNew", nil)
        if type(speed) == "number" and speed > 0 then hours = hours / speed end

        local d = AllInfo.duration(hours * 60)
        if d then AllInfo.rowIf(out, "SeedGrow", getText("Tooltip_AllInfo_GrowTime"), d) end
    end

    -- One month per row, like the weapons on an ammo box: a comma-joined list
    -- of up to twelve month names would stretch the tooltip off-screen.
    if plant.sowMonth and #plant.sowMonth > 0 then
        for i = 1, #plant.sowMonth do
            AllInfo.rowIf(out, "SeedMonths",
                i == 1 and getText("Tooltip_AllInfo_SowMonths") or "",
                -- Reuses vanilla's month names, so this is translated everywhere.
                getText("Sandbox_StartMonth_option" .. plant.sowMonth[i]))
        end
    end
end)
