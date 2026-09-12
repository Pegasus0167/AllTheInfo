require "AllInfo/Core"

-- Vanilla paints Condition and Damage as bars only (setProgress), never as
-- numbers. That is what this provider is for.
--
-- Durability loss mirrors InventoryItem.damageCheck():
--   chance = (int)(getConditionLowerChance() * mult + bonus)
--   bonus += getMaintenanceMod(useMaint, chr)   then Rand.NextBool(chance)
-- which is a 1-in-N roll. Both getters are public, unlike in B41.

-- Fishing gear is a HandWeapon in the scripts, so it gets the full combat
-- block: crit, swing type, attack speed, knockback. Nobody clubs a zombie with
-- a rod, and the numbers bury the fishing ones. HideFishingCombat drops our
-- block on anything tagged as rod or net.
--
-- ⚠️ FISHING_SPEAR is deliberately NOT in this list any more. All 21 spears in
-- weapon.txt carry base:fishingspear, the crafted ones included, so the option
-- was silently blanking the tooltip of every spear in the game -- and
-- FishingGear.lua gives them nothing either, because they are in none of
-- Fishing.rods / line / hook / lure. A spear is a weapon first, and in B42 it
-- cannot be used to fish at all; the tag is left over.
--
-- The bars vanilla draws (condition, damage) stay: DoTooltipEmbedded is one
-- atomic Java call with no Lua seam, so they cannot be removed by anyone.
local FISHING_TAGS = { ItemTag.FISHING_ROD, ItemTag.FISHING_NET }

local function isFishingGear(item)
    for i = 1, #FISHING_TAGS do
        if FISHING_TAGS[i] and item:hasTag(FISHING_TAGS[i]) then return true end
    end
    return false
end

-- The six categories that grant XP, with the perk each one feeds. Straight from
-- server/XpSystem/XpUpdate.lua:86-105, which is the code that actually awards
-- it. IMPROVISED and UNARMED are left out on purpose: XpUpdate ignores them,
-- they do not enter the weapon level either, and IMPROVISED is the only category
-- that ever doubles up -- every two-category weapon in vanilla is
-- improvised;<something> -- so leaving it out means one weapon, one skill.
-- On AllInfo.MeleeWeapon rather than a local because SelfTest sweeps it.
AllInfo.MeleeWeapon = AllInfo.MeleeWeapon or {}
AllInfo.MeleeWeapon.XP_CATEGORIES = {
    { WeaponCategory.AXE,         Perks.Axe },
    { WeaponCategory.BLUNT,       Perks.Blunt },
    { WeaponCategory.SPEAR,       Perks.Spear },
    { WeaponCategory.LONG_BLADE,  Perks.LongBlade },
    { WeaponCategory.SMALL_BLADE, Perks.SmallBlade },
    { WeaponCategory.SMALL_BLUNT, Perks.SmallBlunt },
}

-- Attack speed, out of IsoPlayer.calculateCombatSpeed(), which is what
-- CombatManager hands to setCombatSpeed() on every swing:
--
--     s  = 0.8 * weapon.getBaseSpeed()
--     s *= 0.77                  two-handed and not held in both hands
--     s *= getChopTreeSpeed()    axes only: 1.0 with Axe Man, 0.8 without
--     s -= 0.07 * moodle(ENDURANCE)
--     s -= 0.07 * moodle(HEAVY_LOAD)
--     s += 0.03 * getWeaponLevel()
--     s += 0.02 * Fitness
--     ... then a container in the off hand, Rand(1.1, 1.2), arm injuries,
--     thermoregulation, a clamp to [0.8, 1.6] and a two-handed heavy bonus.
--
-- This used to read HandWeapon.getSpeedMod(), which is **dead code** in B42.20:
-- nothing in the jar and nothing in vanilla's Lua calls it, only this mod did.
-- It also only scaled for Axe, Blunt and Spear, so blades and short blunt sat
-- at a flat 100% here while in the game they gain like everything else, and
-- Fitness never showed up at all (state, trap 92).
local BASE_FACTOR    = 0.8
local LEVEL_STEP     = 0.03
local FITNESS_STEP   = 0.02

-- getChopTreeSpeed(), which despite the name is only ever called from
-- calculateCombatSpeed and only for axes: 1.0 with Ax-pert, 0.8 without. So an
-- axe in untrained hands swings at four fifths of its base speed, and the trait
-- is worth a flat +25 points on the row below, not the +5%% the trait block used
-- to claim -- that figure lived inside the dead getSpeedMod (state, trap 173).
local AXE_WITHOUT_AXEMAN = 0.8

-- getWeaponLevel(weapon) takes a weapon and then reads the one in your hands
-- anyway, the argument being only a null guard, so it cannot be asked about an
-- item sitting in a bag and the walk is reproduced. Starts at -1, the AXE branch
-- *assigns* where the other five *add*, capped at 10, and a level still at -1
-- comes back as 0. That last rule is why a non-axe counts the same at skill 0
-- and at skill 1, and it is the same off-by-one the damage line already carries.
-- On AllInfo.MeleeWeapon so SelfTest can hold it against the Java method for
-- the one case where that method works: the weapon actually in your hands.
function AllInfo.MeleeWeapon.weaponLevel(item, chr)
    local level = -1

    for i = 1, #AllInfo.MeleeWeapon.XP_CATEGORIES do
        local pair = AllInfo.MeleeWeapon.XP_CATEGORIES[i]
        if item:isOfWeaponCategory(pair[1]) then
            if pair[1] == WeaponCategory.AXE then
                level = chr:getPerkLevel(pair[2])
            else
                level = level + chr:getPerkLevel(pair[2])
            end
        end
    end

    if level > 10 then level = 10 end
    if level < 0 then level = 0 end
    return level
end

-- 100% is the floor: **this** weapon with both skills at zero and, on an axe,
-- without Ax-pert. Nothing ever reads under it, and everything above it is
-- something the character brings. Three things do, and on this scale they add
-- up rather than compound, which is the whole reason for normalising here:
--
--     weapon skill   +0.03 per effective level, over the floor
--     Fitness        +0.02 per level, over the floor
--     Ax-pert        a flat +25 points, axes only
--
-- What a point is worth in percent depends on the weapon, because the floor
-- does: 0.03 over a base-speed-1.0 weapon is 3.75%, over an axe (whose floor
-- carries the 0.8) it is 4.7%, and over a fast 1.2 weapon 3.1%. That is real,
-- not a rounding: a slower weapon gains proportionally more from the same point.
--
-- Left out on purpose, because it belongs to the moment and not to the weapon:
-- the tiredness and heavy-load moodles, arm injuries, body temperature, the
-- 1.1-1.2 spread on every swing, and the 0.77 for holding a two-hander with the
-- off hand full -- that last one is a grip you have not taken yet while the item
-- is sitting in a bag, and equipping a two-hander fills both hands by itself.
local function attackSpeed(item, chr)
    local base = item:getBaseSpeed()
    if not base or base <= 0 then return nil end

    local isAxe = item:isOfWeaponCategory(WeaponCategory.AXE)
    local floor = BASE_FACTOR * base * (isAxe and AXE_WITHOUT_AXEMAN or 1)

    local speed = BASE_FACTOR * base
    if isAxe then speed = speed * chr:getChopTreeSpeed() end

    speed = speed + LEVEL_STEP * AllInfo.MeleeWeapon.weaponLevel(item, chr)
                  + FITNESS_STEP * chr:getPerkLevel(Perks.Fitness)

    return speed / floor
end

-- Muscle strain one swing costs, as stiffness points on each part of the arm.
-- BodyPart.addStiffness clamps to [0,100], so the figure already is a
-- percentage of that bar and needs no scaling of ours.
--
-- IsoGameCharacter.addCombatMuscleStrain(), melee branch, verified in B42.20:
--     s  = weight * 0.15 * enduranceMod * 0.3 * 4      (= weight * 0.18 * mod)
--     s *= (zombies hit + 1) * (15 - Strength) / 10
--     s *= HandWeapon.muscleStrainMod(chr)
--     s *= 0.5   for a two-hander actually held in both hands
--     s *= 0.65
-- and then addArmMuscleStrain() finishes with * 2.5 * MuscleStrainFactor.
--
-- muscleStrainMod is called, not mirrored: it is public, and it is where the
-- weapon's own skill lives, at -7.5% per level.
--
-- ponytail: zombies hit is fixed at one, the normal case. It multiplies the
-- whole thing, so a swing that catches three costs twice this. The two-hander
-- held in a single hand is not modelled either -- that is the mistake case, not
-- the one a tooltip gets read for.
--
-- On AllInfo.MeleeWeapon rather than a local because SelfTest checks it.
function AllInfo.MeleeWeapon.strain(w, chr)
    if not chr or not w:isUseEndurance() or w:isRanged() then return nil end

    local s = w:getWeight() * 0.18 * w:getEnduranceMod()
        * 2                                              -- (zombies hit + 1)
        * (15 - chr:getPerkLevel(Perks.Strength)) / 10
        * w:muscleStrainMod(chr)
        * 0.65 * 2.5
        * AllInfo.gameSandbox("MuscleStrainFactor", 1)

    if w:isTwoHandWeapon() then s = s * 0.5 end
    if s <= 0 then return nil end   -- MuscleStrainFactor 0 switches it all off
    return s
end

-- No "real damage" row, and this is a decision, not a gap. The chain is closed:
-- every step was confirmed in bytecode and the last two doubtful multipliers
-- were settled in game by switching them off in CombatConfig and measuring
-- again (x1.5 for a non-player target and x0.15 for melee, both confirmed to
-- 0.8%). See plans/allinfo-estado.md 23.5 and 23.6.
--
-- What stops the row is what is left after the permanent part: a hit is also
-- multiplied by 2 * distance / maxRange, which has no ceiling in the code and
-- measured 2.4 in play, and by 1.5 for any hit that is not dead-on frontal.
-- Those two are worth 3.6x between them, so a row carrying only the derivable
-- part would print a quarter of what the player watches a zombie lose. A number
-- that is right on paper and wrong on screen is worse than no number.

-- Critical chance the character will actually roll, not the script number.
-- IsoPlayer.calculateCritChance(), melee branch: the weapon's own
-- CriticalChance plus three points per level of the skill that weapon trains,
-- rolled as Rand.Next(100) < crit. It was static before, which made a maxed
-- skill look like it did nothing for crits.
--
-- The two situational modifiers vanilla also applies there, the bonus from
-- behind and the penalty for holding a two-hander in one hand, are deliberately
-- left out: they describe the swing, not the weapon.
local function critChance(w, chr)
    local crit = w:getCriticalChance()
    if crit <= 0 then return nil end

    local scriptItem = chr and w:getScriptItem()
    if scriptItem then
        for i = 1, #AllInfo.MeleeWeapon.XP_CATEGORIES do
            local pair = AllInfo.MeleeWeapon.XP_CATEGORIES[i]
            if scriptItem:containsWeaponCategory(pair[1]) then
                crit = crit + chr:getPerkLevel(pair[2]) * 3
                break
            end
        end
    end

    if crit > 100 then crit = 100 end
    return crit
end

AllInfo.register("MeleeWeapon", 20, nil, function(out, item, chr)
    if not instanceof(item, "HandWeapon") or item:isRanged() then return end
    if AllInfo.enabled("HideFishingCombat") and isFishingGear(item) then return end

    -- Deltas go against the weapon in hand, and only when it is melee too.
    local other = AllInfo.compareTo(item, chr)
    if other and (not instanceof(other, "HandWeapon") or other:isRanged()) then other = nil end

    -- Two blocks: everything about the hit, then everything about the weapon
    -- lasting. The blank row does the grouping and the sweep at the end drops
    -- it if either block came out empty.
    local function blank() AllInfo.addRow(out, "", "") end

    local scriptItem = item:getScriptItem()

    -- 1. The hit --------------------------------------------------------------
    if AllInfo.enabled("WpnDamage") then AllInfo.damageRow(out, item, other) end

    local crit = critChance(item, chr)
    if crit then
        AllInfo.rowIf(out, "WpnCrit", getText("Tooltip_AllInfo_Critical"), AllInfo.num(crit, 1) .. "%",
            nil, AllInfo.delta(crit, other and critChance(other, chr), true, 1, "%"))
    end

    -- What a critical is worth. It runs from 200% to 1200% across vanilla
    -- weapons and appears nowhere on screen. Only drawn when a crit is
    -- possible at all.
    --
    -- The floor is 2, not the script value: IsoGameCharacter.processHitDamage()
    -- multiplies by Math.max(2, getCriticalDamageMultiplier()), so the fifteen
    -- vanilla weapons that ship a 1.0 (brooms, umbrellas, rakes, mop, tennis
    -- racket) and the griddle pan's 1.7 all crit for double anyway. Printing
    -- the script number there described a mechanic the game does not have.
    local critMult = crit and AllInfo.criticalDamage(item)
    if critMult then
        AllInfo.rowIf(out, "WpnCritDmg", getText("Tooltip_AllInfo_CriticalDamage"),
            AllInfo.pct(critMult, 0), nil,
            AllInfo.deltaPct(critMult,
                other and AllInfo.criticalDamage(other), true, 0))
    end

    -- Sharpness, which vanilla draws as a bar with no numbers on it, same as
    -- condition and damage.
    --
    -- The ceiling is the part nobody tells you: getMaxSharpness() is
    -- headCondition / headConditionMax, so a hand axe with a half-worn head
    -- cannot be sharpened past 50% no matter how long you work on it. And it
    -- matters, because getMaxDamage() is minDamage + (max - min) * (sharp+1)/2:
    -- a blunt edge drops the top of the damage range to its midpoint.
    --
    -- Written as "60 % / 80 %", the same "value / ceiling" shape the condition
    -- rows already use, so it needs no key of its own.
    if item:hasSharpness() then
        local sharp, cap = item:getSharpness(), item:getMaxSharpness()
        local value = AllInfo.pct(sharp, 0)
        if cap < 1 then value = value .. " / " .. AllInfo.pct(cap, 0) end

        AllInfo.rowIf(out, "WpnSharp", getText("Tooltip_weapon_Sharpness"), value, nil,
            AllInfo.deltaPct(sharp, other and other:hasSharpness() and other:getSharpness(),
                true, 0))
    end

    -- No colour on the value. It used to go green whenever the multiplier beat
    -- 1, which is a threshold of ours painting a judgement on a plain number:
    -- 105% read as "good weapon" when it only meant "this category scales at
    -- all". Here a delta *can* exist, so the comparison carries the colour.
    if chr then
        local speed = attackSpeed(item, chr)
        local otherSpeed = other and attackSpeed(other, chr)

        if speed then
            AllInfo.rowIf(out, "WpnSpeed", getText("Tooltip_AllInfo_AttackSpeed"),
                AllInfo.pct(speed), nil,
                AllInfo.deltaPct(speed, otherSpeed, true, 0))
        end
    end

    -- Reach, and it is not decoration: CombatManager multiplies the whole hit
    -- by 2 * distance / maxRange, capped nowhere and only reset to 1 when it
    -- would drop under 0.3. So a swing landed at the edge of your reach does up
    -- to twice the damage of one landed halfway in, and a longer weapon has a
    -- wider band in which that pays. Verified in bytecode; the Steam guide that
    -- documents this calls the 0.3 a floor, and it is not, it is a jump back
    -- to 1.
    --
    -- getMaxRange(chr) rather than getMaxRange(): the character's own version
    -- is the one the damage formula calls.
    local reach = chr and item:getMaxRange(chr) or item:getMaxRange()
    if reach and reach > 0 then
        local otherReach = other and (chr and other:getMaxRange(chr) or other:getMaxRange())
        AllInfo.rowIf(out, "WpnReach", getText("Tooltip_AllInfo_Reach"), AllInfo.num(reach, 2),
            nil, AllInfo.delta(reach, otherReach, true, 2))
    end

    -- No knockback row. PushBackMod scales the hit-direction vector, but every
    -- consumer of that vector's *length* in B42.20 is cosmetic: the speed of
    -- the giblets in IsoZombie and the blood splatter. ZombieHitReactionState
    -- only takes the angle to turn the zombie around, and StaggerBackState
    -- copies the direction while keeping its own length, so the zombie is never
    -- pushed by this number. Shown as "knockback" it described a mechanic the
    -- game does not have. KnockdownMod is worse: nothing outside the item
    -- editor and a debug CSV reads it at all.
    local strain = AllInfo.MeleeWeapon.strain(item, chr)
    if strain then
        local otherStrain = other and AllInfo.MeleeWeapon.strain(other, chr)
        AllInfo.rowIf(out, "WpnStrain", getText("Tooltip_AllInfo_MuscleStrain"),
            AllInfo.pct(strain / 100, 2), nil,
            AllInfo.deltaPct(strain / 100, otherStrain and otherStrain / 100, false, 2))
    end

    -- What actually separates a slow weapon from a fast one is its swing
    -- animation, and the clip length is not exposed to Lua. The animation name
    -- is, so we show that: it is the only consultable signal, and it is what
    -- makes a wood axe (Heavy) feel slower than a machete (Bat).
    -- Swingtime in the scripts is NOT it: only the firearm debug windows read
    -- it in B42, no melee combat class does.
    local swingAnim = scriptItem and scriptItem:getSwingAnim()
    if swingAnim and swingAnim ~= "" then
        local label = getTextOrNull("Tooltip_AllInfo_Swing_" .. swingAnim)
        if label then
            AllInfo.rowIf(out, "WpnSwing", getText("Tooltip_AllInfo_SwingType"), label)
        end
    end

    -- Which skill this weapon trains, which is also which skill drives its
    -- damage multiplier and its speed. perk:getName() and not
    -- "IGUI_perks_" .. getId(): five perks feed that key a hardcoded string that
    -- is not their id (see character/Core.lua), and getName() is exactly what
    -- PerkFactory.getPerkName() calls. Free in all 29 languages, no key of ours.
    -- No category, no row -- nothing invented for a weapon that trains nothing.
    if scriptItem then
        for i = 1, #AllInfo.MeleeWeapon.XP_CATEGORIES do
            local pair = AllInfo.MeleeWeapon.XP_CATEGORIES[i]
            if scriptItem:containsWeaponCategory(pair[1]) then
                AllInfo.rowIf(out, "WpnCategory", getText("Tooltip_AllInfo_WeaponType"), pair[2]:getName())
                break   -- one weapon, one XP category; SelfTest sweeps for a second
            end
        end
    end

    blank()

    -- 2. How long it lasts ----------------------------------------------------
    if AllInfo.enabled("WpnCondition") then AllInfo.conditionRow(out, item, other) end

    -- Maintenance and this weapon's own skill change the number, so it is only
    -- exact with a character. Lower is better here, hence the inverted color.
    --
    -- Two rolls on a tool weapon, one per part, side by side: the head is a
    -- separate check with its own odds, so a hammer wears its handle at 1 in 30
    -- and its head at 1 in 60. Weapons with no head keep the single row and its
    -- original label.
    local loss = AllInfo.conditionLoss(item, chr)
    local headLoss = AllInfo.headConditionLoss(item, chr)

    if loss then
        AllInfo.rowIf(out, "WpnLoss", getText(headLoss and "Tooltip_AllInfo_ConditionLossHandle"
                or "Tooltip_AllInfo_ConditionLoss"),
            AllInfo.pct(loss, 2),
            nil, AllInfo.deltaPct(loss, other and AllInfo.conditionLoss(other, chr), false, 2))
    end

    if headLoss then
        AllInfo.rowIf(out, "WpnLoss", getText("Tooltip_AllInfo_ConditionLossHead"),
            AllInfo.pct(headLoss, 2),
            nil, AllInfo.deltaPct(headLoss, other and AllInfo.headConditionLoss(other, chr),
                false, 2))
    end

    -- The one row that compares any two weapons, whatever parts they are made
    -- of: how many more swings this one has in it. See AllInfo.hitsToBreak.
    local hits = AllInfo.hitsToBreak(item, chr)
    if hits then
        AllInfo.rowIf(out, "WpnHits", getText("Tooltip_AllInfo_HitsLeft"), AllInfo.num(hits, 0),
            nil, AllInfo.delta(hits, other and AllInfo.hitsToBreak(other, chr), true, 0))
    end

    -- A separator only earns its line with rows on both sides of it: a weapon
    -- with no head, no edge or no category skips whole blocks, and the gaps
    -- would otherwise pile up. Collapsed in place, since `out` is the table the
    -- caller keeps.
    local tidy = {}
    for i = 1, #out do
        local isBlank = out[i].label == "" and out[i].value == ""
        local lastBlank = #tidy > 0 and tidy[#tidy].label == "" and tidy[#tidy].value == ""
        if not isBlank or (#tidy > 0 and not lastBlank) then tidy[#tidy + 1] = out[i] end
    end
    while #tidy > 0 and tidy[#tidy].label == "" and tidy[#tidy].value == "" do
        tidy[#tidy] = nil
    end
    for i = #out, 1, -1 do out[i] = nil end
    for i = 1, #tidy do out[i] = tidy[i] end
end)
