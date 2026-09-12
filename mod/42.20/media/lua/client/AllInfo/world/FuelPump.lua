require "AllInfo/Core"

AllInfo.FuelPump = AllInfo.FuelPump or {}

-- Right-click a gas pump -> "Gas Pump" -> "Info", the same shape and the same
-- vanilla icon the farming menu uses for a crop. Hovering Info is enough: the
-- figures ride in the option's own tooltip, exactly like the Sleep option's,
-- so there is nothing to click and nothing to close.
--
-- Vanilla already puts three greyed-out lines on that menu -- no power, empty,
-- no container -- so what it never tells you is the one number that matters:
-- how much is left in the tank. It knows it (ContextMenu_PumpFuelAmount) and
-- only prints it as a debug option. This tooltip prints it, plus what is keeping
-- the pump alive, the grid or your own generator.
--
-- Client-side and read-only, like everything else here.

local INFO_ICON = "media/ui/inventoryPanes/Button_Info.png"

-- A pump is any object whose sprite carries the fuelAmount property. That is
-- exactly the test ISWorldObjectContextMenuLogic.doFuelMenu runs to decide
-- there is a pump on the square, so this menu appears with vanilla's own and
-- never on anything else. All eight vanilla pump sprites declare 20000.
local function pumpIn(worldobjects)
    for i = 1, #worldobjects do
        local obj = worldobjects[i]
        local sprite = obj and obj:getSprite()
        if sprite and sprite:getProperties():has("fuelAmount") then return obj end
    end
end

-- Vanilla's own power test, mirrored from doFuelMenu:
--     (AllowExteriorGenerator and square:haveElectricity()) or square:hasGridPower()
-- The two branches name the source, because they do not overlap:
-- haveElectricity() is generator-only (IsoChunk.isGeneratorPoweringSquare) and
-- hasGridPower() is the world grid (!isNoPower() and doesPowerGridExist()).
local function powerKey(obj)
    local square = obj:getSquare()
    if not square then return nil end

    if square:hasGridPower() then return "UI_AllInfo_PumpMains" end
    if AllInfo.gameSandbox("AllowExteriorGenerator", true) and square:haveElectricity() then
        return "UI_AllInfo_PumpGenerator"
    end
    return nil
end

-- getPipedFuelAmount() rolls the tank the first time it is asked, and only
-- while the pump has power; before that it answers -1, which is "the game has
-- not decided yet", not "empty". Reporting that as a zero would be a lie.
-- Right-clicking already calls it once for every object in the click, so asking
-- here adds no side effect of ours.
local function amountLine(obj)
    -- Vanilla's own label is ContextMenu_PumpFuelAmount, "Fuel Pump Amount
    -- Remaining", which repeats the tooltip's own title. Ours is one of the few
    -- own keys here.
    local label = getText("UI_AllInfo_FuelRemaining") .. ": "

    if AllInfo.gameSandbox("FuelStationGasInfinite", false) then
        return label .. getText("Sandbox_FuelStationGas_option9")
    end

    local left = obj:getPipedFuelAmount()
    if not left or left < 0 then return label .. getText("Fluid_Unknown") end

    local full = tonumber(obj:getSprite():getProperties():get("fuelAmount"))
    local value = AllInfo.num(left, 0)
    if full and full > 0 then
        value = value .. " / " .. AllInfo.num(full, 0) .. "  (" .. AllInfo.pct(left / full, 0) .. ")"
    end

    if left <= 0 then return " <RED> " .. label .. value .. " <RGB:1,1,1> " end
    return label .. value
end

function AllInfo.FuelPump.describe(obj)
    local lines = {}
    if AllInfo.enabled("PumpFuel") then lines[1] = amountLine(obj) end

    if AllInfo.enabled("PumpPower") then
        local key = powerKey(obj)
        if key then
            lines[#lines + 1] = getText("IGUI_RadioPower") .. ": " .. getText(key)
        else
            lines[#lines + 1] = " <RED> " .. getText("ContextMenu_FuelPumpNoPower")
                .. " <RGB:1,1,1> "
        end
    end

    return table.concat(lines, " <LINE> ")
end

function AllInfo.FuelPump.build(context, worldobjects, test)
    local pump = pumpIn(worldobjects)
    if not pump then return end
    if test then return ISWorldObjectContextMenu.setTest() end

    local parent = context:addOption(getText("IGUI_GasPump"), worldobjects, nil)
    local sub = ISContextMenu:getNew(context)
    context:addSubMenu(parent, sub)

    -- No callback: the entry exists to be hovered, and the tooltip beside it is
    -- the whole feature.
    local option = sub:addOption(getText("ContextMenu_Info"), worldobjects, nil)
    option.iconTexture = getTexture(INFO_ICON):splitIcon()

    local tooltip = ISWorldObjectContextMenu.addToolTip()
    tooltip:setName(getText("IGUI_GasPump"))
    tooltip.description = AllInfo.FuelPump.describe(pump)
    option.toolTip = tooltip
end

-- Everything else in this mod can fail into a missing row. This one runs while
-- the right-click menu is being built, so an error here takes the whole menu
-- down with it -- the worst thing the mod could do to a save. Same self-
-- disabling policy as the crop panel, and the swap has to be on the *field*:
-- the event holds the function value it was given, so replacing that would
-- change nothing.
local function fill(player, context, worldobjects, test)
    if not AllInfo.enabled("PumpFuel") and not AllInfo.enabled("PumpPower") then return end

    local ok, result = pcall(AllInfo.FuelPump.build, context, worldobjects, test)
    if ok then return result end

    print("[AllInfo] fuel pump menu disabled: " .. tostring(result))
    AllInfo.FuelPump.build = function() end
end

Events.OnFillWorldObjectContextMenu.Add(fill)
