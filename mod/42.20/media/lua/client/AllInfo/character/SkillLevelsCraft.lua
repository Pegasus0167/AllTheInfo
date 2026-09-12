require "AllInfo/Core"
require "AllInfo/character/SkillLevels"

-- Per-level lines for the twenty skills of the Agriculture, Crafting and
-- Survivalist trees. The six weapon skills live in SkillLevels.lua; the nine
-- physical and firearm ones are still hand-written keys in IG_UI.json.
--
-- The wiki was checked first, as asked, and it is only half a source: Cooking
-- and Electrical are exact, Agriculture and Foraging are wrong, First Aid is
-- half wrong, and Carpentry, Animal Care, Butchering, Trapping, Tracking and
-- Mechanics carry no figures at all. So every number below was read out of the
-- game and the wiki was used as a checklist, nothing more.
--
-- ponytail: these mirror one-line formulas that live inside methods needing a
-- real character, so they cannot be called with an arbitrary level. Fishing is
-- the exception and is called for real. SelfTest holds the mirrors against the
-- player's own level every run, which is what stops them rotting.

AllInfo.SkillLevels = AllInfo.SkillLevels or {}

local function frag(key, ...)
    return getText(key, ...)
end

-- Time formulas are all "base - k * level" tick counts. What the player can use
-- is how much faster that is than untrained, so they are reported that way.
local function faster(base, perLevel, level)
    return AllInfo.round(perLevel * level / base * 100, 1)
end

-- 1. Agriculture ------------------------------------------------------------
-- SPlantGlobalObject:seed / :initHealth / :cureAphids, and
-- getVegetablesNumber in farming_vegetableconf.lua.
local function farming(n, out)
    out[#out + 1] = frag("UI_AllInfo_perk_CropHealth", "+" .. n)
    out[#out + 1] = frag("UI_AllInfo_perk_CropCursed", (11 - n) * 5)
    out[#out + 1] = frag("UI_AllInfo_perk_CropBonus", (9 + n) * 5)
    out[#out + 1] = frag("UI_AllInfo_perk_CropCure", 10 + n)
    out[#out + 1] = frag("UI_AllInfo_perk_CropYield", n * 10, n)
    out[#out + 1] = frag("UI_AllInfo_perk_BackStrain", "-" .. (n * 5))
end

-- ISMilkAnimal / ISShearAnimal: the stress roll drops 5 points per level and
-- only matters up to level 7, above which a stressed animal never breaks off.
local function husbandry(n, out)
    if n >= 8 then
        out[#out + 1] = frag("UI_AllInfo_perk_AnimalCalm")
    else
        out[#out + 1] = frag("UI_AllInfo_perk_AnimalStress", "-" .. (n * 5))
    end
    -- ISShearAnimal: timePerLiter starts at 100 and drops 2 per level. The
    -- milking action has the same line commented out, so this is shearing only.
    out[#out + 1] = frag("UI_AllInfo_perk_ShearTime", "-" .. (n * 2))
end

-- ButcheringUtil.getPartChance and .addAnimalPart.
local function butchering(n, out)
    out[#out + 1] = frag("UI_AllInfo_perk_ButcherParts", AllInfo.num(n / 7, 2))
    out[#out + 1] = frag("UI_AllInfo_perk_ButcherYield",
        AllInfo.num(1 + math.floor(n / 2) / 10, 2))
    out[#out + 1] = frag("UI_AllInfo_perk_ButcherBlood", 22 - n * 2)
end

-- 2. Crafting ---------------------------------------------------------------
-- buildUtil.getWoodHealth, ISBuildingObject:getMaxTime, ISBarricadeAction and
-- ISMoveableSpriteProps.
local function woodwork(n, out)
    out[#out + 1] = frag("UI_AllInfo_perk_BuildHealth", "+" .. (n * 50))
    out[#out + 1] = frag("UI_AllInfo_perk_BuildTime", "-" .. faster(200, 5, n))
    out[#out + 1] = frag("UI_AllInfo_perk_BarricadeTime", "-" .. faster(100, 5, n))
    -- ISMoveableSpriteProps rolls ZombRand(100) < 10 + level * 10, so from
    -- level 9 on it is a certainty and the raw 110 would be a lie.
    out[#out + 1] = frag("UI_AllInfo_perk_Dismantle", math.min(100, 10 + n * 10))
end

-- EvolvedRecipe.addItem: the ingredient is consumed at (100 - 3n)% and each
-- one carries (1 + n/15) times its nutrients. RecipeManager gates rotten food
-- at level 7.
local function cooking(n, out)
    out[#out + 1] = frag("UI_AllInfo_perk_CookIngredient", 100 - n * 3)
    out[#out + 1] = frag("UI_AllInfo_perk_CookNutrition", AllInfo.num(1 + n / 15, 2))
    -- addItem's rotten branch: a rotten ingredient is worth 5%% of its base
    -- hunger at 7 and 8, and 10%% at 9 and 10. Below 7 RecipeManager refuses it
    -- outright, so there is nothing to say.
    if n >= 9 then
        out[#out + 1] = frag("UI_AllInfo_perk_CookRotten", 10)
    elseif n >= 7 then
        out[#out + 1] = frag("UI_AllInfo_perk_CookRotten", 5)
    end
end

-- ISSplint, ISApplyBandage and the four ISHealthPanel thresholds.
local function doctor(n, out)
    out[#out + 1] = frag("UI_AllInfo_perk_Fracture", AllInfo.num((n + 1) / 2, 2))
    out[#out + 1] = frag("UI_AllInfo_perk_Bandage",
        AllInfo.num((n + 1) * 0.5, 1), AllInfo.num(n + 1, 1))
    out[#out + 1] = frag("UI_AllInfo_perk_MedTime", "-" .. faster(120, 4, n))
    if n == 3 then out[#out + 1] = frag("UI_AllInfo_perk_MedWound") end
    if n == 5 then out[#out + 1] = frag("UI_AllInfo_perk_MedPain") end
    if n == 7 then out[#out + 1] = frag("UI_AllInfo_perk_MedStitch") end
    if n == 9 then out[#out + 1] = frag("UI_AllInfo_perk_MedInfection") end
end

-- ISRemovePatch.chanceToGetPatchBack and :getDuration.
local function tailoring(n, out)
    -- Two different things, both scaling on floor(level / 2), and worth telling
    -- apart because the player sees two different items come out:
    --   ripClothing      -> rags, clamped to the parts the garment covers
    --   pickAramidThread -> aramid thread, raising the top of the roll, cap 10
    if n >= 2 then
        out[#out + 1] = frag("UI_AllInfo_perk_RipCloth", "+" .. math.floor(n / 2))
        out[#out + 1] = frag("UI_AllInfo_perk_ThreadPick", "+" .. math.floor(n / 2))
    end
    out[#out + 1] = frag("UI_AllInfo_perk_PatchBack", 10 + n * 5)
    out[#out + 1] = frag("UI_AllInfo_perk_PatchTime", "-" .. faster(150, 6, n))
    if n == 8 then out[#out + 1] = frag("UI_AllInfo_perk_PatchFull") end
end

-- ISFixGenerator and BaseVehicle.tryHotwire.
local function electricity(n, out)
    out[#out + 1] = frag("UI_AllInfo_perk_Generator", AllInfo.num(4 + n / 2, 1))
    out[#out + 1] = frag("UI_AllInfo_perk_Hotwire", "+" .. (n * 4))
    out[#out + 1] = frag("UI_AllInfo_perk_Alarm", 12 - n)
end

local function mechanics(n, out)
    if n == 4 then out[#out + 1] = frag("UI_AllInfo_perk_EngineStandard") end
    if n == 5 then out[#out + 1] = frag("UI_AllInfo_perk_EngineHeavy") end
    if n == 6 then out[#out + 1] = frag("UI_AllInfo_perk_EngineSport") end
end

local function masonry(n, out)
    if n == 5 then out[#out + 1] = frag("UI_AllInfo_perk_BrickWall") end
end

-- 3. Survivalist ------------------------------------------------------------
-- Fishing.Utils.getFishSizeChancesBySkillLevel is a pure function of the level,
-- so it is *called*, not mirrored. Nothing here can go stale.
local function fishing(n, out)
    local ok, small, medium, big = pcall(function()
        return Fishing.Utils.getFishSizeChancesBySkillLevel(n, false, 1)
    end)
    if ok and small then
        out[#out + 1] = frag("UI_AllInfo_perk_FishSize", small, medium, big)
    end
end

-- forageSystem: poisonChance + ((10 - level) * 3) on berries and mushrooms.
local function foraging(n, out)
    out[#out + 1] = frag("UI_AllInfo_perk_ForagePoison", "+" .. ((10 - n) * 3))
end

-- ISInspectAnimalTrackAction:getDuration.
local function tracking(n, out)
    out[#out + 1] = frag("UI_AllInfo_perk_TrackTime", "-" .. faster(100, 1.5, n))
end

-- Carving, Blacksmithing, Pottery, Glassmaking and Knapping read the level
-- nowhere outside the recipe gate. Saying so is more honest than a blank, and
-- the recipe line right underneath already lists what this level unlocks.
local function recipesOnly(n, out)
    out[#out + 1] = frag("UI_AllInfo_perk_RecipesOnly")
end

local BY_ID = {
    Farming = farming,
    Husbandry = husbandry,
    Butchering = butchering,
    Woodwork = woodwork,
    Cooking = cooking,
    Doctor = doctor,
    Tailoring = tailoring,
    Electricity = electricity,
    Mechanics = mechanics,
    Masonry = masonry,
    Fishing = fishing,
    PlantScavenging = foraging,
    Tracking = tracking,
    Carving = recipesOnly,
    Blacksmith = recipesOnly,
    Pottery = recipesOnly,
    Glassmaking = recipesOnly,
    FlintKnapping = recipesOnly,
}

-- Trapping and MetalWelding are absent on purpose: TrapSystem only stores the
-- level on the trap and never reads it back in B42.20, and Welding gates
-- recipes through the same list Carving does but also drives the forge, which
-- is not derivable. Neither gets an invented line.

function AllInfo.SkillLevels.craft(perk, level)
    if not perk or type(level) ~= "number" or level < 1 or level > 10 then return nil end

    local fn = BY_ID[perk:getId()]
    if not fn then return nil end

    local parts = {}
    fn(level, parts)
    if #parts == 0 then return nil end

    -- " <LINE> " with the spaces: this tooltip splits on that, and a tag glued
    -- to a word swallows the word.
    return table.concat(parts, " <LINE> ")
end
