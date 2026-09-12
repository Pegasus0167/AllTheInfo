require "AllInfo/Core"
require "AllInfo/CraftingUI"   -- AllInfo.xpLines, shared with the crafting window
require "Entity/ISUI/BuildRecipe/ISBuildRecipePanel"

AllInfo.Structures = AllInfo.Structures or {}

-- Structure health, on two surfaces: what a thing you already built has left,
-- and what a thing you are about to build would start with.
--
-- Replaces [K] Show Wall Health, which is B41, round-trips to the server for a
-- number the client already holds, and keys off modData.wallType (gone in B42).
-- Client-only here: getHealth() is read straight off the object. Exact in
-- single player; in MP it can lag the server by a tick, and no network traffic
-- is added to fix that.

-- 1) Already built ----------------------------------------------------------

-- instanceof, NOT duck typing on obj.getMaxHealth. PZ's Lua binding does not
-- expose Java methods as indexable fields: `obj.getMaxHealth` is nil even when
-- the method is right there, so that guard rejected every object and the menu
-- entry silently never appeared. Vanilla never duck-types a Java object
-- anywhere in media/lua either -- now we know why.
--
-- These three are exactly the IsoObject subclasses implementing
-- zombie.iso.IHasHealth. IsoWindow is deliberately absent: it has getHealth()
-- but no getMaxHealth(), so there is no "X / Y" to show and calling it would
-- throw.
-- ponytail: a crafting station built as a thumpable shows a row too. Filtering
-- those needs the entity's CraftLogic component; add it if a loom shows up.
local function isStructure(obj)
    return instanceof(obj, "IsoThumpable")
        or instanceof(obj, "IsoDoor")
        or instanceof(obj, "IsoBarricade")
end

local function healthOf(obj)
    if not obj or not isStructure(obj) then return nil end

    local max = obj:getMaxHealth()
    if not max or max <= 0 then return nil end

    local health = obj:getHealth()
    if not health then return nil end

    return health, max
end

-- Drawn under the mouse instead of behind a context-menu entry: right-clicking
-- the exact square a wall sits on is fiddly, because a wall renders upward from
-- its tile and the cursor is usually over the tile behind it.
--
-- IsoObjectPicker picks by *sprite*, which is what "hovering the wall" actually
-- means, and is the same thing the game uses for its own right-click menu.
-- Instance is a public static field, and those do reach Lua (Perks.Axe is one);
-- it is instance fields that do not (see the padLeft trap).
-- The pick is the one expensive thing this file does: FBORenderObjectPicker
-- reads pixels back from a framebuffer, and OnPostUIDraw fires every frame. So
-- the answer is remembered. Mouse position alone is not a safe key -- the world
-- scrolls under a still cursor while you walk -- hence the time bound as well.
-- 100 ms is ~6 picks per second instead of 60, and the lag is invisible.
local PICK_MS = 100
local pickX, pickY, pickTime, picked = nil, nil, 0, nil

local function pickStructure()
    -- OnPostUIDraw fires on the main menu too, and there
    -- FBORenderObjectPicker.getObjectsAt() dereferences IsoPlayer without a
    -- null check and throws. No player means nothing to point at anyway.
    if not getSpecificPlayer(0) then return nil end

    local picker = IsoObjectPicker.Instance
    if not picker then return nil end

    local mx, my = getMouseX(), getMouseY()
    local now = getTimestampMs()
    if mx == pickX and my == pickY and (now - pickTime) < PICK_MS then return picked end

    -- Thumpables cover player-built walls, frames, fences and containers;
    -- doors are picked separately because they are their own class.
    picked = picker:PickThumpable(mx, my) or picker:PickDoor(mx, my, false)
    pickX, pickY, pickTime = mx, my, now

    return picked
end

-- Pinned to the cursor rather than to the foot of the wall. ISCoordConversion
-- .ToScreen() lands in a different space than the one DrawString uses --
-- vanilla's own two callers disagree on whether the zoom factor belongs there
-- -- so the number drifted away from the wall. The mouse position needs no
-- conversion at all, and the label sits next to what you are pointing at,
-- which is the whole point.
local MOUSE_GAP = 22

function AllInfo.Structures.drawHover()
    local health, max = healthOf(pickStructure())
    if not health then return end

    local font = UIFont.Small
    getTextManager():DrawString(font,
        getMouseX() + MOUSE_GAP,
        getMouseY() - getTextManager():getFontHeight(font) / 2,
        health .. " / " .. max, 1, 1, 1, 1)
end

-- Runs every frame, so it stays quiet when there is nothing under the cursor
-- and switches itself off for the session on the first error.
local broken = false

local function onPostUIDraw()
    if broken or not AllInfo.enabled("StructureInspect") then return end

    -- Raised before the call and cleared after it returns. A Java exception
    -- thrown inside a Lua->Java call did NOT stop at our pcall -- it kept going
    -- and the handler fired again every frame -- so the flag is what actually
    -- shuts this down. pcall stays for the message when it does catch.
    broken = true
    local ok, err = pcall(AllInfo.Structures.drawHover)
    broken = false

    if not ok then
        broken = true
        print("[AllInfo] structure hover disabled: " .. tostring(err))
    end
end

Events.OnPostUIDraw.Add(onPostUIDraw)

-- 2) About to be built ------------------------------------------------------

-- ISBuildIsoEntity.lua:653-664, reproduced exactly:
--     bonusHealth = script:getBonusHealth() * multiplier(ConstructionBonusPoints)
--     skillBonus  = craftRecipe:getHighestRelevantSkillLevel(chr) * script:getSkillBaseHealth()
--     baseHealth  = max(script:getHealth(), 0)
--     total       = baseHealth + bonusHealth + skillBonus
local BONUS_MULTIPLIER = { [1] = 0.5, [2] = 0.7, [4] = 1.3, [5] = 1.5 }   -- 3 is unchanged

local function healthAtSkill(script, skillLevel)
    local bonus = script:getBonusHealth()

    local option = getSandboxOptions():getOptionByName("ConstructionBonusPoints")
    local setting = option and option:getValue()
    if setting and BONUS_MULTIPLIER[setting] then bonus = bonus * BONUS_MULTIPLIER[setting] end

    return math.max(script:getHealth(), 0) + bonus + skillLevel * script:getSkillBaseHealth()
end

local function addLabel(panel, text, color)
    local label = ISXuiSkin.build(panel.xuiSkin, "S_NeedsAStyle", ISLabel, 0, 0, -1, text,
        color.r, color.g, color.b, 1, UIFont.NewSmall, true)
    label:initialise()
    label:instantiate()

    local row = panel.rootTable:addRow()
    panel.rootTable:setElement(0, row:index(), label)
end

-- The rows a build menu can show, as text and colour. Vanilla's panel turns
-- them into labels; Neat Building's draws them itself, which is why the numbers
-- live here and the drawing does not.
function AllInfo.Structures.buildRows(logic, player)
    local rows = {}
    if not AllInfo.enabled("StructStrength") and not AllInfo.enabled("StructAtMax") then
        return rows
    end

    local info = logic and logic:getSelectedBuildObject()
    local script = info and info:getScript()
    if not script then return rows end

    -- What the game's formula gives this build with the relevant skill maxed.
    -- Zero means the script declares no health of any kind, which is a chair or
    -- a shelter, not a wall: there is no number to give, so no rows.
    --
    -- This used to read `if script:getHealth() == -1 then return end`, taken
    -- off ISBuildIsoEntity:getHealth() as the game's own "no health" marker. It
    -- means the opposite: -1 is "no health *declared in the script*", and the
    -- figure then comes from skillBaseHealth. It cost the rows on the 33
    -- entities that carry skillBaseHealth without health, which is nearly every
    -- metal and brick door, frame, gate and window in the game.
    if healthAtSkill(script, 10) <= 0 then return rows end

    local recipe = info:getRecipe()
    local craftRecipe = recipe and recipe:getCraftRecipe()
    if not craftRecipe then return rows end

    local level = craftRecipe:getHighestRelevantSkillLevel(player)
    if AllInfo.enabled("StructStrength") then
        rows[#rows + 1] = {
            text = getText("UI_AllInfo_StructureStrength") .. ": "
                .. AllInfo.num(healthAtSkill(script, level), 0),
            color = { r = 1, g = 1, b = 1 },
        }
    end

    -- What another five levels would buy you, which is the whole reason to
    -- know the number before building. Skipped when it changes nothing.
    local perSkill = script:getSkillBaseHealth()
    if perSkill <= 0 or level >= 10 then return rows end

    -- getHighestRelevantSkill() only looks at the recipe's *required* skills,
    -- while getHighestRelevantSkillLevel() -- the one ISBuildIsoEntity actually
    -- multiplies by -- also counts the XP awards. A build like the Advanced
    -- Forge requires nothing and awards nothing, so the perk came back nil and
    -- the line printed "With  at 10: 650" with a hole in it. The fallback
    -- covers the award case; with neither there is no skill that raises this
    -- build's health at all, so the line has nothing true to say and goes.
    local perk = craftRecipe:getHighestRelevantSkill(player)
        or craftRecipe:getHighestRelevantSkillFromXpAward(player)
    if not perk then return rows end

    -- getName() is the perk's translated display name and the only thing that
    -- is right for every perk: "IGUI_perks_" .. getId() misses the five whose
    -- id and key differ (Foraging is registered as PlantScavenging) and printed
    -- the raw key.
    if AllInfo.enabled("StructAtMax") then
        rows[#rows + 1] = {
            text = getText("UI_AllInfo_StructureAtMax", perk:getName())
                .. ": " .. AllInfo.num(healthAtSkill(script, 10), 0),
            color = AllInfo.color(true),
        }
    end

    return rows
end

function AllInfo.Structures.addBuildRows(panel)
    for _, row in ipairs(AllInfo.Structures.buildRows(panel.logic, panel.player)) do
        addLabel(panel, row.text, row.color)
    end
end

-- createDynamicChildren rebuilds the whole panel on every recipe change and
-- ends with xuiRecalculateLayout(), so appending a row afterwards means laying
-- it out again. The table does the positioning, which is why the row goes
-- there instead of into ISWidgetTitleHeader's hand-placed labels.
local baseCreate = ISBuildRecipePanel.createDynamicChildren

function ISBuildRecipePanel:createDynamicChildren(...)
    baseCreate(self, ...)
    if not self.rootTable or not self.logic or not self.logic:getRecipe() then return end

    local ok, err = pcall(AllInfo.Structures.addBuildRows, self)
    if not ok then
        print("[AllInfo] structure build rows disabled: " .. tostring(err))
        AllInfo.Structures.addBuildRows = function() end
        return
    end

    self:xuiRecalculateLayout()
end

AllInfo.hooks = AllInfo.hooks or {}
AllInfo.hooks.BuildRecipePanel = ISBuildRecipePanel.createDynamicChildren

-- 3) Neat Building ----------------------------------------------------------

-- Neat Building replaces ISEntityUI.OpenBuildWindow, so the vanilla panel
-- hooked above is never opened: the strength rows *and* the XP line from
-- CraftingUI are both gone while it is on, with no error and no log line.
--
-- Its detail panel is the piece that carries what a build demands. Unlike Neat
-- Crafting's it grows: calculateLayout() sizes it and the parent is an
-- ISTableLayout that respects the result, which is the same mechanism vanilla's
-- panel uses. So the rows go on screen, not into a tooltip, and cost one hook
-- to measure and one to draw.
--
-- Its logic is BuildLogic, the very same Java object vanilla's panel carries,
-- so buildRows() reads it unchanged.

local FONT_HGT_SMALL = getTextManager():getFontHeight(UIFont.Small)

local function neatRows(panel)
    local recipe = panel.logic and panel.logic:getRecipe()
    if not recipe then return {} end

    local rows = {}

    -- XP first: it belongs with the skill requirement it sits under.
    if AllInfo.enabled("MasterCrafting") then
        for _, text in ipairs(AllInfo.xpLines(recipe) or {}) do
            rows[#rows + 1] = { text = text, color = AllInfo.color(true) }
        end
    end

    for _, row in ipairs(AllInfo.Structures.buildRows(panel.logic, panel.player)) do
        rows[#rows + 1] = row
    end

    return rows
end

-- The same arithmetic its own render walks: padding, the wrapped description,
-- padding, one line per skill requirement. Repeating it is what keeps the rows
-- under the last line it drew, whatever that line was.
local function drawNeatRows(panel)
    local rows = neatRows(panel)
    if #rows == 0 then return end

    local recipe = panel.logic:getRecipe()
    local width = panel.width - panel.padding * 2
    local y = panel.padding

    if recipe:getTooltip() then
        local wrapped = getTextManager():WrapText(UIFont.Small, getText(recipe:getTooltip()), width)
        for _ in string.gmatch(wrapped, "[^\n]+") do y = y + FONT_HGT_SMALL end
        y = y + panel.padding
    end

    y = y + FONT_HGT_SMALL * #panel:getSkillRequirements()

    for _, row in ipairs(rows) do
        local text = row.text
        if NeatTool and NeatTool.truncateText then
            text = NeatTool.truncateText(text, width, UIFont.Small, "...")
        end

        panel:drawText(text, panel.padding, y, row.color.r, row.color.g, row.color.b, 1, UIFont.Small)
        y = y + FONT_HGT_SMALL
    end
end

local function installNeatBuilding()
    local class = NB_BuildingInfoDetailPanel
    if not class then return end
    if AllInfo.hooks.NB_DetailLayout == class.calculateLayout then return end   -- already ours

    local baseLayout = class.calculateLayout
    local baseRender = class.render

    -- Its own calculateLayout recomputes from minimumHeight every time, so this
    -- adds to a fresh figure and never accumulates.
    class.calculateLayout = function(self, ...)
        baseLayout(self, ...)

        local ok, rows = pcall(neatRows, self)
        if ok and #rows > 0 then
            self:setHeight(self.height + FONT_HGT_SMALL * #rows)
        end
    end

    class.render = function(self, ...)
        baseRender(self, ...)

        local ok, err = pcall(drawNeatRows, self)
        if not ok then
            print("[AllInfo] Neat Building rows disabled: " .. tostring(err))
            class.calculateLayout = baseLayout
            class.render = baseRender
        end
    end

    AllInfo.hooks.NB_DetailLayout = class.calculateLayout
    AllInfo.hooks.NB_DetailRender = class.render
end

-- Same load-order reason as Neat Crafting in CraftingUI.lua: the class is nil
-- here unless we happen to load last, and OnGameStart is the pass that lands.
installNeatBuilding()

if not AllInfo.hooks.neatBuildingHooked then
    AllInfo.hooks.neatBuildingHooked = true
    Events.OnGameStart.Add(installNeatBuilding)
end
