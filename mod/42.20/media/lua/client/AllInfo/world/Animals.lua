require "AllInfo/Core"
require "ISUI/Animal/ISAnimalUI"

AllInfo.Animals = AllInfo.Animals or {}

-- Extra rows under vanilla's animal panel (right-click an animal -> Info).
--
-- Vanilla's ISAnimalUI stops at nine rows without debug mode: type, breed,
-- gender, age, health, appearance, attitude, livestock zone and udder. Every
-- one of those that is a number underneath is printed as a word, and a good
-- half of the panel is gated behind Husbandry or only appears with the animal
-- cheat on. Four figures exist in no screen at all, cheat included: butchering
-- yield, milk and wool rate, old age and the weight ceiling.
--
-- Which rows appear depends on the animal, exactly like vanilla's: a cockerel
-- has no udder and cannot be pregnant, a cow has no feathers.
--
-- AnimalContextMenu.cheat is never flipped to unlock vanilla's own rows: it is
-- a real cheat flag (it re-genders and re-ages animals from the same panel),
-- the same reason ISFarmingMenu.cheat is left alone in Crops.lua.

local FONT_HGT_SMALL = getTextManager():getFontHeight(UIFont.Small)
local LINE = FONT_HGT_SMALL + 4

-- Vanilla's own Husbandry thresholds, reused verbatim when AnimalGate is on.
-- Each one is the level at which ISAnimalUI itself starts showing that value
-- (its checks read `skillLvl > N`, so these are N + 1). None of them is ours.
local GATE = {
    weight = 5,      -- the weight row
    fertilized = 3,  -- fertilised / pregnant
    stress = 5,      -- getStressTxt only splits into four steps from here
}

local function allowed(level, needed)
    if not AllInfo.enabled("AnimalGate") then return true end
    return level >= needed
end

-- With the animal cheat on, vanilla already prints health, hunger, thirst,
-- stress, udder, wool, pregnancy and player acceptance *with numbers*, so
-- repeating them is pure noise -- the same duplication the crop panel had. The
-- four rows it never draws in any mode stay.
local function vanillaAlreadyShows()
    return AnimalContextMenu and AnimalContextMenu.cheat == true
end

-- Hours until a fluid-like store fills up, or nil when it never will. Milk and
-- wool both grow by a fixed amount every game hour (AnimalData.updateMilk and
-- hourGrow, one call per hour from update()), so this is a division, not an
-- estimate.
local function fillTime(current, max, perHour)
    if not max or max <= 0 or not perHour or perHour <= 0 then return nil end
    if current >= max then return nil end
    return AllInfo.duration((max - current) / perHour * 60)
end

-- The rows, as data. Kept separate from the drawing so SelfTest can sweep a
-- live animal without a panel open.
--
-- The fourth field of every row is the key of its hover description. Those are
-- the only place in the block where a figure is spelled out in words, so each
-- one is a number verified in the bytecode -- never a guess about what the game
-- probably does with the stat.
function AllInfo.Animals.rows(animal, chr, level, cheat)
    local out = {}
    local data = animal:getData()
    if not data then return out end

    -- Every row answers to its own switch, so the panel is whatever the
    -- player asked for and nothing else.
    local function row(opt, label, value, color, tip)
        if value == nil or value == "" then return end
        if not AllInfo.enabled(opt) then return end
        out[#out + 1] = { label = label, value = value, color = color, tip = tip }
    end

    -- 1. What no screen shows, cheat included ------------------------------

    -- Butchering yield. ButcheringUtil multiplies both the number of meat
    -- pieces and the hunger/calories of each one by size * meatRatio, so this
    -- single figure is what answers "is it worth killing yet?".
    row("AnimalMeat", getText("UI_AllInfo_animal_Meat"),
        "x" .. AllInfo.num(animal:getAnimalSize() * animal:getMeatRatio(), 2),
        AllInfo.color(animal:getAnimalSize() * animal:getMeatRatio() >= 1),
        "UI_AllInfo_animal_tip_Meat")

    -- Blood, in litres: the definitions carry centilitres, getBloodQuantity()
    -- divides by 100 and ISGatherBloodFromAnimal pours the result straight
    -- into a fluid container as FluidType.AnimalBlood.
    --
    -- The figure climbs steeply on a well-fed animal, and that is vanilla's:
    -- its interpolation divides by (maxWeight - weight) instead of
    -- (maxWeight - minWeight), so it blows up as the animal nears its ceiling
    -- and is undefined right at it. Reported as it will really be poured, with
    -- the infinity guarded rather than the number smoothed over.
    local blood = animal:getBloodQuantity()
    if blood and blood > 0 and blood < math.huge then
        row("AnimalBlood", getText("Fluid_Name_AnimalBlood"), AllInfo.num(blood, 2) .. " L", nil,
            "UI_AllInfo_animal_tip_Blood")
    end

    -- Feathers, only for breeds that have them. The label is the item's own
    -- name, so it costs no translation key and says "Chicken Feather".
    local featherItem = data:getBreed() and data:getBreed():getFeatherItem()
    local feathers = featherItem and animal:getFeatherNumber() or 0
    if feathers > 0 then
        row("AnimalFeathers", getItemNameFromFullType(featherItem), tostring(feathers), nil,
            "UI_AllInfo_animal_tip_Feathers")
    end

    -- Old age. getGeriatricPercentage() stays at 0 until 70% of the animal's
    -- life expectancy and reaches 1 at the end of it; past that point
    -- AnimalData.checkOld() starts taking health away.
    local maxAge = data:getMaxAgeGeriatric()
    if maxAge and maxAge > 0 then
        local age = AllInfo.duration(data:getAge() * 1440)
        local span = AllInfo.duration(maxAge * 1440)
        local geriatric = data:getGeriatricPercentage()
        local value = AllInfo.pct(geriatric, 0)
        if age and span then value = value .. "  (" .. age .. " / " .. span .. ")" end
        row("AnimalAge", getText("IGUI_Animal_Geriatric"), value, AllInfo.color(geriatric <= 0),
            "UI_AllInfo_animal_tip_Geriatric")
    end

    -- Weight against the ceiling this animal can reach. Vanilla shows the
    -- current weight from Husbandry 5 and the maximum never.
    local maxWeight = data:getMaxWeight()
    if maxWeight and maxWeight > 0 and allowed(level, GATE.weight) then
        row("AnimalWeight", getText("IGUI_char_Weight"),
            getText("IGUI_AnimalWeight",
                AllInfo.num(data:getWeight(), 1) .. " / " .. AllInfo.num(maxWeight, 1)),
            AllInfo.color(data:getWeight() >= maxWeight * 0.9),
            "UI_AllInfo_animal_tip_Weight")
    end

    -- How much this animal trusts you: it decides whether milking and shearing
    -- succeed (ISMilkAnimal subtracts acceptance * 5 from the failure chance).
    -- ponytail: getPlayerAcceptance() seeds the entry with Rand(0, 20) the
    -- first time it is asked, so opening the panel brings forward a roll the
    -- first pet or feed would have made anyway. There is no read-only getter.
    if not cheat then
        row("AnimalTrust", getText("IGUI_Animal_PlayerAcceptance"),
            AllInfo.num(animal:getPlayerAcceptance(chr), 0) .. " / 100", nil,
            "UI_AllInfo_animal_tip_Acceptance")
    end

    if cheat then return out end

    -- 2. A number where vanilla gives a word -------------------------------

    -- Health. Vanilla's own steps are 0.8 / 0.55 / 0.3.
    row("AnimalHealth", getText("IGUI_XP_Health"), AllInfo.pct(animal:getHealth(), 0),
        AllInfo.color(animal:getHealth() >= 0.8), "UI_AllInfo_animal_tip_Health")

    -- Hunger and thirst, which vanilla lumps into "Appearance" as two words.
    -- Both are 0-1 and count *upwards*: 0.3 is well fed, over 0.6 is starving.
    row("AnimalHunger", getText("IGUI_HaloNote_Hunger"), AllInfo.pct(animal:getHunger(), 0),
        AllInfo.color(animal:getHunger() < 0.3), "UI_AllInfo_animal_tip_Hunger")
    row("AnimalThirst", getText("IGUI_HaloNote_Thirst"), AllInfo.pct(animal:getThirst(), 0),
        AllInfo.color(animal:getThirst() < 0.3), "UI_AllInfo_animal_tip_Thirst")

    -- Stress, the "Attitude" row. Scale is 0-100, not 0-1, and vanilla splits
    -- it at 40 / 60 / 80 -- but only from Husbandry 5; below that there are
    -- two steps for the whole range.
    if allowed(level, GATE.stress) then
        row("AnimalStress", getText("IGUI_Animal_Stress"), AllInfo.num(animal:getStress(), 0) .. " / 100",
            AllInfo.color(animal:getStress() < 40), "UI_AllInfo_animal_tip_Stress")
    end

    -- Milk. Six words in vanilla, and the wait is the useful half of it.
    if animal:hasUdder() and data:canHaveMilk() then
        local milk, maxMilk = data:getMilkQuantity(), data:getMaxMilkActual()
        local value = AllInfo.num(milk, 2) .. " / " .. AllInfo.num(maxMilk, 2) .. " L"
        local wait = fillTime(milk, maxMilk, data:getMilkInc())
        if wait then value = value .. "  (" .. getText("UI_AllInfo_animal_Full", wait) .. ")" end
        row("AnimalMilk", getText("IGUI_Animal_Udder"), value, AllInfo.color(animal:canBeMilked()),
            "UI_AllInfo_animal_tip_Udder")
    end

    -- Wool. Five words in vanilla, and a full coat takes 100 days to grow.
    if animal:canBeSheared() then
        local wool, maxWool = data:getWoolQuantity(), data:getMaxWool()
        local value = AllInfo.num(wool, 1) .. " / " .. AllInfo.num(maxWool, 1)
        local wait = fillTime(wool, maxWool, data:getWoolInc())
        if wait then value = value .. "  (" .. getText("UI_AllInfo_animal_Full", wait) .. ")" end
        row("AnimalWool", getText("IGUI_Animal_Wool"), value, AllInfo.color(wool >= maxWool),
            "UI_AllInfo_animal_tip_Wool")
    end

    -- Pregnancy and fertilised eggs, which vanilla turns into four words and a
    -- yes/no. The two counters run on different clocks and mixing them up
    -- would be off by 24x: pregnancy is bumped by growUp(), which AnimalData's
    -- update() only calls when the *day* rolls over (a cow's pregnantPeriod is
    -- 280, "9 months and 10 days"), while fertilised eggs are bumped by
    -- checkFertilizedTime() from hourGrow(), once an hour.
    if allowed(level, GATE.fertilized) then
        if data:isPregnant() then
            local left = AllInfo.duration((data:getPregnantPeriod() - data:getPregnancyTime()) * 1440)
            row("AnimalBreeding", getText("IGUI_Animal_Pregnant"), left, nil, "UI_AllInfo_animal_tip_Pregnant")
        elseif data:isFertilized() then
            local left = AllInfo.duration((animal:getFertilizedTimeMax() - data:getFertilizedTime()) * 60)
            row("AnimalBreeding", getText("IGUI_Animal_Fertilized"), left, nil, "UI_AllInfo_animal_tip_Fertilized")
        end
    end

    return out
end

-- The hover box: what the stat above the cursor actually means. Drawn by hand
-- rather than through ISToolTip because this runs inside the window's own
-- render, which is the only place the row rectangles are known -- the same
-- approach Moodles.lua takes for the moodle descriptions.
--
-- MeasureStringX and MeasureStringY both cope with the newlines a <br> leaves
-- behind (trap 71 and 3.21): the first answers with the longest line, the second
-- counts the lines. So the box follows the text in both directions and nothing
-- has to be split or counted here.
local BOX_PAD = 6

-- Beside the window and level with its row, never under the cursor: a box that
-- follows the mouse covers the rows you are trying to compare, and it hides
-- which row it belongs to. Left side if the window is close to the right edge
-- of the screen. Nothing clips here, so drawing outside the window is fine.
local function drawTip(self, title, body, rowY)
    local tm = getTextManager()
    local w = math.max(tm:MeasureStringX(UIFont.Small, title),
                       tm:MeasureStringX(UIFont.Small, body))
    local h = tm:MeasureStringY(UIFont.Small, title) + tm:MeasureStringY(UIFont.Small, body)
    local boxW, boxH = w + BOX_PAD * 2, h + BOX_PAD * 2

    local x = self.width + 8
    if self:getAbsoluteX() + x + boxW > getCore():getScreenWidth() then x = -boxW - 8 end

    -- Level with the row, pulled up if the bottom would fall off the screen.
    local top = rowY - BOX_PAD
    local overflow = self:getAbsoluteY() + top + boxH - getCore():getScreenHeight()
    if overflow > 0 then top = top - overflow end

    self:drawRect(x, top, boxW, boxH, 0.9, 0, 0, 0)
    self:drawRectBorder(x, top, boxW, boxH, 0.7, 0.4, 0.4, 0.4)
    self:drawText(title, x + BOX_PAD, top + BOX_PAD, 1, 1, 1, 1, UIFont.Small)
    self:drawText(body, x + BOX_PAD, top + BOX_PAD + tm:MeasureStringY(UIFont.Small, title),
        0.85, 0.85, 0.85, 1, UIFont.Small)
end

function AllInfo.Animals.draw(self, y)
    local animal = self.animal
    if not animal or not self.chr then return y end

    local rows = AllInfo.Animals.rows(animal, self.chr, self.skillLvl or 0, vanillaAlreadyShows())
    if #rows == 0 then return y end

    -- A 1px rule in the panel's own border colour, the same one vanilla draws
    -- under the animal's name, so the block reads as part of the window.
    local left = self.avatarPanel.x + self.avatarPanel.width + 30
    self:drawRect(left, y + 2, math.max(self.width - left - 10, 1), 1,
        self.borderColor.a, self.borderColor.r, self.borderColor.g, self.borderColor.b)
    y = y + 8

    -- Resize before asking about the mouse, not after drawing. isMouseOver()
    -- is no flag: it is isPointOver(Mouse.getXA(), Mouse.getYA()) against the
    -- rectangle as it stands right then, and right then the window still ends
    -- 30px below vanilla's last row -- above every row of ours, which would
    -- answer "cursor not on me" for all of them but the first.
    local needed = y + #rows * LINE + 30
    if self:getHeight() < needed then self:setHeight(needed) end

    -- ISUIElement's own getMouseY(), which takes the scroll offset off as well
    -- as the absolute position.
    local mx, my
    if self:isMouseOver() then mx, my = self:getMouseX(), self:getMouseY() end
    local tipTitle, tipBody, tipY

    for i = 1, #rows do
        local r = rows[i]

        -- Only the vertical band is tested: isMouseOver() already says the
        -- cursor is inside the window, and nothing else shares that line. Any
        -- left margin here would drop the rows whose label starts further left
        -- than the others, and pointing at the label is the natural thing.
        local hovered = mx ~= nil and r.tip ~= nil and my >= y and my < y + LINE
        if hovered then
            local body = getTextOrNull(r.tip)
            if body then
                tipTitle, tipBody, tipY = r.label, body, y
                -- The row lights up, so the box is never orphaned from it.
                -- Full width, matching the hover target.
                self:drawRect(8, y - 1, math.max(self.width - 16, 1), LINE, 0.25, 1, 1, 1)
            end
        end

        self:drawTextRight(r.label, self.xOffset, y, 1, 1, 1, 1, UIFont.Small)
        local c = r.color
        if c then
            self:drawText(r.value, self.xOffset + 10, y, c.r, c.g, c.b, 1, UIFont.Small)
        else
            self:drawText(r.value, self.xOffset + 10, y, 1, 1, 1, 0.5, UIFont.Small)
        end

        -- Nothing clips inside this window, so a long value would paint over
        -- the edge instead of being cut. Vanilla widens itself the same way
        -- when the milk button does not fit.
        local right = self.xOffset + 10 + getTextManager():MeasureStringX(UIFont.Small, r.value) + 10
        if self.width < right then self:setWidth(right) end

        y = y + LINE
    end

    if tipBody then drawTip(self, tipTitle, tipBody, tipY) end

    return y
end

-- The hooked flag lives on the table, never in a local: with debug mode on,
-- deploying while the game is open runs this file again and a second pass
-- would wrap our own wrapper, drawing the block twice.
if not AllInfo.Animals.hooked then
    local baseRender = ISAnimalUI.render

    -- ponytail: the panel's height is corrected after vanilla has already
    -- sized itself, so the backdrop is one frame short the first time an
    -- animal is opened. Same ceiling as Crops.lua, same upgrade path: mirror
    -- vanilla's own row count, which means duplicating the whole of render().
    function ISAnimalUI:render(...)
        baseRender(self, ...)

        if not self.animal or not self.avatarPanel then return end

        -- Vanilla's last act is setHeight(math.max(avatarBottom, y) + 30), so
        -- this is where it stopped drawing -- or the bottom of the avatar when
        -- the panel is shorter than the picture, still below every row.
        local y = self:getHeight() - 30

        local ok, result = pcall(AllInfo.Animals.draw, self, y)
        if not ok then
            print("[AllInfo] animal info disabled: " .. tostring(result))
            AllInfo.Animals.draw = function(_, at) return at end
            return
        end

        if result > y then self:setHeight(result + 30) end
    end

    AllInfo.Animals.hooked = true
end

AllInfo.hooks = AllInfo.hooks or {}
AllInfo.hooks.AnimalUIRender = ISAnimalUI.render
