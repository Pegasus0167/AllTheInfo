require "AllInfo/Core"

-- Corpse-sickness protection from masks.
--
-- Clothing.getCorpseSicknessDefense():
--     if getCondition() <= 0            -> 0
--     base = script CorpseSicknessDefense
--     if hasFilter():
--         def = 25                                    (basicMaskDefense)
--         if getUsedDelta() > 0:                      (filter still has charge)
--             def = 85 if IMPROVISED_GAS_MASK else 100
--         base = max(base, def)
--
-- BodyDamage.UpdateIllness applies it as: rate *= max(0, 1 - def/100).
--
-- Never call IsoGameCharacter.getCorpseSicknessDefense(float, boolean): with
-- true it consumes the filter. The Clothing getter is read-only.

AllInfo.Mask = AllInfo.Mask or {}

-- ZomboidGlobals.corpseSicknessFilterDrainMultiplier, loaded from
-- media/lua/shared/defines.lua. ZomboidGlobals is not exposed to Lua, so this
-- one number cannot be read back.
-- ponytail: mirrors a define, re-check on each PZ update.
local FILTER_DRAIN = 0.3

-- In-game hours the filter has left, and the corpse count driving that.
--
-- The filter does not run down with time, it runs down with *exposure*:
-- BodyDamage.UpdateIllness() calls getCorpseSicknessDefense(base, true), which
-- drains `base * 0.3 * filter.UseDelta * GameTime.getMultiplier()`. `base` is
-- GetBaseCorpseSickness(), zero at five corpses or fewer, so a mask worn in the
-- woods lasts forever and one worn over a pile lasts minutes. There is no
-- single "duration" to print, only the pace right now, same as the food rows.
--
-- The multiplier is inside drainGasMask, not in its caller, so the drain is
-- steady in game time and does not ride on the frame rate. One in-game hour is
-- 120 * dayLength multiplier units (see character/Health.lua).
--
-- Returns the hours left and the corpse count. With no exposure the hours come
-- back nil and the count still comes back, because "nothing is being spent" is
-- itself the answer there: dropping the row entirely made it look like the mod
-- had lost track of the filter.
function AllInfo.Mask.filterHours(item, chr)
    if not chr then return nil end

    local body = chr:getBodyDamage()
    local base = body and body:GetBaseCorpseSickness()
    if not base then return nil end
    if base <= 0 then return nil, 0 end

    local filter = item:getFilterType()
    local script = filter and getScriptManager():getItem(filter)
    local useDelta = script and script:getUseDelta()
    if not useDelta or useDelta <= 0 then return nil end

    local day = getSandboxOptions():getDayLengthMinutes()
    if not day or day <= 0 then return nil end

    local perHour = base * FILTER_DRAIN * useDelta * 120 * day
    if perHour <= 0 then return nil end

    -- Shared with the Nauseous moodle, which shows the same count without a mask
    -- in hand. Nil here rather than 0: this branch already returned above when
    -- there was no exposure, so a zero would be a contradiction.
    return item:getUsedDelta() / perHour, AllInfo.corpseCount(chr)
end

-- Colour comes from the comparison and nothing else, like every other clothing
-- row: white on its own, green or red only against the mask you are wearing.
-- A fixed threshold painted 25% red, which reads as "this mask is broken" when
-- 25% is simply what a filterless mask gives you.
AllInfo.register("Mask", 95, nil, function(out, item, chr)
    if not instanceof(item, "Clothing") then return end

    local defense = item:getCorpseSicknessDefense()
    if not defense or defense <= 0 then return end   -- no protection, or broken

    local other = AllInfo.replacedClothing(item, chr)

    -- BodyDamage.UpdateIllness turns this into rate *= max(0, 1 - def/100), but
    -- one number says it well enough: 100% defense is immunity.
    AllInfo.rowIf(out, "MaskDefense", getText("Tooltip_AllInfo_CorpseDefense"),
        AllInfo.num(defense, 0) .. "%", nil,
        AllInfo.delta(defense, other and other:getCorpseSicknessDefense(), true, 0, "%"))

    -- Filter charge, when the mask takes one at all.
    if item:hasFilter() then
        local used = item:getUsedDelta()
        if used ~= nil then
            AllInfo.rowIf(out, "MaskCharge", getText("Tooltip_AllInfo_FilterCharge"),
                AllInfo.pct(used, 0), nil,
                AllInfo.deltaPct(used, other and other:hasFilter() and other:getUsedDelta(),
                    true, 0))

            local hours, corpses = AllInfo.Mask.filterHours(item, chr)
            local left = hours and AllInfo.duration(hours * 60)

            if left and corpses then
                left = left .. "  ("
                    .. getText("UI_AllInfo_mask_Corpses", AllInfo.num(corpses, 0)) .. ")"
            elseif not left and corpses then
                -- No exposure: the filter is not running down at all, and
                -- saying so is more useful than a blank where a row was.
                left = getText("UI_AllInfo_mask_NotDraining", AllInfo.num(corpses, 0))
            end

            if left then
                AllInfo.rowIf(out, "MaskLeft", getText("UI_AllInfo_mask_FilterLeft"), left)
            end
        end
    end
end)
