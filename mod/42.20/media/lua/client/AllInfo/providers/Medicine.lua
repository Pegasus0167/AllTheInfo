require "AllInfo/Core"

-- How long a pill lasts, how long it takes to start, and what it does per
-- minute. Vanilla says none of it: the tooltip of a bottle of beta blockers is
-- the same as the tooltip of a rock.
--
-- The clocks live in IsoGameCharacter and are set by BodyDamage.JustTookPill().
-- They tick down by GameTime.getThirtyFPSMultiplier(), which is
-- getMultiplier() / 1.6, and GameTime.update() advances the day by
-- multiplier / (120 * dayLength) hours. So one in-game hour is
-- 120 * dayLength multiplier units, i.e. 75 * dayLength of these, and a pill's
-- duration in in-game minutes is units * 0.8 / dayLength.
--
-- Corollary worth keeping in mind: a pill lasts a fixed amount of *real* time
-- and a variable number of in-game hours, exactly like wound healing. Nothing
-- here is a constant; every figure is recomputed from the sandbox day length.

local function dayLength()
    local day = getSandboxOptions and getSandboxOptions():getDayLengthMinutes()
    if not day or day <= 0 then return nil end
    return day
end

-- Thirty-FPS units -> in-game minutes.
local function minutesFor(units)
    local day = dayLength()
    if not day or not units or units <= 0 then return nil end
    return units * 0.8 / day
end

-- A per-unit rate -> points per in-game minute. Everything is normalised to a
-- 0..100 bar: pain, panic and unhappiness already are, fatigue is a 0..1 stat
-- (the Tired moodle trips at 0.6) and gets scaled here so the five pills can be
-- read side by side. Without that, "-105 pain" and "+0.75 fatigue" look like
-- numbers from different games.
local function perMinute(rate, scale)
    local day = dayLength()
    if not day then return nil end
    return rate * 1.25 * day * (scale or 1)
end

-- Verified in IsoGameCharacter, the block that decrements each effect:
--   panic       stats.remove(PANIC,        0.6      * thirtyFPS)
--   unhappiness stats.remove(UNHAPPINESS,  0.03     * thirtyFPS)
--   pain        stats.remove(PAIN,         0.0233.. * thirtyFPS)
--   fatigue     stats.add(FATIGUE, 0.0016667 * dose * thirtyFPS)
--
-- Only the sleeping tablets multiply by their dose; the other three ignore the
-- delta they store. What the beta blockers' delta *is* used for is
-- BodyDamage.IncreasePanic(), which scales incoming panic by 1 - delta.
--
-- `first` is the wait before the effect starts, and only PillsAntiDep has one:
-- BetaAntiDepress() sets depressFirstTakeTime = 10000 the first time only,
-- while depressEffect is still 0.
local PILLS = {
    ["Base.Pills"] = {
        duration = 5400, rate = 0.0233333, stat = "IGUI_StatsAndBody_Pain",
        detail = { "UI_AllInfo_med_PainFreeze", "UI_AllInfo_med_DrunkThird" },
    },
    ["Base.PillsBeta"] = {
        duration = 6600, rate = 0.6, stat = "IGUI_StatsAndBody_Panic",
        detail = { "UI_AllInfo_med_BetaIncoming", "UI_AllInfo_med_DrunkHalf",
                   "UI_AllInfo_med_SleepCancels" },
    },
    ["Base.PillsAntiDep"] = {
        duration = 6600, first = 10000, rate = 0.03, stat = "IGUI_StatsAndBody_Unhappiness",
        detail = { "UI_AllInfo_med_FirstDoseOnly", "UI_AllInfo_med_DrunkHalf" },
    },
    -- The only pill intoxication does not weaken: JustTookPill() hands the
    -- sleeping tablet a flat 0.1 whatever your state. What it does instead is
    -- count the dose twice towards the overdose, in setSleepingPillsTaken(),
    -- and the counter only walks back down one every two in-game hours.
    ["Base.PillsSleepingTablets"] = {
        duration = 6600, rate = 0.0016667 * 0.1, scale = 100, gain = true,
        stat = "IGUI_StatsAndBody_Fatigue",
        detail = { "UI_AllInfo_med_SleepCancels", "UI_AllInfo_med_Overdose",
                   "UI_AllInfo_med_DrunkDouble" },
    },
    -- The antibiotic has no rate: it does not drain a bar, it cancels the
    -- zombie fever's growth tick for tick until its 50 points of power run out.
    -- infectionGrowthRate is a flat 0.001 nobody changes, so the duration is
    -- power / (0.001 * 120 * dayLength) hours. Note this one drains in plain
    -- multiplier units, not thirty-FPS ones, so it does not go through
    -- minutesFor().
    ["Base.Antibiotics"] = {
        power = 50, stat = nil,
        detail = { "UI_AllInfo_med_AntibioticFreeze", "UI_AllInfo_med_NoStacking" },
    },
}

local INFECTION_GROWTH = 0.001

local function antibioticMinutes(power)
    local day = dayLength()
    if not day or not power or power <= 0 then return nil end
    return power / (INFECTION_GROWTH * 120 * day) * 60
end

AllInfo.register("Medicine", 90, nil, function(out, item, chr)
    local pill = PILLS[item:getFullType()]
    if not pill then return end

    local minutes = pill.power and antibioticMinutes(pill.power) or minutesFor(pill.duration)
    local d = minutes and AllInfo.duration(minutes)
    if d then AllInfo.rowIf(out, "MedDuration", getText("UI_AllInfo_med_Duration"), d) end

    -- The wait is real but one-shot: once depressEffect is running, a second
    -- dose acts immediately. Showing it on a character who is already medicated
    -- would be a lie, so it is dropped there.
    if pill.first then
        local pending = not chr or chr:getDepressEffect() <= 0
        local wait = pending and AllInfo.duration(minutesFor(pill.first))
        if wait then AllInfo.rowIf(out, "MedWait", getText("UI_AllInfo_med_Wait"), wait) end
    end

    if pill.rate then
        local rate = perMinute(pill.rate, pill.scale)
        if rate and rate > 0 then
            -- The rate on its own: it is what compares two pills at a glance,
            -- and it is the *net* pace with no new sources, so a horde raising
            -- panic while the pill lowers it is not this number's business.
            AllInfo.rowIf(out, "MedEffect", getText("UI_AllInfo_med_Effect"),
                AllInfo.signed(pill.gain and rate or -rate, 2)
                    .. " " .. getText(pill.stat)
                    .. " / " .. getText("IGUI_Gametime_minute"))
        end
    elseif pill.power then
        AllInfo.rowIf(out, "MedEffect", getText("UI_AllInfo_med_Effect"),
            getText("UI_AllInfo_med_FeverHeld"))
    end

    -- Everything else the pill does, behind its own option and on a single
    -- labelled row rather than a stack of unlabelled ones.
    if not AllInfo.enabled("MedicineDetail") then return end

    local details = {}
    for i = 1, #pill.detail do
        details[#details + 1] = getText(pill.detail[i])
    end
    if #details > 0 then
        AllInfo.addRow(out, getText("UI_AllInfo_med_Details"),
            table.concat(details, ", "))
    end
end)
