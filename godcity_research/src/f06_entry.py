import sys; sys.path.insert(0,"/home/user/NetflixProject/godcity_research/src")
from style import *
import numpy as np, matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

# ============================ F6  entry ticket for a ~600 sq yd villa plot
ITEMS = [  # label, low(₹L), high(₹L), colour, evidence class
 ("Raw agricultural land, interior\nSindhudurg (Vaibhavwadi / Devgad)",  4.9,  8.2, "#9AA5A2", "obs"),
 ("Raw land with road frontage\n(Kudal / Malvan belt)",                 11.9, 20.0, TEAL_L,    "obs"),
 ("Unorganised N.A. plot\n(Kudal / Sawantwadi)",                        20.5, 34.6, TEAL,      "int"),
 ("Gated layout plot, Mopa side\n(Sawantwadi — e.g. Cida De Luxora)",   42.0, 57.0, TEAL_D,    "obs"),
 ("Positioned “luxury township” plot\n(God City — price NOT published)",45.0,140.0, TERRA,     "unk"),
 ("Comparable villa plot,\nNorth Goa",                                 150.0,200.0, PLUM,      "mkt"),
]
fig = plt.figure(figsize=(10.2, 6.4))
ax = fig.add_axes([0.275, 0.235, 0.505, 0.565])
ys = np.arange(len(ITEMS))[::-1]
for y, (lab, lo, hi, c, ev) in zip(ys, ITEMS):
    if ev == "unk":
        ax.plot([lo, hi], [y, y], color=c, lw=11, solid_capstyle="round",
                alpha=0.18, zorder=3)
        ax.plot([lo, hi], [y, y], color=c, lw=1.4, ls=(0,(4,3)), zorder=4)
        ax.text((lo+hi)/2, y + 0.34, "no published price band", fontsize=7.2,
                color=c, ha="center", va="bottom", fontweight="bold", zorder=6)
        ax.text((lo+hi)/2, y - 0.36, "bar drawn to span the plausible range, not to assert one",
                fontsize=6.4, color=c, ha="center", va="top", style="italic", zorder=6)
    else:
        ax.plot([lo, hi], [y, y], color=c, lw=11, solid_capstyle="round", zorder=3)
        ax.text(hi + 4, y, f"₹{lo:,.0f}–{hi:,.0f} L", fontsize=7.8, color=c,
                va="center", fontweight="bold", zorder=6)
ax.set_yticks(ys); ax.set_yticklabels([i[0] for i in ITEMS], fontsize=7.8, linespacing=1.5)
ax.set_xlim(0, 232); ax.set_ylim(-0.7, len(ITEMS)-0.3)
ax.set_xlabel("All-in land cost for a ~600 sq yd (≈5,400 sq ft) villa plot — ₹ lakh, excluding stamp duty, registration and construction")
frame(ax, left=False, grid="x")
ax.tick_params(axis="y", labelcolor=INK)
ax.set_xticks(range(0, 240, 40))

ax.annotate("", xy=(42, 2.62), xytext=(16, 4.42),
            arrowprops=dict(arrowstyle="-|>", color=TERRA, lw=1.4,
                            connectionstyle="arc3,rad=0.30"), zorder=8)
ax.text(96, 4.62, "The whole commercial question in one gap:\n"
        "a buyer pays roughly 3–5× the frontage-land rate for\n"
        "servicing, layout approval, amenity and brand.",
        fontsize=7.4, color=TERRA, va="top", linespacing=1.6, zorder=8)

fig.text(0.275, 0.148,
 "Where God City's band sits is unknown, and that is the point.  The promoter publishes a 150-acre scale, a Hafeez Contractor master plan and "
 "a\nGoa-adjacent location, but no rate card, no plot schedule and no MahaRERA registration. The dashed bar above is drawn wide deliberately: it "
 "spans\neverything from “Sawantwadi gated layout pricing” to “Goa-substitute pricing”, and nothing in the public domain narrows it.",
 fontsize=7.3, color="#7A5409", va="top", linespacing=1.75,
 bbox=dict(boxstyle="round,pad=0.6", fc="#FFF6E8", ec=AMBER, lw=0.9))
h = [plt.Line2D([],[],color=TEAL,lw=8,label="Anchored to observed listings"),
     plt.Line2D([],[],color=TEAL,lw=8,alpha=0.45,label="Interpolated from anchors"),
     plt.Line2D([],[],color=PLUM,lw=8,label="Developer-marketing figure"),
     plt.Line2D([],[],color=TERRA,lw=1.4,ls=(0,(4,3)),label="No published price")]
ax.legend(handles=h, loc="upper left", bbox_to_anchor=(-0.34, 1.045), ncol=4,
          columnspacing=1.9, handlelength=1.6)
titleblock(fig, "Figure 6 · What it actually costs to get in — the same 600 sq yd, six rungs of the ladder",
  "Converted to a single comparable unit so the rungs can be read against each other. The North Goa figure is the developer's own\n"
  "comparison and should be treated as marketing, not as an independent valuation.")
source(fig, "Sources: Kudal and Malvan listing data (99acres, RealEstateIndia, 2025–26) converted at 1 guntha = 1,089 sq ft; published Mopa-side gated-layout rates of ₹7,000–9,500 per sq yd; SSL Realty / Cida De Luxora "
            "published pricing of ₹45–55 lakh for\n600+ sq yd plots and its own stated North Goa comparison of ₹1.5–2.0 crore. God City LLP publishes no price. Figures exclude stamp duty (on the higher of agreement value or ready-reckoner rate), 1% registration, "
            "GST where applicable, development charges and construction.")
save(fig, "f06_entry_ticket")
