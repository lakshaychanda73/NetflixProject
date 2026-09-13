import sys; sys.path.insert(0,"/home/user/NetflixProject/godcity_research/src")
from style import *
import numpy as np, matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle

# ============================ F18  district fundamentals + seasonality
fig = plt.figure(figsize=(11.0, 8.5))

TILES = [
 ("5,207", "km² district area", TEAL_D),
 ("8", "talukas · 748 villages", TEAL_D),
 ("8.50 lakh", "population (Census 2011)", TEAL),
 ("163", "persons per km²", TEAL),
 ("1,036", "sex ratio — vs 929 statewide", GREEN),
 ("85.6%", "literacy — vs 82.3% statewide", GREEN),
 ("~4,608 mm", "annual rainfall", BLUE),
 ("23", "MahaRERA projects in abeyance", RED),
]
for i, (big, small, col) in enumerate(TILES):
    x = 0.020 + (i % 4) * 0.2455
    y = 0.672 - (i // 4) * 0.142
    a = fig.add_axes([x, y, 0.222, 0.122]); a.axis("off")
    a.set_xlim(0,1); a.set_ylim(0,1)
    a.add_patch(Rectangle((0,0),1,1, fc=PAPER_W, ec=RULE, lw=0.8))
    a.add_patch(Rectangle((0,0.93),1,0.07, fc=col, ec="none"))
    a.text(0.5, 0.60, big, fontsize=16.5, fontweight="bold", color=col,
           ha="center", va="center")
    a.text(0.5, 0.25, small, fontsize=7.4, color=INK_SOFT, ha="center", va="center")

# rainfall / usability seasonality
ax = fig.add_axes([0.020, 0.100, 0.540, 0.330])
M = ["Jun","Jul","Aug","Sep","Oct","Nov","Dec","Jan","Feb","Mar","Apr","May"]
RAIN = [880, 1450, 1150, 620, 240, 55, 15, 5, 4, 8, 30, 150]
x = np.arange(12)
ax.bar(x, RAIN, width=0.64, color=[BLUE if r > 200 else TEAL_XL for r in RAIN],
       edgecolor="none", zorder=3)
ax.set_xticks(x); ax.set_xticklabels(M)
ax.set_ylabel("indicative rainfall, mm")
ax.set_ylim(0, 1900)
frame(ax)
ax.add_patch(Rectangle((-0.45, 0), 4.4, 1900, fc=BLUE, alpha=0.055, zorder=1))
ax.add_patch(Rectangle((8.55, 0), 2.9, 1900, fc=TERRA, alpha=0.075, zorder=1))
ax.text(1.75, 1830, "MONSOON\nbuilding and site visits stop", fontsize=7.2,
        color=BLUE, ha="center", va="top", fontweight="bold", linespacing=1.5)
ax.text(10.0, 1830, "DRY SEASON\nwater stress", fontsize=7.2, color=TERRA,
        ha="center", va="top", fontweight="bold", linespacing=1.5)
ax.text(6.3, 1830, "the ~7-month\nworking window", fontsize=7.2, color=GREEN,
        ha="center", va="top", fontweight="bold", linespacing=1.5)
ax.set_title("Seasonality — why Konkan build programmes slip, and why April–May site visits mislead",
             fontsize=8.8, fontweight="bold", loc="left", pad=8)

pan = fig.add_axes([0.600, 0.095, 0.392, 0.395]); pan.axis("off")
pan.set_xlim(0,1); pan.set_ylim(0,1)
pan.text(0, 1.0, "READING THE FUNDAMENTALS", fontsize=7.8, fontweight="bold",
         color=TEAL_D, va="top")
pan.plot([0,1],[0.955,0.955], color=RULE, lw=0.8, clip_on=False)
pan.text(0, 0.900,
 "Sindhudurg is small, sparsely populated and unusually well-educated,\n"
 "with a sex ratio far above the state average — the classic signature of\n"
 "long-run out-migration of working-age men to Mumbai and Goa.\n\n"
 "That matters commercially. Local end-user demand for premium housing\n"
 "is thin, so a township here sells almost entirely to outside buyers, and\n"
 "its absorption tracks sentiment in Mumbai and Pune rather than anything\n"
 "happening in the district itself.\n\n"
 "The rainfall profile is not a footnote either. Roughly four-fifths of the\n"
 "~4,608 mm arrives in four months, compressing earthworks, roads and\n"
 "services into a seven-month season — which makes a twelve-month\n"
 "construction programme arithmetically impossible. Then the district runs\n"
 "short in April and May, so a buyer who inspects in the pleasant dry\n"
 "months sees neither how the site drains nor how it holds water.\n\n"
 "And 23 registrations already sit in abeyance in this one district.\n"
 "Execution attrition here is the norm, not the exception.",
 fontsize=7.2, color=INK_SOFT, va="top", linespacing=1.72)

titleblock(fig, "Figure 18 · District fundamentals — and the two seasonal facts most decks leave out",
  "Sindhudurg's demographics explain who a township here can realistically sell to; its rainfall explains why building it takes\n"
  "longer than a spreadsheet assumes.")
source(fig, "Sources: Census of India 2011 for area, population, density, sex ratio and literacy; Sindhudurg district administration for administrative divisions; district rainfall reported at ~4,608 mm. The monthly distribution shown is an indicative "
            "south-west monsoon profile for the Konkan coast,\nnot a station record for a specific year. MahaRERA abeyance count as reported for Sindhudurg district.")
save(fig, "f18_fundamentals")
