import sys; sys.path.insert(0,"/home/user/NetflixProject/godcity_research/src")
from style import *
import numpy as np, matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

# ================================== F15  what "150 acres" actually contains
SEG = [
 ("Saleable plots, villas and studios", 52.0, TEAL_D,
  "The only land that generates revenue — and the only land a buyer owns."),
 ("Roads, circulation and parking",     19.0, "#6F8A86",
  "Township standards demand real carriageway widths, not village cart tracks."),
 ("Open space, parks and playgrounds",  11.0, GREEN,
  "Statutory reservation under the Integrated Township Policy."),
 ("Social housing (15% of resi. FSI)",   6.0, PLUM,
  "An explicit ITP obligation, expressed here as its land equivalent."),
 ("Clubhouse, amenity and convenience",  5.0, GOLD,
  "The amenity the brochure sells; a cost line until it is built."),
 ("Utilities — STP, WTP, substation",    3.0, BLUE,
  "At ~4,600 mm of rain and a dry April–May, these are not optional."),
 ("Buffers — CRZ, stream, ESA setbacks", 4.0, RED,
  "Unknown until the site is identified. Coastal parcels can lose far more."),
]
fig = plt.figure(figsize=(10.6, 6.9))
ax = fig.add_axes([0.055, 0.545, 0.895, 0.210])
left = 0.0
for name, pct, col, _ in SEG:
    ax.barh([0], [pct], left=left, height=0.62, color=col, edgecolor=PAPER, lw=1.4, zorder=3)
    if pct >= 5:
        ax.text(left + pct/2, 0, f"{pct:g}%", ha="center", va="center",
                fontsize=8.4, color=PAPER, fontweight="bold", zorder=4)
    left += pct
ax.set_xlim(0, 100); ax.set_ylim(-0.45, 1.05)
ax.set_yticks([]); ax.set_xticks(range(0, 101, 10))
ax.set_xticklabels([f"{v}%" for v in range(0, 101, 10)])
frame(ax, left=False, bottom=True, grid="x")
ax.annotate("", xy=(52, 0.52), xytext=(0, 0.52),
            arrowprops=dict(arrowstyle="<|-|>", color=TEAL_D, lw=1.3))
ax.text(26, 0.62, "≈ 78 of the 150 acres are saleable product", fontsize=7.8,
        color=TEAL_D, ha="center", va="bottom", fontweight="bold")
ax.annotate("", xy=(100, 0.52), xytext=(52, 0.52),
            arrowprops=dict(arrowstyle="<|-|>", color=INK_SOFT, lw=1.1))
ax.text(76, 0.62, "≈ 72 acres are obligation, not product", fontsize=7.8,
        color=INK_SOFT, ha="center", va="bottom")

leg = fig.add_axes([0.055, 0.075, 0.895, 0.400]); leg.axis("off")
leg.set_xlim(0,1); leg.set_ylim(0,1)
y = 0.98
for name, pct, col, why in SEG:
    leg.add_patch(Rectangle((0.0, y-0.052), 0.014, 0.046, fc=col, ec="none"))
    leg.text(0.028, y-0.010, name, fontsize=8.0, color=INK, va="center", fontweight="bold")
    leg.text(0.355, y-0.010, f"{pct:g}%", fontsize=8.0, color=col, va="center",
             fontweight="bold", ha="right")
    leg.text(0.385, y-0.010, why, fontsize=7.3, color=INK_SOFT, va="center")
    y -= 0.107
leg.text(0.0, y + 0.020,
 "The headline number is a land area, not an inventory.  A 150-acre township is not 150 acres of product. On the allocation above — "
 "which is\nconventional for an ITP-compliant scheme, not a pessimistic one — roughly half the site is roads, reservations, obligations and buffers. "
 "That matters\ntwice over: it halves the revenue base the developer has to fund the other half from, and it means “150 acres” tells a buyer almost "
 "nothing about how\nmany plots will exist, how big they are, or how much open space will still be there in ten years. Only a sanctioned layout answers that.",
 fontsize=7.4, color="#7A5409", va="top", linespacing=1.75,
 bbox=dict(boxstyle="round,pad=0.6", fc="#FFF6E8", ec=AMBER, lw=0.9))

titleblock(fig, "Figure 15 · What “~150 acres” actually contains once township standards are applied",
  "Indicative land budget for an Integrated Township Project of this scale. Percentages are typical planning norms applied to the\n"
  "promoter's stated area — God City has published no layout, so this is what the number implies, not what has been sanctioned.")
source(fig, "Norms applied from the Maharashtra Integrated Township Policy (minimum 40 ha contiguous, parks/playgrounds/community facility reservations, 15% of residential FSI for social housing) together with conventional plotted-township "
            "planning ratios. The buffer allowance is a\nplaceholder: the true figure depends entirely on the site's CRZ position under the Sindhudurg CZMP, its distance to watercourses, and any Western Ghats ESA overlay — none of which can be established until the survey numbers are disclosed.")
save(fig, "f15_land_budget")

# ============================== F16  capital required vs capital subscribed
STEPS = [
 ("Land\nassembly", 165, TEAL_D),
 ("Duties &\nstatutory", 12, TEAL),
 ("Design &\napprovals", 14, BLUE),
 ("Trunk\ninfrastructure", 96, TERRA),
 ("Amenities &\nclubhouse", 26, GOLD),
 ("Marketing\n& channel", 34, PLUM),
 ("Finance &\ncontingency", 42, "#9AA5A2"),
]
fig = plt.figure(figsize=(10.8, 7.4))
ax = fig.add_axes([0.068, 0.290, 0.600, 0.480])
cum = 0
for i, (lab, v, col) in enumerate(STEPS):
    ax.bar([i], [v], bottom=[cum], width=0.62, color=col, edgecolor="none", zorder=4)
    ax.text(i, cum + v/2, f"₹{v}", ha="center", va="center", fontsize=8.0,
            color=PAPER, fontweight="bold", zorder=5)
    if i > 0:
        ax.plot([i-1+0.31, i-0.31], [cum, cum], color=RULE, lw=0.9, ls=(0,(2,2)), zorder=3)
    cum += v
ax.bar([len(STEPS)], [cum], width=0.62, color=INK, edgecolor="none", zorder=4)
ax.text(len(STEPS), cum/2, f"₹{cum}\ncrore", ha="center", va="center",
        fontsize=9.2, color=PAPER, fontweight="bold", zorder=5, linespacing=1.4)
ax.set_xticks(range(len(STEPS)+1))
ax.set_xticklabels([s[0] for s in STEPS] + ["TOTAL\nREQUIREMENT"],
                   fontsize=7.2, linespacing=1.5)
ax.get_xticklabels()[-1].set_fontweight("bold")
ax.set_ylabel("₹ crore, indicative")
ax.set_ylim(0, cum*1.14)
frame(ax)

pan = fig.add_axes([0.700, 0.085, 0.292, 0.685]); pan.axis("off")
pan.set_xlim(0,1); pan.set_ylim(0,1)
pan.add_patch(Rectangle((0,0.735),1,0.265, fc="#FBEFEE", ec=RED, lw=1.3))
pan.text(0.5, 0.978, "AGAINST WHICH:", fontsize=7.6, fontweight="bold",
         color="#7E2A24", ha="center", va="top")
pan.text(0.5, 0.913, "₹1,00,000", fontsize=20, fontweight="bold", color=RED,
         ha="center", va="center")
pan.text(0.5, 0.858, "total partner contribution\nin God City LLP", fontsize=7.3,
         color="#7E2A24", ha="center", va="top", linespacing=1.6)
pan.text(0.5, 0.793, "a ratio of roughly  1 : 389,000", fontsize=7.8,
         color="#7E2A24", ha="center", va="top", fontweight="bold")
pan.text(0.0, 0.695,
 "This is not, by itself, an accusation.\nDevelopers routinely fund schemes\n"
 "through project-level SPVs, landowner\njoint ventures, development-\n"
 "management agreements, debt and\ncustomer advances — and an LLP's\n"
 "contribution figure says nothing about\nwhat those vehicles hold.\n\n"
 "But that is precisely the point. Some\nother entity must be carrying this, and\n"
 "the buyer has not been told which one,\nor what is on its balance sheet.\n\n"
 "Ask for the funding structure in writing.\nIf the answer is that customer advances\n"
 "will fund the infrastructure, then the\nbuyer is the lender — which is exactly\n"
 "what the 70% escrow rule under RERA\nexists to control.",
 fontsize=7.0, color=INK_SOFT, va="top", linespacing=1.68)

titleblock(fig, "Figure 16 · What a 150-acre township costs to build — and what the named entity is capitalised at",
  "An order-of-magnitude build-up, not a valuation. Every input is an assumption and is stated as one; the purpose is to establish\n"
  "the scale of capital the promise implies, because that scale is the thing a buyer is being asked to trust.")
source(fig, "Assumptions: land at ~₹250 per sq ft across 6.53 million sq ft (150 acres); stamp duty at Maharashtra rates net of the 50% Integrated Township Policy concession, plus registration, N.A. and development charges; "
            "trunk infrastructure at ~₹250 per sq ft over ~55% saleable area;\nmarketing and channel at ~6% of an assumed gross development value; finance and contingency at ~15% of the preceding lines. These are planning-grade figures for establishing magnitude and should not be relied on as a cost plan. "
            "The ₹1,00,000 figure is the total contribution recorded\nagainst GOD CITY LLP (LLPIN ACF-3634) in Ministry of Corporate Affairs data.")
save(fig, "f16_capital")
