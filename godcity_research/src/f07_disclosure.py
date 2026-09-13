import sys; sys.path.insert(0,"/home/user/NetflixProject/godcity_research/src")
from style import *
import numpy as np, matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle

# status: pub | part | none | na | ind
ROWS = [
 ("MahaRERA project registration number",      "none",
  "Without it the project cannot lawfully be advertised, marketed, booked or sold at all "
  "(MahaRERA s.3: any project over 500 sq m or 8 plots)."),
 ("Entity that will sign the agreement for sale", "none",
  "God City LLP is the brand on the website. The promoter on a MahaRERA registration is a specific "
  "legal person — and it may not be this LLP."),
 ("Village, gat / survey numbers, site boundary", "none",
  "Nothing can be title-searched, CRZ-checked, ESA-checked or valued without them. This is the "
  "irreducible minimum for any diligence."),
 ("Sanctioned layout plan and N.A. order",     "none",
  "Determines whether plots legally exist, how many, of what size, and what may be built on them."),
 ("Title chain, 7/12 extracts, search report", "none",
  "The Konkan's specific traps — kul tenancy, Devasthan/Inam, Class-II tenure, private-forest "
  "classification — all live in these documents."),
 ("CRZ position and CZMP map reference",       "none",
  "The Sindhudurg coast is largely CRZ-III B with a 200 m No-Development Zone. Applicability is "
  "decided survey number by survey number."),
 ("Western Ghats ESA / wildlife-corridor status","none",
  "The Bombay High Court has directed ESA notification of 25 Sawantwadi–Dodamarg villages. "
  "Whether the site is one of them is material."),
 ("Integrated Township Project locational clearance", "none",
  "At ~150 acres the project is above the 40 ha ITP threshold. ITP brings real benefits and real "
  "obligations, including 15% social housing."),
 ("Price list, payment schedule, area statement","none",
  "No rate card exists in the public domain, so no buyer can compare the offer to the market or to "
  "the ready-reckoner rate."),
 ("Committed possession / completion date", "none",
  "The date from which delay interest under RERA s.18 would run. Absent registration there is no "
  "such date and no such remedy."),
 ("70% escrow / designated account",           "na",
  "A statutory consequence of registration. Until the project is registered, money paid is not "
  "protected by the escrow mechanism at all."),
 ("Master planner engagement",                 "part",
  "Architect Hafeez Contractor is named as master planner. The claim is specific and checkable in "
  "principle, but no scope, drawing or confirmation is published."),
 ("Project scale (~150 acres) and product mix", "part",
  "Stated as luxury plots, villas and studios across ~150 acres. Asserted by the promoter; no land "
  "schedule or aggregation status supports it."),
 ("Promoter background and biographies",       "pub",
  "Published on the company website. Self-reported, and — as Figure 8 shows — the credential cited "
  "belongs to a different group's project."),
 ("Corporate registration (LLPIN, partners)",  "ind",
  "The one item independently verifiable today: LLPIN ACF-3634, incorporated 6 Feb 2024, RoC-Kanpur, "
  "total contribution ₹1,00,000, two designated partners."),
 ("Channel-partner / broker recruitment",      "pub",
  "Active. Note the ordering: a sales channel is being built before a registration number exists to "
  "sell against."),
]
CFG = {"none":(RED,     "Not found in the public domain"),
       "part":(AMBER,   "Asserted by promoter, unverified"),
       "pub" :(TEAL,    "Published (self-reported)"),
       "ind" :(GREEN,   "Independently verifiable"),
       "na"  :("#9AA5A2","Not applicable until registered")}

fig = plt.figure(figsize=(10.6, 10.0))
ax = fig.add_axes([0.012, 0.062, 0.976, 0.815]); ax.axis("off")
ax.set_xlim(0, 1); ax.set_ylim(0, 1)
n = len(ROWS); top = 0.958; h = top / n
for i, (item, st, why) in enumerate(ROWS):
    y = top - i * h
    col, _ = CFG[st]
    if i % 2 == 0:
        ax.add_patch(Rectangle((0, y-h+0.004), 1, h-0.004, fc=PAPER_W, ec="none", zorder=1))
    ax.add_patch(Circle((0.019, y - h/2), 0.0088, fc=col, ec="none", zorder=3))
    ax.text(0.040, y - h/2 + 0.0125, item, fontsize=8.0, color=INK,
            fontweight="bold", va="center", zorder=3, linespacing=1.45)
    ax.text(0.040, y - h/2 - 0.0205, why, fontsize=7.0, color=INK_SOFT,
            va="center", zorder=3, linespacing=1.5)
    ax.add_patch(FancyBboxPatch((0.815, y - h/2 - 0.0125), 0.170, 0.025,
        boxstyle="round,pad=0.004,rounding_size=0.012", fc=col, ec="none",
        alpha=0.16, zorder=3))
    ax.text(0.900, y - h/2, CFG[st][1], fontsize=6.8, color=col, ha="center",
            va="center", fontweight="bold", zorder=4)
    ax.plot([0, 1], [y-h, y-h], color=RULE, lw=0.6, zorder=2)
ax.plot([0, 1], [top, top], color=INK, lw=1.1, zorder=2)
ax.text(0.040, top + 0.013, "DISCLOSURE ITEM  ·  and why a buyer needs it", fontsize=7.2,
        color=TEAL_D, fontweight="bold", va="bottom")
ax.text(0.900, top + 0.013, "STATUS, FEB 2026", fontsize=7.2, color=TEAL_D,
        fontweight="bold", va="bottom", ha="center")

titleblock(fig, "Figure 7 · The evidence ledger — what a buyer needs, against what God City actually publishes",
  "Sixteen disclosure items, ordered from most to least decision-critical. Ten of the first ten are absent. The four items that are\n"
  "present are marketing assets — a scale, a famous architect, two biographies and a broker programme — none of which a\n"
  "conveyancing lawyer, a valuer or a lender can act on.",
  y=0.987)
source(fig, "Method: every public God City LLP web page (home, about, blog, channel-partner) was searched, together with MahaRERA's project search, lapsed-project and suspended-project registers, and general web search, in February 2026. "
            "“Not found in the public\ndomain” means exactly that — it is not a finding that the document does not exist. A promoter may hold all of these and simply not publish them, and a serious enquiry should request every one of them in writing before any payment is made.")
save(fig, "f07_disclosure")
