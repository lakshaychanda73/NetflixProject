"""fig_deck.py — the charts and diagrams for the 12-slide deck."""

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


# ============================================================ S1 · registrations
def s1_registrations():
    """Dark mini-chart: the monthly transaction heartbeat."""
    m = E.MONTHLY_REGISTRATIONS
    months = [x[0] for x in m]
    regs = [x[1] for x in m]

    fig = plt.figure(figsize=(7.4, 3.15))
    fig.patch.set_facecolor(DARK)
    ax = fig.add_axes([0.045, 0.165, 0.94, 0.66])
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
    fig.text(0.045, 0.905, "MUMBAI PROPERTY REGISTRATIONS PER MONTH · 2026", fontsize=8.0,
             color=D_MUTED, fontweight="700")
    fig.text(0.045, 0.035, "Source: Knight Frank / IGR monthly releases. Jan–May apportioned to the published H1 total.",
             fontsize=6.4, color=D_MUTED)
    T.save(fig, "s1_registrations.png", dark=True)


# ============================================================ S2 · Sheesham growth
def s2_sheesham():
    """Lakshay's own revenue: the single most persuasive object in the deck."""
    fig = plt.figure(figsize=(6.5, 3.5))
    ax = fig.add_axes([0.085, 0.155, 0.885, 0.66])

    q25 = F.SHEESHAM_QUARTERS["FY 2024-25"]
    q26 = F.SHEESHAM_QUARTERS["FY 2025-26"]
    xs = list(range(4)) + [x + 5 for x in range(4)]
    vals = q25 + q26
    cols = ["#D8D5CC"] * 4 + [ORANGE] * 4
    for x, v, c in zip(xs, vals, cols):
        T.bar(ax, x - 0.36, 0, 0.72, v, c, r=0.9)
        ax.text(x, v + 1.0, f"₹{v}L", ha="center", fontsize=7.8,
                color=INK if c == ORANGE else MUTED, fontweight="700" if c == ORANGE else "500")

    ax.set_xticks([1.5, 6.5])
    ax.set_xticklabels(["FY 2024-25   ·   ₹51.8 L", "FY 2025-26   ·   ₹1.08 Cr"],
                       fontsize=8.6, fontweight="600")
    ax.set_ylim(0, 39); ax.set_xlim(-0.9, 8.9)
    ax.set_yticks([0, 10, 20, 30])
    ax.set_yticklabels(["0", "₹10L", "₹20L", "₹30L"], fontsize=7.4)
    T.clean(ax)
    for lab, i in zip(ax.get_xticklabels(), [0, 1]):
        lab.set_color(MUTED if i == 0 else INK)

    ax.annotate("", xy=(4.25, 34.5), xytext=(4.25, 6),
                arrowprops=dict(arrowstyle="-", color=HAIR, lw=1.2))
    ax.text(4.25, 36.4, "+108%", ha="center", fontsize=10.5, color=GOOD, fontweight="700")
    ax.text(4.25, 33.2, "YoY", ha="center", fontsize=6.8, color=MUTED)

    fig.text(0.085, 0.90, "SHEESHAM.IN — QUARTERLY SALES, 100% BOOTSTRAPPED", fontsize=7.6,
             color=INK, fontweight="700")
    fig.text(0.085, 0.035, "Source: Sheesham.in incubation deck, July 2026. Vaishali Nagar showroom, Jaipur.",
             fontsize=6.2, color=MUTED)
    T.save(fig, "s2_sheesham.png")


# ============================================================ S3 · vision arc
def s3_vision():
    """The three-stage journey, on dark."""
    fig, ax = T.canvas(12.6, 4.9, dark=True)

    stages = F.STAGES
    W, GAP = 30.0, 3.5
    x0 = 3.0
    for i, (num, name, sub, when, thesis, gains) in enumerate(stages):
        x = x0 + i * (W + GAP)
        c = [ORANGE, BLUE, GREEN][i]
        T.card(ax, x, 10, W, 82, fc=DARK_2, ec=D_HAIR, lw=1.0)
        ax.add_patch(Rectangle((x, 10), W, 0.9, facecolor=c, edgecolor="none", zorder=3))

        ax.text(x + 2.6, 85.0, num, fontsize=26, color=c, fontweight="700",
                va="center", alpha=0.85, zorder=4)
        ax.text(x + 10.0, 86.8, name, fontsize=12.2, color=D_INK, fontweight="700",
                va="center", zorder=4)
        ax.text(x + 10.0, 82.2, sub, fontsize=8.2, color=D_INK2, va="center", zorder=4)
        T.chip(ax, x + W - 8.6, 85.0, when, fc=c, size=6.2, z=6)

        ax.plot([x + 2.6, x + W - 2.6], [77.5, 77.5], color=D_HAIR, lw=1.0, zorder=4)
        ax.text(x + 2.6, 72.5, T.wrap(thesis, 44), fontsize=7.4, color=D_INK2,
                va="top", linespacing=1.65, zorder=4)

        ax.text(x + 2.6, 55.5, "WHAT COMPOUNDS", fontsize=6.4, color=c,
                fontweight="700", va="center", zorder=4)
        yy = 50.0
        for g in gains[:4]:
            w = T.wrap(g, 38)
            ax.plot([x + 3.0], [yy - 0.9], marker="o", ms=2.4, color=c, zorder=5)
            ax.text(x + 5.0, yy, w, fontsize=6.9, color=D_INK2,
                    va="top", linespacing=1.55, zorder=4)
            yy -= 3.9 * (1 + w.count("\n")) + 1.8

        if i < 2:
            T.arrow(ax, (x + W + 0.5, 50), (x + W + GAP - 0.5, 50),
                    color=D_MUTED, lw=1.6, ms=9, z=5)

    ax.text(50, 6.2,
            "Each stage funds and de-risks the next. Nothing here requires a leap — only that the previous stage actually worked.",
            ha="center", fontsize=8.0, color=D_MUTED, style="italic")
    T.save(fig, "s3_vision.png", dark=True)


# ============================================================ S4 · opportunity funnel
def s4_funnel():
    """80,221 city registrations narrowing to a reachable number."""
    fig, ax = T.canvas(12.4, 5.0)

    stages = [
        ("80,221", "registrations in H1 2026", "Mumbai city — the whole base", 74, "#C9CCD1"),
        ("≈ 7,200", "in one corridor", "Eastern & Central's share of city transactions", 56, BLUE_L),
        ("≈ 1,100", "in our pocket set", "the 20–30 pockets we actually work", 40, BLUE),
        ("≈ 600", "broker-intermediated", "the rest are direct or developer walk-in", 27, ORANGE_L),
        ("15", "closures we need", "≈2.5% of the reachable pool", 16, ORANGE),
    ]
    top, band, gap = 92.0, 11.5, 5.4
    for i, (val, unit, note, w, c) in enumerate(stages):
        y = top - i * (band + gap)
        x0 = 42 - w / 2
        T.card(ax, x0, y - band, w, band, fc=c, ec="none", r=1.0)
        ax.text(42, y - band / 2 + 1.4, val, ha="center", va="center",
                fontsize=15 if i else 13, color="white" if i > 0 else INK, fontweight="700")
        ax.text(42, y - band / 2 - 3.4, unit, ha="center", va="center",
                fontsize=7.4, color="white" if i > 0 else INK2)
        ax.text(x0 + w + 3.0, y - band / 2, note, ha="left", va="center",
                fontsize=8.0, color=INK2)
        if i < len(stages) - 1:
            nw = stages[i + 1][3]
            ax.add_patch(Polygon([[x0, y - band], [x0 + w, y - band],
                                  [42 + nw / 2, y - band - gap], [42 - nw / 2, y - band - gap]],
                                 closed=True, facecolor=c, edgecolor="none",
                                 alpha=0.20, zorder=1))

    ax.text(2, 8.0, "We do not need the market to grow. We need 15 transactions out of 80,000.",
            fontsize=9.6, color=INK, fontweight="600")
    ax.text(2, 3.4,
            "Corridor share, pocket share and intermediation rate are analyst estimates — the 90-day pilot exists to replace them with measurements.",
            fontsize=6.8, color=MUTED)
    T.save(fig, "s4_funnel.png")


# ============================================================ S5 · MMR map
def s5_map():
    """Corridor map with entry sequence."""
    fig, ax = T.canvas(8.4, 5.6)
    ax.set_ylim(0, 74)

    ax.add_patch(Polygon([[0, 0], [11, 0], [9, 22], [7, 40], [4, 56], [1.5, 74], [0, 74]],
                         closed=True, facecolor="#EDF1F6", edgecolor="none", zorder=0))
    ax.text(4.6, 34, "Arabian\nSea", fontsize=7.4, color="#A9BACD", ha="center",
            style="italic", linespacing=1.4, zorder=1)
    ax.add_patch(Polygon([[58, 3], [68, 2], [67, 14], [61, 16], [57, 9]],
                         closed=True, facecolor="#EDF1F6", edgecolor="none", zorder=0))

    corridors = [
        ("SOUTH MUMBAI",  "Colaba · Fort · Worli",             15, 2,   22, 11,  "#B9BDC4", "6"),
        ("WESTERN",       "Bandra · Andheri · Borivali",       12, 32,  22, 36,  PURPLE,    "4"),
        ("EASTERN & CENTRAL", "Powai · Kanjurmarg · Vikhroli\nBhandup · Mulund · Ghatkopar",
                                                               38, 28,  26, 25,  ORANGE,    "1"),
        ("HARBOUR",       "Wadala · Chembur · Sewri",          33, 15,  25, 10,  "#B9BDC4", "5"),
        ("THANE",         "Ghodbunder · Pokhran · Kolshet",    39, 58,  25, 12,  BLUE,      "2"),
        ("NAVI MUMBAI",   "Airoli · Vashi\nKharghar · Panvel", 70, 16,  23, 38,  GREEN,     "3"),
    ]
    for name, subs, x, y, w, h, c, phase in corridors:
        prim = phase == "1"
        if not prim:
            T.card(ax, x, y, w, h, fc=c, ec=c, lw=1.2, alpha=0.10, r=1.2)
            T.card(ax, x, y, w, h, fc="none", ec=c, lw=1.2, r=1.2)
        else:
            T.card(ax, x, y, w, h, fc=c, ec=c, lw=2.0, r=1.2)
        tc = "white" if prim else INK
        ax.text(x + w / 2, y + h - 3.2, name, ha="center", va="top", fontsize=7.8,
                color=tc, fontweight="700", zorder=5)
        ax.text(x + w / 2, y + h - 7.4, subs, ha="center", va="top", fontsize=6.4,
                color="white" if prim else INK2, zorder=5, linespacing=1.5)
        ax.scatter([x + 2.8], [y + 2.6], s=180, marker="o",
                   facecolor="white" if prim else c, edgecolor=c, linewidth=1.3, zorder=6)
        ax.text(x + 2.8, y + 2.6, phase, ha="center", va="center", fontsize=6.8,
                fontweight="700", color=c if prim else "white", zorder=7)

    for p0, p1 in [((50, 53), (50, 58)), ((64, 40), (70, 38)),
                   ((38, 42), (34, 44)), ((48, 28), (48, 25.4)), ((33, 18), (29, 15))]:
        T.arrow(ax, p0, p1, color=MUTED, lw=1.4, ms=8, z=4)

    T.save(fig, "s5_map.png")


# ============================================================ S6 · seven metrics
def s6_metrics():
    """Radial seven-metric framework — the DreamSleep pattern."""
    fig, ax = T.canvas(7.6, 5.6)
    ax.set_ylim(0, 74)
    cx, cy, R = 50, 37, 25.5

    labels = [
        ("Transaction\ndepth", "0.20", "Registered volume the\ncorridor actually produces"),
        ("Infrastructure\ncatalyst", "0.16", "Weighted by what is\noperating, not announced"),
        ("Entry cost\n(inverse)", "0.14", "Lower ticket, faster\nfirst closure"),
        ("Execution\nsimplicity", "0.14", "Travel time, site access,\nbroker reachability"),
        ("Data\naccessibility", "0.12", "RERA and IGR coverage\nat pocket level"),
        ("Rental\ndepth", "0.12", "Second revenue line\nand lead nursery"),
        ("Competitive\nwhitespace", "0.12", "Advisory-grade rivals\nper pocket"),
    ]
    n = len(labels)
    ang0 = np.pi / 2
    pts = []
    for i in range(n):
        a = ang0 - i * 2 * np.pi / n
        pts.append((cx + R * np.cos(a) * 1.02, cy + R * np.sin(a) * 0.86))

    ax.add_patch(Polygon(pts, closed=True, facecolor="none", edgecolor=HAIR,
                         lw=1.1, zorder=1, linestyle=(0, (4, 4))))

    ax.add_patch(Circle((cx, cy), 11.2, facecolor=ORANGE, edgecolor="none", zorder=4,
                        transform=ax.transData))
    ax.text(cx, cy + 3.2, "7", ha="center", va="center", fontsize=20,
            color="white", fontweight="700", zorder=5)
    ax.text(cx, cy - 2.6, "WEIGHTED\nMETRICS", ha="center", va="center", fontsize=6.6,
            color="white", fontweight="700", zorder=5, linespacing=1.5)

    for i, ((lab, wt, note), (px, py)) in enumerate(zip(labels, pts)):
        c = SERIES[i % 4]
        ax.plot([cx, px], [cy, py], color=HAIR, lw=1.0, zorder=2)
        ax.scatter([px], [py], s=520, facecolor=CARD, edgecolor=c, linewidth=1.6, zorder=5)
        ax.text(px, py + 0.4, wt, ha="center", va="center", fontsize=7.6,
                color=c, fontweight="700", zorder=6)
        # label placed outward
        dx, dy = px - cx, py - cy
        norm = max((dx ** 2 + dy ** 2) ** 0.5, 1e-6)
        lx, ly = px + dx / norm * 9.5, py + dy / norm * 7.0
        ha = "center"
        if lx < cx - 6: ha = "right"; lx = px - 6.0
        elif lx > cx + 6: ha = "left"; lx = px + 6.0
        ax.text(lx, ly + 1.2, lab, ha=ha, va="center", fontsize=7.4,
                color=INK, fontweight="700", zorder=6, linespacing=1.4)
        ax.text(lx, ly - 3.6, note, ha=ha, va="center", fontsize=6.0,
                color=MUTED, zorder=6, linespacing=1.45)

    T.save(fig, "s6_metrics.png")


# ============================================================ S7 · scorecard
def s7_scorecard():
    """Heatmap + ranked totals — why Eastern & Central wins."""
    order = [k for k, _, _, _ in E.CRITERIA]
    labels = [l for _, l, _, _ in E.CRITERIA]
    weights = {k: w for k, _, w, _ in E.CRITERIA}
    ranked = E.ranked_regions()
    regions = [r for r, _ in ranked]
    M = np.array([[E.REGION_SCORES[r][k] for k in order] for r in regions], float)

    fig = plt.figure(figsize=(12.4, 4.5))
    ax = fig.add_axes([0.155, 0.175, 0.545, 0.70])
    im = ax.imshow(M, cmap=SEQ_ORANGE, vmin=1, vmax=10, aspect="auto")
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            v = int(M[i, j])
            ax.text(j, i, str(v), ha="center", va="center", fontsize=9.6,
                    color="white" if v >= 7 else INK, fontweight="700")
    ax.set_xticks(range(len(labels)))
    nice = ["Transaction\ndepth", "Infrastructure\ncatalyst", "Entry cost\n(inverse)",
            "Data\naccessibility", "Rental\ndepth", "Competitive\nwhitespace",
            "Execution\nsimplicity"]
    ax.set_xticklabels(nice, fontsize=7.4, linespacing=1.4)
    ax.set_yticks(range(len(regions)))
    ax.set_yticklabels([f"{i+1}.  {r}" for i, r in enumerate(regions)], fontsize=8.6)
    for i, lab in enumerate(ax.get_yticklabels()):
        lab.set_color(INK if i == 0 else INK2)
        lab.set_fontweight("700" if i == 0 else "400")
    ax.tick_params(length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xticks(np.arange(-0.5, len(labels), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(regions), 1), minor=True)
    ax.grid(which="minor", color=LIGHT, linewidth=2.6)
    ax.tick_params(which="minor", length=0)
    ax.xaxis.set_ticks_position("top")

    # weight strip
    axw = fig.add_axes([0.155, 0.088, 0.545, 0.045]); T.blank(axw)
    axw.set_xlim(-0.5, len(labels) - 0.5); axw.set_ylim(0, 1)
    for j, k in enumerate(order):
        axw.text(j, 0.55, f"{weights[k]:.2f}", ha="center", fontsize=6.8,
                 color=MUTED, fontweight="600")
    axw.text(-0.62, 0.55, "weight", ha="right", fontsize=6.6, color=MUTED)

    # ranked totals
    ax2 = fig.add_axes([0.755, 0.175, 0.215, 0.70])
    for i, (r, sc) in enumerate(ranked):
        c = ORANGE if i == 0 else "#C9CCD1"
        T.bar(ax2, 0, i - 0.30, sc, 0.60, c, r=0.22)
        ax2.text(sc + 0.18, i, f"{sc:.2f}", va="center", fontsize=9.2,
                 color=INK, fontweight="700" if i == 0 else "500")
    ax2.set_yticks([]); ax2.set_ylim(len(ranked) - 0.45, -0.55)
    ax2.set_xlim(0, 9.9); ax2.set_xticks([0, 5, 10])
    ax2.set_xticklabels(["0", "5", "10"], fontsize=7)
    T.clean(ax2, ygrid=False, xgrid=True)
    ax2.set_title("WEIGHTED SCORE", fontsize=7.2, color=INK, loc="left",
                  pad=9, fontweight="700")

    fig.text(0.012, 0.028,
             "Analyst model. Scores are 1–10 judgements against the evidence base; weights encode one strategy — a single founder needing a first closure inside two quarters.",
             fontsize=6.4, color=MUTED)
    T.save(fig, "s7_scorecard.png")


# ============================================================ S8 · operating model
def s8_operating():
    """The transaction engine, as a loop."""
    fig, ax = T.canvas(12.4, 4.4)
    ax.set_ylim(0, 58)

    steps = [
        ("01", "ACQUIRE", "Referrals · briefs\nco-broking · content", ORANGE),
        ("02", "QUALIFY", "Budget · timeline\nauthority · area fit", ORANGE),
        ("03", "SHORTLIST", "Hard filters, then\nweighted scoring", BLUE),
        ("04", "SITE VISIT", "Accompanied, batched\nby pocket", BLUE),
        ("05", "NEGOTIATE", "Registered comparables\nnot opinions", GREEN),
        ("06", "TRANSACT", "Diligence · loan\nregistration", GREEN),
        ("07", "CAPTURE", "Closed price · objections\nreferral ask", PURPLE),
    ]
    W, GAP = 12.6, 1.4
    x0 = 2.2
    for i, (num, name, sub, c) in enumerate(steps):
        x = x0 + i * (W + GAP)
        T.card(ax, x, 24, W, 24, fc=CARD, ec=HAIR)
        ax.add_patch(Rectangle((x, 44.8), W, 3.2, facecolor=c, edgecolor="none", zorder=3))
        ax.text(x + 1.7, 46.4, num, fontsize=6.6, color="white", fontweight="700",
                va="center", zorder=4)
        ax.text(x + W / 2 + 1.3, 46.4, name, ha="center", va="center", fontsize=7.0,
                color="white", fontweight="700", zorder=4)
        ax.text(x + W / 2, 35.0, T.wrap(sub.replace("\n", " "), 17), ha="center",
                va="center", fontsize=6.5, color=INK2, zorder=4, linespacing=1.7)
        if i < len(steps) - 1:
            T.arrow(ax, (x + W + 0.1, 36), (x + W + GAP - 0.1, 36),
                    color=RULE, lw=1.2, ms=7, z=4)

    # feedback loop
    xr = x0 + 6 * (W + GAP) + W / 2
    xl = x0 + W / 2
    ax.plot([xr, xr], [24, 16], color=PURPLE, lw=1.7, zorder=2)
    ax.plot([xl, xr], [16, 16], color=PURPLE, lw=1.7, zorder=2)
    T.arrow(ax, (xl, 16), (xl, 23.4), color=PURPLE, lw=1.7, ms=9, z=3)
    ax.text(50, 9.0, "Every closure re-enters at step 1 as proprietary evidence — closed prices, objections, society rules, true commute.",
            ha="center", fontsize=8.0, color=INK2)
    ax.text(50, 4.2, "This is the compounding loop. It costs nothing to build and it is the only asset a better-funded competitor cannot simply buy.",
            ha="center", fontsize=7.4, color=MUTED, style="italic")
    T.save(fig, "s8_operating.png")


# ============================================================ S9 · economics
def s9_economics():
    """Hours -> transactions -> revenue, then the three scenarios."""
    fig = plt.figure(figsize=(12.4, 4.4))

    # --- chain
    ax = fig.add_axes([0.012, 0.10, 0.545, 0.80]); T.blank(ax)
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    chain = [
        ("2,860", "founder hours", "55 h/week × 52 weeks", "#C9CCD1"),
        ("15", "closures", "at the base-case funnel", BLUE),
        ("₹2.30 cr", "avg consideration", "blended across the mix", BLUE),
        ("1.33%", "blended commission", "resale, primary and rental", ORANGE),
        ("₹45.7 L", "gross commission", "before cost and tax", ORANGE),
    ]
    bw, gp = 16.0, 2.6
    for i, (v, lab, sub, c) in enumerate(chain):
        x = 1.0 + i * (bw + gp)
        T.card(ax, x, 32, bw, 44, fc=CARD, ec=HAIR)
        ax.add_patch(Rectangle((x, 32), bw, 1.0, facecolor=c, edgecolor="none", zorder=3))
        ax.text(x + bw / 2, 66, v, ha="center", va="center", fontsize=13.5,
                color=INK, fontweight="700", zorder=4)
        ax.text(x + bw / 2, 54, lab, ha="center", va="center", fontsize=7.6,
                color=INK2, fontweight="600", zorder=4)
        ax.text(x + bw / 2, 43, T.wrap(sub, 20), ha="center", va="center", fontsize=6.4,
                color=MUTED, zorder=4, linespacing=1.5)
        if i < len(chain) - 1:
            ops = ["\u2192", "\u00d7", "\u00d7", "="]
            ax.text(x + bw + gp / 2, 54, ops[i], ha="center", va="center",
                    fontsize=11, color=MUTED, fontweight="600", zorder=4)
    ax.text(1.0, 22, "₹32.6 L", fontsize=17, color=INK, fontweight="700", va="center")
    ax.text(19.5, 24.5, "post-tax to founder in Year 1", fontsize=8.2, color=INK2, va="center")
    ax.text(19.5, 19.0, "≈ ₹1,140 per founder hour — the honest comparator to a salary",
            fontsize=7.0, color=MUTED, va="center")
    ax.text(1.0, 8.0, "Costs: ₹4.2 L operating + ₹0.5 L one-off setup. GST is an output tax; 2% TDS under 194H is creditable.",
            fontsize=6.4, color=MUTED)

    # --- scenarios
    ax2 = fig.add_axes([0.635, 0.20, 0.335, 0.595])
    scen = [("Conservative", 7, 21.3, 15.3), ("Base", 15, 45.7, 32.6),
            ("Stretch", 27, 82.3, 57.8)]
    idx = np.arange(3); wid = 0.30
    for i, (name, n, gross, post) in enumerate(scen):
        T.bar(ax2, i - wid - 0.02, 0, wid, gross, ORANGE, r=0.14)
        T.bar(ax2, i + 0.02, 0, wid, post, "#9BA3B0", r=0.14)
        ax2.text(i - wid / 2 - 0.02, gross + 2.6, f"{gross:.0f}", ha="center",
                 fontsize=8.0, color=INK, fontweight="700")
        ax2.text(i + wid / 2 + 0.02, post + 2.6, f"{post:.0f}", ha="center",
                 fontsize=8.0, color=INK2, fontweight="600")
    ax2.set_xticks(idx)
    ax2.set_xticklabels([f"{s_[0]}\n{s_[1]} closures" for s_ in scen],
                        fontsize=8.0, linespacing=1.7)
    ax2.tick_params(axis="x", pad=7)
    ax2.set_ylim(0, 97); ax2.set_yticks([0, 25, 50, 75])
    ax2.set_yticklabels(["0", "25", "50", "75"], fontsize=7)
    ax2.set_xlim(-0.62, 2.62)
    T.clean(ax2)
    ax2.plot([], [], "s", color=ORANGE, ms=7, label="gross commission")
    ax2.plot([], [], "s", color="#9BA3B0", ms=7, label="post-tax to founder")
    ax2.legend(loc="upper left", fontsize=7.0, handletextpad=0.5, borderpad=0.2)
    ax2.set_title("YEAR-1 OUTCOME BY SCENARIO  \u00b7  \u20b9 lakh", fontsize=7.4,
                  color=INK, loc="left", pad=9, fontweight="700")

    T.save(fig, "s9_economics.png")


# ============================================================ S10 · 90 days
def s10_90days():
    """Twelve weeks, four phases, one hard gate."""
    fig, ax = T.canvas(12.4, 4.0)
    ax.set_ylim(0, 52)

    phases = [
        ("WEEKS 1–2", "Become legal", ORANGE,
         ["MahaRERA agent registration filed",
          "20-hour Certificate of Competency booked",
          "Entity, PAN/TAN, GST, CA engaged"]),
        ("WEEKS 2–4", "Lock the corridor", BLUE,
         ["5 localities, 20–30 pockets, frozen",
          "MahaRERA project register built",
          "IGR registered-price baseline"]),
        ("WEEKS 4–6", "Build the edge", BLUE,
         ["Site visits and broker network",
          "Society rules, maintenance, commute",
          "Pocket scorecards live"]),
        ("WEEKS 6–12", "Sell", GREEN,
         ["Certificate issued — marketing opens",
          "30+ qualified leads, source-tagged",
          "First site visits and offers"]),
    ]
    W, GAP = 22.6, 2.6
    for i, (when, title, c, items) in enumerate(phases):
        x = 2.0 + i * (W + GAP)
        T.card(ax, x, 6, W, 40, fc=CARD, ec=HAIR)
        ax.add_patch(Rectangle((x, 42.6), W, 3.4, facecolor=c, edgecolor="none", zorder=3))
        ax.text(x + 2.2, 44.3, when, fontsize=6.8, color="white", fontweight="700",
                va="center", zorder=4)
        ax.text(x + 2.2, 36.6, title, fontsize=11, color=INK, fontweight="700", va="center", zorder=4)
        yy = 31.0
        for it in items:
            w = T.wrap(it, 27)
            ax.plot([x + 2.9], [yy - 0.9], marker="o", ms=2.4, color=c, zorder=5)
            ax.text(x + 4.6, yy, w, fontsize=7.1, color=INK2,
                    va="top", linespacing=1.55, zorder=4)
            yy -= 4.6 * (1 + w.count("\n")) + 2.0
        if i < 2:
            T.arrow(ax, (x + W + 0.3, 26), (x + W + GAP - 0.3, 26), color=RULE,
                    lw=1.3, ms=8, z=4)

    gx = 2.0 + 3 * (W + GAP) - GAP / 2
    ax.plot([gx, gx], [3.5, 49], color=BAD, lw=1.4, ls=(0, (4, 3)), zorder=6)
    ax.text(gx, 50.6, "COMPLIANCE GATE  ·  no advertising, listing or client work before this line",
            ha="center", fontsize=6.9, color=BAD, fontweight="700")
    T.save(fig, "s10_90days.png")


# ============================================================ S11 · scale
def s11_scale():
    """Month 3 -> 6 -> 12, with the revenue ramp underneath."""
    fig = plt.figure(figsize=(12.4, 4.6))

    ax = fig.add_axes([0.012, 0.42, 0.976, 0.53]); T.blank(ax)
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    miles = [
        ("MONTH 3", "Proof", ORANGE,
         ["Corridor mapped to pocket level", "30+ qualified leads", "First closure or evidenced pipeline"]),
        ("MONTH 6", "Repeatable", BLUE,
         ["Deal engine runs without improvisation", "Rental desk covers fixed costs",
          "Referral coefficient measured"]),
        ("MONTH 12", "Compounding", GREEN,
         ["15 closures · ₹45.7 L gross commission", "Corridor 2 opened on evidence",
          "Proprietary dataset no rival holds"]),
    ]
    W, GAP = 29.6, 3.6
    for i, (when, title, c, items) in enumerate(miles):
        x = 2.0 + i * (W + GAP)
        T.card(ax, x, 6, W, 84, fc=CARD, ec=HAIR)
        ax.add_patch(Rectangle((x, 86.0), W, 4.0, facecolor=c, edgecolor="none", zorder=3))
        ax.text(x + 2.6, 88.0, when, fontsize=7.4, color="white", fontweight="700",
                va="center", zorder=4)
        ax.text(x + 2.6, 74, title, fontsize=13, color=INK, fontweight="700", va="center", zorder=4)
        yy = 60
        for it in items:
            ax.plot([x + 3.3], [yy + 0.6], marker="o", ms=2.8, color=c, zorder=5)
            ax.text(x + 5.4, yy, T.wrap(it, 34), fontsize=7.6, color=INK2,
                    va="top", linespacing=1.6, zorder=4)
            yy -= 13.0 * (1 + T.wrap(it, 34).count("\n"))
        if i < 2:
            T.arrow(ax, (x + W + 0.4, 48), (x + W + GAP - 0.4, 48), color=RULE,
                    lw=1.4, ms=9, z=4)

    ax2 = fig.add_axes([0.055, 0.12, 0.90, 0.24])
    months = np.arange(1, 13)
    closures = np.array([0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3])
    cum = np.cumsum(closures)
    ax2.fill_between(months, cum, color=ORANGE, alpha=0.16, zorder=2)
    ax2.plot(months, cum, color=ORANGE, lw=2.4, zorder=3)
    ax2.scatter(months, cum, s=22, color=ORANGE, zorder=4, edgecolor=LIGHT, linewidth=1.2)
    for m in (3, 6, 12):
        ax2.axvline(m, color=HAIR, lw=1.0, zorder=1)
    ax2.text(12, cum[-1] + 1.1, "15 closures", ha="right", fontsize=8, color=INK,
             fontweight="700")
    ax2.set_xlim(1, 12.4); ax2.set_ylim(0, 19)
    ax2.set_xticks([1, 3, 6, 9, 12])
    ax2.set_xticklabels(["M1", "M3", "M6", "M9", "M12"], fontsize=7.4)
    ax2.set_yticks([0, 5, 10, 15]); ax2.set_yticklabels(["0", "5", "10", "15"], fontsize=7)
    T.clean(ax2)
    ax2.set_title("CUMULATIVE CLOSURES — BASE CASE", fontsize=7.2, color=INK,
                  loc="left", pad=8, fontweight="700")
    T.save(fig, "s11_scale.png")


# ============================================================ S12 · end game
def s12_endgame():
    """The compounding staircase, on dark."""
    fig, ax = T.canvas(12.4, 4.9, dark=True)

    steps = [
        ("MUMBAI", "Advisory & brokerage", "Years 1–3", ORANGE, 4, 16,
         "₹45 L", "gross commission in Year 1"),
        ("DEVELOPMENT", "Partnerships, then own projects", "Years 3–6", BLUE, 36, 27,
         "₹5–15 Cr", "project value per scheme"),
        ("JAIPUR", "Build at scale, at home", "Years 6+", GREEN, 68, 38,
         "24 years", "of family ecosystem to build on"),
    ]
    H = 44
    for i, (name, sub, when, c, x, y, val, vlab) in enumerate(steps):
        w = 28
        T.card(ax, x, y, w, H, fc=DARK_2, ec=D_HAIR)
        ax.add_patch(Rectangle((x, y), w, 0.9, facecolor=c, edgecolor="none", zorder=3))
        ax.text(x + 2.8, y + H - 7.0, name, fontsize=13, color=D_INK,
                fontweight="700", va="center", zorder=4)
        ax.text(x + 2.8, y + H - 12.6, T.wrap(sub, 30), fontsize=7.8, color=D_INK2,
                va="center", zorder=4, linespacing=1.5)
        T.chip(ax, x + 2.8, y + H - 19.6, when, fc=c, size=6.2, z=6)
        ax.plot([x + 2.8, x + w - 2.8], [y + H - 25.0, y + H - 25.0],
                color=D_HAIR, lw=1.0, zorder=4)
        ax.text(x + 2.8, y + H - 32.0, val, fontsize=16, color=c, fontweight="700",
                va="center", zorder=4)
        ax.text(x + 2.8, y + H - 37.4, T.wrap(vlab, 26), fontsize=6.8, color=D_MUTED,
                va="center", zorder=4, linespacing=1.5)
        if i < 2:
            T.arrow(ax, (x + w + 0.8, y + H - 6),
                    (steps[i + 1][4] - 0.8, steps[i + 1][5] + H - 6),
                    color=D_MUTED, lw=1.6, ms=9, z=5)

    ax.text(2, 8.2, "Brokerage is the entry vehicle, not the destination.",
            fontsize=11, color=D_INK, fontweight="600")
    ax.text(2, 3.4,
            "Each stage funds the next and de-risks it. The capability compounds; the market changes; the family ecosystem waits.",
            fontsize=7.8, color=D_MUTED)
    T.save(fig, "s12_endgame.png", dark=True)


ALL = [s1_registrations, s2_sheesham, s3_vision, s4_funnel, s5_map, s6_metrics,
       s7_scorecard, s8_operating, s9_economics, s10_90days, s11_scale, s12_endgame]

if __name__ == "__main__":
    T.apply()
    os.makedirs(T.OUTDIR, exist_ok=True)
    for f in ALL:
        f(); print("ok", f.__name__)
