require "AllInfo/Core"

-- Remaining reading time, in in-game hours and minutes.
--
-- ISReadABook:getDuration() works in action ticks, not minutes:
--     f    = 1 / getMinutesPerDay() / 2
--     time = pages * MinutesPerPage / f  =  pages * MinutesPerPage * mpd * 2
-- One in-game day lasts mpd real minutes, which at the reference rate is
-- mpd * 3600 ticks. So the time in in-game minutes is
--     time / (mpd * 3600) * 1440  =  pages * MinutesPerPage * 0.8
-- and minutesPerDay cancels out, which is what we want: how long a book takes
-- in game time must not depend on how long the player's day is.
local TICKS_TO_GAME_MINUTES = 0.8

-- Vanilla refuses to read a skill book that is too advanced or already
-- outgrown. Same test as ISInventoryPaneContextMenu.lua:1061-1068, so what we
-- report matches whether the "Read" option is actually there.
-- Returns a translation key, or nil when the book is readable.
local function uselessReason(item, chr)
    if not chr then return nil end

    local book = SkillBook and SkillBook[item:getSkillTrained()]
    local perk = book and book.perk
    if not perk then return nil end

    local level = chr:getPerkLevel(perk)

    if item:getLvlSkillTrained() ~= -1 and item:getLvlSkillTrained() > level + 1 then
        return "Tooltip_AllInfo_BookTooAdvanced"
    end
    if item:getMaxLevelTrained() ~= -1 and item:getMaxLevelTrained() <= level then
        return "Tooltip_AllInfo_BookOutgrown"
    end

    return nil
end

AllInfo.register("Books", 70, nil, function(out, item, chr)
    if not instanceof(item, "Literature") then return end

    local pages = item:getNumberOfPages()
    if pages <= 0 then return end

    local useless = uselessReason(item, chr)
    if useless then
        AllInfo.rowIf(out, "BookTime", getText("Tooltip_AllInfo_ReadingTime"),
            getText(useless), AllInfo.color(false))
        return
    end

    -- Page count is vanilla's job; we only add the time it implies.
    local read = 0
    if chr then read = chr:getAlreadyReadPages(item:getFullType()) or 0 end
    if read > pages then read = pages end

    local remaining = pages - read
    if remaining <= 0 then return end

    local perPage = AllInfo.gameSandbox("MinutesPerPage", 2.0)
    if type(perPage) ~= "number" or perPage < 0 then perPage = 2.0 end   -- vanilla's own guard

    local minutes = remaining * perPage * TICKS_TO_GAME_MINUTES

    -- Vanilla throws the page count away for these and uses a flat 50 ticks,
    -- which is near-instant. Same conversion, but mpd does not cancel out here.
    if item:hasTag(ItemTag.FAST_READ) then
        local mpd = getGameTime() and getGameTime():getMinutesPerDay()
        minutes = (mpd and mpd > 0) and (50 / (mpd * 3600) * 1440) or 0
    end

    -- Every modifier scales the *time taken*, so below 1 means faster. Vanilla
    -- applies them after the flat FAST_READ duration, and so do we.
    local timeFactor = 1.0
    if chr then
        if chr:hasTrait(CharacterTrait.FAST_READER) then timeFactor = timeFactor * 0.7 end
        if chr:hasTrait(CharacterTrait.SLOW_READER) then timeFactor = timeFactor * 1.3 end

        local eyes = chr:getWornItems():getItem(ItemBodyLocation.EYES)
        if eyes and eyes:getType() == "Glasses_Reading" then timeFactor = timeFactor * 0.9 end

        -- ISReadABook.lua:476-478 gives the same x0.9 on the ground or in a chair.
        if chr:isSitOnGround() or chr:isSittingOnFurniture() then timeFactor = timeFactor * 0.9 end
    end

    minutes = minutes * timeFactor

    -- Speed is the inverse of time taken: x0.7 time is 143% speed.
    --
    -- Always drawn, a flat 100% included, and it keeps its threshold colour
    -- while the weapon rows lost theirs. The rule is whether a delta is
    -- possible at all: this row describes the *character*, not the book, so two
    -- books under the cursor would read exactly the same and no comparison can
    -- ever exist. With nothing to compare against, the threshold is the only
    -- thing that can orient the player, same reasoning as the bed rows.
    -- 100% is neither, so it stays white instead of falling into the "bad" half
    -- of a two-way test.
    local speed = 1 / timeFactor
    AllInfo.rowIf(out, "BookSpeed", getText("Tooltip_AllInfo_ReadingSpeed"), AllInfo.pct(speed),
        speed ~= 1 and AllInfo.color(speed > 1) or nil)

    local d = AllInfo.duration(minutes)
    if d then AllInfo.rowIf(out, "BookTime", getText("Tooltip_AllInfo_ReadingTime"), d) end
end)
