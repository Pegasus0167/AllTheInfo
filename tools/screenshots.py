"""Normalises the in-game captures into a Workshop screenshot set.

Steam shows every screenshot in one carousel at one size, so a set of crops at
nine different aspect ratios reads as sloppy. Each one is fitted onto the same
1920x1080 frame, centred, on the panel colour the mod's own art uses, so the
set looks like one thing.

Nothing is cropped to fill: letterboxing loses no content, and content is the
whole point of these shots. The only crop is the bed one, and it is there to
cut the debug entries out of the context menu.

Order is carousel order. The generator goes first because it is the only shot
that reads at thumbnail size; the rest are panels of text that need a click.
"""
import os
from PIL import Image

SRC = r"C:\Users\alexp\Pictures\Screenshots"
OUT = r"C:\Users\alexp\Desktop\Proyectos y cosas mias\PZ_InfoMod\workshop\screenshots"

W, H = 1920, 1080
BG = (16, 18, 22)
LIMIT = 2 * 1024 * 1024   # Steam refuses anything over 2 MB


def shot(n):
    return os.path.join(SRC, "Captura de pantalla 2026-08-11 %s.png" % n)


# (source, output name, crop or None). The number comes from the position, so
# dropping a line renumbers everything below it.
SET = [
    ("153736", "generator_range", None),
    # The three inventory shots have the character standing in dead space to
    # the right. Cropped at the panel edge, the tooltip lands about twice as
    # large in the frame, which is the difference between readable and not.
    # Cropped shorter than the panel as well: at full height this one fitted
    # at x1.92 while the other two inventory shots landed at x2.26, so its
    # text came out visibly smaller in the carousel. 492 clears the tooltip
    # by a few pixels and puts the scale at x2.20.
    ("153903", "firearm_compare", (0, 0, 745, 492)),
    ("153149", "traits_and_professions", None),
    ("153256", "melee_compare", (0, 0, 727, 477)),
    ("153245", "clothing_compare", (0, 0, 727, 482)),
    ("153800", "options_tab", None),
    # The top four rows of this context menu are debug entries (Tile Report,
    # Coordinates, Seed, Debug). Cropped away: they make it look like a dev
    # screenshot rather than a mod screenshot.
    ("154146", "bed_rest_quality", (520, 585, 1420, 821)),

    # Held back on purpose, both to be retaken:
    #   ("153529", "skill_levels", None)      Lightfooted has no recipes, so the
    #       shot misses the per-level recipe list, which is the point of the
    #       feature. Retake on Carpentry level 3 or 4.
    #   ("153937", "crafting_output", None)   The tooltip lands over the panel
    #       and PZ's translucent tooltip background lets the text underneath
    #       bleed through. Retake with the tooltip over an empty area.
]

def save(frame, stem):
    """PNG while it fits, JPEG when it does not.

    The UI shots are flat colour and compress fine as PNG. The world renders do
    not: the generator one is 3.2 MB. Reducing it to a 256-colour palette would
    band the grass; JPEG at 95 with no chroma subsampling comes out the same
    size and leaves the tooltip text clean, so that is the fallback.
    """
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

for order, (src, name, crop) in enumerate(SET, 1):
    im = Image.open(shot(src)).convert("RGB")
    if crop:
        im = im.crop(crop)

    scale = min(W / im.width, H / im.height)
    im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)

    frame = Image.new("RGB", (W, H), BG)
    frame.paste(im, ((W - im.width) // 2, (H - im.height) // 2))

    path = save(frame, os.path.join(OUT, "%02d_%s" % (order, name)))
    print("%-34s %5.2f MB  (fuente %s, escala %.2f)"
          % (os.path.basename(path), os.path.getsize(path) / 1048576, src, scale))

print("\n-> " + OUT)
