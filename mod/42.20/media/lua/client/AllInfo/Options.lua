require "AllInfo/Core"
require "PZAPI/ModOptions"

-- Registers every AllInfo toggle with PZAPI.ModOptions so we inherit its
-- persistence (ModOptions.ini), loading and apply cycle for free. The controls
-- are *drawn* by OptionsTab.lua in our own tab, not in the Mods tab.

AllInfo.Options = AllInfo.Options or {}

AllInfo.Options.MOD_ID = "AllInfo"

-- { id, default, tooltipKey, nameKey }. Order here is the order shown in the tab.
--
-- nameKey is what makes the per-line switches cheap: a switch that hides a single
-- tooltip row is named with the key of that row's own label, so it reads exactly
-- like the line it hides and costs no translation of ours. Most of them are
-- vanilla keys, which is 29 languages free. Left out, the name falls back to
-- "UI_AllInfo_opt_" .. id, which is what the block switches use.
--
-- Three levels, not two: section, group, option. The groups are what makes the
-- tab readable once every tooltip line gets its own switch, and they are the
-- unit the tab folds. Section order and group order are both the order on
-- screen.
--
-- section.options is derived below by flattening the groups, because the
-- cascade and the SelfTest both walk it and neither cares about grouping.
AllInfo.Options.sections = {
    {
        key = "items",
        master = "MasterItems",
        groups = {
            -- One group per block of the tooltip, and inside it one switch per
            -- line, in the order the lines are drawn. No block switch on top of
            -- them: a switch called "Melee: damage, speed and durability" is
            -- three of the lines under it wearing a hat, and the group header
            -- with its tally already says what turning all of them off does.
            -- What survives here is only what a line switch cannot express: a
            -- rule about which items qualify, or an extra term in a figure.
            { key = "melee", options = {
                { "WpnDamage", true, "UI_AllInfo_opt_WpnDamage_tip", "Tooltip_weapon_Damage" },
                { "WpnCrit", true, "UI_AllInfo_opt_WpnCrit_tip", "Tooltip_AllInfo_Critical" },
                { "WpnCritDmg", true, "UI_AllInfo_opt_WpnCritDmg_tip", "Tooltip_AllInfo_CriticalDamage" },
                { "WpnSharp", true, "UI_AllInfo_opt_WpnSharp_tip", "Tooltip_weapon_Sharpness" },
                { "WpnSpeed", true, "UI_AllInfo_opt_WpnSpeed_tip", "Tooltip_AllInfo_AttackSpeed" },
                { "WpnReach", true, "UI_AllInfo_opt_WpnReach_tip", "Tooltip_AllInfo_Reach" },
                { "WpnStrain", true, "UI_AllInfo_opt_WpnStrain_tip", "Tooltip_AllInfo_MuscleStrain" },
                { "WpnSwing", true, "UI_AllInfo_opt_WpnSwing_tip", "Tooltip_AllInfo_SwingType" },
                { "WpnCategory", true, "UI_AllInfo_opt_WpnCategory_tip", "Tooltip_AllInfo_WeaponType" },
                { "WpnCondition", true, "UI_AllInfo_opt_WpnCondition_tip", "Tooltip_weapon_Condition" },
                { "WpnLoss", true, "UI_AllInfo_opt_WpnLoss_tip", "Tooltip_AllInfo_ConditionLoss" },
                { "WpnHits", true, "UI_AllInfo_opt_WpnHits_tip", "Tooltip_AllInfo_HitsLeft" },
                { "HideFishingCombat", true, "UI_AllInfo_opt_HideFishingCombat_tip" },
            } },
            { key = "firearm", options = {
                { "GunCondition", true, "UI_AllInfo_opt_GunCondition_tip", "Tooltip_weapon_Condition" },
                { "GunDamage", true, "UI_AllInfo_opt_GunDamage_tip", "Tooltip_weapon_Damage" },
                { "GunRange", true, "UI_AllInfo_opt_GunRange_tip", "Tooltip_weapon_Range" },
                { "GunHitChance", true, "UI_AllInfo_opt_GunHitChance_tip", "Tooltip_AllInfo_HitChance" },
                { "GunCrit", true, "UI_AllInfo_opt_GunCrit_tip", "Tooltip_AllInfo_Critical" },
                { "GunNoise", true, "UI_AllInfo_opt_GunNoise_tip", "Tooltip_AllInfo_NoiseRadius" },
                { "GunAim", true, "UI_AllInfo_opt_GunAim_tip", "Tooltip_AllInfo_AimingTime" },
                { "GunReload", true, "UI_AllInfo_opt_GunReload_tip", "Tooltip_AllInfo_ReloadTime" },
                { "GunClip", true, "UI_AllInfo_opt_GunClip_tip", "Tooltip_AllInfo_Capacity" },
                { "GunLoss", true, "UI_AllInfo_opt_GunLoss_tip", "Tooltip_AllInfo_ConditionLoss" },
                { "GunJam", true, "UI_AllInfo_opt_GunJam_tip", "Tooltip_AllInfo_JamChance" },
            } },
            { key = "ammo", label = "IGUI_ItemCat_Ammo", options = {
                { "AmmoCount", true, "UI_AllInfo_opt_AmmoCount_tip", "Tooltip_AllInfo_Capacity" },
                { "AmmoType", true, "UI_AllInfo_opt_AmmoType_tip", "Tooltip_weapon_Ammo" },
                { "AmmoGuns", true, "UI_AllInfo_opt_AmmoGuns_tip", "Tooltip_AllInfo_UsedBy" },
            } },
            { key = "food", label = "IGUI_ItemCat_Food", options = {
                { "FoodStale", true, "UI_AllInfo_opt_FoodStale_tip", "Tooltip_AllInfo_Stale" },
                { "FoodRots", true, "UI_AllInfo_opt_FoodRots_tip", "Tooltip_AllInfo_Rots" },
                { "FoodCooking", true, "UI_AllInfo_opt_FoodCooking_tip", "Tooltip_AllInfo_CookingTime" },
                { "FoodBurning", true, "UI_AllInfo_opt_FoodBurning_tip", "IGUI_invpanel_Burning" },
                { "CookingWarmUp", false, "UI_AllInfo_opt_CookingWarmUp_tip" },
            } },
            { key = "drink", options = {
                { "DrinkThirst", true, "UI_AllInfo_opt_DrinkThirst_tip", "Fluid_Prop_Thirst" },
                { "DrinkHunger", true, "UI_AllInfo_opt_DrinkHunger_tip", "Fluid_Prop_Hunger" },
                { "DrinkFatigue", true, "UI_AllInfo_opt_DrinkFatigue_tip", "Fluid_Prop_Fatigue" },
                { "DrinkStress", true, "UI_AllInfo_opt_DrinkStress_tip", "Fluid_Prop_Stress" },
                { "DrinkUnhappy", true, "UI_AllInfo_opt_DrinkUnhappy_tip", "Fluid_Prop_Unhappy" },
                { "DrinkCalories", true, "UI_AllInfo_opt_DrinkCalories_tip", "Fluid_Prop_Calories" },
                { "DrinkCarbs", true, "UI_AllInfo_opt_DrinkCarbs_tip", "Fluid_Prop_Carbohydrates" },
                { "DrinkProteins", true, "UI_AllInfo_opt_DrinkProteins_tip", "Fluid_Prop_Proteins" },
                { "DrinkFat", true, "UI_AllInfo_opt_DrinkFat_tip", "Fluid_Prop_Lipids" },
                { "DrinkAlcohol", true, "UI_AllInfo_opt_DrinkAlcohol_tip", "Fluid_Prop_Alcohol" },
                { "DrinkPoison", true, "UI_AllInfo_opt_DrinkPoison_tip", "Fluid_Poison" },
            } },
            { key = "nutrition", label = "UI_AllInfo_group_nutrition", options = {
                { "NutCalories", false, "UI_AllInfo_opt_NutCalories_tip", "Tooltip_food_Calories" },
                { "NutCarbs", false, "UI_AllInfo_opt_NutCarbs_tip", "Tooltip_food_Carbs" },
                { "NutProteins", false, "UI_AllInfo_opt_NutProteins_tip", "Tooltip_AllInfo_Proteins" },
                { "NutFat", false, "UI_AllInfo_opt_NutFat_tip", "Tooltip_food_Fat" },
            } },
            { key = "clothing", label = "IGUI_ItemCat_Clothing", options = {
                { "ClothCondition", true, "UI_AllInfo_opt_ClothCondition_tip", "Tooltip_weapon_Condition" },
                { "ClothInsulation", true, "UI_AllInfo_opt_ClothInsulation_tip", "Tooltip_item_Insulation" },
                { "ClothWind", true, "UI_AllInfo_opt_ClothWind_tip", "Tooltip_item_Windresist" },
                { "ClothWater", true, "UI_AllInfo_opt_ClothWater_tip", "Tooltip_item_Waterresist" },
                { "ClothRun", true, "UI_AllInfo_opt_ClothRun_tip", "Tooltip_RunSpeedModifier" },
                { "ClothCombat", true, "UI_AllInfo_opt_ClothCombat_tip", "Tooltip_CombatSpeedModifier" },
                { "ClothDiscomfort", true, "UI_AllInfo_opt_ClothDiscomfort_tip", "Tooltip_item_Discomfort" },
                { "ClothStomp", true, "UI_AllInfo_opt_ClothStomp_tip", "Tooltip_AllInfo_StompPower" },
                { "ClothBlood", true, "UI_AllInfo_opt_ClothBlood_tip", "Tooltip_clothing_bloody" },
                { "ClothDirt", true, "UI_AllInfo_opt_ClothDirt_tip", "Tooltip_clothing_dirty" },
                { "ClothWet", true, "UI_AllInfo_opt_ClothWet_tip", "Tooltip_clothing_wet" },
            } },
            { key = "container", label = "IGUI_ItemCat_Container", options = {
                { "BagRun", true, "UI_AllInfo_opt_BagRun_tip", "Tooltip_RunSpeedModifier" },
                { "BagCombat", true, "UI_AllInfo_opt_BagCombat_tip", "Tooltip_CombatSpeedModifier" },
            } },
            { key = "mask", label = "IGUI_ItemCat_ProtectiveGear", options = {
                { "MaskDefense", true, "UI_AllInfo_opt_MaskDefense_tip", "Tooltip_AllInfo_CorpseDefense" },
                { "MaskCharge", true, "UI_AllInfo_opt_MaskCharge_tip", "Tooltip_AllInfo_FilterCharge" },
                { "MaskLeft", true, "UI_AllInfo_opt_MaskLeft_tip", "UI_AllInfo_mask_FilterLeft" },
            } },
            { key = "medicine", label = "IGUI_ItemCat_FirstAid", options = {
                { "MedDuration", true, "UI_AllInfo_opt_MedDuration_tip", "UI_AllInfo_med_Duration" },
                { "MedWait", true, "UI_AllInfo_opt_MedWait_tip", "UI_AllInfo_med_Wait" },
                { "MedEffect", true, "UI_AllInfo_opt_MedEffect_tip", "UI_AllInfo_med_Effect" },
                { "MedicineDetail", false, "UI_AllInfo_opt_MedicineDetail_tip", "UI_AllInfo_med_Details" },
            } },
            { key = "books", label = "IGUI_ItemCat_Literature", options = {
                { "BookSpeed", true, "UI_AllInfo_opt_BookSpeed_tip", "Tooltip_AllInfo_ReadingSpeed" },
                { "BookTime", true, "UI_AllInfo_opt_BookTime_tip", "Tooltip_AllInfo_ReadingTime" },
            } },
            { key = "media", label = "IGUI_ItemCat_Entertainment", options = {
                { "MediaXp", true, "UI_AllInfo_opt_MediaXp_tip", "UI_AllInfo_line_MediaXp" },
                { "MediaRecipes", true, "UI_AllInfo_opt_MediaRecipes_tip", "Tooltip_AllInfo_TeachesRecipes" },
                { "MediaWatched", true, "UI_AllInfo_opt_MediaWatched_tip", "Tooltip_AllInfo_Watched" },
            } },
            { key = "sleep", label = "UI_AllInfo_group_sleep", options = {
                { "SleepQuality", true, "UI_AllInfo_opt_SleepQuality_tip", "Tooltip_AllInfo_RestQuality" },
                { "SleepDiscomfort", true, "UI_AllInfo_opt_SleepDiscomfort_tip", "Tooltip_AllInfo_Discomfort" },
            } },
            { key = "light", label = "IGUI_ItemCat_LightSource", options = {
                { "PowerLeft", true, "UI_AllInfo_opt_PowerLeft_tip", "IGUI_invpanel_Remaining" },
                { "PowerLife", true, "UI_AllInfo_opt_PowerLife_tip", "Tooltip_AllInfo_PowerLife" },
                { "LightDistance", true, "UI_AllInfo_opt_LightDistance_tip", "Tooltip_AllInfo_LightDistance" },
                { "LightStrength", true, "UI_AllInfo_opt_LightStrength_tip", "Tooltip_AllInfo_LightStrength" },
                { "LightBeam", true, "UI_AllInfo_opt_LightBeam_tip", "Tooltip_AllInfo_LightBeam" },
            } },
            { key = "fishgear", label = "IGUI_ItemCat_Fishing", options = {
                { "RodTension", true, "UI_AllInfo_opt_RodTension_tip", "Tooltip_AllInfo_fish_RodTension" },
                { "RodBreaks", true, "UI_AllInfo_opt_RodBreaks_tip", "Tooltip_AllInfo_fish_Breaks" },
                { "GearHook", true, "UI_AllInfo_opt_GearHook_tip", "Tooltip_AllInfo_fish_HookChance" },
                { "GearLine", true, "UI_AllInfo_opt_GearLine_tip", "Tooltip_AllInfo_fish_LineWear" },
                { "BaitFor", true, "UI_AllInfo_opt_BaitFor_tip", "Tooltip_AllInfo_fish_BaitFor" },
            } },
            { key = "supplies", options = {
                { "SeedGrow", true, "UI_AllInfo_opt_SeedGrow_tip", "Tooltip_AllInfo_GrowTime" },
                { "SeedMonths", true, "UI_AllInfo_opt_SeedMonths_tip", "Tooltip_AllInfo_SowMonths" },
                { "FuelBurn", true, "UI_AllInfo_opt_FuelBurn_tip", "Tooltip_AllInfo_BurnTime" },
            } },
            { key = "compare", options = {
                { "ShowDeltas", true, "UI_AllInfo_opt_ShowDeltas_tip" },
            } },
        },
    },
    {
        key = "crafting",
        master = "MasterCrafting",
        groups = {
            { key = "recipes", label = "IGUI_LiteratureUI_Recipes", options = {
                { "CraftingTooltips", true, "UI_AllInfo_opt_CraftingTooltips_tip" },
            } },
        },
    },
    {
        key = "world",
        master = "MasterWorld",
        groups = {
            { key = "generator", label = "ContextMenu_Generator", options = {
                { "GenNoise", true, "UI_AllInfo_opt_GenNoise_tip", "UI_AllInfo_GeneratorNoise" },
                { "GenFuel", true, "UI_AllInfo_opt_GenFuel_tip", "IGUI_invpanel_Remaining" },
                { "GenToWarn", true, "UI_AllInfo_opt_GenToWarn_tip", "UI_AllInfo_line_GenToWarn" },
                { "GenToDead", true, "UI_AllInfo_opt_GenToDead_tip", "UI_AllInfo_GeneratorToDead" },
                { "GenBackfire", true, "UI_AllInfo_opt_GenBackfire_tip", "UI_AllInfo_GeneratorBackfire" },
                { "GenDanger", true, "UI_AllInfo_opt_GenDanger_tip", "UI_AllInfo_GeneratorDanger" },
                { "GeneratorRealTime", false, "UI_AllInfo_opt_GeneratorRealTime_tip" },
                { "GeneratorHighlight", true, "UI_AllInfo_opt_GeneratorHighlight_tip" },
            } },
            { key = "pump", label = "IGUI_GasPump", options = {
                { "PumpFuel", true, "UI_AllInfo_opt_PumpFuel_tip", "UI_AllInfo_FuelRemaining" },
                { "PumpPower", true, "UI_AllInfo_opt_PumpPower_tip", "IGUI_RadioPower" },
            } },
            { key = "building", label = "IGUI_Build_Name", options = {
                { "StructureInspect", true, "UI_AllInfo_opt_StructureInspect_tip" },
                { "StructStrength", true, "UI_AllInfo_opt_StructStrength_tip", "UI_AllInfo_StructureStrength" },
                { "StructAtMax", true, "UI_AllInfo_opt_StructAtMax_tip", "UI_AllInfo_line_StructAtMax" },
            } },
            { key = "farming", label = "ContextMenu_Farming", options = {
                { "CropHealth", true, "UI_AllInfo_opt_CropHealth_tip", "Farming_Health" },
                { "CropPhase", true, "UI_AllInfo_opt_CropPhase_tip", "Farming_Current_growing_phase" },
                { "CropNextPhase", true, "UI_AllInfo_opt_CropNextPhase_tip", "Farming_Next_growing_phase" },
                { "CropWater", true, "UI_AllInfo_opt_CropWater_tip", "Farming_Water_levels" },
                { "CropDisease", true, "UI_AllInfo_opt_CropDisease_tip", "Farming_Disease" },
                { "CropWatered", true, "UI_AllInfo_opt_CropWatered_tip", "Farming_Last_time_watered" },
                { "CropFertilizer", true, "UI_AllInfo_opt_CropFertilizer_tip", "Farming_Fertilized" },
                { "FarmingGate", false, "UI_AllInfo_opt_FarmingGate_tip" },
            } },
            { key = "fishing", label = "ContextMenu_Fishing", options = {
                { "FishTime", true, "UI_AllInfo_opt_FishTime_tip", "Sandbox_TimeOptions" },
                { "FishTemp", true, "UI_AllInfo_opt_FishTemp_tip", "IGUI_Temperature" },
                { "FishWeather", true, "UI_AllInfo_opt_FishWeather_tip", "IGUI_ClimateControl_Weather" },
                { "FishWind", true, "UI_AllInfo_opt_FishWind_tip", "IGUI_Fishing_Wind" },
                { "FishFog", true, "UI_AllInfo_opt_FishFog_tip", "IGUI_climate_Fog" },
                { "FishHook", true, "UI_AllInfo_opt_FishHook_tip", "UI_AllInfo_fish_Hook" },
                { "FishTrash", true, "UI_AllInfo_opt_FishTrash_tip", "UI_AllInfo_fish_Trash" },
                { "FishCount", true, "UI_AllInfo_opt_FishCount_tip", "UI_AllInfo_fish_Fish" },
                { "FishBite", true, "UI_AllInfo_opt_FishBite_tip", "UI_AllInfo_fish_Bite" },
                { "FishWait", true, "UI_AllInfo_opt_FishWait_tip", "UI_AllInfo_fish_Wait" },
                { "FishMinLevel", true, "UI_AllInfo_opt_FishMinLevel_tip", "UI_AllInfo_line_FishMinLevel" },
                { "FishSize", true, "UI_AllInfo_opt_FishSize_tip", "UI_AllInfo_line_FishSize" },
                { "FishTrophy", true, "UI_AllInfo_opt_FishTrophy_tip", "UI_AllInfo_line_FishTrophy" },
                { "FishOdds", true, "UI_AllInfo_opt_FishOdds_tip", "UI_AllInfo_line_FishOdds" },
                { "FishBaits", true, "UI_AllInfo_opt_FishBaits_tip", "UI_AllInfo_line_FishBaits" },
                { "FishPredator", true, "UI_AllInfo_opt_FishPredator_tip", "UI_AllInfo_line_FishPredator" },
                { "FishingGate", false, "UI_AllInfo_opt_FishingGate_tip" },
            } },
            { key = "animals", label = "IGUI_ItemCat_Animal", options = {
                { "AnimalMeat", true, "UI_AllInfo_opt_AnimalMeat_tip", "UI_AllInfo_animal_Meat" },
                { "AnimalBlood", true, "UI_AllInfo_opt_AnimalBlood_tip", "Fluid_Name_AnimalBlood" },
                { "AnimalFeathers", true, "UI_AllInfo_opt_AnimalFeathers_tip", "UI_AllInfo_line_Feathers" },
                { "AnimalAge", true, "UI_AllInfo_opt_AnimalAge_tip", "IGUI_Animal_Geriatric" },
                { "AnimalWeight", true, "UI_AllInfo_opt_AnimalWeight_tip", "IGUI_char_Weight" },
                { "AnimalTrust", true, "UI_AllInfo_opt_AnimalTrust_tip", "IGUI_Animal_PlayerAcceptance" },
                { "AnimalHealth", true, "UI_AllInfo_opt_AnimalHealth_tip", "IGUI_XP_Health" },
                { "AnimalHunger", true, "UI_AllInfo_opt_AnimalHunger_tip", "IGUI_HaloNote_Hunger" },
                { "AnimalThirst", true, "UI_AllInfo_opt_AnimalThirst_tip", "IGUI_HaloNote_Thirst" },
                { "AnimalStress", true, "UI_AllInfo_opt_AnimalStress_tip", "IGUI_Animal_Stress" },
                { "AnimalMilk", true, "UI_AllInfo_opt_AnimalMilk_tip", "IGUI_Animal_Udder" },
                { "AnimalWool", true, "UI_AllInfo_opt_AnimalWool_tip", "IGUI_Animal_Wool" },
                { "AnimalBreeding", true, "UI_AllInfo_opt_AnimalBreeding_tip", "IGUI_Animal_Pregnant" },
                { "AnimalGate", false, "UI_AllInfo_opt_AnimalGate_tip" },
            } },
            { key = "traps", label = "IGUI_ItemCat_Trapping", options = {
                { "TrapPrey", true, "UI_AllInfo_opt_TrapPrey_tip", "UI_AllInfo_trap_Prey" },
                { "TrapHours", true, "UI_AllInfo_opt_TrapHours_tip", "UI_AllInfo_trap_Window_Hours" },
                { "TrapCatch", true, "UI_AllInfo_opt_TrapCatch_tip", "UI_AllInfo_trap_CatchChance" },
                { "TrapBait", true, "UI_AllInfo_opt_TrapBait_tip", "UI_AllInfo_trap_Bait" },
                { "TrapBaitState", true, "UI_AllInfo_opt_TrapBaitState_tip", "UI_AllInfo_trap_BaitState" },
                { "TrapBaitLoss", true, "UI_AllInfo_opt_TrapBaitLoss_tip", "UI_AllInfo_trap_BaitLoss" },
                { "TrapZone", true, "UI_AllInfo_opt_TrapZone_tip", "UI_AllInfo_trap_Zone" },
                { "TrapDestroyed", true, "UI_AllInfo_opt_TrapDestroyed_tip", "UI_AllInfo_trap_Destroyed" },
                { "TrapInside", true, "UI_AllInfo_opt_TrapInside_tip", "UI_AllInfo_trap_Inside" },
                { "TrapWarnings", true, "UI_AllInfo_opt_TrapWarnings_tip", "UI_AllInfo_line_TrapWarnings" },
                { "TrapAttracts", true, "UI_AllInfo_opt_TrapAttracts_tip", "UI_AllInfo_trap_Attracts" },
                { "TrapGate", false, "UI_AllInfo_opt_TrapGate_tip" },
            } },
        },
    },
    {
        key = "character",
        master = "MasterCharacter",
        groups = {
            { key = "skills", label = "IGUI_XP_Skills", options = {
                { "XpMultiplierFix", true, "UI_AllInfo_opt_XpMultiplierFix_tip" },
                { "SkillRecipes", true, "UI_AllInfo_opt_SkillRecipes_tip" },
            } },
            { key = "traits", options = {
                { "TraitInfoCreation", true, "UI_AllInfo_opt_TraitInfoCreation_tip" },
                { "TraitInfoScreen", true, "UI_AllInfo_opt_TraitInfoScreen_tip" },
                { "TraitManualEffects", true, "UI_AllInfo_opt_TraitManualEffects_tip" },
            } },
            { key = "health", label = "IGUI_CraftCategory_Health", options = {
                { "HealthRecovery", true, "UI_AllInfo_opt_HealthRecovery_tip", "UI_AllInfo_health_Recovery" },
                { "HealthWound", true, "UI_AllInfo_opt_HealthWound_tip", "IGUI_ItemCat_Wound" },
                { "HealthStrain", true, "UI_AllInfo_opt_HealthStrain_tip", "IGUI_health_Stiffness" },
                { "HealthFracture", true, "UI_AllInfo_opt_HealthFracture_tip", "IGUI_health_Fracture" },
                { "HealthStitch", true, "UI_AllInfo_opt_HealthStitch_tip", "IGUI_health_Stitched" },
                { "HealthInfection", true, "UI_AllInfo_opt_HealthInfection_tip", "UI_AllInfo_health_WoundInfection" },
                { "HealthRisk", true, "UI_AllInfo_opt_HealthRisk_tip", "UI_AllInfo_health_InfectionRisk" },
                { "HealthBandage", true, "UI_AllInfo_opt_HealthBandage_tip", "IGUI_health_Bandaged" },
                { "HealthPoultice", true, "UI_AllInfo_opt_HealthPoultice_tip", "UI_AllInfo_health_Poultice" },
                { "HealthLodged", true, "UI_AllInfo_opt_HealthLodged_tip", "UI_AllInfo_line_Lodged" },
                { "HealthGate", false, "UI_AllInfo_opt_HealthGate_tip" },
                { "TempValues", true, "UI_AllInfo_opt_TempValues_tip" },
            } },
            { key = "moodles", options = {
                { "MoodleTooltip", true, "UI_AllInfo_opt_MoodleTooltip_tip" },
                { "MoodleCorpses", true, "UI_AllInfo_opt_MoodleCorpses_tip" },
            } },
        },
        -- Skill and moodle *texts* ship as translation files: nothing to toggle.
        note = "UI_AllInfo_note_translations",
    },
}

-- Flattened view of the same thing. Everything that only needs "every option in
-- this section" reads this and stays blind to the grouping.
for _, section in ipairs(AllInfo.Options.sections) do
    section.options = {}
    for _, group in ipairs(section.groups) do
        for _, o in ipairs(group.options) do
            section.options[#section.options + 1] = o
        end
    end
end

local handle = PZAPI.ModOptions:create(AllInfo.Options.MOD_ID, "UI_optionscreen_allinfo")
AllInfo.Options.handle = handle

-- Masters are a write shortcut, not state: AllInfo.enabled() always reads the
-- individual option, so ticking a section back on keeps the fine-grained
-- choices the user did not overwrite with the cascade.
local function cascade(ids)
    return function(_, selected)
        for i = 1, #ids do
            local o = handle:getOption(ids[i])
            if o then o:setValue(selected) end   -- also updates the on-screen tickbox
        end
    end
end

-- No page-wide "enable everything" switch: the tab's preset dropdown already
-- offers All, Reset to default and None, and two controls doing the same job is
-- one more than anybody needs.
for _, section in ipairs(AllInfo.Options.sections) do
    -- Every Translator key must carry its file's prefix (UI.json -> "UI_"),
    -- or the key is dropped on load and getText() returns the raw key.
    handle:addTitle("UI_AllInfo_section_" .. section.key)

    local childIds = {}
    for _, o in ipairs(section.options) do
        childIds[#childIds + 1] = o[1]
    end

    local master = handle:addTickBox(section.master, "UI_AllInfo_opt_" .. section.master, true)
    master.onChange = cascade(childIds)

    for _, o in ipairs(section.options) do
        handle:addTickBox(o[1], o[4] or ("UI_AllInfo_opt_" .. o[1]), o[2], o[3])
    end

    if section.note then handle:addDescription(section.note) end
end

handle:addSeparator()
handle:addButton("RunSelfTest", "UI_AllInfo_opt_RunSelfTest", nil, function()
    AllInfo.SelfTest.run()
end)
