require "AllInfo/Core"

AllInfoChar = AllInfoChar or {}

-- What a skill level actually gates, read from the script manager instead of
-- written by hand.
--
-- This is the answer to "what does level 6 of Carpentry give me", which is the
-- only per-level question most crafting skills have. Hardcoding it would be
-- wrong twice over: the lists are long, and they change with every patch and
-- with every mod that adds a recipe. Derived, they cost one sweep and are
-- always right.
--
-- CraftRecipe.getRequiredSkill(i) returns a RequiredSkill with getPerk() and
-- getLevel(), and both getAllCraftRecipes() and getAllBuildableRecipes() carry
-- them. The line says **requires**, not "unlocks", and that is deliberate: a
-- recipe can also need a magazine (needToBeLearn), in which case the level is
-- necessary but not sufficient. A requirement is true either way.
--
-- ponytail: LIMIT names then "(+N)". Carpentry level 1 alone gates dozens, and
-- a skill tooltip that fills the screen is worse than a truncated one. Upgrade
-- path if it ever annoys: a panel of its own.
--
-- One per line and the same 8 the trait block uses (character/Core.lua), so the
-- two lists in this mod cut at the same place. Eight names on one line ran off
-- the side of the tooltip; eight lines is taller but every name is readable.
local LIMIT = 8

-- What this tooltip splits on. Vanilla writes its own separators with the
-- spaces, and a <br> glued to a word was swallowing it whole.
local SEP = " <LINE> "

local index   -- [perkId][level] = sorted list of names, built once

local function collect(recipes, byPerk)
    if not recipes then return end

    for i = 0, recipes:size() - 1 do
        local recipe = recipes:get(i)

        for s = 0, recipe:getRequiredSkillCount() - 1 do
            local required = recipe:getRequiredSkill(s)
            local perk = required and required:getPerk()
            local level = required and required:getLevel()

            -- Level 0 is "no requirement" dressed up as one.
            if perk and level and level > 0 then
                local id = perk:getId()
                local levels = byPerk[id]
                if not levels then levels = {}; byPerk[id] = levels end

                local list = levels[level]
                if not list then list = {}; levels[level] = list end

                -- getTranslationName() is what the crafting UI itself puts on
                -- screen, so this is translated everywhere for free.
                local name = recipe:getTranslationName()
                if name and name ~= "" then list[#list + 1] = name end
            end
        end
    end
end

local function build()
    local byPerk = {}

    local manager = getScriptManager()
    if manager then
        collect(manager:getAllCraftRecipes(), byPerk)
        collect(manager:getAllBuildableRecipes(), byPerk)
    end

    -- Sorted and de-duplicated once, here, rather than on every hover. Two
    -- recipes really can share a display name (the same wall in two materials).
    for _, levels in pairs(byPerk) do
        for level, list in pairs(levels) do
            table.sort(list)

            local unique, last = {}, nil
            for i = 1, #list do
                if list[i] ~= last then unique[#unique + 1] = list[i]; last = list[i] end
            end
            levels[level] = unique
        end
    end

    return byPerk
end

-- "Needs this level:" and then one recipe per line, the last one carrying
-- "(+4)" when the list was cut. nil when this level gates nothing, which is the
-- common case for the combat skills.
function AllInfoChar.recipeLine(perk, level)
    if not perk or not level or level <= 0 then return nil end
    if not AllInfo.enabled("SkillRecipes") then return nil end

    -- Built on the first hover, never at load: the script manager has not
    -- finished reading the scripts while client Lua is still being executed.
    if not index then index = build() end

    local levels = index[perk:getId()]
    local names = levels and levels[level]
    if not names or #names == 0 then return nil end

    local shown = #names
    if shown <= LIMIT then
        return getText("UI_AllInfo_SkillRecipes") .. ":" .. SEP .. table.concat(names, SEP)
    end

    local head = {}
    for i = 1, LIMIT do head[i] = names[i] end
    -- The count rides on the last name shown, not on a line of its own.
    head[LIMIT] = head[LIMIT] .. " (+" .. (shown - LIMIT) .. ")"
    return getText("UI_AllInfo_SkillRecipes") .. ":" .. SEP .. table.concat(head, SEP)
end
