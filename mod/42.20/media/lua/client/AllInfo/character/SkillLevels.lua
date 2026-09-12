require "AllInfo/Core"

-- What each level of a weapon skill actually gives you, under vanilla's own
-- per-level tooltip in the skills panel.
--
-- These used to be 60 hand-written translation keys, ten per weapon skill, and
-- all six shared the same copied text. Three of its four numeric lines were
-- wrong: attack speed was claimed for three skills that do not have it, the
-- crit figure was a third of the real one, and the damage table was right only
-- for Axe. Writing them by hand is what let that rot, so now they are derived.
--
-- Vanilla only ships IGUI_perks_<skill>_Description without a number, so
-- dropping ours leaves no hole: getTextOrNull comes back nil and vanilla adds
-- nothing.

AllInfo.SkillLevels = AllInfo.SkillLevels or {}

-- Perk -> is it the axe branch. Not cosmetic: see the damage note below, and
-- the speed line rides on the same off-by-one.
-- Perks.Blunt is "Long Blunt" and Perks.SmallBlunt is "Short Blunt".
local WEAPON_PERKS = {
    { Perks.Axe,        true  },
    { Perks.Blunt,      false },
    { Perks.Spear,      false },
    { Perks.LongBlade,  false },
    { Perks.SmallBlade, false },
    { Perks.SmallBlunt, false },
}

-- Attack speed. IsoPlayer.calculateCombatSpeed() adds 0.03 per weapon level to
-- a figure that starts at 0.8 * the weapon's BaseSpeed, so what a level is worth
-- in percent depends on the weapon. A skill tooltip has no weapon in front of
-- it, so it answers for base speed 1.0, which is 104 of the melee weapons in the
-- game: 0.03 / 0.8 = 3.75% a level.
--
-- Axes divide by 0.64 instead, not 0.8: their floor carries the 0.8 of
-- getChopTreeSpeed() without Ax-pert, so the same 0.03 is a bigger share of a
-- smaller number. Same rule the weapon tooltip uses, so the two agree.
--
-- All six branches scale, and that is the correction. This used to read
-- HandWeapon.getSpeedMod(), which only moved for Axe, Blunt and Spear and which
-- **nothing in the game calls** (state, trap 173).
local SPEED_BASE     = 0.8
local AXE_FLOOR      = 0.8 * 0.8
local SPEED_INCREMENT = 0.03

-- IsoPlayer.calculateCritChance(): crit += perkLevel * 3, rolled as
-- Rand.Next(100) < crit, so it is three percentage points per level.
-- HandWeapon.muscleStrainMod(): (1 - weaponSkill * 0.075) * strainModifier.
-- ponytail: both hardcoded, no getter exists for either. The strain figure is
-- the weapon's half of it; Strength carries the other half, x(15 - Strength)/10
-- in addCombatMuscleStrain(), and says so on its own tooltip.
local CRIT_PER_LEVEL = 3
local STRAIN_PER_LEVEL = 7.5

-- The damage multiplier is the one thing the game will hand over, so it is read
-- instead of copied: CombatConfig is exposed to Lua and getCombatConfig() is a
-- global. If Indie Stone retunes combat, this line retunes with it.
local FALLBACK_BASE, FALLBACK_INCREMENT = 0.3, 0.1

local function damageMultipliers()
    local cfg = getCombatConfig and getCombatConfig()
    if not cfg or not CombatConfigKey then return FALLBACK_BASE, FALLBACK_INCREMENT end

    local ok, base, increment = pcall(function()
        return cfg:get(CombatConfigKey.BASE_WEAPON_DAMAGE_MULTIPLIER),
               cfg:get(CombatConfigKey.WEAPON_LEVEL_DAMAGE_MULTIPLIER_INCREMENT)
    end)
    if not ok or type(base) ~= "number" or type(increment) ~= "number" then
        return FALLBACK_BASE, FALLBACK_INCREMENT
    end
    return base, increment
end

-- CombatManager.applyWeaponLevelDamageModifier() feeds on getWeaponLevel(), not
-- on the perk level, and getWeaponLevel() starts at -1 and then *assigns* in
-- the AXE branch while every other category *adds*. So outside the axe branch
-- the effective level is one below the skill level, and the damage table is
-- shifted by one for five of the six skills. Level 0 is the exception: the -1
-- comes back out as 0, so all six agree there.
--
-- Reproduced on purpose. It looks like a vanilla slip (the first branch written
-- with = and the rest copied with +=) but it is what the game rolls.
local function effectiveLevel(level, isAxe)
    local eff = isAxe and level or (level - 1)
    if eff < 0 then eff = 0 end
    if eff > 10 then eff = 10 end
    return eff
end

-- One "+3%" / "-70%" fragment, or nil when the value rounds to nothing worth a
-- line. Every key carries its own sign through AllInfo.signed.
local function fragment(key, value, decimals)
    if value == 0 then return nil end
    return getText(key, AllInfo.signed(value, decimals))
end

function AllInfo.SkillLevels.describe(perk, level)
    if not perk or type(level) ~= "number" or level < 1 or level > 10 then return nil end

    local isAxe
    for i = 1, #WEAPON_PERKS do
        if WEAPON_PERKS[i][1] == perk then
            isAxe = WEAPON_PERKS[i][2]
            break
        end
    end
    if isAxe == nil then return nil end   -- not a weapon skill, not ours

    local parts = {}
    local eff = effectiveLevel(level, isAxe)

    local base, increment = damageMultipliers()
    parts[#parts + 1] = fragment("UI_AllInfo_perk_Damage",
        ((base + eff * increment) - 1) * 100, 0)

    -- On the effective level, like the damage above: calculateCombatSpeed feeds
    -- on the same getWeaponLevel(), so outside the axe branch level 1 is worth
    -- nothing here either.
    parts[#parts + 1] = fragment("UI_AllInfo_perk_Speed",
        eff * SPEED_INCREMENT / (isAxe and AXE_FLOOR or SPEED_BASE) * 100, 1)

    parts[#parts + 1] = fragment("UI_AllInfo_perk_Crit", level * CRIT_PER_LEVEL, 0)
    parts[#parts + 1] = fragment("UI_AllInfo_perk_Strain", -level * STRAIN_PER_LEVEL, 1)

    -- The same floor(level / 2) AllInfo.conditionLoss already adds to the
    -- durability roll, so both surfaces agree by construction.
    local maintenance = math.floor(eff / 2)
    if maintenance > 0 then
        parts[#parts + 1] = getText("UI_AllInfo_perk_Durability", maintenance)
    end

    if #parts == 0 then return nil end
    -- " <LINE> ", with the spaces, is what this tooltip separates on: vanilla
    -- writes them that way and <br> glued to a word was swallowing it whole.
    return table.concat(parts, " <LINE> ")
end

-- No wrapper of its own on purpose. character/XpMultiplier.lua already owns the
-- one hook on ISSkillProgressBar:updateTooltip and builds an `extra` list of
-- lines there; this hangs off that instead of stacking a second wrapper on the
-- same method, which would also break the SelfTest's hook identity check.
