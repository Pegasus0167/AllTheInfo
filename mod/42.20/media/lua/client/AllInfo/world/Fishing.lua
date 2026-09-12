require "AllInfo/Core"
require "Fishing/FishingUtils"
require "Fishing/fishing_properties"
require "Fishing/FishingZones"
require "PZAPI/ui/organisms/FishWindow"

-- Fishing panel (right-click water -> "Fishing"). Not a debug window: the option
-- comes from ISWorldObjectContextMenuLogic when the square has the water flag,
-- is under 20 tiles away, is not shore and you are not sitting on the ground.
-- No rod needed either. FishingDebugWindow.lua is a different panel that no Lua
-- of the game ever instantiates.
--
-- Vanilla prints "Normal" / "Good" / "Bad" for four factors and never says what
-- they are worth, hides two more (hook and fish abundance) that weigh exactly
-- the same in the roll, and gates the four rows behind Fishing 2/4/6/8.
--
-- Nothing here reimplements a formula vanilla exposes: the coefficients are
-- asked to Fishing.Utils and the tables (hook, rods, line, fishes) are read
-- live, so any fishing mod that adds to them is picked up for free.

AllInfo.Fishing = AllInfo.Fishing or {}

local F = AllInfo.Fishing

-- Vanilla's own level thresholds, reused verbatim when FishingGate is on. Each
-- one is the level at which FishWindow.lua itself stops printing "Unknown".
local GATE = { time = 2, temperature = 4, weather = 6, wind = 8 }

-- Two separate questions, and mixing them was a bug: whether vanilla is already
-- printing the value, and whether we are allowed to fill in the gap it leaves.
function F.vanillaShows(level, needed)
    return level >= needed
end

function F.mayReveal()
    return not AllInfo.enabled("FishingGate")
end

-- Numbers ------------------------------------------------------------------

-- ponytail: the 0.8 base and the five wait steps are inline constants inside
-- Bobber:attractFish / Bobber:getNibbleTime, so they are copied here. Anything
-- vanilla exposes as a function is called, not copied. Re-check on each patch.
local BASE_CHANCE = 0.8

-- 45 lb, the hard ceiling initFishSizeData puts on any caught fish.
local WEIGHT_CAP = 45 / 2.2

-- Bobber:getNibbleTime() recomputes the abundance coefficient with 0 for an
-- empty square, while getFishNumParams answers 0.1 for the same case. Two
-- copies of one table that vanilla wrote differently: the wait uses this one.
local function nibbleCoeff(abundance)
    if abundance == 0 then return 0 end
    if abundance < 10 then return 0.5 end
    if abundance <= 25 then return 1.0 end
    return 1.5
end

local function nibbleTicks(product)
    if product == 0 then return 2000 end
    if product < 40 then return 1500 end
    if product < 65 then return 1000 end
    if product < 80 then return 650 end
    return 500
end

-- How much longer than the best possible case you wait between bites. 500 ticks
-- is that best case; near shore doubles it and a bobber under 3 tiles away
-- triples it, both applied in Bobber:update after the first attempt.
function F.waitRatio(ticks, nearShore, tooClose)
    local ratio = ticks / 500
    if nearShore then ratio = ratio * 2 end
    if tooClose then ratio = ratio * 3 end
    return ratio
end

-- Lowest Fishing level whose weight cap lets this species bite at all
-- (Fish:getFishByLure -> canCatch = maxWeight <= skillSizeLimit[level]).
function F.minLevel(cfg)
    if type(cfg.maxWeight) ~= "number" then return nil end
    for lvl = 0, 10 do
        if cfg.maxWeight <= Fishing.Utils.skillSizeLimit[lvl] then return lvl end
    end
    return nil
end

-- Chance of each species given the bait, the water and your level, derived the
-- same way Fish:getFishByLure rolls it: proportional to fishConfig.lure[bait]
-- among the candidates.
--
-- Two regimes, because predators only bite while you are reeling in (isReel):
-- `base` is the sedentary case and excludes them, `reel` includes them. A single
-- blended figure would be wrong in both.
function F.speciesOdds(lure, isRiver, level)
    local out = { base = {}, reel = {} }
    if not lure then return out end

    local cap = Fishing.Utils.skillSizeLimit[level] or 0
    local sumBase, sumReel = 0, 0
    local candidates = {}

    for _, cfg in ipairs(Fishing.fishes) do
        local weight = cfg.lure[lure]
        local fits = type(cfg.maxWeight) == "number" and cfg.maxWeight <= cap
        local here = (isRiver and cfg.isRiver) or (not isRiver and cfg.isLake)
        if weight and weight > 0 and fits and here then
            candidates[#candidates + 1] = cfg
            sumReel = sumReel + weight
            if not cfg.isPredator then sumBase = sumBase + weight end
        end
    end

    for _, cfg in ipairs(candidates) do
        local weight = cfg.lure[lure]
        if sumReel > 0 then out.reel[cfg.itemType] = weight / sumReel * 100 end
        if sumBase > 0 and not cfg.isPredator then
            out.base[cfg.itemType] = weight / sumBase * 100
        end
    end

    return out
end

-- The panel has no square of its own. While you are fishing the answer is where
-- the bobber sits; otherwise it is the square the mouse points at, which is
-- exactly where a cast would land. The last valid water square is remembered so
-- the rows do not blank out while the mouse is over the panel itself.
local function fishingBobber(player)
    local key = isMultiplayer() and player:getUsername() or player:getPlayerNum()
    local manager = Fishing.ManagerInstances and Fishing.ManagerInstances[key]
    local rod = manager and manager.fishingRod
    return rod and rod.bobber or nil
end

function F.targetSquare(player)
    local bobber = fishingBobber(player)
    if bobber then
        F.lastX, F.lastY = bobber:getX(), bobber:getY()
        return F.lastX, F.lastY
    end

    local x, y = Fishing.Utils.getAimCoords(player)
    if x and y and Fishing.Utils.isWaterCoords(x, y) then
        F.lastX, F.lastY = x, y
    end
    return F.lastX, F.lastY
end

-- Everything the rows need, in one table. Fields that cannot be known are left
-- nil and the caller drops the row: never a made-up number.
function F.params(player)
    if not player then return nil end

    -- hasTag() is called, never indexed: a Java method read as a field comes
    -- back nil, which would silently drop every rod.
    local rod = player:getPrimaryHandItem()
    if rod and not rod:hasTag(ItemTag.FISHING_ROD) then rod = nil end
    local mod = rod and rod:getModData() or nil

    local p = {
        level = player:getPerkLevel(Perks.Fishing),
        rod = rod,
        lure = mod and mod.fishing_Lure or nil,
        temperature = Fishing.Utils.getTemperatureParams(player),
        weather = Fishing.Utils.getWeatherParams(),
        time = Fishing.Utils.getTimeParams(),
        hook = Fishing.Utils.getHookParams(mod and mod.fishing_HookType or nil),
        wind = getClimateManager():getWindPower(),
        fog = getClimateManager():getFogIntensity(),
    }

    local x, y = F.targetSquare(player)
    if x and y then
        -- FishSchoolManager takes (int, int), so the tile is floored here
        -- rather than trusting the binding to narrow a double.
        local tx, ty = math.floor(x), math.floor(y)
        p.x, p.y = tx, ty
        p.noFish = Fishing.isNoFishZone(tx, ty)
        p.isRiver = Fishing.isRiver(tx, ty)
        p.nearShore = Fishing.Utils.isNearShore(tx, ty)
        p.tooClose = IsoUtils.DistanceTo(player:getX(), player:getY(), x, y) < 3
        p.fish = Fishing.Utils.getFishNumParams(tx, ty)
        p.trash = FishSchoolManager.getInstance():getTrashAbundance(tx, ty)
    end

    -- Bite chance per attempt. ZombRand(100) < chance*100 saturates at 100%.
    if p.fish then
        local chance = BASE_CHANCE * p.temperature.coeff * p.weather.coeff
            * p.time.coeff * p.hook.coeff * p.fish.coeff
        p.bite = math.min(chance, 1)

        local product = nibbleCoeff(p.fish.value) * p.temperature.coeff
            * p.weather.coeff * p.time.coeff * 100
        p.wait = F.waitRatio(nibbleTicks(product), p.nearShore, p.tooClose)
    end

    return p
end

-- Tooltips -------------------------------------------------------------------

local INFO = PZAPI.UI.FishWindow.children.body.children.tabPanel.children.info

-- Same shape as vanilla's own FishTooltip in FishWindow.lua (a black box that
-- grows to its text), which is local to that file and cannot be reused.
local Tooltip = PZAPI.UI.Texture{
    r = 0, g = 0, b = 0, a = 0.85,
    width = 316, height = 100,
    children = {
        text = PZAPI.UI.Text{
            x = 8, y = 8,
            height = 32,
            scaleX = 0.5, scaleY = 0.5,
            pivotY = 0, pivotX = 0,
            -- The box is measured from the text, in both directions, and the
            -- word wrap is switched off to make that possible: setAutoWidth
            -- breaks a long line *during the render*, after the measuring has
            -- happened, so every wrapped line was one line of height that the
            -- box never got. With no wrap, getTextHeight() is exactly the
            -- newlines the text carries and getTextWidth() is its longest line.
            --
            -- Both getters answer in unscaled units while the node draws at
            -- scale, hence the multiplications. 16 is the 8px padding twice.
            -- A long line now makes the box wider instead of spilling out of it.
            init = function(self)
                self.javaObj:setAutoWidth(99999)
                self:setText(self.parent.body or "")
                self.parent:setHeight(self.javaObj:getTextHeight() * self.scaleY + 16)
                self.parent:setWidth(math.max(316,
                    self.javaObj:getTextWidth() * self.scaleX + 16))
            end
        }
    }
}

-- Exposed on the table on purpose: F.build is defined further down but a local
-- declared after a function is not an upvalue of it, and the species hover
-- lives inside F.build. Through the table it resolves per call.
function F.showTooltip(node, body)
    local pos = node.javaObj:getLuaAbsolutePosition(8, 8)
    node.tooltip = Tooltip{ x = pos.x, y = pos.y }
    node.tooltip.body = body or ""
    node.tooltip:instantiate()
end

function F.hideTooltip(node)
    if node.tooltip then
        UIManager.RemoveElement(node.tooltip.javaObj)
        node.tooltip = nil
    end
end

-- Vanilla's four header rows get their hover on the *template*, before anything
-- is instantiated: UI._applyHooks reads onHover when the element is built and
-- registers the mouse dispatcher then. The width is capped because a UI.Text
-- defaults to Node's 256, so the left column would reach x=286 and swallow the
-- hover of the right one.
local function attachTip(node, key)
    node.width = 190
    node.height = 17
    node.onHover = function(self, state)
        if state then
            F.showTooltip(self, getText(key))
        else
            F.hideTooltip(self)
        end
    end
end

attachTip(INFO.children.textTime, "UI_AllInfo_fish_tip_Time")
attachTip(INFO.children.textTemperature, "UI_AllInfo_fish_tip_Temperature")
attachTip(INFO.children.textWeather, "UI_AllInfo_fish_tip_Weather")
attachTip(INFO.children.textWind, "UI_AllInfo_fish_tip_Wind")

-- The vanilla rows -----------------------------------------------------------

-- Green when good, red when bad, plain white in between: three states out of
-- AllInfo.color's two, so a middling figure does not read as a problem. Each
-- caller states its own thresholds, since "more is better" flips row to row.
local function tone(node, good, bad)
    if good then
        local c = AllInfo.color(true)
        node:setColor(c.r, c.g, c.b, 1)
    elseif bad then
        local c = AllInfo.color(false)
        node:setColor(c.r, c.g, c.b, 1)
    else
        node:setColor(1, 1, 1, 1)
    end
end

-- "x1.2" next to whatever vanilla just wrote. Its update() runs every frame and
-- rewrites the four labels from scratch, so this appends to the text it left
-- behind instead of composing our own: colour, wording and translation stay
-- vanilla's, and a future patch that changes them changes ours too.
local function suffix(node, coeff)
    if not node.text or node.text == "" then return end
    node:setText(node.text .. "  (x" .. AllInfo.num(coeff, 2) .. ")")
end

-- A row vanilla left as "Unknown" because of the level gate. Rewrites the whole
-- label, since there is no vanilla text worth keeping there. Three states like
-- tone(): a x1 is neither good nor bad, and painting it green said the weather
-- was helping when it was only not hurting.
local function reveal(node, label, state, coeff, good, bad)
    tone(node, good, bad)
    node:setText(getText(label) .. ": " .. state .. "  (x" .. AllInfo.num(coeff, 2) .. ")")
end

-- Everything that must survive a re-execution lives in AllInfo.Fishing, never in
-- a local: with debug mode on, deploying while the game is open runs this file
-- again and a second pass would chain a wrapper onto our own.
if not F.hookedUpdate then
    local baseUpdate = INFO.update

    INFO.update = function(self)
        baseUpdate(self)

        local player = self.player or getPlayer()
        if not player then return end

        local ok, err = pcall(F.decorate, self, player)
        if not ok then
            print("[AllInfo] fishing panel disabled: " .. tostring(err))
            F.decorate = function() end
        end
    end

    F.hookedUpdate = true
end

function F.decorate(self, player)
    local p = F.params(player)
    if not p then return end

    local level = p.level
    local c = self.children

    -- Time. Vanilla shows it from Fishing 2.
    if not AllInfo.enabled("FishTime") then       -- vanilla's row, untouched
    elseif F.vanillaShows(level, GATE.time) then
        suffix(c.textTime, p.time.coeff)
    elseif F.mayReveal() then
        reveal(c.textTime, "Sandbox_TimeOptions",
            getText(p.time.coeff > 1 and "IGUI_health_Good" or "Sandbox_Normal"),
            p.time.coeff, p.time.coeff > 1, false)
    end

    -- Temperature, with the actual reading. Vanilla never shows the degrees.
    local degrees = "  " .. getText("UI_AllInfo_fish_Degrees",
        AllInfo.num(p.temperature.temperature, 0))
    if not AllInfo.enabled("FishTemp") then
    elseif F.vanillaShows(level, GATE.temperature) then
        suffix(c.textTemperature, p.temperature.coeff)
        c.textTemperature:setText(c.textTemperature.text .. degrees)
    elseif F.mayReveal() then
        local state = getText("IGUI_health_Good")
        if p.temperature.coeff < 1 then state = getText("Sandbox_Normal") end
        if p.temperature.coeff <= 0.5 then state = getText("IGUI_Fishing_BadParam") end
        reveal(c.textTemperature, "IGUI_Temperature", state, p.temperature.coeff,
            p.temperature.coeff >= 1, p.temperature.coeff <= 0.5)
        c.textTemperature:setText(c.textTemperature.text .. degrees)
    end

    -- Weather.
    if not AllInfo.enabled("FishWeather") then
    elseif F.vanillaShows(level, GATE.weather) then
        suffix(c.textWeather, p.weather.coeff)
    elseif F.mayReveal() then
        local state = getText("Sandbox_Normal")
        if p.weather.isFog then state = getText("IGUI_Fishing_BadParam") end
        if p.weather.isRain then state = getText("IGUI_health_Good") end
        reveal(c.textWeather, "IGUI_ClimateControl_Weather", state, p.weather.coeff,
            p.weather.coeff > 1, p.weather.coeff < 1)
    end

    -- Wind. It has no coefficient of its own: over 0.5 it *is* the weather 0.8,
    -- the same one fog sets, and the two never stack. Printed as the share it
    -- takes of the weather coefficient so two rows stop looking like two
    -- separate penalties.
    -- Two states, not three, and that is why the row is rewritten even when
    -- vanilla is already showing it: wind is either under the threshold and
    -- free, or over it and costs the x0.8. Vanilla writes "Normal" for the free
    -- half, which reads like a middle step that does not exist.
    local windCoeff = p.wind >= 0.5 and 0.8 or 1
    if AllInfo.enabled("FishWind")
        and (F.vanillaShows(level, GATE.wind) or F.mayReveal()) then
        reveal(c.textWind, "IGUI_Fishing_Wind",
            getText(windCoeff < 1 and "IGUI_Fishing_BadParam" or "IGUI_health_Good"),
            windCoeff, windCoeff >= 1, windCoeff < 1)
        c.textWind:setText(c.textWind.text .. "  " .. AllInfo.pct(p.wind, 0))
    end

    -- The six cells AllInfo adds. Each one is filled only when its data is
    -- knowable; an unknown square leaves the bottom four empty rather than
    -- printing a figure that is not true here.
    --
    -- Nothing is drawn clipped: a UI.Text overflows its width, so a long cell
    -- paints over the next column. Every cell stays short and the detail goes
    -- in its tooltip.
    if not c.allInfoHook then return end

    local function cell(node, opt, text)
        node:setText(AllInfo.enabled(opt) and text or "")
    end

    -- Fog gets its own cell because it is half of what vanilla lumps into
    -- Weather: fog over 40% and wind over 50% set the same x0.8, and vanilla's
    -- Weather row reports neither -- it says "Good" for rain while a gale is
    -- blowing. Same gate as Weather, since it is the same reading, and the same
    -- two states as wind.
    local fogCoeff = p.fog >= 0.4 and 0.8 or 1
    if F.vanillaShows(level, GATE.weather) or F.mayReveal() then
        cell(c.allInfoFog, "FishFog", getText("IGUI_climate_Fog") .. ": "
            .. getText(fogCoeff < 1 and "IGUI_Fishing_BadParam" or "IGUI_health_Good")
            .. "  (x" .. AllInfo.num(fogCoeff, 2) .. ")  " .. AllInfo.pct(p.fog, 0))
        tone(c.allInfoFog, fogCoeff >= 1, fogCoeff < 1)
    else
        c.allInfoFog:setText("")
    end

    local hookName = getText("UI_AllInfo_fish_NoHook")
    if p.hook.hook then hookName = getItemNameFromFullType(p.hook.hook) end
    cell(c.allInfoHook, "FishHook", getText("UI_AllInfo_fish_Hook") .. ": " .. hookName
        .. "  (x" .. AllInfo.num(p.hook.coeff, 2) .. ")")
    tone(c.allInfoHook, p.hook.coeff > 1, p.hook.coeff < 1)

    -- With the gate on, bite chance and waiting time are held back until the
    -- level at which vanilla itself reveals the last of the four factors they
    -- are made of. Hook, trash and fish count have no vanilla equivalent.
    local hideDerived = not F.mayReveal() and not F.vanillaShows(level, GATE.wind)

    if p.noFish then
        cell(c.allInfoFish, "FishCount", getText("UI_AllInfo_fish_Fish") .. ": "
            .. getText("UI_AllInfo_fish_NoFishZone"))
        tone(c.allInfoFish, false, true)
        c.allInfoTrash:setText("")
        c.allInfoBite:setText("")
        c.allInfoWait:setText("")
        return
    end

    if not p.fish then
        c.allInfoFish:setText("")
        c.allInfoTrash:setText("")
        c.allInfoBite:setText("")
        c.allInfoWait:setText("")
        return
    end

    cell(c.allInfoTrash, "FishTrash", getText("UI_AllInfo_fish_Trash") .. ": "
        .. AllInfo.pct(p.trash or 0, 0))
    tone(c.allInfoTrash, (p.trash or 0) <= 0.25, (p.trash or 0) >= 0.5)

    cell(c.allInfoFish, "FishCount", getText("UI_AllInfo_fish_Fish") .. ": "
        .. AllInfo.num(p.fish.value, 0)
        .. "  (x" .. AllInfo.num(p.fish.coeff, 2) .. ")")
    tone(c.allInfoFish, p.fish.coeff > 1, p.fish.coeff < 1)

    if hideDerived then
        c.allInfoBite:setText("")
        c.allInfoWait:setText("")
        return
    end

    -- 0.8 is the ceiling before any bonus, so 60% is genuinely good and only a
    -- third or less is worth painting red.
    cell(c.allInfoBite, "FishBite", getText("UI_AllInfo_fish_Bite") .. ": "
        .. AllInfo.pct(p.bite, 0))
    tone(c.allInfoBite, p.bite >= 0.6, p.bite < 0.35)

    local wait = p.wait <= 1 and getText("UI_AllInfo_fish_Best")
        or "x" .. AllInfo.num(p.wait, 1)
    cell(c.allInfoWait, "FishWait", getText("UI_AllInfo_fish_Wait") .. ": " .. wait)
    tone(c.allInfoWait, p.wait <= 1, p.wait >= 2)
end

-- The new rows --------------------------------------------------------------

-- ponytail: vanilla's layout is hardcoded here -- header rows at y=17 and y=34,
-- separator at y=52, species from y=60 in steps of 25, second column at x=220.
-- Ours go at y=51, 68 and 85, so everything below moves down by three rows.
-- A patch that moves vanilla's rows needs these numbers updated.
local SHIFT = 51
local ROW_H = 17
local COL_LEFT, COL_RIGHT = 30, 240

-- width is set on purpose, same reason as attachTip. The tooltip callback is
-- passed in at creation time so UI._addChild registers the mouse hook for us.
-- The six cells we add ourselves. init() makes the window taller for them,
-- so it has to know whether a single one of them is still wanted.
local CELLS = { "FishHook", "FishTrash", "FishCount", "FishFog", "FishBite", "FishWait" }

function F.anyCell()
    for i = 1, #CELLS do
        if AllInfo.enabled(CELLS[i]) then return true end
    end
    return false
end

local function newText(y, x, tipKey)
    return PZAPI.UI.Text{
        x = x, y = y,
        width = 190, height = ROW_H,
        scaleX = 0.4, scaleY = 0.4,
        pivotY = 0.5,
        text = "",
        onHover = function(self, state)
            if state then
                F.showTooltip(self, getText(tipKey))
            else
                F.hideTooltip(self)
            end
        end
    }
end

if not F.hookedInit then
    local baseInit = INFO.init

    INFO.init = function(self)
        baseInit(self)

        if not F.anyCell() then return end

        local ok, err = pcall(F.build, self)
        if not ok then
            print("[AllInfo] fishing rows disabled: " .. tostring(err))
            F.build = function() end
        end
    end

    F.hookedInit = true
end

function F.build(self)
    -- Everything vanilla drew below the header moves down. The species rows are
    -- keyed by item type, so they are found through the same table vanilla
    -- filled in its own init.
    self.children.line:setY(self.children.line.y + SHIFT)

    for _, cfg in ipairs(Fishing.fishes) do
        local row = self.children[cfg.itemType]
        if row then
            row:setY(row.y + SHIFT)

            -- Vanilla's own hover shows a flavour description, and only from
            -- Fishing 6 and once you have caught that species. Ours replaces it
            -- unless the gate is on. No Extensions.Mouse call is needed here:
            -- fishItemUI already ships an onHover, so the dispatcher exists and
            -- reads self.onHover on every call.
            local baseHover = row.onHover
            local itemType = cfg.itemType
            row.onHover = function(node, state)
                if AllInfo.enabled("FishingGate") then return baseHover(node, state) end

                if state then
                    F.showTooltip(node, F.speciesBlock(itemType, getPlayer()))
                else
                    F.hideTooltip(node)
                end
            end
        end
    end

    self.children.allInfoHook = newText(51, COL_LEFT, "UI_AllInfo_fish_tip_Hook")
    self.children.allInfoTrash = newText(68, COL_LEFT, "UI_AllInfo_fish_tip_Trash")
    self.children.allInfoFish = newText(85, COL_LEFT, "UI_AllInfo_fish_tip_Fish")
    self.children.allInfoFog = newText(51, COL_RIGHT, "UI_AllInfo_fish_tip_Fog")
    self.children.allInfoBite = newText(68, COL_RIGHT, "UI_AllInfo_fish_tip_Bite")
    self.children.allInfoWait = newText(85, COL_RIGHT, "UI_AllInfo_fish_tip_Wait")

    PZAPI.UI._addChild(self, self.children.allInfoHook)
    PZAPI.UI._addChild(self, self.children.allInfoTrash)
    PZAPI.UI._addChild(self, self.children.allInfoFish)
    PZAPI.UI._addChild(self, self.children.allInfoFog)
    PZAPI.UI._addChild(self, self.children.allInfoBite)
    PZAPI.UI._addChild(self, self.children.allInfoWait)

    -- The window sized itself for vanilla's rows in the init we just called.
    local win = self.parent.parent.parent
    win:setHeight(win.height + SHIFT)
end

-- Species --------------------------------------------------------------------

local function configFor(itemType)
    for _, cfg in ipairs(Fishing.fishes) do
        if cfg.itemType == itemType then return cfg end
    end
    return nil
end

-- The three baits with the highest coefficient for this species, one per line
-- and indented: a single comma-separated line was the hardest part to read.
local function bestBaits(cfg)
    local sorted = {}
    for item, weight in pairs(cfg.lure) do
        if weight and weight > 0 then sorted[#sorted + 1] = { item = item, weight = weight } end
    end
    table.sort(sorted, function(a, b)
        if a.weight == b.weight then return a.item < b.item end
        return a.weight > b.weight
    end)

    local names = {}
    for i = 1, math.min(#sorted, 3) do
        names[#names + 1] = "    " .. getItemNameFromFullType(sorted[i].item)
    end
    if #names == 0 then return nil end
    return names
end

-- Facts only, one per line. Newline, not "<br>": AtomUIText treats char 10 as a
-- real line break (it resets x and adds getLineHeight(), verified in the
-- bytecode), while "<br>" is a Translator convention and this text never goes
-- through Translator, so it would print literally.
--
-- No river/lake line: every species in B42.20 is setLocation(true, true), so it
-- would be the same sentence 21 times.
function F.speciesBlock(itemType, player)
    local cfg = configFor(itemType)
    if not cfg then return nil end

    local p = player and F.params(player) or nil
    local lines = { getItemNameFromFullType(itemType), "" }

    local lvl = F.minLevel(cfg)
    if lvl and AllInfo.enabled("FishMinLevel") then
        lines[#lines + 1] = getText("UI_AllInfo_fish_MinLevel", lvl)
    end

    -- Size is a range, not a ceiling: initFishSizeData spreads lengths from
    -- minLength to maxLength and weights from 0.1 kg up, capped at 45 lb.
    if cfg.minLength and cfg.maxLength and cfg.maxWeight and AllInfo.enabled("FishSize") then
        lines[#lines + 1] = getText("UI_AllInfo_fish_Size",
            AllInfo.num(cfg.minLength, 0), AllInfo.num(cfg.maxLength, 0),
            AllInfo.num(math.min(0.1, cfg.maxWeight), 2),
            AllInfo.num(math.min(cfg.maxWeight, WEIGHT_CAP), 1))
    end

    -- A catch is marked as a trophy once it beats the species maximum, which is
    -- only possible on the 1-in-20 roll a Fishing 8 character gets on a big
    -- fish. trophyLength / trophyWeight are how far that roll can push it.
    if cfg.trophyLength and cfg.maxLength and cfg.maxWeight
        and AllInfo.enabled("FishTrophy") then
        lines[#lines + 1] = getText("UI_AllInfo_fish_Trophy",
            AllInfo.num(cfg.maxLength, 0), AllInfo.num(cfg.maxWeight, 1))
    end

    -- Odds only mean something once bait and water are known.
    if p and p.lure and p.isRiver ~= nil and AllInfo.enabled("FishOdds") then
        local odds = F.speciesOdds(p.lure, p.isRiver, p.level)
        local pct = cfg.isPredator and odds.reel[itemType] or odds.base[itemType]
        if pct then
            lines[#lines + 1] = getText("UI_AllInfo_fish_Odds", AllInfo.num(pct, 1))
        else
            lines[#lines + 1] = getText("UI_AllInfo_fish_NoOdds")
        end
    end

    local baits = AllInfo.enabled("FishBaits") and bestBaits(cfg)
    if baits then
        lines[#lines + 1] = getText("UI_AllInfo_fish_Baits")
        for i = 1, #baits do lines[#lines + 1] = baits[i] end
    end

    -- Last, and only when it applies: it changes whether the fish bites at all.
    if cfg.isPredator and AllInfo.enabled("FishPredator") then
        lines[#lines + 1] = ""
        lines[#lines + 1] = getText("UI_AllInfo_fish_Predator")
    end

    return table.concat(lines, "\n")
end
