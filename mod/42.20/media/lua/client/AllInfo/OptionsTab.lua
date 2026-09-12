require "AllInfo/Core"
require "AllInfo/Options"
require "OptionScreens/MainOptions"

-- Gives AllInfo its own tab next to "Mods" instead of crowding that one with
-- ~30 toggles. Both vanilla functions are wrapped, never replaced.

AllInfo.OptionsTab = AllInfo.OptionsTab or {}

-- 1) Keep AllInfo out of the vanilla Mods tab -------------------------------

local baseModPanel = MainOptions.addModOptionsPanel

function MainOptions:addModOptionsPanel()
    local all = PZAPI.ModOptions.Data

    local filtered = {}
    for i = 1, #all do
        if all[i].modOptionsID ~= AllInfo.Options.MOD_ID then
            filtered[#filtered + 1] = all[i]
        end
    end

    -- Vanilla only reaches here because AllInfo is in Data. With no other mod
    -- there is nothing to draw, but load() still has to run: it is what reads
    -- ModOptions.ini, and skipping it would silently reset every toggle.
    if #filtered == 0 then
        PZAPI.ModOptions:load()
        return
    end

    PZAPI.ModOptions.Data = filtered
    local ok, err = pcall(baseModPanel, self)
    -- Restore on every path. MainOptions:apply() iterates Data to save, so
    -- leaving it filtered would stop other mods from persisting their options.
    PZAPI.ModOptions.Data = all
    if not ok then error(err) end
end

-- 2) Add our own page -------------------------------------------------------

local baseCreate = MainOptions.create

AllInfo.hooks = AllInfo.hooks or {}

function MainOptions:create()
    baseCreate(self)
    -- Proof for SelfTest that our link still runs. Asserting that
    -- MainOptions.create is still *our* function was the wrong question: Mod
    -- Options, CombatText and Grab & Drop all wrap it correctly, so any of them
    -- loading after us takes the field over and the check went red on a setup
    -- where our tab worked perfectly. What matters is being called, not being
    -- last. MainScreen:create() calls this at startup, so the flag is set long
    -- before anyone can run SelfTest in game.
    AllInfo.hooks.mainOptionsRan = true
    if self.allInfoTabBuilt then return end
    self.allInfoTabBuilt = true
    AllInfo.OptionsTab.build(self)
end

-- Nobody else in the workshop wraps addModOptionsPanel, so identity is still a
-- fair check there. If that ever changes, it gets the same flag treatment.
AllInfo.hooks.MainOptionsModPanel = MainOptions.addModOptionsPanel


-- 3) The page ---------------------------------------------------------------

-- Laid out like vanilla's key bindings screen, which is the one options page a
-- Zomboid player already knows how to read: a full-width rule per section, and
-- the switches under it in two columns.
--
-- Three levels. Sections are always open and carry the rule; groups fold; the
-- options live inside a group, two per row. Groups are what keeps this readable
-- when every tooltip line eventually gets its own switch.
--
-- ⚠️ EVERY control is built once, on the first open, and never destroyed.
-- Folding and searching only move rows and flip their visibility. The line that
-- persists an option is `main.gameOptions:add(gameOption)` and it only runs for
-- controls that got built, so a folded group that skipped building would
-- silently stop saving. Hidden ISUIElements cost nothing to draw.
--
-- ⚠️ Built from AllInfo.Options.sections rather than from PZAPI's flat data
-- list, because the grouping only exists on ours. PZAPI is still the owner of
-- the values: every row looks its option up in opts.dict by id.
--
-- ⚠️ MainOptions:addYesNo() builds a label and a tickbox and returns only the
-- tickbox, so the label would be unreachable and would stay on screen when its
-- row hides. Its lines are inlined below instead.

local GAP = 6            -- between rows
local TOP_PAD = 28       -- above the search box, so it does not touch the tabs
local BLOCK_GAP = 18     -- around the page-wide controls and between sections
local INDENT = 22        -- a group header against its section rule
local ROW_INDENT = 40    -- an option against its group header
local TICK_W = 20
local LABEL_PAD = 14     -- between the longest label of a group and its tickbox
local COL_GAP = 34       -- between columns
local COLS = 3           -- fixed, so every group lines up with every other one

AllInfo.OptionsTab.collapsed = AllInfo.OptionsTab.collapsed or {}

-- Reused from vanilla, so four of these five cost no keys of ours and read
-- right in all 29 languages.
local function presetNames()
    return {
        getText("ContextMenu_All"),
        getText("UI_optionscreen_gamepad_preset_Default_Label"),
        getText("Farming_None"),
        getText("UI_AllInfo_preset_Custom"),
    }
end

local function defaults()
    local out = {}

    for _, section in ipairs(AllInfo.Options.sections) do
        out[section.master] = true
        for _, o in ipairs(section.options) do out[o[1]] = o[2] end
    end
    return out
end

-- Option names are whole sentences ("Batteries and radios: charge left, how long
-- it lasts and how far a torch reaches"), and two columns do not have room for
-- one. Cut to fit and let the hover carry the rest, which is also where the
-- description lives.
local function fit(text, width)
    local tm = getTextManager()
    if tm:MeasureStringX(UIFont.Small, text) <= width then return text end

    local cut = text
    while #cut > 4 and tm:MeasureStringX(UIFont.Small, cut .. "...") > width do
        cut = string.sub(cut, 1, #cut - 1)
    end
    return cut .. "..."
end

-- ⚠️ MainOptions:addTextEntry() does `_text = _text or " "`, so the box is born
-- holding a SPACE, not empty. Comparing against "" left the page believing a
-- search was running from the first frame, and a search deliberately ignores
-- folding, which is why every group looked stuck open and the fold buttons
-- looked dead. Trim before deciding.
--
-- ⚠️ getInternalText(), not getText(). UITextBox2 carries two strings:
-- internalText is what the box holds, and onKeyBack() writes it and only it
-- before firing onTextChange; text is the visible slice and is not recomputed
-- until the next render. Reading getText() from the change handler therefore ran
-- every search one keystroke behind, and deleting the last character left the
-- page filtering on that character, which matches nearly every option: the box
-- read empty while every group stayed forced open. Vanilla's own mod options
-- read getInternalText() for the same reason.
local function currentFilter(page)
    local raw = page.search:getInternalText() or ""
    return string.lower((string.gsub(string.gsub(raw, "^%s+", ""), "%s+$", "")))
end

local function rowMatches(row, filter)
    return filter == "" or string.find(row.search, filter, 1, true) ~= nil
end

-- Counters and the preset readout. Deferred, not called from build(): the
-- stored values are written by gameOption.toUI() AFTER the page is built, so
-- counting during build gave every section a flat 0.
function AllInfo.OptionsTab.recount(page)
    for _, sec in ipairs(page.sections) do
        local on, total = 0, 0

        for _, grp in ipairs(sec.groups) do
            local gOn = 0
            for _, row in ipairs(grp.rows) do
                if row.tick:isSelected(1) then gOn = gOn + 1 end
            end

            local folded = AllInfo.OptionsTab.collapsed[grp.id]
            grp.header:setTitle((folded and "[+]  " or "[-]  ") .. grp.title
                .. "    " .. gOn .. " / " .. #grp.rows)
            grp.header:setWidthToTitle()

            on = on + gOn
            total = total + #grp.rows
        end

        -- ⚠️ setNameWithoutMoving, never setName: ISLabel:setName() starts with
        -- `self:setX(self.originalX)`, and originalX is frozen at construction
        -- and never follows setX(). Every label this page positions itself was
        -- built at x = 0, so renaming one threw it against the left edge of the
        -- panel, where the section tally was drawn half off screen and over the
        -- title. relayout() is the only thing that decides x here.
        sec.count:setNameWithoutMoving(on .. " / " .. total)

        -- The section switch is derived, never remembered: ticked means "this
        -- whole section is on". Writing it only when the user clicked it left
        -- it stuck at whatever it said last, so turning the last option of a
        -- section back on by hand did not tick it again. Nothing reads the
        -- stored master value, AllInfo.enabled() always asks the individual
        -- option, so deriving it costs nothing.
        sec.master:setSelected(1, on == total)
    end

    local def, all, none, same = defaults(), true, true, true
    for _, row in ipairs(page.every) do
        local v = row.tick:isSelected(1)
        if not v then all = false end
        if v then none = false end
        if v ~= def[row.id] then same = false end
    end

    local at = 4
    if all then at = 1 elseif same then at = 2 elseif none then at = 3 end
    page.preset.selected = at
end

-- Lays the page out from scratch. Visible rows get the next slot, hidden ones
-- are pushed aside. Runs on every fold, keystroke and preset.
function AllInfo.OptionsTab.relayout(page)
    local filter = currentFilter(page)
    local y = page.top
    local shown = 0

    for _, sec in ipairs(page.sections) do
        local hits = 0
        for _, grp in ipairs(sec.groups) do
            for _, row in ipairs(grp.rows) do
                if rowMatches(row, filter) then hits = hits + 1 end
            end
        end

        local live = hits > 0
        sec.rule:setVisible(live)
        sec.title:setVisible(live)
        sec.count:setVisible(live)
        sec.master:setVisible(live)

        if live then
            -- Title on the left, tally and switch on the right, all on one
            -- line, and the rule under them. Splitting the title above the rule
            -- and the tally below it made them read as two unrelated rows.
            -- Title, tally and switch travel together rather than being pinned
            -- to the right edge, where the switch floated alone in the empty
            -- half of a page whose grid ends well before it.
            local titleW = getTextManager():MeasureStringX(UIFont.Medium, sec.title.name)
            y = y + BLOCK_GAP
            sec.title:setY(y)
            sec.count:setX(page.margin + titleW + 24)
            sec.count:setY(y)
            sec.master:setX(page.margin + titleW + 24
                + getTextManager():MeasureStringX(UIFont.Small, sec.count.name) + 12)
            sec.master:setY(y)
            y = y + page.rowH + 2
            sec.rule:setY(y)
            y = y + GAP * 2
        end

        for _, grp in ipairs(sec.groups) do
            -- A search ignores folding: hiding a hit inside a closed group is
            -- the one thing a search box must never do.
            local folded = filter == "" and AllInfo.OptionsTab.collapsed[grp.id]
            local gHits = 0
            for _, row in ipairs(grp.rows) do
                if rowMatches(row, filter) then gHits = gHits + 1 end
            end

            grp.header:setVisible(gHits > 0)
            if gHits > 0 then
                grp.header:setY(y)
                y = y + page.rowH + GAP
            end

            -- ⚠️ The grid is the page's, not the group's. Three columns of
            -- identical width, and the tickbox at the same offset inside every
            -- one of them, so a group of short names and a group of long ones
            -- still read as the same table. A cell whose label does not fill it
            -- leaves the rest reserved and empty rather than pulling its switch
            -- left, which is what keeps the columns straight all the way down
            -- the page. Measured once in build(), because a figure that changed
            -- per group is exactly what broke the alignment.
            local col = 0
            for _, row in ipairs(grp.rows) do
                local on = gHits > 0 and not folded and rowMatches(row, filter)
                row.label:setVisible(on)
                row.tick:setVisible(on)

                if on then
                    row.label:setX(page.colX[col + 1])
                    row.tick:setX(page.colX[col + 1] + page.labelW + LABEL_PAD)
                    row.label:setY(y)
                    row.tick:setY(y)

                    col = col + 1
                    if col == COLS then
                        col = 0
                        y = y + page.rowH + GAP
                    end
                    shown = shown + 1
                end
            end

            if col > 0 then y = y + page.rowH + GAP end
        end
    end

    -- ⚠️ Only while a search is running. Everything folded also leaves shown at
    -- zero, and saying "nothing matches" over a page full of groups is a lie.
    -- ⚠️ And it takes its slot from the same y as everything else, before the
    -- tail: pinning it to the top while the buttons still started at page.top
    -- printed the two on the same line.
    local noHits = shown == 0 and filter ~= ""
    page.empty:setVisible(noHits)
    if noHits then
        y = y + BLOCK_GAP
        page.empty:setY(y)
        y = y + page.rowH + GAP
    end

    for _, tail in ipairs(page.tail) do
        y = y + BLOCK_GAP
        tail:setY(y)
        y = y + page.rowH + GAP
    end

    page.main.mainPanel:setScrollHeight(y + BLOCK_GAP * 3)
end

-- One option: its label and its tickbox. X is set by relayout, so only the
-- widths matter here.
-- ⚠️ ISLabel:new(x, y, h, name, r, g, b, a, font, bLeft) right-aligns the text
-- on x unless bLeft is true: it does `o.x = o.x - o.width` in the constructor.
-- Every label meant to read left to right has to pass that true, or it hangs off
-- the left edge, which is what ate the start of every section title. The one
-- place the default is what we want is the section tally, which should END
-- where the tickbox begins.
local function buildRow(main, h, name, hover)
    local label = ISLabel:new(0, 0, h, name, 1, 1, 1, 1, UIFont.Small, true)
    label:initialise()
    main.mainPanel:addChild(label)

    local tick = ISTickBox:new(0, 0, h, h, "")
    tick.choicesColor = { r = 1, g = 1, b = 1, a = 1 }
    tick:initialise()
    tick:addOption("")
    if hover then tick.tooltip = hover end
    main.mainPanel:addChild(tick)
    main.mainPanel:insertNewLineOfButtons(tick)

    label:setHeight(tick:getHeight())
    return label, tick
end

local function bindOption(main, page, option, tick)
    -- ⚠️ PZAPI's Option:setValue() writes to the screen with
    -- `if self.element ~= nil then self.element:setSelected(1, value) end`, and
    -- element is what vanilla's own builder assigns. Without it a section master
    -- changed every stored value and no tickbox, and then apply() read the
    -- untouched tickboxes back over them: the master looked like it did nothing.
    option.element = tick

    local gameOption = GameOption:new(AllInfo.Options.MOD_ID .. "." .. option.id, tick)

    function gameOption.toUI(self)
        self.control:setSelected(1, option.value)
        -- The values land here, one per option, after build() is done. Marking
        -- the page dirty is what gets the counters off zero without polling.
        page.dirty = true
    end

    function gameOption.apply(self)
        local box = self.control
        if option.onChangeApply and option.value ~= box:isSelected(1) then
            option:onChangeApply(box:isSelected(1))
        end
        option.value = box:isSelected(1)
        -- The tooltip cache keys on the item, so without this a hover started
        -- within half a second of pressing Accept still shows the old rows.
        AllInfo.flushRows()
    end

    function gameOption.onChange(self, index, selected)
        if option.onChange then option:onChange(selected) end
        page.dirty = true
    end

    main.gameOptions:add(gameOption)
end

-- The description, and nothing else. The name is already on the row the cursor
-- is sitting on, and repeating it above the text turned every hover into a
-- header and a paragraph saying the same thing twice.
--
-- It comes back only when `cut` says the label did not fit its cell and was
-- trimmed, which is the one case where the row on screen does not say it in
-- full, and for the section switch, which has no label of its own at all.
local function hoverText(name, tipKey, cut)
    local tip = tipKey and getText(tipKey)
    if tip == tipKey or tip == "" then tip = nil end
    if not cut then return tip end
    return tip and (name .. " <LINE> <LINE> " .. tip) or name
end

function AllInfo.OptionsTab.build(main)
    local opts = PZAPI.ModOptions.Dict[AllInfo.Options.MOD_ID]
    if not opts then return end

    PZAPI.ModOptions:load()
    main:addPage(getText("UI_optionscreen_allinfo"))

    local h = MainOptions.style.buttonHeight
    local width = main:getWidth()
    local margin = 40

    -- ⚠️ The two columns start where the option labels start, not at the margin.
    -- Splitting the full width instead put column one's tickbox further right
    -- than column two's label, and the two overlapped.
    local left = margin + ROW_INDENT
    local usable = width - left - margin - 26       -- 26 leaves room for the scrollbar

    -- Three equal cells and the gaps between them. The widest a label may be is
    -- whatever is left of a cell once its own tickbox and the padding are out;
    -- anything longer is cut and the hover carries the full text.
    local cellW = (usable - COL_GAP * (COLS - 1)) / COLS
    local maxLabel = cellW - LABEL_PAD - TICK_W

    local page = {
        main = main, sections = {}, every = {}, tail = {},
        rowH = h, ruleH = 12, margin = margin, left = left, usable = usable,
    }
    AllInfo.OptionsTab.page = page

    -- Centred, and with air above them: they are the controls that drive the
    -- whole page, so they read as a header rather than as the first row.
    main.addY = TOP_PAD
    local boxW = math.min(460, width / 3)
    page.search = main:addTextEntry((width - boxW) / 2, 0, getText("IGUI_DebugMenu_Search"))
    page.search:setWidth(boxW)
    page.search.onTextChangeFunction = function() AllInfo.OptionsTab.relayout(page) end

    page.preset = main:addCombo((width - boxW) / 2, 0, boxW, h, "", presetNames(), 1,
        page, function(_, box) AllInfo.OptionsTab.applyPreset(page, box.selected) end)

    page.top = TOP_PAD + main.addY

    for _, section in ipairs(AllInfo.Options.sections) do
        -- Full width on purpose, even though the switches now stop well before
        -- it: the rule is what separates one section from the next.
        local rule = ISPanel:new(margin, 0, ROW_INDENT + usable, 1)
        rule.backgroundColor = { r = 1, g = 1, b = 1, a = 0.25 }
        rule:initialise()
        main.mainPanel:addChild(rule)

        local title = ISLabel:new(margin, 0, h,
            getText("UI_AllInfo_section_" .. section.key), 1, 1, 1, 1, UIFont.Medium, true)
        title:initialise()
        main.mainPanel:addChild(title)

        -- The section's own switch and its tally, right-aligned under the rule.
        local count = ISLabel:new(0, 0, h, "", 0.7, 0.7, 0.7, 1, UIFont.Small, true)
        count:initialise()
        main.mainPanel:addChild(count)

        local sec = { key = section.key, rule = rule, title = title, count = count, groups = {} }

        local masterOption = opts.dict[section.master]
        local _, masterTick = buildRow(main, h, "",
            masterOption and hoverText(getText(masterOption.name), masterOption.tooltip, true))
        if masterOption then bindOption(main, page, masterOption, masterTick) end
        sec.master = masterTick

        for _, group in ipairs(section.groups) do
            local id = section.key .. "/" .. group.key
            -- Seven of the sixteen group names already exist in vanilla,
            -- so those declare the key they borrow and cost us nothing in
            -- 29 languages. The rest fall back to one of ours.
            local gTitle = getText(group.label or ("UI_AllInfo_group_" .. group.key))

            local header = ISButton:new(margin + INDENT, 0, 200, h, "[-]  " .. gTitle)
            header:initialise()
            header.internal = id
            -- ISButton calls onclick(self.target, self, ...), so the button is
            -- the SECOND argument. Reading it as the first is a silent nil.
            header:setOnClick(function(_, button)
                local at = button.internal
                AllInfo.OptionsTab.collapsed[at] = not AllInfo.OptionsTab.collapsed[at]
                AllInfo.OptionsTab.recount(page)
                AllInfo.OptionsTab.relayout(page)
            end)
            main.mainPanel:addChild(header)
            main.mainPanel:insertNewLineOfButtons(header)

            local grp = { id = id, title = gTitle, header = header, rows = {} }

            for _, o in ipairs(group.options) do
                local option = opts.dict[o[1]]
                if option then
                    local name = getText(option.name)
                    local shortName = fit(name, maxLabel)
                    local hover = hoverText(name, option.tooltip, shortName ~= name)
                    local label, tick = buildRow(main, h, shortName, hover)
                    bindOption(main, page, option, tick)

                    local row = {
                        id = o[1], label = label, tick = tick,
                        w = getTextManager():MeasureStringX(UIFont.Small, shortName),
                        search = string.lower(name .. " " .. (hover or "")),
                    }
                    grp.rows[#grp.rows + 1] = row
                    page.every[#page.every + 1] = row
                end
            end

            sec.groups[#sec.groups + 1] = grp
        end

        -- A section's closing note goes on its title, where it costs no layout:
        -- vanilla draws it with an ISRichTextPanel whose height is whatever the
        -- text needs, and a row of unknown height does not fit a grid built on
        -- one row height. PZAPI already ran getText() on it when it was declared.
        -- PZAPI ran getText() on the note when it was declared, so section.note
        -- is still the key and the translated text lives in its data entry.
        -- Only one section carries a note today; if a second one ever does,
        -- this needs the entry's position rather than its type.
        if section.note then
            title:setTooltip(getText(section.note))
        end

        page.sections[#page.sections + 1] = sec
    end

    for _, entry in ipairs(opts.data) do
        if entry.type == "button" then
            local button = main:addButton(margin, 0, getText(entry.name))
            button.id = AllInfo.Options.MOD_ID .. "." .. entry.id
            button.target = entry.target
            button:setOnClick(entry.onclick, entry.args[1], entry.args[2], entry.args[3], entry.args[4])
            button.onClickArgs = entry.args
            if entry.tooltip then button:setTooltip(getText(entry.tooltip)) end
            page.tail[#page.tail + 1] = button
        end
    end

    page.empty = ISLabel:new(left, 0, h, getText("UI_AllInfo_opt_NoMatches"), 1, 1, 1, 1, UIFont.Small, true)
    page.empty:initialise()
    page.empty:setVisible(false)
    main.mainPanel:addChild(page.empty)

    -- The one measurement the whole grid hangs on, taken with every row built.
    -- Short of the cap it pulls the switches in against the longest name on the
    -- page; at the cap the switches sit at the edge of their cell. Either way it
    -- is one number for every group, which is what makes the columns line up.
    local widest = 0
    for _, row in ipairs(page.every) do
        if row.w > widest then widest = row.w end
    end
    page.labelW = math.min(widest, maxLabel)

    page.colX = {}
    for c = 1, COLS do page.colX[c] = left + (c - 1) * (cellW + COL_GAP) end

    -- Folded on arrival: the section rules and the group tallies say more at a
    -- glance than sixty rows, and the search is right at the top.
    for _, sec in ipairs(page.sections) do
        for _, grp in ipairs(sec.groups) do
            if AllInfo.OptionsTab.collapsed[grp.id] == nil then
                AllInfo.OptionsTab.collapsed[grp.id] = true
            end
        end
    end

    -- ⚠️ The counters cannot be filled here: gameOption.toUI() writes the stored
    -- values after this function returns. The panel's own prerender picks it up
    -- on the first frame, which is also what keeps the tallies live while the
    -- page is open.
    page.dirty = true

    local basePrerender = main.mainPanel.prerender

    main.mainPanel.prerender = function(self, ...)
        if page.dirty then
            page.dirty = false
            AllInfo.OptionsTab.recount(page)
            AllInfo.OptionsTab.relayout(page)
        end
        return basePrerender(self, ...)
    end

    AllInfo.OptionsTab.relayout(page)
end

-- All, defaults, or nothing. Written through the tickbox so the screen and the
-- stored value stay in step, the same reason Options.lua's cascade() sets the
-- control too.
function AllInfo.OptionsTab.applyPreset(page, choice)
    if choice > 3 then return end

    local def = defaults()
    for _, row in ipairs(page.every) do
        local want = choice == 1 or (choice == 2 and def[row.id])
        row.tick:setSelected(1, want and true or false)
    end

    -- The section switches follow from the options, so recount() below is what
    -- puts them right: None leaves them all off without this loop having to say
    -- so, and Default turns off the ones whose section is not fully on.
    AllInfo.OptionsTab.recount(page)
    -- The tally changes width, and the section switch sits right after it.
    AllInfo.OptionsTab.relayout(page)
end
