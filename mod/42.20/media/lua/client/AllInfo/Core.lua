-- AllInfo core: provider registry, cache, formatting helpers and colors.
-- Hard rule: this layer never knows what an item is, and providers never draw.

AllInfo = AllInfo or {}
AllInfo.providers = AllInfo.providers or {}

local CACHE_MS = 500

-- Registry -----------------------------------------------------------------

-- fn(out, item, chr) fills `out` through AllInfo.addRow. It must not draw.
function AllInfo.register(id, order, optionId, fn)
    for i = 1, #AllInfo.providers do
        if AllInfo.providers[i].id == id then return end   -- file re-executed
    end
    AllInfo.providers[#AllInfo.providers + 1] = {
        id = id, order = order or 100, optionId = optionId, fn = fn,
    }
    table.sort(AllInfo.providers, function(a, b) return a.order < b.order end)
end

-- Reads the individual toggle straight from PZAPI, which owns loading and
-- saving and is therefore the only source of truth for the value. Section
-- masters are a write shortcut and are never consulted here. An unknown option
-- means "on": Options.lua may not have loaded, and a provider must never
-- disappear because of that.
function AllInfo.enabled(optionId)
    if not optionId then return true end

    local dict = PZAPI and PZAPI.ModOptions and PZAPI.ModOptions.Dict
    local opts = dict and dict["AllInfo"]
    if not opts then return true end

    local o = opts.dict[optionId]
    if not o then return true end
    return o.value == true
end

-- Vanilla sandbox var (SandboxVars.FoodRotSpeed, ...), nil in the main menu.
function AllInfo.gameSandbox(id, default)
    local v = SandboxVars and SandboxVars[id]
    if v == nil then return default end
    return v
end

-- Rows ---------------------------------------------------------------------

function AllInfo.addRow(out, label, value, color, delta, deltaColor)
    out[#out + 1] = {
        label = label or "",
        value = value ~= nil and tostring(value) or "",
        color = color,
        delta = delta,
        deltaColor = deltaColor,
    }
end

-- addRow with a switch in front of it. The row is what the player sees, so the
-- row is the unit they get to turn off: every per-line toggle in the options tab
-- lands here. An unknown id means "on", same as AllInfo.enabled(), so a provider
-- never disappears because its option failed to register.
--
-- The lookup is a table index per row and rows are cached for CACHE_MS, so this
-- costs nothing worth measuring next to the getters it guards.
function AllInfo.rowIf(out, optionId, label, value, color, delta, deltaColor)
    if not AllInfo.enabled(optionId) then return end
    AllInfo.addRow(out, label, value, color, delta, deltaColor)
end

local cacheItem, cacheChr, cacheHeld, cacheTime, cacheRows

function AllInfo.rows(item, chr)
    -- ISToolTipInv is not item-only: ISFluidBar:activateToolTip() builds one over
    -- a FluidContainer component (or a ResourceFluid), which is what the water
    -- barrel transfer panel puts under the cursor. Providers only speak
    -- InventoryItem, so Ammo called getAmmoType() on a component and threw. The
    -- guard lives here, where every caller routes through, not per provider.
    if not item or not instanceof(item, "InventoryItem") then return nil end

    -- What the character holds is an input to every delta, so it belongs in
    -- the key: swapping weapons with the cursor parked on another item must
    -- not keep serving a comparison against the old one for up to CACHE_MS.
    local held = chr and chr:getPrimaryHandItem() or nil

    local now = getTimestampMs()
    if cacheRows and cacheItem == item and cacheChr == chr and cacheHeld == held
        and (now - cacheTime) < CACHE_MS then
        return cacheRows
    end

    local out = {}
    for i = 1, #AllInfo.providers do
        local p = AllInfo.providers[i]
        if AllInfo.enabled(p.optionId) then
            -- Providers fill a scratch table: a provider that throws halfway
            -- must not leave half of its rows behind.
            local scratch = {}
            local ok, err = pcall(p.fn, scratch, item, chr)
            if ok then
                for j = 1, #scratch do out[#out + 1] = scratch[j] end
            elseif not p.reported then
                -- The failure is per *item*, so it is skipped per item too. This
                -- used to switch the provider off for the whole session, which
                -- turned one odd modded item into "the numbers are gone and the
                -- option is still ticked" -- silent, and only a restart fixed it.
                -- Reported once so a hover that keeps failing does not flood the
                -- log, and with the fullType so the next report is actionable.
                --
                -- The reporter must not be able to throw, and this one did: a
                -- FluidContainer reached rows(), a provider failed on it, and
                -- then this line asked the component for a getFullType() it does
                -- not have. One bad hover, two stack dumps in the player's log --
                -- and a pcall around it would not have helped, because Kahlua
                -- prints the trace even when the error is caught. Asking first is
                -- what stops it. instanceof never throws, getFullType is declared
                -- String so it cannot come back as something unconcatenable, and
                -- tostring() works on anything, so the worst case is a vaguer
                -- name in the log rather than a second error on top of the first.
                p.reported = true
                local id = instanceof(item, "InventoryItem") and item:getFullType()
                    or tostring(item)
                print("[AllInfo] provider '" .. p.id .. "' failed on "
                    .. id .. ": " .. tostring(err))
            end
        end
    end

    cacheItem, cacheChr, cacheHeld, cacheTime, cacheRows = item, chr, held, now, out
    return out
end

-- Throws the cached list away. The cache key is the item and the character, so
-- anything that changes what a provider would *answer* about the same item is
-- invisible to it: applying the options screen, and the SelfTest sweeping every
-- switch. Both call this, and it is the only reason that sweep means anything.
function AllInfo.flushRows()
    cacheRows = nil
end

-- Prototypes ---------------------------------------------------------------

-- Cached throwaway item used by the crafting UI, which only has a fullType.
-- Never added to a container.
local protoCache = {}

function AllInfo.proto(fullType)
    if not fullType then return nil end

    local cached = protoCache[fullType]
    if cached ~= nil then
        if cached == false then return nil end
        return cached
    end

    -- instanceItem() is the global the game itself uses. InventoryItemFactory
    -- is not exposed to Lua at all, despite what the plan said.
    local ok, item = pcall(instanceItem, fullType)
    if not ok or not item then
        protoCache[fullType] = false   -- remember the failure, don't retry per frame
        return nil
    end

    protoCache[fullType] = item
    return item
end

-- Formatting ---------------------------------------------------------------
-- No string.format on dynamic text: a '%' in an item name breaks it since
-- 42.20.1. Lua's tostring() uses %.14g, so a rounded 2.0 already prints "2".

function AllInfo.round(n, dec)
    local m = 10 ^ (dec or 0)
    return math.floor(n * m + 0.5) / m
end

function AllInfo.num(n, dec)
    if type(n) ~= "number" or n ~= n then return "" end   -- nil / NaN
    return tostring(AllInfo.round(n, dec))
end

function AllInfo.pct(n, dec)
    return AllInfo.num(n * 100, dec) .. "%"
end

function AllInfo.signed(n, dec)
    local v = AllInfo.round(n, dec)
    if v > 0 then return "+" .. tostring(v) end
    return tostring(v)
end

-- Reuses vanilla's IGUI_Gametime_* keys, so this is translated in all 29
-- languages for free. Returns nil for junk input; callers skip the row.
-- How many rotting corpses are close enough to be making you ill, or nil when
-- the count cannot be worked out.
--
-- CorpseCount is not exposed to Lua, so the number is read back out of the game
-- rather than recomputed: GetBaseCorpseSickness() is zero at five corpses or
-- fewer and linear in the count above that, and getSicknessFromCorpsesRate(6)
-- gives the size of one step, so one call inverts it. Reading it back beats
-- copying the curve, which is the sandbox-dependent part.
--
-- Returns 0, not nil, below the threshold: "there are corpses but not enough to
-- matter yet" is an answer, and callers want to tell it apart from "no idea".
-- The pcall guards the static call the same way Mask.lua always did.
function AllInfo.corpseCount(chr)
    if not chr then return nil end

    local body = chr:getBodyDamage()
    local base = body and body:GetBaseCorpseSickness()
    if not base then return nil end
    if base <= 0 then return 0 end

    local ok, unit = pcall(function() return BodyDamage.getSicknessFromCorpsesRate(6) end)
    if not ok or type(unit) ~= "number" or unit <= 0 then return nil end

    return base / unit + 5
end

function AllInfo.duration(minutes)
    if type(minutes) ~= "number" or minutes ~= minutes or minutes < 0 then return nil end
    if minutes == math.huge then return nil end

    local days = math.floor(minutes / 1440)
    local hours = math.floor((minutes - days * 1440) / 60)
    local mins = math.floor(minutes - days * 1440 - hours * 60)

    local parts = {}
    if days > 0 then
        parts[#parts + 1] = days .. " " .. getText(days == 1 and "IGUI_Gametime_day" or "IGUI_Gametime_days")
    end
    if hours > 0 then
        parts[#parts + 1] = hours .. " " .. getText(hours == 1 and "IGUI_Gametime_hour" or "IGUI_Gametime_hours")
    end
    -- Minutes are noise next to days.
    if mins > 0 and days == 0 then
        parts[#parts + 1] = mins .. " " .. getText(mins == 1 and "IGUI_Gametime_minute" or "IGUI_Gametime_minutes")
    end

    if #parts == 0 then return "< 1 " .. getText("IGUI_Gametime_minute") end
    return table.concat(parts, " ")
end

-- Colors -------------------------------------------------------------------

function AllInfo.color(good)
    local c = good and getCore():getGoodHighlitedColor() or getCore():getBadHighlitedColor()
    return { r = c:getR(), g = c:getG(), b = c:getB() }
end

-- Weapon condition loss ----------------------------------------------------

-- Mirrors IsoGameCharacter.getWeaponLevel(HandWeapon) for a weapon that is
-- *not* in your hands, which the Java method cannot answer: it ignores its
-- argument entirely, running all six isOfWeaponCategory() checks against
-- getPrimaryHandItem(). Asking it about an axe on the floor reports the skill
-- of the bat you are holding, so item:getMaintenanceMod(false, chr) is only
-- correct for the equipped item.
--
-- Verified in the B42.20 bytecode, quirks reproduced on purpose because this
-- has to predict what the game will really roll once you equip the thing: the
-- total starts at -1, AXE assigns while every other category adds (so any
-- non-axe weapon comes out one level short), the result is capped at 10, and
-- -1 means 0. SelfTest cross-checks it against Java on the equipped weapon.
function AllInfo.weaponLevel(w, chr)
    local level = -1
    if w:isOfWeaponCategory(WeaponCategory.AXE) then level = chr:getPerkLevel(Perks.Axe) end
    if w:isOfWeaponCategory(WeaponCategory.SPEAR) then level = level + chr:getPerkLevel(Perks.Spear) end
    if w:isOfWeaponCategory(WeaponCategory.SMALL_BLADE) then level = level + chr:getPerkLevel(Perks.SmallBlade) end
    if w:isOfWeaponCategory(WeaponCategory.LONG_BLADE) then level = level + chr:getPerkLevel(Perks.LongBlade) end
    if w:isOfWeaponCategory(WeaponCategory.BLUNT) then level = level + chr:getPerkLevel(Perks.Blunt) end
    if w:isOfWeaponCategory(WeaponCategory.SMALL_BLUNT) then level = level + chr:getPerkLevel(Perks.SmallBlunt) end

    if level > 10 then level = 10 end
    if level == -1 then return 0 end
    return level
end

-- Odds of a weapon losing a condition point on a hit. InventoryItem
-- .damageCheck() rolls Rand.NextBool(getConditionLowerChance() + maintenance
-- mod), which is a 1-in-N roll, so the answer is 1/N. The maintenance mod is
-- Maintenance + weaponLevel/2 with Java's truncating integer division.
-- nil when N <= 0: that is not a valid roll, and never a divide by zero.
local function rollOdds(base, w, chr)
    local n = base
    if chr then
        n = n + chr:getPerkLevel(Perks.Maintenance) + math.floor(AllInfo.weaponLevel(w, chr) / 2)
    end

    n = math.floor(n)
    if n <= 0 then return nil end
    return 1 / n
end

function AllInfo.conditionLoss(w, chr)
    return rollOdds(w:getConditionLowerChance(), w, chr)
end

-- Swings this weapon has left before it breaks, which is the one figure that
-- compares a hammer with a bat.
--
-- Only the handle breaks a weapon: InventoryItem.setCondition() sets
-- broken = condition <= 0 and nothing anywhere looks at headCondition for that.
-- A head that runs out does not end the weapon, it caps the sharpness (see
-- MeleeWeapon.lua), and when the handle finally goes the OnBreak script hands
-- the head back as a separate item.
--
-- Expected value of a 1-in-N roll repeated until `condition` points are gone,
-- so it moves with Maintenance and with the weapon's own skill. nil when there
-- is no valid roll, which is the same case conditionLoss already refuses.
function AllInfo.hitsToBreak(w, chr)
    local loss = AllInfo.conditionLoss(w, chr)
    if not loss or loss <= 0 then return nil end
    return w:getCondition() / loss
end

-- What a critical really multiplies by. Not the script number:
-- IsoGameCharacter.processHitDamage() rolls
-- Math.max(2, getCriticalDamageMultiplier()), so 2 is a floor and the fifteen
-- vanilla weapons carrying a 1.0 (plus the griddle pan's 1.7) all crit for
-- double. getCriticalDamageMultiplier() on the item and not critDmgMultiplier
-- on the script: the script field is public but instance fields do not reach
-- Lua (see the padLeft trap), and the item's copy is the one accessories can
-- have changed.
function AllInfo.criticalDamage(w)
    local mult = w:getCriticalDamageMultiplier()
    if type(mult) ~= "number" or mult < 2 then return 2 end
    return mult
end

-- The same roll for the head of a tool weapon, and it is a second, independent
-- one: damageCheck() calls headConditionCheck() before its own roll, so a hit
-- can wear the handle, the head, both or neither.
--
-- getHeadConditionLowerChance() is already (int)(getConditionLowerChance() *
-- HeadConditionLowerChanceMultiplier), and that multiplier is 1.0, 1.5 or 2.0
-- on all but one vanilla weapon, so the head almost always outlasts the handle.
-- Maintenance counts here too: damageCheck folds the maintenance mod into the
-- `bonus` it passes on, with useMaintenance false so it is never added twice.
function AllInfo.headConditionLoss(w, chr)
    if not w:hasHeadCondition() then return nil end
    return rollOdds(w:getHeadConditionLowerChance(), w, chr)
end

-- Shared rows ---------------------------------------------------------------
-- Condition and damage are drawn by vanilla as bars with no numbers on them,
-- and the bar cannot be removed: DoTooltipEmbedded is one atomic Java call with
-- no Lua seam. Three providers (MeleeWeapon, Firearm, Clothing) put the exact
-- figures next to it, so the rows live here instead of three times over.

-- Every condition row compares what the two items have **left**, not what they
-- were built with.
--
-- It used to compare maximums on weapons, on the grounds that 32/45 against
-- 8/10 answered no useful question. That reasoning is dead now: "Effective
-- durability" says how many swings each one has in it, which is the comparison
-- of models done properly, so this row is free to answer the other question,
-- which of the two is the less worn right now.
--
-- A tool weapon (hammers, axes, picks, hoes: 57 items in B42.20) carries a
-- second, separate condition for its head, and then what vanilla's own labels
-- call the item's condition is the *handle*. Both keys are vanilla's, so this
-- reads right in the 29 languages the game ships. The head only ever compares
-- against another head: a bat has none, and inventing a zero for it would make
-- every axe look like an upgrade over every bat.
function AllInfo.conditionRow(out, item, other)
    local max = item:getConditionMax()
    if max <= 0 then return end

    local head = item:hasHeadCondition()

    AllInfo.addRow(out,
        getText(head and "Tooltip_weapon_HandleCondition" or "Tooltip_weapon_Condition"),
        item:getCondition() .. " / " .. max,
        nil, AllInfo.delta(item:getCondition(), other and other:getCondition(), true, 0))

    if not head then return end

    local headMax = item:getHeadConditionMax()
    if headMax <= 0 then return end

    local otherHead = other and other:hasHeadCondition() and other:getHeadCondition()
    AllInfo.addRow(out, getText("Tooltip_weapon_HeadCondition"),
        item:getHeadCondition() .. " / " .. headMax,
        nil, AllInfo.delta(item:getHeadCondition(), otherHead, true, 0))
end

-- The damage row shows a range, but a delta is a single number, so it compares
-- the midpoint: that is the damage you actually average per hit.
local function avgDamage(w)
    return (w:getMinDamage() + w:getMaxDamage()) / 2
end

function AllInfo.damageRow(out, w, other)
    local max = w:getMaxDamage()
    if max <= 0 then return end

    AllInfo.addRow(out, getText("Tooltip_weapon_Damage"),
        AllInfo.num(w:getMinDamage(), 2) .. " - " .. AllInfo.num(max, 2),
        nil, AllInfo.delta(avgDamage(w), other and avgDamage(other), true, 2))
end

-- Deltas against the equipped item -----------------------------------------

-- What to compare against: whatever the character holds, unless that already
-- is the hovered item. nil switches every delta off downstream, which is also
-- how the ShowDeltas toggle is honoured -- once, here.
-- isPrimaryHandItem() is an identity compare inside Java (if_acmpne) with its
-- own null guard, so it beats an == between two Lua-wrapped Java objects.
function AllInfo.compareTo(item, chr)
    if not chr or not AllInfo.enabled("ShowDeltas") then return nil end
    if chr:isPrimaryHandItem(item) then return nil end
    return chr:getPrimaryHandItem()
end

-- Returns "(+0.35)" and its color, or nothing when there is no honest
-- comparison to make. Designed to be spliced into the tail of addRow():
--     AllInfo.addRow(out, label, value, nil, AllInfo.delta(a, b, true, 2))
-- It must be the last argument: `and`/`or` truncate to a single value in Lua,
-- so `other and AllInfo.delta(...)` would silently drop the color. Pass a nil
-- `old` instead -- that is what makes `other and other:getX()` work inline.
-- The clothing counterpart of compareTo: the piece this one would replace, or
-- nil when there is nothing to compare against and every row stays white.
--
-- getWornItem() alone is not enough: body locations are *exclusive*, not
-- identical. A shirt sits in SHIRT and a t-shirt in TSHIRT and the two cannot be
-- worn together, so asking for TSHIRT while wearing a shirt answers nil and the
-- comparison silently disappears -- which is exactly what happened once already.
-- BodyLocationGroup knows which slots exclude which, so the fallback walks the
-- worn items and asks it.
function AllInfo.replacedClothing(item, chr)
    if not chr or not AllInfo.enabled("ShowDeltas") then return nil end
    -- isEquippedClothing() is an identity check inside Java with its own null
    -- guard, so it beats an == between two Lua-wrapped Java objects.
    if chr:isEquippedClothing(item) then return nil end

    local where = item:getBodyLocation()
    if not where then return nil end

    local function asClothing(c)
        return c and instanceof(c, "Clothing") and c or nil
    end

    local direct = chr:getWornItem(where)
    if direct then return asClothing(direct) end

    local group = chr:getBodyLocationGroup()
    local slot = group and group:getLocation(where)
    local worn = chr:getWornItems()
    if not slot or not worn then return nil end

    for i = 0, worn:size() - 1 do
        local entry = worn:get(i)
        local location = entry and entry:getLocation()
        if location and slot:isExclusive(location) then return asClothing(entry:getItem()) end
    end
    return nil
end

function AllInfo.delta(new, old, higherIsBetter, dec, suffix)
    if type(new) ~= "number" or type(old) ~= "number" then return nil end

    local d = AllInfo.round(new - old, dec)
    if d ~= d or d == 0 then return nil end   -- NaN, or nothing at this precision

    return "(" .. AllInfo.signed(d, dec) .. (suffix or "") .. ")",
           AllInfo.color((d > 0) == higherIsBetter)
end

-- Same, for rows whose value is a 0..1 ratio printed with AllInfo.pct().
function AllInfo.deltaPct(new, old, higherIsBetter, dec)
    if type(new) ~= "number" or type(old) ~= "number" then return nil end
    return AllInfo.delta(new * 100, old * 100, higherIsBetter, dec, "%")
end
