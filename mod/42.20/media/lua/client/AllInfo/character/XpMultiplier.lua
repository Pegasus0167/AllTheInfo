require "AllInfo/Core"
require "AllInfo/character/SkillRecipes"   -- recipeLine, appended to the tooltip below
require "AllInfo/character/SkillLevels"    -- describe(), appended to the same tooltip
require "AllInfo/character/SkillLevelsCraft" -- craft(), the other twenty skills
require "OptionScreens/CharacterCreationProfession"
require "XpSystem/ISUI/ISSkillProgressBar"
require "ISUI/PlayerStats/ISPlayerStatsUI"

AllInfoChar = AllInfoChar or {}

-- Vanilla shows an XP boost as "+ 75%", which is wrong by a factor of four.
--
-- Verified in IsoGameCharacter$XP.AddXP: a skill with *no* boost is multiplied
-- by 0.25, not by 1. So a level-1 boost taking it to 1.00 does not add 75%, it
-- quadruples the gain. The four surfaces that print it all get the real figure.
--
-- The exclusion lists mirror the private methods isSkillExcludedFromSpeed-
-- Reduction / ...Increase. Re-check them on each PZ update.
local function excludedFromReduction(perk)
    return perk == Perks.Sprinting or perk == Perks.Fitness or perk == Perks.Strength
end

local function excludedFromIncrease(perk)
    return perk == Perks.Fitness or perk == Perks.Strength
end

-- The boost half of AddXP, absolute.
local function boostFactor(perk, boost)
    if boost == 0 then return excludedFromReduction(perk) and 1.0 or 0.25 end
    if boost == 1 then return perk == Perks.Sprinting and 1.25 or 1.0 end
    if boost >= 2 and not excludedFromIncrease(perk) then
        return boost == 2 and 1.33 or 1.66
    end
    return 1.0
end

-- What the boost is actually worth: the gain with it over the gain without it.
--
-- No character needed, and that is not a shortcut. AddXP applies the trait
-- modifiers (Fast Learner x1.3, Slow Learner x0.7, Pacifist x0.75, Crafty
-- x1.3) *after* the boost factor and identically whether the boost is there or
-- not, so they cancel in the ratio. Only the perk and the boost matter.
function AllInfoChar.xpRelative(perk, boost)
    local none = boostFactor(perk, 0)
    if none <= 0 then return nil end
    return boostFactor(perk, boost) / none
end

-- "x 4", "x 5.32", "x 1.25". nil when the boost changes nothing, so callers can
-- leave vanilla's own text alone rather than print "x 1".
function AllInfoChar.xpRelativeText(perk, boost)
    local rel = AllInfoChar.xpRelative(perk, boost)
    if not rel or rel == 1 then return nil end
    return "x " .. AllInfo.num(rel, 2)
end

-- Perk description keys are built from the perk's **English display name**, not
-- from its id:
--     EN  "IGUI_perks_Woodwork": "Carpentry"
--         "IGUI_perks_Carpentry_Description": "..."
--     ES  "IGUI_perks_Woodwork": "Carpintería"
--         "IGUI_perks_Carpentry_Description": "..."   <- translated, English key
--
-- Vanilla composes the key with getName(), which is translated, so in English it
-- lands on the right key by accident and everywhere else it asks for
-- "IGUI_perks_Carpintería_Description" and prints that raw. **Every perk
-- description in B42.20 is broken outside English**, even though the translated
-- text is right there in the file.
--
-- getId() is not the answer either: thirteen ids differ from their English
-- name, which is exactly what this table is. Everything else -- Aiming,
-- Cooking, Maintenance, Nimble, Sneaking, Lightfooted, Foraging... -- matches
-- its id.
--
-- Six of these were missing until now, and they are the ones whose English name
-- contains a *space*: "Long Blunt", "Short Blunt", "Long Blade", "Short Blade",
-- "First Aid", "Animal Care". Vanilla does have a description for each; without
-- the mapping the wrapper asked for "IGUI_perks_Blunt_Description", which does
-- not exist, so those six skills showed nothing at all -- in English too.
--
-- ponytail: derived from vanilla's own EN/IG_UI.json by matching each
-- IGUI_perks_<id> against the _Description keys that actually resolve; re-check
-- if TIS renames a skill. A wrong entry only costs the description line.
--
-- Three more were missing until now, and they are the ones whose *display key*
-- also differs from the id: PerkFactory registers Foraging under the id
-- PlantScavenging, Lightfooted under Lightfoot and Sneaking under Sneak. All
-- three have a vanilla description and a per-level table in this mod, and none
-- of them was reachable.
AllInfoChar.englishName = {
    Blacksmith = "Blacksmithing",
    Blunt = "Long Blunt",
    Doctor = "First Aid",
    Electricity = "Electrical",
    Farming = "Agriculture",
    FlintKnapping = "Knapping",
    Husbandry = "Animal Care",
    Lightfoot = "Lightfooted",
    LongBlade = "Long Blade",
    MetalWelding = "Welding",
    PlantScavenging = "Foraging",
    SmallBlade = "Short Blade",
    SmallBlunt = "Short Blunt",
    Sneak = "Sneaking",
    Sprinting = "Running",
    Woodwork = "Carpentry",
}

function AllInfoChar.descriptionName(perk)
    local id = perk:getId()
    return AllInfoChar.englishName[id] or id
end

-- 1) Character creation ------------------------------------------------------
-- drawXpBoostMap draws the percentage with a single drawTextRight call, so the
-- method is swapped on the instance for the duration of the original and put
-- back afterwards. Same trick Render.lua uses on setHeight/setWidth.
--
-- Wrapping the class function is enough even though the listbox captures it by
-- value (`doDrawItem = CharacterCreationProfession.drawXpBoostMap`): that
-- assignment runs when the screen is built, long after this file has loaded.
local baseDrawXpBoostMap = CharacterCreationProfession.drawXpBoostMap

function CharacterCreationProfession:drawXpBoostMap(y, item, alt)
    if not AllInfo.enabled("XpMultiplierFix") or not item or not item.item then
        return baseDrawXpBoostMap(self, y, item, alt)
    end

    local text = AllInfoChar.xpRelativeText(item.item.perk, item.item.level)
    if not text then return baseDrawXpBoostMap(self, y, item, alt) end

    -- rawget for the restore so we put back nil, not a frozen copy of the
    -- class method; plain index for the call so we get whatever would really
    -- have run. The listbox is a Lua table, so both behave normally here.
    local hadInstance = rawget(self, "drawTextRight")
    local original = self.drawTextRight

    self.drawTextRight = function(s, _, ...) return original(s, text, ...) end

    local ok, result = pcall(baseDrawXpBoostMap, self, y, item, alt)
    self.drawTextRight = hadInstance

    if not ok then error(result) end
    return result
end

-- 2) Skill panel tooltip -----------------------------------------------------
-- The message is rebuilt by vanilla on every hover, so it is edited afterwards
-- rather than intercepted. Replacing the global getText for the duration would
-- be the obvious alternative and is what the plan suggested; it is not worth
-- the risk, because a Java exception can walk straight through a pcall (see the
-- picker crash) and would leave the entire game without getText.
local VANILLA_PERCENT = { [1] = "75%", [2] = "100%", [3] = "125%" }

-- Cuts one line out of a rich-text message. Plain find, never a pattern: these
-- strings carry '%', '-' and ':'.
local function cutText(message, text)
    if not text or text == "" then return message end

    local line = " <LINE> " .. text
    local at = message:find(line, 1, true)
    if at then return message:sub(1, at - 1) .. message:sub(at + #line) end

    at = message:find(text, 1, true)
    if at then return message:sub(1, at - 1) .. message:sub(at + #text) end

    return message   -- another mod rewrote it; leave it alone
end

-- Cutting text out of the middle leaves its separators behind, and vanilla
-- writes them in pairs (" <LINE><LINE> " before the description and again
-- before the per-level line), so dropping the generic blurb left four in a row
-- and the tooltip showed a band of empty rows between vanilla's block and ours.
-- Rather than teach every cut about its own separator, the message is tidied
-- once at the end: a run of more than two becomes two -- one blank line, which
-- is the spacing vanilla uses everywhere -- and dangling ones at the tail go.
function AllInfoChar.tidyTooltip(message)
    local n
    repeat
        message, n = message:gsub("<LINE>(%s*)<LINE>%s*<LINE>", "<LINE>%1<LINE>")
    until n == 0
    repeat
        message, n = message:gsub("%s*<LINE>%s*$", "")
    until n == 0
    return message
end

local baseUpdateTooltip = ISSkillProgressBar.updateTooltip

function ISSkillProgressBar:updateTooltip(lvlSelected)
    baseUpdateTooltip(self, lvlSelected)

    local perk = self.perk
    if not self.message or not perk or not self.char then return end

    local perkType = perk:getType()
    local xp = self.char:getXp()
    local message = self.message

    -- Vanilla builds the description key from getName(), which is *translated*.
    -- In English it happens to equal getId() and the key resolves; in Spanish it
    -- asks for IGUI_perks_Cocina_Description and prints that raw string on
    -- screen. Fixed regardless of the XP toggle: it is a vanilla bug, not our
    -- feature, and leaving it on would look like ours.
    -- This is also what makes the per-level keys reachable outside English,
    -- which the whole of phase 9 depends on.
    local badKey = "IGUI_perks_" .. perk:getName() .. "_Description"
    local goodKey = "IGUI_perks_" .. AllInfoChar.descriptionName(perk) .. "_Description"

    -- getText() echoes the key back when it cannot resolve it, so finding the
    -- literal key inside the message *is* the test for "vanilla failed here".
    -- Two separate vanilla bugs land on this line: the translated-name key, and
    -- perks that simply have no description key in any language (Sprinting is
    -- one). Both print raw text on screen; neither is ours to show.
    -- The per-level line wins over the generic one. Vanilla's blurb for a weapon
    -- skill is "increases attack speed and damage", which is exactly what the
    -- numbers underneath already say, so keeping both is noise.
    -- Used to be getTextOrNull(goodKey .. level), one of 60 hand-written keys.
    -- Those are gone: the weapon skills derive their line now (see
    -- character/SkillLevels.lua) and the nine other skills still have theirs.
    -- It still lands here rather than in `extra` because it has to *replace*
    -- vanilla's generic blurb, which for a weapon skill says "increases attack
    -- speed and damage" -- exactly what the figures below spell out.
    -- Tracked apart from levelText: vanilla appends this very key's text itself,
    -- below the description, so the branch further down has to tell "vanilla
    -- already printed a level line" from "ours would be the only one".
    local keyed = getTextOrNull(goodKey .. (lvlSelected + 1))
    if keyed == "" then keyed = nil end
    local levelText = keyed

    -- Sin opcion propia: no la tuvo nunca de verdad. Apagarla no quitaba la
    -- linea, cambiaba la derivada por la frase generica de vanilla ("increases
    -- attack speed and damage"), que dice lo mismo peor y sin cifras. Un
    -- interruptor que elige entre dos textos igual de presentes no es un
    -- interruptor. La seccion Personaje ya se apaga entera con su maestro.
    -- Two derived sources, tried in order: the six weapon skills, then the
    -- twenty of the Agriculture, Crafting and Survivalist trees. A perk that
    -- belongs to neither falls through to vanilla's own blurb.
    if not levelText then
        local fine, derived = pcall(AllInfo.SkillLevels.describe, perk, lvlSelected + 1)
        if not fine then
            print("[AllInfo] skill levels disabled: " .. tostring(derived))
            AllInfo.SkillLevels.describe = function() return nil end
        else
            levelText = derived
        end
    end

    if not levelText and AllInfo.SkillLevels.craft then
        local fine, derived = pcall(AllInfo.SkillLevels.craft, perk, lvlSelected + 1)
        if not fine then
            print("[AllInfo] craft skill levels disabled: " .. tostring(derived))
            AllInfo.SkillLevels.craft = nil
        else
            levelText = derived
        end
    end

    local at = message:find(badKey, 1, true)
    if at then
        local replacement = levelText or getTextOrNull(goodKey)

        if replacement then
            message = message:sub(1, at - 1) .. replacement .. message:sub(at + #badKey)
        else
            -- Nothing to say: drop the line vanilla appended, blank lines too.
            local whole = " <LINE><LINE> " .. badKey
            local from = message:find(whole, 1, true)
            if from then
                message = message:sub(1, from - 1) .. message:sub(from + #whole)
            else
                message = message:sub(1, at - 1) .. message:sub(at + #badKey)
            end
        end
    elseif levelText then
        -- Vanilla resolved the generic description itself, which only happens
        -- when the perk's display name equals its key: the English case.
        -- It also appends its own per-level line there, but *only* for the nine
        -- skills that still ship a Description<n> key. The six weapon skills
        -- lost theirs when they went derived in 0.9.19, and the twenty craft
        -- ones never had any, so cutting the blurb and trusting vanilla to
        -- print underneath left those levels saying nothing at all in English.
        -- Swap the blurb for the derived line, or just cut it when vanilla did
        -- print one below.
        local generic = getTextOrNull(goodKey)
        local from = generic and message:find(generic, 1, true)
        if from then
            message = message:sub(1, from - 1) .. (keyed and "" or levelText)
                .. message:sub(from + #generic)
        end
    end

    -- Our own lines are collected first and appended in one go, after a blank
    -- line: the description above is prose and this is a table of figures, so
    -- they read as two blocks rather than one run-on paragraph.
    local extra = {}

    if AllInfo.enabled("XpMultiplierFix") then
        -- Vanilla's own boost line goes: wrong number, and it is where ours
        -- belongs. IGUI_XP_tooltipxpboost is "XP Boost: +%1" with the '+' baked
        -- in, so the key cannot be reused with a different argument either.
        local boost = xp:getPerkBoost(perkType)
        local percent = VANILLA_PERCENT[boost]
        if percent then message = cutText(message, getText("IGUI_XP_tooltipxpboost", percent)) end

        -- The separate "Multiplier: 5" line goes too: that is the book you are
        -- reading, and it is folded into the single figure below. AddXP applies
        -- it on top of the boost factor (`if m > 1 then xp = xp * m`), so they
        -- multiply, and two numbers for one thing is worse than one.
        local book = xp:getMultiplier(perkType)
        if book and book > 0 then
            message = cutText(message, getText("IGUI_skills_Multiplier", round(book, 2)))
        end

        local total = AllInfoChar.xpRelative(perkType, boost) or 1
        if book and book > 1 then total = total * book end

        if total ~= 1 then
            extra[#extra + 1] = getText("UI_AllInfo_XpBoost", "x " .. AllInfo.num(total, 2))
        end
    end

    -- What this level gates, derived from the script manager. Last, because it
    -- is the longest line and the only one that can run to several rows.
    -- Isolated: a broken sweep must not take the whole tooltip with it.
    -- `perk`, not `perkType`: the index is keyed on Perk.getId(), which is the
    -- same key descriptionName() builds the description from, so the two lines
    -- can never end up talking about different skills.
    local ok, recipes = pcall(AllInfoChar.recipeLine, perk, lvlSelected + 1)
    if not ok then
        print("[AllInfo] skill recipes disabled: " .. tostring(recipes))
        AllInfoChar.recipeLine = function() return nil end
    elseif recipes then
        extra[#extra + 1] = recipes
    end

    -- Progress through the level, on the title line vanilla already wrote:
    -- "Long Blunt level 6, 73%". The two figures are the ones vanilla divides
    -- in render() to fill the bar, so this adds no reading of its own.
    --
    -- Only on the level in progress. An unlocked level is always at 100 and a
    -- locked one always at 0, and vanilla says "unlocked"/"locked" there
    -- anyway, so a percentage on those two is a number that never moves.
    --
    -- Inserted before the first <LINE> rather than appended: everything after
    -- that separator is a row of its own, and this belongs to the title.
    -- No option of its own, same reasoning as the XP line below: the Character
    -- section master already covers it.
    if self.level == lvlSelected and self.xpForLvl and self.xpForLvl > 0 then
        local head = message:find(" <LINE>", 1, true)
        if head then
            message = message:sub(1, head - 1) .. " - "
                .. AllInfo.pct(self.xp / self.xpForLvl) .. message:sub(head)
        end
    end

    message = AllInfoChar.tidyTooltip(message)
    if #extra > 0 then
        message = message .. " <LINE><LINE> " .. table.concat(extra, " <LINE> ")
    end

    self.message = message
end

-- 3) Player stats panel ------------------------------------------------------
-- loadPerks stores the percentage as a plain string on each row, so the rows
-- are rewritten after it has built them. Its boost-0 case prints "50%", which
-- is wrong in a third way: no boost is the baseline, not half of anything.
local baseLoadPerks = ISPlayerStatsUI.loadPerks

ISPlayerStatsUI.loadPerks = function(self)
    baseLoadPerks(self)
    if not AllInfo.enabled("XpMultiplierFix") then return end

    local items = self.xpListBox and self.xpListBox.items
    if not items then return end

    for i = 1, #items do
        local row = items[i].item
        if row and row.perk then
            local boost = self.char:getXp():getPerkBoost(row.perk)
            row.boost = AllInfoChar.xpRelativeText(row.perk, boost) or "x 1"
        end
    end
end

AllInfo.hooks = AllInfo.hooks or {}
AllInfo.hooks.XpBoostMap = CharacterCreationProfession.drawXpBoostMap
AllInfo.hooks.XpSkillTooltip = ISSkillProgressBar.updateTooltip
AllInfo.hooks.XpStatsPanel = ISPlayerStatsUI.loadPerks
