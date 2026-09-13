import sys; sys.path.insert(0,"/home/user/NetflixProject/godcity_research/src")
from style import *
import numpy as np, matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle

# ========================================================= F11  SWOT
Q = [
 ("STRENGTHS", "internal · helpful", GREEN, "#F0F6F2", 0.012, 0.505, [
  "Master planning attributed to Architect Hafeez Contractor — a genuinely top-tier,\n"
  "verifiable-in-principle appointment and the single strongest fact in the project.",
  "Scale. At ~150 acres the scheme clears the 40 ha Integrated Township Policy\n"
  "threshold, which unlocks 50% stamp-duty concession and up to 50% relief on\n"
  "development charges — a real structural advantage over 5–15 acre competitors.",
  "Location thesis is sound. Sub-30-minute reach to Mopa, an in-district airport, a\n"
  "four-laned NH-66 and a live Ro-Ro ferry are facts, not projections.",
  "Product fit. Plots, villas and studios at three price points is the right ladder for\n"
  "a market split between end-users, holiday-home buyers and pure investors.",
  "Channel infrastructure is being built early, which usually shortens absorption\n"
  "once a registration exists.",
 ]),
 ("WEAKNESSES", "internal · harmful", RED, "#FBF1F0", 0.503, 0.508, [
  "No MahaRERA registration in the public domain. Until one exists the project may\n"
  "not lawfully be advertised, marketed, booked or sold.",
  "The developing entity is two years old with total partner contribution of\n"
  "₹1,00,000 — against a scheme whose trunk infrastructure alone is a multi-\n"
  "hundred-crore undertaking.",
  "No delivery track record as an entity. The credential cited belongs to one partner,\n"
  "at another group's project (Winsten Park / VHR Group), in another state.",
  "No site identification at all — no village, no gat or survey numbers — so no title,\n"
  "CRZ, ESA or valuation work can even begin.",
  "No published price, payment schedule, area statement or possession date.",
  "Promoter base and registered office are in Noida; Konkan land tenure and CRZ\n"
  "practice are highly local specialisms.",
 ]),
 ("OPPORTUNITIES", "external · helpful", TEAL, "#EDF4F3", 0.012, 0.062, [
  "Sindhudurg is genuinely early. Land is 3–10× cheaper than North Goa and the\n"
  "second-home thesis has not yet been arbitraged away.",
  "A dense, unusually credible public-sector tourism pipeline: the IHCL/Taj hotel at\n"
  "Shiroda, India's first submarine-and-reef museum, the Chipi Aerocity concept and\n"
  "a Swadesh Darshan 2.0 destination designation.",
  "Maharashtra Tourism Policy 2024 offers capital subsidy up to ₹20 crore or 20%,\n"
  "SGST reimbursement, electricity-duty exemption and fast-track approvals for\n"
  "hospitality — directly relevant to a resort-led township.",
  "Access is still improving: NH-66 completion, Konkan Railway electrification, a\n"
  "runway extension and the possibility of a direct Mumbai air link.",
  "First-mover advantage in branded, master-planned supply. Today's competition is\n"
  "mostly 5–15 acre layouts with no planning depth.",
 ]),
 ("THREATS", "external · harmful", AMBER, "#FFF8EC", 0.503, 0.062, [
  "Regulatory tightening on the coast: CRZ-III B imposes a 200 m No-Development\n"
  "Zone, and the Bombay High Court has directed ESA notification for 25 Sawantwadi\n"
  "and Dodamarg villages.",
  "Konkan-specific title risk — kul tenancy, Devasthan/Inam, Occupant Class-II\n"
  "tenure and private-forest classification routinely strand parcels for years.",
  "Announcement risk. The Film City, the Aerocity and the ₹70,000 crore greenfield\n"
  "expressway carry no sanctioned DPR. The missed Navi Mumbai air link is the\n"
  "calibration point.",
  "Financing friction: plot loans run at 60–75% LTV, 10–15 year tenures, 8.5–11.5%,\n"
  "and NRIs are largely ineligible — so demand is thin, cash and cyclical.",
  "Execution attrition is the industry norm: MahaRERA holds 23 Sindhudurg\n"
  "registrations in abeyance and ~1,750 statewide.",
  "Climate exposure: ~4,608 mm of annual rainfall, a rising Arabian Sea cyclone\n"
  "frequency and Western Ghats landslide susceptibility.",
 ]),
]
fig = plt.figure(figsize=(11.6, 8.8))
for title, sub, col, bg, x, y, items in Q:
    a = fig.add_axes([x, y, 0.485, 0.392]); a.axis("off")
    a.set_xlim(0,1); a.set_ylim(0,1)
    a.add_patch(Rectangle((0,0),1,1, fc=bg, ec=col, lw=1.1, zorder=1))
    a.add_patch(Rectangle((0,0.905),1,0.095, fc=col, ec="none", zorder=2))
    a.text(0.022, 0.9525, title, fontsize=10.2, fontweight="bold", color=PAPER,
           va="center", zorder=3)
    a.text(0.978, 0.9525, sub.upper(), fontsize=7.0, color=PAPER, va="center",
           ha="right", zorder=3, alpha=0.92)
    yy = 0.858
    for it in items:
        a.plot([0.030],[yy-0.014], marker="o", ms=3.0, mfc=col, mec="none", zorder=3)
        a.text(0.058, yy, it, fontsize=7.2, color=INK, va="top", zorder=3,
               linespacing=1.62)
        yy -= (it.count("\n")+1) * 0.0455 + 0.030
titleblock(fig, "Figure 11 · SWOT — the honest version, with the asymmetry left in",
  "Read the diagonal, not the four boxes. Strengths and opportunities are overwhelmingly about the district; weaknesses are\n"
  "overwhelmingly about the promoter — so the location case and the counterparty case must be underwritten separately.",
  y=0.998)
save(fig, "f11_swot")
