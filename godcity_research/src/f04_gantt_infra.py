import sys; sys.path.insert(0,"/home/user/NetflixProject/godcity_research/src")
from style import *
import numpy as np, matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

# (label, start, end, status, note)   status: done|live|build|contract|announced|slipped|unknown
ROWS = [
 ("Manohar Intl. Airport (Mopa/GOX), Goa opens",        2023.05, 2023.05, "done",   "Jan 2023 · the corridor's real air gateway"),
 ("Sindhudurg (Chipi/SDW) airport commissioned",        2021.80, 2021.80, "done",   "Oct 2021"),
 ("Vande Bharat · CSMT ↔ Madgaon via Konkan Rly",       2023.49, 2023.49, "done",   "27 Jun 2023"),
 ("Sindhudurg Coastal Zone Mgmt Plan approved",         2023.50, 2023.50, "done",   "CRZ 2019 basis · fixes the 200 m NDZ line"),
 ("NH-66 four-laning — Sindhudurg district stretch",    2016.0,  2025.9,  "done",   "packages P-9 / P-10 ≈99% complete"),
 ("NH-66 four-laning — full Panvel→Sindhudurg (466 km)",2016.0,  2027.2,  "build",  "target end-2026 / early-2027 after repeated slippage"),
 ("Mumbai ↔ Vijaydurg Ro-Ro ferry (M2M Princess)",      2026.17, 2027.0,  "live",   "launched 1 Mar 2026 · 16 trips scheduled in month one"),
 ("Ex-INS Guldar scuttled — artificial reef",           2026.38, 2026.38, "done",   "19 May 2026 · ~22 m depth, Nivati Rocks"),
 ("Submarine + underwater museum open to public",       2026.55, 2027.3,  "announced","₹110.58 cr sanctioned · bookings 'after safety clearances'"),
 ("Konkan Rly electrification (K2 Infragen package)",   2026.47, 2029.0,  "contract","₹1.58 bn order awarded Jun 2026"),
 ("Konkan Rly doubling / patch doubling",               2027.0,  2032.0,  "unknown", "contested — Save Konkan Ecology Forum opposition"),
 ("Chipi runway extension 2,500 m → ~3,000 m",          2026.0,  2028.5,  "announced","state announcement Sep 2025 · no award traced"),
 ("Navi Mumbai ↔ Chipi air service",                    2026.62, 2026.62, "slipped", "15 Aug 2026 start date passed with no service"),
 ("IHCL / Taj hotel, Shiroda–Velagar (~138 acres)",     2025.5,  2029.5,  "announced","tripartite pact signed · land issue dates to 1994"),
 ("Aerocity around Chipi airport",                      2026.0,  2032.0,  "unknown", "concept stage · hotels, retail, offices, expo"),
 ("Film City, Nandos village (~200 acres)",             2026.0,  2032.0,  "unknown", "proposed · no sanctioned DPR traced"),
 ("Adali MIDC pharma hub, Sawantwadi taluka",           2025.0,  2029.0,  "announced","internal roads, power and water reported laid"),
 ("Greenfield Konkan Expressway (MSRDC, 389 km)",       2024.95, 2033.0,  "unknown", "revised DPR Dec 2024 · env. clearance queries pending"),
 ("GOD CITY — LLP incorporated",                        2024.10, 2024.10, "done",   "6 Feb 2024 · LLPIN ACF-3634, RoC-Kanpur"),
 ("GOD CITY — public marketing / channel-partner drive",2025.4,  2027.0,  "live",   "website, blog and agent recruitment active"),
 ("GOD CITY — MahaRERA registration & sales launch",    2026.3,  2027.5,  "unknown", "NO registration number in the public domain"),
]
CFG = {
 "done":     (GREEN,  "Delivered"),
 "live":     (TEAL,   "Operating now"),
 "build":    (BLUE,   "Under construction"),
 "contract": (PLUM,   "Contracted / funded"),
 "announced":(GOLD,   "Announced, timeline soft"),
 "slipped":  (RED,    "Announced date missed"),
 "unknown":  ("#9AA5A2","Concept — no firm timeline"),
}
fig = plt.figure(figsize=(11.2, 10.2))
ax = fig.add_axes([0.290, 0.310, 0.410, 0.560])
rail = fig.add_axes([0.012, 0.045, 0.976, 0.180]); rail.axis("off")
N = len(ROWS)
for i, (lab, s0, s1, st, note) in enumerate(ROWS):
    y = N - 1 - i
    col, _ = CFG[st]
    if i >= N - 3:
        ax.add_patch(Rectangle((2015.4, y-0.46), 2033.6-2015.4, 0.92,
                               fc="#FFF6E8", ec="none", zorder=1))
    if s1 - s0 < 0.10:                       # milestone
        ax.plot([s0],[y], marker="D", ms=7.2, mfc=col, mec=PAPER, mew=1.2, zorder=5)
        if st == "slipped":
            ax.plot([s0],[y], marker="x", ms=5.2, mec=PAPER, mew=1.5, zorder=6)
    else:
        hatch = "///" if st == "unknown" else None
        ax.add_patch(FancyBboxPatch((s0, y-0.26), s1-s0, 0.52,
            boxstyle="round,pad=0.0,rounding_size=0.16", fc=col, ec="none",
            alpha=0.30 if st == "unknown" else 0.92, hatch=hatch, zorder=4,
            lw=0))
        if st == "unknown":
            ax.add_patch(FancyBboxPatch((s0, y-0.26), s1-s0, 0.52,
                boxstyle="round,pad=0.0,rounding_size=0.16", fc="none",
                ec=col, lw=0.9, ls=(0,(3,2)), zorder=5))
    ax.annotate(note, xy=(1.018, y), xycoords=("axes fraction", "data"),
                fontsize=6.7, color=INK_SOFT, va="center", ha="left",
                annotation_clip=False, zorder=6)
ax.axvline(2026.19, color=TERRA, lw=1.4, zorder=8)
ax.text(2026.35, N-0.30, "today\nFeb 2026", fontsize=7.0, color=TERRA,
        fontweight="bold", va="top", zorder=9, linespacing=1.4)
ax.set_yticks(range(N))
ax.set_yticklabels([r[0] for r in ROWS][::-1], fontsize=7.5)
for t, r in zip(ax.get_yticklabels(), ROWS[::-1]):
    if r[0].startswith("GOD CITY"):
        t.set_color(TERRA); t.set_fontweight("bold")
ax.set_xlim(2015.4, 2033.6); ax.set_ylim(-0.75, N-0.25)
ax.set_xticks(range(2016, 2034, 2))
ax.set_xticklabels([str(y) for y in range(2016, 2034, 2)])
frame(ax, left=False, grid="x")
ax.tick_params(axis="y", labelcolor=INK)

h = [plt.Line2D([],[],color=c,lw=7,solid_capstyle="round",label=l)
     for k,(c,l) in CFG.items() if k != "unknown"]
h.append(plt.Line2D([],[],color="#9AA5A2",lw=7,alpha=0.4,label="Concept — no firm timeline"))
h.append(plt.Line2D([],[],ls="none",marker="D",ms=7,mfc=INK_SOFT,mec=PAPER,label="One-off milestone"))
ax.legend(handles=h, loc="upper left", bbox_to_anchor=(-0.355, -0.055), ncol=4,
          fontsize=7.3, labelspacing=0.55, columnspacing=1.8, handlelength=1.5,
          frameon=False)
rail.text(0.0, 1.0, "HOW TO READ THIS", fontsize=8.0, fontweight="bold",
          color=TEAL_D, transform=rail.transAxes, va="top")
rail.plot([0,1],[0.905,0.905], color=RULE, lw=0.9, transform=rail.transAxes, clip_on=False)
COLS = [
 (0.000, "Green and teal \u2014 already banked",
  "Delivered or operating. Mopa and Chipi are open,\n"
  "the Vande Bharat runs, the district's NH-66 stretch\n"
  "is effectively done and the Ro-Ro sails. Every one of\n"
  "these is already reflected in the land price quoted\n"
  "today. Buying now does not capture this value \u2014 it\n"
  "pays for it."),
 (0.255, "Blue and purple \u2014 contracted",
  "Funded and awarded: the balance of the NH-66\n"
  "corridor and the Konkan Railway electrification\n"
  "package. Reasonable to underwrite in a holding-\n"
  "period assumption, with a generous slippage\n"
  "allowance. NH-66 alone has moved its completion\n"
  "date repeatedly over a decade."),
 (0.510, "Gold and grey \u2014 announcements",
  "The Film City, the Aerocity, the runway extension\n"
  "and the \u20b970,000 cr greenfield Konkan Expressway\n"
  "carry no traceable sanctioned DPR, award or funded\n"
  "programme. They may all happen. None is a\n"
  "schedule, and none belongs in an entry valuation\n"
  "as though it were."),
 (0.765, "Red and amber \u2014 the calibration",
  "The Navi Mumbai\u2013Chipi link was announced with a\n"
  "firm date; the date passed with no service. That is\n"
  "the base rate at which this district's promises\n"
  "should be discounted. The amber band is God City\n"
  "itself \u2014 and the row a buyer actually needs, the\n"
  "MahaRERA registration, is grey."),
]
for x, head, body in COLS:
    rail.text(x, 0.800, head, fontsize=7.4, fontweight="bold", color=INK,
              transform=rail.transAxes, va="top")
    rail.text(x, 0.660, body, fontsize=6.9, color=INK_SOFT,
              transform=rail.transAxes, va="top", linespacing=1.62)

titleblock(fig, "Figure 4 · Infrastructure catalyst timeline — sorted by how firm the commitment actually is",
  "Every catalyst cited in Sindhudurg marketing, placed on one axis and colour-coded by evidence class rather than by enthusiasm.\n"
  "Bars are indicative durations, not contract programmes; grey hatched bars are concepts with no sanctioned timetable and their\n"
  "end-points should be read as “unknown”, not as forecasts.")
source(fig, "Sources: NHAI/MSRDC (NH-66, Konkan Expressway DPR and EC status); Konkan Railway Corporation and reported electrification award, June 2026; Maharashtra Maritime Board / operator (Ro-Ro, 1 Mar 2026); "
            "MTDC and Maharashtra Tourism\n(submarine + underwater museum, ₹110.58 cr; Ex-INS Guldar scuttled 19 May 2026); IHCL press release and MTDC tripartite agreement (Shiroda–Velagar); MIDC (Adali); Airports Authority of India and Fly91 schedules "
            "(Chipi, Navi Mumbai link);\nMinistry of Corporate Affairs (God City LLP, LLPIN ACF-3634, incorporated 6 Feb 2024). Compiled February 2026.")
save(fig, "f04_gantt_infra")
