require "AllInfo/character/Core"
require "XpSystem/ISUI/ISCharacterScreen"

-- The same blocks in the in-game character info tab.
--
-- Separator is "\n" here too. The plan said "<br>", but loadTraits itself does
-- `setMouseOverText(label .. "\n" .. description)`, so newlines are what this
-- surface already speaks.

local baseLoadTraits = ISCharacterScreen.loadTraits

ISCharacterScreen.loadTraits = function(self)
    baseLoadTraits(self)
    if not AllInfo.enabled("TraitInfoScreen") or not self.traits then return end

    for _, image in ipairs(self.traits) do
        -- loadTraits stores the definition on the image and setMouseOverText
        -- keeps its text in mouseovertext, both plain Lua fields.
        if image.trait then
            image:setMouseOverText(AllInfoChar.appendBlock(image.mouseovertext, image.trait, "\n"))
        end
    end
end

-- loadProfession only puts the profession's *name* in self.profession, which
-- render() hands to profImage:setMouseOverText. So the block is the only thing
-- this tooltip has ever said beyond the name.
local baseLoadProfession = ISCharacterScreen.loadProfession

ISCharacterScreen.loadProfession = function(self)
    baseLoadProfession(self)
    if not AllInfo.enabled("TraitInfoScreen") or not self.profession then return end

    -- With no texture, render() draws self.profession as plain text next to the
    -- name instead of hanging it off the icon, and a multi-line block there
    -- would spill across the panel. Vanilla professions all have one; a modded
    -- one might not.
    if not self.professionTexture then return end

    local descriptor = self.char and self.char:getDescriptor()
    local profession = descriptor and descriptor:getCharacterProfession()
    if not profession then return end

    -- `full`, and this is the only caller that passes it. render() hands
    -- setMouseOverText nothing but getUIName(), so unlike every other surface
    -- the profession's description -- and with it the "+N Skill" lines vanilla
    -- appends to it, plus its granted traits -- never reaches the screen. Here
    -- the block is the only thing that can state them.
    local def = CharacterProfessionDefinition.getCharacterProfessionDefinition(profession)
    if def then self.profession = AllInfoChar.appendBlock(self.profession, def, "\n", true) end
end

AllInfo.hooks = AllInfo.hooks or {}
AllInfo.hooks.TraitInfoScreen = ISCharacterScreen.loadTraits
AllInfo.hooks.ProfInfoScreen = ISCharacterScreen.loadProfession
