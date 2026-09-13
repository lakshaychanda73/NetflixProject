import sys; sys.path.insert(0,"/home/user/NetflixProject/godcity_research/src")
from style import *
import numpy as np, matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle

# ================================================== F9 capability radar
AXES = ["Corporate vintage\n& capitalisation","Regulatory evidence\n(RERA · ITP · CRZ)",
        "Delivery track record\nof this entity","Disclosure\ntransparency",
        "Master-planning\ncredentials","Konkan / Maharashtra\nexecution depth",
        "Sales & channel\nreadiness","Market narrative\n& positioning"]
GOD  = [1.0, 0.5, 0.5, 1.0, 4.0, 1.0, 3.5, 4.0]
NEED = [4.5, 5.0, 4.0, 4.5, 3.5, 4.5, 3.0, 3.0]
N = len(AXES)
ang = np.linspace(0, 2*np.pi, N, endpoint=False)
cl = lambda v: np.concatenate([v, v[:1]])
ac = np.concatenate([ang, ang[:1]])

fig = plt.figure(figsize=(10.4, 6.6))
ax = fig.add_subplot(121, polar=True)
ax.set_position([0.030, 0.140, 0.395, 0.615])
ax.set_theta_offset(np.pi/2); ax.set_theta_direction(-1)
ax.plot(ac, cl(np.array(NEED)), color=TEAL_D, lw=1.6, ls=(0,(4,3)), zorder=4)
ax.fill(ac, cl(np.array(NEED)), color=TEAL_D, alpha=0.055, zorder=2)
ax.plot(ac, cl(np.array(GOD)), color=TERRA, lw=2.0, zorder=5)
ax.fill(ac, cl(np.array(GOD)), color=TERRA, alpha=0.20, zorder=3)
ax.set_xticks(ang); ax.set_xticklabels(AXES, fontsize=6.9, linespacing=1.4)
ax.tick_params(axis="x", pad=13)
ax.set_yticks([1,2,3,4,5]); ax.set_yticklabels(["1","2","3","4","5"], fontsize=6.4, color="#A9B2AF")
ax.set_ylim(0, 5); ax.grid(color=RULE, lw=0.6)
ax.spines["polar"].set_color(RULE)
ax.legend(handles=[plt.Line2D([],[],color=TERRA,lw=2.2,label="God City LLP, as evidenced today"),
                   plt.Line2D([],[],color=TEAL_D,lw=1.8,ls=(0,(4,3)),label="What a 150-acre township needs")],
          loc="upper center", bbox_to_anchor=(0.5, -0.105), ncol=1, fontsize=7.4)

pan = fig.add_axes([0.545, 0.070, 0.445, 0.700]); pan.axis("off")
pan.set_xlim(0,1); pan.set_ylim(0,1)
pan.text(0, 1.0, "HOW EACH SCORE WAS SET", fontsize=7.8, fontweight="bold",
         color=TEAL_D, va="top")
pan.plot([0,1],[0.962,0.962], color=RULE, lw=0.8, clip_on=False)
NOTES = [
 ("Corporate vintage & capitalisation", "1 / 5",
  "An LLP incorporated 6 Feb 2024 with total partner contribution of ₹1,00,000.\n"
  "That is the legal minimum, not a development balance sheet."),
 ("Regulatory evidence", "0.5 / 5",
  "No MahaRERA number, no ITP locational clearance, no CRZ position, no N.A.\n"
  "order in the public domain."),
 ("Delivery track record of this entity", "0.5 / 5",
  "God City LLP has delivered nothing. The credential offered belongs to one\n"
  "partner, at another group's project, in another state."),
 ("Disclosure transparency", "1 / 5",
  "Ten of the ten most decision-critical documents are unpublished (Figure 7)."),
 ("Master-planning credentials", "4 / 5",
  "Hafeez Contractor is a genuine, top-tier appointment — and the strongest single\n"
  "fact in the project's favour. Marked down only because it is unconfirmed."),
 ("Konkan / Maharashtra execution depth", "1 / 5",
  "Registered office in Noida; both partners' histories are NCR-based. Konkan land\n"
  "tenure and CRZ practice are specialist local disciplines."),
 ("Sales & channel readiness", "3.5 / 5",
  "A channel-partner programme is live. Note the sequence: distribution is being\n"
  "built before there is a registration to sell against."),
 ("Market narrative & positioning", "4 / 5",
  "The “Goa without Goa prices” thesis is coherent, well-timed and supported by\n"
  "real infrastructure. Positioning is the strongest part of this proposition."),
]
y = 0.930
for k, sc, why in NOTES:
    pan.text(0.0, y, k, fontsize=7.5, fontweight="bold", color=INK, va="top")
    pan.text(1.0, y, sc, fontsize=7.5, fontweight="bold", color=TERRA,
             va="top", ha="right")
    pan.text(0.0, y - 0.036, why, fontsize=6.8, color=INK_SOFT, va="top",
             linespacing=1.6)
    y -= 0.036 + (why.count("\n")+1) * 0.030 + 0.030
titleblock(fig, "Figure 9 · Capability profile — measured against what a 150-acre integrated township actually demands",
  "Scores are this report's judgement, applied consistently and shown with their reasoning so a reader can disagree item by item.\n"
  "The shape matters more than any single score: the promoter is strong exactly where marketing is strong, and weak exactly\n"
  "where money is at risk.")
source(fig, "Basis: Ministry of Corporate Affairs LLP data (LLPIN ACF-3634); God City LLP published material; MahaRERA registers; Maharashtra Integrated Township Policy thresholds; "
            "UP RERA registrations for Winsten Park. Scored February 2026.")
save(fig, "f09_capability")

# ===================================================== F10 risk matrix
RISKS = [
 ("R1","No MahaRERA registration before money is taken",4.5,5.0,"reg"),
 ("R2","150-acre aggregation incomplete or merely optioned",4.0,5.0,"land"),
 ("R3","Konkan title defects — kul, Inam, Class-II, forest",3.15,4.98,"land"),
 ("R4","CRZ-III B 200 m NDZ bites part of the site",2.86,4.10,"reg"),
 ("R5","Western Ghats ESA / wildlife-corridor notification",2.20,4.30,"reg"),
 ("R6","ITP obligations reprice the scheme",2.90,3.18,"reg"),
 ("R7","Promoter capital inadequate for trunk infrastructure",4.22,4.86,"fin"),
 ("R8","Amenities never delivered after plots are sold",3.96,4.22,"exec"),
 ("R9","Exit illiquidity — thin, seasonal, cash resale market",4.34,3.94,"mkt"),
 ("R10","Plot loans scarce; NRIs largely ineligible",3.98,2.98,"fin"),
 ("R11","Announced catalysts never actually land",4.58,3.04,"mkt"),
 ("R12","Entry price already embeds delivered infrastructure",3.98,4.06,"mkt"),
 ("R13","Monsoon, cyclone and landslide exposure",3.26,3.26,"env"),
 ("R14","Water and power adequacy at township scale",3.14,3.86,"exec"),
 ("R15","Post-handover maintenance and CAM vacuum",4.02,3.34,"exec"),
 ("R16","Access concentrated in one airline, one ferry",3.30,2.90,"mkt"),
 ("R17","Registration lapses into abeyance",2.24,3.94,"reg"),
 ("R18","Buyer's own s.63 / N.A. constraints",2.84,3.02,"reg"),
]
CATC = {"reg":(RED,"Regulatory / legal"), "land":(TERRA,"Land & title"),
        "fin":(PLUM,"Financial"), "exec":(BLUE,"Execution & delivery"),
        "mkt":(GOLD,"Market & exit"), "env":(GREEN,"Environmental")}
fig = plt.figure(figsize=(10.6, 7.4))
ax = fig.add_axes([0.075, 0.105, 0.545, 0.660])
for x0, x1, c, a in [(0,2.5,GREEN,0.06),(2.5,3.6,GOLD,0.07),(3.6,5.3,RED,0.06)]:
    ax.add_patch(Rectangle((x0,0),x1-x0,5.4, fc=c, ec="none", alpha=a, zorder=1))
xs = np.linspace(0.5, 5.3, 60)
for lvl, lab, col in [(9.0,"", "#E2DCD1"), (13.0,"", "#D7CEC0"), (17.0,"", "#CBBFAE")]:
    ax.plot(xs, lvl/xs, color=col, lw=0.8, ls=(0,(2,3)), zorder=2)
for code, lab, L, I, cat in RISKS:
    c = CATC[cat][0]
    sev = L * I
    ax.scatter([L],[I], s=290 + sev*17, c=c, alpha=0.85, edgecolors=PAPER,
               linewidths=1.2, zorder=5)
    ax.text(L, I, code, fontsize=7.0, color=PAPER, ha="center", va="center",
            fontweight="bold", zorder=6)
ax.set_xlim(1.55, 5.15); ax.set_ylim(2.35, 5.45)
ax.set_xlabel("Likelihood  →", fontsize=8.6); ax.set_ylabel("Impact on the buyer  →", fontsize=8.6)
ax.set_xticks([2,3,4,5]); ax.set_xticklabels(["Unlikely","Possible","Likely","Near-certain"])
ax.set_yticks([3,4,5]); ax.set_yticklabels(["Material","Severe","Capital-threatening"])
frame(ax, grid="both")
ax.text(5.08, 5.38, "the top-right corner is where\nan investment decision is made\nor lost",
        fontsize=6.9, color=RED, ha="right", va="top", fontweight="bold", linespacing=1.55)
ax.legend(handles=[plt.Line2D([],[],ls="none",marker="o",ms=8,mfc=c,mec=PAPER,label=l)
                   for c,l in CATC.values()],
          loc="lower left", bbox_to_anchor=(0.005,0.015), ncol=2,
          columnspacing=1.4, labelspacing=0.55, fontsize=7.2,
          frameon=True, facecolor=PAPER, edgecolor=RULE, framealpha=0.92)

pan = fig.add_axes([0.645, 0.075, 0.350, 0.690]); pan.axis("off")
pan.set_xlim(0,1); pan.set_ylim(0,1)
pan.text(0, 1.0, "THE REGISTER", fontsize=7.8, fontweight="bold", color=TEAL_D, va="top")
pan.plot([0,1],[0.972,0.972], color=RULE, lw=0.8, clip_on=False)
order = sorted(RISKS, key=lambda r: -(r[2]*r[3]))
y = 0.944
for code, lab, L, I, cat in order:
    c = CATC[cat][0]
    pan.add_patch(FancyBboxPatch((0.0, y-0.026), 0.048, 0.026,
        boxstyle="round,pad=0.001,rounding_size=0.008", fc=c, ec="none",
        clip_on=False))
    pan.text(0.024, y-0.013, code, fontsize=6.2, color=PAPER, ha="center",
             va="center", fontweight="bold", clip_on=False)
    pan.text(0.066, y-0.002, lab, fontsize=6.9, color=INK_SOFT, va="top",
             linespacing=1.5)
    pan.text(1.0, y-0.002, f"{L*I:.0f}", fontsize=7.0, color=c, va="top",
             ha="right", fontweight="bold")
    y -= 0.0525
titleblock(fig, "Figure 10 · Risk register — eighteen exposures, positioned by likelihood and by what they cost the buyer",
  "Scored from this report's evidence base. Bubble size is likelihood × impact; the number in the register is that product.\n"
  "Note how the cluster is shaped: the heaviest risks are documentary and financial, not environmental or market-cyclical.")
source(fig, "Scoring is this report's own judgement, derived from the sourced evidence set out in Figures 1–9 and from the regulatory framework in Figure 12. Likelihood is assessed as at February 2026 and is conditional on the project's "
            "present, pre-registration state; several\nof these risks — R1, R2, R4, R5, R17 in particular — fall sharply the moment a MahaRERA registration and a sanctioned layout exist. This is a framework for asking questions, not a substitute for legal and technical diligence on a specific parcel.")
save(fig, "f10_risk")
