require "AllInfo/Core"

-- Charge, autonomy and light of anything that runs down: drainables on one
-- clock, battery-powered radios on another.
--
-- Vanilla draws the charge as a bar with no number on it (ISInventoryPane.lua,
-- drawTextAndProgressBar(text, item:getCurrentUsesFloat(), ...), and the radio
-- panel's own battery widget); the percentage only shows up in two stray context
-- menus, never in the tooltip. How long the thing lasts, and how far it lights,
-- are printed nowhere at all.
--
-- Clock 1, verified in DrainableComboItem.update() (offsets 587-644):
--
--     if (owner instanceof IsoPlayer && canBeActivated() && isActivated()
--         && (player.isHandItem(this) || player.isAttachedItem(this))) {
--         int bucket = (GameTime.getMinutes() / 10) * 10;
--         if (bucket != lastUpdateMinutes) {
--             if (lastUpdateMinutes > -1) Use(false, false, GameClient.client);
--             lastUpdateMinutes = bucket;
--         }
--     }
--
-- So one UseDelta per *ten* game minutes, and only while the item is in a hand
-- or attached: the else branch of that same method switches off a torch that
-- ends up in a bag. A full HandTorch (UseDelta 0.006) therefore lasts 27.8 game
-- hours.
--
-- Clock 2, verified in DeviceData.update(boolean, boolean) (offsets 0-175):
-- the method ticks off GameTime.getMinutesStamp() against lastMinuteStamp and
-- then, for a device that is on and running off a battery, does
--
--     setPower(powerDelta - useDelta * minutesElapsed);
--
-- which is one UseDelta per *single* minute. A WalkieTalkie1 (UseDelta 0.007)
-- lasts 2h23m on a full battery, not 27 hours: the two clocks are a factor of
-- ten apart and must never share an arithmetic line. SelfTest asserts both.
--
-- TicksPerEquipUse is dead in B42.20: nothing outside DrainableComboItem and the
-- item script ever reads it. It plays no part in any of this.
local MINUTES_PER_USE = 10

AllInfo.Power = AllInfo.Power or {}

-- Minutes left on a battery-powered device. Kept on the module so SelfTest can
-- assert the arithmetic without a radio that happens to have a battery in it.
function AllInfo.Power.deviceMinutes(power, delta)
    if not power or not delta or delta <= 0 then return nil end
    return power / delta        -- no x10 here: that is clock 1, not this one
end

local function drainable(item)
    return item and instanceof(item, "DrainableComboItem") and item or nil
end

-- How wide the beam is, in degrees, or nil for a light that is not a cone.
--
-- IsoGridSquare's torch pass normalises the vector to the square, normalises the
-- direction the character faces, takes Vector2.dot of the two and tests it
-- against +/- TorchInfo.dot, which TorchInfo.set() copies from the item. A dot
-- product of two unit vectors compared against a constant is a cone of
-- half-angle acos(constant) by construction, so the beam is twice that. The
-- vanilla figures come out at 120 degrees for the hand torch and the angle-head,
-- 116 for the army one, 97 for the heavy duty and the crafted, and 83 for the
-- penlight.
--
-- TorchCone = false takes the other branch of that test entirely: the hurricane
-- lanterns light around themselves and have no angle at all, which is why they
-- get a word instead of a number.
--
-- ponytail: the lighting that ships runs through the native updateTorch(), which
-- cannot be read. The Java pass above is the same two fields under the same
-- test, and the gap it draws between the hand torch and the penlight is wide
-- enough to check by eye with both switched on.
local function torchBeam(item)
    if not item:isTorchCone() then return nil end

    -- getTorchDot() reads scriptItem.torchDot with no guard of its own, and the
    -- script leaves the field out on everything that is not a cone.
    local dot = item:getTorchDot()
    if type(dot) ~= "number" or dot <= -1 or dot >= 1 then return nil end

    return math.deg(math.acos(dot)) * 2
end

-- Radio is the only InventoryItem implementing WaveSignalDevice, so it covers
-- radios, walkie-talkies and televisions alike. Off the battery there is nothing
-- to report: DeviceData only spends powerDelta when isBatteryPowered is set, and
-- a device on the mains keeps running with powerDelta at zero.
local function device(item)
    if not item or not instanceof(item, "Radio") then return nil end

    local data = item:getDeviceData()
    if not data or not data:getIsBatteryPowered() then return nil end
    return data
end

AllInfo.register("Power", 55, nil, function(out, item, chr)
    local compare = AllInfo.compareTo(item, chr)

    if drainable(item) then
        local other = drainable(compare)

        -- Charge. Every drainable gets this row: propane, paint and duct tape
        -- have no number in the tooltip either.
        local charge = item:getCurrentUsesFloat()
        AllInfo.rowIf(out, "PowerLeft", getText("IGUI_invpanel_Remaining"),
            AllInfo.pct(charge, 0), nil,
            AllInfo.deltaPct(charge, other and other:getCurrentUsesFloat(), true, 0))

        -- Autonomy, only for the family that actually has a clock. A tin of
        -- paint does not run down with time, so giving it a duration would be
        -- a lie.
        local function life(it)
            if not it:canBeActivated() then return nil end
            local delta = it:getUseDelta()
            if not delta or delta <= 0 then return nil end
            return it:getCurrentUsesFloat() / delta * MINUTES_PER_USE
        end

        local minutes = life(item)
        if minutes then
            local text = AllInfo.duration(minutes)
            if text then
                AllInfo.rowIf(out, "PowerLife", getText("Tooltip_AllInfo_PowerLife"), text, nil,
                    AllInfo.delta(minutes, other and life(other), true, 0))
            end
        end

        -- Light. IsoGameCharacter$TorchInfo.set() copies these two straight from
        -- the item, and IsoPlayer.getTorchStrength() returns getLightStrength()
        -- with nothing else on top: the script figure is the one that lights the
        -- ground.
        local dist = item:getLightDistance()
        if dist and dist > 0 then
            AllInfo.rowIf(out, "LightDistance", getText("Tooltip_AllInfo_LightDistance"),
                AllInfo.num(dist, 0), nil,
                AllInfo.delta(dist, other and other:getLightDistance(), true, 0))

            local strength = item:getLightStrength()
            AllInfo.rowIf(out, "LightStrength", getText("Tooltip_AllInfo_LightStrength"),
                AllInfo.num(strength, 2), nil,
                AllInfo.delta(strength,
                    other and other:getLightDistance() > 0 and other:getLightStrength(),
                    true, 2))

            -- Beam. Every light is either a cone you aim or a lamp that lights
            -- all around, and vanilla says neither. The unit rides on the label,
            -- same as "Reach (tiles)": no degree sign in the value, so nothing
            -- depends on the font having one.
            local beam = torchBeam(item)
            AllInfo.rowIf(out, "LightBeam", getText("Tooltip_AllInfo_LightBeam"),
                beam and AllInfo.num(beam, 0)
                    or getText("Tooltip_AllInfo_LightBeamAll"),
                nil,
                -- Cone against cone only. A lantern has no angle to compare
                -- against, and calling it 360 would be a number nothing in the
                -- game supports.
                AllInfo.delta(beam, other and torchBeam(other), true, 0))
        end
    end

    local data = device(item)
    if data then
        local other = device(compare)

        local power = data:getPower()
        AllInfo.rowIf(out, "PowerLeft", getText("IGUI_invpanel_Remaining"),
            AllInfo.pct(power, 0), nil,
            AllInfo.deltaPct(power, other and other:getPower(), true, 0))

        local minutes = AllInfo.Power.deviceMinutes(power, data:getUseDelta())
        local text = minutes and AllInfo.duration(minutes)
        if text then
            AllInfo.rowIf(out, "PowerLife", getText("Tooltip_AllInfo_PowerLife"), text, nil,
                AllInfo.delta(minutes,
                    other and AllInfo.Power.deviceMinutes(other:getPower(), other:getUseDelta()),
                    true, 0))
        end
    end
end)
