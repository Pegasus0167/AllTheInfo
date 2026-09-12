require "AllInfo/Core"
-- ISToolTipInv lives in a folder that loads after AllInfo/ alphabetically, so
-- require it rather than trusting load order.
require "ISUI/ISToolTipInv"

-- Draws the AllInfo block under vanilla's tooltip content.
--
-- ISToolTipInv:render() runs measure -> clamp -> self:setWidth(tw) ->
-- self:setHeight(th) -> drawRect + drawRectBorder -> draw content. Because
-- setWidth/setHeight run *before* the background is painted, intercepting them
-- on the instance grows the panel using this frame's numbers. (More Item
-- Information reads the previous frame's height instead, which is why it
-- misaligns.)
--
-- ISToolTipItemSlot, the crafting ingredient and tool slots, is deliberately
-- not hooked: those are items you already own and the recipe screen reads
-- better without a block on every slot. The crafting *output* is phase 5.

local SEPARATOR_H = 5    -- 1px rule plus breathing room
local GAP = 16           -- minimum gap between the label and value columns
local DELTA_GAP = 6

AllInfo.hooks = AllInfo.hooks or {}

-- ObjectTooltip.padLeft/padRight are public Java fields, but PZ's Lua binding
-- exposes methods only, so reading them yields nil. ObjectTooltip.checkFont()
-- sets both to MeasureStringX(font, "0"), so deriving it here matches vanilla
-- exactly at any tooltip font size or UI scale instead of hardcoding a number.
function AllInfo.pad(font)
    return getTextManager():MeasureStringX(font, "0")
end

-- Where one axis of the tooltip has to sit once our rows have changed its size.
--
-- ISToolTipInv:render() measures vanilla's tooltip, places it with *that* size,
-- and only then calls the two setters we intercept, so the placement it decided
-- is stale by the time our block exists and has to be redone here.
--
-- `anchor` is the coordinate of an edge the panel hangs *from*, not the corner
-- it starts at: that is the controller UI. ISInventoryPane clears followMouse
-- and hands over an anchorBottomLeft, and vanilla then places the tooltip by its
-- bottom edge, `y = anchor.y - th`. A taller panel has to move up; growing down
-- from vanilla's y is what put the block on top of the inventory panel.
-- Reported by QuickBASIC.
--
-- With no anchor the origin stands and only the clamp applies, which is
-- vanilla's own `max(0, min(v, screen - size - 1))` with our size instead of
-- its. That half is not controller-only: vanilla clamped x against the width it
-- measured, and ours is wider, so near the right edge the block ran off screen
-- with the mouse too.
--
-- Pure arithmetic on purpose. It is the only part of this fix that can be
-- asserted without a controller plugged in, and SelfTest does.
function AllInfo.clampPos(origin, anchor, size, screen)
    local v = anchor and (anchor - size) or origin
    return math.max(0, math.min(v, screen - size - 1))
end

-- Two or three MeasureStringX calls into Java per row, on every frame the
-- tooltip is up. AllInfo.rows hands back the *same* table while its own cache
-- is warm, so remembering the last answer skips the whole sweep until the rows
-- are actually rebuilt. One entry is enough: only one tooltip is ever on screen.
local lastRows, lastFont, lastPad, lastWidth

local function measure(rows, font, pad)
    if rows == lastRows and font == lastFont and pad == lastPad then return lastWidth end

    local tm = getTextManager()
    local widest = 0

    for i = 1, #rows do
        local r = rows[i]
        local w = tm:MeasureStringX(font, r.label) + GAP + tm:MeasureStringX(font, r.value)
        if r.delta then w = w + DELTA_GAP + tm:MeasureStringX(font, r.delta) end
        if w > widest then widest = w end
    end

    lastRows, lastFont, lastPad, lastWidth = rows, font, pad, widest + pad * 2
    return lastWidth
end

function AllInfo.draw(panel, rows, vanillaH, width, font, lineH, pad)
    local tt = panel.tooltip
    local tm = getTextManager()

    panel:drawRect(pad, vanillaH + 2, width - pad * 2, 1, 0.35, 1, 1, 1)

    local y = vanillaH + SEPARATOR_H
    for i = 1, #rows do
        local r = rows[i]
        tt:DrawText(font, r.label, pad, y, 1, 1, 1, 1)

        local right = width - pad
        if r.delta then
            local dc = r.deltaColor or { r = 1, g = 1, b = 1 }
            tt:DrawTextRight(font, r.delta, right, y, dc.r, dc.g, dc.b, 1)
            right = right - tm:MeasureStringX(font, r.delta) - DELTA_GAP
        end

        local c = r.color or { r = 1, g = 1, b = 1 }
        tt:DrawTextRight(font, r.value, right, y, c.r, c.g, c.b, 1)

        y = y + lineH
    end
end

-- Set of the wrappers we have installed, so install() can recognise its own
-- work. On AllInfo.hooks because a debug hot reload re-runs this file and the
-- wrapper already on the field was made by the previous run.
AllInfo.hooks.ours = AllInfo.hooks.ours or {}

-- Nesting depth across every wrapper of ours in the chain. If a mod between two
-- of ours calls through, the inner one must pass the call along and add nothing:
-- one block per tooltip, drawn by the outermost link, which is the one whose
-- setWidth/setHeight interception is still in place.
--
-- The count also has to break a loop, which is what it did not do before. A mod
-- that reinstalls its own wrapper in OnGameStart -- after ours, the same trick we
-- use ourselves for the same reason -- can leave our link calling theirs and
-- theirs calling ours straight back. Verified in game: three lines close the
-- ring, and the process hangs on the first frame a tooltip appears. Handing the
-- call to `base` is exactly what closes it, so the old `depth > 0 -> base(self)`
-- was the loop rather than a guard against it. Past LIMIT links we return having
-- called nothing: that costs one frame of tooltip, ours and theirs, and saves the
-- session.
--
-- ponytail: LIMIT is a flat 8. Honest depth only grows when someone overwrites
-- the field between two of our installs, so 8 covers eight of those in a single
-- session, well past anything real. A loop burns all 8 every frame and a probe
-- doing 20 per frame still held 60 FPS, so the ceiling is generous on purpose.
-- Raise it if a real chain is ever seen near it -- the log line names the case.
local depth = 0
local LIMIT = 8
local loopReported = false

-- The counter is reset every frame, and that half is load-bearing.
--
-- Reproduced in game: force one throw between the increment and the decrement
-- and `depth` stays at 1 for good. From the next frame on every call takes the
-- `depth > 1` pass-through branch, no row is ever built again, and the whole mod
-- is off for the session with every toggle still ticked -- silent, and only a
-- restart clears it. That is the ronda 11 bug wearing a new hat, and it is the
-- player report: "no text is displayed when the mouse is over any item". One
-- error, anywhere in the path, once.
--
-- No arrangement of pcalls prevents that: a Java exception crosses pcall
-- (trap 19), so the decrement can always be skipped. Resetting beats trusting
-- the unwind. UIManager.render() fires OnPreUIDraw before it draws any UI
-- element, on the Lua thread, so honest nesting -- which never outlives a frame
-- -- is untouched, while a leak cannot outlive the frame that caused it. It also
-- makes the LIMIT message stop lying: reaching 8 now really does mean recursion
-- inside a single frame, which is the only thing it ever claimed to detect.
--
-- Re-subscribes on a debug hot reload, because the new run closes over a new
-- `depth` and the old handler would be zeroing a counter nobody reads.
if AllInfo.hooks.frameReset then Events.OnPreUIDraw.Remove(AllInfo.hooks.frameReset) end
AllInfo.hooks.frameReset = function() depth = 0 end
Events.OnPreUIDraw.Add(AllInfo.hooks.frameReset)

-- SelfTest reads this. A depth stuck above zero would silently hide the block for
-- the rest of the session with every toggle still ticked, which is the ronda 11
-- bug wearing a new hat, so it is worth an assertion of its own.
function AllInfo.hooks.renderDepth() return depth end

-- Items whose block threw: skipped for them from then on, reported once.
--
-- The failure belongs to the *item*, not to the session: one odd modded item
-- must not take the block away from every other tooltip. Same reasoning and same
-- shape as the per-provider report in AllInfo.rows, one layer up -- that one
-- covers a provider throwing, this one covers everything around it.
--
-- Reporting once is not politeness, it is the only thing that works: Kahlua
-- prints the trace even when the error is caught (trap 75), so catching is not
-- enough to keep the log quiet. Not calling again is. A throw on every frame is
-- some 2000 lines a second to disk, which is the "hard freeze" half of the same
-- report.
-- The count is what SelfTest and the debug console read: Kahlua's BaseLib has no
-- `next`, so "is this table empty" is not a question Lua can ask here (verified
-- against the jar -- the only vanilla file that calls it is ISPriorityTable.lua).
AllInfo.hooks.renderFailed = AllInfo.hooks.renderFailed or {}
AllInfo.hooks.renderFails = AllInfo.hooks.renderFails or 0
local failed = AllInfo.hooks.renderFailed

-- Diagnostics only: clears the marks without restarting the game, so a test can
-- run more than once per session. Reassigns rather than emptying in place --
-- deleting keys while iterating is not something Kahlua promises.
function AllInfo.hooks.renderReset()
    failed = {}
    AllInfo.hooks.renderFailed = failed
    AllInfo.hooks.renderFails = 0
end

local function fail(self, err)
    local item = self.item or false
    if failed[item] then return end
    failed[item] = true
    AllInfo.hooks.renderFails = AllInfo.hooks.renderFails + 1

    -- An error handler must not interrogate the object that just failed
    -- (trap 75): ask instanceof first, fall back to tostring.
    local id = item and instanceof(item, "InventoryItem") and item:getFullType()
        or tostring(item)
    print("[AllInfo] tooltip block failed on " .. id .. ": " .. tostring(err)
        .. " -- skipped for that item, vanilla's tooltip is unaffected")
end

local renderRows   -- defined below; makeRender closes over the name

-- Builds the rows for this tooltip, or nil when there is nothing to add. Split
-- out so the whole of *our* work sits inside one pcall: this ran bare between
-- the increment and the decrement, and a throw here is what stranded the
-- counter -- verified in game, `Render.lua:139` in the trace.
local function collect(self)
    local item = self.item
    if not item or failed[item] then return nil end
    return AllInfo.rows(item, self.tooltip and self.tooltip:getCharacter())
end

local function makeRender(base)
    return function(self)
        if depth >= LIMIT then
            if not loopReported then
                loopReported = true
                print("[AllInfo] ISToolTipInv.render calls back into itself past "
                    .. LIMIT .. " of our links: another mod reinstalls its own"
                    .. " wrapper after ours. Item tooltips are skipped while that"
                    .. " lasts. Moving AllInfo later in the load order avoids it.")
            end
            return
        end

        depth = depth + 1

        -- Only our own work is guarded. A throw out of `base` belongs to vanilla
        -- or to the mod we wrapped, and goes up untouched: swallowing it would
        -- hide their bug and paint nothing anyway. The frame reset above is what
        -- makes letting it through safe -- an escaping error can no longer strand
        -- the counter, so there is no reason left to catch what is not ours.
        if depth > 1 then
            base(self)                      -- inner link: pass through, add nothing
        else
            local ok, rows = pcall(collect, self)
            if not ok then
                fail(self, rows)
                rows = nil
            end

            if rows and #rows > 0 then
                renderRows(self, rows, base)
            else
                base(self)
            end
        end

        depth = depth - 1
    end
end

-- Draws vanilla's tooltip (through `base`) with our block appended, growing the
-- panel by intercepting the two setters on the instance while it runs.
renderRows = function(self, rows, base)
    local tt = self.tooltip
    local font = tt:getFont()
    local lineH = tt:getLineSpacing()
    local pad = AllInfo.pad(font)
    local extraH = #rows * lineH + SEPARATOR_H
    local neededW = measure(rows, font, pad)

    -- rawget so we restore to nil rather than freezing a copy of a method
    -- another mod may have put on the instance.
    local hadSetH, hadSetW = rawget(self, "setHeight"), rawget(self, "setWidth")
    local vanillaH, finalW

    self.setHeight = function(s, h, ...)
        vanillaH = h
        local total = h + extraH

        -- Bottom-anchored only in the controller UI. followMouse is checked
        -- first because that is the flag vanilla itself branches on, and the
        -- pane leaves anchorBottomLeft set while the mouse is back in charge.
        local anchorY
        if not s.followMouse and s.anchorBottomLeft then
            anchorY = s.anchorBottomLeft.y
        end

        local y = AllInfo.clampPos(s.tooltip:getY(), anchorY, total,
            getCore():getScreenHeight())
        s.tooltip:setY(y)
        s:setY(y)

        return ISPanel.setHeight(s, total, ...)
    end

    self.setWidth = function(s, w, ...)
        finalW = math.max(w, neededW)

        -- No anchor on this axis: anchorBottomLeft is a *left* edge, so the
        -- origin is already the corner the panel starts at.
        local x = AllInfo.clampPos(s.tooltip:getX(), nil, finalW,
            getCore():getScreenWidth())
        s.tooltip:setX(x)
        s:setX(x)

        s.tooltip:setWidth(finalW)   -- keeps vanilla's right-aligned column in line
        return ISPanel.setWidth(s, finalW, ...)
    end

    local ok, err = pcall(base, self)
    self.setHeight, self.setWidth = hadSetH, hadSetW
    if not ok then error(err) end

    -- vanillaH is still nil when a context menu is open: vanilla skips its
    -- whole render body, so there is no background to draw our rows on.
    --
    -- Guarded on its own, and after `base` has already painted: vanilla's tooltip
    -- is on screen by now, so a throw here costs our rows and nothing else.
    -- Calling `base` again to "recover" would draw it twice, at a different size,
    -- with the setters already restored.
    if vanillaH then
        local dok, derr = pcall(AllInfo.draw, self, rows, vanillaH,
            finalW or self:getWidth(), font, lineH, pad)
        if not dok then fail(self, derr) end
    end
end

-- Wrapping once at load time only wins if we load last, and load order is the
-- mod list: whoever comes after us decides whether we survive. Nature's Call
-- reassigns ISToolTipInv.render at load, saves the previous one in
-- NC_OriginalRender and *never calls it*, so every mod that loaded earlier is
-- simply gone from the tooltip -- no error, no log line, and the options screen
-- still shows every toggle ticked. That is the "last update broke the numbers
-- again" report, and it comes back whenever the mod list is reordered.
--
-- OnGameStart runs after every mod's Lua, so we wrap again there. Whatever sits
-- on the field by then is what we call through to, vanilla's or another mod's:
-- NC's render measures and then calls self:setWidth/self:setHeight exactly like
-- vanilla, which is all our block needs to size itself and land underneath. If
-- some future render never calls setHeight, vanillaH stays nil and we simply
-- draw nothing rather than painting on air.
--
-- Each install captures its own base, so nothing is ever rewired behind an
-- existing link: an older wrapper of ours keeps calling exactly what it wrapped.
-- That, plus the depth guard, is what makes running this twice harmless rather
-- than an endless call -- the failure mode a single shared base would have had
-- against a mod that wraps us correctly (More Item Information does).
--
-- Worst case with such a mod is now two of our links in one chain, and the inner
-- one passes through: same tooltip, same single block, one extra function call.
local function install()
    if AllInfo.hooks.ours[ISToolTipInv.render] then return end   -- already ours

    local wrapper = makeRender(ISToolTipInv.render)
    AllInfo.hooks.ours[wrapper] = true     -- SelfTest checks the field is one of these
    ISToolTipInv.render = wrapper
end

install()

-- One subscription, however many times this file runs (debug hot reload).
if not AllInfo.hooks.installHooked then
    AllInfo.hooks.installHooked = true
    Events.OnGameStart.Add(install)
end
