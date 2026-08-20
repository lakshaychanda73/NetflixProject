"""fig_market.py — Part A: market evidence figures."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Polygon, Rectangle
import theme as T
from theme import (SURFACE, INK, INK2, MUTED, GRID, BASELINE, BLUE, ORANGE, AQUA,
                   YELLOW, MAGENTA, GREEN, VIOLET, RED, GOOD, WARN, SERIOUS, CRITICAL,
                   SEQ_BLUE, SEQ_BLUE_ORD, BLUE_RAMP)
import evidence as E

OUT = "../figures/"


# ---------------------------------------------------------------- A1 -------
def fig_market_scale():
    """Stat tiles + the demand/supply/overhang relationship. Headline numbers."""
    fig = plt.figure(figsize=(11.2, 5.5))
    T.titleblock(fig, "Mumbai residential market at a glance — H1 2026",
                 "Demand is stable and record-deep by registration count; supply is running slightly ahead of it; "
                 "the unsold pool is the largest in India.\nThat combination is why selection and negotiability, not price forecasting, is the sellable skill.")

    tiles = [
        ("47,355", "units sold H1 2026", "+1% YoY", GOOD, BLUE),
        ("49,161", "units launched H1 2026", "+8% YoY", WARN, ORANGE),
        ("1,57,410", "unsold units", "largest pool in India", CRITICAL, RED),
        ("80,221", "BMC registrations H1", "+6% YoY · best since 2013", GOOD, AQUA),
        ("₹6,968 cr", "stamp duty H1 2026", "state exchequer", GOOD, VIOLET),
        ("₹36,881", "average price / sq ft", "India's costliest market", MUTED, INK2),
    ]
    ax = fig.add_axes([0.012, 0.50, 0.976, 0.26]); T.blank(ax)
    ax.set_xlim(0, 6); ax.set_ylim(0, 1)
    for i, (val, lab, delta, dcol, accent) in enumerate(tiles):
        ax.add_patch(FancyBboxPatch((i + 0.02, 0.03), 0.96, 0.94,
                                    boxstyle="round,pad=0,rounding_size=0.05",
                                    fc=SURFACE, ec=BASELINE, lw=1.0))
        ax.add_patch(Rectangle((i + 0.02, 0.03), 0.035, 0.94, fc=accent, ec="none"))
        ax.text(i + 0.13, 0.72, val, fontsize=17, fontweight="600", color=INK, va="center")
        ax.text(i + 0.13, 0.44, lab, fontsize=8.2, color=INK2, va="center")
        ax.text(i + 0.13, 0.21, delta, fontsize=7.6, color=dcol if dcol != MUTED else MUTED,
                va="center", fontweight="600" if dcol != MUTED else "400")

    # Absorption gap bar
    ax2 = fig.add_axes([0.065, 0.185, 0.38, 0.245]); T.clean(ax2, ygrid=False, xgrid=True)
    labels = ["Sold", "Launched", "Unsold pool"]
    vals = [47355, 49161, 157410]
    cols = [BLUE, ORANGE, RED]
    for i, (v, c) in enumerate(zip(vals, cols)):
        T.rbar(ax2, 0, i - 0.30, v, 0.60, c, r=900)
        ax2.text(v + 3000, i, f"{T.inr(v)}", va="center", fontsize=8.6, color=INK, fontweight="600")
    ax2.set_yticks(range(3)); ax2.set_yticklabels(labels, fontsize=8.8)
    ax2.set_xlim(0, 205000); ax2.set_ylim(-0.65, 2.65)
    ax2.invert_yaxis()
    ax2.set_xticks([0, 50000, 100000, 150000])
    ax2.set_xticklabels(["0", "50k", "1.0 L", "1.5 L"], fontsize=8)
    ax2.set_title("H1 2026 volumes  ·  units", fontsize=9.6, color=INK, loc="left",
                  pad=7, fontweight="600")

    # Sellability gauges
    ax3 = fig.add_axes([0.55, 0.185, 0.43, 0.245]); T.blank(ax3)
    ax3.set_xlim(0, 2); ax3.set_ylim(0, 1)
    ax3.set_title("Sellability — how long the market takes to clear", fontsize=9.6, color=INK,
                  loc="left", pad=7, fontweight="600")
    for i, (v, cap, sub, mx, col) in enumerate([
            (6.5, "6.5 quarters", "quarters-to-sell at current velocity", 12, ORANGE),
            (13.5, "13.5 quarters", "age of unsold stock (was 14.3)", 20, BLUE)]):
        x0 = i * 1.0 + 0.03
        ax3.add_patch(FancyBboxPatch((x0, 0.46), 0.90, 0.15,
                                     boxstyle="round,pad=0,rounding_size=0.07",
                                     fc=GRID, ec="none"))
        ax3.add_patch(FancyBboxPatch((x0, 0.46), 0.90 * v / mx, 0.15,
                                     boxstyle="round,pad=0,rounding_size=0.07",
                                     fc=col, ec="none"))
        ax3.text(x0, 0.79, cap, fontsize=13, fontweight="600", color=INK, va="center")
        ax3.text(x0, 0.30, sub, fontsize=7.8, color=INK2, va="center")
        ax3.text(x0, 0.11, f"scale 0–{mx} quarters", fontsize=7, color=MUTED, va="center")

    T.footnote(fig, "Sources: Knight Frank India Real Estate H1 2026 [SRC-004, SRC-032]; Knight Frank / IGR registration coverage [SRC-005]. "
                    "All figures are published market statistics, not analyst estimates.\n"
                    "Average price is a city-wide weighted figure on the publisher's own area basis — it is context, never a comparable for a specific unit.")
    T.save(fig, "A1_market_at_a_glance.png")


# ---------------------------------------------------------------- A2 -------
def fig_registration_engine():
    """Monthly registrations and stamp duty — two measures, two panels. Never dual-axis."""
    m = E.MONTHLY_REGISTRATIONS
    months = [x[0] for x in m]
    regs = [x[1] for x in m]
    duty = [x[2] for x in m]
    reported = [x[3] == "reported" for x in m]

    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.3))
    fig.subplots_adjust(top=0.66, bottom=0.17, wspace=0.22, left=0.06, right=0.985)
    T.titleblock(fig, "The registration engine — Mumbai (BMC jurisdiction), calendar 2026",
                 "Roughly 13,000–14,000 registrations clear every month and each one is a dated, addressable, public transaction record.\n"
                 "This monthly cadence — not the half-yearly consultancy report — is the heartbeat a micro-market desk should run on.")

    ax = axes[0]; T.clean(ax)
    for i, (v, rep) in enumerate(zip(regs, reported)):
        T.rbar(ax, i - 0.34, 0, 0.68, v, BLUE if rep else BLUE_RAMP[3], r=0.02)
        ax.text(i, v + 400, f"{v:,}", ha="center", fontsize=7.8,
                color=INK if rep else MUTED, fontweight="600" if rep else "400")
    ax.set_xticks(range(len(months))); ax.set_xticklabels(months)
    ax.set_ylim(0, 16500); ax.set_xlim(-0.7, len(months) - 0.3)
    ax.set_ylabel("registrations", fontsize=8.4)
    ax.set_title("Property registrations per month", fontsize=10, color=INK, loc="left",
                 pad=8, fontweight="600")
    ax.plot([], [], "s", color=BLUE, ms=7, label="reported")
    ax.plot([], [], "s", color=BLUE_RAMP[3], ms=7, label="reconciled to published H1 total")
    ax.legend(loc="lower right", fontsize=7.6, handletextpad=0.5)

    ax = axes[1]; T.clean(ax)
    for i, (v, rep) in enumerate(zip(duty, reported)):
        T.rbar(ax, i - 0.34, 0, 0.68, v, AQUA if rep else "#a7e0c9", r=0.02)
        ax.text(i, v + 35, f"{v:,}", ha="center", fontsize=7.8,
                color=INK if rep else MUTED, fontweight="600" if rep else "400")
    ax.set_xticks(range(len(months))); ax.set_xticklabels(months)
    ax.set_ylim(0, 1520); ax.set_xlim(-0.7, len(months) - 0.3)
    ax.set_ylabel("₹ crore", fontsize=8.4)
    ax.set_title("Stamp duty collected per month", fontsize=10, color=INK, loc="left",
                 pad=8, fontweight="600")
    ax.annotate("July 2026: ₹1,223 cr,\n+8.9% YoY — highest\nJuly in 14 years",
                xy=(6, 1223), xytext=(3.7, 1380),
                fontsize=7.6, color=INK2, ha="left",
                arrowprops=dict(arrowstyle="-", color=BASELINE, lw=0.9,
                                connectionstyle="arc3,rad=-0.2"))

    T.footnote(fig, "Sources: H1 2026 aggregate 80,221 registrations / ₹6,968 cr [SRC-005]; June and July 2026 monthly readings [SRC-006]. "
                    "January–May are apportioned to reconcile exactly to the published H1 aggregate and are marked as reconciled, not reported —\n"
                    "replace each with the monthly Knight Frank / IGR release as it is published. Two measures on different scales are shown as two panels, never as one dual-axis chart.")
    T.save(fig, "A2_registration_engine.png")


# ---------------------------------------------------------------- A3 -------
def fig_inventory_context():
    """Where the unsold pool sits, and what the buyer is actually buying."""
    fig = plt.figure(figsize=(11.2, 4.6))
    T.titleblock(fig, "Overhang and the shape of demand",
                 "Mumbai carries 30% of the unsold stock of India's eight largest markets. At the same time the ticket mix is moving upmarket\n"
                 "while the size mix stays compact — the market is paying more per square foot for the same small flat.")

    # left: unsold by city
    ax = fig.add_axes([0.055, 0.13, 0.36, 0.55]); T.clean(ax, ygrid=False, xgrid=True)
    rows = E.UNSOLD_BY_CITY
    names = [r[0] for r in rows]; vals = [r[1] for r in rows]
    cols = [RED, BLUE_RAMP[5], BLUE_RAMP[3], GRID]
    for i, (v, c) in enumerate(zip(vals, cols)):
        T.rbar(ax, 0, i - 0.32, v, 0.64, c, r=800)
        ax.text(v + 2500, i, f"{T.inr(v)}", va="center", fontsize=8.4,
                color=INK, fontweight="600" if i == 0 else "400")
    ax.set_yticks(range(len(names))); ax.set_yticklabels(names, fontsize=8.6)
    ax.invert_yaxis(); ax.set_xlim(0, 235000)
    ax.set_xticks([0, 50000, 100000, 150000, 200000])
    ax.set_xticklabels(["0", "50k", "1.0 L", "1.5 L", "2.0 L"])
    ax.set_title("Unsold units — top-8 markets, H1 2026", fontsize=9.8, color=INK,
                 loc="left", pad=8, fontweight="600")
    ax.set_xlabel("units · top-8 total 5,25,695 (+4% YoY)", fontsize=7.8)

    # middle: ticket mix shift
    ax = fig.add_axes([0.49, 0.13, 0.20, 0.55]); T.clean(ax)
    yrs = ["H1 2025", "H1 2026"]
    above = [49, 54]
    below = [51, 46]
    for i in range(2):
        T.rbar(ax, i - 0.30, 0, 0.60, below[i], BLUE_RAMP[2], r=0.02)
        T.rbar(ax, i - 0.30, below[i] + 1.2, 0.60, above[i] - 1.2, VIOLET, r=0.02)
        ax.text(i, below[i] / 2, f"{below[i]}%", ha="center", va="center",
                fontsize=8.6, color=INK, fontweight="600")
        ax.text(i, below[i] + above[i] / 2, f"{above[i]}%", ha="center", va="center",
                fontsize=8.6, color="white", fontweight="600")
    ax.set_xticks([0, 1]); ax.set_xticklabels(yrs, fontsize=8.6)
    ax.set_ylim(0, 108); ax.set_xlim(-0.62, 1.62)
    ax.set_yticks([0, 25, 50, 75, 100]); ax.set_yticklabels(["0", "25", "50", "75", "100%"])
    ax.set_title("Sales by ticket size", fontsize=9.8, color=INK, loc="left", pad=8, fontweight="600")
    ax.plot([], [], "s", color=VIOLET, ms=7, label="above ₹1 crore")
    ax.plot([], [], "s", color=BLUE_RAMP[2], ms=7, label="up to ₹1 crore")
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.30), fontsize=7.4, ncol=1,
              handletextpad=0.5)

    # right: size mix
    ax = fig.add_axes([0.755, 0.13, 0.23, 0.55]); T.blank(ax)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_title("Registrations by flat size", fontsize=9.8, color=INK, loc="left",
                 pad=8, fontweight="600")
    bands = [("500–1,000 sq ft", 45, BLUE), ("under 500 sq ft", 36, BLUE_RAMP[3]),
             ("above 1,000 sq ft", 19, GRID)]
    y = 0.80
    for lab, pct, c in bands:
        ax.add_patch(FancyBboxPatch((0.0, y - 0.055), 0.72, 0.085,
                                    boxstyle="round,pad=0,rounding_size=0.03",
                                    fc=GRID, ec="none"))
        ax.add_patch(FancyBboxPatch((0.0, y - 0.055), 0.72 * pct / 50, 0.085,
                                    boxstyle="round,pad=0,rounding_size=0.03",
                                    fc=c, ec="none"))
        ax.text(0.76, y - 0.012, f"{pct}%", fontsize=10, fontweight="600", color=INK, va="center")
        ax.text(0.0, y + 0.075, lab, fontsize=8, color=INK2, va="center")
        y -= 0.27
    ax.text(0.0, 0.02, "81% of registrations are flats\nof 1,000 sq ft or less.",
            fontsize=7.8, color=INK2, va="bottom", linespacing=1.4)

    T.footnote(fig, "Sources: unsold inventory and ticket-size mix [SRC-032]; flat-size mix from the February 2026 registration reading [SRC-033] — a single-month observation, "
                    "treated as indicative of the shape of demand rather than as a half-yearly statistic.\n"
                    "Read together: the transaction is small and expensive. A 2BHK of 500–1,000 sq ft above ₹1 crore is the modal deal, and that is the unit the desk should be built around.")
    T.save(fig, "A3_inventory_and_demand_shape.png")


# ---------------------------------------------------------------- A4 -------
def fig_price_ladder():
    """Micro-market asking-price ladder with explicit low-confidence framing."""
    mm = sorted(E.MICRO_MARKETS, key=lambda r: -(r[2] + r[3]) / 2)
    fig, ax = plt.subplots(figsize=(11.2, 7.4))
    fig.subplots_adjust(top=0.805, bottom=0.155, left=0.20, right=0.97)
    T.titleblock(fig, "MMR micro-market asking-price ladder",
                 "Portal asking aggregates, August 2026. The bar is the observed range, not a single price — and the range is the point:\n"
                 "dispersion inside one locality is routinely 30–50%, which is exactly the gap a pocket-level desk is paid to explain.")

    corridor_col = {"Eastern/Central": BLUE, "Thane": AQUA, "Navi Mumbai": ORANGE,
                    "Western": VIOLET, "South-Central": MAGENTA, "South Mumbai": RED,
                    "Harbour": YELLOW}
    for i, r in enumerate(mm):
        name, corr, lo, hi = r[0], r[1], r[2], r[3]
        c = corridor_col[corr]
        T.rbar(ax, lo, i - 0.28, hi - lo, 0.56, c, r=700)
        ax.text(hi + 1600, i, f"₹{lo//1000}k–{hi//1000}k", va="center", fontsize=8,
                color=INK2)
        ax.plot([lo, lo], [i - 0.40, i + 0.40], color=SURFACE, lw=1.6, zorder=5)
    ax.set_yticks(range(len(mm)))
    ax.set_yticklabels([r[0] for r in mm], fontsize=8.8)
    ax.invert_yaxis()
    ax.set_xlim(0, 132000)
    ax.set_xticks([0, 20000, 40000, 60000, 80000, 100000, 120000])
    ax.set_xticklabels(["0", "₹20k", "₹40k", "₹60k", "₹80k", "₹1.0 L", "₹1.2 L"])
    ax.set_xlabel("asking price per sq ft (area basis not declared by source)", fontsize=8.4)
    T.clean(ax, ygrid=False, xgrid=True)

    # city average reference
    ax.axvline(36881, color=INK2, lw=1.1, ls=(0, (4, 3)), zorder=1)
    ax.text(37800, len(mm) - 0.4, "city weighted\naverage ₹36,881",
            fontsize=7.6, color=INK2, va="bottom", linespacing=1.3)

    handles = [plt.Line2D([], [], marker="s", ls="", color=c, ms=7, label=k)
               for k, c in corridor_col.items()]
    ax.legend(handles=handles, loc="lower right", bbox_to_anchor=(1.0, 0.02),
              fontsize=7.8, ncol=2, handletextpad=0.5, columnspacing=1.2)

    T.footnote(fig, "Source: portal asking-price aggregates [SRC-027]; city average [SRC-004].  CONFIDENCE: LOW — every bar on this chart is an asking price, "
                    "the area basis is not declared by the publisher, and listings are neither deduplicated nor aged.\n"
                    "Use this chart to triage corridors and nothing else. No number here may reach a client without being re-derived from IGR registered "
                    "instruments on a declared carpet-area basis with the sample size shown.")
    T.save(fig, "A4_price_ladder.png")


# ---------------------------------------------------------------- A5 -------
def fig_price_yield_map():
    """Price vs yield positioning — three corridor groups only (all-pairs cap)."""
    fig, ax = plt.subplots(figsize=(11.2, 6.4))
    fig.subplots_adjust(top=0.78, bottom=0.11, left=0.075, right=0.98)
    T.titleblock(fig, "Price against yield — the investor's trade-off across MMR",
                 "Capital value and rental yield move in opposite directions across the region with near-perfect consistency.\n"
                 "An advisory desk earns its fee by knowing where a specific pocket sits off this line, not by repeating that the line exists.")

    groups = {"Eastern/Central": BLUE, "Thane + Navi Mumbai": ORANGE, "Western + South": AQUA}
    gmap = {"Eastern/Central": "Eastern/Central", "Thane": "Thane + Navi Mumbai",
            "Navi Mumbai": "Thane + Navi Mumbai", "Western": "Western + South",
            "South-Central": "Western + South", "South Mumbai": "Western + South",
            "Harbour": "Eastern/Central"}

    for r in E.MICRO_MARKETS:
        name, corr, lo, hi, rent, ylo, yhi = r[0], r[1], r[2], r[3], r[4], r[5], r[6]
        mid = (lo + hi) / 2
        ymid = (ylo + yhi) / 2
        g = gmap[corr]
        c = groups[g]
        size = 40 + (rent / 1000) * 2.6
        ax.scatter(mid, ymid, s=size, color=c, alpha=0.92, zorder=4,
                   edgecolor=SURFACE, linewidth=1.6)
        ax.annotate(name, (mid, ymid), textcoords="offset points",
                    xytext=(0, -13 if name in ("Kanjurmarg", "Mulund", "Airoli", "Borivali", "Chembur") else 11),
                    ha="center", fontsize=7.5, color=INK2)

    # trend
    xs = np.array([(r[2] + r[3]) / 2 for r in E.MICRO_MARKETS])
    ys = np.array([(r[5] + r[6]) / 2 for r in E.MICRO_MARKETS])
    k = np.polyfit(np.log(xs), ys, 1)
    gx = np.linspace(xs.min() * 0.92, xs.max() * 1.05, 100)
    ax.plot(gx, np.polyval(k, np.log(gx)), color=MUTED, lw=1.1, ls=(0, (5, 4)), zorder=2)
    ax.text(78000, 3.05, "the region's price–yield line", fontsize=7.6, color=MUTED, style="italic")

    ax.set_xscale("log")
    ax.set_xticks([15000, 20000, 30000, 40000, 60000, 90000])
    ax.set_xticklabels(["₹15k", "₹20k", "₹30k", "₹40k", "₹60k", "₹90k"])
    ax.set_xlim(11000, 115000)
    ax.set_ylim(1.3, 4.8)
    ax.set_xlabel("mid asking price per sq ft  (log scale)", fontsize=8.6)
    ax.set_ylabel("indicative gross rental yield  (%)", fontsize=8.6)
    T.clean(ax, ygrid=True, xgrid=True)

    handles = [plt.Line2D([], [], marker="o", ls="", color=c, ms=8, label=k_)
               for k_, c in groups.items()]
    handles.append(plt.Line2D([], [], marker="o", ls="", color=MUTED, ms=5,
                              label="bubble size = 2BHK monthly rent"))
    ax.legend(handles=handles, loc="upper right", fontsize=7.8, handletextpad=0.6)

    ax.text(0.012, 0.045,
            "The desk's whole proposition, in one sentence: two flats in the same pocket, on the same line of this chart,\n"
            "can differ by 15% in realised price because of floor, view, society rules, maintenance and true commute.",
            transform=ax.transAxes, fontsize=8, color=INK2, linespacing=1.45,
            bbox=dict(boxstyle="round,pad=0.55", fc="#f2f6fd", ec=BLUE_RAMP[2], lw=0.9))

    T.footnote(fig, "Sources: asking prices [SRC-027]; yield bands [SRC-028]. CONFIDENCE: LOW on both axes. Yields are indicative bands derived from asking price and asking rent, "
                    "before maintenance, vacancy, property tax and transaction cost.\nNet yield is materially lower and is the only yield figure that should ever be shown to an investor client.")
    T.save(fig, "A5_price_yield_map.png")


# ---------------------------------------------------------------- A6 -------
def fig_infra_ladder():
    """Infrastructure status ladder — the single most abused variable in Indian RE research."""
    infra = E.INFRASTRUCTURE
    fig = plt.figure(figsize=(11.2, 6.6))
    ax = fig.add_axes([0.215, 0.155, 0.235, 0.615])
    T.titleblock(fig, "Infrastructure status ladder — weight by what is running, not by what is announced",
                 "Every asset below is real. They are not equally real to a buyer deciding this quarter. The bar length is the scoring weight\n"
                 "this system assigns, and it collapses hard as an asset moves from operating to merely approved.")

    status_col = {"operational": GOOD, "commissioning": AQUA,
                  "under_construction": WARN, "approved": SERIOUS}
    status_lab = {"operational": "Operational", "commissioning": "Commissioning",
                  "under_construction": "Under construction", "approved": "Approved"}

    for i, row in enumerate(infra):
        name, corr, status, milestone, target, conf, src, w = row
        c = status_col[status]
        T.rbar(ax, 0, i - 0.28, w, 0.56, c, r=0.012)
        ax.text(w + 0.03, i, f"{w:.2f}", va="center", fontsize=8.4,
                color=INK, fontweight="600")

    ax.set_yticks(range(len(infra)))
    ax.set_yticklabels([r[0] for r in infra], fontsize=8.7)
    ax.invert_yaxis()
    ax.set_xlim(0, 1.16); ax.set_ylim(len(infra) - 0.45, -0.6)
    ax.set_xticks([0, 0.5, 1.0]); ax.set_xticklabels(["0", "0.5", "1.0"], fontsize=8)
    ax.set_xlabel("scoring weight", fontsize=8.2)
    T.clean(ax, ygrid=False, xgrid=True)

    # Detail column, laid out in figure coordinates so nothing can collide.
    y_top, y_bot = 0.770, 0.155
    n = len(infra)
    for i, row in enumerate(infra):
        name, corr, status, milestone, target, conf, src, w = row
        yc = y_top - (i + 0.5) * (y_top - y_bot) / n
        fig.text(0.478, yc + 0.016, f"{status_lab[status]}", fontsize=7.4,
                 color=status_col[status], fontweight="700", va="center")
        fig.text(0.625, yc + 0.016, milestone, fontsize=7.6, color=INK2, va="center")
        fig.text(0.478, yc - 0.017,
                 f"catchment: {corr}    ·    target: {target}    ·    [{src}]",
                 fontsize=6.8, color=MUTED, va="center")

    handles = [plt.Line2D([], [], marker="s", ls="", color=c, ms=7, label=status_lab[k])
               for k, c in status_col.items()]
    fig.legend(handles=handles, loc="lower left", bbox_to_anchor=(0.012, 0.815),
               fontsize=7.8, ncol=4, handletextpad=0.5, columnspacing=1.6)

    T.footnote(fig, "Sources: Metro 3 commissioning [SRC-007]; Metro 6 [SRC-008]; Metro 2B [SRC-009]; NMIA [SRC-010]; road and corridor programme [SRC-029].\n"
                    "Rule enforced by the schema: every infrastructure record carries status, target_date, slippage_months and last_verified. An asset whose target date has moved twice "
                    "is downgraded a rung regardless of how prominent it is in developer marketing.")
    T.save(fig, "A6_infrastructure_ladder.png")


# ---------------------------------------------------------------- A7 -------
def fig_mmr_map():
    """Schematic corridor map — honest about being schematic, but genuinely informative."""
    fig = plt.figure(figsize=(11.2, 8.4))
    ax = fig.add_axes([0.015, 0.215, 0.97, 0.575])
    T.blank(ax)
    ax.set_xlim(0, 100); ax.set_ylim(0, 62)
    T.titleblock(fig, "MMR strategic coverage map — phasing, not geometry",
                 "A schematic of how the region is entered, in what order and on what trigger. Relative position and adjacency are meaningful;\n"
                 "distances and boundaries are not. Production mapping must use verified GIS boundaries and coordinates.")

    # Water
    ax.add_patch(Polygon([[0, 0], [14, 0], [12, 18], [10, 34], [6, 48], [3, 62], [0, 62]],
                         closed=True, fc="#eef4fb", ec="none", zorder=0))
    ax.text(5.5, 30, "Arabian\nSea", fontsize=8.4, color="#9db6d4", ha="center",
            style="italic", linespacing=1.4, zorder=1)
    ax.add_patch(Polygon([[57, 2], [66, 1], [65, 12], [60, 14], [56, 8]],
                         closed=True, fc="#eef4fb", ec="none", zorder=0))
    ax.text(61, 6.5, "Thane\nCreek", fontsize=6.4, color="#9db6d4", ha="center",
            style="italic", linespacing=1.3, zorder=1)

    # Corridors: (label, x, y, w, h, colour, phase, trigger)
    corridors = [
        ("SOUTH MUMBAI\nColaba · Fort · Worli", 16, 2, 21, 10.5, RED, "6",
         "After an HNI referral network exists"),
        ("WESTERN SUBURBS\nBandra · Andheri\nGoregaon · Borivali", 13, 29, 21, 30, VIOLET, "4",
         "Only with a real edge"),
        ("EASTERN & CENTRAL SUBURBS\nPowai · Kanjurmarg · Vikhroli\nBhandup · Mulund · Ghatkopar", 37, 25, 25, 21, BLUE, "1",
         "START HERE — week 2"),
        ("HARBOUR / EASTERN WATERFRONT\nWadala · Chembur · Sewri", 32, 14, 24, 10, YELLOW, "5",
         "Follows Eastern depth"),
        ("THANE\nGhodbunder · Pokhran · Kolshet", 38, 50, 24, 10.5, AQUA, "2",
         "Contiguous — Metro 4 links it"),
        ("NAVI MUMBAI\nAiroli · Vashi\nKharghar · Panvel", 68, 14, 22, 32, ORANGE, "3",
         "Highest catalyst, highest friction"),
    ]
    for lab, x, y, w, h, c, phase, trigger in corridors:
        prim = phase == "1"
        if not prim:
            ax.add_patch(FancyBboxPatch((x, y), w, h,
                                        boxstyle="round,pad=0,rounding_size=1.2",
                                        fc=c, ec="none", alpha=0.10, zorder=2))
        ax.add_patch(FancyBboxPatch((x, y), w, h,
                                    boxstyle="round,pad=0,rounding_size=1.2",
                                    fc=c if prim else "none", ec=c,
                                    lw=2.2 if prim else 1.4, zorder=3))
        ax.text(x + w / 2, y + h - 2.0, lab, ha="center", va="top", fontsize=7.6,
                color="white" if prim else INK, fontweight="600" if prim else "500",
                linespacing=1.55, zorder=5)
        ax.scatter([x + 2.6], [y + 2.4], s=210, marker="o",
                   facecolor="white" if prim else c, edgecolor=c, linewidth=1.3, zorder=6)
        ax.text(x + 2.6, y + 2.4, phase, ha="center", va="center", fontsize=7.2,
                fontweight="700", color=c if prim else "white", zorder=7)
        ax.text(x + 5.6, y + 2.4, trigger, ha="left", va="center", fontsize=6.5,
                color="white" if prim else MUTED, zorder=7, style="italic")

    # Expansion sequence arrows out of the Phase-1 box
    for p0, p1 in [((49, 25), (49, 24.3)),      # -> Harbour
                   ((62, 34), (68, 32)),         # -> Navi Mumbai
                   ((50, 46), (50, 50)),         # -> Thane
                   ((37, 38), (34, 40)),         # -> Western
                   ((34, 14), (30, 12.7))]:      # Harbour -> South Mumbai
        T.arrow(ax, p0, p1, color=MUTED, lw=1.5, ms=8, z=4)

    # Infrastructure spines — drawn clear of every box
    ax.plot([64.5, 64.5], [26, 48], color=GOOD, lw=1.8, ls=(0, (1, 2.2)), zorder=1)
    ax.text(65.4, 47.5, "Eastern Express Hwy", fontsize=6.3, color=GOOD, rotation=90, va="top")
    ax.plot([37, 62], [47.8, 47.8], color=BLUE_RAMP[7], lw=1.8, ls=(0, (1, 2.2)), zorder=1)
    ax.text(37.6, 48.3, "Metro 6 (Pink) · JVLR alignment", fontsize=6.3, color=BLUE_RAMP[9])
    ax.plot([56, 68], [18, 18], color=ORANGE, lw=1.8, ls=(0, (1, 2.2)), zorder=1)
    ax.text(62, 19.0, "Atal Setu (MTHL)", fontsize=6.3, color=ORANGE, ha="center")
    ax.scatter([79], [9.5], s=190, marker="o", facecolor=GOOD, edgecolor="white",
               linewidth=1.3, zorder=8)
    ax.text(79, 6.4, "NMIA — operational", fontsize=6.6, color=GOOD, ha="center",
            va="top", fontweight="600", zorder=8)

    # Rationale strip below the map — its own band, so nothing can collide
    axr = fig.add_axes([0.015, 0.068, 0.97, 0.128]); T.blank(axr)
    axr.set_xlim(0, 3); axr.set_ylim(0, 1)
    panels = [
        ("1 — EASTERN / CENTRAL FIRST", BLUE,
         "The only corridor combining real transaction depth with the highest execution simplicity in "
         "the region: one contiguous belt reachable end to end inside an hour, an operating employment "
         "catchment, a live metro alignment, and advisory whitespace the Western suburbs no longer offer."),
        ("2 — THANE, THEN 3 — NAVI MUMBAI", ORANGE,
         "Thane is contiguous with the pilot belt and Metro 4 physically links them, so the same broker "
         "network and travel pattern extend into it. Navi Mumbai carries the stronger catalyst — NMIA has "
         "run 24×7 since February 2026 — but sits behind a creek crossing and separate civic jurisdictions."),
        ("WHY NOT WESTERN OR SOUTH FIRST", MUTED,
         "The Western suburbs score joint-third on raw deal flow alone; on whitespace they score 4 of 10. "
         "Entering there means competing on price against established firms with no informational edge. "
         "South Mumbai has the highest ticket, the thinnest depth, and runs on relationships a new entrant lacks."),
    ]
    for i, (head, c, body) in enumerate(panels):
        axr.add_patch(FancyBboxPatch((i + 0.008, 0.02), 0.984, 0.96,
                                     boxstyle="round,pad=0,rounding_size=0.04",
                                     fc="#f6f7f9", ec=GRID, lw=0.9))
        axr.add_patch(Rectangle((i + 0.008, 0.02), 0.012, 0.96, fc=c, ec="none"))
        axr.text(i + 0.045, 0.86, head, fontsize=7.4, fontweight="700", color=c, va="top")
        axr.text(i + 0.045, 0.63, T.wrap(" ".join(body.split()), 74),
                 fontsize=6.5, color=INK2, va="top", linespacing=1.65)

    T.footnote(fig, "Phase order is the output of the corrected entry model in section B3, not a geographic judgement. Phase numbers denote sequence, "
                    "and each carries an explicit trigger rather than a date.\nInfrastructure spines shown are indicative alignments for orientation only [SRC-007 to SRC-010, SRC-029].")
    T.save(fig, "A7_mmr_coverage_map.png")


# ---------------------------------------------------------------- A8 -------
def fig_revenue_pool():
    """Where the addressable commission pool actually is."""
    fig = plt.figure(figsize=(11.2, 6.4))
    ax = fig.add_axes([0.015, 0.075, 0.97, 0.70])
    T.blank(ax)
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    T.titleblock(fig, "From market size to the pool one desk can actually reach",
                 "The funnel from headline market to realistic Year-1 revenue spans nearly four orders of magnitude. Every strategy document that stops\n"
                 "at the first bar is selling optimism; the only number that matters is the one at the bottom.")

    stages = [
        ("Mumbai registrations, H1 2026", "80,221", "transactions", 68, BLUE_RAMP[10],
         "the whole BMC市 base — context, not a target"),
        ("One corridor's share (~9% of city)", "≈ 7,200", "transactions", 52, BLUE_RAMP[8],
         "measure directly from IGR by sub-registrar office"),
        ("Pilot pocket set (20–30 pockets)", "≈ 1,100", "transactions", 38, BLUE_RAMP[6],
         "the geography frozen for the 90-day pilot"),
        ("Broker-intermediated share (~55%)", "≈ 600", "transactions", 26, BLUE_RAMP[4],
         "the rest are direct, family or developer walk-in"),
        ("Reachable by one desk in Year 1", "≈ 15", "closures", 15, ORANGE,
         "≈2.5% of the reachable pool — base case, section G1"),
    ]
    stages[0] = (stages[0][0], stages[0][1], stages[0][2], stages[0][3], stages[0][4],
                 "the whole BMC city base — context, not a target")

    top, band, gap = 96.0, 11.0, 6.8
    for i, (lab, val, unit, w, c, note) in enumerate(stages):
        y = top - i * (band + gap)
        x0 = 50 - w / 2
        ax.add_patch(FancyBboxPatch((x0, y - band), w, band,
                                    boxstyle="round,pad=0,rounding_size=0.9",
                                    fc=c, ec="none", zorder=3))
        ax.text(50, y - band / 2, lab, ha="center", va="center", fontsize=8.3,
                color="white", fontweight="600", zorder=4)
        ax.text(x0 - 2.0, y - band / 2 + 1.4, val, ha="right", va="center", fontsize=11.5,
                color=INK, fontweight="600", zorder=4)
        ax.text(x0 - 2.0, y - band / 2 - 2.6, unit, ha="right", va="center", fontsize=7.4,
                color=MUTED, zorder=4)
        ax.text(50 + w / 2 + 2.0, y - band / 2, note, ha="left", va="center",
                fontsize=7.2, color=MUTED, zorder=4)
        if i < len(stages) - 1:
            nxt = stages[i + 1][3]
            ax.add_patch(Polygon([[x0, y - band], [x0 + w, y - band],
                                  [50 + nxt / 2, y - band - gap], [50 - nxt / 2, y - band - gap]],
                                 closed=True, fc=c, ec="none", alpha=0.18, zorder=2))
            drop = 100 * stages[i + 1][3] / w
            ax.text(50, y - band - gap / 2, f"↓", ha="center", va="center",
                    fontsize=8, color=MUTED, zorder=5)

    ax.text(50, 2.0,
            "At a ₹2.4 crore average consideration and 1% per side, 15 closures is roughly ₹36 lakh of gross commission.\n"
            "That is the entire Year-1 prize for a single-founder desk, and every cost in this plan must fit inside it.",
            ha="center", va="bottom", fontsize=8.5, color=INK, linespacing=1.55, fontweight="500")

    T.footnote(fig, "Registration base [SRC-005]. Corridor share, pocket share, intermediation rate and the reachable-closure figure are ANALYST ASSUMPTIONS, not observed statistics — "
                    "they are the first four numbers the 90-day pilot exists to replace.\nMeasure each one directly from IGR sub-registrar data and your own funnel before planning Year 2.")
    T.save(fig, "A8_revenue_pool.png")


if __name__ == "__main__":
    T.apply()
    import os
    os.makedirs(OUT, exist_ok=True)
    for f in [fig_market_scale, fig_registration_engine, fig_inventory_context,
              fig_price_ladder, fig_price_yield_map, fig_infra_ladder,
              fig_mmr_map, fig_revenue_pool]:
        f(); print("ok", f.__name__)
