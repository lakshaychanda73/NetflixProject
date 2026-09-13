import sys; sys.path.insert(0,"/home/user/NetflixProject/godcity_research/src")
from style import *
import numpy as np, matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

PLOT_SQFT, RATE = 5400, 1000
land = PLOT_SQFT * RATE / 1e5
ITEMS = [
 ("Headline plot price — 5,400 sq ft @ ₹1,000/sq ft", land,      TEAL_D),
 ("Stamp duty @ 6%",                                  land*0.06, TERRA),
 ("Registration @ 1%, capped at ₹30,000",             0.30,      TERRA),
 ("Legal, title search, survey, mutation",            1.20,      BLUE),
 ("Development / infrastructure charge @ 8%",         land*0.08, GOLD),
 ("Maintenance corpus + two years' CAM",              1.80,      PLUM),
]
total = sum(v for _, v, _ in ITEMS)

fig = plt.figure(figsize=(11.0, 8.4))
ax = fig.add_axes([0.315, 0.500, 0.330, 0.290])
ys = np.arange(len(ITEMS)+1)[::-1]
for y, (lab, v, col) in zip(ys[:-1], ITEMS):
    ax.barh([y], [v], height=0.58, color=col, edgecolor="none", zorder=3)
    ax.text(v + total*0.012, y, f"₹{v:,.2f} L", fontsize=7.4, color=col,
            va="center", fontweight="bold")
ax.barh([ys[-1]], [total], height=0.58, color=INK, edgecolor="none", zorder=3)
ax.text(total + total*0.012, ys[-1], f"₹{total:,.2f} L", fontsize=8.2, color=INK,
        va="center", fontweight="bold")
ax.set_yticks(ys)
ax.set_yticklabels([i[0] for i in ITEMS] + ["ALL-IN COST OF OWNERSHIP"], fontsize=7.4)
ax.get_yticklabels()[-1].set_fontweight("bold")
ax.set_xlim(0, total*1.20); ax.set_ylim(-0.95, len(ITEMS)+0.6)
ax.set_xlabel("₹ lakh")
frame(ax, left=False, grid="x")
ax.tick_params(axis="y", labelcolor=INK)
ax.annotate(f"+{(total/land-1)*100:.0f}% over the brochure number",
            xy=(total*0.78, -0.72), fontsize=8.0, color=RED, ha="center",
            fontweight="bold")

ax2 = fig.add_axes([0.315, 0.095, 0.330, 0.285])
yrs = np.arange(0, 11)
for cagr, col, lab in [(0.14, GREEN, "Bull  14% p.a."), (0.08, TEAL, "Base  8% p.a."),
                       (0.03, TERRA, "Bear  3% p.a.")]:
    v = land * (1+cagr)**yrs
    ax2.plot(yrs, v, color=col, lw=2.0, zorder=5)
    ax2.text(9.85, v[-1], lab, fontsize=7.0, color=col, va="bottom", ha="right",
             fontweight="bold")
be = total / 0.98
ax2.axhline(be, color=RED, lw=1.4, ls=(0,(4,3)), zorder=6)
ax2.fill_between(yrs, 40, be, color=RED, alpha=0.05, zorder=1)
ax2.text(0.15, be*1.025, f"break-even on resale ≈ ₹{be:,.0f} L", fontsize=7.0,
         color=RED, va="bottom", fontweight="bold")
t8 = int(np.argmax(land*1.08**yrs >= be)); t3 = int(np.argmax(land*1.03**yrs >= be))
for t, c, r in [(t8, TEAL, 1.08), (t3, TERRA, 1.03)]:
    ax2.scatter([t], [land*r**t], s=46, c=c, edgecolors=PAPER, zorder=7, linewidths=1.2)
    ax2.annotate(f"year {t}", xy=(t, land*r**t), xytext=(t+0.25, land*r**t - 16),
                 fontsize=6.8, color=c, fontweight="bold",
                 arrowprops=dict(arrowstyle="-", color=c, lw=0.7))
ax2.set_xlim(0, 10); ax2.set_ylim(40, 215)
ax2.set_xlabel("Years held"); ax2.set_ylabel("Plot value, ₹ lakh")
ax2.set_xticks(range(0, 11, 2)); frame(ax2)
ax2.set_title("When does the buyer actually get square?", fontsize=9.0,
              fontweight="bold", loc="left", pad=8)

pan = fig.add_axes([0.685, 0.088, 0.305, 0.700]); pan.axis("off")
pan.set_xlim(0,1); pan.set_ylim(0,1)
pan.text(0, 1.0, "WHAT THE TWO CHARTS SAY TOGETHER", fontsize=7.8,
         fontweight="bold", color=TEAL_D, va="top")
pan.plot([0,1],[0.972,0.972], color=RULE, lw=0.8, clip_on=False)
BLOCKS = [
 ("The brochure price is not the price.",
  f"On these assumptions a ₹{land:,.0f} lakh plot costs\n₹{total:,.1f} lakh to own — {(total/land-1)*100:.0f}% more — before a\n"
  "single brick is laid. Stamp duty is charged on\nthe higher of agreement value or the ready-\n"
  "reckoner rate, so a “discount” off an inflated\nheadline may not reduce it at all."),
 ("That gap sets the real hurdle.",
  f"Including a 2% exit cost the plot must reach\nabout ₹{be:,.0f} lakh before the buyer is square.\n"
  f"At 8% a year that is roughly {t8} years; at 3% it is\n{t3}. Any shorter holding period is a loss dressed\n"
  "up as an appreciating asset."),
 ("The scenarios are not symmetric.",
  "The bull case needs the announced catalysts to\nland. The bear case needs only for them to slip.\n"
  "And a plotted scheme that stalls before its\namenities are built does not track the bear line\n"
  "at all — it trades below raw land, because a\n"
  "stranded plot inside an unfinished layout is\nharder to sell than a field."),
 ("That tail is not drawn here.",
  "It is the one worth insuring against — and the\nonly reliable insurance is refusing to pay until\n"
  "the gates in Figure 13 are cleared."),
]
y = 0.938
for head, body in BLOCKS:
    pan.text(0, y, head, fontsize=7.6, fontweight="bold", color=INK, va="top")
    pan.text(0, y - 0.035, body, fontsize=7.1, color=INK_SOFT, va="top",
             linespacing=1.70)
    y -= 0.035 + (body.count("\n")+1)*0.0345 + 0.040
titleblock(fig, "Figure 17 · The buyer's arithmetic — all-in entry cost, and the hurdle it creates on exit",
  "Worked on an illustrative 5,400 sq ft (~600 sq yd) plot at ₹1,000 per sq ft — the mid-point of observed Mopa-side gated-layout\n"
  "rates. God City publishes no price, so this is a template to run the promoter's number through, not a quote.")
source(fig, "Assumptions: Maharashtra stamp duty taken at 6% (the applicable rate varies with location and buyer category, and any Integrated Township Policy concession attaches to the developer's land purchase, not automatically to the buyer's); "
            "registration at 1% capped at ₹30,000; professional\nfees, development charges and maintenance corpus at indicative market levels; exit cost at 2% brokerage. Ready-reckoner rates rose ~3.89% on average across Maharashtra for FY 2025-26 and ~3.7% in rural areas. Illustrative arithmetic for stress-testing "
            "an offer — not a forecast, a valuation, or tax advice.")
save(fig, "f17_buyer_math")
