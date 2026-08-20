"""images.py — photograph slots for the deck.

Drop a photograph into ../images/ named after its slot (any of .jpg .jpeg .png
.webp .heic) and it is cropped, resized and placed automatically on the next
build. If a slot is empty the slide falls back to its typography-led layout,
so the deck always builds and always looks deliberate.

    cd deck/build && python3 images.py     # report which slots are filled
    make all                               # place them and rebuild the PDF

EDITORIAL RULE — set by the founder, enforced here:
  Photographs earn their place by supporting the argument on the slide they
  sit on. A picture of the corridor we actually work is evidence. A postcard
  of the Gateway of India is decoration, and worse, it is South Mumbai — the
  market slide 5 argues against entering. Do not fill a slot just because it
  is empty.

Nothing watermarked, nothing stock, nothing credited to a third party.
"""

import os, glob

IMG_DIR = os.path.abspath("../images")
OUT_DIR = os.path.abspath("../figures")
EXTS = (".jpg", ".jpeg", ".png", ".webp", ".heic", ".tif", ".tiff")

# slot -> (out width px, out height px, vertical focal bias, what it must show)
#   focal bias: 0.0 crops to the top of the frame, 0.5 centre, 1.0 bottom.
#   Skylines want a bias above centre so the towers survive the crop.
SLOTS = {
    "s1_corridor": (
        2400, 686, 0.42,
        "Slide 1, dark. A wide band of the Eastern corridor at scale — the Powai "
        "golden-hour panorama. Establishes that the market on the chart is a real "
        "place with real towers in it."),
    "s5_corridor": (
        1180, 1560, 0.38,
        "Slide 5, light. A tall rail beside the priced locality ladder. Powai lake "
        "with the Hiranandani towers behind it: the exact six-locality spine the "
        "slide argues for."),
    "s12_founder": (
        1000, 1220, 0.30,
        "Slide 12, dark. The founder portrait, beside his own P&L. Bias is high in "
        "the frame so the crop keeps the head and shoulders, not the floor."),
    "s12_jaipur": (
        1180, 780, 0.45,
        "Slide 12, dark, OPTIONAL. Only a Chanda Properties site, scheme or plot — "
        "the endpoint of the arc as an operating asset. Not a fort, not Hawa Mahal, "
        "not a skyline. Leave empty rather than fill it with a postcard."),
}


def source(slot):
    """The source file for a slot, or None."""
    for ext in EXTS:
        hits = sorted(glob.glob(os.path.join(IMG_DIR, slot + ext)))
        if hits:
            return hits[0]
    return None


def have(slot):
    return source(slot) is not None


def placed(slot):
    """Filename of the placed image, relative to ../figures/."""
    return f"img_{slot}.jpg"


def place(slot):
    """Crop and resize the slot's source into ../figures/. Returns True if placed."""
    from PIL import Image, ImageOps

    src = source(slot)
    if not src:
        return False
    w, h, bias, _ = SLOTS[slot]

    im = Image.open(src)
    im = ImageOps.exif_transpose(im)          # honour camera rotation
    im = im.convert("RGB")

    # Crop to the target aspect, keeping the focal band, then resize.
    target = w / h
    sw, sh = im.size
    if sw / sh > target:                       # too wide — trim the sides
        nw = int(round(sh * target))
        left = (sw - nw) // 2
        im = im.crop((left, 0, left + nw, sh))
    else:                                      # too tall — trim to the focal band
        nh = int(round(sw / target))
        top = int(round((sh - nh) * bias))
        top = max(0, min(top, sh - nh))
        im = im.crop((0, top, sw, top + nh))

    im = im.resize((w, h), Image.LANCZOS)
    os.makedirs(OUT_DIR, exist_ok=True)
    im.save(os.path.join(OUT_DIR, placed(slot)), "JPEG", quality=88, optimize=True)
    return True


def place_all():
    done = []
    for slot in SLOTS:
        if place(slot):
            done.append(slot)
    return done


if __name__ == "__main__":
    os.makedirs(IMG_DIR, exist_ok=True)
    print(f"looking in {IMG_DIR}\n")
    for slot, (w, h, bias, note) in SLOTS.items():
        src = source(slot)
        mark = "FILLED " if src else "empty  "
        print(f"  [{mark}] {slot}  ({w}×{h})")
        print(f"            {note}")
        if src:
            place(slot)
            print(f"            <- {os.path.basename(src)}  ->  figures/{placed(slot)}")
        print()
    n = sum(1 for s in SLOTS if have(s))
    print(f"{n} of {len(SLOTS)} slots filled. "
          "Empty slots fall back to the typography-led layout.")
