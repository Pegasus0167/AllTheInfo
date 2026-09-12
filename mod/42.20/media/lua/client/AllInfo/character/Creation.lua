require "AllInfo/character/Core"
require "OptionScreens/CharacterCreationProfession"

-- Trait and profession blocks in the character creation screen.
--
-- Every list entry stores its own tooltip (ISScrollingListBox:addItem's third
-- argument *is* entry.tooltip, and the profession and chosen-trait lists assign
-- it by hand), so one pass over list.items covers every path without
-- intercepting addItem.
--
-- The pass runs from prerender rather than from the populate* functions,
-- because those are not the only writers: addTrait() puts the entry straight
-- into listboxTraitSelected with `trait:getDescription()` as its tooltip, and so
-- do onSelectProf() for the free traits of a profession and the saved-build
-- presets. Wrapping the four populate* entry points left a trait you had just
-- clicked showing vanilla's bare description until something else rebuilt the
-- list -- picking a different profession, which is exactly the "sometimes it
-- fixes itself" in the report. prerender is downstream of all of them.
--
-- ⚠️ Plain "\n", never " <LINE> ": controller mode rewrites these tooltips and
-- turns newlines into " <SPACE> ". MoreDescriptionForTraits4166 clones 44 KB of
-- this screen to do the same job; this only wraps.

-- The four lists that carry a definition. No per-list flag any more: the block
-- itself no longer repeats anything vanilla prints (see character/Core.lua),
-- so every list gets the same one.
local LISTS = { "listboxProf", "listboxTraitSelected", "listboxTrait", "listboxBadTrait" }

local function addBlocks(list)
    if not list or not list.items then return end

    for i = 1, #list.items do
        local entry = list.items[i]
        -- The flag matters: the lists are not cleared before being refilled, so
        -- without it every frame would stack another copy of the block.
        if entry.item and not entry.allInfoBlock then
            entry.tooltip = AllInfoChar.appendBlock(entry.tooltip, entry.item, "\n")
            entry.allInfoBlock = true
        end
    end
end

local function addAllBlocks(self)
    if not AllInfo.enabled("TraitInfoCreation") then return end
    for i = 1, #LISTS do addBlocks(self[LISTS[i]]) end
end

-- Runs every frame, so it switches itself off for the session on first error
-- instead of filling the log.
local broken = false

local basePrerender = CharacterCreationProfession.prerender

function CharacterCreationProfession:prerender(...)
    local result = basePrerender(self, ...)

    if not broken then
        local ok, err = pcall(addAllBlocks, self)
        if not ok then
            broken = true
            print("[AllInfo] trait block disabled: " .. tostring(err))
        end
    end

    return result
end

AllInfo.hooks = AllInfo.hooks or {}
AllInfo.hooks.TraitCreationPrerender = CharacterCreationProfession.prerender
