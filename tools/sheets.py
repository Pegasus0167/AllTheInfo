"""Grouped Workshop shots: several inventory windows on one 1920x1080 frame.

A visitor scrolling the carousel gives each image about a second, and a single
tooltip does not say "this works on every garment" -- three of them side by side
do. So the sheets group captures that make one point, with a branding cell in
the fourth slot carrying the claim in words.

The window is a fixed size per type -- 715x481 for the inventory, 853x480 for a
container -- and 2x2 of the widest still fits inside 1920x1080, so nothing is
resized: UI text stays pixel-exact, which is the whole reason anyone opens these
images. Cells take the widest window on the sheet and narrower ones sit centred
in them, so a sheet mixing both types still lines up.

Source captures come from encuadrar.py, already cropped to the window frame.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SRC = r"C:\Users\alexp\Desktop\Nueva carpeta (2)\D1\encuadradas"
SRC_RAW = r"C:\Users\alexp\Desktop\Nueva carpeta (2)\D1"
RAW = "Captura de pantalla %s.png"
OUT = r"C:\Users\alexp\Desktop\Proyectos y cosas mias\PZ_InfoMod\workshop\screenshots"

W, H = 1920, 1080
GAP = 28
LIMIT = 2 * 1024 * 1024   # Steam refuses anything over 2 MB

# Palette and fonts are art.py's, so the sheets and the title art read as one set.
BG = (16, 18, 22)
FRAME = (102, 102, 102)   # the game's own 1 px window border
WHITE = (236, 238, 240)
GREY = (138, 145, 155)
GREEN = (122, 189, 78)

F = "C:/Windows/Fonts/"
black = lambda s: ImageFont.truetype(F + "ariblk.ttf", s)
bold = lambda s: ImageFont.truetype(F + "arialbd.ttf", s)

SHEETS = [
    dict(
        name="clothing_sheet",
        heading="CLOTHING, COMPARED",
        # Head, legs, feet: three slots, so the point reads as "any garment"
        # rather than "helmets". The broken sneakers go last because the red
        # column is what sells the comparison.
        shots=["112400_helmets", "112242_jeans_vs_chefpants", "112158_sneakers_vs_boots"],
        lines=[
            "The exact figure where vanilla only draws a bar",
            "Every stat compared against what you have equipped",
            "Defense, insulation, wind and water, speed, condition",
        ],
    ),
    dict(
        name="weapons_sheet",
        heading="WEAPONS, COMPARED",
        # Firearms first: thirteen rows of numbers is the loudest of the three.
        # All three are A-vs-B comparisons, same as the clothing sheet -- the
        # ammo shot was dropped because "used by" is a different feature and it
        # broke the one thing the sheet is supposed to say.
        shots=["120843_shotgun_vs_pistol", "112054_axe_vs_bat", "121611_wrench_vs_hook"],
        lines=[
            "Damage, range, accuracy and jam chance, as numbers",
            "Every stat compared against the weapon in your hands",
            "Condition, knockback and wear per hit, to the decimal",
        ],
    ),
    dict(
        name="food_sheet",
        heading="SPOILAGE, TIMED",
        # Read as a progression: on you, in the fridge, in the freezer. Vanilla
        # gives none of these three a number, so the sheet only works as a set --
        # "1 day 23 hours" means nothing until "Never" is next to it.
        shots=["113649_rabbit_fresh", "130944_rabbit_fridge", "113926_rabbit_freezer"],
        lines=[
            "How long it stays fresh, and how long until it rots",
            "The same item, timed where you actually store it",
            "Calories, carbohydrates, proteins and fat",
        ],
    ),
    dict(
        name="cooking_sheet",
        # Same 3x2 as the reading sheet, and for the same reason: the point is a
        # sequence of four states, not three examples of one thing.
        layout="grid3",
        heading="COOKING, PREDICTED",
        # Container windows are 853x480 and three of those do not fit across
        # 1920, so each is cut at its tooltip's right edge -- 600 clears the
        # widest of the three (585), 680 the oven dials plus their tooltip (665).
        # What goes is the Category column and the Turn on / Settings buttons;
        # the labels say which appliance is running, and the tooltip already
        # quotes the temperature it is working from.
        #
        # The dial shot leads because it is the one that needs the extra width,
        # and the three below then read as a sequence: cold microwave, cold oven,
        # and the same meat once it is cooked and on its way to burnt.
        title_strip=(650, 1, 853, 19),
        wipe=(550, 20, 52),
        raw=[("2026-08-13 085256", (5, 5, 685, 485), "OVEN RUNNING AT 100°C"),
             ("2026-08-13 084605", (6, 9, 606, 489), "MICROWAVE, STILL OFF"),
             ("2026-08-13 084701", (4, 9, 604, 489), "OVEN, STILL OFF"),
             ("2026-08-13 084959", (8, 13, 608, 493), "COOKED, NOW BURNING")],
        lines=[
            "How long it needs, before you even switch the oven on",
            "Microwave, oven or campfire, each with its own ceiling",
            "Live from the dial once it is hot, and when it will burn",
        ],
    ),
    dict(
        name="fishing_sheet",
        # Three tall panels side by side, banner over them: same shape as the
        # crafting sheet, and for the same reason -- the window is 533x615 and
        # two rows of that do not fit in 1080.
        layout="row",
        heading="FISHING, CALCULATED",
        # One row of three, so the whole 533x615 window fits with room to spare:
        # nothing is spliced out and nothing is cut off. Each box is the frame
        # exactly -- the widest tooltip ends at 546 and the frame at 547, so
        # nothing overhangs and no outside world comes along.
        raw=[("2026-08-14 122700", (17, 30, 550, 645),
              "EVERY FACTOR, WITH ITS MULTIPLIER"),
             ("2026-08-14 122752", (31, 21, 564, 636),
              "THE SCALE BEHIND EACH ROW"),
             ("2026-08-14 122911", (15, 16, 548, 631),
              "SIZE, TROPHY, BAITS AND HABITS")],
        # Short, like the crafting sheet's: three bullets on one banner row.
        lines=[
            "What Good and Normal are worth, as multipliers",
            "Bite chance and wait, from factors vanilla hides",
            "Level, size, trophy and baits, species by species",
        ],
    ),
    dict(
        name="sleep_sheet",
        # Four across: the three states are one climb (110 -> 154 -> 161) and
        # the pillow tooltip is where the +5% in the middle of it comes from.
        layout="row",
        heading="SLEEP, RATED",
        # A context menu opens wherever the player clicked, so these three crops
        # of the same panel differ by ~70 px in height. Each box just trims the
        # world back to an even margin around the panel; the shared caption
        # height does the rest.
        raw=[("2026-08-14 125053", (4, 12, 430, 523), "A GOOD BED"),
             ("2026-08-14 125029", (15, 21, 465, 550), "+ NIGHT OWL"),
             ("2026-08-14 125133", (21, 41, 455, 625), "+ A PILLOW"),
             # Cut at 400: the tooltip ends at 380 and the Category column starts
             # well after it, so nothing is sliced mid-word.
             ("2026-08-14 123311", (9, 20, 400, 501), "WHAT THE PILLOW ADDS")],
        lines=[
            "The number behind Good, Average and Bad",
            "Bed, pillow and traits, multiplied into one",
            "What a pillow adds, read off the pillow",
        ],
    ),
    dict(
        name="moodles_sheet",
        # Four different moodles at their worst, ordered by how much they have
        # to say: five lines to thirteen. Four in a row rather than a 2x2 --
        # thirteen lines twice over is taller than 1080 once scaled.
        layout="row",
        # A hover is ~300x300 where the other sheets work with 850 px windows;
        # at 1:1 the four of them would sit in a puddle in the middle of 1080.
        # 1.5 rather than 2 because two of these run to eleven and thirteen
        # lines, and at 2 the row no longer fits across 1920.
        scale=1.5,
        heading="MOODLES, EXPLAINED",
        # Boxed to the hover plus its icon with an even 4 px of grass around it,
        # so crops the player framed by hand read as one set. The heights still
        # differ, and should: that is the moodle having more to say.
        raw=[("2026-08-15 142823", (58, 9, 278, 144), "HUNGER, LEVEL FOUR"),
             ("2026-08-15 142616", (31, 23, 376, 244), "FATIGUE, LEVEL FOUR"),
             ("2026-08-15 143951", (0, 0, 324, 270), "PANIC, LEVEL FOUR"),
             ("2026-08-15 143848", (0, 0, 278, 333), "ENDURANCE, LEVEL FOUR")],
        lines=[
            "Every effect it is having on you, spelled out",
            "A different list at every level it reaches",
            "All 26 moodles, checked against B42.20",
        ],
    ),
    dict(
        name="animals_sheet",
        # Two panels rather than four shots: one animal window plus its hover is
        # 1040 px wide, and two of those do not fit across 1920. So one panel
        # shows the rows and the other shows a row explaining itself.
        layout="row",
        heading="ANIMALS, IN NUMBERS",
        # Boxed to the window frame; the second runs on to take in the hover,
        # which floats outside the window over the world -- as it does in game.
        raw=[("2026-08-18 093811", (17, 11, 697, 532),
              "NINE ROWS OF WORDS, NINE OF NUMBERS"),
             ("2026-08-18 094011", (15, 19, 1056, 540),
              "AND EVERY ONE EXPLAINS ITSELF")],
        lines=[
            "Healthy and Well Fed, as the numbers underneath",
            "Four figures no screen in the game will show you",
            "Every row explains itself when you hover it",
        ],
    ),
    dict(
        name="health_sheet",
        # Three parts, three kinds of wound: a scratch that might turn, a
        # laceration still bleeding, a burn already dressed. One would read as
        # "it times scratches"; three read as "it times whatever you have".
        layout="row",
        heading="WOUNDS, TIMED",
        # Boxed to the panel and run on to the hover, which opens beside the
        # list. Margins are 0 -- panel plus hover is ~600 px and three of those
        # only clear 1920 with nothing to spare.
        raw=[("2026-08-23 163818", (21, 28, 621, 426),
              "SCRATCHED, AND THE INFECTION RISK"),
             ("2026-08-23 163832", (18, 52, 618, 450),
              "LACERATED, AND STILL BLEEDING"),
             ("2026-08-23 163826", (46, 38, 648, 436),
              "BURNED, AND THE BANDAGE CLOCK")],
        lines=[
            "Twenty-two figures vanilla keeps for debug mode",
            "Every wound timed to the minute, in game hours",
            "Bandage, poultice and infection risk, part by part",
        ],
    ),
    dict(
        name="more_sheet",
        heading="AND MUCH MORE",
        # The catch-all, so the carousel does not read as "a clothes and guns
        # mod". Three unrelated item types on purpose: a book, a round and a
        # log have nothing in common except that the mod has a number for each.
        shots=["122550_skill_book", "112951_ammo_762", "113515_log_firewood"],
        lines=[
            "How many pages left, and how long they will take",
            "Which guns take the round you just picked up",
            "How many hours a log actually burns for",
        ],
    ),
    dict(
        name="reading_sheet",
        # Four shots, not three: the point is a progression -- nothing, trait,
        # trait plus glasses, and sitting down -- and dropping any step turns
        # "here is how the number is built" into "here is a number". Four cells
        # plus branding is a 3x2 with the branding two cells wide.
        layout="grid3",
        heading="READING SPEED, MEASURED",
        # These are not window-framed like the other sheets: the tooltip and the
        # character panel live in two overlapping windows, so each crop is one
        # region covering both. Boxes are the Info panel's top edge (which drifts
        # a few px per shot) minus 162, plus 321 -- which clears the highest
        # tooltip and the avatar box, and cuts "Favorite Weapon" and "Zombies
        # Killed", 90 px of nothing to do with reading. Without dropping them two
        # rows of 570 px do not fit in 1080.
        #
        # Labelled because the last step does not show: sitting on the ground is
        # the player sprite out in the world, well outside the crop, so cell four
        # would otherwise be cell three with a different number.
        raw=[("2026-08-12 113320", (0, 75, 555, 558), "NO MODIFIERS"),
             ("2026-08-12 113349", (0, 78, 555, 561), "FAST READER TRAIT"),
             ("2026-08-12 113406", (0, 76, 555, 559), "+ READING GLASSES"),
             ("2026-08-12 113417", (0, 78, 555, 561), "+ SITTING DOWN")],
        lines=[
            "The hours a book still needs, not just its page count",
            "Fast Reader, reading glasses and sitting down, all counted",
            "Your speed as a percentage, updated as you change it",
        ],
    ),
    dict(
        name="crafting_sheet",
        # A Crafting window is ~1300x800 and three of those only fit 2x2 at a
        # scale where the text stops being readable, so this one runs as a
        # banner over three columns of just the result panel -- recipe, Required
        # Items, Outputs and the tooltip, which is all the sheet has to show.
        layout="row",
        heading="OUTPUT, COMPARED",
        shots=["craft_newspaper_hat", "craft_hunting_knife", "craft_wooden_fence"],
        # Kept short: on one row, three sentences the length of the grid sheets'
        # would overrun the banner.
        lines=[
            "Stats before you spend the materials",
            "Compared to what you have equipped",
            "Build strength, now and at Carpentry 10",
        ],
    ),
]


def text_w(d, s, f):
    b = d.textbbox((0, 0), s, font=f)
    return b[2] - b[0]


def branding(sheet, cw, ch):
    """The fourth cell: same size and border as a game window, so the grid is even."""
    cell = Image.new("RGB", (cw, ch), BG)

    # Same green glow as the title art, keeps the cell from reading as a flat box.
    glow = Image.new("RGB", cell.size, BG)
    ImageDraw.Draw(glow).ellipse((-60, 30, cw + 60, 300), fill=(30, 40, 34))
    cell = Image.blend(cell, glow.filter(ImageFilter.GaussianBlur(80)), 0.85)

    d = ImageDraw.Draw(cell)
    d.rectangle((0, 0, cw - 1, ch - 1), outline=FRAME, width=1)

    f = black(72)
    parts = [("All", WHITE), ("The", GREY), ("Info", GREEN)]
    x = (cw - sum(text_w(d, p, f) for p, _ in parts)) // 2
    for part, colour in parts:
        d.text((x + 2, 83), part, font=f, fill=(0, 0, 0))
        d.text((x, 80), part, font=f, fill=colour)
        x += text_w(d, part, f)

    sub, fs = "THE NUMBERS THE GAME HIDES", bold(17)
    d.text(((cw - text_w(d, sub, fs)) // 2, 178), sub, font=fs, fill=GREY)

    d.line((cw // 8, 228, cw - cw // 8, 228), fill=(90, 96, 104))

    fh = bold(30)
    d.text(((cw - text_w(d, sheet["heading"], fh)) // 2, 256), sheet["heading"],
           font=fh, fill=WHITE)

    # Bullets are left-aligned to each other but centred as a block, so the cell
    # works at either window width without the text drifting off to one side.
    fl = bold(20)
    widest = max(text_w(d, line, fl) for line in sheet["lines"])
    # Nothing wraps; a line that overruns would just run off the cell edge.
    assert widest + 22 < cw - 80, "line too long: " + max(sheet["lines"], key=len)
    x0, y = (cw - widest - 22) // 2, 316
    for line in sheet["lines"]:
        d.rectangle((x0, y + 7, x0 + 6, y + 13), fill=GREEN)
        d.text((x0 + 22, y), line, font=fl, fill=(206, 210, 216))
        y += 37

    foot, ff = "PROJECT ZOMBOID  ·  BUILD 42", bold(15)
    d.text(((cw - text_w(d, foot, ff)) // 2, ch - 42), foot, font=ff,
           fill=(96, 102, 112))
    return cell


def banner(sheet, bw, bh):
    """Branding as a wide strip instead of a cell, for the row layout."""
    cell = Image.new("RGB", (bw, bh), BG)
    glow = Image.new("RGB", cell.size, BG)
    ImageDraw.Draw(glow).ellipse((bw // 4, -80, bw - bw // 4, bh - 40), fill=(30, 40, 34))
    cell = Image.blend(cell, glow.filter(ImageFilter.GaussianBlur(90)), 0.85)

    d = ImageDraw.Draw(cell)
    d.rectangle((0, 0, bw - 1, bh - 1), outline=FRAME, width=1)

    f = black(62)
    parts = [("All", WHITE), ("The", GREY), ("Info", GREEN)]
    x = (bw - sum(text_w(d, p, f) for p, _ in parts)) // 2
    for part, colour in parts:
        d.text((x + 2, 29), part, font=f, fill=(0, 0, 0))
        d.text((x, 26), part, font=f, fill=colour)
        x += text_w(d, part, f)

    fh = bold(28)
    d.text(((bw - text_w(d, sheet["heading"], fh)) // 2, 112), sheet["heading"],
           font=fh, fill=WHITE)

    # One row of bullets: each is its own marker-plus-text unit, the row centred.
    fl, gap = bold(20), 44
    units = [(22 + text_w(d, line, fl), line) for line in sheet["lines"]]
    total = sum(w for w, _ in units) + gap * (len(units) - 1)
    assert total < bw - 60, "bullet row too wide: " + str(total)
    x, y = (bw - total) // 2, 172
    for width, line in units:
        d.rectangle((x, y + 7, x + 6, y + 13), fill=GREEN)
        d.text((x + 22, y), line, font=fl, fill=(206, 210, 216))
        x += width + gap

    foot, ff = "THE NUMBERS THE GAME HIDES  ·  PROJECT ZOMBOID  ·  BUILD 42", bold(15)
    d.text(((bw - text_w(d, foot, ff)) // 2, bh - 36), foot, font=ff, fill=(96, 102, 112))
    return cell


def captioned(shot, label, height=None):
    """Shot with the modifier it adds written under it, in the branding's voice.

    A shared height keeps a row's labels on one line even when the crops do not
    come out the same size -- a context menu lands where the player clicked, so
    three shots of the same window can differ by a hundred pixels. The shot sits
    centred in that height rather than hanging from the top.
    """
    h = max(height or 0, shot.height)
    out = Image.new("RGB", (shot.width, h + 24), BG)
    out.paste(shot, (0, (h - shot.height) // 2))
    d, f = ImageDraw.Draw(out), bold(16)
    d.text(((shot.width - text_w(d, label, f)) // 2, h + 5), label, font=f, fill=GREY)
    return out


def save(frame, stem):
    """PNG while it fits, JPEG when it does not -- same rule as screenshots.py."""
    png = stem + ".png"
    frame.save(png, optimize=True)
    if os.path.getsize(png) <= LIMIT:
        return png
    os.remove(png)
    for quality in (95, 92, 88, 84, 80):
        jpg = stem + ".jpg"
        frame.save(jpg, quality=quality, subsampling=0)
        if os.path.getsize(jpg) <= LIMIT:
            return jpg
    return jpg


os.makedirs(OUT, exist_ok=True)

BANNER_H = 250

for sheet in SHEETS:
    if sheet.get("raw"):
        # Cut from an unframed capture, so the crop is given the game's own 1 px
        # border back: on the sheet it then sits like the framed ones.
        strip = sheet.get("title_strip")
        shots = []
        for name, box, label in sheet["raw"]:
            full = Image.open(os.path.join(SRC_RAW, RAW % name)).convert("RGB")
            # A list of boxes stacks them, dropping whatever fell between: rows
            # of a list that are all the same empty "---" cut at their own
            # boundaries, so the seam is invisible and no reading is lost.
            boxes = box if isinstance(box, list) else [box]
            parts = [full.crop(b) for b in boxes]
            shot = Image.new("RGB", (max(p.width for p in parts),
                                     sum(p.height for p in parts)))
            y = 0
            for part in parts:
                shot.paste(part, (0, y))
                y += part.height
            if strip:
                # The container's name and capacity sit at the far right of the
                # title bar, past the cut. Slid back in against the new right
                # edge -- where a narrower window would have put them anyway --
                # because "which appliance" is half of what the sheet claims.
                x0, y0 = boxes[0][0], boxes[0][1]
                bar = full.crop((x0 + strip[0], y0 + strip[1],
                                 x0 + strip[2], y0 + strip[3]))
                shot.paste(bar, (shot.width - bar.width, strip[1]))
            if sheet.get("wipe"):
                # The Category header would be sliced mid-word by the cut. Its
                # own gradient, one empty column of it stretched over the rest of
                # the row, so no cell ends in half a word.
                x, y0, y1 = sheet["wipe"]
                shot.paste(shot.crop((x - 1, y0, x, y1))
                               .resize((shot.width - x, y1 - y0)), (x, y0))
            if sheet.get("scale"):
                # NEAREST rather than a smooth filter: it repeats pixels instead
                # of blending them, so the text stays the text it was, only
                # bigger -- which a moodle hover needs, being a tenth the size of
                # the windows every other sheet is built from.
                s = sheet["scale"]
                shot = shot.resize((int(shot.width * s), int(shot.height * s)),
                                   Image.NEAREST)
            ImageDraw.Draw(shot).rectangle((0, 0, shot.width - 1, shot.height - 1),
                                           outline=FRAME, width=1)
            shots.append((shot, label))
        tall = max(s.height for s, _ in shots)
        shots = [captioned(s, label, tall) for s, label in shots]
    else:
        shots = [Image.open(os.path.join(SRC, s + ".png")).convert("RGB")
                 for s in sheet["shots"]]

    if sheet.get("layout") == "grid3":
        # Branding spans the top-left two cells, so the four shots read left to
        # right, top row then bottom. The bottom row sets the column width and
        # the branding takes whatever the first shot leaves: that lets the shot
        # that needs more width sit on the top row without skewing the grid.
        cw = max(s.width for s in shots[1:])
        ch = max(s.height for s in shots)
        total = cw * 3 + GAP * 2
        assert total <= W and ch * 2 + GAP <= H, "3x2 does not fit " + sheet["name"]
        assert shots[0].width + GAP < total, "lead shot too wide " + sheet["name"]
        ox, oy = (W - total) // 2, (H - (ch * 2 + GAP)) // 2
        pieces = [(branding(sheet, total - shots[0].width - GAP, ch), ox, oy),
                  (shots[0], ox + total - shots[0].width,
                   oy + (ch - shots[0].height) // 2)]
        # Shots shorter than the cell sit centred in it, so a sheet whose crops
        # do not all come out the same height still lines up.
        pieces += [(s, ox + (cw + GAP) * i + (cw - s.width) // 2,
                    oy + ch + GAP + (ch - s.height) // 2)
                   for i, s in enumerate(shots[1:])]
    elif sheet.get("layout") == "row":
        # Panels vary in height, so they hang from a common top edge: the recipe
        # headers line up, which is what the eye compares across the three.
        bw = sum(s.width for s in shots) + GAP * (len(shots) - 1)
        assert bw <= W - 60, "row too wide: " + sheet["name"]
        ox = (W - bw) // 2
        oy = (H - (BANNER_H + GAP + max(s.height for s in shots))) // 2
        pieces = [(banner(sheet, bw, BANNER_H), ox, oy)]
        x = ox
        for shot in shots:
            pieces.append((shot, x, oy + BANNER_H + GAP))
            x += shot.width + GAP
    else:
        # The cell is the widest window on the sheet; a sheet mixing inventory
        # and container windows gets container cells and centres the narrow ones.
        cw = max(s.width for s in shots)
        ch = max(s.height for s in shots)
        assert cw * 2 + GAP <= W and ch * 2 + GAP <= H, "grid does not fit " + sheet["name"]
        ox, oy = (W - (cw * 2 + GAP)) // 2, (H - (ch * 2 + GAP)) // 2
        slots = [(ox, oy), (ox + cw + GAP, oy),
                 (ox, oy + ch + GAP), (ox + cw + GAP, oy + ch + GAP)]
        pieces = [(cell, x + (cw - cell.width) // 2, y + (ch - cell.height) // 2)
                  for cell, (x, y) in zip([branding(sheet, cw, ch)] + shots, slots)]

    frame = Image.new("RGB", (W, H), BG)

    # Drop shadows first, so the windows sit on the frame instead of floating.
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    for im, x, y in pieces:
        md.rectangle((x - 4, y + 4, x + im.width + 4, y + im.height + 12), fill=170)
    frame = Image.composite(Image.new("RGB", (W, H), (0, 0, 0)),
                            frame, mask.filter(ImageFilter.GaussianBlur(16)))

    for im, x, y in pieces:
        frame.paste(im, (x, y))

    path = save(frame, os.path.join(OUT, sheet["name"]))
    print("%-28s %5.2f MB" % (os.path.basename(path), os.path.getsize(path) / 1048576))

print("\n-> " + OUT)
