require "AllInfo/Core"
require "Farming/ISUI/ISFarmingInfo"

AllInfo.Crops = AllInfo.Crops or {}

-- Extra rows under vanilla's crop panel (right-click a crop -> its info window).
--
-- Vanilla already has ISFarmingInfo, but most of it is locked behind
-- ISFarmingMenu.cheat or a Farming level, and what does get through is
-- qualitative. Without debug mode the plant's health and its current growing
-- phase are never shown at all, the next phase needs level 6 and only says
-- "Days", and the water level is a word, not a number.
--
-- Everything below is read straight off the plant table, which is plain Lua
-- (CPlantGlobalObject), so no Java-binding rules apply here.
--
-- ISFarmingMenu.cheat is deliberately NOT flipped to unlock vanilla's own
-- rows: it is a real cheat flag, not a display one -- it also plants without
-- seeds (ISFarmingMenu.lua:1032), makes actions instant (:553) and sends a
-- 'cheat' command to the server (:1330).

local FONT_HGT = getTextManager():getFontHeight(UIFont.Normal)
local PAD = 1
local LINE = FONT_HGT + PAD * 2

-- Vanilla's own Farming thresholds, reused verbatim when the FarmingGate option
-- is on. Each one is the level at which vanilla itself starts showing or
-- colouring that value; none of these numbers is ours.
local GATE = {
    phase = 2,        -- getCurrentGrowingPhase()
    nextPhase = 6,    -- the `farmingLevel >= 6` branch in render()
    health = 2,       -- getHealthColor()
    water = 3,        -- getWaterLvlColor()
    waterNumber = 4,  -- the water bar
    watered = 2,      -- getNoWateredSinceColor()
    disease = 3,      -- the disease block, magnifier included
}

local function allowed(level, needed)
    if not AllInfo.enabled("FarmingGate") then return true end
    return level >= needed
end

-- With the debug cheat flag on, vanilla already prints phase, fertilizer,
-- health, water and pests *with numbers*, so repeating them is pure noise. The
-- only row it never draws in any mode is time since the last watering.
local function vanillaAlreadyShows()
    return ISFarmingMenu and ISFarmingMenu.cheat == true
end

-- Exact time to the next growing phase, from the plant table. Shared by our own
-- row (below Farming 6) and by the getNextGrowingPhase wrapper (from 6 up), so
-- the same figure appears wherever the row happens to be drawn.
local function nextPhaseText(plant)
    if not plant.nextGrowing then return nil end
    local hours = plant.nextGrowing - CFarmingSystem.instance.hoursElapsed
    return AllInfo.duration(math.max(hours, 0) * 60)
end

-- Wrappers ------------------------------------------------------------------
--
-- Vanilla already has the numeric form of three of its own rows; it just hides
-- them behind ISFarmingMenu.cheat and writes a word instead. Filling in its
-- value is a far smaller change than drawing a second row of our own next to
-- it, and it also reaches the two places we do not hook at all: the floating
-- tooltip over a crop (CFarmingSystem.DoSpecialTooltip1) and the planting
-- cursor (ISFarmingMenu), which call the same getters.
--
-- Every wrapper returns vanilla's own text untouched when the option is off,
-- when the cheat flag is on -- vanilla is already printing numbers there -- or
-- when FarmingGate is on and the level is too low.

local baseWaterLvl = ISFarmingInfo.getWaterLvl

function ISFarmingInfo.getWaterLvl(plant, farmingLevel)
    local text = baseWaterLvl(plant, farmingLevel)
    if not AllInfo.enabled("CropWater") or vanillaAlreadyShows() then return text end
    if not plant or not plant.waterLvl then return text end
    if not allowed(farmingLevel or 0, GATE.water) then return text end

    text = text .. " " .. AllInfo.num(plant.waterLvl, 0) .. " / 100"

    -- waterNeeded is per-seed and is what calcWater() compares against. It is
    -- the number that makes the level actionable, and vanilla never shows it.
    if plant.waterNeeded and allowed(farmingLevel or 0, GATE.waterNumber) then
        text = text .. "  (>= " .. AllInfo.num(plant.waterNeeded, 0) .. ")"
    end
    return text
end

local baseNextPhase = ISFarmingInfo.getNextGrowingPhase

function ISFarmingInfo.getNextGrowingPhase(info)
    if not AllInfo.enabled("CropNextPhase") or vanillaAlreadyShows() then
        return baseNextPhase(info)
    end
    if not info or not info.plant or not info.plant:isAlive() then
        return baseNextPhase(info)
    end

    local level = CFarmingSystem.instance:getXp(info.character)
    if not allowed(level, GATE.nextPhase) then return baseNextPhase(info) end

    return nextPhaseText(info.plant) or baseNextPhase(info)
end

local baseDisease = ISFarmingInfo.getDiseaseString

-- farmingLevel arrives already including the magnifier bonus from vanilla's own
-- caller, so this does not add it a second time.
function ISFarmingInfo.getDiseaseString(diseaseLvl, farmingLevel)
    local text = baseDisease(diseaseLvl, farmingLevel)
    if not AllInfo.enabled("CropDisease") or vanillaAlreadyShows() then return text end
    if type(diseaseLvl) ~= "number" or diseaseLvl <= 0 then return text end
    if not allowed(farmingLevel or 0, GATE.disease) then return text end

    return text .. " " .. AllInfo.num(diseaseLvl, 0) .. " / 100"
end

function AllInfo.Crops.draw(self, y)
    local plant = self.plant
    if not plant then return y end

    local level = CFarmingSystem.instance:getXp(self.character)
    local width = self.width - 25

    local function row(label, value, color)
        self:drawRect(13, y, width, LINE, 0.05, 1.0, 1.0, 1.0)
        self:drawText(label .. " : ", 13, y + PAD, 1, 1, 1, 1, UIFont.Normal)
        local c = color or { r = 1, g = 1, b = 1 }
        self:drawTextRight(value, self.width - 17, y + PAD, c.r, c.g, c.b, 1, UIFont.Normal)
        y = y + LINE
    end

    if not plant:isAlive() then
        row(getText("Farming_Health"), getText("Farming_Dead"), AllInfo.color(false))
        return y
    end

    local props = farming_vegetableconf.props[plant.typeOfSeed]

    -- Everything except the last-watering row is something vanilla itself
    -- prints with the cheat flag on, so with debug mode up the whole block is
    -- skipped rather than tested row by row.
    if not vanillaAlreadyShows() then
        -- Health. Vanilla only ever prints this with the cheat flag on.
        if plant.health and allowed(level, GATE.health)
            and AllInfo.enabled("CropHealth") then
            row(getText("Farming_Health"), AllInfo.num(plant.health, 0) .. " / 100",
                AllInfo.color(plant.health >= 50))
        end

        -- Current phase as a count. getObjectPhase() is vanilla's own naming.
        if props and plant.nbOfGrow and props.fullGrown and allowed(level, GATE.phase)
            and AllInfo.enabled("CropPhase") then
            row(getText("Farming_Current_growing_phase"),
                farming_vegetableconf.getObjectPhase(plant)
                    .. " " .. plant.nbOfGrow .. " / " .. (props.fullGrown + 1))
        end

        -- Hours to the next phase, but only when vanilla is not drawing that
        -- row itself. From Farming 6 up it does, and the wrapper below fills
        -- its value with this same figure, so a row here would be the second
        -- copy of it. Below 6 vanilla draws nothing and this is the only one.
        if plant.nextGrowing and allowed(level, GATE.nextPhase)
            and level < GATE.nextPhase and AllInfo.enabled("CropNextPhase") then
            row(getText("Farming_Next_growing_phase"), nextPhaseText(plant))
        end
    end

    -- Hours since the last watering. Vanilla computes this to pick a colour and
    -- then never draws the number, in any mode.
    if plant.lastWaterHour and allowed(level, GATE.watered)
        and AllInfo.enabled("CropWatered") then
        local since = CFarmingSystem.instance.hoursElapsed - plant.lastWaterHour
        local text = AllInfo.duration(math.max(since, 0) * 60)
        if text then
            row(getText("Farming_Last_time_watered"), text, AllInfo.color(since < 50))
        end
    end

    if vanillaAlreadyShows() then return y end

    -- Fertilizer. Vanilla hides this behind the cheat flag; 1 is the useful
    -- amount and anything above it is the "too much" case in its own code.
    if plant.fertilizer and plant.fertilizer > 0 and AllInfo.enabled("CropFertilizer") then
        row(getText("Farming_Fertilized"), AllInfo.num(plant.fertilizer, 2),
            AllInfo.color(plant.fertilizer <= 1))
    end

    -- No pest rows here any more: vanilla draws one per pest from Farming 3 up
    -- (magnifier included) and the getDiseaseString wrapper puts the number
    -- into its own value, so ours were the second copy of the same line.

    return y
end

local baseRender = ISFarmingInfo.render

-- ponytail: the panel's height is corrected after vanilla has already sized
-- itself, so the backdrop is one frame short the first time a crop is opened.
-- Fixing it properly means predicting vanilla's own row count, which is the
-- whole of its render(). Upgrade path if it ever shows: mirror the count.
function ISFarmingInfo:render(...)
    baseRender(self, ...)

    if not self.plant or not self.character then return end

    -- Vanilla's last act is setHeightAndParentHeight(y + 8), so this recovers
    -- exactly where it stopped drawing, in the same frame.
    local y = self:getHeight() - 8

    local ok, result = pcall(AllInfo.Crops.draw, self, y)
    if not ok then
        print("[AllInfo] crop info disabled: " .. tostring(result))
        AllInfo.Crops.draw = function(_, at) return at end
        return
    end

    if result > y then self:setHeightAndParentHeight(result + 8) end
end

AllInfo.hooks = AllInfo.hooks or {}
AllInfo.hooks.FarmingInfoRender = ISFarmingInfo.render
AllInfo.hooks.FarmingWaterLvl = ISFarmingInfo.getWaterLvl
AllInfo.hooks.FarmingNextPhase = ISFarmingInfo.getNextGrowingPhase
AllInfo.hooks.FarmingDisease = ISFarmingInfo.getDiseaseString
