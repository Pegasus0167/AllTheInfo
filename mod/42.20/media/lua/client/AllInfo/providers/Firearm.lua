require "AllInfo/Core"

-- Mirrors HandWeapon.checkJam():
--     chance = jamGunChance * FirearmJamMultiplier
--     if chance == 0 -> never jams, vanilla returns early
--     weak   = (Aiming < 3 and Strength < 5) or (Aiming < 5 and Strength < 3)
--     wear   = (conditionMax - condition) / (8 * condition / conditionMax)
--     chance = (chance + (weak and 0.5 or 0) + wear) * 0.01
-- then Rand.Next(0,1) < chance. Returns a 0..1 probability, or nil when there
-- is nothing honest to show.
local function jamChance(item, chr)
    local base = item:getJamGunChance() * AllInfo.gameSandbox("FirearmJamMultiplier", 1.0)
    if base <= 0 then return nil end   -- this gun cannot jam at all

    local conditionMax = item:getConditionMax()
    if conditionMax <= 0 then return nil end

    local condition = item:getCondition()
    -- At condition 0 Java divides by zero and the chance goes infinite: the
    -- gun always jams. Say that outright instead of printing "inf".
    if condition <= 0 then return 1.0 end

    local weak = false
    if chr and not item:isManuallyRemoveSpentRounds() then
        local aiming = chr:getPerkLevel(Perks.Aiming)
        local strength = chr:getPerkLevel(Perks.Strength)
        weak = (aiming < 3 and strength < 5) or (aiming < 5 and strength < 3)
    end

    local wear = (conditionMax - condition) / (8 * condition / conditionMax)

    return (base + (weak and 0.5 or 0) + wear) * 0.01
end

-- Everything vanilla either hides or only paints as a bar, all the same shape:
-- a number, its delta against the gun in hand, and whether more is better.
-- Getters are wrapped in closures because Java methods cannot be indexed as
-- fields from Lua -- `item.getMaxRange` comes back nil even though it exists.
-- { label, getter, higher is better, decimals, suffix, option id }
local ROWS = {
    { "Tooltip_weapon_Range",        function(w) return w:getMaxRange() end,        true,  1, nil, "GunRange" },
    { "Tooltip_AllInfo_HitChance",   function(w) return w:getHitChance() end,       true,  0, "%", "GunHitChance" },
    { "Tooltip_AllInfo_Critical",    function(w) return w:getCriticalChance() end,  true,  1, "%", "GunCrit" },
    -- A louder gun pulls a bigger horde, and a slower one leaves you standing
    -- still: for these three, less is better.
    { "Tooltip_AllInfo_NoiseRadius", function(w) return w:getSoundRadius() end,     false, 0, nil, "GunNoise" },
}

-- Aiming and reloading, in seconds, because the raw script numbers are not a
-- unit of anything a player can use: "aiming time 40" says nothing.
--
-- Aiming. IsoGameCharacter.resetAimingDelay() seeds aimingDelay with the
-- weapon's aimingTime (x0.8 with Dextrous, x1.2 with All Thumbs), and
-- updateAimingDelay() burns it down by
--     0.625 * GameTime.getMultiplier() * (1 + 0.05 * Aiming + 0.1 if Marksman)
-- per frame. One real second is 48 multiplier units (a real hour is 172 800,
-- see character/Health.lua), so the wait is
--     aimingTime / (0.625 * modifier) / 48  seconds.
-- Real seconds, not in-game ones: this is a combat clock and does not stretch
-- with the day length.
local UNITS_PER_REAL_SECOND = 48
local AIM_DRAIN = 0.625

local function aimingSeconds(w, chr)
    local base = w:getAimingTime()
    if not base or base <= 0 then return nil end

    local modifier = 1
    if chr then
        if chr:hasTrait(CharacterTrait.DEXTROUS) then base = base * 0.8
        elseif chr:hasTrait(CharacterTrait.ALL_THUMBS) then base = base * 1.2 end

        modifier = 1 + 0.05 * chr:getPerkLevel(Perks.Aiming)
        if chr:hasTrait(CharacterTrait.MARKSMAN) then modifier = modifier + 0.1 end
    end

    return base / (AIM_DRAIN * modifier) / UNITS_PER_REAL_SECOND
end

-- Reloading. HandWeapon.getReloadTime() is **dead in B42.20**: nothing outside
-- the item editor, the debug panel and the network packet ever reads it. What
-- the game actually runs is a fixed number of milliseconds per action, divided
-- by the ReloadSpeed animation variable, and that variable is what
-- ISReloadWeaponAction.setReloadSpeed() computes:
--     0.8 + Reloading * 0.10 - panicMoodleLevel * 0.05
-- So the old row was quoting a number that changes nothing. This one quotes the
-- action the gun will really perform: a magazine goes in whole, everything else
-- is fed a round at a time.
local MAGAZINE_MS = 1500
local BULLET_MS = 550

local function reloadSpeed(chr)
    if not chr then return 0.8 end
    local speed = 0.8 + chr:getPerkLevel(Perks.Reloading) * 0.10
    local moodles = chr:getMoodles()
    if moodles then
        speed = speed - moodles:getMoodleLevel(MoodleType.PANIC) * 0.05
    end
    return speed > 0.1 and speed or 0.1
end

local function reloadSeconds(w, chr)
    local magazine = w.getMagazineType and w:getMagazineType()
    local base = (magazine and magazine ~= "") and MAGAZINE_MS or BULLET_MS
    return base / 1000 / reloadSpeed(chr), base == BULLET_MS
end

-- Same idea as MeleeWeapon: condition and damage are what vanilla only draws
-- as bars, plus the numbers it never shows at all.

AllInfo.register("Firearm", 25, nil, function(out, item, chr)
    if not instanceof(item, "HandWeapon") or not item:isRanged() then return end

    -- Deltas go against the gun in hand, and only when it is a gun too.
    local other = AllInfo.compareTo(item, chr)
    if other and (not instanceof(other, "HandWeapon") or not other:isRanged()) then other = nil end

    if AllInfo.enabled("GunCondition") then AllInfo.conditionRow(out, item, other) end
    if AllInfo.enabled("GunDamage") then AllInfo.damageRow(out, item, other) end

    for i = 1, #ROWS do
        local label, get, higherIsBetter, dec, suffix = ROWS[i][1], ROWS[i][2],
            ROWS[i][3], ROWS[i][4], ROWS[i][5]
        local v = get(item)
        if v > 0 then
            AllInfo.rowIf(out, ROWS[i][6], getText(label), AllInfo.num(v, dec) .. (suffix or ""),
                nil, AllInfo.delta(v, other and get(other), higherIsBetter, dec, suffix))
        end
    end

    local aim = aimingSeconds(item, chr)
    if aim then
        AllInfo.rowIf(out, "GunAim", getText("Tooltip_AllInfo_AimingTime"),
            getText("UI_AllInfo_gun_Seconds", AllInfo.num(aim, 2)), nil,
            AllInfo.delta(aim, other and aimingSeconds(other, chr), false, 2))
    end

    local reload, perBullet = reloadSeconds(item, chr)
    if reload and reload > 0 then
        AllInfo.rowIf(out, "GunReload", getText("Tooltip_AllInfo_ReloadTime"),
            getText(perBullet and "UI_AllInfo_gun_PerBullet" or "UI_AllInfo_gun_Seconds",
                AllInfo.num(reload, 2)))
    end

    -- No delta on this one: it really is the state of this magazine, not a
    -- property of the model, so there is nothing honest to compare it with.
    local clip = item:getClipSize()
    if clip > 0 then
        AllInfo.rowIf(out, "GunClip", getText("Tooltip_AllInfo_Capacity"),
            item:getCurrentAmmoCount() .. " / " .. clip)
    end

    -- No firearm matches any melee WeaponCategory, so the weapon-level half of
    -- the maintenance mod is always 0 here and only Maintenance moves it.
    local loss = AllInfo.conditionLoss(item, chr)
    if loss then
        AllInfo.rowIf(out, "GunLoss", getText("Tooltip_AllInfo_ConditionLoss"), AllInfo.pct(loss, 2),
            nil, AllInfo.deltaPct(loss, other and AllInfo.conditionLoss(other, chr), false, 2))
    end

    -- jamChance() returns nil for a gun that cannot jam at all, and that nil
    -- means "no comparison", not "zero": no delta rather than a made-up one.
    --
    -- No threshold colour: the 5% that used to paint this red was ours, not
    -- the game's, and a fixed cutoff reads as "this gun is broken" when it only
    -- means "this gun is a gun". The colour lives in the delta, where there is
    -- an actual comparison behind it.
    local jam = jamChance(item, chr)
    if jam then
        AllInfo.rowIf(out, "GunJam", getText("Tooltip_AllInfo_JamChance"),
            AllInfo.pct(jam, 2), nil,
            AllInfo.deltaPct(jam, other and jamChance(other, chr), false, 2))
    end
end)
