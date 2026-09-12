require "AllInfo/Core"

-- Tapes and CDs: what a recording actually teaches you before you play it.
--
-- Each line of a MediaData carries a comma-separated "codes" string:
--   XXX+N  skill XP      RCP=Name  recipe taught
--   BOR-N  boredom       STS+N     stress        FAT  fatigue
--
-- Vanilla's own mapping (ISRadioInteractions.lua) is a table of *functions*,
-- so the code -> perk pairs have to be mirrored here.
-- ponytail: mirrors ISRadioInteractions, re-check on each PZ update.
local CODE_TO_PERK = {
    CRP = Perks.Woodwork,  COO = Perks.Cooking,   FRM = Perks.Farming,
    DOC = Perks.Doctor,    ELC = Perks.Electricity, MTL = Perks.MetalWelding,
    MEC = Perks.Mechanics, TAI = Perks.Tailoring, FIS = Perks.Fishing,
    TRA = Perks.Trapping,  FOR = Perks.PlantScavenging, HUS = Perks.Husbandry,
    FKN = Perks.FlintKnapping, CRV = Perks.Carving, BLA = Perks.Blacksmith,
    POT = Perks.Pottery,   GLA = Perks.Glassmaking, MAS = Perks.Masonry,
    BUT = Perks.Butchering, TRK = Perks.Tracking, AIM = Perks.Aiming,
    REL = Perks.Reloading, BAA = Perks.Axe,       BUA = Perks.Blunt,
    SBU = Perks.SmallBlunt, LBA = Perks.LongBlade, SBA = Perks.SmallBlade,
    SPE = Perks.Spear,     SPR = Perks.Sprinting, LFT = Perks.Lightfoot,
    NIM = Perks.Nimble,    SNE = Perks.Sneak,
}

-- ISRadioInteractions.doSkill(): "local amount = 50*_amount". The number in the
-- code is a multiplier, not the XP itself.
-- ponytail: hardcoded in vanilla Lua, re-check on each PZ update.
local XP_PER_CODE = 50

AllInfo.register("RecordedMedia", 100, nil, function(out, item, chr)
    local media = item:getMediaData()
    if not media then return end

    local lineCount = media:getLineCount()
    if not lineCount or lineCount <= 0 then return end

    -- Only unheard lines still pay out, so the progress check has to come
    -- first: a half-watched tape must not advertise XP it already gave.
    local recorded
    do
        local ok, value = pcall(function() return getZomboidRadio():getRecordedMedia() end)
        recorded = ok and value or nil
    end

    -- Called through a closure, never as pcall(obj.method, ...): indexing a
    -- Java method as a field yields nil and blows up outside the pcall.
    local function alreadyHeard(line)
        if not recorded or not chr or not line then return false end
        local ok, heard = pcall(function()
            return recorded:hasListenedToLine(chr, line:getTextGuid())
        end)
        return ok and heard or false
    end

    local xpByPerk, recipes = {}, {}
    local heardCount = 0

    for i = 0, lineCount - 1 do
        local line = media:getLine(i)
        local codes = line and line:getCodes()

        local heard = alreadyHeard(line)
        if heard then heardCount = heardCount + 1 end

        if codes and codes ~= "" and not heard then
            for code in codes:gmatch("[^,]+") do
                code = code:match("^%s*(.-)%s*$")

                local perkCode, amount = code:match("^(%a%a%a)%+(%d+)$")
                if perkCode and CODE_TO_PERK[perkCode] then
                    xpByPerk[perkCode] = (xpByPerk[perkCode] or 0) + tonumber(amount)
                end

                local recipe = code:match("^RCP=(.+)$")
                if recipe then recipes[#recipes + 1] = recipe end
            end
        end
    end

    -- XP still on offer, one row per skill.
    --
    -- ISRadioInteractions.doSkill() multiplies the code amount by 50, so a
    -- "COO+1" line is worth 50 XP, not 1. It also refuses to grant anything
    -- once the character reaches SandboxVars.LevelForMediaXPCutoff.
    --
    -- Perk.getName() returns the *translated* name, so "IGUI_perks_"..getName()
    -- builds a key that exists in no language. getId() is the internal one.
    local cutoff = AllInfo.gameSandbox("LevelForMediaXPCutoff", nil)

    for perkCode, codeTotal in pairs(xpByPerk) do
        local perk = CODE_TO_PERK[perkCode]
        local label = getText("IGUI_perks_" .. perk:getId())

        local capped = chr and type(cutoff) == "number"
            and chr:getPerkLevel(perk) >= cutoff

        if capped then
            AllInfo.rowIf(out, "MediaXp", label, getText("Tooltip_AllInfo_NoMoreXp"), AllInfo.color(false))
        else
            AllInfo.rowIf(out, "MediaXp", label, "+" .. (codeTotal * XP_PER_CODE) .. " XP", AllInfo.color(true))
        end
    end

    -- One recipe per row, same shape as the ammo weapon list.
    local unknown = {}
    for i = 1, #recipes do
        if not chr or not chr:isRecipeActuallyKnown(recipes[i]) then
            unknown[#unknown + 1] = getTextOrNull("Recipe_" .. recipes[i]) or recipes[i]
        end
    end

    if #unknown > 0 then
        table.sort(unknown)
        for i = 1, #unknown do
            AllInfo.rowIf(out, "MediaRecipes",
                i == 1 and getText("Tooltip_AllInfo_TeachesRecipes") or "",
                unknown[i], AllInfo.color(true))
        end
    end

    -- Boredom and stress are dropped on purpose: vanilla already covers the
    -- mood side of media, and what it never tells you is the XP and recipes.

    if recorded and chr then
        AllInfo.rowIf(out, "MediaWatched", getText("Tooltip_AllInfo_Watched"),
            heardCount .. " / " .. lineCount, AllInfo.color(heardCount >= lineCount))
    end
end)
