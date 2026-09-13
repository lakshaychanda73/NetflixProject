import sys; sys.path.insert(0,"/home/user/NetflixProject/godcity_research/src")
from style import *
import numpy as np, matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

# =============================================== F2 travel-time compression
modes = [
 ("Road · Mumbai → Sindhudurg\nNH-66 corridor", 12.5, 6.0, TERRA,
  "NH-66 four-laning: district stretch ~99% complete;\nfull Panvel–Sindhudurg corridor targeted end-2026 / early-2027"),
 ("Sea · Mumbai → Vijaydurg\nRo-Ro ferry (M2M Princess)", 12.0, 6.5, BLUE,
  "Live since 1 Mar 2026. ₹2,500 economy / ₹4,000 premium;\ncar ₹6,000. 390 pax + 21 cars on day one"),
 ("Air · Mumbai → Sindhudurg\nvia Chipi (SDW)", 12.5, 1.2, GREEN,
  "NOT YET AVAILABLE. The 15 Aug 2026 Navi Mumbai–Chipi\nstart date passed with no service; only PNQ, HYD, BLR fly"),
 ("Air · Delhi/Bengaluru → Goa\nMopa (GOX) + ~1 h road", 9.0, 3.5, PLUM,
  "The corridor's real air gateway today.\nMopa is ~14 km from Sawantwadi"),
]
LIVE = [True, True, False, True]   # is the "after" state actually available today?
fig = plt.figure(figsize=(9.6, 5.5))
ax = fig.add_axes([0.255, 0.150, 0.505, 0.640])
ys = np.arange(len(modes))[::-1]
for y, (lab, a, b, c, note), live in zip(ys, modes, LIVE):
    if live:
        ax.plot([b, a], [y, y], color=RULE, lw=5.5, solid_capstyle="round", zorder=2)
        ax.plot([b, a], [y, y], color=c, lw=5.5, solid_capstyle="round",
                zorder=3, alpha=0.22)
        ax.plot([b], [y], marker="o", ms=10.5, mfc=c, mec=PAPER, mew=1.6, zorder=6)
        ax.text(b - 0.35, y, f"{b:g} h", fontsize=9.0, color=c, va="center",
                ha="right", fontweight="bold", zorder=7)
    else:
        ax.plot([b, a], [y, y], color=RED, lw=1.5, ls=(0,(4,3)), zorder=3, alpha=0.55)
        ax.plot([b], [y], marker="o", ms=10.5, mfc=PAPER, mec=RED, mew=1.6,
                zorder=6, ls="none")
        ax.plot([b], [y], marker="x", ms=6.0, mec=RED, mew=1.6, zorder=7, ls="none")
        ax.text(b - 0.35, y, f"({b:g} h)", fontsize=8.4, color=RED, va="center",
                ha="right", fontweight="bold", zorder=7)
        ax.text(b + 0.30, y - 0.30, "advertised, not operating", fontsize=6.7,
                color=RED, va="center", ha="left", style="italic", zorder=7)
    ax.plot([a], [y], marker="o", ms=9.5, mfc=PAPER, mec=INK_SOFT, mew=1.6, zorder=5)
    ax.text(a + 0.35, y, f"{a:g} h", fontsize=8.0, color=INK_SOFT, va="center", zorder=7)
    ax.text(14.6, y + 0.19, note, fontsize=6.9,
            color=RED if not live else INK_SOFT, va="center",
            ha="left", linespacing=1.55, zorder=7)
ax.set_yticks(ys); ax.set_yticklabels([m[0] for m in modes], fontsize=8.0, linespacing=1.5)
ax.set_xlim(0, 14.2); ax.set_ylim(-0.62, len(modes) - 0.38)
ax.set_xlabel("Door-to-door journey time from Mumbai (hours)")
frame(ax, left=False, grid="x")
ax.tick_params(axis="y", labelcolor=INK)
h = [plt.Line2D([],[],ls="none",marker="o",ms=8,mfc=PAPER,mec=INK_SOFT,mew=1.5,label="Legacy journey time"),
     plt.Line2D([],[],ls="none",marker="o",ms=8,mfc=TEAL,mec=PAPER,mew=1.5,label="Available today"),
     plt.Line2D([],[],ls="none",marker="o",ms=8,mfc=PAPER,mec=RED,mew=1.5,label="Announced but not operating")]
ax.legend(handles=h, loc="lower left", bbox_to_anchor=(-0.02, 1.03), ncol=3,
          columnspacing=2.2)
titleblock(fig, "Figure 2 · The access story — how far it has actually moved, mode by mode",
  "Sindhudurg's investment case rests almost entirely on time-compression from Mumbai and Pune. Three of the four channels have\n"
  "genuinely improved. The fourth — the direct Mumbai air link that would matter most to a weekend-home buyer — has not started.")
source(fig, "Sources: NHAI / MSRDC progress reporting on NH-66 Panvel–Sindhudurg; Maharashtra Maritime Board and operator announcements for the Mumbai–Vijaydurg Ro-Ro (launched 1 March 2026); "
            "Fly91 published schedules and\nSindhudurg Airport (SDW) traffic data; Airports Authority of India / Manohar International Airport (GOX) for the Goa gateway. Journey times are typical door-to-door estimates, not timetable times.")
save(fig, "f02_traveltime")

# =============================================== F3 Chipi traffic
fig = plt.figure(figsize=(9.6, 5.4))
ax1 = fig.add_axes([0.075, 0.300, 0.385, 0.500])
ax2 = fig.add_axes([0.585, 0.300, 0.385, 0.500])
yrs = ["FY 2023-24", "FY 2024-25", "FY 2025-26"]
pax = [None, 14_650, 73_022]
mv  = [None, 522, 1_566]
def growthbars(ax, vals, colr, ttl, unit, note):
    x = np.arange(3)
    shown = [0 if v is None else v for v in vals]
    bars = ax.bar(x, shown, width=0.56, color=[RULE, colr, colr],
                  edgecolor="none", zorder=3)
    bars[1].set_alpha(0.42)
    for i, v in enumerate(vals):
        if v is None:
            ax.text(i, max(shown) * 0.035, "not\ncomparable", fontsize=6.8,
                    color=INK_SOFT, ha="center", va="bottom", linespacing=1.5)
        else:
            ax.text(i, v + max(shown) * 0.035, f"{v:,}", fontsize=8.6,
                    color=colr if i == 2 else INK_SOFT, ha="center",
                    fontweight="bold" if i == 2 else "normal")
    ax.annotate("", xy=(2, max(shown)*0.72), xytext=(1, max(shown)*0.30),
                arrowprops=dict(arrowstyle="-|>", color=colr, lw=1.5,
                                connectionstyle="arc3,rad=-0.28"), zorder=5)
    ax.text(1.52, max(shown)*0.80, note, fontsize=9.4, color=colr,
            fontweight="bold", ha="center", zorder=6)
    ax.set_xticks(x); ax.set_xticklabels(yrs)
    ax.set_title(ttl, fontsize=9.2, fontweight="bold", loc="left", pad=9)
    ax.set_ylabel(unit); frame(ax)
    ax.set_ylim(0, max(shown) * 1.24)
growthbars(ax1, pax, TEAL, "Passengers handled", "passengers", "+398%")
growthbars(ax2, mv, TERRA, "Aircraft movements", "movements", "+200%")
fig.text(0.075, 0.075,
  "Read the base, not just the rate.  73,022 passengers in a year is roughly 200 a day — about three flights, on one "
  "carrier, to three cities, none of\nthem Mumbai. A ~400% increase off a near-dormant base is a restart, not yet a market. "
  "The honest reading is that air access to Sindhudurg\nis early-stage and single-operator — which is an opportunity if it "
  "deepens, and a concentration risk while it does not.",
  fontsize=7.4, color="#7A5409", va="bottom", linespacing=1.7,
  bbox=dict(boxstyle="round,pad=0.55", fc="#FFF6E8", ec=AMBER, lw=0.9))
titleblock(fig, "Figure 3 · Sindhudurg (Chipi) airport — spectacular growth rate, very small absolute base",
  "The single most-quoted statistic in Sindhudurg sales decks, shown with the denominator attached.")
source(fig, "Source: Sindhudurg Airport (SDW) traffic statistics for April 2025 – March 2026, reported as 73,022 passengers (+398.48%) and 1,566 aircraft movements (+200%). "
            "FY 2024-25 figures are back-calculated from those\npublished growth rates and are therefore approximate. FY 2023-24 is not shown: the airport's service pattern in that year makes it a non-comparable base.")
save(fig, "f03_chipi")
