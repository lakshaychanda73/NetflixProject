import sys; sys.path.insert(0,"/home/user/NetflixProject/godcity_research/src")
from style import *
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

ROWS = [
 ("Holiday-home end-user\nMumbai / Pune, buying to use", "wait",
  "The district thesis genuinely works for you — access has improved, the coast is\n"
  "beautiful, and entry is a fraction of North Goa. But you cannot buy a plot that has no\n"
  "survey number. Keep Sindhudurg on the list and keep this project on a watchlist.",
  "A MahaRERA number, a sanctioned layout with your plot on it, and a clean title opinion."),
 ("Land investor\nholding for appreciation", "wait",
  "Most of the appreciation story being sold to you has already happened: Mopa, Chipi,\n"
  "NH-66 and the ferry are delivered and are in today's price. What is left to capture is\n"
  "the announcement tier — and that is the tier with no sanctioned DPR behind it.",
  "Registration, plus a price that stands against the ready-reckoner rate and three\n"
  "verified comparables. Underwrite a 7+ year hold, not a 3-year flip."),
 ("NRI buyer", "avoid for now",
  "You carry every risk above plus two of your own: Indian banks largely will not fund\n"
  "NRI plot purchases, and remote buyers are structurally worst-placed to police title,\n"
  "demarcation and construction quality in a district they cannot visit often.",
  "Everything in the rows above, plus resident representation on the ground and a\n"
  "completed, conveyed plot rather than a promise."),
 ("Channel partner / broker", "do not sell yet",
  "Marketing an unregistered project is not a grey area — RERA prohibits advertising,\n"
  "marketing and booking before registration, and the agent is exposed alongside the\n"
  "promoter. Your own MahaRERA agent registration is the thing at stake.",
  "The project's registration number, verified by you on the portal, before a single\n"
  "enquiry is worked."),
 ("Co-investor or JV partner\nin the development itself", "deep diligence first",
  "A different question entirely, and potentially a real opportunity: the land thesis is\n"
  "sound and the master-planner appointment is credible. But you would be underwriting\n"
  "a ₹389 crore programme against a ₹1 lakh LLP, so the whole exercise is counterparty.",
  "Audited accounts of the land-holding entity, the aggregation status gat by gat, the\n"
  "funding structure, and the full Winsten Park delivery record."),
 ("Already in discussions,\nor has paid a token", "stop and document", 
  "Put your questions in writing and keep the replies. Do not pay a further rupee against\n"
  "a project with no registration. If money has already gone, get the receipt, the entity\n"
  "name and the written basis of the payment on record now, while relations are cordial.",
  "Written confirmation of the registration status. MahaRERA's complaint route is open\n"
  "to a buyer even where the project is unregistered."),
]
CFG = {"wait":(AMBER,"#FFF6E8","WAIT"),
       "avoid for now":(RED,"#FBEFEE","AVOID FOR NOW"),
       "do not sell yet":(RED,"#FBEFEE","DO NOT SELL YET"),
       "deep diligence first":(BLUE,"#EEF3F8","DILIGENCE FIRST"),
       "stop and document":(TERRA,"#FCF1E9","STOP & DOCUMENT")}

fig = plt.figure(figsize=(11.8, 9.2))
ax = fig.add_axes([0.012, 0.048, 0.976, 0.792]); ax.axis("off")
ax.set_xlim(0, 100); ax.set_ylim(0, 100)
TOP = 95.5; h = (TOP - 1.0) / len(ROWS)
ax.text(1.0, 97.8, "WHO YOU ARE", fontsize=7.2, fontweight="bold", color=TEAL_D, va="bottom")
ax.text(22.5, 97.8, "VERDICT", fontsize=7.2, fontweight="bold", color=TEAL_D, va="bottom", ha="center")
ax.text(33.0, 97.8, "WHY", fontsize=7.2, fontweight="bold", color=TEAL_D, va="bottom")
ax.text(75.0, 97.8, "WHAT WOULD CHANGE THE ANSWER", fontsize=7.2, fontweight="bold", color=TEAL_D, va="bottom")
ax.plot([0, 100], [96.6, 96.6], color=INK, lw=1.1)

for i, (who, st, why, chg) in enumerate(ROWS):
    y1 = TOP - i*h; y0 = y1 - h
    col, bg, lab = CFG[st]
    if i % 2 == 0:
        ax.add_patch(Rectangle((0, y0+0.4), 100, h-0.4, fc=PAPER_W, ec="none", zorder=1))
    ax.add_patch(Rectangle((0, y0+0.4), 0.9, h-0.4, fc=col, ec="none", zorder=2))
    ax.text(2.2, y1 - 2.4, who, fontsize=8.0, fontweight="bold", color=INK,
            va="top", zorder=3, linespacing=1.5)
    ax.add_patch(FancyBboxPatch((16.5, y1 - 4.6), 12.0, 2.8,
        boxstyle="round,pad=0.30,rounding_size=0.6", fc=bg, ec=col, lw=1.0, zorder=3))
    ax.text(22.5, y1 - 3.2, lab, fontsize=7.4, color=col, ha="center",
            va="center", fontweight="bold", zorder=4)
    ax.text(33.0, y1 - 2.2, why, fontsize=6.95, color=INK_SOFT, va="top",
            zorder=3, linespacing=1.62)
    ax.text(75.0, y1 - 2.2, chg, fontsize=7.1, color=col, va="top",
            zorder=3, linespacing=1.62)
    ax.plot([0, 100], [y0+0.4, y0+0.4], color=RULE, lw=0.6, zorder=2)

titleblock(fig, "Figure 19 · The verdict — six different readers, six different right answers",
  "There is no single recommendation here, because the question is not the same for everybody. What is common to all six rows\n"
  "is the trigger: none of these verdicts is permanent, and each one names the specific document that would move it. This is a\n"
  "judgement on the evidence available in February 2026 — not on the people involved, and not on Sindhudurg.",
  y=0.990)
source(fig, "Basis: the evidence set compiled in Figures 1–18 and the regulatory framework summarised in Figure 12. Not investment, legal or tax advice. Every verdict here is conditional on the public record as at February 2026 and should be revisited "
            "the moment a MahaRERA registration, a sanctioned\nlayout or a title opinion becomes available. Readers in or near a transaction should retain a Maharashtra-qualified advocate and an independent registered valuer before acting.")
save(fig, "f19_verdict")
