require "AllInfo/Core"
require "AllInfo/Render"   -- the ISToolTipInv wrapper this subclass inherits
require "Entity/ISUI/CraftRecipe/ISWidgetOutput"
require "Entity/ISUI/CraftRecipe/ISWidgetTooltipOutput"
require "Entity/ISUI/Controls/ISWidgetTitleHeader"

-- Full item tooltips on the *output* of a recipe: what the thing you are about
-- to craft will actually be, instead of vanilla's bare display name.
--
-- The output widgets build a plain text ISToolTip in createScriptValues() and
-- feed it through icon:setMouseOverText(). ISImage:updateTooltip() then drives
-- that object with getIsVisible / addToUIManager / setVisible / .description /
-- setDesiredPosition / removeFromUIManager. ISToolTipInv inherits all of those
-- from ISPanel except setDesiredPosition, so adapting that one call is the
-- whole job: no vanilla class is modified, only which tooltip gets instanced.
--
-- Inputs and tools are deliberately left alone. They are items you already own
-- and the recipe screen reads better without a block on every slot.

AllInfoItemTip = ISToolTipInv:derive("AllInfoItemTip")

-- ISImage:updateTooltip() calls this unconditionally to pin an ISToolTip under
-- the icon, and ISToolTipInv has no such method. Deliberately a no-op: leaving
-- followMouse alone (ISToolTipInv:new sets it) is what makes render() take
-- getMouseX/getMouseY, so the block on a recipe output trails the cursor
-- exactly like the same item does from the inventory. Anchoring it to the icon
-- instead was the odd one out.
function AllInfoItemTip:setDesiredPosition(_x, _y)
end

function AllInfoItemTip:new(item)
    return ISToolTipInv.new(self, item)
end

-- ISImage:updateTooltip() only ever hides the tooltip object it is holding at
-- that moment, so swapping one out while it is on screen would leave it stuck
-- there forever.
local function useTip(icon, tip)
    local current = icon.tooltipUI
    if current == tip then return end

    if current and current:getIsVisible() then
        current:setVisible(false)
        current:removeFromUIManager()
    end
    icon.tooltipUI = tip
end

local function hookOutputWidget(class, name)
    local baseCreate = class.createScriptValues

    class.createScriptValues = function(self, _script, ...)
        local t = baseCreate(self, _script, ...)

        -- Fluid and energy outputs have no InventoryItem behind them, so they
        -- keep vanilla's text tooltip.
        if t and t.icon and _script:getResourceType() == ResourceType.Item then
            t.allInfoVanillaTip = t.icon.tooltipUI

            local tip = AllInfoItemTip:new(nil)
            tip:setOwner(t.icon)
            tip:setVisible(false)
            tip:setAlwaysOnTop(true)
            -- The character is what makes the figures match the ones the same
            -- item shows in your inventory (Maintenance, attack speed), and it
            -- is also what lets the block compare the output against the tool
            -- or weapon you are holding.
            tip:setCharacter(self.player)
            t.allInfoTip = tip
        end

        return t
    end

    local baseUpdate = class.updateScriptValues

    class.updateScriptValues = function(self, _table, ...)
        baseUpdate(self, _table, ...)
        if not _table or not _table.allInfoTip then return end

        -- Read every frame: the icon cycles through getPossibleResultItems()
        -- when a recipe has several, and the tooltip has to follow it.
        -- ponytail: this follows the rotating candidate. With
        -- isManualSelectInputs() vanilla overrides the icon afterwards in
        -- updateValues() with outputMapper:getOutputItem(); the tooltip can
        -- then show a different possible result of the same recipe. Upgrade
        -- path is hooking updateValues() and re-running the mapper.
        local proto = AllInfo.enabled("CraftingTooltips")
            and AllInfo.proto(_table.inputFullName) or nil

        if proto then
            _table.allInfoTip:setItem(proto)
            useTip(_table.icon, _table.allInfoTip)
        else
            -- Unknown fullType or the toggle is off: back to vanilla's text.
            useTip(_table.icon, _table.allInfoVanillaTip)
        end
    end

    AllInfo.hooks[name] = class.updateScriptValues   -- SelfTest checks this is still ours
end

hookOutputWidget(ISWidgetOutput, "ISWidgetOutput")
hookOutputWidget(ISWidgetTooltipOutput, "ISWidgetTooltipOutput")

-- Neat Crafting -------------------------------------------------------------

-- Neat Crafting (Workshop 3502080466) replaces the crafting window whole, so
-- the two widgets above are never instanced and everything up to here is dead
-- code while it is on. Its own output slots build an ISToolTip carrying the
-- display name and nothing else, which is the "no comparison against my weapon"
-- report.
--
-- Only createTooltip is swapped. Its removeTooltip does setVisible(false) +
-- removeFromUIManager() and drops the field, all three of which ISToolTipInv
-- inherits from ISPanel, so the teardown already works on ours. Nothing here
-- runs unless the mod is installed, and the vanilla hooks above stay live
-- because Neat Crafting can be toggled back to the vanilla window in its own
-- options.
local function hookNeatSlot(class, name, scriptOf, playerOf)
    if not class then return end
    if AllInfo.hooks[name] == class.createTooltip then return end   -- already ours

    local base = class.createTooltip

    class.createTooltip = function(self, ...)
        if self.tooltip or not AllInfo.enabled("CraftingTooltips") then
            return base(self, ...)
        end

        -- Fluid outputs have no script item behind them and keep vanilla's text.
        local script = scriptOf(self)
        local proto = script and AllInfo.proto(script:getFullName())
        if not proto then return base(self, ...) end

        local tip = AllInfoItemTip:new(proto)
        tip:setOwner(self)
        tip:setItem(proto)
        -- Same reason as the vanilla widgets: the character is what makes the
        -- figures match your inventory and what lets the block compare the
        -- output against the weapon in your hands. Guarded because it is read
        -- off Neat Crafting's own panels, and a nil there would reach Java.
        local chr = playerOf(self)
        if chr then tip:setCharacter(chr) end
        tip:addToUIManager()
        tip:setVisible(true)
        tip:setAlwaysOnTop(true)
        self.tooltip = tip
    end

    AllInfo.hooks[name] = class.createTooltip
end

local hookNeatXp   -- defined at the end, once AllInfo.xpLines exists

-- The result slot, and the boxes in the output picker that slot opens.
local function installNeat()
    hookNeatSlot(NC_CraftOutput_Slot, "NC_CraftOutput_Slot",
        function(self) return self.actualOutputItem end,
        function(self) return self.player end)

    hookNeatSlot(NC_OutputSwitch_Box, "NC_OutputSwitch_Box",
        function(self) return self.itemInfo and self.itemInfo.scriptItem end,
        function(self) return self.parentPanel and self.parentPanel.player end)

    hookNeatXp()
end

-- XP per craft ---------------------------------------------------------------

-- What a recipe pays, which the game reads out of `xpAward = Tailoring:13` and
-- never shows. The base figure only: no XP boost from the profession, no book
-- multiplier, no trait. Those are the same for every recipe and already have
-- their own line on the skill tooltip, and folding them in here would make one
-- number mean two things.
--
-- ISWidgetTitleHeader is the piece both recipe windows share: crafting
-- (ISCraftRecipePanel) and building (ISBuildRecipePanel). One hook, both.
--
-- It went to ISCraftRecipeInfoBox first, and that showed nothing anywhere,
-- because the only thing that builds an InfoBox is ISCraftRecipeTooltip, and
-- **that tooltip never appears**: all three panels that could raise one set
-- `recipesPanel.noTooltip = true` on themselves, so only the debug recipe
-- browser ever shows it. Finished vanilla code wired to nothing (state, trap
-- 183), and the reason a hook can look right and be invisible.
--
-- The label is pushed onto requiredSkillList, which is not a hack: that list is
-- only ever walked to measure and to place, so a line added there lands right
-- under "Requires Tailoring Level 2" and the layout does the arithmetic. Writing
-- our own y would mean redoing a layout that already knows how.
--
-- No option of its own: the section master already covers it, and a tickbox for
-- one row of five words is a setting nobody goes looking for.
-- The one place that reads `xpAward` off a recipe, shared by the three windows
-- that can carry the line: vanilla's, Neat Crafting's and Neat Building's.
-- Returns nil when the recipe pays nothing.
--
-- The guard `if not recipe.getXPAwardCount then return end` is gone: it was
-- written against an older script format that cannot happen, since both methods
-- are on CraftRecipe itself, so every recipe has them and one that awards
-- nothing counts zero. It was not firing either, which trap 15 would predict
-- (a Java method indexed as a field reads nil): the line was on screen in
-- 0.9.22, so that trap is narrower than it reads and does not cover this class.
function AllInfo.xpLines(recipe)
    if not recipe then return nil end

    local lines = nil

    for i = 0, recipe:getXPAwardCount() - 1 do
        local award = recipe:getXPAward(i)
        local perk = award and award:getPerk()
        local amount = award and award:getAmount()

        if perk and amount and amount > 0 then
            lines = lines or {}
            lines[#lines + 1] = getText("UI_AllInfo_CraftXp") .. " " .. perk:getName()
                .. " +" .. amount
        end
    end

    return lines
end

-- Repair: what it gives back and what it can cost ----------------------------

-- Vanilla says "Chance of failing and damaging the item" and stops there, with
-- a whole mechanic behind it that nobody sees: every repair makes the next one
-- worse. The seven Repair recipes call
-- RecipeCodeOnCreate.genericFixer(data, chr, t, item), verified in bytecode:
--
--   r     = item:getHaveBeenRepaired(), read *before* the call bumps it
--   fail  = clamp(25 - 5t - 5*Maintenance + 2r, 0, 95), and at Maintenance 0
--           it is +10 rather than -0
--   the roll is `Rand.Next(100) <= fail`, so the real odds are (fail + 1)%:
--           a clamped 0 still fails one time in a hundred
--   gain  = max(1, (condMax - cond) * (10t / max(r,1) + min(5*Maint, 25)) / 100)
--   failing costs one condition point
--
-- ponytail: the tier comes from a table of seven recipe names because it cannot
-- be read at runtime. CraftRecipe.getLuaCallString(LuaCall.OnCreate) answers it
-- in Java, but LuaCall is not among the 1007 classes LuaManager.Exposer
-- registers, so Lua cannot build the argument. A repair recipe from another mod
-- gets no line at all, which is the right way to fail: one row less beats an
-- invented number. Upgrade path: if a build ever exposes LuaCall, swap the
-- table for that one call and every modded recipe is covered for free.
local REPAIR_TIER = {
    FixWithAdhesiveTape = 1,
    FixWithZipties      = 1,
    FixWithGlue         = 1,
    FixWithEpoxyAndRags = 1,
    FixWithDuctTape     = 2,
    FixWithWoodGlue     = 2,
    FixWithEpoxy        = 3,
}

-- Returns nil for anything that is not one of the seven, or when no item is
-- picked yet: with no item there is no r and no condition, so there is no
-- honest figure to print.
function AllInfo.repairLine(recipe, logic, chr)
    if not recipe or not logic or not chr then return nil end

    local tier = REPAIR_TIER[recipe:getName()]
    if not tier then return nil end

    -- ⚠️ NOT getSatisfiedInputItems(): it is declared
    -- `List<zombie.scripting.objects.Item>`, so it answers with the item
    -- *definitions* that would satisfy the input, not the thing in your bag.
    -- A script Item has no condition and no repair count, so asking it for
    -- getHaveBeenRepaired() threw "tried to call nil" and took the whole recipe
    -- panel down with it. ISWidgetInput gets away with that call because it only
    -- ever asks for the texture and the display name, which both kinds carry.
    --
    -- getFirstInputItemWithFlag answers with the real InventoryItem the player
    -- has in the slot. IsDamaged rather than Prop2: both flags sit on the same
    -- input in all seven recipes, but Prop2 is an animation prop and IsDamaged
    -- is the one that actually means "this is the thing being repaired".
    local data = logic:getRecipeData()
    local item = data and data:getFirstInputItemWithFlag("IsDamaged")
    if not item then return nil end

    local maint = chr:getPerkLevel(Perks.Maintenance)
    local repaired = item:getHaveBeenRepaired() or 0

    local fail = 25 - tier * 5
    if maint > 0 then fail = fail - maint * 5 else fail = fail + 10 end
    fail = fail + repaired * 2
    if fail < 0 then fail = 0 elseif fail > 95 then fail = 95 end

    local worn = item:getConditionMax() - item:getCondition()
    local gain = worn * (tier * 10 / math.max(repaired, 1) + math.min(maint * 5, 25)) / 100
    if gain < 1 then gain = 1 end

    -- The count only earns its place once it is doing something: at zero it
    -- would be a row saying the number changes nothing.
    local key = repaired > 0 and "UI_AllInfo_RepairAgain" or "UI_AllInfo_Repair"
    return getText(key, math.floor(gain), AllInfo.pct((fail + 1) / 100), repaired)
end

-- ⚠️ Isolated like every provider, and here it matters more than usual: this
-- runs inside the recipe panel's own createChildren, so an error that escapes
-- does not cost us a row, it costs the player the entire panel. Vanilla's
-- crafting window then shows a highlighted recipe with nothing beside it and no
-- hint that a mod did it, which is exactly what the first build of this row did
-- before the guard went in.
--
-- Switches itself off for the session on the first throw rather than filling
-- console.txt one frame at a time.
-- Takes the three pieces rather than a panel, because the two windows that can
-- carry the row keep them under different names: vanilla's widget has .recipe,
-- Neat Crafting's panel gets the recipe as an argument and holds the rest.
local function safeRepairLine(recipe, logic, chr)
    if not AllInfo.repairLine then return "" end
    if not AllInfo.enabled("MasterCrafting") then return "" end

    local ok, text = pcall(AllInfo.repairLine, recipe, logic, chr)
    if not ok then
        print("[AllInfo] repair line disabled: " .. tostring(text))
        AllInfo.repairLine = nil
        return ""
    end

    return text or ""
end

local baseTitleHeader = ISWidgetTitleHeader.createChildren

function ISWidgetTitleHeader:createChildren()
    baseTitleHeader(self)

    if not self.requiredSkillList then return end
    if not AllInfo.enabled("MasterCrafting") then return end

    for _, text in ipairs(AllInfo.xpLines(self.recipe) or {}) do
        -- -1, not a font height: vanilla's own labels in this widget pass
        -- that and ISLabel reads "<= 0" as "measure the font yourself".
        -- FONT_HGT_SMALL is a *local* of each vanilla file, not a global, so
        -- it arrives here as nil and ISLabel dies on `nil <= 0`.
        local label = ISXuiSkin.build(self.xuiSkin, "S_NeedsAStyle", ISLabel,
            0, 0, -1, text,
            self.colGood.r, self.colGood.g, self.colGood.b, self.colGood.a,
            UIFont.NewSmall, true)
        label.origTitleStr = text
        label:initialise()
        label:instantiate()
        self:addChild(label)
        self.requiredSkillList[#self.requiredSkillList + 1] = label
    end

    -- Built for any of the seven, even when the text is still empty. The row is
    -- the only one here whose figures move while the panel is open, so it needs
    -- a handle to refresh; and claiming its height up front keeps the layout
    -- from jumping the moment an item lands in the slot. createChildren can run
    -- before the inputs are auto-populated, which is exactly the case that
    -- would otherwise never show a line at all.
    if REPAIR_TIER[self.recipe and self.recipe:getName()] then
        local text = safeRepairLine(self.recipe, self.logic, self.player)
        local label = ISXuiSkin.build(self.xuiSkin, "S_NeedsAStyle", ISLabel,
            0, 0, -1, text,
            self.colGood.r, self.colGood.g, self.colGood.b, self.colGood.a,
            UIFont.NewSmall, true)
        label.origTitleStr = text
        label:initialise()
        label:instantiate()
        self:addChild(label)
        self.requiredSkillList[#self.requiredSkillList + 1] = label
        self.allInfoRepairLabel = label
    end
end

AllInfo.hooks.CraftXp = ISWidgetTitleHeader.createChildren

-- updateLabels is what the recipe panel calls after the inputs change, so it is
-- the seam that keeps the figures honest when the player swaps the weapon or
-- repairs it again. Wrapped rather than replaced, and it never throws on its
-- own: repairLine returns nil for anything it cannot answer.
local baseUpdateLabels = ISWidgetTitleHeader.updateLabels

function ISWidgetTitleHeader:updateLabels(...)
    baseUpdateLabels(self, ...)

    local label = self.allInfoRepairLabel
    if not label then return end

    local text = safeRepairLine(self.recipe, self.logic, self.player)
    label.origTitleStr = text
    label:setName(text)
end

AllInfo.hooks.CraftRepair = ISWidgetTitleHeader.updateLabels

-- The XP line under Neat Crafting --------------------------------------------

-- Neat Crafting has no ISWidgetTitleHeader either, so the hook above is dead
-- while it is on. Its own recipe panel is a *fixed* height, NCConfig sizes it
-- as one medium line plus three small ones, and a loaded recipe (description,
-- workstation, skill) already fills it, so there is no room on screen for a
-- fourth row. That is why its author put the skill requirements inside a
-- button's tooltip, and it is where the XP goes too.
--
-- self.skillRequirements is plain text that its own prerender paints, green
-- when met and red when not, so a row appended there needs no drawing and no
-- layout of ours: ours is always green, because XP is not something you fail.
local function xpLinesOf(recipe)
    if not AllInfo.enabled("MasterCrafting") then return nil end
    return AllInfo.xpLines(recipe)
end

-- createSkillRequirementIcon returns before building anything when the recipe
-- demands no skill, and a recipe can pay XP while demanding nothing: saying
-- nothing there would tell the player that build is worth no XP, which is the
-- one thing this mod does not do. So the button is built by its own code
-- anyway, with a recipe that reports one requirement.
--
-- ponytail: these three methods are everything that function reads off the
-- recipe today. If it grows a fourth, the pcall below swallows the nil call and
-- the button just does not appear; add the method here when that happens.
local function countProxy(recipe)
    return {
        getRequiredSkillCount = function() return 1 end,
        getTooltip = function() return recipe:getTooltip() end,
        requiresSpecificWorkstation = function() return recipe:requiresSpecificWorkstation() end,
    }
end

hookNeatXp = function()
    local class = NC_RecipeInfoPanel
    if not class then return end
    if AllInfo.hooks.NC_SkillRequirements == class.updateSkillRequirements then return end

    local baseRequirements = class.updateSkillRequirements

    class.updateSkillRequirements = function(self, recipe, ...)
        baseRequirements(self, recipe, ...)

        for _, text in ipairs(xpLinesOf(recipe) or {}) do
            self.skillRequirements[#self.skillRequirements + 1] = { text = text, isMet = true }
        end

        -- The repair row rides in the same list. Neat Crafting replaces the
        -- whole window, so ISWidgetTitleHeader is never built and the vanilla
        -- path above is dead while it is on: without this the seven repair
        -- recipes said nothing at all there.
        --
        -- Always green: these are figures, not a requirement you can fail.
        -- The recipe arrives as an argument here, the logic and the player off
        -- the panel, which is why safeRepairLine takes the three apart.
        local repair = safeRepairLine(recipe, self.logic, self.player)
        if repair ~= "" then
            self.skillRequirements[#self.skillRequirements + 1] =
                { text = repair, isMet = true, allInfoRepair = true }
        end
    end

    -- ⚠️ Neat Crafting rebuilds that list only from onRecipeChanged, so picking
    -- a different weapon in the ingredient slot left the figures describing the
    -- one before it. Vanilla does not have the problem because its own update()
    -- calls updateTitleWidget() every frame.
    --
    -- The row is refreshed in place rather than by re-running
    -- updateSkillRequirements: that function clears the whole table, and doing
    -- it per frame would throw away the requirement icons built alongside it.
    -- The flag set above is what finds our row again.
    local basePrerender = class.prerender

    class.prerender = function(self, ...)
        if self.logic and self.skillRequirements then
            for _, req in ipairs(self.skillRequirements) do
                if req.allInfoRepair then
                    req.text = safeRepairLine(self.logic:getRecipe(), self.logic, self.player)
                end
            end
        end

        basePrerender(self, ...)
    end

    AllInfo.hooks.NC_Prerender = class.prerender

    AllInfo.hooks.NC_SkillRequirements = class.updateSkillRequirements

    local baseIcon = class.createSkillRequirementIcon

    class.createSkillRequirementIcon = function(self, recipe, ...)
        baseIcon(self, recipe, ...)

        -- Its own call built one: the XP rows are already inside that tooltip.
        if self.skillRequirementIcon or not recipe then return end
        if not xpLinesOf(recipe) then return end

        -- The label is a local of its function, read through getText on every
        -- call, so this is the only seam that reaches it. Without it the button
        -- would read "Required skills" on a recipe that requires none.
        -- ponytail: a global swapped for the length of one call, restored even
        -- if that call throws. Replacing its prerender instead would mean
        -- copying 20 lines of another mod's drawing code and going stale with
        -- it.
        local label = getText("UI_AllInfo_CraftXp")
        local realGetText = getText

        getText = function(key, ...)
            if key == "IGUI_NC_RequiredSkills" then return label end
            return realGetText(key, ...)
        end

        local ok, err = pcall(baseIcon, self, countProxy(recipe))
        getText = realGetText

        if not ok then
            print("[AllInfo] Neat Crafting XP button disabled: " .. tostring(err))
            class.createSkillRequirementIcon = baseIcon
        end
    end

    AllInfo.hooks.NC_SkillIcon = class.createSkillRequirementIcon
end

-- Load order decides whether those classes exist yet, and it is the mod list:
-- with AllInfo before Neat Crafting they are all nil here. OnGameStart runs
-- after every mod's Lua, so that is the pass that lands; the call below only
-- wins when we happen to load last, and each hook returns early rather than
-- wrapping itself twice.
installNeat()

if not AllInfo.hooks.neatHooked then
    AllInfo.hooks.neatHooked = true
    Events.OnGameStart.Add(installNeat)
end

-- The quick repair menu -------------------------------------------------------

-- Right-clicking a damaged weapon offers "Repair with duct tape" straight from
-- the inventory, with a tooltip that lists the ingredients and ends on vanilla's
-- "Chance of failing and damaging the item". Same sentence, same missing number,
-- and it is the route most people actually use: the crafting window is the long
-- way round for one repair.
--
-- CraftTooltip is a local of ISInventoryPaneContextMenu.lua, but the file
-- publishes it as ISRecipeTooltip, and the context menu hands it .recipe,
-- .character and .logic, which is exactly what repairLine needs.
--
-- ⚠️ layoutContents caches: it returns early when self.contents is already
-- built, and the tooltips come out of a pool that reset() empties. So the row
-- is appended only on the pass that actually builds the contents, never on the
-- cached ones, and the figures are those of the moment the tooltip opened.
-- That is right for this menu: nothing can change while it is on screen.
require "ISUI/ISInventoryPaneContextMenu"

if ISRecipeTooltip and AllInfo.hooks.RecipeTooltip ~= ISRecipeTooltip.layoutContents then
    local baseLayout = ISRecipeTooltip.layoutContents

    function ISRecipeTooltip:layoutContents(x, y)
        local cached = self.contents ~= nil
        local width, height = baseLayout(self, x, y)
        if cached or not self.contents then return width, height end

        local text = safeRepairLine(self.recipe, self.logic, self.character)
        if text == "" then return width, height end

        -- Vanilla's own margins, read off layoutContents: 20 left, 10 bottom.
        -- The last line ends at height minus that bottom margin, so the row goes
        -- just under it and the box grows by one line.
        self:addText(x + 20, y + height - 10 + 4, text)

        -- Same closing loop vanilla runs, because the box was measured before
        -- this row existed.
        self.contentsWidth = 0
        self.contentsHeight = 0
        for _, v in ipairs(self.contents) do
            self.contentsWidth = math.max(self.contentsWidth, v.x + v.width - x)
            self.contentsHeight = math.max(self.contentsHeight, v.y + v.height + 10 - y)
        end

        return self.contentsWidth, self.contentsHeight
    end

    AllInfo.hooks.RecipeTooltip = ISRecipeTooltip.layoutContents
end
