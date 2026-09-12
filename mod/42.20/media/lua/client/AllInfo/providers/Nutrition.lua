require "AllInfo/Core"

-- Ships with its toggle OFF. Vanilla only reveals this block for packaged food
-- or a Nutritionist character, so showing it on everything would quietly undo
-- that trait. Opt-in for players who want it anyway.

AllInfo.register("Nutrition", 15, nil, function(out, item, chr)
    if not instanceof(item, "Food") then return end

    -- Packaged food carries a nutrition label, so vanilla already prints this
    -- block for it. Repeating it would just double every line.
    if item:isPackaged() then return end

    local calories = item:getCalories()
    if calories and calories ~= 0 then
        AllInfo.rowIf(out, "NutCalories", getText("Tooltip_food_Calories"), AllInfo.num(calories, 0))
    end

    local carbs = item:getCarbohydrates()
    if carbs and carbs ~= 0 then
        AllInfo.rowIf(out, "NutCarbs", getText("Tooltip_food_Carbs"), AllInfo.num(carbs, 1))
    end

    local proteins = item:getProteins()
    if proteins and proteins ~= 0 then
        AllInfo.rowIf(out, "NutProteins", getText("Tooltip_AllInfo_Proteins"), AllInfo.num(proteins, 1))
    end

    local fat = item:getLipids()
    if fat and fat ~= 0 then
        AllInfo.rowIf(out, "NutFat", getText("Tooltip_food_Fat"), AllInfo.num(fat, 1))
    end
end)
