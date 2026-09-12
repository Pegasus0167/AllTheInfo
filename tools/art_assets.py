"""Derives the three shipped images from the mascot art.

  workshop/preview.png   the Steam Workshop thumbnail. **Exactly 256x256** --
                         the game's own uploader refuses anything else with
                         "The preview.png file must be exactly 256x256 pixels
                         in size." That is a Project Zomboid rule, not a Steam
                         one; Steam itself takes far larger, so a nicer image
                         can be swapped in from the Workshop page afterwards.
  mod/42.20/poster.png   256x256, the picture in the game's own mod list.
  mod/42.20/icon.png     32x32, the tiny one next to the name in that list.
                         The whole composition is mush at 32 px, so this is a
                         crop of the face alone.

Run it again after changing SRC; nothing here is committed by hand.
"""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "workshop", "AllTheInfo_mascot_light_1024.png")

# The face, in source pixels. Measured off the 1024 art: ears to chin, with the
# raised paw deliberately outside so the crop reads as a head and not a shape.
FACE = (250, 380, 880, 1010)


def save(img, path):
    img.save(path, "PNG", optimize=True)
    print("%-42s %sx%s  %d bytes"
          % (os.path.relpath(path, ROOT), img.width, img.height, os.path.getsize(path)))


def main():
    src = Image.open(SRC).convert("RGBA")
    small = src.resize((256, 256), Image.LANCZOS)

    save(small, os.path.join(ROOT, "workshop", "preview.png"))
    save(small, os.path.join(ROOT, "mod", "42.20", "poster.png"))
    save(src.crop(FACE).resize((32, 32), Image.LANCZOS), os.path.join(ROOT, "mod", "42.20", "icon.png"))


if __name__ == "__main__":
    main()
