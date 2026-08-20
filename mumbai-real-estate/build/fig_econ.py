"""fig_econ.py — Part D: funnel, unit economics, runway, risk."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Polygon, Circle
import theme as T
from theme import (SURFACE, INK, INK2, MUTED, GRID, BASELINE, BLUE, ORANGE, AQUA,
                   YELLOW, MAGENTA, GREEN, VIOLET, RED, GOOD, WARN, SERIOUS, CRITICAL,
                   SEQ_BLUE, BLUE_RAMP)
import evidence as E

L = 100_000          # one lakh
CR = 10_000_000      # one crore


# ------------------------------------------------------------------ model --
# Every economic quantity comes from evidence.py so the report, the figures,
# the CSVs, the workbook and the deck cannot drift apart.
commission_for = E.commission_for
blended        = E.blended
income_tax     = E.income_tax
ONE_OFF, MONTHLY, DRAWINGS, OPEX = E.ONE_OFF, E.MONTHLY, E.DRAWINGS, E.OPEX


# ---------------------------------------------------------------- D1 -------
def fig_funnel():
    """The deal funnel in three scenarios, with stage conversion made explicit."""
    stages = E.FUNNEL_STAGES
    fig = plt.figure(figsize=(11.2, 6.2))
    T.titleblock(fig, "The deal funnel — three scenarios for Year 1",
                 "Everything downstream of this chart depends on two numbers: qualified-lead rate and site-visit conversion.\n"
                 "They are the first two things the 90-day pilot must measure, because every plan built on assumed values is fiction.")

    ax = fig.add_axes([0.055, 0.115, 0.40, 0.615])
    labels = [s[0] for s in stages]
    base = [s[2] for s in stages]
    maxv = base[0]
    for i, (lab, cons, bas, stre) in enumerate(stages):
        w = max(100 * bas / maxv, 13)
        x0 = 50 - w / 2
        c = BLUE_RAMP[3 + i * 2] if i < 4 else ORANGE
        ax.add_patch(FancyBboxPatch((x0, -i * 20 - 15), w, 13,
                                    boxstyle="round,pad=0,rounding_size=0.8",
                                    fc=c, ec="none", zorder=3))
        ax.text(50, -i * 20 - 8.5, f"{bas:,}", ha="center", va="center",
                fontsize=11, color="white", fontweight="700", zorder=4)
        ax.text(50, -i * 20 - 1.5, lab, ha="center", va="bottom", fontsize=8.2,
                color=INK, fontweight="600", zorder=4)
        if i < len(stages) - 1:
            nxt = stages[i + 1][2]
            rate = 100 * nxt / bas
            ax.text(96, -i * 20 - 21.5, f"{rate:.0f}%", ha="right", va="center",
                    fontsize=8.6, color=INK, fontweight="700", zorder=4)
            ax.text(96, -i * 20 - 26.0, "convert", ha="right", va="center",
                    fontsize=6.6, color=MUTED, zorder=4)
            ax.add_patch(Polygon([[x0, -i * 20 - 15], [x0 + w, -i * 20 - 15],
                                  [50 + max(100 * nxt / maxv, 13) / 2, -i * 20 - 20],
                                  [50 - max(100 * nxt / maxv, 13) / 2, -i * 20 - 20]],
                                 closed=True, fc=c, ec="none", alpha=0.18, zorder=2))
    ax.set_xlim(0, 100); ax.set_ylim(-98, 4)
    T.blank(ax)
    ax.set_title("BASE CASE", fontsize=8.6, color=INK, loc="left", pad=6, fontweight="700")

    # scenario comparison
    ax2 = fig.add_axes([0.575, 0.155, 0.225, 0.575])
    idx = np.arange(len(stages))
    wid = 0.26
    for j, (name, col, key) in enumerate([("Conservative", BLUE_RAMP[2], 1),
                                          ("Base", BLUE, 2),
                                          ("Stretch", ORANGE, 3)]):
        vals = [s[key] for s in stages]
        ax2.barh(idx + (j - 1) * wid, vals, height=wid * 0.88, color=col,
                 zorder=3, label=name)
    ax2.set_yticks(idx); ax2.set_yticklabels(labels, fontsize=7.8)
    ax2.invert_yaxis()
    ax2.set_xscale("log"); ax2.set_xlim(4, 2600)
    ax2.set_xticks([10, 100, 1000]); ax2.set_xticklabels(["10", "100", "1,000"], fontsize=7.4)
    ax2.set_xlabel("count (log scale)", fontsize=8)
    T.clean(ax2, ygrid=False, xgrid=True)
    ax2.legend(loc="lower right", fontsize=7.4, handletextpad=0.5)
    ax2.set_title("ALL THREE SCENARIOS", fontsize=8.6, color=INK, loc="left",
                  pad=6, fontweight="700")

    # revenue rail
    fig.text(0.815, 0.720, "WHAT EACH SCENARIO PAYS", fontsize=7.8, fontweight="700",
             color=INK, va="top")
    consid, rate = blended()
    y = 0.660
    for name, col, key in [("Conservative", BLUE_RAMP[2], 1), ("Base", BLUE, 2),
                           ("Stretch", ORANGE, 3)]:
        n = stages[-1][key]
        gross = commission_for(n)
        profit = gross - OPEX * 12 - ONE_OFF
        post = profit - income_tax(max(profit, 0))
        fig.patches.append(Rectangle((0.815, y - 0.004), 0.013, 0.019, fc=col, ec="none",
                                     transform=fig.transFigure))
        fig.text(0.836, y, f"{name} — {n} closures", fontsize=7.6, fontweight="600",
                 color=INK, va="baseline")
        for lab, v in [("gross commission", gross), ("post-tax to founder", post)]:
            y -= 0.030
            fig.text(0.836, y, lab, fontsize=6.9, color=INK2, va="baseline")
            fig.text(0.985, y, f"₹{v/L:,.1f} L", fontsize=7.2, color=INK, va="baseline",
                     ha="right", fontweight="600")
        y -= 0.052
    fig.text(0.815, y + 0.012,
             T.wrap(f"Blended assumptions: average consideration ₹{consid/CR:.2f} crore, "
                    f"blended commission {rate*100:.2f}%, operating cost "
                    f"₹{OPEX*12/L:.1f} L a year before any founder drawings.", 42),
             fontsize=6.6, color=MUTED, va="top", linespacing=1.65)

    T.footnote(fig, "ILLUSTRATIVE PLANNING MODEL [model]. Conversion rates, segment mix and commission rates are assumptions, not observations — replace "
                    "every one of them after 30–50 qualified leads. Tax is indicative on FY2025-26 individual new-regime slabs for a proprietorship and is "
                    "not advice; confirm the entity and tax position with a CA [SRC-031]. Brokerage attracts 18% GST as an output tax [SRC-012] and 2% TDS "
                    "under section 194H on receipt [SRC-024]; neither is shown as a cost above because both are pass-through or creditable.")
    T.save(fig, "D1_deal_funnel.png")


# ---------------------------------------------------------------- D2 -------
def fig_unit_economics():
    """Where a single closure's money goes, and what a year of them adds up to."""
    fig = plt.figure(figsize=(11.2, 5.9))
    T.titleblock(fig, "Unit economics — one closure, then a year of them",
                 "Left: the cash journey of a single average closure, from consideration to what reaches the founder.\n"
                 "Right: the Year-1 profit and loss in the base case, with the founder's own time priced in.")

    # ---- single deal
    ax = fig.add_axes([0.145, 0.135, 0.305, 0.575])
    consid, rate = blended()
    gross = consid * rate
    gst = gross * 0.18
    tds = gross * 0.02
    steps = [
        ("Average consideration", consid, BLUE_RAMP[1], "the flat's price"),
        (f"Commission at {rate*100:.2f}%", gross, BLUE, "blended across the segment mix"),
        ("GST added, 18%", gst, GRID, "collected from client, remitted"),
        ("TDS withheld, 2%", -tds, WARN, "recoverable against income tax"),
        ("Cash on receipt", gross - tds, GOOD, "what actually lands in the bank"),
    ]
    ypos = [0, 1, 2, 3, 4]
    ax.barh(0, consid / L, height=0.5, color=BLUE_RAMP[1], zorder=3)
    ax.text(consid / L + 3, 0, f"₹{consid/L:,.0f} L", va="center", fontsize=8,
            color=INK, fontweight="600")
    ax.barh(1, gross / L, height=0.5, color=BLUE, zorder=3)
    ax.text(gross / L + 3, 1, f"₹{gross/L:,.2f} L", va="center", fontsize=8,
            color=INK, fontweight="600")
    ax.barh(2, gross / L, height=0.5, color=BLUE, alpha=0.35, zorder=3)
    ax.barh(2, gst / L, left=gross / L, height=0.5, color=GRID, zorder=3)
    ax.text((gross + gst) / L + 3, 2, f"+₹{gst/L:,.2f} L GST", va="center",
            fontsize=7.4, color=MUTED)
    ax.barh(3, (gross - tds) / L, height=0.5, color=BLUE, alpha=0.35, zorder=3)
    ax.barh(3, tds / L, left=(gross - tds) / L, height=0.5, color=WARN, zorder=3)
    ax.text(gross / L + 3, 3, f"−₹{tds/L:,.2f} L TDS", va="center",
            fontsize=7.4, color=MUTED)
    ax.barh(4, (gross - tds) / L, height=0.5, color=GOOD, zorder=3)
    ax.text((gross - tds) / L + 3, 4, f"₹{(gross-tds)/L:,.2f} L", va="center",
            fontsize=8.4, color=INK, fontweight="700")
    ax.set_yticks(ypos)
    ax.set_yticklabels([s[0] for s in steps], fontsize=8)
    ax.invert_yaxis()
    ax.set_xscale("symlog", linthresh=1)
    ax.set_xlim(0, 700)
    ax.set_xticks([1, 10, 100]); ax.set_xticklabels(["₹1 L", "₹10 L", "₹100 L"], fontsize=7.4)
    T.clean(ax, ygrid=False, xgrid=True)
    ax.set_title("ONE AVERAGE CLOSURE  ·  log scale", fontsize=8.6, color=INK,
                 loc="left", pad=7, fontweight="700")
    for i, (_, _, _, note) in enumerate(steps):
        ax.text(0.6, i + 0.34, note, fontsize=6.4, color=MUTED, va="center")

    # ---- year P&L waterfall
    ax2 = fig.add_axes([0.560, 0.155, 0.420, 0.555])
    n = E.FUNNEL_STAGES[-1][2]
    g = commission_for(n)
    items = [
        ("Gross commission\n15 closures", g, BLUE, True),
        ("Data, travel,\nmarketing, tools", -OPEX * 12, ORANGE, False),
        ("One-off setup\n& certification", -ONE_OFF, ORANGE, False),
        ("Business profit", None, AQUA, True),
        ("Income tax\n(indicative)", None, RED, False),
        ("To the founder", None, GOOD, True),
    ]
    profit = g - OPEX * 12 - ONE_OFF
    tax = income_tax(profit)
    vals = [g, -OPEX * 12, -ONE_OFF, profit, -tax, profit - tax]
    running, bars = 0.0, []
    for i, (lab, _, c, is_total) in enumerate(items):
        v = vals[i]
        if is_total:
            bars.append((i, 0, v, c))
            running = v
        else:
            bars.append((i, running + v, -v, c))
            running += v
    for i, bottom, height, c in bars:
        ax2.bar(i, height / L, bottom=bottom / L, width=0.6, color=c,
                edgecolor=SURFACE, linewidth=1.2, zorder=3)
    for i, (lab, _, c, is_total) in enumerate(items):
        v = vals[i]
        top = max(v, 0) if is_total else max(bars[i][1] + bars[i][2], bars[i][1])
        ax2.text(i, top / L + 1.6, f"{'−' if v < 0 else ''}₹{abs(v)/L:,.1f} L",
                 ha="center", fontsize=7.6, color=INK,
                 fontweight="700" if is_total else "400")
    ax2.set_xticks(range(len(items)))
    ax2.set_xticklabels([it[0] for it in items], fontsize=7.0, linespacing=1.4)
    ax2.set_ylim(0, 56)
    ax2.set_ylabel("₹ lakh", fontsize=8.2)
    T.clean(ax2)
    ax2.set_title("YEAR-1 PROFIT AND LOSS  ·  base case", fontsize=8.6, color=INK,
                  loc="left", pad=7, fontweight="700")
    ax2.axhline((profit - tax) / L / 12 * 12, color="none")
    hourly = (profit - tax) / 2860
    ax2.text(0.985, 0.94,
             f"₹{(profit-tax)/L:,.1f} L for 2,860 founder-hours\n= ₹{hourly:,.0f} per hour, post-tax",
             transform=ax2.transAxes, ha="right", va="top", fontsize=7.4,
             color=INK2, linespacing=1.6,
             bbox=dict(boxstyle="round,pad=0.5", fc="#f2f6fd", ec=BLUE_RAMP[2], lw=0.9))

    T.footnote(fig, "ILLUSTRATIVE [model]. The hourly figure is the number this plan should actually be judged against: it is what the founder earns for "
                    "the year's whole effort in the base case, and it is the honest comparator to a salaried alternative. In the conservative case it falls "
                    "to roughly a third of that. Tax is indicative FY2025-26 new-regime individual slabs and not advice [SRC-031].")
    T.save(fig, "D2_unit_economics.png")


# ---------------------------------------------------------------- D3 -------
def fig_runway():
    """The cash curve — how much capital the plan actually needs before it turns."""
    months = np.arange(1, 25)
    # closures per month, base case: nothing before month 5, then a ramp
    closures = np.array([0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3,
                         3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5], dtype=float)
    per_closure = commission_for(1)
    lag = 1.5   # months between closure and cash

    # conservative: first closure two months later, half the ramp
    closures_cons = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1,
                              1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3], dtype=float)

    def curve(cl):
        inflow = np.zeros(len(months))
        for i, c in enumerate(cl):
            j = int(round(i + lag))
            if j < len(inflow):
                inflow[j] += c * per_closure * 0.98   # net of 2% TDS
        outflow = np.full(len(months), float(OPEX + DRAWINGS))
        outflow[0] += ONE_OFF
        return np.cumsum(inflow - outflow)

    cash = curve(closures)
    cash_cons = curve(closures_cons)
    trough = cash.min(); trough_m = int(np.argmin(cash)) + 1
    breakeven = next((m for m, v in zip(months, cash) if v > 0), None)

    fig = plt.figure(figsize=(11.2, 5.8))
    ax = fig.add_axes([0.062, 0.145, 0.60, 0.585])
    T.titleblock(fig, "The cash curve — how much capital this plan actually needs",
                 "Cumulative cash from a standing start, before any outside funding. The trough is the number that matters:\n"
                 "it is what must be in the bank on day one for the plan to reach its own break-even without a forced sale.")

    ax.fill_between(months, cash / L, 0, where=(cash < 0), color=RED, alpha=0.13, zorder=2)
    ax.fill_between(months, cash / L, 0, where=(cash >= 0), color=GOOD, alpha=0.13, zorder=2)
    ax.plot(months, cash / L, color=BLUE, lw=2.2, zorder=4, label="Base — 15 closures in Year 1")
    ax.plot(months, cash_cons / L, color=ORANGE, lw=2.0, ls=(0, (5, 3)), zorder=4,
            label="Conservative — 7 closures in Year 1")
    ax.axhline(0, color=BASELINE, lw=1.0, zorder=3)
    tr_c = cash_cons.min(); tr_cm = int(np.argmin(cash_cons)) + 1
    ax.scatter([tr_cm], [tr_c / L], s=50, color=ORANGE, zorder=6,
               edgecolor=SURFACE, linewidth=1.5)
    ax.annotate(f"conservative trough  −₹{abs(tr_c)/L:,.1f} L at month {tr_cm}",
                xy=(tr_cm, tr_c / L), xytext=(tr_cm + 1.2, tr_c / L - 9.0),
                fontsize=7.0, color=ORANGE, fontweight="600",
                arrowprops=dict(arrowstyle="-", color=ORANGE, lw=0.9))
    ax.legend(loc="upper left", bbox_to_anchor=(0.015, 0.99), fontsize=7.2,
              handletextpad=0.7, labelspacing=0.4)
    ax.scatter([trough_m], [trough / L], s=60, color=RED, zorder=6,
               edgecolor=SURFACE, linewidth=1.6)
    ax.annotate(f"trough  −₹{abs(trough)/L:,.1f} L\nmonth {trough_m}",
                xy=(trough_m, trough / L), xytext=(trough_m - 3.4, trough / L + 13.0),
                fontsize=7.6, color=INK, fontweight="600", linespacing=1.5,
                arrowprops=dict(arrowstyle="-", color=BASELINE, lw=0.9))
    if breakeven:
        ax.axvline(breakeven, color=GOOD, lw=1.1, ls=(0, (4, 3)), zorder=3)
        ax.text(breakeven + 0.25, ax.get_ylim()[1] * 0.72,
                f"cumulative break-even\nmonth {breakeven}", fontsize=7.4,
                color="#0a7a0a", fontweight="600", linespacing=1.5)
    ax.axvspan(0.5, 12.5, color=BLUE, alpha=0.035, zorder=0)
    lo, hi = ax.get_ylim()
    ax.text(2.6, lo + (hi - lo) * 0.045, "YEAR 1", ha="center", fontsize=7.0,
            color=MUTED, fontweight="700")
    ax.text(18.5, lo + (hi - lo) * 0.045, "YEAR 2", ha="center", fontsize=7.0,
            color=MUTED, fontweight="700")
    ax.set_xlim(1, 24); ax.set_xticks([1, 3, 6, 9, 12, 15, 18, 21, 24])
    ax.set_xticklabels([f"M{m}" for m in [1, 3, 6, 9, 12, 15, 18, 21, 24]], fontsize=7.6)
    ax.set_ylabel("cumulative cash, ₹ lakh", fontsize=8.4)
    T.clean(ax)

    # rail
    fig.text(0.690, 0.722, "WHAT THIS MEANS FOR CAPITAL", fontsize=7.8,
             fontweight="700", color=INK, va="top")
    rows = [
        ("Trough — base case", f"₹{abs(trough)/L:,.1f} L",
         "if the first closure lands in month 5"),
        ("Trough — conservative case", f"₹{abs(cash_cons.min())/L:,.1f} L",
         "if it lands in month 7 and the ramp halves"),
        ("Capital to actually raise", f"₹{abs(cash_cons.min())*1.4/L:,.0f} L",
         "the conservative trough plus 40% — plan for this one"),
        ("Fixed monthly burn", f"₹{(OPEX+DRAWINGS)/1000:,.0f} k",
         f"of which ₹{DRAWINGS/1000:.0f}k is founder drawings"),
        ("Months before first cash", "6",
         "closure in month 5, payment lands ~6 weeks later"),
        ("Cumulative break-even", f"month {breakeven}" if breakeven else "beyond M24",
         "when the business has repaid its own start-up"),
    ]
    y = 0.672
    for lab, val, sub in rows:
        fig.text(0.690, y, lab, fontsize=7.3, color=INK2, va="baseline")
        fig.text(0.985, y, val, fontsize=9.2, color=INK, va="baseline", ha="right",
                 fontweight="700")
        y -= 0.026
        fig.text(0.690, y, sub, fontsize=6.5, color=MUTED, va="baseline")
        y -= 0.048

    fig.text(0.690, y + 0.014,
             T.wrap("Founder drawings are the single largest line in the burn. Halving them "
                    "roughly halves the capital requirement — which is why the honest first "
                    "question is not 'is the market good?' but 'how long can this household "
                    "run on less?'", 46),
             fontsize=6.7, color=INK2, va="top", linespacing=1.7)

    T.footnote(fig, "ILLUSTRATIVE [model]. Closure timing is the most fragile assumption on this page: a single closure slipping from month 5 to month 8 "
                    "deepens the trough by roughly one lakh and pushes break-even out by a quarter. Payout lag is modelled at six weeks; primary-market "
                    "channel payouts commonly run 60–90 days and should be tracked per counterparty from the first deal.")
    T.save(fig, "D3_cash_runway.png")


# ---------------------------------------------------------------- D4 -------
def fig_kpi_tree():
    """The KPI tree — which numbers drive which, and where to intervene."""
    fig = plt.figure(figsize=(11.2, 6.4))
    ax = fig.add_axes([0.012, 0.055, 0.976, 0.715]); T.blank(ax)
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    T.titleblock(fig, "The KPI tree — nine numbers, and what each one is telling you",
                 "Revenue is not a lever; it is an outcome. These are the nine measurable quantities that produce it, arranged so that a bad\n"
                 "result at the top can be traced to the one branch that caused it.")

    ax.add_patch(FancyBboxPatch((36, 87), 28, 11,
                                boxstyle="round,pad=0,rounding_size=0.8",
                                fc=BLUE, ec="none", zorder=4))
    ax.text(50, 94.2, "REALISED COMMISSION", ha="center", va="center", fontsize=9,
            fontweight="700", color="white", zorder=5)
    ax.text(50, 89.8, "closures × average commission × collection rate",
            ha="center", va="center", fontsize=7.0, color="white", zorder=5, alpha=0.9)

    branches = [
        ("VOLUME", 4, AQUA, [
            ("Qualified leads / month", "budget + timeline + authority + area fit — all four, or it is not qualified"),
            ("Site-visit conversion", "visits ÷ qualified leads. Below 40% the matching is wrong, not the market"),
            ("Close rate", "closures ÷ qualified leads. The single clearest measure of business health"),
        ]),
        ("VALUE", 36, ORANGE, [
            ("Average realised commission", "revenue ÷ closures. Falling means discounting, or drifting down-ticket"),
            ("Payout days", "cash receipt minus closure. This is working capital, not an accounting detail"),
            ("Segment concentration", "share from any one developer or channel. Above 40% is a single point of failure"),
        ]),
        ("EFFICIENCY", 68, VIOLET, [
            ("Research hours / closure", "the system's return on effort. Must fall across the year or the system is a hobby"),
            ("Referral coefficient", "new qualified referrals per closed client. Above 0.5 the business compounds"),
            ("Data freshness coverage", "non-stale high/medium-confidence facts ÷ facts required. Operational trust"),
        ]),
    ]
    for name, x, c, kpis in branches:
        ax.add_patch(FancyBboxPatch((x, 74), 28, 7.5,
                                    boxstyle="round,pad=0,rounding_size=0.7",
                                    fc=c, ec="none", zorder=4))
        ax.text(x + 14, 77.75, name, ha="center", va="center", fontsize=8.2,
                fontweight="700", color="white", zorder=5)
        ax.plot([50, x + 14], [87, 83.5], color=BASELINE, lw=1.0, zorder=1)
        ax.plot([x + 14, x + 14], [83.5, 81.5], color=BASELINE, lw=1.0, zorder=1)
        for j, (kpi, why) in enumerate(kpis):
            yy = 58 - j * 19
            ax.add_patch(FancyBboxPatch((x, yy), 28, 14,
                                        boxstyle="round,pad=0,rounding_size=0.6",
                                        fc=SURFACE, ec=c, lw=1.2, zorder=3))
            ax.add_patch(Rectangle((x, yy), 0.9, 14, fc=c, ec="none", zorder=4))
            ax.text(x + 2.2, yy + 10.4, kpi, fontsize=7.5, fontweight="600",
                    color=INK, va="center")
            ax.text(x + 2.2, yy + 4.6, T.wrap(why, 44), fontsize=6.4, color=INK2,
                    va="center", linespacing=1.55)
            ax.plot([x + 1.0, x + 1.0], [74 if j == 0 else yy + 19, yy + 14],
                    color=c, lw=1.0, alpha=0.45, zorder=1)

    T.footnote(fig, "Definitions and formulas are the operating standard for this business [model]. Two rules make the tree work: every KPI is computed "
                    "from the CRM rather than from memory, and a qualified lead means all four tests passed. Loosening the definition of a qualified lead "
                    "is the most common way a founder hides a demand problem from themselves for two quarters.")
    T.save(fig, "D4_kpi_tree.png")


# ---------------------------------------------------------------- D5 -------
def fig_risk_matrix():
    """Risk register as a likelihood x impact matrix, with the controls named."""
    risks = E.RISKS
    fig = plt.figure(figsize=(11.2, 8.4))
    ax = fig.add_axes([0.055, 0.395, 0.375, 0.375])
    T.titleblock(fig, "Risk register — likelihood against impact",
                 "Fourteen risks, positioned by how likely they are and how much damage they do. The top-right quadrant is not a watchlist;\n"
                 "it is the set of things that must have a named control before month 1 ends.")

    for i in range(1, 6):
        for j in range(1, 6):
            sev = i * j
            c = "#f6f6f4" if sev <= 6 else ("#fdf6e8" if sev <= 12 else "#fdeeee")
            ax.add_patch(Rectangle((i - 0.5, j - 0.5), 1, 1, fc=c, ec=SURFACE, lw=1.4,
                                   zorder=1))

    for idx, (name, lk, im, warn, ctrl, phase) in enumerate(risks, 1):
        sev = lk * im
        c = CRITICAL if sev >= 16 else (WARN if sev >= 9 else MUTED)
        jitter = ((idx * 37) % 7 - 3) * 0.055
        jitter2 = ((idx * 53) % 5 - 2) * 0.055
        ax.scatter([lk + jitter], [im + jitter2], s=210, color=c, zorder=4,
                   edgecolor=SURFACE, linewidth=1.6, alpha=0.95)
        ax.text(lk + jitter, im + jitter2, str(idx), ha="center", va="center",
                fontsize=7.2, color="white", fontweight="700", zorder=5)

    ax.set_xlim(0.5, 5.5); ax.set_ylim(0.5, 5.5)
    ax.set_xticks(range(1, 6)); ax.set_yticks(range(1, 6))
    ax.set_xticklabels(["rare", "unlikely", "possible", "likely", "near\ncertain"],
                       fontsize=7.0, linespacing=1.3)
    ax.set_yticklabels(["minor", "moderate", "serious", "major", "existential"], fontsize=7.0)
    ax.set_xlabel("likelihood", fontsize=8.4)
    ax.set_ylabel("impact", fontsize=8.4)
    T.clean(ax, ygrid=False, xgrid=False)
    ax.tick_params(length=0)
    ax.text(5.42, 5.42, "ACT NOW", ha="right", va="top", fontsize=7.2,
            color=CRITICAL, fontweight="700", alpha=0.8)

    # ranked list
    order = sorted(range(len(risks)), key=lambda i: -(risks[i][1] * risks[i][2]))
    fig.text(0.455, 0.780, "RANKED BY SEVERITY  ·  likelihood × impact", fontsize=7.8,
             fontweight="700", color=INK, va="top")
    y = 0.745
    for rank, i in enumerate(order):
        name, lk, im, warn, ctrl, phase = risks[i]
        sev = lk * im
        c = CRITICAL if sev >= 16 else (WARN if sev >= 9 else MUTED)
        fig.patches.append(Circle((0.4665, y + 0.004), 0.0062, fc=c, ec="none",
                                  transform=fig.transFigure))
        fig.text(0.4665, y + 0.004, str(i + 1), fontsize=5.6, color="white",
                 ha="center", va="center", fontweight="700", zorder=5)
        fig.text(0.478, y, T.wrap(name, 36), fontsize=7.0, color=INK, va="baseline",
                 fontweight="600")
        fig.text(0.690, y, T.wrap(ctrl, 66), fontsize=6.2, color=INK2, va="baseline",
                 linespacing=1.55)
        fig.text(0.478, y - 0.017, f"severity {sev}  ·  {phase}", fontsize=6.0,
                 color=MUTED, va="baseline")
        y -= 0.0497

    T.footnote(fig, "Likelihood and impact are analyst judgements for a single-founder start [model]. The register is only useful if it is re-scored at "
                    "every decision gate: risks 1 and 6 fall away once compliance is complete, while risks 4 and 8 rise sharply the moment real money is "
                    "in play. Regulatory basis for risks 1, 6 and 10: [SRC-001, SRC-002, SRC-017, SRC-018, SRC-023].")
    T.save(fig, "D5_risk_matrix.png")


# ---------------------------------------------------------------- D6 -------
def fig_channels():
    """Lead channels: what each costs, what each is worth, how long each takes."""
    channels = [
        # name, cost per qualified lead (Rs), close rate %, months to productive, note
        ("Referral network", 900, 22, 2, "Alumni, colleagues, CA / lawyer / lender contacts", GOOD, (-4, -24)),
        ("Existing clients", 300, 28, 7, "Post-close support plus an explicit referral ask", GOOD, (14, 10)),
        ("Broker co-broking", 1800, 14, 2, "Reliable counterparties by locality and project", WARN, (-30, -6)),
        ("Developer channel", 2200, 12, 3, "Registered channel partner; developer pays", WARN, (2, -26)),
        ("WhatsApp pocket briefs", 1400, 11, 3, "One-page comparison with source and date", WARN, (-40, -14)),
        ("Search / intent content", 3600, 8, 8, "Specific queries: '2BHK Powai vs Vikhroli'", SERIOUS, (0, -30)),
        ("Corporate rentals", 2600, 16, 5, "HR and admin contacts near business districts", WARN, (24, 6)),
        ("Paid portal listings", 6200, 5, 1, "Fast, expensive, and the least defensible", CRITICAL, (0, 15)),
    ]
    fig = plt.figure(figsize=(11.2, 6.2))
    ax = fig.add_axes([0.145, 0.170, 0.41, 0.560])
    T.titleblock(fig, "Lead channels — cost, quality, and time to become productive",
                 "The cheapest channels are the slowest to build and the hardest to buy. That is precisely why they are worth building:\n"
                 "a referral engine cannot be outspent by a competitor, and a portal listing can be outbid by anyone, this afternoon.")

    order = sorted(range(len(channels)), key=lambda i: channels[i][1])
    for row, i in enumerate(order):
        name, cost, close, ramp, note, c, _ = channels[i]
        T.rbar(ax, 0, row - 0.28, cost, 0.56, c, r=60)
        ax.text(cost + 180, row, f"₹{cost:,}", va="center", fontsize=7.8,
                color=INK, fontweight="600")
        ax.text(cost + 1250, row, f"{close}% close  ·  {ramp} mo to ramp",
                va="center", fontsize=6.8, color=MUTED)
    ax.set_yticks(range(len(channels)))
    ax.set_yticklabels([channels[i][0] for i in order], fontsize=8.2)
    ax.invert_yaxis()
    ax.set_xlim(0, 9400)
    ax.set_xticks([0, 2000, 4000, 6000])
    ax.set_xticklabels(["₹0", "₹2,000", "₹4,000", "₹6,000"], fontsize=7.6)
    ax.set_xlabel("cost per qualified lead", fontsize=8.4)
    T.clean(ax, ygrid=False, xgrid=True)

    # scatter: cost vs quality
    ax2 = fig.add_axes([0.635, 0.170, 0.345, 0.560])
    for name, cost, close, ramp, note, c, off in channels:
        ax2.scatter([cost], [close], s=60 + ramp * 34, color=c, zorder=4,
                    edgecolor=SURFACE, linewidth=1.5, alpha=0.95)
        ax2.annotate(T.wrap(name, 15), (cost, close), textcoords="offset points",
                     xytext=off, ha="center", fontsize=6.5, color=INK2, linespacing=1.35)
    ax2.set_xlim(-400, 7400); ax2.set_ylim(0, 34)
    ax2.set_xticks([0, 2000, 4000, 6000])
    ax2.set_xticklabels(["₹0", "₹2k", "₹4k", "₹6k"], fontsize=7.4)
    ax2.set_xlabel("cost per qualified lead", fontsize=8.2)
    ax2.set_ylabel("close rate (%)", fontsize=8.2)
    T.clean(ax2, ygrid=True, xgrid=True)
    ax2.set_title("BUBBLE SIZE = MONTHS TO BECOME PRODUCTIVE", fontsize=7.4,
                  color=INK, loc="left", pad=7, fontweight="700")
    ax2.annotate("build these first,\nthey pay for years",
                 xy=(700, 25), xytext=(2100, 30), fontsize=6.8, color="#0a7a0a",
                 linespacing=1.5, fontweight="600",
                 arrowprops=dict(arrowstyle="-|>,head_width=0.22,head_length=0.42",
                                 color=GOOD, lw=1.0, connectionstyle="arc3,rad=0.25"))

    T.footnote(fig, "ILLUSTRATIVE PLANNING ASSUMPTIONS [model] — no channel-level CAC data exists for a business that has not yet run. These are starting "
                    "hypotheses to be replaced by measurement: tag every single lead with its source from day one, and re-draw this chart at day 90 with "
                    "real numbers. Every published brief and listing is an advertisement under the MahaRERA disclosure order and must carry the QR code and "
                    "registration number [SRC-017].")
    T.save(fig, "D6_lead_channels.png")


if __name__ == "__main__":
    T.apply()
    for f in [fig_funnel, fig_unit_economics, fig_runway, fig_kpi_tree,
              fig_risk_matrix, fig_channels]:
        f(); print("ok", f.__name__)
