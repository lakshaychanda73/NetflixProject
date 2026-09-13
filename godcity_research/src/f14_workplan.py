import sys; sys.path.insert(0,"/home/user/NetflixProject/godcity_research/src")
from style import *
import numpy as np, matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch

# (workstream, task, start_week, end_week, owner, lane)
LANES = [
 ("A", "COUNTERPARTY", TEAL_D),
 ("B", "SITE & TITLE", TERRA),
 ("C", "STATUTORY & ENVIRONMENTAL", RED),
 ("D", "TECHNICAL FEASIBILITY", BLUE),
 ("E", "MARKET & VALUATION", GOLD),
 ("F", "COMMERCIAL & CLOSING", PLUM),
]
T = [
 ("A","Issue a written information request; log every answer and non-answer",0,2,"You / advisor"),
 ("A","MCA pull: LLP master data, partners, charges, annual filings",1,3,"CA"),
 ("A","Identify the actual land-holding entity and its financials",1,5,"CA / advocate"),
 ("A","Confirm the Hafeez Contractor engagement directly with the practice",1,4,"You"),
 ("A","Trace the Winsten Park record: UP RERA status, delivery, complaints",2,5,"Advisor"),
 ("B","Obtain village, gat / survey numbers and the site boundary",0,4,"Promoter → you"),
 ("B","7/12, 8-A, property cards and mutation entries for every gat",3,6,"Search clerk"),
 ("B","30-year title search; Itar Hakk analysis; public notice",4,10,"Advocate"),
 ("B","Kul / s.32G, Inam, Devasthan, Class-II and private-forest screening",5,10,"Advocate"),
 ("B","Physical demarcation and boundary walk with a licensed surveyor",6,9,"Surveyor"),
 ("C","CRZ position against the approved Sindhudurg CZMP",4,9,"Env. consultant"),
 ("C","Western Ghats ESA and wildlife-corridor exposure check",4,8,"Env. consultant"),
 ("C","Confirm N.A. order and Integrated Township locational clearance",5,11,"Advocate"),
 ("C","MahaRERA verification — registration, phase, promoter, timeline",0,2,"You"),
 ("C","MahaRERA lapsed / abeyance / deregistered register screening",1,3,"You"),
 ("D","Water: source, bulk allocation, monsoon and summer yield",7,12,"Civil engineer"),
 ("D","Power sanction, road access, drainage and flood/landslide screen",7,12,"Civil engineer"),
 ("D","Cost the trunk infrastructure the promoter has committed to",9,13,"QS / engineer"),
 ("E","e-ASR ready-reckoner rate for the exact village and survey group",2,4,"You"),
 ("E","Three verified registered comparables — sub-registrar data",3,8,"Valuer"),
 ("E","Absorption, resale depth and rental evidence in the micro-market",4,9,"Valuer"),
 ("E","Independent valuation and downside scenario",9,13,"Valuer"),
 ("F","Negotiate price, milestone-linked payment plan and indemnities",11,15,"You / advocate"),
 ("F","Draft and vet the agreement for sale; amenity and CAM schedules",12,17,"Advocate"),
 ("F","Registration, stamp duty, mutation; escrow payment discipline",16,19,"Advocate"),
 ("F","Post-closing monitoring: quarterly RERA updates, association formation",19,26,"You"),
]
GATES = [(2,"G1  Registration\nverified"),(10,"G2  Title\nopinion"),
         (13,"G3  Feasibility\n& value"),(19,"G4  Closing")]

fig = plt.figure(figsize=(12.2, 9.6))
ax = fig.add_axes([0.320, 0.150, 0.625, 0.665])
rows = []          # (kind, payload)
for code, lname, col in LANES:
    rows.append(("head", (f"{code}   {lname}", col)))
    for (c, task, s0, s1, own) in T:
        if c == code:
            rows.append(("task", (task, s0, s1, own, col)))
N = len(rows)
ticklab, tickcol, tickbold = [], [], []
for j, (kind, p) in enumerate(rows):
    y = N - 1 - j
    if kind == "head":
        name, col = p
        ax.add_patch(Rectangle((-0.4, y-0.46), 27.9, 0.92, fc=col, ec="none",
                               alpha=0.13, zorder=2))
        ticklab.append(name); tickcol.append(col); tickbold.append(True)
    else:
        task, s0, s1, own, col = p
        ax.add_patch(FancyBboxPatch((s0, y-0.28), max(s1-s0, 0.6), 0.56,
            boxstyle="round,pad=0.0,rounding_size=0.18", fc=col, ec="none",
            alpha=0.90, zorder=4))
        ax.text(s1 + 0.45, y, own, fontsize=6.3, color=INK_SOFT, va="center", zorder=5)
        ticklab.append(task); tickcol.append(INK); tickbold.append(False)
for w, lab in GATES:
    ax.axvline(w, color=INK, lw=1.0, ls=(0,(3,2)), zorder=3, alpha=0.55)
    ax.annotate(lab, xy=(w, N - 0.25), xytext=(w, N + 0.55), ha="center",
                va="bottom", fontsize=6.8, color=INK, fontweight="bold",
                linespacing=1.4, annotation_clip=False,
                bbox=dict(boxstyle="round,pad=0.30", fc="#F4F1EA", ec=RULE, lw=0.7))
ax.set_yticks(range(N)); ax.set_yticklabels(ticklab[::-1], fontsize=7.0)
for t, c, b in zip(ax.get_yticklabels(), tickcol[::-1], tickbold[::-1]):
    t.set_color(c)
    if b: t.set_fontweight("bold"); t.set_fontsize(7.4)
ax.set_xlim(-0.4, 27.5); ax.set_ylim(-0.8, N + 0.1)
ax.set_xticks(range(0, 28, 2))
ax.set_xticklabels([f"W{w}" for w in range(0, 28, 2)])
ax.set_xlabel("Weeks from the start of the enquiry")
frame(ax, left=False, grid="x")
ax.tick_params(axis="y", labelcolor=INK)

ax.text(13.2, N - 0.9,
 "SEQUENCING RULE\n\n"
 "Gate G1 costs nothing and takes an afternoon — it is a lookup on the\n"
 "MahaRERA portal. Run it first, and if it fails, run nothing else.\n\n"
 "Everything below G1 spends real money on advocates, surveyors, valuers\n"
 "and engineers. The largest avoidable cost in a plotted-land purchase is\n"
 "diligence commissioned on a project that was never registered at all.",
 fontsize=7.2, color="#7A5409", va="top", linespacing=1.78, zorder=8,
 bbox=dict(boxstyle="round,pad=0.60", fc="#FFF6E8", ec=AMBER, lw=0.9))
titleblock(fig, "Figure 14 · The work plan — twenty-six tasks, six workstreams, four gates, about six months",
  "A structured programme for anyone actually evaluating this opportunity, whether as a plot buyer, a channel partner or an\n"
  "investor. Bars are indicative durations; the right-hand label is who should own the task. The four dashed gates are\n"
  "stop/go points — work to the right of a gate should not be commissioned until the gate is cleared.")
source(fig, "Programme constructed for this report. Durations assume a single site in one taluka, a cooperating counterparty and normal Collectorate turnaround; contested title, multi-taluka assembly or an ESA question will extend workstreams B and C "
            "materially. Costs are not modelled here —\nas a rough order, workstreams A–C are the cheap ones and workstream D is where professional fees start to matter.")
save(fig, "f14_workplan")
