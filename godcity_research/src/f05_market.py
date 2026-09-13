import sys; sys.path.insert(0,"/home/user/NetflixProject/godcity_research/src")
from style import *
import numpy as np, matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, LogNorm
from matplotlib.patches import Rectangle, FancyBboxPatch

CMAP = LinearSegmentedColormap.from_list("gc", SEQ)

# ============================================ F5  land value ladder heatmap
TAL = ["Vaibhavwadi","Dodamarg","Devgad","Kankavli","Vengurla","Kudal",
       "Malvan","Sawantwadi"]
TIER = ["Interior\nagricultural land","Raw land with\nroad frontage",
        "N.A. plot in an\nunorganised layout","Plot in a developed\ngated layout",
        "Sea-view / sea-touch\ndeveloped plot"]
V = np.array([
 [ 90, 150, 260, 420, np.nan],
 [140, 230, 420, 700, np.nan],
 [140, 220, 380, 620, 2400],
 [150, 250, 420, 650, np.nan],
 [190, 320, 560, 900, 3200],
 [230, 370, 640, 950, np.nan],
 [210, 350, 600, 950, 3600],
 [200, 330, 620,1000, np.nan],
])
OBS = {(5,0):"₹2.5 L/guntha", (5,1):"₹4.0 L/guntha", (6,1):"₹3.0 L/guntha",
       (7,3):"₹7–9.5 k/sq yd", (4,4):"listed band", (6,4):"listed band"}

fig = plt.figure(figsize=(10.4, 7.4))
ax = fig.add_axes([0.175, 0.300, 0.560, 0.520])
cax = fig.add_axes([0.755, 0.300, 0.016, 0.520])
m = np.ma.masked_invalid(V)
im = ax.imshow(m, cmap=CMAP, aspect="auto", norm=LogNorm(vmin=80, vmax=4000))
ax.set_facecolor("#F1EFEA")
for i in range(len(TAL)):
    for j in range(len(TIER)):
        if np.isnan(V[i, j]):
            ax.text(j, i, "n/a\nlandlocked", ha="center", va="center",
                    fontsize=6.2, color="#9AA5A2", linespacing=1.4)
            continue
        v = V[i, j]
        tc = PAPER if v > 700 else INK
        ax.text(j, i - 0.13, f"{v:,.0f}", ha="center", va="center",
                fontsize=8.6, color=tc, fontweight="bold")
        if (i, j) in OBS:
            ax.add_patch(Rectangle((j-0.5, i-0.5), 1, 1, fill=False,
                                   ec=TERRA, lw=1.9, zorder=5))
            ax.text(j, i + 0.26, OBS[(i, j)], ha="center", va="center",
                    fontsize=5.9, color=TERRA if v <= 700 else "#FFD9BE",
                    fontweight="bold")
ax.set_ylim(9.3, -0.6)
ax.set_xticks(range(len(TIER))); ax.set_xticklabels(TIER, fontsize=7.4, linespacing=1.45)
ax.set_yticks(range(len(TAL))); ax.set_yticklabels(TAL, fontsize=8.0)
ax.xaxis.set_ticks_position("top"); ax.xaxis.set_label_position("top")
ax.tick_params(length=0, pad=6)
for s in ax.spines.values(): s.set_visible(False)
cb = fig.colorbar(im, cax=cax); cb.outline.set_visible(False)
cb.set_ticks([100, 300, 1000, 3000])
cb.set_ticklabels(["₹100", "₹300", "₹1,000", "₹3,000"])
cb.ax.tick_params(length=0, labelsize=7.2)
cb.set_label("₹ per sq ft of land (log scale)", fontsize=7.4, labelpad=8)

ax.annotate("", xy=(3.42, 8.15), xytext=(-0.42, 8.15),
            arrowprops=dict(arrowstyle="-|>", color=TERRA, lw=1.6), zorder=9)
ax.text(1.5, 8.45, "≈ 5× uplift from raw land to serviced gated plot — this spread, not "
        "coastal scarcity,\nis where a plotted-township developer's margin is actually made",
        fontsize=7.0, color=TERRA, ha="center", va="top", fontweight="bold",
        linespacing=1.5, clip_on=False)

fig.text(0.175, 0.208,
 "Cells outlined in orange are anchored to an actual observed listing or published band (label beneath the figure). "
 "Every other cell is an\nindicative interpolation built from those anchors and from the reported ₹1,000–2,000 / sq ft "
 "inland and ₹3,000–6,000 / sq ft sea-view\nranges. Treat the pattern as directional and the individual numbers as "
 "hypotheses to be tested against the e-ASR ready-reckoner rate\nand three live comparables before any offer is made. "
 "1 guntha = 1,089 sq ft; 1 acre = 40 guntha.",
 fontsize=7.2, color=INK_SOFT, va="top", linespacing=1.72)
fig.text(0.175, 0.082,
 "Observed anchors →  Kudal, residential plot 2 km from the railway station: ₹4.0 lakh/guntha (₹367/sq ft)  ·  Kudal, 22-guntha parcel "
 "at ₹55 lakh: ₹2.5 lakh/guntha (₹230/sq ft)\n"
 "Achara, Malvan, sea-face land: ₹3.0 lakh/guntha (₹275/sq ft)  ·  Sawantwadi Mopa-side gated layouts: ₹7,000–9,500/sq yd (₹778–1,056/sq ft)  ·  "
 "sea-view developed plots: ₹3,000–6,000/sq ft",
 fontsize=6.6, color=TERRA, va="top", linespacing=1.85)

titleblock(fig, "Figure 5 · The Sindhudurg land-value ladder — the same acre, priced five different ways",
  "A plot buyer and a land buyer are not in the same market. The gap between the columns is the single most important\n"
  "commercial fact in this district, and it is the gap a 150-acre plotted township is built to monetise.")
source(fig, "Sources: live listing data from 99acres and RealEstateIndia for Kudal, Malvan and Sawantwadi (2025–26); published ₹/sq-yd bands for Mopa-side gated layouts; reported ₹1,000–2,000 (inland) and "
            "₹3,000–6,000 (sea-view) per sq ft ranges for\nSindhudurg plots. Listing asks are not transaction prices and typically sit above them. Nothing here is a valuation of any specific parcel.")
save(fig, "f05_price_heatmap")
