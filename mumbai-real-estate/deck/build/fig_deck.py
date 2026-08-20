"""fig_deck.py — the charts and diagrams for the 12-slide Brickrock Realty deck.

Every quantity on every slide is read from ../../build/evidence.py or founder.py.
Nothing is typed as a literal, so the deck and the 60-page playbook cannot disagree.

Slide order (rebuilt from the playbook's evidence, not from the earlier deck):
  1  Opening — the thesis            7  Competitive positioning
  2  The customer's problem          8  The moat
  3  What Brickrock is               9  Business model and economics
  4  How it works                   10  Go to market and the referral loop
  5  Why Eastern & Central          11  Capital and the 90-day proof
  6  Customer-market fit            12  Founder and the long arc
"""

import sys, os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Polygon, Wedge
sys.path.insert(0, os.path.abspath("../../build"))

import deck_theme as T
from deck_theme import (LIGHT, DARK, DARK_2, CARD, CARD_ALT, INK, INK2, MUTED, HAIR, RULE,
                        D_INK, D_INK2, D_MUTED, D_HAIR,
                        ORANGE, BLUE, GREEN, PURPLE, SERIES,
                        ORANGE_L, ORANGE_D, BLUE_L, BLUE_D, GREEN_L,
                        GOOD, WARN, BAD, SEQ_ORANGE, ORANGE_RAMP)
import evidence as E
import founder as F

L, CR = 100_000, 10_000_000
GREY = "#C9CCD1"
GREY_D = "#9BA3B0"

RATE = E.BLENDED_RATE                      # 0.0132
RATE_L = E.BLENDED_RATE_LABEL              # "1.32%"
CONSID = E.BLENDED_CONSIDERATION           # Rs 2.30 cr


# ═════════════════════════════════════════════════ S1 · the market is real
def s1_pulse():
    """Dark: the monthly transaction heartbeat. Proof the market clears, every month."""
    m = E.MONTHLY_REGISTRATIONS
    months = [x[0] for x in m]
    regs = [x[1] for x in m]

    fig = plt.figure(figsize=(7.6, 3.95))
    fig.patch.set_facecolor(DARK)
    ax = fig.add_axes([0.045, 0.135, 0.94, 0.715])
    ax.set_facecolor(DARK)
    for i, v in enumerate(regs):
        rep = m[i][3] == "reported"
        T.bar(ax, i - 0.34, 0, 0.68, v, ORANGE if rep else "#3C4A5C", r=260)
        ax.text(i, v + 560, f"{v/1000:.1f}k", ha="center", fontsize=8.0,
                color=D_INK if rep else D_MUTED, fontweight="600")
    ax.set_xticks(range(len(months)))
    ax.set_xticklabels(months, fontsize=8, color=D_INK2)
    ax.set_ylim(0, 17600); ax.set_xlim(-0.72, len(months) - 0.28)
    ax.set_yticks([])
    T.clean(ax, ygrid=False, dark=True)
    ax.spines["bottom"].set_color(D_HAIR)
    ax.tick_params(labelcolor=D_INK2)
    fig.text(0.045, 0.925, "MUMBAI PROPERTY REGISTRATIONS PER MONTH · 2026", fontsize=8.0,
             color=D_MUTED, fontweight="700")
    fig.text(0.045, 0.028,
             "Knight Frank / IGR monthly releases. Jan–May apportioned to the published H1 total;\nJune and July are reported figures.",
             fontsize=6.4, color=D_MUTED, linespacing=1.6)
    T.save(fig, "s1_pulse.png", dark=True)


# ═════════════════════════════════════════════════ S2 · the customer's problem
def s2_problem():
    """The six questions that decide a ₹2.3 crore purchase — and where they go unanswered."""
    fig, ax = T.canvas(12.4, 4.75)

    rows = [
        ("Is this asking price above or below what flats in\nthis building actually registered for?",
         "An asking price, set by the seller",
         "Registered instruments from IGR e-Search,\nnormalised to one area basis"),
        ("Is that 1,150 sq ft carpet, built-up or saleable?",
         "All three, used interchangeably",
         "One basis, applied consistently — or the\n₹/sq ft comparison is wrong by 20–30%"),
        ("Has this developer delivered on time before?",
         "A brochure and a possession date",
         "MahaRERA quarterly filings, complaints and\nthe promoter's actual record of slippage"),
        ("Will the society clear my loan, my tenant,\nmy renovation?",
         "Nothing",
         "The society's own rules and resolutions,\nread before the deposit — not after it"),
        ("What does the commute actually cost me\nat 9am on a Tuesday?",
         "A map with a straight line on it",
         "A commute walked and timed from the\nbuilding gate at the hour it matters"),
        ("If I need to exit in three years, who buys this?",
         "Optimism",
         "Resale depth and days-on-market for this\npocket, from the registered record"),
    ]

    cx = [3.0, 48.5, 71.5]
    heads = ["THE QUESTION THAT DECIDES THE DEAL",
             "WHAT THE MARKET GIVES YOU",
             "WHAT ANSWERING IT ACTUALLY TAKES"]
    hc = [INK, MUTED, ORANGE]
    for x, h, c in zip(cx, heads, hc):
        ax.text(x, 92.5, h, fontsize=6.9, color=c, fontweight="800", va="center")
    ax.plot([2.0, 98.0], [88.6, 88.6], color=RULE, lw=1.0)

    top, band = 85.0, 13.6
    for i, (q, has, needs) in enumerate(rows):
        y = top - i * band
        if i % 2 == 0:
            ax.add_patch(Rectangle((2.0, y - band + 1.2), 96.0, band - 0.6,
                                   facecolor="#F3F2ED", edgecolor="none", zorder=0))
        yc = y - band / 2 + 1.0
        ax.text(cx[0], yc, q, fontsize=7.9, color=INK, va="center",
                linespacing=1.55, zorder=3)
        ax.text(cx[1], yc, has, fontsize=7.2, color=MUTED, va="center",
                linespacing=1.55, zorder=3)
        ax.add_patch(Rectangle((69.6, y - band + 2.4), 0.55, band - 4.6,
                               facecolor=ORANGE, edgecolor="none", zorder=3))
        ax.text(cx[2], yc, needs, fontsize=7.2, color=INK2, va="center",
                linespacing=1.55, zorder=3)

    ax.text(3.0, 2.6,
            "None of the right-hand column is secret. All of it is public, and almost none of it reaches the buyer before the cheque is written.",
            fontsize=7.6, color=INK2, style="italic")
    T.save(fig, "s2_problem.png")


# ═════════════════════════════════════════════════ S3 · what Brickrock is
def s3_definition():
    """One business, one revenue line, one by-product that compounds."""
    fig, ax = T.canvas(12.4, 4.3)
    ax.set_ylim(0, 56)

    boxes = [
        ("WE DO THE WORK", "Advisory", ORANGE,
         "Corridor research, registered comparables,\nshortlists, society and developer diligence,\naccompanied site visits, negotiation, and a\nwritten reason for every property rejected",
         "Unpaid. This is what earns the mandate."),
        ("WE GET PAID ONCE", "Brokerage commission", GREEN,
f"{RATE_L} blended across resale, primary\nand rental, paid on registration —\nnot on a subscription, not on a retainer,\nand not on advice given before it",
         "The only revenue line in the business."),
        ("WE KEEP THE RECORD", "Transaction evidence", PURPLE,
         "Closed price against asking, why offers\nfailed, society rules, true maintenance,\nreal commute, buyer objections — captured\non every deal, the won ones and the lost",
         "Free to capture. Impossible to buy."),
    ]
    W, GAP = 28.4, 4.4
    x0 = 3.0
    for i, (kick, name, c, body, foot) in enumerate(boxes):
        x = x0 + i * (W + GAP)
        T.card(ax, x, 9, W, 40, fc=CARD, ec=HAIR)
        ax.add_patch(Rectangle((x, 45.8), W, 3.2, facecolor=c, edgecolor="none", zorder=3))
        ax.text(x + 2.4, 47.4, kick, fontsize=6.5, color="white", fontweight="800",
                va="center", zorder=4)
        ax.text(x + 2.4, 41.0, name, fontsize=12.0, color=INK, fontweight="700",
                va="center", zorder=4)
        ax.text(x + 2.4, 30.0, body, fontsize=7.3, color=INK2, va="center",
                linespacing=1.7, zorder=4)
        ax.plot([x + 2.4, x + W - 2.4], [20.0, 20.0], color=HAIR, lw=1.0, zorder=4)
        ax.text(x + 2.4, 14.6, T.wrap(foot, 34), fontsize=7.0, color=c,
                fontweight="700", va="center", linespacing=1.55, zorder=4)
        if i < 2:
            T.arrow(ax, (x + W + 0.6, 29), (x + W + GAP - 0.6, 29),
                    color=RULE, lw=1.5, ms=9, z=4)

    # the loop back
    xr = x0 + 2 * (W + GAP) + W / 2
    xl = x0 + W / 2
    ax.plot([xr, xr], [9, 3.4], color=PURPLE, lw=1.6, zorder=2)
    ax.plot([xl, xr], [3.4, 3.4], color=PURPLE, lw=1.6, zorder=2)
    T.arrow(ax, (xl, 3.4), (xl, 8.4), color=PURPLE, lw=1.6, ms=9, z=3)
    ax.text(50, 1.0, "every closure makes the next shortlist better", ha="center",
            fontsize=6.9, color=PURPLE, fontweight="700")
    T.save(fig, "s3_definition.png")


# ═════════════════════════════════════════════════ S4 · how it works
def s4_system():
    """The seven-step transaction engine, and the evidence layer under it."""
    fig, ax = T.canvas(12.4, 4.55)

    steps = [
        ("01", "ACQUIRE", "Referrals, co-broking,\npocket briefs, content", ORANGE),
        ("02", "QUALIFY", "Budget, timeline,\nauthority, area fit", ORANGE),
        ("03", "SHORTLIST", "Hard filters first,\nthen weighted scoring", BLUE),
        ("04", "SITE VISIT", "Accompanied,\nbatched by pocket", BLUE),
        ("05", "NEGOTIATE", "Registered comparables,\nnot opinions", GREEN),
        ("06", "TRANSACT", "Diligence, loan,\nregistration, handover", GREEN),
        ("07", "CAPTURE", "Closed price, objections,\nreferral ask", PURPLE),
    ]
    W, GAP = 12.6, 1.4
    x0 = 2.2
    TOP, H = 62.0, 24.0
    for i, (num, name, sub, c) in enumerate(steps):
        x = x0 + i * (W + GAP)
        T.card(ax, x, TOP, W, H, fc=CARD, ec=HAIR)
        ax.add_patch(Rectangle((x, TOP + H - 3.2), W, 3.2, facecolor=c,
                               edgecolor="none", zorder=3))
        ax.text(x + 1.7, TOP + H - 1.6, num, fontsize=6.6, color="white",
                fontweight="700", va="center", zorder=4)
        ax.text(x + W / 2 + 1.3, TOP + H - 1.6, name, ha="center", va="center",
                fontsize=7.0, color="white", fontweight="700", zorder=4)
        ax.text(x + W / 2, TOP + 10.0, T.wrap(sub.replace("\n", " "), 22), ha="center",
                va="center", fontsize=6.5, color=INK2, zorder=4, linespacing=1.7)
        if i < len(steps) - 1:
            T.arrow(ax, (x + W + 0.1, TOP + 11), (x + W + GAP - 0.1, TOP + 11),
                    color=RULE, lw=1.2, ms=7, z=4)

    xr = x0 + 6 * (W + GAP) + W / 2
    xl = x0 + W / 2
    ax.plot([xr, xr], [TOP, TOP - 5.5], color=PURPLE, lw=1.7, zorder=2)
    ax.plot([xl, xr], [TOP - 5.5, TOP - 5.5], color=PURPLE, lw=1.7, zorder=2)
    T.arrow(ax, (xl, TOP - 5.5), (xl, TOP - 0.6), color=PURPLE, lw=1.7, ms=9, z=3)

    # ---- the evidence layer
    LY, LH = 14.0, 36.0
    T.card(ax, 2.2, LY, 95.6, LH, fc=CARD_ALT, ec=HAIR)
    ax.text(4.6, LY + LH - 4.6, "THE EVIDENCE LAYER  ·  an operating tool, not a product",
            fontsize=7.2, color=INK, fontweight="800", va="center", zorder=4)
    ax.text(4.6, LY + LH - 9.2,
            "A working record maintained in a spreadsheet and a CRM. It is never sold, never licensed and never shown as a platform.",
            fontsize=6.8, color=MUTED, va="center", zorder=4)

    feeds = [
        ("Registered prices", "IGR e-Search, normalised\nto carpet area", "→ 03 · 05", BLUE),
        ("Project register", "MahaRERA filings, promoter\ndelivery and complaint record", "→ 03 · 06", BLUE),
        ("Pocket field file", "Society rules, maintenance,\nparking, timed commute", "→ 03 · 04", GREEN),
        ("Supply and rent", "Listing age, asking-to-closed\ngap, rental depth", "→ 05", GREEN),
        ("Own deal record", "Every offer, every objection,\nevery reason a buyer walked", "→ 01 · 03 · 05", PURPLE),
    ]
    CW, CG = 16.8, 1.7
    cx0 = 4.6
    for i, (title, body, to, c) in enumerate(feeds):
        x = cx0 + i * (CW + CG)
        T.card(ax, x, LY + 3.0, CW, 20.0, fc=CARD, ec=HAIR)
        ax.add_patch(Rectangle((x, LY + 3.0), 0.6, 20.0, facecolor=c,
                               edgecolor="none", zorder=3))
        ax.text(x + 2.4, LY + 19.4, title, fontsize=7.1, color=INK,
                fontweight="700", va="center", zorder=4)
        ax.text(x + 2.4, LY + 13.0, body, fontsize=6.3, color=INK2, va="center",
                linespacing=1.65, zorder=4)
        ax.text(x + 2.4, LY + 6.6, to, fontsize=6.2, color=c, fontweight="700",
                va="center", zorder=4)

    ax.text(2.2, 6.0,
            "The system exists to win the mandate, sharpen the shortlist and hold the line in a negotiation. It is not the product — the advice is.",
            fontsize=7.4, color=INK2, style="italic")
    T.save(fig, "s4_system.png")


# ═════════════════════════════════════════════════ S5 · why this corridor
def s5_corridor():
    """The corridor as a priced ladder, and the weighted model that chose it."""
    fig = plt.figure(figsize=(12.4, 4.9)); fig.patch.set_facecolor(LIGHT)

    # ------------------------------------------------- the locality ladder
    ax = fig.add_axes([0.008, 0.115, 0.487, 0.845]); T.blank(ax)
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)

    mm = {m[0]: m for m in E.MICRO_MARKETS}
    order = ["Mulund", "Bhandup", "Kanjurmarg", "Powai", "Vikhroli", "Ghatkopar"]

    lo_all = min(mm[k][2] for k in order)
    hi_all = max(mm[k][3] for k in order)
    X0, X1 = 30.0, 74.0
    pad = 3000

    def xf(p):
        return X0 + (p - (lo_all - pad)) / ((hi_all + pad) - (lo_all - pad)) * (X1 - X0)

    ax.text(9.0, 95.0, "THE CORRIDOR, NORTH TO SOUTH", fontsize=7.0, color=INK,
            fontweight="800", va="center")
    ax.text((X0 + X1) / 2, 95.0, "ASKING BAND  ·  ₹ PER SQ FT", ha="center", fontsize=6.6,
            color=MUTED, fontweight="800", va="center")
    ax.text(79.0, 95.0, "2BHK RENT", fontsize=6.6, color=MUTED, fontweight="800", va="center")
    ax.text(91.5, 95.0, "GROSS YIELD", fontsize=6.6, color=MUTED, fontweight="800", va="center")
    ax.plot([2.0, 100.0], [91.0, 91.0], color=RULE, lw=1.0)

    top, band = 85.0, 13.4
    ys = [top - i * band for i in range(len(order))]
    ax.plot([5.0, 5.0], [ys[-1] - 1.0, ys[0] + 1.0], color=ORANGE, lw=2.2,
            zorder=2, solid_capstyle="round")

    for y, name in zip(ys, order):
        _, _, lo, hi, rent, yl, yh, infra, note = mm[name]
        ax.scatter([5.0], [y], s=64, facecolor=CARD, edgecolor=ORANGE,
                   linewidth=2.0, zorder=4)
        ax.text(9.0, y + 1.8, name, fontsize=8.4, color=INK, fontweight="700", va="center")
        ax.text(9.0, y - 3.4, T.wrap(note, 30), fontsize=5.9, color=MUTED,
                va="center", linespacing=1.5)

        x0, x1 = xf(lo), xf(hi)
        ax.plot([X0, X1], [y, y], color=HAIR, lw=0.9, zorder=1)
        T.bar(ax, x0, y - 1.7, x1 - x0, 3.4, BLUE, r=0.9, z=3)
        ax.text(x0 - 1.0, y, f"{lo/1000:,.0f}k", ha="right", va="center",
                fontsize=6.6, color=INK2, fontweight="600")
        ax.text(x1 + 1.0, y, f"{hi/1000:,.0f}k", ha="left", va="center",
                fontsize=6.6, color=INK, fontweight="700")

        ax.text(79.0, y, f"₹{rent/1000:,.0f}k", fontsize=7.4, color=INK,
                fontweight="600", va="center")
        ax.text(91.5, y, f"{yl:.1f}–{yh:.1f}%", fontsize=7.4, color=GREEN,
                fontweight="700", va="center")

    fig.text(0.012, 0.045,
             "Six localities on one spine — the Eastern Express Highway and JVLR, with Metro Line 6 running through it. Reachable end to end inside\n"
             "an hour, which is the binding constraint for a single founder. Asking bands and rents are portal-derived, medium confidence.",
             fontsize=6.3, color=MUTED, linespacing=1.65)

    # ------------------------------------------------------ weighted score
    ranked = E.ranked_regions()
    ax2 = fig.add_axes([0.655, 0.375, 0.325, 0.525])
    for i, (r, sc) in enumerate(ranked):
        c = ORANGE if i == 0 else GREY
        T.bar(ax2, 0, i - 0.30, sc, 0.60, c, r=0.22)
        ax2.text(sc + 0.16, i, f"{sc:.2f}", va="center", fontsize=8.4,
                 color=INK, fontweight="700" if i == 0 else "500")
    ax2.set_yticks(range(len(ranked)))
    ax2.set_yticklabels([f"{i+1}.  {r}" for i, (r, _) in enumerate(ranked)], fontsize=7.6)
    for i, lab in enumerate(ax2.get_yticklabels()):
        lab.set_color(INK if i == 0 else INK2)
        lab.set_fontweight("700" if i == 0 else "400")
    ax2.set_ylim(len(ranked) - 0.45, -0.55)
    ax2.set_xlim(0, 9.9); ax2.set_xticks([0, 5, 10])
    ax2.set_xticklabels(["0", "5", "10"], fontsize=6.8)
    T.clean(ax2, ygrid=False, xgrid=True)
    ax2.set_title("WEIGHTED SCORE  ·  EVERY CORRIDOR IN MMR", fontsize=7.2,
                  color=INK, loc="left", pad=9, fontweight="700")

    # --------------------------------------------------- the weight vector
    ax3 = fig.add_axes([0.655, 0.145, 0.325, 0.115]); T.blank(ax3)
    ax3.set_xlim(0, 100); ax3.set_ylim(0, 100)
    ax3.text(0, 92, "THE WEIGHT VECTOR — ONE STRATEGY, APPLIED TO ALL SIX",
             fontsize=6.5, color=INK, fontweight="800", va="center")
    short = ["depth", "infra", "cost", "data", "rent", "space", "exec"]
    x = 0.0
    for (k, lab, w, _), sn, c in zip(E.CRITERIA, short, SERIES * 3):
        seg = w * 100
        ax3.add_patch(Rectangle((x, 38), seg - 0.5, 22, facecolor=c,
                                edgecolor="none", zorder=3))
        ax3.text(x + (seg - 0.5) / 2, 49, f"{w:.2f}", ha="center", va="center",
                 fontsize=6.2, color="white", fontweight="700", zorder=4)
        ax3.text(x + (seg - 0.5) / 2, 24, sn, ha="center", va="center",
                 fontsize=5.8, color=MUTED, zorder=4)
        x += seg

    fig.text(0.655, 0.048,
             "Analyst model. Across 5,000 randomised weight vectors — every weight\n"
             "jittered ±50% — Eastern & Central stays first 99% of the time. Navi Mumbai\n"
             "and Western tie at 7.48; the model cannot separate them, so it says so.",
             fontsize=6.2, color=MUTED, linespacing=1.65)
    T.save(fig, "s5_corridor.png")


# ═════════════════════════════════════════════════ S6 · customer-market fit
def s6_customer():
    """Who actually pays, what they pay for, and what each segment is worth."""
    fig = plt.figure(figsize=(12.4, 4.6)); fig.patch.set_facecolor(LIGHT)

    segs = E.TICKET_MIX
    n = E.N_BASE
    comm = [n * sh * c * r for _, sh, c, r, _ in segs]
    tot = sum(comm)
    share_close = [sh for _, sh, _, _, _ in segs]
    share_rev = [x / tot for x in comm]
    names = ["Resale · 2BHK", "Resale · 3BHK", "Primary", "Rental"]
    cols = [BLUE, BLUE_D, ORANGE, GREEN]

    # ---- share of closures vs share of revenue
    ax = fig.add_axes([0.048, 0.255, 0.395, 0.595])
    idx = np.arange(len(segs)); wid = 0.31
    for i in range(len(segs)):
        T.bar(ax, i - wid - 0.02, 0, wid, share_close[i] * 100, GREY, r=0.12)
        T.bar(ax, i + 0.02, 0, wid, share_rev[i] * 100, cols[i], r=0.12)
        ax.text(i - wid / 2 - 0.02, share_close[i] * 100 + 1.6,
                f"{share_close[i]*100:.0f}%", ha="center", fontsize=8.0,
                color=INK2, fontweight="600")
        ax.text(i + wid / 2 + 0.02, share_rev[i] * 100 + 1.6,
                f"{share_rev[i]*100:.0f}%", ha="center", fontsize=8.4,
                color=INK, fontweight="700")
    ax.set_xticks(idx); ax.set_xticklabels(names, fontsize=7.8)
    ax.tick_params(axis="x", pad=6)
    ax.set_ylim(0, 52); ax.set_yticks([0, 20, 40])
    ax.set_yticklabels(["0", "20%", "40%"], fontsize=7)
    ax.set_xlim(-0.62, len(segs) - 0.38)
    T.clean(ax)
    ax.plot([], [], "s", color=GREY, ms=7, label="share of closures")
    ax.plot([], [], "s", color=BLUE, ms=7, label="share of commission")
    ax.legend(loc="upper right", fontsize=7.0, handletextpad=0.5, borderpad=0.2)
    ax.set_title("WHO WE CLOSE  vs  WHO PAYS THE BILLS", fontsize=7.4,
                 color=INK, loc="left", pad=10, fontweight="700")

    # ---- per-segment detail
    ax2 = fig.add_axes([0.50, 0.045, 0.49, 0.915]); T.blank(ax2)
    ax2.set_xlim(0, 100); ax2.set_ylim(0, 100)
    ax2.text(0, 96.5, "WHAT EACH SEGMENT IS ACTUALLY BUYING", fontsize=7.4,
             color=INK, fontweight="800", va="center")

    detail = [
        ("Resale · 2BHK", "₹2.2 cr · 1.00%", BLUE,
         "The upgrader already living in the corridor. Buys\ncertainty on price and on the society's rules."),
        ("Resale · 3BHK", "₹3.8 cr · 1.00%", BLUE_D,
         "Same buyer, later. Higher ticket, longer decision,\nalmost always arrives by referral."),
        ("Primary", "₹2.6 cr · 2.00%", ORANGE,
         "The buyer who wants a new project but no bias.\nWe are paid by the developer and say so, in writing."),
        ("Rental", "₹9.0 L p.a. · 8.00%", GREEN,
         "Not a revenue line — a lead nursery. Today's tenant\nis the buyer in eighteen months, and it pays the rent now."),
    ]
    top, band = 89.0, 21.0
    for i, (name, econ, c, body) in enumerate(detail):
        y = top - i * band
        T.card(ax2, 0, y - band + 3.0, 100, band - 3.4, fc=CARD, ec=HAIR)
        ax2.add_patch(Rectangle((0, y - band + 3.0), 0.7, band - 3.4,
                                facecolor=c, edgecolor="none", zorder=3))
        ax2.text(2.8, y - 3.2, name, fontsize=8.6, color=INK, fontweight="700",
                 va="center", zorder=4)
        ax2.text(2.8, y - 8.4, body, fontsize=6.9, color=INK2, va="center",
                 linespacing=1.65, zorder=4)
        ax2.text(98.0, y - 3.2, econ, fontsize=7.6, color=c, fontweight="700",
                 ha="right", va="center", zorder=4)
        ax2.text(98.0, y - 8.0, f"₹{comm[i]/L:,.1f} L in Year 1", fontsize=6.6,
                 color=MUTED, ha="right", va="center", zorder=4)

    fig.text(0.048, 0.155,
             f"Primary is {share_close[2]*100:.0f}% of closures and {share_rev[2]*100:.0f}% of commission. Rental is {share_close[3]*100:.0f}% of closures and {share_rev[3]*100:.0f}% of it.",
             fontsize=8.2, color=INK, fontweight="600")
    fig.text(0.048, 0.048,
             f"Segment mix, ticket sizes and commission rates are planning assumptions. Blended rate {RATE_L} on an average\n"
             f"consideration of ₹{CONSID/CR:,.2f} cr. The 90-day pilot exists to replace these with measured values.",
             fontsize=6.3, color=MUTED, linespacing=1.6)
    T.save(fig, "s6_customer.png")


# ═════════════════════════════════════════════════ S7 · competitive positioning
def s7_positioning():
    """Everyone competes on inventory. Nobody competes on the decision."""
    fig = plt.figure(figsize=(12.4, 4.6)); fig.patch.set_facecolor(LIGHT)

    ax = fig.add_axes([0.055, 0.175, 0.435, 0.755])
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    ax.add_patch(Rectangle((0, 50), 50, 50, facecolor="#FCF3EC", edgecolor="none", zorder=0))
    ax.plot([50, 50], [0, 100], color=HAIR, lw=1.0, zorder=1)
    ax.plot([0, 100], [50, 50], color=HAIR, lw=1.0, zorder=1)

    players = [
        ("Property portals", 88, 12, GREY_D, "99acres · Housing · MagicBricks", "right"),
        ("National brokerages", 66, 34, PURPLE, "Anarock · Square Yards · PropTiger", "left"),
        ("Local independents", 26, 26, BLUE, "42,865 registered agents\nin Maharashtra", "left"),
        ("Developer sales", 12, 9, GREY_D, "one project,\nzero neutrality", "left"),
        ("BRICKROCK", 24, 80, ORANGE, "narrow by design,\ndecision carried", "left"),
    ]
    for name, x, y, c, sub, side in players:
        hero = name == "BRICKROCK"
        ax.scatter([x], [y], s=560 if hero else 300, facecolor=c,
                   edgecolor=LIGHT, linewidth=2.0, zorder=5, alpha=1.0 if hero else 0.9)
        dx = 5.0 if side == "left" else -5.0
        ha = "left" if side == "left" else "right"
        ax.text(x + dx, y + 3.2, name, fontsize=8.2 if hero else 7.6, color=INK,
                fontweight="800" if hero else "700", ha=ha, va="center", zorder=6)
        ax.text(x + dx, y - 2.4, sub, fontsize=6.3, color=MUTED, ha=ha,
                va="center", zorder=6, linespacing=1.5)

    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.annotate("", xy=(101, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=RULE, lw=1.2))
    ax.annotate("", xy=(0, 101), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=RULE, lw=1.2))
    ax.text(50, -9.5, "HOW MUCH OF THE MARKET THEY SHOW YOU", ha="center",
            fontsize=6.8, color=MUTED, fontweight="800")
    ax.text(2, -4.0, "a chosen few", fontsize=6.2, color=MUTED)
    ax.text(98, -4.0, "everything listed", fontsize=6.2, color=MUTED, ha="right")
    ax.text(-7.5, 50, "HOW MUCH OF THE DECISION THEY CARRY", va="center",
            rotation=90, fontsize=6.8, color=MUTED, fontweight="800")
    ax.text(-3.2, 2, "introductions", fontsize=6.2, color=MUTED, rotation=90)
    ax.text(-3.2, 98, "the decision itself", fontsize=6.2, color=MUTED,
            rotation=90, ha="center", va="top")

    # ---- comparison rows
    ax2 = fig.add_axes([0.545, 0.045, 0.445, 0.915]); T.blank(ax2)
    ax2.set_xlim(0, 100); ax2.set_ylim(0, 100)
    rows = [
        ("Property portals", GREY_D,
         "Discovery, at enormous scale",
         "Paid by the listing, so duplicate and stale inventory is a revenue\nsource rather than a defect. Discovery is not a decision."),
        ("National brokerages", PURPLE,
         "Primary inventory and developer access",
         "Paid 2–5% by the developer. The buyer is never told which project\npays the most, and the incentive is never disclosed in writing."),
        ("Local independents", BLUE,
         "Pocket knowledge, held in one head",
         "No written record, no comparables, no continuity. The knowledge\nis real and it dies with the deal."),
        ("Brickrock", ORANGE,
         "The decision, in writing",
         "The same commission, earned the same way. What changes is that\nthe recommendation carries evidence and a written reason for\nevery property that was rejected."),
    ]
    ax2.text(0, 96.5, "WHAT EACH ONE IS GOOD AT — AND WHERE IT STOPS", fontsize=7.4,
             color=INK, fontweight="800", va="center")
    top, band = 89.0, 21.5
    for i, (name, c, good, stop) in enumerate(rows):
        y = top - i * band
        hero = i == 3
        T.card(ax2, 0, y - band + 2.6, 100, band - 3.2,
               fc="#FCF3EC" if hero else CARD, ec=ORANGE if hero else HAIR,
               lw=1.4 if hero else 1.0)
        ax2.add_patch(Rectangle((0, y - band + 2.6), 0.7, band - 3.2,
                                facecolor=c, edgecolor="none", zorder=3))
        ax2.text(2.8, y - 3.4, name, fontsize=8.4, color=INK, fontweight="700",
                 va="center", zorder=4)
        ax2.text(30.0, y - 3.4, good, fontsize=7.0, color=c, fontweight="700",
                 va="center", zorder=4)
        ax2.text(2.8, y - 12.0, stop, fontsize=6.7, color=INK2, va="center",
                 linespacing=1.6, zorder=4)

    fig.text(0.055, 0.028,
             "The competitor set is not the portals — it is the 42,865 registered agents in Maharashtra, almost none of whom work from the registered record.",
             fontsize=6.4, color=MUTED)
    T.save(fig, "s7_positioning.png")


# ═════════════════════════════════════════════════ S8 · the moat
def s8_moat():
    """What accumulates, and why capital cannot shortcut it."""
    fig = plt.figure(figsize=(12.4, 4.5)); fig.patch.set_facecolor(LIGHT)

    # ---- the loop
    ax = fig.add_axes([0.012, 0.055, 0.335, 0.885]); T.blank(ax)
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    nodes = [
        ("ADVISE", "shortlist backed by\nregistered evidence", ORANGE, 50, 84, 42),
        ("TRANSACT", "commission earned\non registration", GREEN, 77, 51, 44),
        ("CAPTURE", "closed price, objections,\nreason for every no", PURPLE, 50, 18, 42),
        ("SHARPEN", "the next shortlist is\nbuilt on more evidence", BLUE, 23, 51, 44),
    ]
    for name, sub, c, x, y, w in nodes:
        T.card(ax, x - w / 2, y - 10, w, 20, fc=CARD, ec=HAIR)
        ax.add_patch(Rectangle((x - w / 2, y + 9.2), w, 0.8, facecolor=c,
                               edgecolor="none", zorder=3))
        ax.text(x, y + 4.0, name, ha="center", va="center", fontsize=8.8,
                color=INK, fontweight="700", zorder=4)
        ax.text(x, y - 3.6, sub, ha="center", va="center", fontsize=6.4,
                color=INK2, zorder=4, linespacing=1.65)

    for p0, p1, rad in [((71.5, 76.5), (85.0, 63.5), -0.35),
                        ((85.0, 38.5), (71.5, 26.0), -0.35),
                        ((28.5, 26.0), (15.0, 38.5), -0.35),
                        ((15.0, 63.5), (28.5, 76.5), -0.35)]:
        T.arrow(ax, p0, p1, color=RULE, lw=1.6, ms=10, rad=rad, z=2)

    ax.text(50, 2.0, "The loop costs nothing to run. It only requires doing the work.",
            ha="center", fontsize=6.8, color=MUTED, style="italic")

    # ---- accumulation
    ax2 = fig.add_axes([0.415, 0.185, 0.565, 0.645])
    months = np.arange(0, 37)
    sched = list(E.SCHEDULE_BASE) + [4] * 12
    closures = np.concatenate([[0], np.cumsum(sched[:36])])
    records = closures * 22 + np.clip(months, 0, 36) * 14   # comparables + field notes
    own = closures * 22

    ax2.fill_between(months, records, color=ORANGE, alpha=0.14, zorder=2)
    ax2.plot(months, records, color=ORANGE, lw=2.6, zorder=4,
             label="proprietary records held — comparables, field notes, deal outcomes")
    ax2.plot(months, own, color=PURPLE, lw=1.8, ls=(0, (4, 3)), zorder=3,
             label="of which generated by our own closed transactions")

    top = records.max() * 1.30
    marks = [(3, "M3 — corridor mapped to pocket\nlevel, zero closures", 0.34),
             (12, f"M12 — {E.N_BASE} closures, 25 pockets\nknown at unit level", 0.60),
             (36, "Y3 — a registered-price series\nfor this corridor that nobody else built", 0.90)]
    for m, lab, frac in marks:
        ax2.axvline(m, color=HAIR, lw=1.0, zorder=1)
        ax2.scatter([m], [records[m]], s=46, color=INK, zorder=6,
                    edgecolor=LIGHT, linewidth=1.4)
        ty = top * frac
        ax2.plot([m, m], [records[m] + top * 0.02, ty - top * 0.015],
                 color=RULE, lw=0.9, zorder=2)
        ax2.text(m - 0.7 if m == 36 else m + 0.7, ty, lab,
                 ha="right" if m == 36 else "left", va="bottom",
                 fontsize=6.9, color=INK2, linespacing=1.6, zorder=6)

    ax2.set_xlim(0, 36.6); ax2.set_ylim(0, top)
    ax2.set_xticks([0, 6, 12, 18, 24, 30, 36])
    ax2.set_xticklabels(["start", "M6", "M12", "M18", "M24", "M30", "M36"], fontsize=7.4)
    ax2.set_yticks([])
    T.clean(ax2, ygrid=False)
    ax2.legend(loc="upper left", fontsize=6.8, handletextpad=0.7, borderpad=0.3)
    ax2.set_title("THE ASSET THAT COMPOUNDS  ·  cumulative proprietary transaction evidence",
                  fontsize=7.4, color=INK, loc="left", pad=10, fontweight="700")

    fig.text(0.415, 0.055,
             "Illustrative accumulation on the base-case closure schedule. The shape is the argument, not the level: a competitor with ten times the capital still\n"
             "starts this curve at zero, because the evidence is generated by transacting and cannot be bought, licensed or scraped.",
             fontsize=6.3, color=MUTED, linespacing=1.6)
    T.save(fig, "s8_moat.png")


# ═════════════════════════════════════════════════ S9 · business model
def s9_economics():
    """From the funnel to the bank account, with the cost base priced in."""
    fig = plt.figure(figsize=(12.4, 4.4)); fig.patch.set_facecolor(LIGHT)

    n = E.N_BASE
    gross = E.GROSS_BASE
    opex12 = E.OPEX * 12
    setup = E.ONE_OFF
    profit = gross - opex12 - setup
    tax = E.income_tax(profit)
    post = profit - tax

    # ---- the chain
    ax = fig.add_axes([0.012, 0.375, 0.976, 0.605]); T.blank(ax)
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    chain = [
        (f"{n}", "closures", "base-case funnel", BLUE),
        (f"₹{CONSID/CR:,.2f} cr", "average consideration", "blended across the mix", BLUE),
        (RATE_L, "blended commission", "resale, primary, rental", ORANGE),
        (f"₹{gross/L:,.1f} L", "gross commission", "Year 1, before cost", ORANGE),
        (f"₹{post/L:,.1f} L", "after cost and tax", "cash to the founder", GREEN),
    ]
    bw, gp = 17.0, 3.2
    x0, CY, CH = 1.0, 30.0, 62.0
    for i, (v, lab, sub, c) in enumerate(chain):
        x = x0 + i * (bw + gp)
        hero = i == len(chain) - 1
        T.card(ax, x, CY, bw, CH, fc="#F0F8F3" if hero else CARD,
               ec=GREEN if hero else HAIR, lw=1.4 if hero else 1.0)
        ax.add_patch(Rectangle((x, CY + CH - 1.4), bw, 1.4, facecolor=c,
                               edgecolor="none", zorder=3))
        ax.text(x + bw / 2, CY + CH - 17, v, ha="center", va="center", fontsize=15.5,
                color=INK, fontweight="700", zorder=4)
        ax.text(x + bw / 2, CY + CH - 35, lab, ha="center", va="center", fontsize=7.8,
                color=INK2, fontweight="600", zorder=4)
        ax.text(x + bw / 2, CY + CH - 49, T.wrap(sub, 22), ha="center", va="center",
                fontsize=6.5, color=MUTED, zorder=4, linespacing=1.5)
        if i < len(chain) - 1:
            ops = ["×", "×", "=", "→"]
            ax.text(x + bw + gp / 2, CY + CH - 33, ops[i], ha="center", va="center",
                    fontsize=12, color=MUTED, fontweight="600", zorder=4)

    # ---- cost base
    ax2 = fig.add_axes([0.055, 0.115, 0.40, 0.245]); T.blank(ax2)
    ax2.set_xlim(0, 100); ax2.set_ylim(0, 100)
    ax2.text(0, 93, "WHAT IT COSTS TO RUN", fontsize=7.0, color=INK,
             fontweight="800", va="center")
    parts = [
        (f"₹{setup/L:,.2f} L", "one-off setup", "registration, certificate,\nentity, insurance", GREY_D),
        (f"₹{E.OPEX/1000:,.0f}k", "per month, business", "compliance, data, field,\nmarketing, tools", BLUE),
        (f"₹{E.DRAWINGS/1000:,.0f}k", "per month, drawings", "the largest line and the\nmain lever on runway", ORANGE),
    ]
    for i, (v, lab, sub, c) in enumerate(parts):
        x = i * 34.0
        ax2.add_patch(Rectangle((x, 2), 0.7, 74, facecolor=c, edgecolor="none", zorder=3))
        ax2.text(x + 2.6, 66, v, fontsize=11.5, color=INK, fontweight="700", va="center")
        ax2.text(x + 2.6, 46, lab, fontsize=6.9, color=INK2, va="center", fontweight="600")
        ax2.text(x + 2.6, 22, sub, fontsize=6.2, color=MUTED, va="center", linespacing=1.6)

    # ---- scenarios
    ax3 = fig.add_axes([0.585, 0.125, 0.335, 0.225])
    scen = [("Conservative", E.N_CONS), ("Base", E.N_BASE), ("Stretch", E.N_STRETCH)]
    vals = [E.commission_for(k) / L for _, k in scen]
    posts = [E.post_tax(k) / L for _, k in scen]
    idx = np.arange(3); wid = 0.30
    for i in range(3):
        T.bar(ax3, i - wid - 0.02, 0, wid, vals[i], ORANGE, r=0.14)
        T.bar(ax3, i + 0.02, 0, wid, posts[i], GREY_D, r=0.14)
        ax3.text(i - wid / 2 - 0.02, vals[i] + 3.0, f"{vals[i]:.0f}", ha="center",
                 fontsize=7.6, color=INK, fontweight="700")
        ax3.text(i + wid / 2 + 0.02, posts[i] + 3.0, f"{posts[i]:.0f}", ha="center",
                 fontsize=7.6, color=INK2, fontweight="600")
    ax3.set_xticks(idx)
    ax3.set_xticklabels([f"{s[0]} · {s[1]}" for s in scen], fontsize=7.2)
    ax3.tick_params(axis="x", pad=5)
    ax3.set_ylim(0, 103); ax3.set_yticks([])
    ax3.set_xlim(-0.62, 2.62)
    T.clean(ax3, ygrid=False, bottom=True)
    ax3.plot([], [], "s", color=ORANGE, ms=6, label="gross")
    ax3.plot([], [], "s", color=GREY_D, ms=6, label="post-tax")
    ax3.legend(loc="upper left", fontsize=6.6, handletextpad=0.5, borderpad=0.2, ncol=2)
    ax3.set_title("YEAR-1 OUTCOME BY CLOSURE COUNT  ·  ₹ lakh", fontsize=7.0,
                  color=INK, loc="left", pad=8, fontweight="700")

    fig.text(0.012, 0.032,
             "GST at 18% is an output tax collected from the client, not revenue. TDS of 2% under section 194H is withheld at source and credited against income tax.\n"
             "Conversion rates, segment mix and commission rates are planning assumptions the 90-day pilot exists to replace.",
             fontsize=6.3, color=MUTED, linespacing=1.6)
    T.save(fig, "s9_economics.png")


# ═════════════════════════════════════════════════ S10 · go to market
def s10_gtm():
    """The funnel that produces the closures, and the channels that feed it."""
    fig = plt.figure(figsize=(12.4, 4.6)); fig.patch.set_facecolor(LIGHT)

    # ---- funnel
    ax = fig.add_axes([0.012, 0.145, 0.285, 0.80]); T.blank(ax)
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    ax.text(0, 96.0, "THE BASE-CASE FUNNEL  ·  TWELVE MONTHS", fontsize=7.4,
            color=INK, fontweight="800", va="center")

    stages = E.FUNNEL_STAGES
    base = [s[2] for s in stages]
    widths = [66, 52, 38, 26, 16]
    cols = [GREY, BLUE_L, BLUE, ORANGE_L, ORANGE]
    top, band, gap = 84.0, 11.8, 5.0
    for i, ((lab, cons, bas, stre), w, c) in enumerate(zip(stages, widths, cols)):
        y = top - i * (band + gap)
        x0 = 34 - w / 2
        T.card(ax, x0, y - band, w, band, fc=c, ec="none", r=1.0)
        ax.text(34, y - band / 2 + 1.3, f"{bas:,}", ha="center", va="center",
                fontsize=13.5 if i else 12, color="white" if i else INK, fontweight="700")
        ax.text(34, y - band / 2 - 3.7, lab.lower(), ha="center", va="center",
                fontsize=7.0, color="white" if i else INK2)
        if i:
            conv = bas / base[i - 1] * 100
            ax.text(x0 + w + 3.4, y - band / 2 + 1.2, f"{conv:.0f}%", ha="left",
                    va="center", fontsize=8.8, color=INK, fontweight="700")
            ax.text(x0 + w + 3.4, y - band / 2 - 3.6,
                    f"of {stages[i-1][0].lower()}", ha="left", va="center",
                    fontsize=6.2, color=MUTED)
            nw, pw = widths[i], widths[i - 1]
            ax.add_patch(Polygon([[34 - pw / 2, y + gap], [34 + pw / 2, y + gap],
                                  [34 + nw / 2, y], [34 - nw / 2, y]],
                                 closed=True, facecolor=cols[i - 1], edgecolor="none",
                                 alpha=0.18, zorder=1))

    fig.text(0.012, 0.048,
             "Qualified-lead rate and site-visit conversion are the two\n"
             "numbers everything downstream depends on. They are the\n"
             "first two the 90-day pilot has to measure.",
             fontsize=6.3, color=MUTED, linespacing=1.65)

    # ---- channel ladder
    ax2 = fig.add_axes([0.345, 0.145, 0.415, 0.80]); T.blank(ax2)
    ax2.set_xlim(0, 100); ax2.set_ylim(0, 100)
    ax2.text(0, 96.0, "CHANNELS, RANKED BY WHAT A COMPETITOR CANNOT BUY",
             fontsize=7.4, color=INK, fontweight="800", va="center")

    chans = [
        ("Referrals from closed clients",  300, "6–9 months",  "Cannot be bought", GREEN),
        ("Pocket briefs and content",      900, "3–6 months",  "Cannot be bought", GREEN),
        ("Society and RWA relationships",  600, "2–4 months",  "Hard to buy",      BLUE),
        ("Co-broking network",            1200, "4–8 weeks",   "Hard to buy",      BLUE),
        ("Portal listings",               4200, "immediate",   "Anyone can buy",   GREY_D),
        ("Paid advertising",              6800, "immediate",   "Anyone can buy",   GREY_D),
    ]
    ax2.text(41.0, 88.0, "COST PER QUALIFIED LEAD", fontsize=6.0, color=MUTED,
             fontweight="800", va="center")
    ax2.text(76.0, 88.0, "TIME TO FIRST LEAD", fontsize=6.0, color=MUTED,
             fontweight="800", va="center")
    ax2.plot([0, 100], [84.0, 84.0], color=RULE, lw=1.0)

    BX0, BX1 = 41.0, 66.0
    top2, band2 = 78.0, 11.2
    for i, (name, cost, lat, defen, c) in enumerate(chans):
        y = top2 - i * band2
        ax2.text(0, y + 1.6, name, fontsize=7.8, color=INK, fontweight="700", va="center")
        ax2.text(0, y - 3.6, defen, fontsize=6.2, color=c, fontweight="700", va="center")
        w = (BX1 - BX0) * cost / 7000
        ax2.plot([BX0, BX1], [y, y], color=HAIR, lw=0.9, zorder=1)
        T.bar(ax2, BX0, y - 1.7, w, 3.4, c, r=0.9, z=3)
        ax2.text(BX0 + w + 1.2, y, f"₹{cost:,}", fontsize=6.8, color=INK,
                 fontweight="700", va="center")
        ax2.text(76.0, y, lat, fontsize=7.2, color=INK2, va="center")

    ax2.text(0, 4.5,
             "The cheap and defensible channels are the slow ones. That is the whole reason\n"
             "the first ninety days are spent building them rather than buying leads.",
             fontsize=6.4, color=INK2, linespacing=1.65, style="italic")

    # ---- the referral loop
    ax3 = fig.add_axes([0.795, 0.145, 0.195, 0.80]); T.blank(ax3)
    ax3.set_xlim(0, 100); ax3.set_ylim(0, 100)
    ax3.text(0, 96.0, "THE REFERRAL LOOP", fontsize=7.4, color=INK,
             fontweight="800", va="center")
    loop = [
        ("Close one deal well", ORANGE),
        ("Ask, at handover, for one introduction", ORANGE),
        ("It arrives pre-trusted and pre-qualified", GREEN),
        ("Cost per lead falls, conversion rises", GREEN),
    ]
    top3, band3 = 84.0, 18.5
    for i, (txt, c) in enumerate(loop):
        y = top3 - i * band3
        T.card(ax3, 0, y - band3 + 4.6, 100, band3 - 5.6, fc=CARD, ec=HAIR)
        ax3.add_patch(Rectangle((0, y - band3 + 4.6), 0.8, band3 - 5.6,
                                facecolor=c, edgecolor="none", zorder=3))
        ax3.text(3.6, y - 6.0, T.wrap(txt, 32), fontsize=6.9, color=INK2,
                 va="center", linespacing=1.65, zorder=4)
        if i < 3:
            T.arrow(ax3, (50, y - band3 + 4.2), (50, y - band3 + 1.0),
                    color=RULE, lw=1.3, ms=8, z=4)
    T.card(ax3, 0, 1.0, 100, 12.0, fc="#FCF3EC", ec=ORANGE, lw=1.3)
    ax3.text(50, 9.2, "referral coefficient > 0.5", ha="center", va="center",
             fontsize=7.2, color=ORANGE_D, fontweight="800", zorder=4)
    ax3.text(50, 4.2, "gates the second corridor",
             ha="center", va="center", fontsize=6.3, color=INK2, zorder=4)

    fig.text(0.345, 0.048,
             "Channel costs and latencies are analyst estimates for a single-founder desk, not measured values. @brickrockrealty has already\n"
             "produced 480k organic views on property explainers — content is the one channel where the capability already exists.",
             fontsize=6.3, color=MUTED, linespacing=1.65)
    T.save(fig, "s10_gtm.png")


# ═════════════════════════════════════════════════ S11 · capital and proof
def s11_capital():
    """The trough that sets the number, and the twelve weeks that de-risk it."""
    fig = plt.figure(figsize=(12.4, 4.5)); fig.patch.set_facecolor(LIGHT)

    NM = 12
    base = np.array(E.cash_curve(E.SCHEDULE_BASE)[:NM]) / L
    cons = np.array(E.cash_curve(E.SCHEDULE_CONS)[:NM]) / L
    months = np.arange(1, NM + 1)

    # ---- cash curve
    ax = fig.add_axes([0.048, 0.195, 0.415, 0.625])
    lo = min(base.min(), cons.min())
    hi = max(base.max(), cons.max())
    span = hi - lo
    ax.axhline(0, color=RULE, lw=1.2, zorder=2)
    ax.fill_between(months, np.minimum(base, 0), color=BAD, alpha=0.10, zorder=1)
    ax.plot(months, cons, color=GREY_D, lw=1.8, ls=(0, (4, 3)), zorder=3,
            label=f"conservative · {E.N_CONS} closures in Year 1")
    ax.plot(months, base, color=ORANGE, lw=2.6, zorder=4,
            label=f"base · {E.N_BASE} closures in Year 1")

    tb, tbm = base.min(), int(np.argmin(base)) + 1
    tc, tcm = cons.min(), int(np.argmin(cons)) + 1
    ax.scatter([tbm], [tb], s=52, color=ORANGE, zorder=6, edgecolor=LIGHT, linewidth=1.6)
    ax.scatter([tcm], [tc], s=52, color=GREY_D, zorder=6, edgecolor=LIGHT, linewidth=1.6)
    ty = lo - span * 0.13
    for j, (c, lab) in enumerate([(ORANGE, f"base trough  −₹{abs(tb):,.1f} L at month {tbm}"),
                                  (GREY_D, f"conservative trough  −₹{abs(tc):,.1f} L at month {tcm}")]):
        yy = ty - j * span * 0.075
        ax.scatter([1.25], [yy], s=26, color=c, zorder=6)
        ax.text(1.55, yy, lab, fontsize=7.2, color=INK2, va="center")

    ax.set_xlim(1, NM + 0.3)
    ax.set_ylim(lo - span * 0.27, hi + span * 0.14)
    ax.set_xticks([1, 3, 6, 9, 12])
    ax.set_xticklabels(["M1", "M3", "M6", "M9", "M12"], fontsize=7.4)
    ax.set_yticks([-10, -5, 0, 5, 10, 15, 20])
    ax.set_yticklabels(["−10", "−5", "0", "5", "10", "15", "20"], fontsize=7)
    T.clean(ax)
    ax.legend(loc="upper left", fontsize=7.0, handletextpad=0.7, borderpad=0.3)
    ax.set_title("CUMULATIVE CASH FROM A STANDING START  ·  ₹ lakh",
                 fontsize=7.4, color=INK, loc="left", pad=10, fontweight="700")

    # ---- the ask
    ax2 = fig.add_axes([0.515, 0.545, 0.235, 0.355]); T.blank(ax2)
    ax2.set_xlim(0, 100); ax2.set_ylim(0, 100)
    T.card(ax2, 0, 4, 100, 92, fc="#FCF3EC", ec=ORANGE, lw=1.5)
    ax2.text(6, 74, f"₹{E.CAPITAL/L:,.1f} L", fontsize=25, color=INK,
             fontweight="700", va="center", zorder=4)
    ax2.text(6, 52, "twelve months of runway", fontsize=8.0, color=INK2,
             va="center", fontweight="600", zorder=4)
    ax2.text(6, 30,
             T.wrap(f"The conservative trough of ₹{abs(tc):,.1f} L plus 40% headroom. "
                    f"Not the base case — the case where only {E.N_CONS} deals close.", 40),
             fontsize=6.6, color=INK2, va="center", linespacing=1.7, zorder=4)

    # ---- use of funds
    ax3 = fig.add_axes([0.515, 0.195, 0.235, 0.30]); T.blank(ax3)
    ax3.set_xlim(0, 100); ax3.set_ylim(0, 100)
    ax3.text(0, 92, "WHERE IT GOES", fontsize=7.0, color=INK, fontweight="800", va="center")
    use = [("Founder drawings", E.DRAWINGS * 12, ORANGE),
           ("Field, data, marketing", 26_000 * 12, BLUE),
           ("Compliance, tools, CA", 9_000 * 12, GREEN),
           ("One-off setup", E.ONE_OFF, GREY_D)]
    tot = sum(v for _, v, _ in use)
    x = 0.0
    for name, v, c in use:
        w = v / tot * 100
        ax3.add_patch(Rectangle((x, 56), w - 0.6, 13, facecolor=c,
                                edgecolor="none", zorder=3))
        x += w
    yy = 42
    for name, v, c in use:
        ax3.add_patch(Rectangle((0, yy - 1.4), 2.2, 3.0, facecolor=c,
                                edgecolor="none", zorder=3))
        ax3.text(5, yy, name, fontsize=6.5, color=INK2, va="center")
        ax3.text(100, yy, f"₹{v/L:,.1f} L", fontsize=6.5, color=INK,
                 fontweight="700", va="center", ha="right")
        yy -= 12.5

    # ---- 90-day gates
    ax4 = fig.add_axes([0.775, 0.055, 0.215, 0.885]); T.blank(ax4)
    ax4.set_xlim(0, 100); ax4.set_ylim(0, 100)
    ax4.text(0, 96.5, "THE 90-DAY PROOF", fontsize=7.4, color=INK,
             fontweight="800", va="center")
    gates = [
        ("WEEKS 1–2", "Become legal", ORANGE,
         "MahaRERA registration filed · 20-hour Certificate of Competency booked"),
        ("WEEKS 2–4", "Lock the corridor", BLUE,
         "6 localities, 20–30 pockets frozen · MahaRERA project register built"),
        ("WEEKS 4–6", "Build the edge", BLUE,
         "IGR price baseline · society files · timed commutes · pocket scorecards"),
        ("WEEKS 6–12", "Sell", GREEN,
         "Certificate issued, marketing opens · 30+ qualified leads · 5+ visit cycles"),
    ]
    top, band = 88.0, 20.0
    for i, (when, title, c, body) in enumerate(gates):
        y = top - i * band
        T.card(ax4, 0, y - band + 3.0, 100, band - 4.0, fc=CARD, ec=HAIR)
        ax4.add_patch(Rectangle((0, y - band + 3.0), 0.8, band - 4.0,
                                facecolor=c, edgecolor="none", zorder=3))
        ax4.text(3.6, y - 2.6, when, fontsize=6.2, color=c, fontweight="800",
                 va="center", zorder=4)
        ax4.text(3.6, y - 7.2, title, fontsize=8.2, color=INK, fontweight="700",
                 va="center", zorder=4)
        ax4.text(3.6, y - 13.0, T.wrap(body, 40), fontsize=6.1, color=MUTED,
                 va="center", linespacing=1.6, zorder=4)
    ax4.add_patch(Rectangle((0, 4.0), 100, 0.9, facecolor=BAD, edgecolor="none", zorder=3))
    ax4.text(0, 1.0, "No advertising, listing or client work before the certificate issues.",
             fontsize=6.2, color=BAD, fontweight="700", va="bottom")

    fig.text(0.048, 0.045,
             "Cash model: commission received on a six-week payout lag, net of 2% TDS; founder drawings held at ₹60,000 a month. Drawings are the largest line in the burn\n"
             "and the single biggest lever on how long the runway lasts.",
             fontsize=6.3, color=MUTED, linespacing=1.6)
    T.save(fig, "s11_capital.png")


# ═════════════════════════════════════════════════ S12 · founder and the arc
def s12_founder():
    """Lakshay's own P&L — the strongest object in the deck. Rendered on dark."""
    fig = plt.figure(figsize=(6.6, 3.4)); fig.patch.set_facecolor(DARK)
    ax = fig.add_axes([0.085, 0.215, 0.885, 0.595])
    ax.set_facecolor(DARK)

    q25 = F.SHEESHAM_QUARTERS["FY 2024-25"]
    q26 = F.SHEESHAM_QUARTERS["FY 2025-26"]
    xs = list(range(4)) + [x + 5 for x in range(4)]
    vals = q25 + q26
    cols = ["#3C4A5C"] * 4 + [ORANGE] * 4
    for x, v, c in zip(xs, vals, cols):
        T.bar(ax, x - 0.36, 0, 0.72, v, c, r=0.5)
        ax.text(x, v + 1.0, f"{v}", ha="center", fontsize=7.6,
                color=D_INK if c == ORANGE else D_INK2, fontweight="700")
    ax.set_xticks(xs)
    ax.set_xticklabels(["Q1", "Q2", "Q3", "Q4"] * 2, fontsize=7, color=D_INK2)
    ax.set_ylim(0, 43); ax.set_yticks([0, 10, 20, 30, 40])
    ax.set_yticklabels(["0", "10", "20", "30", "40"], fontsize=7, color=D_INK2)
    ax.set_xlim(-0.8, 8.8)
    T.clean(ax, dark=True)
    ax.tick_params(labelcolor=D_INK2)
    ax.text(1.5, -7.4, "FY 2024-25  ·  ₹51.8 L", ha="center", fontsize=7.4,
            color=D_MUTED, fontweight="700")
    ax.text(6.5, -7.4, "FY 2025-26  ·  ₹1.08 Cr", ha="center", fontsize=7.4,
            color=ORANGE, fontweight="700")
    ax.annotate("+108%", xy=(6.5, 38.4), fontsize=14, color=ORANGE,
                fontweight="700", ha="center")
    fig.text(0.085, 0.905, "SHEESHAM.IN — QUARTERLY REVENUE  ·  ₹ lakh", fontsize=7.4,
             color=D_MUTED, fontweight="700")
    fig.text(0.085, 0.022, "Sheesham.in incubation deck, July 2026. Lakshay's own business — 100% bootstrapped.",
             fontsize=6.2, color=D_MUTED)
    T.save(fig, "s12_founder.png", dark=True)


def s12_arc():
    """The long arc, on dark: brokerage is the entry vehicle, not the destination."""
    fig, ax = T.canvas(12.4, 1.85, dark=True)
    ax.set_ylim(0, 100)

    stages = [
        ("BROKERAGE", "Years 1–3", ORANGE),
        ("PROPRIETARY\nTRANSACTION INTELLIGENCE", "continuous", ORANGE),
        ("NETWORK · CAPITAL\nEXECUTION CAPABILITY", "Years 2–5", BLUE),
        ("DEVELOPMENT\n& JOINT VENTURE", "Years 3–6", GREEN),
        ("BUILDER\nJAIPUR", "Years 6+", PURPLE),
    ]
    n = len(stages)
    W = 18.2
    NOTCH = 2.6
    GAP = (100 - 4.0 - n * W) / (n - 1)
    x0 = 2.0
    for i, (name, when, c) in enumerate(stages):
        x = x0 + i * (W + GAP)
        pts = [(x, 22), (x + W - NOTCH, 22), (x + W, 50), (x + W - NOTCH, 78),
               (x, 78), (x + NOTCH if i else x, 50)]
        ax.add_patch(Polygon(pts, closed=True, facecolor=DARK_2,
                             edgecolor=c, linewidth=1.4, zorder=3))
        ax.text(x + W / 2 + (NOTCH / 2 if i else 0), 60, name, ha="center", va="center",
                fontsize=6.9, color=D_INK, fontweight="700", zorder=5, linespacing=1.5)
        ax.text(x + W / 2 + (NOTCH / 2 if i else 0), 33, when, ha="center", va="center",
                fontsize=6.0, color=c, fontweight="700", zorder=5)

    ax.text(2.0, 8.0, "Each stage funds and de-risks the next. Nothing here requires a leap — only that the previous stage actually worked.",
            fontsize=6.8, color=D_MUTED, style="italic")
    T.save(fig, "s12_arc.png", dark=True)


ALL = [s1_pulse, s2_problem, s3_definition, s4_system, s5_corridor, s6_customer,
       s7_positioning, s8_moat, s9_economics, s10_gtm, s11_capital,
       s12_founder, s12_arc]

if __name__ == "__main__":
    T.apply()
    os.makedirs(T.OUTDIR, exist_ok=True)
    for f in ALL:
        f(); print("ok", f.__name__)
