require "AllInfo/Core"
require "XpSystem/ISUI/ISHealthPanel"

AllInfo.Health = AllInfo.Health or {}

-- Hover a body part in the health panel and this puts the numbers beside the
-- list, in a tooltip of ours. No clicking, no menu entry: vanilla's treatment
-- menu stays exactly as it was, and the information is one cursor move away.
--
-- The health panel is the one place where vanilla has every figure written
-- down and decides not to show it: ISHealthPanel.cheat opens 22 raw numbers in
-- debug only, and doctorLevel opens words, never numbers. ISHealthPanel.cheat
-- is deliberately NOT flipped -- it also opens the debug buttons that *write*
-- to the body (setBleedingTime(10) at ISHealthPanel.lua:198).
--
-- THE CLOCK, and it is exact, not fitted. BodyDamage.Update() calls
-- BodyPart.DamageUpdate() once per frame for all 17 parts, and every wound
-- timer there moves by `constant * GameTime.getMultiplier()`. GameTime.update()
-- advances the day by `multiplier / (120 * minutesPerDay)` hours, so one
-- in-game hour is exactly 120 * minutesPerDay multiplier units. Every duration
-- below is `units / rate / (120 * dayLength)` hours, nothing else.
--
-- THE LAYOUT is three blocks separated by a blank line: how the part is doing,
-- what is wrong with it, what it is wearing. There are no "what you would gain"
-- rows: treating a wound changes its number and its colour on the spot, which
-- says the same thing without a line that reads like data (it did read like
-- data -- ISRichTextPanel trims every line, so indentation is not available).
--
-- COLOUR carries the state, and only on the value:
--   green  treated, or going well
--   red    missing its treatment, or getting worse
--   white  neither -- an opportunity, like a clean bandage about to go dirty
--
-- Fast Healer / Slow Healer are absent on purpose: they only roll the wound's
-- *starting* value (a bite is 50-80 normally, 30-50 fast, 80-150 slow) and
-- never touch a rate, so the trait is already inside every number here.

-- Vanilla's own colours from ISHealthBodyPartListBox:doDrawItem, so the tooltip
-- and the panel behind it speak the same language.
local RED = " <RGB:0.89,0.28,0.28> "
local GREEN = " <RGB:0.28,0.89,0.28> "
local WHITE = " <RGB:1,1,1> "

-- A clean bandage worth less than this is the moment to swap it: change it now
-- and ISApplyBandage hands the bandage back, let it go dirty and it consumes it.
local SWAP_SOON_HOURS = 1

-- Vanilla's own Doctor gates, the `doctorLevel > n` branches of
-- ISHealthBodyPartListBox:doDrawItem, as `>=`. Bleeding and bites are the two
-- vanilla never gates, but it gates every wound *evaluation* at 3 ("a doctor
-- will evaluate the wound"), and a remaining time is an evaluation, so they
-- take the same floor rather than a number of ours.
local GATE = {
    wound = 3,      -- scratch, cut, bleeding, bite: doctorLevel > 2
    deep = 5,       -- deep wound, splint quality, burn cleaning: > 4
    fracture = 7,   -- fracture, stitches: > 6
    infection = 9,  -- wound infection: > 8
}

-- Wound clocks, straight from BodyPart.DamageUpdate. `bare` is the untreated
-- rate, `wrapped` the bandaged one, `herb` what a plantain poultice subtracts on
-- top of the bandage -- a second subtraction, not a multiplier, and it does
-- nothing without the bandage.
--
-- `stop` is the value the clock actually stops at, which is not always zero:
-- glass keeps bleeding pinned at 3, and a deep wound stays at 3 while it has
-- glass in it *or* while it is not bandaged. Reporting the time to reach zero
-- there would be announcing a moment that never arrives.
local WOUNDS = {
    { label = "IGUI_health_Scratched", gate = GATE.wound,
      units = function(bp) return bp:getScratchTime() end,
      bare = 1e-5, wrapped = 1.5e-4, herb = 1e-4 },
    { label = "IGUI_health_Cut", gate = GATE.wound,
      units = function(bp) return bp:getCutTime() end,
      bare = 1e-6, wrapped = 5e-5, herb = 5e-5 },
    { label = "IGUI_health_DeepWound", gate = GATE.deep,
      units = function(bp) return bp:getDeepWoundTime() end,
      bare = 2e-6, wrapped = 2e-5, herb = 7e-6,
      stop = function(bp)
          if bp:haveGlass() then return 3, "UI_AllInfo_health_GlassInside" end
          if not bp:bandaged() then return 3, "UI_AllInfo_health_NeedsBandage" end
          return 0
      end },
    { label = "IGUI_health_Bleeding", gate = GATE.wound,
      units = function(bp) return bp:getBleedingTime() end,
      bare = 2e-5, wrapped = 2e-4,
      stop = function(bp)
          if bp:haveGlass() then return 3, "UI_AllInfo_health_GlassInside" end
          return 0
      end },
    { label = "IGUI_health_Bitten", gate = GATE.wound,
      units = function(bp) return bp:getBiteTime() end,
      bare = 5e-6, wrapped = 1e-4 },
    { label = "IGUI_health_Burned", gate = GATE.deep,
      units = function(bp) return bp:getBurnTime() end,
      bare = 5e-6, wrapped = 1e-4 },
}

-- What the bandage pays for every wound it covers, per multiplier unit, from
-- the same method. A bandage over a bleeding deep wound burns 0.005 a unit,
-- sixteen times the plain bleeding rate: that is why it needs changing so soon.
local function bandageDrain(bp)
    local drain = 0
    if bp:getBiteTime() > 0 then drain = drain + 1e-4 end
    if bp:getBurnTime() > 0 then drain = drain + 1e-4 end
    if bp:getBleedingTime() > 0 then
        drain = drain + (bp:getDeepWoundTime() > 0 and 0.005 or 3e-4)
    end
    if bp:getScratchTime() > 0 then drain = drain + 8e-5 end
    if bp:getCutTime() > 0 then drain = drain + 1e-5 end
    if bp:getDeepWoundTime() > 0 then drain = drain + 1e-4 end
    if bp:getStitchTime() > 0 and bp:getStitchTime() < 50 then drain = drain + 1e-4 end
    if bp:isInfectedWound() then drain = drain + 2e-4 end
    return drain
end

-- Multiplier units in one in-game hour. The sandbox day length is the only
-- variable: a longer day means more frames per in-game hour, so wounds close in
-- fewer in-game hours.
local function unitsPerHour()
    local day = getSandboxOptions():getDayLengthMinutes()
    if not day or day <= 0 then return nil end
    return 120 * day
end

local function hoursFor(units, rate)
    if not units or units <= 0 or not rate or rate <= 0 then return nil end
    local perHour = unitsPerHour()
    if not perHour then return nil end
    return units / rate / perHour
end

local function timeText(units, rate)
    local hours = hoursFor(units, rate)
    if not hours then return nil end
    return AllInfo.duration(hours * 60)
end

local function allowed(level, needed)
    if not AllInfo.enabled("HealthGate") then return true end
    return not needed or (level or 0) >= needed
end

-- One row. The colour rides on the value alone, so the left column stays plain
-- and readable however bad things get.
-- The rich text parser trims every segment, so a plain space before the colour
-- tag disappears. <SPACE> is vanilla's own answer to that (ISZoneDisplay uses
-- the same trick) and adds one space's width plus two pixels.
local function row(out, label, value, color)
    if not value then return end
    out[#out + 1] = label .. ": <SPACE> " .. (color or WHITE) .. value .. WHITE
end

local function blank(out)
    if #out > 0 then out[#out + 1] = "" end
end

-- How the part is doing -----------------------------------------------------

-- BodyDamage.Update picks one of four whole-body rates by the *worst* of
-- hunger, thirst and illness -- levels, not a curve: moodle 2 drops the rate to
-- 0.0013, moodle 3 to 0.0008, and hunger or thirst at 4 stops healing dead.
-- Sleeping replaces all of that with 0.02, ten times the standard rate, unless
-- hunger or thirst is at 4, which zeroes it even asleep. Food adds its own
-- 0.015 while the food timer lasts.
local function healPerUnit(chr)
    local body = chr:getBodyDamage()
    local moodles = chr:getMoodles()
    -- A remote patient in multiplayer can answer without moodles. Reporting the
    -- standard rate there beats taking the whole context menu down over it.
    if not moodles then return body:getStandardHealthAddition(), "Normal" end

    local hungry = moodles:getMoodleLevel(MoodleType.HUNGRY)
    local thirst = moodles:getMoodleLevel(MoodleType.THIRST)
    local sick = moodles:getMoodleLevel(MoodleType.SICK)

    local rate = body:getStandardHealthAddition()
    local state = "Normal"
    if hungry == 2 or thirst == 2 or sick == 2 then
        rate, state = body:getReducedHealthAddition(), "Slowed"
    end
    if hungry == 3 or thirst == 3 or sick == 3 then
        rate, state = body:getSeverlyReducedHealthAddition(), "Slowed"
    end
    if hungry == 4 or thirst == 4 then rate, state = 0, "Stopped" end

    if chr:isAsleep() then
        rate, state = body:getSleepingHealthAddition(), "Asleep"
        if hungry == 4 or thirst == 4 then rate, state = 0, "Stopped" end
    end

    if body:getHealthFromFoodTimer() > 0 then
        rate = rate + body:getHealthFromFood()
    end
    return rate, state
end

-- AddGeneralHealth splits whatever it heals evenly between every part under
-- 100, so four wounded parts each mend at a quarter speed. Nothing in the
-- vanilla UI says this, and it is the whole reason the percentage below spends
-- its life under 100: one bleed drops all 17 parts off full health.
local function hurtParts(chr)
    local parts = chr:getBodyDamage():getBodyParts()
    local count = 0
    for i = 0, parts:size() - 1 do
        if parts:get(i):getHealth() < 100 then count = count + 1 end
    end
    return count
end

-- The damage an open wound keeps dealing to its own part every frame, from the
-- CombatManager.applyDamage calls at the top of DamageUpdate.
local function directDamage(bp)
    local dmg = 0
    if bp:getDeepWoundTime() > 0 and not bp:stitched() then
        dmg = dmg + (bp:bandaged() and 1.5625 or 3.125)
    end
    if bp:haveBullet() then dmg = dmg + (bp:bandaged() and 1.5625 or 3.125) end
    if not bp:bandaged() then
        if bp:getScratchTime() > 0 then dmg = dmg + 0.9375 end
        if bp:getCutTime() > 0 then dmg = dmg + 1.875 end
        if bp:getBiteTime() > 0 then dmg = dmg + 2.1875 end
        if bp:getBurnTime() > 0 then dmg = dmg + 3.75 end
    end
    if bp:getFractureTime() > 0 and not bp:isSplint() then dmg = dmg + 3.125 end
    return dmg * bp:getDamageScaler()
end

-- Bleeding and wound infection do not hit their own part: they go through
-- ReduceGeneralHealth, which splits the damage across all 17 parts and divides
-- again by that part's damage modifier. Leaving them out made the recovery time
-- optimistic exactly when it mattered most.
--
-- ponytail: only these two of the many sources that feed the same accumulator
-- (hypothermia, starvation, pain...). They are the two this tooltip is about;
-- the rest would need mirroring most of BodyDamage.Update.
local function sharedDamage(chr, bp)
    local body = chr:getBodyDamage()
    local parts = body:getBodyParts()
    local total = 0

    for i = 0, parts:size() - 1 do
        local other = parts:get(i)
        if other:getBleedingTime() > 0 and not other:bandaged() then
            total = total + 0.2857143 * other:getDamageScaler() * other:getBleedingTime() / 10
        end
    end

    -- An infected wound bills the body a severe-moodle's worth of damage from
    -- the very first instant, not past some level: the test is
    -- generalWoundInfectionLevel > the zombie infection stat, and that stat is
    -- zero unless you have been bitten.
    if body:getGeneralWoundInfectionLevel() > 0 then
        total = total + body:getHealthReductionFromSevereBadMoodles()
    end

    if total <= 0 then return 0 end
    local share = total / 17
    local modifier = BodyPartType.getDamageModifyer(bp:getIndex())
    if modifier and modifier > 0 then share = share / modifier end
    return share
end

local function statusRows(out, bp, chr)
    if not AllInfo.enabled("HealthRecovery") then return end
    -- A part already at full health has nothing to recover, so neither the speed
    -- nor the estimate mean anything on it.
    local health = bp:getHealth()
    if health >= 100 then return end

    local rate, state = healPerUnit(chr)
    local parts = hurtParts(chr)
    local body = chr:getBodyDamage()

    -- 100% is the baseline player: awake, no moodles, one wounded part. The
    -- base comes off the object rather than a literal so a mod that retunes it
    -- keeps us honest.
    local base = body:getStandardHealthAddition()
    local speed = parts > 0 and rate / parts or rate
    local speedColor = WHITE
    if state == "Slowed" or state == "Stopped" then speedColor = RED end
    if state == "Asleep" then speedColor = GREEN end
    if base > 0 then
        row(out, getText("UI_AllInfo_health_HealSpeed"), AllInfo.pct(speed / base, 0), speedColor)
    end

    local net = speed - directDamage(bp) - sharedDamage(chr, bp)
    if net > 0 then
        row(out, getText("UI_AllInfo_health_Recovery"), timeText(100 - health, net), GREEN)
        return
    end

    local perHour = unitsPerHour()
    local loss = perHour and AllInfo.pct(net * perHour / 100, 0) .. " / " .. getText("IGUI_Gametime_hour")
    row(out, getText("UI_AllInfo_health_Worsening"), loss or getText("IGUI_health_Severe"), RED)
end

-- Muscle strain is BodyPart.getStiffness(), 0 to 100, and it does exactly one
-- thing: getAdditionalPain(true) returns `additionalPain + stiffness / 3.5`.
-- Every consumer of that -- ClimbOverFenceState, IsoMovingObject and
-- IsoGameCharacter -- ignores it until it passes **20**, and then scales with
-- the excess. So on a part with no other pain the penalties start at a strain of
-- 70, and any additional pain brings that threshold down.
--
-- Colours follow the threshold rather than a number of ours: green below half of
-- it, white up to it, red once the penalties are live.
local function strainRow(out, bp)
    if not AllInfo.enabled("HealthStrain") then return end
    local strain = bp:getStiffness()
    if strain <= 0 then return end

    local threshold = (20 - bp:getAdditionalPain()) * 3.5
    if threshold < 1 then threshold = 1 end

    local color = WHITE
    if strain >= threshold then
        color = RED
    elseif strain < threshold / 2 then
        color = GREEN
    end
    row(out, getText("IGUI_health_Stiffness"), AllInfo.pct(strain / 100, 0), color)
end

-- What is wrong with it -----------------------------------------------------

local function woundRows(out, bp, level)
    if not AllInfo.enabled("HealthWound") then return end
    local wrapped = bp:bandaged()
    local plantain = bp:getPlantainFactor() > 0

    for i = 1, #WOUNDS do
        local w = WOUNDS[i]
        local units = w.units(bp)
        if units > 0 and allowed(level, w.gate) then
            local floor, why = 0
            if w.stop then floor, why = w.stop(bp) end

            if units <= floor and why then
                -- The clock is parked. A time here would be a lie.
                row(out, getText(w.label), getText(why), RED)
            else
                local rate = wrapped and w.wrapped or w.bare
                if wrapped and w.herb and plantain then rate = rate + w.herb end
                row(out, getText(w.label), timeText(units - floor, rate),
                    wrapped and GREEN or RED)
            end
        end
    end
end

-- A fracture mends at 5e-5 * splintFactor with a splint and 5e-6 without, so
-- the splint is worth ten times its own factor. Comfrey adds a flat 5e-6 either
-- way. The splint's quality rides in the same line rather than taking one.
--
-- That factor is nothing but the First Aid level of whoever applied it --
-- ISSplint sets (doctorLevel + 1) / 2 and the material is irrelevant -- so a
-- fracture splinted by a level 10 mends eleven times faster than by a level 0,
-- and this is the row where that shows.
local function fractureRow(out, bp, level)
    if not AllInfo.enabled("HealthFracture") then return end
    local units = bp:getFractureTime()
    if units <= 0 or not allowed(level, GATE.fracture) then return end

    local splint = bp:getSplintFactor()
    local rate = (splint > 0 and 5e-5 * splint or 5e-6)
    if bp:getComfreyFactor() > 0 then rate = rate + 5e-6 end

    local text = timeText(units, rate)
    if text and splint > 0 and allowed(level, GATE.deep) then
        text = text .. "  " .. getText("IGUI_health_Splinted") .. " x" .. AllInfo.num(splint, 2)
    end
    row(out, getText("IGUI_health_Fracture"), text, splint > 0 and GREEN or RED)
end

-- Stitches are the one clock that counts *up*: DamageUpdate adds 5e-4 a unit
-- while bandaged and 2e-4 bare, caps at 50, and vanilla calls them good to pull
-- past 40.
local function stitchRow(out, bp, level)
    if not AllInfo.enabled("HealthStitch") then return end
    local units = bp:getStitchTime()
    if units <= 0 or not allowed(level, GATE.fracture) then return end

    if units > 40 then
        row(out, getText("IGUI_health_Stitched"), getText("UI_AllInfo_health_StitchReady"), GREEN)
        return
    end
    row(out, getText("IGUI_health_Stitched"),
        timeText(40 - units, bp:bandaged() and 5e-4 or 2e-4), GREEN)
end

-- The row fires on isInfectedWound(), never on the level. The flag is what a
-- roll sets the instant the wound goes bad, while the level starts at zero and
-- climbs after, so keying on the number hid a fresh infection completely.
-- The number itself is vanilla's own scale: getGeneralWoundInfectionLevel()
-- multiplies the part's level by 10 and caps the body at 100.
--
-- ponytail: an alcohol-soaked bandage subtracts another 6e-4, three times
-- anything else, and it is missing here because `alcoholicBandage` is a private
-- field with no getter -- reporting it would mean guessing.
-- The infection roll, from the top of DamageUpdate, one throw per frame per
-- part while any open wound is on it. AdjustForFramerate multiplies the ceiling
-- by lockFPS/30, and there are lockFPS frames a second, so the odds per *real*
-- second come out at 30/chance whatever the framerate -- which is what makes
-- this reportable at all.
--
-- ponytail: assumes the game reaches its FPS cap. Below it the real risk is
-- lower, proportionally. And an alcohol-soaked bandage skips the roll entirely,
-- which cannot be read from Lua (see the note above infectionRow).
local function infectionChance(bp)
    if bp:getDeepWoundTime() <= 0 and bp:getScratchTime() <= 0
        and bp:getCutTime() <= 0 and bp:getStitchTime() <= 0 then return nil end

    local chance = 40000
    if not bp:bandaged() then
        chance = chance - 10000
    elseif bp:getBandageLife() <= 0 then
        -- A dirty bandage is far worse than no bandage at all: -35000.
        chance = chance - 35000
    end
    if bp:getScratchTime() > 0 then chance = chance - 20000 end
    if bp:getCutTime() > 0 then chance = chance - 25000 end
    if bp:getDeepWoundTime() > 0 then chance = chance - 30000 end
    if bp:haveGlass() then chance = chance - 24000 end
    if bp:getBurnTime() > 0 then chance = chance - 23000 end
    if bp:isNeedBurnWash() then chance = chance - 7000 end
    if bp:hasDirtyClothing() then chance = chance - 20000 end
    if bp:hasBloodyClothing() then chance = chance - 24000 end
    if chance < 5000 then chance = 5000 end
    return chance
end

-- Same odds, expressed over one in-game hour: an hour of game time is
-- 120 * dayLength multiplier units and a real second is 48 of them, so it lasts
-- 2.5 * dayLength real seconds.
local function infectionRiskRow(out, bp, level)
    if not AllInfo.enabled("HealthRisk") then return end
    if bp:isInfectedWound() or not allowed(level, GATE.infection) then return end

    local chance = infectionChance(bp)
    local day = getSandboxOptions():getDayLengthMinutes()
    if not chance or not day or day <= 0 then return end

    local risk = 1 - (1 - 30 / chance) ^ (2.5 * day)
    row(out, getText("UI_AllInfo_health_InfectionRisk"),
        AllInfo.pct(risk, 0) .. " / " .. getText("IGUI_Gametime_hour"),
        risk >= 0.5 and RED or WHITE)
end

local function infectionRow(out, bp, chr, level)
    if not AllInfo.enabled("HealthInfection") then return end
    if not bp:isInfectedWound() or not allowed(level, GATE.infection) then return end

    local text = AllInfo.pct(bp:getWoundInfectionLevel() / 10, 0)
    local cure = 0
    if bp:getAlcoholLevel() > 0 then cure = cure + 2e-4 end
    if bp:getGarlicFactor() > 0 then cure = cure + 2e-4 end
    if chr:getReduceInfectionPower() > 0 then cure = cure + 2e-4 end

    if cure <= 0 then
        row(out, getText("UI_AllInfo_health_WoundInfection"),
            text .. ", " .. getText("UI_AllInfo_health_Rising"), RED)
        return
    end

    local gone = timeText(bp:getWoundInfectionLevel(), cure)
    if gone then text = text .. ", " .. gone end
    row(out, getText("UI_AllInfo_health_WoundInfection"), text, GREEN)
end

-- What it is wearing --------------------------------------------------------

-- bandageLife is not the bandage's life, it is its clock to getting dirty:
-- isBandageDirty() is literally getBandageLife() <= 0. Hitting zero costs the
-- infection protection and, on removal, the bandage itself -- ISApplyBandage
-- consumes it instead of handing it back. It does *not* slow the healing down:
-- every wound rate keys on the bandaged() flag, never on this number.
local function bandageRow(out, bp)
    if not AllInfo.enabled("HealthBandage") then return end
    -- Order matters: isBandageDirty() is `life <= 0`, which is also true when
    -- there is no bandage at all.
    if not bp:bandaged() then
        row(out, getText("IGUI_health_Bandaged"), "-", RED)
        return
    end
    if bp:isBandageDirty() then
        row(out, getText("IGUI_health_Bandaged"), getText("IGUI_health_DirtyBandage"), RED)
        return
    end

    local hours = hoursFor(bp:getBandageLife(), bandageDrain(bp))
    local text = hours and AllInfo.duration(hours * 60)
    if not text then
        row(out, getText("IGUI_health_Bandaged"), getText("IGUI_health_Good"), GREEN)
        return
    end
    row(out, getText("IGUI_health_Bandaged"), text,
        hours < SWAP_SOON_HOURS and WHITE or GREEN)
end

-- Poultices burn out, and each only ticks down inside the wound branch that
-- uses it: plantain over a bandaged scratch *and* a bandaged laceration burns
-- twice as fast, comfrey only while a fracture is open, garlic only while the
-- wound is infected. Alcohol is the disinfectant's own timer and burns either
-- way. They share one line because in practice only one applies at a time.
local function plantainRate(bp)
    if not bp:bandaged() then return 0 end
    local wounds = 0
    if bp:getScratchTime() > 0 then wounds = wounds + 1 end
    if bp:getCutTime() > 0 then wounds = wounds + 1 end
    if bp:getDeepWoundTime() > 0 then wounds = wounds + 1 end
    return 8e-4 * wounds
end

local POULTICES = {
    { "ContextMenu_PlantainCataplasm",
      function(bp) return bp:getPlantainFactor() end, plantainRate },
    { "ContextMenu_ComfreyCataplasm",
      function(bp) return bp:getComfreyFactor() end,
      function(bp) return bp:getFractureTime() > 0 and 5e-4 or 0 end },
    { "ContextMenu_GarlicCataplasm",
      function(bp) return bp:getGarlicFactor() end,
      function(bp) return bp:isInfectedWound() and 8e-4 or 0 end },
    { "ContextMenu_Disinfect",
      function(bp) return bp:getAlcoholLevel() end, function() return 2e-4 end },
}

-- A poultice nothing is consuming -- plantain with no bandage under it, comfrey
-- with no fracture -- has no clock and is doing nothing, so it reads as a dash
-- like having none at all. That is what it is worth right now.
local function poulticeRow(out, bp)
    if not AllInfo.enabled("HealthPoultice") then return end
    local label = getText("UI_AllInfo_health_Poultice")
    for i = 1, #POULTICES do
        local left = POULTICES[i][2](bp)
        local text = left > 0 and timeText(left, POULTICES[i][3](bp))
        if text then
            row(out, label, text, GREEN)
            return
        end
    end
    row(out, label, "-", RED)
end

-- Anything still lodged in there goes last, on its own line and in red: it
-- outlives the wound clocks -- glass pins bleeding and deep wounds at 3 forever
-- -- and no amount of bandaging fixes it. Both labels are vanilla's own.
local function lodgedRows(out, bp)
    if not AllInfo.enabled("HealthLodged") then return end
    if bp:haveGlass() then
        blank(out)
        out[#out + 1] = RED .. getText("IGUI_health_LodgedGlassShards") .. WHITE
    end
    if bp:haveBullet() then
        if not bp:haveGlass() then blank(out) end
        out[#out + 1] = RED .. getText("IGUI_health_LodgedBullet") .. WHITE
    end
end

-- Nothing to say about a part that is whole again, even if the bandage is still
-- on it: taking that off is what the treatment menu is for. HasInjury() covers
-- bites, scratches, cuts, deep wounds, bleeding, fractures, burns and bullets,
-- but not stitches, strain, glass or infection, so those come along explicitly
-- -- stitches outliving their wound is the common case.
local function worthShowing(bp)
    if bp:getHealth() < 100 then return true end
    return bp:HasInjury() or bp:getStitchTime() > 0 or bp:getStiffness() > 0
        or bp:haveGlass() or bp:haveBullet() or bp:isInfectedWound()
end

-- Three blocks separated by a blank line: how the part is doing, what is wrong
-- with it, what it is wearing. Anything lodged in there gets the last word.
function AllInfo.Health.describe(bp, chr, level)
    if not worthShowing(bp) then return nil end

    local out = {}
    statusRows(out, bp, chr)
    strainRow(out, bp)

    local wounds = #out
    woundRows(out, bp, level)
    fractureRow(out, bp, level)
    stitchRow(out, bp, level)
    infectionRow(out, bp, chr, level)
    infectionRiskRow(out, bp, level)

    -- The treatment block also shows up on a part that is still bandaged after
    -- its wound closed: that bandage is doing nothing and wants taking off.
    local injured = #out > wounds
    if injured and wounds > 0 then table.insert(out, wounds + 1, "") end
    if injured or bp:bandaged() then
        blank(out)
        bandageRow(out, bp)
        if injured then poulticeRow(out, bp) end
    end
    lodgedRows(out, bp)

    if #out == 0 then return nil end
    return table.concat(out, " <LINE> ")
end

-- Hover ---------------------------------------------------------------------

function AllInfo.Health.title(bp)
    return BodyPartType.getDisplayName(bp:getType()) ..
        " - " .. AllInfo.pct(bp:getHealth() / 100, 0)
end

-- One tooltip for the whole mod: only one body part can be under the cursor at a
-- time, so pooling like the world menu does would buy nothing.
local tooltip
local showing = false

function AllInfo.Health.hide()
    if not showing then return end
    tooltip:setVisible(false)
    tooltip:removeFromUIManager()
    showing = false
end

-- Runs every frame the part list draws. mouseoverselected is the row under the
-- cursor, kept by ISScrollingListBox itself, and isMouseOver() is what tells a
-- stale index from a live one.
function AllInfo.Health.hover(list)
    local panel = list.parent
    local chr = panel and panel.character
    local index = list.mouseoverselected or -1
    local item = index > 0 and list.items[index]
    local bp = item and item.item and item.item.bodyPart

    if not chr or not bp or panel.blockingMessage
        or not list:isMouseOver() or list:isMouseOverScrollBar() then
        return AllInfo.Health.hide()
    end

    -- The treatment menu opens right where the cursor is, so it wins.
    local playerNum = panel.otherPlayer and panel.otherPlayer:getPlayerNum()
        or chr:getPlayerNum()
    local menu = getPlayerContextMenu(playerNum)
    if menu and menu:getIsVisible() then return AllInfo.Health.hide() end

    local text = AllInfo.Health.describe(bp, chr, panel.doctorLevel or 0)
    if not text then return AllInfo.Health.hide() end

    if not tooltip then
        tooltip = ISToolTip:new()
        tooltip:reset()
        tooltip.followMouse = false
    end
    tooltip:setName(AllInfo.Health.title(bp))
    tooltip.description = text
    -- Beside the list, never on top of it, at the height of the row.
    tooltip:setX(list:getAbsoluteX() + list:getWidth() + 10)
    tooltip:setY(getMouseY() - 12)

    if not showing then
        tooltip:setVisible(true)
        tooltip:addToUIManager()
        showing = true
    end
end

local baseRender = ISHealthBodyPartListBox.render

-- Wrapped, not replaced, so any medicine mod that also wraps the list keeps
-- working. An error here would repeat every frame, so the same self-disabling
-- policy as the crop panel applies.
function ISHealthBodyPartListBox:render(...)
    baseRender(self, ...)



    local ok, err = pcall(AllInfo.Health.hover, self)
    if not ok then
        print("[AllInfo] health info disabled: " .. tostring(err))
        AllInfo.Health.hover = function() end
        AllInfo.Health.hide()
    end
end

local baseSetVisible = ISHealthPanel.setVisible

-- The tooltip lives in the UIManager, so it has to be pulled when the panel
-- goes away: its render stops running and it would stay stuck on screen.
function ISHealthPanel:setVisible(visible, ...)
    if not visible then AllInfo.Health.hide() end
    baseSetVisible(self, visible, ...)
end

AllInfo.hooks = AllInfo.hooks or {}
AllInfo.hooks.HealthListBoxRender = ISHealthBodyPartListBox.render
AllInfo.hooks.HealthPanelVisible = ISHealthPanel.setVisible

-- The figure on the temperature bars ------------------------------------------

-- The body-temperature view draws eleven bars per body part and prints the
-- number on two of them, Insulation and Wind resistance. The other nine are a
-- coloured bar and nothing else, so "how cold is my hand" is a shade of blue.
--
-- Vanilla already has the switch and already writes the number, it just did not
-- set the flag on the rest (ISClothingInsPanel.lua:652):
--
--     if isDebugEnabled() or self.views[j].showValue then
--
-- So this sets it, and vanilla does the drawing, the rounding to two decimals
-- and the placing. Nothing of ours renders here, which is also why there are no
-- translation keys: the titles are vanilla's own.
--
-- It only ever prints for the body part the player has selected, one column at
-- a time, which is the behaviour we wanted anyway.
--
-- create() is the seam rather than the table literals: it builds viewsAdvanced
-- and viewsSimple and then walks both to derive functionNameUI, so a pass after
-- it is the first point where both lists are final.
require "XpSystem/ISUI/ISClothingInsPanel"

local baseCreate = ISClothingInsPanel.create

function ISClothingInsPanel:create(...)
    baseCreate(self, ...)

    if not AllInfo.enabled("TempValues") then return end

    -- Both lists, because the panel swaps self.views between them when the
    -- player toggles the simple and advanced styles.
    for _, list in ipairs({ self.viewsAdvanced, self.viewsSimple }) do
        for i = 1, #(list or {}) do list[i].showValue = true end
    end
end

AllInfo.hooks.TempValues = ISClothingInsPanel.create
