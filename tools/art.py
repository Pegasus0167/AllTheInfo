"""AllTheInfo title art.

The mod's whole pitch is "vanilla draws a bar, we write the number on it", so
the art is that: a tooltip panel with real rows, one of them a bare bar with
the figure written over it. Palette taken from the game's own UI -- near-black
panel, thin grey frame, white text, and the good/bad highlight greens and reds
AllInfo.color() actually uses.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT = r"C:\Users\alexp\Desktop\Proyectos y cosas mias\PZ_InfoMod\workshop"

W = H = 512
BG = (16, 18, 22)
FRAME = (58, 63, 71)
WHITE = (236, 238, 240)
GREY = (138, 145, 155)
GREEN = (122, 189, 78)
RED = (196, 78, 66)
BAR_BG = (38, 41, 47)

F = "C:/Windows/Fonts/"
black = lambda s: ImageFont.truetype(F + "ariblk.ttf", s)
bold = lambda s: ImageFont.truetype(F + "arialbd.ttf", s)
plain = lambda s: ImageFont.truetype(F + "arial.ttf", s)


def text_w(d, s, f):
    b = d.textbbox((0, 0), s, font=f)
    return b[2] - b[0]


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# Soft glow behind the title, so the thumbnail does not read as a flat rectangle.
glow = Image.new("RGB", (W, H), BG)
ImageDraw.Draw(glow).ellipse((-40, 40, W + 40, 300), fill=(30, 40, 34))
img = Image.blend(img, glow.filter(ImageFilter.GaussianBlur(70)), 0.85)
d = ImageDraw.Draw(img)

# Tooltip frame, 1 px like the game's own.
d.rectangle((14, 14, W - 15, H - 15), outline=FRAME, width=2)

# --- Title ----------------------------------------------------------------
# "Info" in the good-highlight green: that is the colour the mod uses for a
# value that improved, and it is what the eye lands on at thumbnail size.
parts = [("All", WHITE), ("The", GREY), ("Info", GREEN)]
size = 92
while True:
    f = black(size)
    total = sum(text_w(d, p, f) for p, _ in parts)
    if total <= W - 90 or size <= 40:
        break
    size -= 2

x = (W - total) // 2
y = 108
for part, colour in parts:
    d.text((x + 2, y + 3), part, font=f, fill=(0, 0, 0))
    d.text((x, y), part, font=f, fill=colour)
    x += text_w(d, part, f)

sub = "THE NUMBERS THE GAME HIDES"
fs = bold(19)
d.text(((W - text_w(d, sub, fs)) // 2, y + size + 22), sub, font=fs, fill=GREY,
       features=None)

# --- Separator, the same 1 px rule Render.lua draws ------------------------
d.line((60, 258, W - 60, 258), fill=(90, 96, 104))

# --- Mock tooltip rows ----------------------------------------------------
fl = bold(21)
fv = bold(21)
fd = bold(18)

rows = [
    ("Condition", "32 / 45", "(+13)", GREEN),
    ("Damage", "1.20 - 2.40", "(-0.35)", RED),
    ("Jam chance", "0.84%", None, None),
]

ry = 284
for label, value, delta, dcol in rows:
    d.text((62, ry), label, font=fl, fill=WHITE)
    right = W - 62
    if delta:
        dw = text_w(d, delta, fd)
        d.text((right - dw, ry + 2), delta, font=fd, fill=dcol)
        right -= dw + 14
    vw = text_w(d, value, fv)
    d.text((right - vw, ry), value, font=fv, fill=WHITE)
    ry += 37

# The point of the mod, drawn literally: vanilla's bare bar, with the figure
# written on top of it.
by = ry + 16
d.text((62, by - 2), "Insulation", font=fl, fill=WHITE)
bx0, bx1 = 250, W - 62
d.rectangle((bx0, by + 2, bx1, by + 22), fill=BAR_BG)
d.rectangle((bx0, by + 2, bx0 + int((bx1 - bx0) * 0.62), by + 22), fill=(70, 104, 60))
num = "62.0%"
d.text((bx0 + (bx1 - bx0 - text_w(d, num, fv)) // 2, by), num, font=fv, fill=WHITE)

# --- Footer ---------------------------------------------------------------
foot = "PROJECT ZOMBOID  ·  BUILD 42"
ff = bold(16)
d.text(((W - text_w(d, foot, ff)) // 2, H - 48), foot, font=ff, fill=(96, 102, 112))

os.makedirs(OUT, exist_ok=True)
main = os.path.normpath(os.path.join(OUT, "AllTheInfo.png"))
img.save(main)
print(main, img.size)

# The two sizes the game itself wants, from the same source.
img.resize((256, 256), Image.LANCZOS).save(os.path.normpath(os.path.join(OUT, "AllTheInfo_poster_256.png")))
print(os.path.normpath(os.path.join(OUT, "AllTheInfo_poster_256.png")), "(256, 256)")
