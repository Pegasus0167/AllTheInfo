require "AllInfo/Core"
-- ISUI/ loads after AllInfo/ alphabetically, so require rather than trust it.
require "ISUI/ISPanel"

-- The moodle column, drawn by us so the hover box can fit its own text.
--
-- The bug: zombie.ui.MoodlesUI sizes that box as (lineHeight + 2) * 2 -- room
-- for exactly two rows, a title and one line of description -- and AllInfo's
-- moodle descriptions are lists several lines long, so everything past the
-- second row lands on the game world with no background behind it. render() is
-- a single Java method with no Lua seam, the field holding the box height is
-- private, and there is no asking it which moodle sits in which slot either:
-- the slots are handed out while iterating a HashMap<MoodleType, ...> keyed on
-- identity hash codes. Reading a hover means owning the column, so this draws
-- the whole thing and vanilla's widget is switched off.
--
-- Everything is reproduced from MoodlesUI's own bytecode: the same textures,
-- the same 10 + iconSize spacing, the same gray -> good/bad tint by level, the
-- same slide-in from 500 px below, the same box geometry and colours. Three
-- deliberate differences: the box grows with the text (the point), the order is
-- fixed instead of varying between launches, and the little wiggle a moodle
-- does when its level changes is not replicated.
--
-- Fails safe: any error here puts vanilla's widget back and this one goes quiet
-- for the rest of the session, so the worst case is the tooltip we started
-- with rather than no moodles at all.

AllInfo.Moodles = AllInfo.Moodles or {}

-- MoodleType -> icon, in a fixed order. Vanilla's own order is HashMap order
-- over identity hash codes, which is why the column reshuffles itself between
-- launches; declaration order is stable and reads better.
-- ponytail: the file names are lifted from MoodleTextureSet's constructor,
-- which builds them with a string concat the compiler inlines, so they cannot
-- be read at runtime -- and the class is not exposed to Lua, so it cannot be
-- instanced either. Re-check when a patch adds a moodle; a wrong entry costs
-- that one icon and nothing else.
local MOODLES = {
    { MoodleType.ENDURANCE,     "Status_DifficultyBreathing" },
    { MoodleType.TIRED,         "Mood_Sleepy" },
    { MoodleType.HUNGRY,        "Status_Hunger" },
    { MoodleType.THIRST,        "Status_Thirst" },
    { MoodleType.PANIC,         "Mood_Panicked" },
    { MoodleType.STRESS,        "Mood_Stressed" },
    { MoodleType.ANGRY,         "Mood_Angry" },
    { MoodleType.UNHAPPY,       "Mood_Sad" },
    { MoodleType.BORED,         "Mood_Bored" },
    { MoodleType.SICK,          "Mood_Nauseous" },
    { MoodleType.HAS_A_COLD,    "Mood_Ill" },
    { MoodleType.INJURED,       "Status_InjuredMinor" },
    { MoodleType.BLEEDING,      "Status_Bleeding" },
    { MoodleType.PAIN,          "Mood_Pained" },
    { MoodleType.DRUNK,         "Mood_Drunk" },
    { MoodleType.HEAVY_LOAD,    "Status_HeavyLoad" },
    { MoodleType.WET,           "Status_Wet" },
    { MoodleType.HYPERTHERMIA,  "Status_TemperatureHot" },
    { MoodleType.HYPOTHERMIA,   "Status_TemperatureLow" },
    { MoodleType.WINDCHILL,     "Status_Windchill" },
    { MoodleType.UNCOMFORTABLE, "Mood_Discomfort" },
    { MoodleType.NOXIOUS_SMELL, "Mood_NoxiousSmell" },
    { MoodleType.CANT_SPRINT,   "Status_MovementRestricted" },
    -- Third field is the level below which the moodle is not drawn at all.
    -- "Well fed" is the only one vanilla hides that way, at
    -- Moodle.MoodleLevel.HighMoodleLevel.ordinal(), and it is the only per-type
    -- rule in the whole of MoodlesUI.update().
    { MoodleType.FOOD_EATEN,    "Status_Hunger", 3 },
    { MoodleType.DEAD,          "Mood_Dead" },
    { MoodleType.ZOMBIE,        "Mood_Zombified" },
}

local SIZES = { 32, 48, 64, 80, 96, 128 }

local FONT = UIFont.Small
local EDGE = 10      -- MoodlesUI.DistFromRightEdge: gap from the icons to the box
local BOX_PAD = 6    -- padding either side of the text inside the box
local SLIDE = 500    -- how far below its slot a new moodle starts
local GRAY = 0.5     -- zombie.core.Color.gray, the untinted background

-- MoodlesUI.getTextureSizeForOption(), fallbacks included: the last option
-- ("match font size") reads the font setting instead, and anything unknown is 32.
local function iconSize()
    local opt = getCore():getOptionMoodleSize() - 1
    if SIZES[opt + 1] then return SIZES[opt + 1] end

    if opt == 6 then
        local font = getCore():getOptionFontSizeReal() - 1
        if SIZES[font + 1] then return SIZES[font + 1] end
    end

    return 32
end

-- Textures are per size and the size only changes from the options screen, so
-- one cached set is enough.
local textures

local function textureSet(size)
    if textures and textures.size == size then return textures end

    local dir = "media/ui/Moodles/" .. size .. "/"
    local set = {
        size = size,
        background = getTexture(dir .. "_Moodles_BGsolid.png"),
        border = getTexture(dir .. "_Moodles_BGoutline.png"),
        icons = {},
    }
    for i = 1, #MOODLES do
        set.icons[i] = getTexture(dir .. MOODLES[i][2] .. ".png")
    end

    textures = set
    return set
end

-- Both hand-maintained and both silent when wrong -- a missing MoodleType or a
-- renamed png just drops an icon -- so SelfTest sweeps them.
AllInfo.Moodles.list = MOODLES
AllInfo.Moodles.textureSet = textureSet

-- MoodlesUI lerps the background from gray toward the good or bad highlight by
-- level/4. It does it on packed ABGR ints; per channel in floats is the same
-- line. 0 is neutral, 1 good, 2 bad (Moodles.NeutralMoodleType and friends).
local function tint(goodBadNeutral, level)
    if goodBadNeutral ~= 1 and goodBadNeutral ~= 2 then return GRAY, GRAY, GRAY end

    local c = goodBadNeutral == 1 and getCore():getGoodHighlitedColor()
        or getCore():getBadHighlitedColor()
    local f = level / 4

    return GRAY + (c:getR() - GRAY) * f,
           GRAY + (c:getG() - GRAY) * f,
           GRAY + (c:getB() - GRAY) * f
end

local function lineCount(text)
    local n = 1
    for _ in text:gmatch("\n") do n = n + 1 end
    return n
end

-- Slot animation state, by index into MOODLES. nil means "not on screen", which
-- is also what makes the next appearance slide in.
local slotY = {}

-- ⚠️ Everything that must survive a re-execution of this file lives on
-- AllInfo.Moodles, never in a local.
--
-- With debug mode on, ZomboidFileSystem hands every mod folder to
-- DebugFileWatcher, so saving over a mod's .lua while the game is running
-- re-runs it in place. A second run of this file used to build a second panel
-- and add it to the UI manager next to the first, and two panels draw the same
-- box, icons and text at the same coordinates: the antialiased edges thicken
-- and the 0.6 alpha box doubles up, which is the "duplicated and bold" report.
-- It only ever happened "after a while", because it takes a deploy while the
-- game is up. AllInfo.register carries the same guard for providers, with the
-- same comment.
if AllInfo.Moodles.loaded then
    print("[AllInfo] Moodles.lua re-executed; keeping the panel that is already up")
end
AllInfo.Moodles.loaded = true

AllInfoMoodlesUI = ISPanel:derive("AllInfoMoodlesUI")
-- ISBaseObject:derive() sets __index on the *parent*, and only ISPanel:new()
-- sets it on the derived table. ensurePanel() re-points an existing panel at
-- this table without going through new(), so it has to be set here or the
-- adopted panel would find no methods at all.
AllInfoMoodlesUI.__index = AllInfoMoodlesUI

function AllInfoMoodlesUI:new()
    local o = ISPanel.new(self, 0, 0, 32, 32)
    o:noBackground()
    -- Nothing here is clickable, and a column-wide mouse trap in front of the
    -- world would be a bug of its own. instantiate() reads this field.
    o.wantMouseEvents = false
    return o
end

-- Vanilla's moodle widget off (and back on).
--
-- **Not setVisible().** That flag does nothing to this widget, and every attempt
-- at hiding it with one was a no-op:
--   * UIManager.render() has no isVisible() check in its loop. It filters on
--     isIgnoreLossControl, isFollowGameWorld and isDefaultDraw and then calls
--     render() straight out.
--   * MoodlesUI overrides UIElement.render() and never calls super, so the
--     guard that stops every Lua panel does not exist here either. Only
--     drawPercentageBackground() looks at the flag, and that method is dead
--     code in B42.20.
-- So vanilla kept drawing its own column right on top of ours, in its own
-- HashMap order: the same moodle in the slots where the two orders happened to
-- agree -- which looked like text drawn twice in bold -- and a different one
-- where they did not. That is precisely the report.
--
-- The character is the real switch: render() and update() both return on the
-- spot when it is null, and setCharacter() is public, idempotent and cheap.
-- This is called from our render(), and this panel is backMost, so it goes
-- first in the UI list and vanilla's render() in the same frame already sees
-- the null.
--
-- Only player 0's widget: IsoPlayer sets its own on creation, so split screen
-- and a fresh game both get theirs back without us.
--
-- Asymmetric on purpose. Hiding repeats every frame because IsoPlayer hands the
-- widget its character back on creation; *showing* only ever gives back what we
-- took. Another mod may be hiding this same widget to draw its own column --
-- "Moodles in Lua", which Nature's Call requires, does exactly that -- and
-- turning it back on every frame with our option off left that player with two
-- columns and no switch that helped: ours off, vanilla's back, theirs still
-- drawing. With this, a player who never turns our column on never has the
-- widget touched by us at all.
local function setVanillaEnabled(on)
    local ui = UIManager.getMoodleUI(0)
    if not ui then return end

    if not on then
        AllInfo.Moodles.hidVanilla = true
        ui:setCharacter(nil)
        return
    end

    if not AllInfo.Moodles.hidVanilla then return end
    local player = getSpecificPlayer(0)
    if not player then return end   -- nothing to hand back yet; stay hidden

    AllInfo.Moodles.hidVanilla = false
    ui:setCharacter(player)
end

-- "Moodles In Lua" (MIL), which Nature's Call requires, replaces the whole
-- column with its own Lua panel and hides vanilla's by moving it off-screen.
-- Two columns drawing the same icons is the bug, and ours is the one that steps
-- aside -- not because theirs is better, because stopping it loses information
-- and stopping ours loses nothing:
--   * Nature's Call hangs its bladder, bowel and gut icons off MIL's render and
--     checks the same `active` flag, so switching MIL off would take those three
--     with it. They are not MoodleTypes, so our column cannot show them.
--   * Everything ours adds is the Moodles_* translation keys, which overwrite
--     vanilla's. MIL asks Java for the description like everyone else, so it
--     shows them without knowing -- and it sizes its box with MeasureStringY,
--     which counts newlines (AngelCodeFont.getHeight starts at 1 line and
--     increments on char 10). The two-row box we exist to fix is already fixed
--     over there.
-- Texture packs and MoodleFramework-style extra moodles need no check of their
-- own: we draw the same textures at the same spacing as vanilla, so a pack
-- reskins us too and anything stacking below lands where it expects.
local function rivalColumn()
    local mil = ISMoodlesInLuaHandle
    return mil ~= nil and mil.active == true
end

-- The whole reason this file exists. Vanilla writes the same six draw calls
-- with the height hardcoded to two rows; here it follows the text.
function AllInfoMoodlesUI:drawHoverBox(moodles, mtype, y, size, player)
    local title = moodles:getMoodleDisplayString(mtype) or ""
    local desc = moodles:getMoodleDescriptionString(mtype) or ""

    -- ⚠️ NOXIOUS_SMELL, not SICK. Corpse sickness does add to
    -- CharacterStat.FOOD_SICKNESS in BodyDamage.UpdateIllness(), which is what
    -- made Nauseous look like the right home for it, but that is the moodle for
    -- food poisoning in general. The one that actually reports corpses is
    -- Noxious smell: Moodle.update() reads
    -- IsoGameCharacter.getCorpseSicknessRate() against MoodleStat.NOXIOUS_SMELL,
    -- whose thresholds are 0.001 and 0.002. Verified in bytecode after a first
    -- pass hung the count on the wrong icon.
    --
    -- How many corpses are doing it is on no screen in the game, cheat mode
    -- included.
    --
    -- Appended, never replacing: vanilla's own text still says what being sick
    -- costs you, and this only adds the cause.
    --
    -- Below six the count is printed anyway when it is not zero, because
    -- "corpses nearby but under the threshold" is the answer that stops you
    -- blaming the food you just ate. AllInfo.corpseCount returns 0 there rather
    -- than nil, so a 0 means "none close enough" and nil means "cannot tell",
    -- and only the second one drops the row.
    if mtype == MoodleType.NOXIOUS_SMELL and AllInfo.enabled("MoodleCorpses") then
        local corpses = player and AllInfo.corpseCount(player)
        if corpses and corpses > 0 then
            desc = desc .. "\n" .. getText("UI_AllInfo_mask_Corpses", AllInfo.num(corpses, 0))
        end
    end

    local tm = getTextManager()
    -- AngelCodeFont.getWidth() restarts its accumulator on a newline, so it
    -- already answers with the longest line and multi-line text needs no
    -- splitting to measure.
    local width = math.max(tm:MeasureStringX(FONT, title), tm:MeasureStringX(FONT, desc))
    local lineH = tm:getFontHeight(FONT)

    -- Vanilla: (lineH + 2) * 2. Same 2 px above and below, any number of rows.
    local height = (1 + lineCount(desc)) * lineH + 4

    local top = math.floor(y) + 1
    if size > height then top = top + math.floor((size - height) / 2) end

    self:drawRect(-EDGE - width - BOX_PAD, top - 2, width + BOX_PAD * 2, height, 0.6, 0, 0, 0)
    self:drawTextRight(title, -EDGE, top, 1, 1, 1, 1, FONT)
    self:drawTextRight(desc, -EDGE, top + lineH, 0.8, 0.8, 0.8, 1, FONT)
end

function AllInfoMoodlesUI:drawColumn(player)
    local moodles = player:getMoodles()
    if not moodles then return end

    local size = iconSize()
    local dist = 10 + size
    local set = textureSet(size)

    local x, y = self:getX(), self:getY()
    local mouseX, mouseY = getMouseX(), getMouseY()
    local hovered = -1
    if mouseX >= x and mouseX < x + size then
        hovered = math.floor((mouseY - y) / dist)
    end

    local slot = 0
    for i = 1, #MOODLES do
        local mtype = MOODLES[i][1]
        local level = mtype and moodles:getMoodleLevel(mtype) or 0
        if level < (MOODLES[i][3] or 1) then level = 0 end

        if level <= 0 then
            slotY[i] = nil
        else
            -- MoodlesUI.update(): a new moodle drops in from SLIDE below its
            -- slot and closes 15% of the gap per frame until it is within 0.8.
            local target = slot * dist
            local pos = slotY[i] or (target + SLIDE)
            if math.abs(pos - target) > 0.8 then
                pos = pos + (target - pos) * 0.15
            else
                pos = target
            end
            slotY[i] = pos

            local r, g, b = tint(moodles:getGoodBadNeutral(mtype), level)
            self:drawTexture(set.background, 0, pos, 1, r, g, b)
            self:drawTexture(set.border, 0, pos, 1)
            if set.icons[i] then self:drawTexture(set.icons[i], 0, pos, 1) end

            if slot == hovered then self:drawHoverBox(moodles, mtype, pos, size, player) end
            slot = slot + 1
        end
    end
end

-- One draw per frame, and one *column* per frame however many panels are on
-- screen: the state is on the shared table so a second run of this file reads
-- the same value. Milliseconds are the only per-frame token available; the game
-- never renders the UI a thousand times a second, so no real frame is lost.
--
-- `broken` is the fail-safe: raised before the draw and cleared after it
-- returns, because a Java exception thrown inside a Lua->Java call has been seen
-- walking straight through a pcall. Once it is up, vanilla's widget comes back
-- and this one stays quiet. Shared for the same reason.
--
-- Everything runs from render() rather than prerender(): UIManager skips an
-- invisible element entirely, so a panel that hides itself never runs again and
-- could not put vanilla's widget back. This one stays visible and draws nothing.
AllInfo.Moodles.lastDraw = AllInfo.Moodles.lastDraw or -1
AllInfo.Moodles.broken = AllInfo.Moodles.broken or false
AllInfo.Moodles.hidVanilla = AllInfo.Moodles.hidVanilla or false

function AllInfoMoodlesUI:frame()
    local vanilla = UIManager.getMoodleUI(0)
    if not vanilla then return end

    -- Nothing here reads UIManager.visibleAllUi. "Hide interface" is
    -- ISUIHandler.setVisibleAllUI, which walks UIManager.getUI() and hides every
    -- visible element one by one -- this panel included -- and a hidden Lua
    -- panel stops rendering, so this stops drawing on its own. (Vanilla's widget
    -- ignores that flag entirely, which is the whole story below, but with no
    -- character it draws nothing either way.) One less static field read, and
    -- that field is a primitive: see what IsoPlayer.numPlayers did.
    local player = getSpecificPlayer(0)
    local mine = player ~= nil and AllInfo.enabled("MoodleTooltip")
    -- Ceding the *drawing* is not ceding the switch. MIL believes it hides
    -- vanilla's widget and does not manage to: hideMoodles() guards on
    -- `ui.setX and ui.setY`, and indexing a Java method as a field yields nil
    -- (trap 3.15), so the branch never runs -- and it never marks the widget as
    -- handled either, so it retries every frame forever, in silence. Leaving
    -- vanilla's column up next to MIL's is the two-column bug all over again,
    -- with the offset that comes of vanilla and MIL each choosing their own top.
    -- So: our option on hides vanilla whoever ends up drawing, our option off
    -- touches nothing.
    local draw = mine and not rivalColumn()

    -- Vanilla draws the icons and the two-line box together, with no way to
    -- keep one without the other, so it is switched off while we are drawing.
    -- Every frame, not once: IsoPlayer hands the widget its character back on
    -- creation, and setCharacter() returns immediately when nothing changed.
    setVanillaEnabled(not mine)
    if not draw then return end

    local now = getTimestampMs()
    if now == AllInfo.Moodles.lastDraw then return end
    AllInfo.Moodles.lastDraw = now

    -- Follow vanilla's widget for position, so screen size, the clock offset
    -- and split screen are all whatever the game already worked out.
    self:setX(vanilla:getX())
    self:setY(vanilla:getY())
    self:setWidth(iconSize())

    self:drawColumn(player)
end

-- The whole frame is inside the guard, hiding vanilla's widget included. It
-- used to sit outside, so the one thing that did throw -- comparing the static
-- int IsoPlayer.numPlayers -- walked past the pcall and up into Java every
-- frame instead of switching this off once.
function AllInfoMoodlesUI:render()
    if AllInfo.Moodles.broken then return end

    AllInfo.Moodles.broken = true
    local ok, err = pcall(self.frame, self)
    AllInfo.Moodles.broken = false

    if not ok then
        AllInfo.Moodles.broken = true
        print("[AllInfo] moodle panel disabled: " .. tostring(err))
        -- Last thing this panel does: give the player their moodles back.
        pcall(setVanillaEnabled, true)
    end
end

-- One panel, ever. A second run of this file adopts the one already on screen
-- -- with this run's methods, so a hot reload still takes effect -- instead of
-- adding another to the UI manager beside it.
local function ensurePanel()
    local p = AllInfo.Moodles.panel
    if p then
        setmetatable(p, AllInfoMoodlesUI)
        return p
    end

    p = AllInfoMoodlesUI:new()
    p:initialise()
    p:instantiate()
    AllInfo.Moodles.panel = p
    return p
end

-- And one handler: Events.OnGameStart.Add on a re-executed file would stack a
-- second subscription, and the next time a save loaded both would run.
if not AllInfo.Moodles.hooked then
    AllInfo.Moodles.hooked = true

    Events.OnGameStart.Add(function()
        local p = ensurePanel()
        -- UIManager.AddUI queues a remove before the add, so re-adding an
        -- element that is already there is safe -- and it is needed, because
        -- going back to the main menu drops it. backMost is a flag on the
        -- element, not a list operation, so the order of these two does not
        -- matter: vanilla's widget is built at startup and therefore sits under
        -- every window, and this one has to as well or it would cover them.
        p:addToUIManager()
        p:backMost()
    end)
end

-- A hot reload happens mid-game, long after OnGameStart: adopt the live panel
-- now so this run's code is what draws the next frame.
if AllInfo.Moodles.panel then ensurePanel() end
