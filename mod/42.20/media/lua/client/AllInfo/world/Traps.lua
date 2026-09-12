require "AllInfo/Core"
require "ISUI/ISCollapsableWindow"
require "ISUI/ISLayoutManager"

AllInfo.Traps = AllInfo.Traps or {}

-- Right-click a placed trap -> its own submenu -> "Info", which opens a window.
-- Clicked, not hovered, and inside vanilla's submenu next to "Dismantle trap",
-- because that is where a player looking for trap information goes.
--
-- The trapping system carries a full probability table per animal, trap, bait,
-- zone and hour of the day, all of it plain Lua in media/lua/server/Traps/, and
-- the game shows exactly none of it. You put down a cage with a carrot and wait
-- without knowing whether any of that was the right call.
--
-- Everything below is read off TrapAnimals and the trap's own mod data, so a
-- mod that adds an animal or a trap is picked up for free: the tables are
-- walked, never copied.
--
-- Two things vanilla defines and never uses, so they are not shown: the
-- animal's `strength`, which was meant to be the hours before it breaks out and
-- is read by nobody in B42.20 -- the animal never escapes -- and `animalHour`.

local INFO_ICON = "media/ui/inventoryPanes/Button_Info.png"
local FONT = UIFont.Small
local PAD = 8

-- STrapGlobalObject:testForAnimal runs two independent rolls per animal:
--     ZombRand(100) < traps[type] + baits[bait] + trappingSkill * 1.5
--     ZombRand(100) < zone[zoneType] + trappingSkill * 1.5
-- Both have to pass, plus the hour window and the bait still being fresh. Every
-- animal that clears all of it goes into a list and *one* is drawn from it, so
-- this is the chance of entering that draw, not of ending up in the trap. The
-- label says so and nothing is multiplied underneath, which would be inventing.
local function roll(value, skill)
    local chance = value + skill * 1.5
    if chance > 100 then chance = 100 end
    if chance < 0 then chance = 0 end
    return chance / 100
end

local function twoDigits(n)
    return (n < 10 and "0" or "") .. n
end

-- checkTime() reads minHour == maxHour as "any hour", so those animals have no
-- window at all rather than a zero-length one.
local function window(animal)
    if animal.minHour == animal.maxHour then return nil end
    return twoDigits(animal.minHour) .. ":00 - " .. twoDigits(animal.maxHour) .. ":00"
end

-- The animal's own name, not the item it drops. Naming them by the drop is what
-- put two "Dead Rabbit" rows in the same window: **the raccoon hands you a
-- rabbit corpse** in B42.20, `raccoon.item = "Base.DeadRabbit"` with a
-- "TODO RJ: ask for model" next to it. So the item is not a name, it is a
-- placeholder two animals share.
--
-- Five of the six have a vanilla key, which is 29 languages free. The bird is
-- the only one with nothing anywhere, so it gets a key of ours, and the item
-- name stays as the last resort for anything a mod adds.
local ANIMAL_KEY = {
    squirrel = "IGUI_ItemCat_Squirrel",
    bird = "UI_AllInfo_trap_animal_bird",
}

local function animalName(animal)
    local key = ANIMAL_KEY[animal.type] or ("IGUI_Animal_Group_" .. tostring(animal.type))
    local name = getTextOrNull(key)
    if name and name ~= "" then return name end

    local script = animal.item and getScriptManager():getItem(animal.item)
    return script and script:getDisplayName() or animal.type
end

-- Zone names, from vanilla's own foraging search-mode keys. All fifteen
-- trapping zones have one, already translated into the 29 languages the game
-- ships, so this needs no key of ours. A zone a mod adds falls back to its raw
-- type, which is still better than nothing and never a wrong name.
local function zoneName(zoneType)
    if not zoneType then return nil end
    local name = getTextOrNull("IGUI_SearchMode_Zone_Names_" .. tostring(zoneType))
    if name and name ~= "" then return name end
    return tostring(zoneType)
end

-- Best zone rather than the sum. calculTrap walks every zone on the square and
-- rolls each one, so more zones means more chances; quoting the best is the
-- honest floor, and saying "at least this" beats adding probabilities that the
-- game rolls separately.
local function zoneChance(animal, trap, skill)
    local best, name
    local zones = trap.zones
    if type(zones) == "table" then
        for zoneType in pairs(zones) do
            local v = animal.zone[zoneType]
            if v and (not best or v > best) then best, name = v, zoneType end
        end
    end
    if not best and trap.zone then
        local v = animal.zone[trap.zone]
        if v then best, name = v, trap.zone end
    end
    if not best then return nil end
    return roll(best, skill), name
end

local function trapDef(trapType)
    if not Traps then return nil end
    for i = 1, #Traps do
        if Traps[i].type == trapType then return Traps[i] end
    end
end

-- Which animal comes out when one does, and it is not each animal's own
-- chance. checkForAnimal() drops every animal that clears its two rolls into a
-- list and then draws ONE of them, so an animal's real share is its chance
-- weighted by how many rivals got into the same draw that hour.
--
--     P(i drawn) = p_i * integral(0..1) prod_{j ~= i} (1 - p_j + p_j * x) dx
--
-- which is the exact expectation of 1/(1+K), K being the others that passed.
-- Six animals at most in B42.20, so expanding the polynomial is cheaper than
-- explaining an approximation, and the shares add up to the catch chance by
-- construction rather than by luck. SelfTest holds those two against each other.
local function draws(p)
    local out = {}
    for i = 1, #p do
        local poly = { 1 }              -- poly[k + 1] is the coefficient of x^k
        for j = 1, #p do
            if j ~= i then
                local acc = {}
                for k = 1, #poly + 1 do acc[k] = 0 end
                for k = 1, #poly do
                    acc[k] = acc[k] + poly[k] * (1 - p[j])
                    acc[k + 1] = acc[k + 1] + poly[k] * p[j]
                end
                poly = acc
            end
        end

        local integral = 0
        for k = 1, #poly do integral = integral + poly[k] / k end
        out[i] = p[i] * integral
    end
    return out
end

-- One row per animal, under "Possible prey". With no bait there is no value at
-- all, because the trap does not roll without one and a percentage would be
-- fiction. With bait the value is that animal's share of the catch, and the
-- odds of there being a catch at all go on their own line.
--
-- The figures are the same at every hour of the day, and the active-hours line
-- next to them is what says when the trap is rolling at all: checkTime() runs
-- before either die, so outside the window every one of these is a flat zero.
-- Folding that into the percentages would hide the reason behind it.
--
-- Returns the zone, the shared hour window, and the chance of catching
-- anything this hour.
local function preyRows(rows, trap, skill)
    if not TrapAnimals then return nil end

    local zone, chances = nil, {}
    for i = 1, #TrapAnimals do
        local animal = TrapAnimals[i]
        local trapChance = animal.traps and animal.traps[trap.trapType]

        if trapChance then
            local baitChance = trap.bait and animal.baits and animal.baits[trap.bait]
            local p

            if baitChance then
                local zoneOdds, foundZone = zoneChance(animal, trap, skill)
                if foundZone then zone = zone or foundZone end
                -- Both rolls have to pass and they are independent, so they
                -- multiply. This is the animal's own chance, before the draw.
                if zoneOdds then p = roll(trapChance + baitChance, skill) * zoneOdds end
            end

            if not trap.bait or baitChance then
                local row = { label = animalName(animal), value = "",
                              indent = true, window = window(animal) }
                rows[#rows + 1] = row
                if p then chances[#chances + 1] = { p = p, row = row } end
            end
        end
    end

    -- The catch chance is "at least one of them passes", which is one minus all
    -- of them failing. Never a sum: two 9% animals are not an 18% trap.
    local catch = nil
    if #chances > 0 then
        local miss = 1
        for i = 1, #chances do miss = miss * (1 - chances[i].p) end
        catch = 1 - miss

        local p = {}
        for i = 1, #chances do p[i] = chances[i].p end
        local drawn = draws(p)

        for i = 1, #chances do
            chances[i].row.value = catch > 0
                and AllInfo.pct(drawn[i] / catch, 0) or ""
        end
    end

    -- Every animal a given trap accepts shares one hour window in B42.20: the
    -- three cage animals are all 19:00-05:00 and the other three are around the
    -- clock. Repeating the same range on every row was noise, so it is lifted
    -- to a line of its own and only stays per animal if they ever disagree.
    --
    -- ponytail: when they do disagree the catch chance is wrong for any given
    -- hour, since it pools animals that are not all awake at once. No vanilla
    -- trap does that, and the per-row windows say so on screen. Split it by
    -- hour the day a mod mixes them.
    local shared, mixed = nil, false
    for i = 1, #rows do
        local w = rows[i].window
        if rows[i].indent then
            if shared == nil then shared = w or false
            elseif shared ~= (w or false) then mixed = true end
        end
    end

    if mixed then
        for i = 1, #rows do
            if rows[i].indent and rows[i].window then
                rows[i].value = rows[i].value ~= ""
                    and (rows[i].value .. "  " .. rows[i].window) or rows[i].window
            end
        end
        return zone, nil, catch
    end

    return zone, shared or nil, catch
end

function AllInfo.Traps.rows(trap)
    local rows = {}
    local function add(opt, key, value, colour)
        if value and AllInfo.enabled(opt) then
            rows[#rows + 1] = { label = getText(key), value = value, color = colour }
        end
    end

    -- Blank rows are what turn a nine-line list into four readable blocks:
    -- what can be caught and when, what is in the trap and where, the condition
    -- of both, what can go wrong per hour, and the one warning.
    local function blank()
        rows[#rows + 1] = { label = "", value = "" }
    end

    local skill = trap.trappingSkill or 0

    if AllInfo.enabled("TrapPrey") then
        rows[#rows + 1] = { label = getText("UI_AllInfo_trap_Prey"), value = "" }
    end
    local zone, hours, catch = preyRows(rows, trap, skill)
    add("TrapHours", "UI_AllInfo_trap_Window_Hours", hours)

    -- The odds of this trap catching anything at all in an hour, which is the
    -- question the per-animal rows do not answer: those are the split of the
    -- catch, this is whether there is one. Two decimals would be noise on a
    -- figure that is already a per-hour rate.
    if catch and catch > 0 then
        add("TrapCatch", "UI_AllInfo_trap_CatchChance",
            getText("UI_AllInfo_trap_PerHour", AllInfo.pct(catch, 1)))
    end
    blank()

    -- Bait, with what is left of it both ways: the share still good, and the
    -- time that share buys. checkBaitFreshness() is
    -- isItemFresh(type, trapBaitDay), i.e. trapBaitDay < DaysFresh, and
    -- STrapSystem.EveryDays walks trapBaitDay up by one a day from whatever age
    -- the item had when it went in. A stale bait keeps sitting there catching
    -- nothing, which is exactly the state worth colouring.
    if trap.bait then
        local script = getScriptManager():getItem(trap.bait)
        local name = script and script:getDisplayName() or trap.bait
        local fresh = script and script:getDaysFresh()
        local stale = false

        if fresh and fresh > 0 and trap.trapBaitDay then
            local left = fresh - trap.trapBaitDay
            local d = left > 0 and AllInfo.duration(left * 1440)
            stale = not d

            name = name .. ", " .. (d and getText("UI_AllInfo_trap_BaitFresh", d)
                or getText("UI_AllInfo_trap_BaitStale"))
        end

        add("TrapBait", "UI_AllInfo_trap_Bait", name, stale and AllInfo.color(false) or nil)
    end

    add("TrapZone", "UI_AllInfo_trap_Zone", zoneName(zone or trap.zone))

    -- Bait condition as a share of its own shelf life, the same figure
    -- isItemFresh() decides on: trapBaitDay against the item's DaysFresh.
    if trap.bait then
        local script = getScriptManager():getItem(trap.bait)
        local fresh = script and script:getDaysFresh()
        if fresh and fresh > 0 and trap.trapBaitDay then
            local share = (fresh - trap.trapBaitDay) / fresh
            if share < 0 then share = 0 end
            add("TrapBaitState", "UI_AllInfo_trap_BaitState", AllInfo.pct(share, 0),
                share <= 0 and AllInfo.color(false) or nil)
        end
    end

    -- What can go wrong in an hour, from checkDestroy():
    --     bait   ZombRand(trapStrength + 10) == 0
    --     trap   ZombRand(40) == 0 and ZombRand(trapStrength) == 0
    -- The trap roll carries an extra `not square`, so it only happens while you
    -- are away, same as the catch itself.
    --
    -- And calculTrap() only calls checkDestroy at all when the trap is empty:
    -- with a catch inside it increments animalAliveHour instead. So neither of
    -- these rows applies to a sprung trap, and showing them there would be
    -- quoting odds the game is not rolling.
    --
    -- There is no trap health row to go with these, on purpose. TrapBO does
    -- build the trap as an IsoThumpable with setMaxHealth(50), but the trapping
    -- system never touches that bar: a trap is not worn down, it is destroyed
    -- outright -- `destroyed = true`, then removeIsoObject() and the debris on
    -- the floor. A bar that only moves when someone physically hits the trap,
    -- sitting next to the odds of it being wrecked, is two different things
    -- wearing the same word, so it is not shown at all.
    local caught = trap.animal and trap.animal.type
    local def = trapDef(trap.trapType)
    local hadRisk = false

    if def and def.trapStrength and def.trapStrength > 0 and not caught then
        if trap.bait then
            add("TrapBaitLoss", "UI_AllInfo_trap_BaitLoss", getText("UI_AllInfo_trap_PerHour",
                AllInfo.pct(1 / (def.trapStrength + 10), 1)))
        end
        add("TrapDestroyed", "UI_AllInfo_trap_Destroyed", getText("UI_AllInfo_trap_PerHour",
            AllInfo.pct(1 / (40 * def.trapStrength), 2)))
        hadRisk = true
    end
    if hadRisk then blank() end

    -- Hours the catch has been sitting there. addAliveAnimal() then simulates
    -- ZombRand(h, h + 15) hours of hunger and thirst in one go, and the animal
    -- can come out already dead.
    if trap.animal and trap.animal.type and trap.animalAliveHour then
        local d = AllInfo.duration(trap.animalAliveHour * 60)
        if d then
            add("TrapInside", "UI_AllInfo_trap_Inside", d)
            if AllInfo.enabled("TrapWarnings") then
                rows[#rows + 1] = { label = getText("UI_AllInfo_trap_InsideWarning"),
                                    value = "", wide = true }
            end
        end
    end

    -- The single most useful thing here, and it is nowhere in the game:
    -- checkForAnimal(square) returns without rolling anything when the square
    -- is loaded. Watching your trap guarantees it catches nothing.
    if AllInfo.enabled("TrapWarnings") then
        rows[#rows + 1] = { label = getText("UI_AllInfo_trap_NearbyWarning"),
                            value = "", wide = true, color = AllInfo.color(false) }
    end

    -- A separator only earns its line if a block landed on each side of it. An
    -- unbaited trap, or one that is not a thumpable, skips whole blocks and
    -- would otherwise leave a gap twice as tall as the others. Collapsing at
    -- the end covers every one of those cases without a flag per block.
    local tidy = {}
    for i = 1, #rows do
        local isBlank = rows[i].label == "" and rows[i].value == "" and not rows[i].wide
        local lastBlank = #tidy > 0 and tidy[#tidy].label == ""
            and tidy[#tidy].value == "" and not tidy[#tidy].wide
        if not isBlank or (#tidy > 0 and not lastBlank) then
            tidy[#tidy + 1] = rows[i]
        end
    end
    while #tidy > 0 and tidy[#tidy].label == "" and tidy[#tidy].value == ""
        and not tidy[#tidy].wide do
        tidy[#tidy] = nil
    end

    return tidy
end

-- The window ------------------------------------------------------------------
-- A plain ISCollapsableWindow that paints the rows, sized to its own content.
-- Same family as vanilla's crop panel, which is where a player has already seen
-- this shape.

AllInfo.TrapWindow = ISCollapsableWindow:derive("AllInfoTrapWindow")

function AllInfo.TrapWindow:render()
    ISCollapsableWindow.render(self)

    local tm = getTextManager()
    local lineHeight = tm:getFontHeight(FONT) + 2
    local y = self:titleBarHeight() + PAD

    for i = 1, #self.rows do
        local row = self.rows[i]
        local c = row.color or { r = 1, g = 1, b = 1 }
        local x = row.indent and (PAD + 12) or PAD

        if row.wide then
            -- One sentence across the whole row: sent through drawTextRight it
            -- ended up hanging off the right edge, out of line with everything.
            self:drawText(row.label, x, y, c.r, c.g, c.b, 1, FONT)
        else
            self:drawText(row.label, x, y, 1, 1, 1, 1, FONT)
            self:drawTextRight(row.value, self.width - PAD, y, c.r, c.g, c.b, 1, FONT)
        end
        y = y + lineHeight
    end
end

-- One window, reused, exactly like ISPlantInfoAction does with the crop panel:
-- it keeps the instance in ISFarmingMenu.info, only swaps the plant, and hands
-- it to ISLayoutManager so the game remembers where the player dragged it. A
-- fresh window per click stacked them up and always reopened in the same corner
-- no matter where you had put the last one.
AllInfo.Traps.window = nil

function AllInfo.Traps.show(trap, name)
    local rows = AllInfo.Traps.rows(trap)

    local tm = getTextManager()
    local lineHeight = tm:getFontHeight(FONT) + 2

    local widest = tm:MeasureStringX(FONT, name) + 40
    for i = 1, #rows do
        local w = tm:MeasureStringX(FONT, rows[i].label)
            + tm:MeasureStringX(FONT, rows[i].value) + 40
        if rows[i].indent then w = w + 12 end
        if w > widest then widest = w end
    end

    local win = AllInfo.Traps.window
    if not win then
        -- ISPlantInfoAction:perform() to the pixel: 70 by 50 in from the top
        -- left of this player's screen.
        local playerNum = getPlayer() and getPlayer():getPlayerNum() or 0
        win = AllInfo.TrapWindow:new(getPlayerScreenLeft(playerNum) + 70,
            getPlayerScreenTop(playerNum) + 50, widest, 240)
        win:setResizable(false)
        win:initialise()
        win:addToUIManager()
        ISLayoutManager.RegisterWindow("allinfo_trap", ISCollapsableWindow, win)
        AllInfo.Traps.window = win
    end

    win.rows = rows
    win.title = name
    win:setWidth(widest)
    win:setHeight(#rows * lineHeight + PAD * 2 + win:titleBarHeight())
    win:setVisible(true)
    win:bringToTop()
    return win
end

-- The menu ---------------------------------------------------------------------

local function trapIn(worldobjects)
    if not CTrapSystem or not CTrapSystem.instance then return nil end
    for i = 1, #worldobjects do
        local obj = worldobjects[i]
        local trap = obj and CTrapSystem.instance:getLuaObjectAt(obj:getX(), obj:getY(), obj:getZ())
        if trap and trap.trapType then return trap end
    end
end

-- Vanilla's own submenu, found by the name it gave the parent option.
-- ISContextMenu:getNew stores each submenu in the root menu's instanceMap under
-- the number it wrote into option.subOption, so this is its own bookkeeping
-- read back rather than a guess about the layout.
local function vanillaSubmenu(context, name)
    local option = context.getOptionFromName and context:getOptionFromName(name)
    if not option or not option.subOption then return nil end
    return context.instanceMap and context.instanceMap[option.subOption]
end

function AllInfo.Traps.build(context, worldobjects, test)
    local trap = trapIn(worldobjects)
    if not trap then return end
    if test then return ISWorldObjectContextMenu.setTest() end

    -- TrapGate mirrors vanilla's own habit of holding information back: it puts
    -- the numbers behind Trapping 3, which is where the crop panel and the
    -- fishing one start talking.
    if AllInfo.enabled("TrapGate") and (trap.trappingSkill or 0) < 3 then return end

    -- The same name ISTrapMenu gave its parent option, so the lookup lands on
    -- vanilla's submenu instead of adding a second one next to it.
    local script = getScriptManager():getItem(trap.trapType)
    local name = script and script:getDisplayName() or getText("ContextMenu_Trap")

    -- Nothing to put in the window means no entry for it.
    if #AllInfo.Traps.rows(trap) == 0 then return end

    local menu = vanillaSubmenu(context, name) or context
    local option = menu:addOption(getText("UI_AllInfo_trap_Window"), worldobjects,
        function() AllInfo.Traps.show(trap, name) end)
    option.iconTexture = getTexture(INFO_ICON):splitIcon()
end

-- Same self-disabling policy as the gas pump: this runs while the right-click
-- menu is being built, so an error here would take the whole menu down.
local function fill(player, context, worldobjects, test)

    local ok, result = pcall(AllInfo.Traps.build, context, worldobjects, test)
    if ok then return result end

    print("[AllInfo] trap menu disabled: " .. tostring(result))
    AllInfo.Traps.build = function() end
end

Events.OnFillWorldObjectContextMenu.Add(fill)

-- Bait side of the same tables, on the item itself: 37 foods are bait for at
-- least one animal, 20 of them for exactly one, and the game never says which.
-- Same idea as the fishing mod's bait rows.
AllInfo.register("Bait", 96, nil, function(out, item, chr)
    if not TrapAnimals then return end
    if not instanceof(item, "Food") then return end

    local fullType = item:getFullType()
    local names = {}
    for i = 1, #TrapAnimals do
        local animal = TrapAnimals[i]
        if animal.baits and animal.baits[fullType] then
            names[#names + 1] = animalName(animal)
        end
    end

    if #names == 0 then return end
    AllInfo.rowIf(out, "TrapAttracts", getText("UI_AllInfo_trap_Attracts"),
        table.concat(names, ", "))
end)
