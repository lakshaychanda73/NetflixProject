"""contact.py — contact sheet of generated figures, for visual QA."""
import sys, glob, os
from PIL import Image

pat = sys.argv[1] if len(sys.argv) > 1 else "*"
cols = int(sys.argv[2]) if len(sys.argv) > 2 else 2
CELL_W = 1000

files = sorted(glob.glob(f"../figures/{pat}.png"))
if not files:
    sys.exit("no files")
ims = []
for f in files:
    im = Image.open(f).convert("RGB")
    h = int(im.height * CELL_W / im.width)
    ims.append((os.path.basename(f), im.resize((CELL_W, h), Image.LANCZOS)))

rows = (len(ims) + cols - 1) // cols
row_h = [max(ims[r * cols + c][1].height for c in range(cols) if r * cols + c < len(ims))
         for r in range(rows)]
sheet = Image.new("RGB", (cols * CELL_W + (cols + 1) * 16,
                          sum(row_h) + (rows + 1) * 16), "#dddddd")
y = 16
for r in range(rows):
    x = 16
    for c in range(cols):
        i = r * cols + c
        if i < len(ims):
            sheet.paste(ims[i][1], (x, y))
        x += CELL_W + 16
    y += row_h[r] + 16
out = f"/tmp/claude-0/-home-user-NetflixProject/b781cc2b-6197-52e0-af1a-4910de612ca8/scratchpad/contact_{pat.replace('*','all')}.png"
sheet.save(out, quality=88)
print(out, sheet.size, len(ims), "figures:", ", ".join(n for n, _ in ims))
