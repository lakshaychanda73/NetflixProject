import sys; sys.path.insert(0,"/home/user/NetflixProject/godcity_research/src")
from style import *
import numpy as np, matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon, Rectangle

# ============ F12  the approval pathway a 150-acre township must actually walk
STAGES = [
 ("1", "LAND ASSEMBLY", "Collector / Talathi",
  "Agreements to sell and mutation of the 7/12 across every single gat number in the assembly. Under s.63 of the\n"
  "Maharashtra Tenancy and Agricultural Lands Act 1948 a non-agriculturist needs the Collector's prior written permission\n"
  "to buy farmland — unless it sits in municipal limits, or under a Special Planning Authority with an N.A. use allocated.", "unknown"),
 ("2", "TITLE DILIGENCE", "Advocate / search clerk",
  "A thirty-year search. The Konkan's specific traps sit in the Itar Hakk (other rights) column: kul tenancy and s.32G entries,\n"
  "Devasthan and Inam grants that are frequently inalienable outright, Occupant Class-II tenure requiring prior sanction and\n"
  "a premium, and land swept into the Maharashtra Private Forests (Acquisition) Act — which has stranded Konkan parcels for decades.", "unknown"),
 ("3", "SITE CONSTRAINTS", "MCZMA · MoEFCC · Forest Dept.",
  "CRZ position read survey number by survey number off the Sindhudurg CZMP approved in 2023 — this coast is largely\n"
  "CRZ-III B, carrying a 200 m No-Development Zone from the High Tide Line. Then Western Ghats ESA status, and for the\n"
  "Sawantwadi–Dodamarg belt the 25-village wildlife-corridor notification the Bombay High Court has directed.", "unknown"),
 ("4", "TOWNSHIP PLANNING", "Collector · Town Planning",
  "Integrated Township Project locational clearance. Minimum 40 ha (~100 acres) as one contiguous piece, every parcel\n"
  "owned by the proponent, at least 15% of residential FSI reserved for social housing, plus parks, playgrounds and\n"
  "community facilities. In exchange: 50% stamp-duty concession and up to 50% off development charges. Collector decides in 45 days.", "unknown"),
 ("5", "LAND CONVERSION", "Collector (Revenue)",
  "Non-agricultural permission under the Maharashtra Land Revenue Code — layout, 7/12, property card, NOCs, site\n"
  "inspection and conversion charges. Buying farmland lawfully does not make it buildable. This is a separate act, and a\n"
  "plot sold before it is granted is a promise, not an asset.", "unknown"),
 ("6", "SERVICES & NOCs", "MJP · MSEDCL · MPCB · Fire",
  "Bulk water allocation, power sanction, sewage treatment and pollution consent, fire clearance, and environmental\n"
  "clearance where built-up area crosses the EIA threshold. At 150 acres in a district that takes ~4,600 mm of rain in four\n"
  "months and runs short in April–May, water and drainage are binding physical constraints — not paperwork.", "unknown"),
 ("7", "MahaRERA REGISTRATION", "MahaRERA",
  "Compulsory the moment the land exceeds 500 sq m or eight plots, counting all phases — and every phase needs its own\n"
  "registration. Until it is granted the project cannot lawfully be advertised, marketed, booked or sold. This is the gate that\n"
  "converts a brochure into an enforceable contract, and everything below it is unavailable to a buyer until it is crossed.", "gate"),
 ("8", "SALES & ESCROW", "Promoter · scheduled bank",
  "70% of every receipt into the designated account, withdrawals certified by architect, engineer and chartered accountant.\n"
  "A registered agreement for sale, a committed completion date, and interest payable under s.18 if that date is missed.", "future"),
 ("9", "DEVELOPMENT", "Promoter",
  "Trunk roads, storm-water, water supply, sewage treatment, power network, plot demarcation and amenities — delivered\n"
  "against the registered timeline, with quarterly progress updates filed on the portal.", "future"),
 ("10","HANDOVER", "Promoter → association",
  "Completion certificate, conveyance, formation of the plot-holders' association, and a funded, governed maintenance\n"
  "regime. This is the stage at which plotted schemes most often fail quietly, years after the last plot is sold.", "future"),
]
CFG = {"unknown":("#9AA5A2","#F2F1EE","Status unknown — nothing published"),
       "gate":(RED,"#FBEFEE","THE GATE — not crossed as at Feb 2026"),
       "future":(RULE,"#F7F6F3","Downstream of the gate")}

fig = plt.figure(figsize=(12.2, 9.9))
ax = fig.add_axes([0.012, 0.048, 0.976, 0.800]); ax.axis("off")
ax.set_xlim(0, 100); ax.set_ylim(0, 100)
TOP, BOT = 97.0, 2.0
n = len(STAGES); h = (TOP - BOT) / n

for i, (num, name, who, body, st) in enumerate(STAGES):
    y1 = TOP - i*h; y0 = y1 - h + 1.0
    c, bg, _ = CFG[st]
    ax.add_patch(FancyBboxPatch((6.5, y0), 91.0, y1-y0,
        boxstyle="round,pad=0.35,rounding_size=0.8", fc=bg, ec=c,
        lw=1.8 if st=="gate" else 0.9, zorder=3))
    ax.add_patch(FancyBboxPatch((0.4, y0+ (y1-y0)/2 - 2.6), 5.2, 5.2,
        boxstyle="circle,pad=0.0", fc=c, ec="none", zorder=4))
    ax.text(3.0, y0 + (y1-y0)/2, num, fontsize=9.0, color=PAPER, ha="center",
            va="center", fontweight="bold", zorder=5)
    ax.text(8.8, y1 - 2.2, name, fontsize=9.0, fontweight="bold",
            color=c if st=="gate" else TEAL_D, va="top", zorder=5)
    ax.text(8.8, y1 - 5.4, who.upper(), fontsize=6.4, color=INK_SOFT,
            va="top", zorder=5, style="italic")
    ax.text(33.0, y1 - 2.4, body, fontsize=6.8, color=INK, va="top",
            zorder=5, linespacing=1.60)
    if i < n-1:
        ax.add_patch(FancyArrowPatch((50, y0-0.1), (50, y0-0.95),
            arrowstyle="-|>", mutation_scale=10, color="#BFC7C4", lw=1.2, zorder=2))

ax.add_patch(FancyBboxPatch((6.5, TOP - 7*h + 1.0 - 0.35), 91.0, h - 1.0 + 0.7,
    boxstyle="round,pad=0.35,rounding_size=0.8", fc="none", ec=RED, lw=2.2,
    zorder=6))
ax.annotate("", xy=(6.0, TOP - 6.5*h + 0.5), xytext=(-1.0, TOP - 6.5*h + 0.5),
            arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.0), zorder=7)

leg = [(c, lab) for c, bg, lab in CFG.values()]
for i, (c, lab) in enumerate(leg):
    ax.add_patch(Rectangle((6.5 + i*31, 99.0), 2.4, 1.6, fc=c, ec="none", zorder=5))
    ax.text(9.7 + i*31, 99.8, lab, fontsize=7.0, color=INK, va="center", zorder=5)

titleblock(fig, "Figure 12 · The approval pathway — ten gates a 150-acre Konkan township has to pass, in order",
  "This is the work programme behind the phrase “coming soon”. Each stage has a named authority, a statutory basis and a real\n"
  "failure mode; several cannot start until the one above is finished. As at February 2026 God City has published no evidence of\n"
  "clearing any of them — and stage 7 is the one that converts a marketing claim into an enforceable contract.",
  y=0.990)
source(fig, "Statutory basis: Maharashtra Tenancy and Agricultural Lands Act 1948 (s.63, as amended 2016); Maharashtra Land Revenue Code (N.A. conversion); Maharashtra Integrated Township Policy (40 ha minimum, contiguity, 15% social housing, "
            "50% stamp-duty concession, 45-day\nCollector decision); CRZ Notification 2019 and the Sindhudurg Coastal Zone Management Plan approved 2023 (CRZ-III B, 200 m NDZ); Bombay High Court directions on the Sawantwadi–Dodamarg corridor; Real Estate (Regulation and Development) "
            "Act 2016 s.3, s.4(2)(l)(D) and s.18 as\nadministered by MahaRERA. Sequence and stage grouping are this report's construction; actual processing is partly parallel and varies with the Collectorate.")
save(fig, "f12_pathway")
