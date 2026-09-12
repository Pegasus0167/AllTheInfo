require "AllInfo/Core"
require "ISUI/ISLiteratureUI"   -- miscRecipes, the five non-craft "recipes"

AllInfoChar = AllInfoChar or {}

-- A trait or profession block. Almost every line comes out of the definition
-- object itself, so a modded trait gets the same block for free and nothing
-- here can go stale with a patch.
--
-- The one exception is the hand-written effects at the bottom, for what is
-- hardcoded in Java and cannot be read at runtime. Those live in UI.json under
-- UI_AllInfo_trait_<id> and there is no table for them here on purpose.

-- getName() is the perk's own translated display name. Building
-- "IGUI_perks_" .. getId() looked equivalent and is not: PerkFactory feeds that
-- key a hardcoded string that differs from the id for five perks -- Foraging is
-- registered as PlantScavenging, Lightfooted as Lightfoot, Sneaking as Sneak,
-- Passive as Passiv and Combat - Melee as Melee -- so those printed the raw key
-- on screen ("IGUI_perks_PlantScavenging +1"). PerkFactory.getPerkName() is
-- literally a call to this method.
local function perkName(perk)
    return perk:getName()
end

local function traitName(trait)
    local def = CharacterTraitDefinition.getCharacterTraitDefinition(trait)
    return def and def:getUIName() or tostring(trait)
end

-- Every list in this block joins on `sep`, which is the same newline the block
-- itself is built with. They used to join on ", " and ran off the side of the
-- tooltip: a ranger's foraging line alone is nine specialisations wide.
local function joinNames(javaList, nameFn, sep)
    if not javaList or javaList:size() == 0 then return nil end

    local names = {}
    for i = 0, javaList:size() - 1 do
        names[#names + 1] = nameFn(javaList:get(i))
    end

    table.sort(names)
    return table.concat(names, sep)
end

-- Starting skill levels, and the one surface that still needs them.
--
-- BaseGameCharacterDetails.SetTraitDescription and .SetProfessionDescription
-- (shared/NPCs/MainCreationMethods.lua) rewrite every definition's description
-- at load: they append one "+N Skill" line per XP boost, sorted by skill name,
-- and the profession one also appends a line per granted trait. So wherever the
-- *description* is on screen, that list is already under it and ours would be a
-- second copy two lines below.
--
-- The exception is ISCharacterScreen.loadProfession, which puts only
-- getUIName() on the tooltip, the bare name. There the description never
-- appears, so nothing lists the boosts, and the block has to. `full` is that
-- one case, and nothing else passes it.
--
-- Same reasoning splits granted traits: SetTraitDescription does not add them,
-- SetProfessionDescription does. Only two vanilla traits grant anything (Weight
-- Gain -> Overweight and Weight Loss -> Underweight), so it is a small line that
-- is still the only place those two are stated.
local function skillList(def, sep)
    local boosts = def:getXpBoosts()
    if not boosts then return nil end

    local skills = {}
    for perk, level in pairs(transformIntoKahluaTable(boosts)) do
        skills[#skills + 1] = perkName(perk) .. " " .. AllInfo.signed(level:intValue())
    end
    if #skills == 0 then return nil end

    table.sort(skills)
    return table.concat(skills, sep)
end

-- Recipe ids do translate after all: CraftRecipe.getTranslationName() is what
-- the crafting UI itself puts on screen (ISWidgetCraftLogicTitle.lua:107). The
-- count stays as the fallback for an id the script manager does not know,
-- which is what a half-loaded mod looks like.
--
-- ponytail: capped at RECIPE_LIMIT names plus a count. The heaviest vanilla
-- profession grants 86 recipes, and a tooltip listing all of them is unusable.
-- Upgrade path if the cap ever annoys: a scrollable panel of its own.
local RECIPE_LIMIT = 8

-- Not every granted "recipe" is a CraftRecipe. Vehicle know-how ships as
-- GrantedRecipes = Basic Mechanics;Intermediate Mechanics, which the script
-- manager does not know, and the whole list used to collapse to its own count:
-- the Mechanics trait printed "Teaches recipes: 2".
--
-- Vanilla keeps those five in ISLiteratureUI.miscRecipes with the key of their
-- own label, so it is read rather than mirrored, and a mod that adds one gets
-- named for free. Guarded: the table lives in a client file.
local function miscRecipeName(id)
    local misc = ISLiteratureUI and ISLiteratureUI.miscRecipes
    local entry = misc and misc[id]
    return entry and entry.tooltip and getTextOrNull(entry.tooltip) or nil
end

-- Three sources, in order, because "granted recipe" covers three different
-- things and only the first is a CraftRecipe:
--   1. the crafting recipes, via the script manager
--   2. the five vehicle and herbalist know-hows in ISLiteratureUI.miscRecipes
--   3. everything in Recipes.json, which is where the growing-season entries
--      live: Translator.getRecipeName is what vanilla's own context menu calls
--
-- Anything still unnamed is skipped rather than thrown, which is the bug this
-- replaces: Herbalist grants nine, five of them are growing seasons, and one
-- unnamed id used to collapse the whole list to "Teaches recipes: 9".
local function nameOfRecipe(id, manager)
    local recipe = manager and manager:getCraftRecipe(id)
    local name = recipe and recipe:getTranslationName()
    if name and name ~= "" then return name end

    name = miscRecipeName(id)
    if name and name ~= "" then return name end

    local ok, translated = pcall(function() return Translator.getRecipeName(id) end)
    if ok and translated and translated ~= "" and translated ~= id then return translated end

    return nil
end

local function recipeNames(ids, sep)
    local names = {}
    local manager = getScriptManager()

    for i = 0, ids:size() - 1 do
        local name = nameOfRecipe(ids:get(i), manager)
        if name then names[#names + 1] = name end
    end
    if #names == 0 then return nil end

    table.sort(names)

    local shown = #names
    if shown > RECIPE_LIMIT then
        local extra = shown - RECIPE_LIMIT
        while #names > RECIPE_LIMIT do table.remove(names) end
        -- The counter stays glued to the last name: on its own line it reads
        -- like a recipe called "(+12)".
        return table.concat(names, sep) .. " (+" .. extra .. ")"
    end

    return table.concat(names, sep)
end

local function recipeList(def, sep)
    local recipes = def:getGrantedRecipes()
    if not recipes or recipes:size() == 0 then return nil end
    return recipeNames(recipes, sep) or tostring(recipes:size())
end

-- Foraging bonuses, straight out of forageSystem's own tables.
--   visionBonus       added to the search radius (getProfessionVisionBonus)
--   weatherEffect     % of the weather penalty cancelled, capped at
--                     forageSystem.effectReductionMax
--   darknessEffect    the same for the darkness penalty
--   specialisations   % added to the roll for that category
-- skillDefs is the indexed copy and only exists once forageSystem.init() has
-- run, which has not happened yet on the character creation screen; the raw
-- definition table is always loaded, so it is the fallback.
local function forageDef(def)
    if not forageSystem then return nil end

    local name = def:getType() and def:getType():getName()
    if not name then return nil end

    local indexed = forageSystem.skillDefs
    local found = indexed and ((indexed.occupation and indexed.occupation[name])
        or (indexed.trait and indexed.trait[name]))
    if found then return found end

    -- Case-insensitive: professions store name = CharacterProfession:getName(),
    -- but traits store a literal like "Whittler" while getName() returns the
    -- ResourceLocation path, which is lower case ("whittler").
    local wanted = string.lower(name)
    for _, entry in pairs(forageSystem.forageSkillDefinitions or {}) do
        if entry.type and entry.name and string.lower(entry.name) == wanted then return entry end
    end
    return nil
end

local function forageLine(def, sep)
    local entry = forageDef(def)
    if not entry then return nil end

    local parts = {}
    if entry.visionBonus and entry.visionBonus ~= 0 then
        parts[#parts + 1] = getText("UI_AllInfo_ForageVision") .. " "
            .. AllInfo.signed(entry.visionBonus, 2)
    end

    local cap = forageSystem.effectReductionMax
    local function reduction(key, label)
        local v = entry[key]
        if not v or v == 0 then return end
        if cap and v > cap then v = cap end
        parts[#parts + 1] = getText(label) .. " -" .. AllInfo.num(v, 0) .. "%"
    end

    reduction("weatherEffect", "UI_AllInfo_ForageWeather")
    reduction("darknessEffect", "UI_AllInfo_ForageDarkness")

    local specials = {}
    for category, bonus in pairs(entry.specialisations or {}) do
        if bonus and bonus ~= 0 then
            -- Vanilla's own category label, so this is translated everywhere.
            local label = getTextOrNull("IGUI_SearchMode_Categories_" .. category) or category
            specials[#specials + 1] = label .. " " .. AllInfo.signed(bonus, 0) .. "%"
        end
    end

    if #specials > 0 then
        table.sort(specials)
        parts[#parts + 1] = table.concat(specials, sep)
    end

    if #parts == 0 then return nil end
    return table.concat(parts, sep)
end

-- Hand-written effects, for what is hardcoded in Java and cannot be read at
-- runtime. There is no table here on purpose: the text lives entirely in
-- UI.json under UI_AllInfo_trait_<id>, so adding a trait is adding a key, and a
-- missing key simply means "nothing to add".
local function manualEffects(def)
    if not AllInfo.enabled("TraitManualEffects") then return nil end

    local id = def:getType() and def:getType():getName()
    local manual = id and getTextOrNull("UI_AllInfo_trait_" .. id)
    if manual == "" then return nil end
    return manual
end

-- def is a CharacterTraitDefinition or a CharacterProfessionDefinition; the two
-- share getXpBoosts / getGrantedTraits / getGrantedRecipes, and only traits have
-- exclusions and the multiplayer flag.
--
-- instanceof, never `def.getMutuallyExclusiveTraits`: Java methods are not
-- indexable as fields from Lua, so duck typing silently reports "no" for
-- everything (the structure-menu bug).
--
-- `skipSkills` is for the character creation screen, which already prints the
-- starting skills in its own column two inches to the right.
function AllInfoChar.definitionBlock(def, sep, full)
    if not def then return "" end
    sep = sep or "\n"

    -- Each section is its label on one line, its content underneath, and a
    -- blank line before the next. A profession that grants eight recipes and
    -- nine foraging bonuses is unreadable as one "Label: a, b, c" per line.
    local blocks = {}
    local function add(labelKey, content)
        if not content or content == "" then return end
        if labelKey then content = getText(labelKey) .. ":" .. sep .. content end
        blocks[#blocks + 1] = content
    end

    local isTrait = instanceof(def, "CharacterTraitDefinition")

    if full then add("UI_AllInfo_TraitSkills", skillList(def, sep)) end
    if isTrait or full then
        add("UI_AllInfo_TraitGrants", joinNames(def:getGrantedTraits(), traitName, sep))
    end
    add("Tooltip_AllInfo_TeachesRecipes", recipeList(def, sep))
    add("UI_AllInfo_Foraging", forageLine(def, sep))
    add(nil, manualEffects(def))

    -- No "incompatible with" line: the creation screen already greys out and
    -- refuses the conflicting traits, so it was a long list saying nothing you
    -- could not see by clicking.
    if isTrait and def:isDisabledInMultiplayer() then
        add(nil, getText("UI_AllInfo_TraitNoMP"))
    end

    return table.concat(blocks, sep .. sep)
end

-- Appends the block to a tooltip that is already there, once. The flag matters:
-- populateProfessionList does not clear its list before filling it, so a second
-- pass would otherwise stack the block on the same entries.
function AllInfoChar.appendBlock(existing, def, sep, full)
    local block = AllInfoChar.definitionBlock(def, sep, full)
    if block == "" then return existing end

    if not existing or existing == "" then return block end
    return existing .. (sep or "\n") .. (sep or "\n") .. block
end
