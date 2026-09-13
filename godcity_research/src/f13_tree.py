import sys; sys.path.insert(0,"/home/user/NetflixProject/godcity_research/src")
from style import *
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon

fig = plt.figure(figsize=(11.6, 11.6))
ax = fig.add_axes([0.012, 0.042, 0.976, 0.812]); ax.axis("off")
ax.set_xlim(0, 100); ax.set_ylim(0, 100)

STEPS = [  # question, the "no" exit text
 ("Does a MahaRERA registration number exist for THIS project,\n"
  "and does the portal entry match what you were shown?",
  "STOP. Pay nothing — not a token, not an “expression of interest”,\n"
  "not a “pre-launch” cheque. Marketing a project before registration is\n"
  "itself a breach. Ask for the number in writing and re-test later."),
 ("Is the promoter named on that registration the same legal entity\n"
  "that will sign your agreement for sale?",
  "STOP. A brand is not a counterparty. Get the registered entity's name,\n"
  "CIN or LLPIN, its MCA filings and its financials before going further."),
 ("Can you see the village, gat / survey numbers and the sanctioned\n"
  "layout, with YOUR plot marked on it?",
  "STOP. Without a survey number nothing can be searched, checked or\n"
  "valued. This is the irreducible minimum and it is not negotiable."),
 ("Does a 30-year title search come back clean — Itar Hakk column\n"
  "clear of kul, Inam, Devasthan, Class-II tenure and private forest?",
  "STOP or reprice. In the Konkan these are not technicalities; they\n"
  "routinely make land unsellable for years. Never accept an oral assurance."),
 ("Is the CRZ position certified against the approved Sindhudurg CZMP,\n"
  "and the Western Ghats ESA position confirmed, for your plot?",
  "STOP. A 200 m No-Development Zone or an ESA notification can remove\n"
  "the right to build entirely, while leaving the land price fully paid."),
 ("Is the N.A. order granted, and — at this scale — the Integrated\n"
  "Township locational clearance in place?",
  "PAUSE. Agricultural land is not buildable land. Tie any payment to the\n"
  "grant of these orders, not to the promise of them."),
 ("Does the price stand up against the e-ASR ready-reckoner rate and\n"
  "three independently verified recent transactions nearby?",
  "NEGOTIATE. Listing asks are not transaction prices. Remember that the\n"
  "delivered infrastructure is already in today's rate — you are not buying it cheap."),
 ("Can you complete without a plot loan, or have you confirmed a lender\n"
  "will actually fund this location at 60–75% LTV?",
  "RESIZE. Rural N.A. plots are poorly banked, tenures are 10–15 years and\n"
  "NRIs are largely ineligible. Assume a cash-only resale market too."),
 ("Are amenities, trunk infrastructure, the maintenance corpus and the\n"
  "handover to a plot-holders' association written into the agreement?",
  "NEGOTIATE. This is where plotted schemes fail quietly. Undelivered\n"
  "amenity is the single most common post-sale grievance in the segment."),
]
TOP, H = 96.0, 9.4
XC, XN = 34.0, 62.0
for i, (q, no) in enumerate(STEPS):
    y = TOP - i * H
    ax.add_patch(FancyBboxPatch((7.0, y - 6.6), 53.0, 7.4,
        boxstyle="round,pad=0.4,rounding_size=0.9", fc="#EDF4F3", ec=TEAL,
        lw=1.1, zorder=3))
    ax.add_patch(FancyBboxPatch((0.4, y - 4.35), 5.4, 5.4,
        boxstyle="circle,pad=0.0", fc=TEAL_D, ec="none", zorder=4))
    ax.text(3.1, y - 2.9, f"Q{i+1}", fontsize=8.0, color=PAPER, ha="center",
            va="center", fontweight="bold", zorder=5)
    ax.text(9.0, y - 1.1, q, fontsize=7.5, color=INK, va="top", zorder=5,
            linespacing=1.62, fontweight="bold")
    ax.add_patch(FancyArrowPatch((60.3, y - 2.9), (XN - 0.6, y - 2.9),
        arrowstyle="-|>", mutation_scale=10, color=RED, lw=1.2, zorder=3))
    ax.text(61.0, y - 1.6, "NO", fontsize=6.8, color=RED, fontweight="bold",
            ha="left", va="bottom", zorder=5)
    ax.add_patch(FancyBboxPatch((XN, y - 6.4), 37.5, 7.0,
        boxstyle="round,pad=0.4,rounding_size=0.9", fc="#FBEFEE", ec=RED,
        lw=0.9, zorder=3))
    ax.text(XN + 1.6, y - 1.2, no, fontsize=6.8, color="#7E2A24", va="top",
            zorder=5, linespacing=1.60)
    if i < len(STEPS) - 1:
        ax.add_patch(FancyArrowPatch((XC, y - 6.7), (XC, y - H + 0.9),
            arrowstyle="-|>", mutation_scale=10, color=TEAL, lw=1.4, zorder=2))
        ax.text(XC + 1.2, y - 7.6, "YES", fontsize=6.6, color=TEAL,
                fontweight="bold", va="center", zorder=5)

y = TOP - len(STEPS) * H
ax.add_patch(FancyArrowPatch((XC, y + 3.2), (XC, y - 0.6),
    arrowstyle="-|>", mutation_scale=10, color=GREEN, lw=1.6, zorder=2))
ax.text(XC + 1.2, y + 1.6, "YES", fontsize=6.6, color=GREEN, fontweight="bold", zorder=5)
ax.add_patch(FancyBboxPatch((7.0, y - 10.6), 92.5, 10.0,
    boxstyle="round,pad=0.4,rounding_size=0.9", fc="#F0F6F2", ec=GREEN,
    lw=1.6, zorder=3))
ax.text(9.0, y - 1.5, "PROCEED — but still stage the money.", fontsize=9.2,
        color=GREEN, va="top", fontweight="bold", zorder=5)
ax.text(9.0, y - 4.0,
  "Tie each instalment to a verified milestone — registration, N.A. order, layout sanction, demarcation on site, services laid — "
  "rather than to elapsed time.\nRegister the agreement for sale. Keep every payment traceable through the designated account. "
  "And re-run Q1 to Q6 before each release: approvals lapse, and phases are registered separately.",
  fontsize=7.2, color=INK, va="top", zorder=5, linespacing=1.65)

titleblock(fig, "Figure 13 · The decision tree — nine gates, in order, and what to do when the answer is “no”",
  "Every question is answerable from a document. None of them requires trusting anybody. Work down the left column; the moment\n"
  "you cannot answer a question with paper, stop at that row — the right column tells you what stopping should look like.\n"
  "As at February 2026, an enquiry into God City stops at Q1.",
  y=0.992)
source(fig, "Framework constructed for this report from: Real Estate (Regulation and Development) Act 2016 ss.3, 4, 13, 18 as administered by MahaRERA; Maharashtra Tenancy and Agricultural Lands Act 1948 s.63; Maharashtra Land Revenue Code; "
            "CRZ Notification 2019 and the Sindhudurg CZMP;\nMaharashtra Integrated Township Policy; Maharashtra ready-reckoner (e-ASR) practice; and reported Indian plot-loan terms for 2026. It is a diligence checklist, not legal advice — a Maharashtra-qualified advocate and a local "
            "surveyor should run every one of these steps on the specific parcel.")
save(fig, "f13_decision_tree")
