import sys; sys.path.insert(0,"/home/user/NetflixProject/godcity_research/src")
from style import *
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

FW, FH = 11.4, 8.9
AXH, YSPAN = 0.775, 112.0
fig = plt.figure(figsize=(FW, FH))
ax = fig.add_axes([0.012, 0.055, 0.976, AXH]); ax.axis("off")
ax.set_xlim(0, 100); ax.set_ylim(0, YSPAN)
U = YSPAN / (AXH * FH * 72)            # data units per typographic point

def box(x0, x1, ytop, title, body, fc, ec, tc=None, fs=8.0, lfs=6.9,
        ls="-", lw=1.2, tls=1.38, bls=1.52, pad=3.2, gap=1.6):
    """Draw a box whose height is derived from its own content."""
    nt = title.count("\n") + 1
    nb = body.count("\n") + 1 if body else 0
    th = nt * fs * tls * U
    bh = (nb * lfs * bls * U + gap) if body else 0
    h = pad * U * 2 + th + bh + 1.2
    y0 = ytop - h
    ax.add_patch(FancyBboxPatch((x0, y0), x1-x0, h,
        boxstyle="round,pad=0.55,rounding_size=1.3", fc=fc, ec=ec, lw=lw,
        linestyle=ls, zorder=3))
    cx = (x0 + x1) / 2
    ax.text(cx, ytop - pad*U, title, fontsize=fs, fontweight="bold",
            color=tc or ec, ha="center", va="top", zorder=4, linespacing=tls)
    if body:
        ax.text(cx, ytop - pad*U - th - gap, body, fontsize=lfs, color=INK_SOFT,
                ha="center", va="top", zorder=4, linespacing=bls)
    return y0

def arrow(p0, p1, color, style="-", lw=1.3, rad=0.0):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=11,
        color=color, lw=lw, linestyle=style, zorder=2,
        connectionstyle=f"arc3,rad={rad}", shrinkA=2, shrinkB=3))

def tag(x, y, text, color, fs=6.5):
    ax.text(x, y, text, fontsize=fs, color=color, ha="center", va="center",
            fontweight="bold", zorder=6, linespacing=1.45,
            bbox=dict(boxstyle="round,pad=0.30", fc=PAPER, ec="none"))

rk = box(1, 31, 97, "Rakesh Kumar\n(“Rakesh Chaudhary”)",
   "Designated Partner\n\n18+ years claimed in the sector.\n"
   "Credential cited: “directorial\nexperience with the WinstenPark\nproject of VHR Group”.",
   "#EAF2F1", TEAL_D)
sk = box(1, 31, 68, "Suresh Kumar\n(“Suresh Chaudhary”)",
   "Designated Partner\n\n14 years claimed in the sector.\n"
   "Also credited with creating\nDelhiwood Pvt. Ltd. and producing\n"
   "the Punjabi film “Hard Kaur” —\nnot a delivery credential.",
   "#EAF2F1", TEAL_D)
pr = box(1, 66, 33, "WHAT THE TRACK RECORD ACTUALLY IS",
   "The credential cited belongs to one partner personally — it is not a project of this LLP.\n\n"
   "Winsten Park, Knowledge Park V, Greater Noida  ·  3.71 acres  ·  3 towers  ·  ~674 units\n"
   "RERA promoter of record: SKV INFOTECH PRIVATE LIMITED  ·  brand: VHR Group (est. 1986)\n"
   "Phase I  UPRERAPRJ5008 — launched 15 Dec 2015, completion due 14 Dec 2020\n"
   "Phase II  UPRERAPRJ9566 — due 7 Jul 2021   ·   Phase III  UPRERAPRJ11430 — due 16 Jan 2028\n"
   "Possession on parts of the scheme reported into Nov–Dec 2025",
   "#FBEFEE", RED, tc="#7E2A24", fs=8.2, lfs=6.9)
lp = box(36, 64, 101, "GOD CITY LLP",
   "LLPIN  ACF-3634\n\nIncorporated  6 February 2024\nRegistrar of Companies, Kanpur\n\n"
   "Registered office:\nA-118, 4th Floor, Noida,\nGautam Buddha Nagar, UP 201301\n\n"
   "Total contribution  ₹1,00,000\nStatus: Active",
   "#FFFFFF", TEAL_D, fs=11.2, lfs=7.0, lw=1.9)
gc = box(36, 64, 56, "godcity.in",
   "Website, blog and channel-partner\nrecruitment. As of February 2026\nthis is the only public face.",
   "#F4F1EA", INK_SOFT)
mb = box(69, 99, 107, "THE MISSING BOX",
   "Land in Maharashtra is held by someone,\nand a MahaRERA promoter must be a\n"
   "named legal person. Neither is disclosed.\nThe entity a buyer eventually contracts\n"
   "with may not be God City LLP — and it is\nthat balance sheet, not this one, that\nstands behind the promise.",
   "#FBEFEE", RED, tc="#7E2A24", fs=8.4, lfs=6.9, lw=1.4)
tw = box(69, 99, 72, "“GOD CITY” TOWNSHIP\nSindhudurg, Maharashtra",
   "~150 acres  (claimed)\nLuxury plots · villas · studios\n\n"
   "✗   no MahaRERA registration\n✗   no village or survey numbers\n"
   "✗   no sanctioned layout\n✗   no published price list\n✗   no land-holding entity named",
   "#FFF6E8", AMBER, tc="#8A5F0B", fs=8.6, lfs=7.0, lw=1.5, ls=(0,(5,3)))
hc = box(69, 99, 31, "Architect Hafeez Contractor",
   "Named by the promoter as master\nplanner. Padma Bhushan 2016;\n"
   "Hiranandani Gardens, The Imperial,\nThe 42. A real credential — if the\nengagement is confirmed.",
   "#F4EFF5", PLUM, lw=1.2, ls=(0,(5,3)))

arrow((31, 88), (36, 90), TEAL_D);  tag(33.5, 95.0, "designated\npartner", TEAL_D)
arrow((31, 60), (36, 76), TEAL_D);  tag(33.5, 51.0, "designated\npartner", TEAL_D)
arrow((50, lp), (50, 56), INK_SOFT); tag(57.2, (lp+56)/2, "operates", INK_SOFT)
arrow((64, 84), (69, 66), AMBER, style=(0,(5,3)))
tag(66.5, 72.5, "claims to be\ndeveloping", "#8A5F0B")
arrow((84, mb), (84, 72), RED, style=(0,(2,3)))
arrow((84, tw), (84, 31), PLUM, style=(0,(5,3)))
tag(84, (tw+31)/2, "states it has engaged", PLUM, fs=6.2)
arrow((33.5, 33), (29.5, 74), RED, style=(0,(2,3)), rad=0.30)

leg = [("Documented in a public register", TEAL_D, "-"),
       ("Claimed by the promoter, unverified", AMBER, (0,(5,3))),
       ("Personal association of an individual, not an entity link", RED, (0,(2,3)))]
for i, (lab, c, ls) in enumerate(leg):
    ax.plot([1 + i*33, 6 + i*33], [110.5, 110.5], color=c, lw=1.7, ls=ls, zorder=5)
    ax.text(7 + i*33, 110.5, lab, fontsize=7.2, color=INK, va="center", zorder=5)

titleblock(fig, "Figure 8 · Who is actually behind this — the corporate structure, and the gap in the middle of it",
  "Solid lines are facts on a public register. Dashed lines are the promoter's own claims. Dotted lines are associations that belong to an\n"
  "individual rather than to the entity a buyer would be contracting with. That distinction is the entire point of the diagram.",
  y=0.988)
source(fig, "Sources: Ministry of Corporate Affairs LLP master data for GOD CITY LLP (LLPIN ACF-3634); God City LLP website (home, about, blog, channel-partner pages) for the biographies, the ~150-acre scale and the Hafeez Contractor engagement; "
            "UP RERA registrations\nUPRERAPRJ5008 / 9566 / 11430 and listing-portal project data for Winsten Park, Knowledge Park V, Greater Noida; VHR Group corporate website for group history. Retrieved February 2026. Nothing here alleges wrongdoing — it "
            "separates what sits on a register from what is asserted.")
save(fig, "f08_structure")
