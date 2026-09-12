require "AllInfo/Core"

-- Days until stale and rotten.
--
-- Food.updateAge() does: age += elapsedHours * foodRotSpeed / 24, with the
-- elapsed hours scaled by fridgeFactor inside a powered fridge, and no ageing
-- at all while frozen. offAge and offAgeMax are in days, so the remaining time
-- is simply (threshold - age) / rate.
--
-- getFoodRotSpeed() and getFridgeFactor() are private in Java, so the two
-- tables below mirror them.
-- ponytail: mirrors private Java methods, re-check on each PZ update.
local ROT_SPEED = { 1.7, 1.4, 1.0, 0.7, 0.4 }
local FRIDGE_FACTOR = { 0.4, 0.3, 0.2, 0.1, 0.03, 0.0 }

local NEVER_ROTS = 1000000000   -- Food.updateAge() treats offAge >= 1e9 as "never"

-- Decay per in-game day where the item currently sits, mirroring updateAge():
--
--   if isFrozen()                 -> elapsed hours *= 0     (does not age, ever)
--   else if fridge or freezer:
--        if powered               -> elapsed hours *= fridgeFactor
--
-- A freezer is not a special case: powered, it slows food by exactly the same
-- fridgeFactor as a fridge. What stops decay is isFrozen(), which updateFreezing
-- flips only after the food has actually frozen through.
-- A fridge keeps cooling even when its square reports no electricity. When
-- haveElectricity() is false, updateAge() falls back to ElecShutModifier: the
-- world-wide grid is still up until worldAgeHours reaches shutDay * 24, and
-- until then the food is still chilled.
--
-- Careful: an appliance that visibly does *not* work still preserves food.
-- Whether it runs is ItemContainer.isPowered() -> IsoGridSquare.hasGridPower(),
-- which also demands !isNoPower() (a NoPower zone, a derelict room, or a room
-- the player built himself). updateAge() asks none of that: fridge or freezer
-- plus a live grid is all it wants. So a fridge in your own base never chills
-- or freezes anything and still slows rotting by the full fridgeFactor. That
-- is vanilla, verified in B42.20 bytecode, and this row reports it.
--
-- ponytail: reports the rate as it is right now. updateAge() blends the cooled
-- and uncooled rates across the exact hour the grid dies; a tooltip that
-- refreshes twice a second does not need that.
local function isCooling(container)
    local square = container:getSourceGrid()
    if square and square:haveElectricity() then return true end

    local options = getSandboxOptions and getSandboxOptions()
    if not options then return false end

    local shutDay = options:getElecShutModifier()
    if shutDay <= -1 then return false end   -- -1 means "power never goes out"

    local time = getGameTime()
    local worldAge = time and time:getWorldAgeHours()
    return worldAge ~= nil and worldAge < shutDay * 24
end

-- Deliberately ignores isFrozen(). Frozen food does not age at all, but the
-- answer the player wants is "how long once it thaws", and that is this rate:
-- the one of the spot the item is sitting in right now. Whether it is frozen
-- only picks the label, in spoilRows().
local function rateOf(item)
    local rate = ROT_SPEED[AllInfo.gameSandbox("FoodRotSpeed", 3)] or 1.0

    local container = item:getOutermostContainer()
    if container and (container:isFridge() or container:isFreezer()) and isCooling(container) then
        rate = rate * (FRIDGE_FACTOR[AllInfo.gameSandbox("FridgeFactor", 3)] or 0.2)
    end

    return rate
end

local function spoilRows(out, item)
    -- Vanilla already labels rotten food. Nothing to add.
    if item:isRotten() then return end

    local offAge, offAgeMax = item:getOffAge(), item:getOffAgeMax()
    if offAge <= 0 or offAge >= NEVER_ROTS then return end   -- never spoils

    local rate = rateOf(item)
    if rate <= 0 then return end   -- FoodRotSpeed out of range: no honest answer

    -- Frozen food does not age while it stays frozen, so saying "never" was
    -- true and useless: the player reads it as a property of the item and then
    -- watches it rot on the counter. The number stays, the label changes, and
    -- the missing "in" is what says the clock is stopped. Vanilla already
    -- writes "Frozen" right above.
    local frozen = item:isFrozen()
    local age = item:getAge()
    local hasRotStage = offAgeMax > 0 and offAgeMax < NEVER_ROTS

    local toStale = (offAge - age) / rate
    if toStale > 0 then
        local d = AllInfo.duration(toStale * 1440)
        if d then
            AllInfo.rowIf(out, "FoodStale", getText(frozen and "Tooltip_AllInfo_StaleThawed"
                or "Tooltip_AllInfo_Stale"), d)
        end
    end

    if hasRotStage then
        local toRotten = (offAgeMax - age) / rate
        if toRotten > 0 then
            local d = AllInfo.duration(toRotten * 1440)
            if d then
                -- Red only when it is stale *now*. Frozen, "already stale" is
                -- not a thing the player can act on until it thaws.
                AllInfo.rowIf(out, "FoodRots", getText(frozen and "Tooltip_AllInfo_RotsThawed"
                        or "Tooltip_AllInfo_Rots"), d,
                    (toStale <= 0 and not frozen) and AllInfo.color(false) or nil)
            end
        end
    end
end

AllInfo.register("Food", 10, nil, function(out, item, chr)
    if not instanceof(item, "Food") then return end
    spoilRows(out, item)
end)

-- Cooking time, and the temperature it assumes.
--
-- Food.update() adds heat/1.5 to cookingTime once per in-game minute and
-- nothing cooks below heat 1.6, so the time left is
-- (minutesToCook - cookingTime) / (heat / 1.5) at that temperature.
--
-- The row quotes the food at temperature, which is the honest answer to "how
-- long does this take". Getting there costs about four minutes more -- the food
-- heats at containerTemp/100 * 0.075 per in-game minute and only starts cooking
-- past heat 1.6, i.e. 60 C -- and that is what the CookingWarmUp option adds.
-- Four covers every appliance (4.1 min at 200 C, 4.5 on a barbecue); it does
-- not cover an electric oven switched on from cold, which spends another three
-- climbing its own ramp.
--
-- ponytail: flat constant instead of simulating the two ramps. The figure has
-- to be final while the player is still setting the dial -- one that jumps the
-- moment the oven lights is one nobody is looking at any more.
local WARM_UP = 4           -- minutes the food spends heating before it cooks
local COOK_HEAT = 1.6       -- Food.update(): at or below this nothing cooks
local MAX_HEAT = 3.0        -- updateTemperature() ceiling, i.e. 200 C
local PER_MINUTE = 1.5      -- Food.update(): cookingTime += heat / 1.5
local REFERENCE_C = 200     -- oven dial ceiling; nothing cooks faster

-- What the appliance reaches once it is running, by ItemContainer type. Only
-- consulted while the container is too cold to cook: once it is hot its own
-- temperature is the truth and the row follows it live.
--
-- ponytail: a player-built campfire is 70 C on fumes and 90 C well fed, but map
-- campfires are IsoFireplace at 80 and the container type does not tell the two
-- apart. 80 for the whole fire family, which reads a little long on a well fed
-- campfire and never short.
local CEILING = {
    microwave = 130,        -- ISMicrowaveUI dial: 50, 70, 90, 110, 130
    barbecue = 80,          -- IsoBarbecue / IsoFireplace: a flat 1.8 while lit
    barbecuepropane = 80,
    fireplace = 80,
    woodstove = 80,
    brazier = 80,
    campfire = 80,
}

local function toHeat(celsius) return celsius / 100 + 1 end
local function toCelsius(heat) return heat * 100 - 100 end

-- Temperature.* is exposed to Lua (LuaManager$Exposer) and honours the
-- player's Celsius/Fahrenheit option, postfix included -- which also keeps the
-- degree sign out of our own files.
local function atTemperature(celsius)
    return " (" .. Temperature.getRoundedDisplayTemperature(celsius)
        .. Temperature.getTemperaturePostfix() .. ")"
end

AllInfo.register("Cooking", 200, nil, function(out, item, chr)
    if not instanceof(item, "Food") then return end
    if not item:isIsCookable() or item:isBurnt() or item:isFrozen() then return end

    local cooked = item:isCooked()
    local goal = cooked and item:getMinutesToBurn() or item:getMinutesToCook()
    local left = goal - item:getCookingTime()
    if left <= 0 then return end

    -- Whatever it is sitting in, if that is warm enough to cook it drives the
    -- rate. Cold, quote what it will reach once it runs -- an oven timer is set
    -- before the oven is lit, so the figure has to hold from the start.
    local container = item:getOutermostContainer()
    local temp = container and container:getTemprature() or 0
    local goalC = REFERENCE_C
    if temp > COOK_HEAT then
        goalC = toCelsius(temp)
    elseif container then
        goalC = CEILING[container:getType()] or REFERENCE_C
    end

    local ceiling = math.min(MAX_HEAT, toHeat(goalC))
    local minutes = left / (ceiling / PER_MINUTE)

    -- Food already up to temperature has that wait behind it.
    if AllInfo.enabled("CookingWarmUp") and item:getHeat() < ceiling then
        minutes = minutes + WARM_UP
    end

    local d = AllInfo.duration(minutes)
    if not d then return end

    if cooked then
        -- Cooked and off the heat is done: nothing left to time.
        if temp <= COOK_HEAT then return end
        AllInfo.rowIf(out, "FoodBurning", getText("IGUI_invpanel_Burning"),
            d .. atTemperature(goalC), AllInfo.color(false))
    else
        AllInfo.rowIf(out, "FoodCooking", getText("Tooltip_AllInfo_CookingTime"),
            d .. atTemperature(goalC))
    end
end)

