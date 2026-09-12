require "AllInfo/Core"
require "ISUI/ISGeneratorInfoWindow"

AllInfo.GeneratorRange = AllInfo.GeneratorRange or {}

-- Outlines the area a generator actually powers on the floor, while its info
-- window is open. Replaces the textual range lines, which said the same thing
-- worse. Only the outer ring is drawn -- see RING below.
--
-- Where the numbers come from, all of it derived:
--   * horizontal radius: SandboxVars.GeneratorTileRange, the same var Java
--     reads into IsoGenerator.generatorRadius;
--   * vertical reach: getMinAffectedLevel()/getMaxAffectedLevel(), public and
--     already clamped to the world's z limits, so the reach shrinks correctly
--     on the top and bottom floors of the map;
--   * the covered test: the same one isPoweringSquare() runs, squared distance
--     between tile centres against radius squared;
--   * the filter: solid floor, and indoors unless AllowExteriorGenerator.
--
-- GeneratorRange (Workshop 2972289937) hardcodes 20 / 2 / 3, which was already
-- wrong for B42.20: the vertical reach is symmetric and sandbox-driven.

-- Only the floor the player is standing on is ever drawn -- the others are not
-- visible anyway -- so only that floor is ever computed. 41x41 squares instead
-- of 41x41x7, recomputed only when the generator, its state or the floor
-- changes.
local forObject, forZ, forState, squares

-- Thickness of the drawn ring, in tiles. Filling the whole disc buried the
-- floor under a wash of colour; the edge is the only part that answers the
-- question you actually have, which is where the power stops.
local RING = 3

local function coveredSquares(object, z)
    local radius = AllInfo.gameSandbox("GeneratorTileRange", nil)
    local origin = object:getSquare()
    if not radius or not origin then return nil end

    -- Outside the vertical reach nothing is covered, and that is a real answer.
    if z < object:getMinAffectedLevel() or z > object:getMaxAffectedLevel() then return {} end

    local exterior = AllInfo.gameSandbox("AllowExteriorGenerator", false)
    local gx, gy = origin:getX(), origin:getY()
    local limit = radius * radius
    -- A generator smaller than the ring is drawn solid: an empty highlight
    -- would be worse than a thick one.
    local inner = math.max(radius - RING, 0)
    inner = inner * inner
    local cell = getCell()
    local out = {}

    for x = gx - radius, gx + radius do
        for y = gy - radius, gy + radius do
            local d = IsoUtils.DistanceToSquared(x + 0.5, y + 0.5, gx + 0.5, gy + 0.5)
            if d <= limit and d > inner then
                -- getGridSquare, not getOrCreateGridSquare: an unloaded chunk
                -- is not on screen, and creating a couple of thousand squares
                -- to draw nothing is how the reference mod stutters.
                local sq = cell:getGridSquare(x, y, z)
                if sq and sq:isSolidFloor() and (exterior or not sq:isOutside()) then
                    out[#out + 1] = sq
                end
            end
        end
    end

    return out
end

function AllInfo.GeneratorRange.draw(window)
    local object = window.object
    if not object or not AllInfo.enabled("GeneratorHighlight") then return end

    -- playerNum comes off the window itself (ISGeneratorInfoWindow:new stores
    -- it), so this works in split screen and never touches getPlayer().
    local player = getSpecificPlayer(window.playerNum)
    local square = player and player:getSquare()
    if not square then return end

    local z = square:getZ()
    local state = object:isActivated()

    if forObject ~= object or forZ ~= z or forState ~= state or not squares then
        squares = coveredSquares(object, z)
        forObject, forZ, forState = object, z, state
    end
    if not squares then return end

    -- Green while it is running, red while it is not: same colours vanilla
    -- uses for good and bad everywhere else.
    local c = AllInfo.color(state)
    for i = 1, #squares do
        local sq = squares[i]
        local x, y = sq:getX(), sq:getY()
        -- Denser than the old fill: a ring is a fraction of the tiles, so the
        -- alpha that read as a haze over the whole disc read as nothing here.
        addAreaHighlightForPlayer(window.playerNum, x, y, x + 1, y + 1, z, c.r, c.g, c.b, 0.3)
    end
end

local function forget()
    forObject, forZ, forState, squares = nil, nil, nil, nil
end

-- The highlight is a per-frame call, so it disappears on its own the moment we
-- stop drawing. Nothing to clean up on screen, only the cache.
local basePrerender = ISGeneratorInfoWindow.prerender

function ISGeneratorInfoWindow:prerender(...)
    if self:getIsVisible() then
        local ok, err = pcall(AllInfo.GeneratorRange.draw, self)
        if not ok then
            print("[AllInfo] generator highlight disabled: " .. tostring(err))
            AllInfo.GeneratorRange.draw = function() end
        end
    end
    return basePrerender(self, ...)
end

local baseRemove = ISGeneratorInfoWindow.removeFromUIManager

function ISGeneratorInfoWindow:removeFromUIManager(...)
    forget()
    return baseRemove(self, ...)
end

AllInfo.hooks = AllInfo.hooks or {}
AllInfo.hooks.GeneratorPrerender = ISGeneratorInfoWindow.prerender
