"""Puts the AllTheInfo title over the mascot art.

Two versions, because the source has an opaque off-white background and the
title's first word is white:

  light  the mascot as it is, with "All" in near-black so it can be read
  dark   the mascot flood-filled onto the mod's own panel colour, with the
         three title colours exactly as they are in tools/art.py

The canvas grows upward instead of squeezing the title into the 209 px of
existing margin: the centre of that margin is the gap between the ears, not
free space.
"""
import os
from PIL import Image, ImageDraw, ImageFont

SRC = r"C:\Users\alexp\Desktop\ChatGPT Image 11 ago 2026, 15_10_34.png"
OUT = r"C:\Users\alexp\Desktop\Proyectos y cosas mias\PZ_InfoMod\workshop"

WHITE = (236, 238, 240)
GREY = (138, 145, 155)
GREEN = (122, 189, 78)
DARK = (16, 18, 22)
INK = (26, 28, 32)          # the "All" colour on a light background
GREY_ON_LIGHT = (120, 126, 136)
PAD_TOP = 212               # makes the canvas square at 1254

F = "C:/Windows/Fonts/"


def text_w(d, s, f):
    b = d.textbbox((0, 0), s, font=f)
    return b[2] - b[0]


def title(img, parts, sub, sub_colour, shadow):
    """Title block centred in the empty band above the artwork."""
    d = ImageDraw.Draw(img)

    size = 150
    while True:
        f = ImageFont.truetype(F + "ariblk.ttf", size)
        total = sum(text_w(d, p, f) for p, _ in parts)
        if total <= img.width - 200 or size <= 60:
            break
        size -= 2

    fs = ImageFont.truetype(F + "arialbd.ttf", max(20, size // 4))
    block = size + 34 + (fs.size + 4)
    y = (PAD_TOP + 209 - block) // 2

    x = (img.width - total) // 2
    for part, colour in parts:
        if shadow:
            d.text((x + 3, y + 4), part, font=f, fill=shadow)
        d.text((x, y), part, font=f, fill=colour)
        x += text_w(d, part, f)

    d.text(((img.width - text_w(d, sub, fs)) // 2, y + size + 30), sub, font=fs, fill=sub_colour)
    return img


def canvas(background):
    src = Image.open(SRC).convert("RGB")
    out = Image.new("RGB", (src.width, src.height + PAD_TOP), background)
    out.paste(src, (0, PAD_TOP))
    return out


SUB = "THE NUMBERS THE GAME HIDES"
os.makedirs(OUT, exist_ok=True)
paths = []

# --- light: the artwork untouched -----------------------------------------
light = canvas(Image.open(SRC).convert("RGB").getpixel((5, 5)))
light = title(light, [("All", INK), ("The", GREY_ON_LIGHT), ("Info", GREEN)], SUB,
              GREY_ON_LIGHT, shadow=None)
p = os.path.join(OUT, "AllTheInfo_mascot_light.png")
light.save(p); paths.append((p, light.size))

# --- dark: same three colours as the other art ----------------------------
# Flood fill from the corners rather than keying by colour: the mascot has a
# white sticker stroke of its own, and keying white would eat it. The black
# outer line stops the fill.
dark = canvas(DARK)
fill = ImageDraw.floodfill
for corner in ((2, PAD_TOP + 2), (dark.width - 3, PAD_TOP + 2),
               (2, dark.height - 3), (dark.width - 3, dark.height - 3)):
    fill(dark, corner, DARK, thresh=40)
dark = title(dark, [("All", WHITE), ("The", GREY), ("Info", GREEN)], SUB, GREY, shadow=(0, 0, 0))
p = os.path.join(OUT, "AllTheInfo_mascot_dark.png")
dark.save(p); paths.append((p, dark.size))

for p, size in paths:
    print(os.path.normpath(p), size)
