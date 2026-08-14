"""fig_work.py — Part C: the flow of work, its division, and the workload."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Polygon, Circle
import theme as T
from theme import (SURFACE, INK, INK2, MUTED, GRID, BASELINE, BLUE, ORANGE, AQUA,
                   YELLOW, MAGENTA, GREEN, VIOLET, RED, GOOD, WARN, SERIOUS, CRITICAL,
                   SEQ_BLUE, BLUE_RAMP)
import evidence as E

WS_COL = {"compliance": VIOLET, "research": BLUE, "field": AQUA,
          "demand": ORANGE, "deal": YELLOW, "system": MAGENTA}
WS_LAB = {k: l for k, l, _, _ in E.WORKSTREAMS}


# ---------------------------------------------------------------- C1 -------
def fig_operating_flow():
    """The end-to-end operating flow: what enters, what happens to it, what leaves."""
    fig = plt.figure(figsize=(11.2, 7.6))
    ax = fig.add_axes([0.012, 0.045, 0.976, 0.745]); T.blank(ax)
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    T.titleblock(fig, "The operating flow — what actually happens, in order",
                 "Six stages. Every stage has a named input, a named output and a rule that must hold before work moves on.\n"
                 "Stage 6 is the one most brokerages never build, and it is the only stage that makes the next cycle cheaper than the last.")

    stages = [
        ("1", "ACQUIRE", BLUE,
         ["MahaRERA project extracts", "IGR registered instruments",
          "Ready Reckoner tables", "MMRDA & BMC infra records"],
         "Raw observation", "Nothing enters without\na source_ref and a date"),
        ("2", "VALIDATE", AQUA,
         ["Declare area_basis", "Declare price_type",
          "Attach sample_size", "Flag source conflicts"],
         "Trusted fact", "Conflicts are retained\nand flagged, never resolved\nby silent preference"),
        ("3", "STRUCTURE", MAGENTA,
         ["Bind to geo_id (L0–L6)", "Bind to RERA project id",
          "Normalise to carpet basis", "Compute pocket aggregates"],
         "Comparable", "An aggregate below the\nminimum n is published\nvisually downgraded"),
        ("4", "INTERPRET", VIOLET,
         ["Pocket scorecards", "Risk matrix",
          "Infrastructure weighting", "Net yield & all-in cost"],
         "Point of view", "Every score traces back\nto the facts that made it"),
        ("5", "MATCH & EXECUTE", ORANGE,
         ["Client-fit filters", "Ranked shortlist",
          "Accompanied site visits", "Offer, terms, closure"],
         "Closed transaction", "Written brokerage terms\nbefore any engagement"),
        ("6", "CAPTURE", YELLOW,
         ["Closed price vs asking", "Objections & lost reasons",
          "Society rules & maintenance", "True commute measured"],
         "Proprietary evidence", "Capture happens during\nthe deal, not after it"),
    ]

    x0, w, gap = 2.0, 15.0, 1.4
    top, boxh = 93.0, 63.0
    for i, (num, name, c, items, output, rule) in enumerate(stages):
        x = x0 + i * (w + gap)
        ax.add_patch(FancyBboxPatch((x, top - boxh), w, boxh,
                                    boxstyle="round,pad=0,rounding_size=0.7",
                                    fc=SURFACE, ec=c, lw=1.5, zorder=3))
        ax.add_patch(FancyBboxPatch((x, top - 8.6), w, 8.6,
                                    boxstyle="round,pad=0,rounding_size=0.7",
                                    fc=c, ec="none", zorder=4))
        ax.add_patch(Rectangle((x, top - 8.6), w, 1.0, fc=c, ec="none", zorder=4))
        ax.text(x + 1.6, top - 4.3, num, ha="center", va="center", fontsize=10,
                fontweight="700", color="white", zorder=6)
        ax.text(x + w / 2 + 1.2, top - 4.3, name, ha="center", va="center", fontsize=8.4,
                fontweight="700", color="white", zorder=6)
        yy = top - 13.8
        for it in items:
            ax.text(x + 1.2, yy, "·", fontsize=8, color=c, va="center", zorder=5)
            ax.text(x + 2.5, yy, T.wrap(it, 21), fontsize=6.7, color=INK2,
                    va="center", zorder=5, linespacing=1.35)
            yy -= 4.5 * (1 + T.wrap(it, 21).count("\n"))
        # output chip
        ax.add_patch(FancyBboxPatch((x + 0.9, top - boxh + 11.0), w - 1.8, 5.0,
                                    boxstyle="round,pad=0,rounding_size=0.5",
                                    fc=c, ec="none", alpha=0.13, zorder=4))
        ax.text(x + w / 2, top - boxh + 13.5, output.upper(), ha="center", va="center",
                fontsize=6.8, fontweight="700", color=c, zorder=5)
        ax.text(x + w / 2, top - boxh + 5.4, rule, ha="center", va="center",
                fontsize=6.2, color=MUTED, zorder=5, linespacing=1.5, style="italic")
        if i < len(stages) - 1:
            T.arrow(ax, (x + w + 0.05, top - 4.3), (x + w + gap - 0.05, top - 4.3),
                    color=BASELINE, lw=1.4, ms=7, z=6)

    # feedback loop
    fy = top - boxh - 8.5
    ax.annotate("", xy=(x0 + 0.6, top - boxh - 0.5), xytext=(x0 + 5 * (w + gap) + w / 2, fy),
                arrowprops=dict(arrowstyle="-|>,head_width=0.3,head_length=0.55",
                                color=YELLOW, lw=1.8,
                                connectionstyle="angle,angleA=0,angleB=90,rad=6"))
    ax.plot([x0 + 5 * (w + gap) + w / 2, x0 + 5 * (w + gap) + w / 2],
            [top - boxh - 0.5, fy], color=YELLOW, lw=1.8, zorder=2)
    ax.text(50, fy - 3.4,
            "THE COMPOUNDING LOOP  ·  every visit, objection and closure re-enters at stage 1 as a proprietary observation "
            "no competitor holds",
            ha="center", va="top", fontsize=7.6, color=INK, fontweight="600")
    ax.text(50, fy - 8.2,
            "This is the only part of the system that gets more valuable the longer it runs. It costs nothing extra to build — "
            "it costs discipline to not skip.",
            ha="center", va="top", fontsize=7.0, color=MUTED, style="italic")

    # compliance gate
    gate_x = x0 + 4 * (w + gap) - gap / 2
    ax.plot([gate_x, gate_x], [top + 5.0, top - boxh - 1.5], color=CRITICAL,
            lw=1.4, ls=(0, (4, 3)), zorder=7)
    ax.text(gate_x - 1.0, top + 5.6, "COMPLIANCE GATE", ha="right", va="bottom",
            fontsize=7.2, fontweight="700", color=CRITICAL)
    ax.text(gate_x + 1.0, top + 5.6,
            "stages 5 and 6 cannot lawfully begin until MahaRERA registration\nand the Certificate of Competency are both in hand",
            ha="left", va="bottom", fontsize=6.7, color=CRITICAL, linespacing=1.5)

    T.footnote(fig, "The correction against the uploaded blueprint: stages 1–4 and stages 5–6 are not sequential phases of the business — they run "
                    "concurrently from month 1, with the compliance gate as the only hard dependency. Building stages 1–4 to completion before starting "
                    "stage 5 is what turns a brokerage into an unfunded data project. Compliance basis: [SRC-001, SRC-002].")
    T.save(fig, "C1_operating_flow.png")


# ---------------------------------------------------------------- C2 -------
def fig_wbs():
    """Work breakdown structure — the whole venture decomposed to assignable packages."""
    fig = plt.figure(figsize=(11.2, 7.8))
    ax = fig.add_axes([0.012, 0.045, 0.976, 0.735]); T.blank(ax)
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    T.titleblock(fig, "Work breakdown structure — the venture decomposed to assignable packages",
                 "Six workstreams, twenty-four work packages. Each package is small enough to be finished, dated and handed over.\n"
                 "The percentage is that workstream's share of the 2,860 Year-1 founder-hours budgeted in C3.")

    hours = {k: sum(v) for k, v in E.WORKLOAD.items()}
    total = sum(hours.values())

    wbs = [
        ("compliance", [
            ("1.1", "MahaRERA agent registration", "Application, fee, documents, ID issued"),
            ("1.2", "Certificate of Competency", "20-hour programme + exam through an empanelled partner"),
            ("1.3", "Entity, tax and banking", "Structure, PAN/TAN, GST position, current account, CA engaged"),
            ("1.4", "Data governance (DPDP)", "Notice, consent, purpose limits, retention, breach drill"),
            ("1.5", "Recurring compliance calendar", "Half-yearly report, GST/TDS cycle, renewals, ad approvals"),
        ]),
        ("research", [
            ("2.1", "Corridor and pocket definition", "5 localities, 20–30 pockets, verified boundaries, frozen"),
            ("2.2", "Statutory project register", "MahaRERA extract for every in-scope project"),
            ("2.3", "Price truth engine", "Registered / asking / RR separated, with basis and n"),
            ("2.4", "Rental layer", "Rents, deposits, maintenance, restrictions, vacancy proxies"),
            ("2.5", "Infrastructure register", "Status ladder, targets, slippage, catchments"),
            ("2.6", "Risk register (geographic)", "Title, flood, CRZ, redevelopment, oversupply"),
        ]),
        ("field", [
            ("3.1", "Site visit programme", "Every project in the pocket set, physically seen"),
            ("3.2", "Broker and counterparty network", "3 reliable counterparties per locality"),
            ("3.3", "Commute and liveability audit", "3 time windows, measured not advertised"),
            ("3.4", "Negotiability log", "Ask, revised quote, incentives, last closed comparable"),
        ]),
        ("demand", [
            ("4.1", "Persona and channel map", "Who buys here, and where they can be reached"),
            ("4.2", "Referral engine", "Alumni, professional, CA/lawyer/lender, post-close ask"),
            ("4.3", "Pocket brief publishing", "Weekly one-pager, compliant artwork, tracked"),
            ("4.4", "Channel partnerships", "Co-broking terms, developer registrations"),
        ]),
        ("deal", [
            ("5.1", "Client-fit and shortlist", "Hard filters, weighted factors, ranked output"),
            ("5.2", "Visit and negotiation cycle", "Accompanied visits, offers, counters, incentives"),
            ("5.3", "Documentation and closure", "Diligence with counsel, loan, registration, handover"),
            ("5.4", "Post-close and referral", "Support, evidence capture, referral conversion"),
        ]),
        ("system", [
            ("6.1", "Schema and identifiers", "Immutable IDs, enums, required fields, versioning"),
            ("6.2", "Workbook, CRM and calculators", "One tool, used on every live lead"),
            ("6.3", "Data health and freshness", "Staleness, conflicts, coverage, confidence reporting"),
            ("6.4", "Automation and monitoring", "Change alerts on permitted sources — checks, not judgement"),
        ]),
    ]

    # two columns, three workstreams each
    layout = [(1.5, [wbs[0], wbs[1], wbs[2]]), (51.5, [wbs[3], wbs[4], wbs[5]])]
    COLW, ROWH, HEADH = 47.0, 4.9, 5.4

    for x0, group in layout:
        y = 99.0
        for key, packages in group:
            c = WS_COL[key]
            share = 100 * hours[key] / total
            ax.add_patch(FancyBboxPatch((x0, y - HEADH), COLW, HEADH,
                                        boxstyle="round,pad=0,rounding_size=0.55",
                                        fc=c, ec="none", zorder=4))
            ax.text(x0 + 1.8, y - HEADH / 2, WS_LAB[key].upper(), fontsize=7.8,
                    fontweight="700", color="white", va="center", zorder=5)
            ax.text(x0 + COLW - 12.0, y - HEADH / 2,
                    f"{hours[key] * 52 / 12:,.0f} h  ·  {len(packages)} packages",
                    fontsize=6.6, color="white", va="center", ha="right", zorder=5,
                    alpha=0.92)
            ax.text(x0 + COLW - 1.8, y - HEADH / 2, f"{share:.0f}%", fontsize=9.0,
                    fontweight="700", color="white", va="center", ha="right", zorder=5)
            y -= HEADH + 1.0
            for code, name, desc in packages:
                ax.add_patch(FancyBboxPatch((x0 + 1.5, y - ROWH + 0.5), COLW - 1.5, ROWH - 0.7,
                                            boxstyle="round,pad=0,rounding_size=0.4",
                                            fc="#f7f7f5", ec=GRID, lw=0.7, zorder=3))
                ax.add_patch(Rectangle((x0 + 1.5, y - ROWH + 0.5), 0.6, ROWH - 0.7,
                                       fc=c, ec="none", zorder=4))
                yc = y - ROWH / 2 + 0.1
                ax.text(x0 + 3.0, yc, code, fontsize=6.6, fontweight="700",
                        color=c, va="center")
                ax.text(x0 + 6.4, yc, name, fontsize=7.1, fontweight="600",
                        color=INK, va="center")
                ax.text(x0 + 24.0, yc, T.wrap(desc, 46), fontsize=6.3, color=INK2,
                        va="center", linespacing=1.35)
                y -= ROWH
            y -= 2.2

    T.footnote(fig, "Shares are computed from the Year-1 hour budget in C3, not assigned by opinion. Twenty-four packages is the point: work that cannot "
                    "be named at this granularity cannot be scheduled, cannot be dropped deliberately, and cannot be handed to a first hire.")
    T.save(fig, "C2_work_breakdown.png")


# ---------------------------------------------------------------- C3 -------
def fig_workload():
    """The hour budget: where 2,860 founder-hours go, and when the shape changes."""
    months = np.arange(1, 13)
    keys = [k for k, _, _, _ in E.WORKSTREAMS]
    data = np.array([E.WORKLOAD[k] for k in keys], dtype=float)

    fig = plt.figure(figsize=(11.2, 6.6))
    ax = fig.add_axes([0.062, 0.30, 0.60, 0.435])
    T.titleblock(fig, "The Year-1 hour budget — 55 hours a week, allocated",
                 "One founder, 55 working hours a week, 52 weeks: 2,860 hours in total. This is the whole resource.\n"
                 "The shape of the stack is the strategy: research-heavy at the start, deal-heavy by the middle, and never zero on compliance.")

    ax.stackplot(months, data, colors=[WS_COL[k] for k in keys],
                 edgecolor=SURFACE, linewidth=1.2, zorder=3)
    ax.axhline(E.FOUNDER_CAPACITY_HRS, color=INK, lw=1.2, ls=(0, (4, 3)), zorder=6)
    ax.text(1.15, 57.4, "founder capacity — 55 h/week", va="bottom", ha="left",
            fontsize=7.0, color=INK, fontweight="600")
    ax.set_xlim(1, 12); ax.set_ylim(0, 62)
    ax.set_xticks(months); ax.set_xticklabels([f"M{m}" for m in months], fontsize=8)
    ax.set_ylabel("hours per week", fontsize=8.4)
    T.clean(ax, ygrid=True)

    # phase bands
    for a, b, lab in [(1, 3, "FOUND"), (3, 6, "PROVE"), (6, 9, "SELL"), (9, 12, "SCALE")]:
        ax.plot([a, b], [59.6, 59.6], color=MUTED, lw=1.0, zorder=5,
                solid_capstyle="butt")
        ax.text((a + b) / 2, 60.4, lab, ha="center", fontsize=6.6, color=MUTED,
                fontweight="700")

    # legend + totals rail
    hours = {k: sum(E.WORKLOAD[k]) * 52 / 12 for k in keys}
    total = sum(hours.values())
    fig.text(0.688, 0.735, "YEAR-1 HOURS BY WORKSTREAM", fontsize=7.8,
             fontweight="700", color=INK, va="top")
    y = 0.695
    for k in keys:
        c = WS_COL[k]
        fig.patches.append(Rectangle((0.688, y - 0.006), 0.014, 0.020, fc=c, ec="none",
                                     transform=fig.transFigure))
        fig.text(0.712, y, WS_LAB[k], fontsize=7.4, color=INK2, va="baseline")
        fig.text(0.958, y, f"{hours[k]:,.0f} h", fontsize=7.4, color=INK, va="baseline",
                 ha="right", fontweight="600")
        fig.text(0.958, y - 0.021, f"{100*hours[k]/total:.0f}% of Year 1", fontsize=6.4,
                 color=MUTED, va="baseline", ha="right")
        y -= 0.052
    fig.text(0.688, y + 0.010, "TOTAL", fontsize=7.6, fontweight="700", color=INK, va="baseline")
    fig.text(0.958, y + 0.010, f"{total:,.0f} h", fontsize=7.6, fontweight="700",
             color=INK, va="baseline", ha="right")

    # small multiples: each workstream's own shape
    for i, k in enumerate(keys):
        axm = fig.add_axes([0.062 + i * 0.157, 0.115, 0.128, 0.115])
        axm.fill_between(months, E.WORKLOAD[k], color=WS_COL[k], alpha=0.22, zorder=2)
        axm.plot(months, E.WORKLOAD[k], color=WS_COL[k], lw=1.8, zorder=3)
        axm.set_ylim(0, 22); axm.set_xlim(1, 12)
        axm.set_xticks([1, 6, 12]); axm.set_xticklabels(["M1", "M6", "M12"], fontsize=6.2)
        axm.set_yticks([0, 10, 20]); axm.set_yticklabels(["0", "10", "20"], fontsize=6.2)
        T.clean(axm)
        axm.set_title(WS_LAB[k], fontsize=7.0, color=WS_COL[k], loc="left",
                      pad=4, fontweight="700")
    fig.text(0.012, 0.268, "THE SHAPE OF EACH WORKSTREAM  ·  hours per week", fontsize=7.6,
             fontweight="700", color=INK, va="top")

    T.footnote(fig, "A planning model [model]. Read the three lines that matter: desk research falls from 18 h to 10 h a week as the corridor is exhausted; "
                    "deal execution rises from zero to 16 h and stays there; compliance never reaches zero, and spikes again at month 12 for the half-yearly "
                    "filing and renewals [SRC-018]. Any week where deal execution is zero after month 5 is a week the plan has failed.")
    T.save(fig, "C3_workload_budget.png")


# ---------------------------------------------------------------- C4 -------
def fig_pilot_gantt():
    """The 90-day pilot, week by week, with hours attached to every line."""
    rows = E.PILOT_90
    fig = plt.figure(figsize=(11.2, 10.6))
    ax = fig.add_axes([0.215, 0.088, 0.345, 0.762])
    T.titleblock(fig, "The 90-day pilot — week by week, with hours",
                 "Twenty-four scheduled work items across twelve weeks. Every bar carries the hours it is expected to consume, so the plan can be\n"
                 "checked against a real week rather than admired. The unallocated remainder is deliberate, and it is what absorbs reality.")

    for i, (wk, ws, goal, output, gate, hrs) in enumerate(rows):
        c = WS_COL[ws]
        T.rbar(ax, wk - 0.42, i - 0.30, 0.84, 0.60, c, r=0.02)
        ax.text(wk, i, f"{hrs}h", ha="center", va="center", fontsize=6.6,
                color="white", fontweight="700", zorder=6)

    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([f"W{wk}  ·  {goal}" for wk, ws, goal, _, _, _ in rows], fontsize=7.4)
    for i, lab in enumerate(ax.get_yticklabels()):
        lab.set_color(WS_COL[rows[i][1]])
        lab.set_fontweight("600")
    ax.invert_yaxis()
    ax.set_xlim(0.4, 12.6); ax.set_ylim(len(rows) - 0.4, -0.7)
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels([f"W{i}" for i in range(1, 13)], fontsize=7.6)
    ax.xaxis.set_ticks_position("top")
    ax.xaxis.set_label_position("top")
    T.clean(ax, ygrid=False, xgrid=True, bottom=False)
    ax.spines["bottom"].set_visible(False)

    # compliance gate marker
    ax.axvspan(5.55, 6.45, color=CRITICAL, alpha=0.07, zorder=1)
    ax.plot([6.0, 6.0], [-0.7, len(rows) - 0.4], color=CRITICAL, lw=1.2,
            ls=(0, (4, 3)), zorder=2)

    # output column
    y_top, y_bot = 0.850, 0.088
    n = len(rows)
    for i, (wk, ws, goal, output, gate, hrs) in enumerate(rows):
        yc = y_top - (i + 0.5) * (y_top - y_bot) / n
        out = T.wrap(output, 96)
        nl = out.count("\n")
        fig.text(0.578, yc + 0.0042 + 0.0034 * nl, out, fontsize=6.5, color=INK2,
                 va="center", linespacing=1.45)
        fig.text(0.578, yc - 0.0088 - 0.0034 * nl, "→  " + T.wrap(gate, 92),
                 fontsize=6.3, color=WS_COL[ws], va="center", linespacing=1.45)
    fig.text(0.578, 0.862, "OUTPUT   ·   →  GATE", fontsize=7.2, fontweight="700",
             color=INK, va="bottom")

    handles = [plt.Line2D([], [], marker="s", ls="", color=WS_COL[k], ms=7, label=WS_LAB[k])
               for k, _, _, _ in E.WORKSTREAMS]
    fig.legend(handles=handles, loc="lower left", bbox_to_anchor=(0.012, 0.885),
               fontsize=7.4, ncol=6, handletextpad=0.5, columnspacing=1.6)

    fig.text(0.012, 0.038, "COMPLIANCE GATE at week 6", fontsize=7.0,
             fontweight="700", color=CRITICAL, va="top")
    fig.text(0.012, 0.023,
             T.wrap("No advertisement, listing, WhatsApp brief or client engagement may precede it. "
                    "Weeks 1–5 are research and preparation only. This is the single hardest constraint in the plan and the "
                    "one most likely to be rationalised away.", 40),
             fontsize=6.4, color=INK2, va="top", linespacing=1.5)

    T.save(fig, "C4_pilot_90_day.png")


# ---------------------------------------------------------------- C5 -------
def fig_gantt_12m():
    """The 12-month schedule, with the gate that ends each workstream."""
    rows = E.GANTT
    fig = plt.figure(figsize=(11.2, 6.4))
    ax = fig.add_axes([0.235, 0.115, 0.335, 0.635])
    T.titleblock(fig, "Twelve-month schedule — every bar ends at a gate, not a date",
                 "A date is a hope; a gate is a test. Each workstream closes when its gate is satisfied, and the workstreams that follow it\n"
                 "are not permitted to start early to make the chart look busy.")

    for i, (label, ws, s, e, gate) in enumerate(rows):
        c = WS_COL[ws]
        T.rbar(ax, s - 0.5, i - 0.28, (e - s) + 1.0, 0.56, c, r=0.05)
        ax.scatter([e + 0.5], [i], marker="D", s=26, color=INK, zorder=6,
                   edgecolor=SURFACE, linewidth=1.0)

    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r[0] for r in rows], fontsize=7.6)
    for i, lab in enumerate(ax.get_yticklabels()):
        lab.set_color(WS_COL[rows[i][1]])
        lab.set_fontweight("600")
    ax.invert_yaxis()
    ax.set_xlim(0.3, 12.9); ax.set_ylim(len(rows) - 0.4, -0.8)
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels([f"M{i}" for i in range(1, 13)], fontsize=7.2)
    ax.xaxis.set_ticks_position("top")
    T.clean(ax, ygrid=False, xgrid=True, bottom=False)
    ax.spines["bottom"].set_visible(False)

    for m, lab, c in [(3, "DAY 90 GATE", CRITICAL), (6, "MONTH 6", MUTED), (9, "MONTH 9", MUTED)]:
        ax.axvline(m + 0.5, color=c, lw=1.1, ls=(0, (4, 3)), zorder=2,
                   alpha=1.0 if c == CRITICAL else 0.6)

    y_top, y_bot = 0.750, 0.115
    n = len(rows)
    for i, (label, ws, s, e, gate) in enumerate(rows):
        yc = y_top - (i + 0.5) * (y_top - y_bot) / n
        fig.text(0.585, yc, "◆ " + T.wrap(gate, 82), fontsize=6.5, color=INK2,
                 va="center", linespacing=1.4)
    fig.text(0.585, 0.762, "◆  THE GATE THAT CLOSES THIS WORKSTREAM", fontsize=7.0,
             fontweight="700", color=INK, va="bottom")

    handles = [plt.Line2D([], [], marker="s", ls="", color=WS_COL[k], ms=7, label=WS_LAB[k])
               for k, _, _, _ in E.WORKSTREAMS]
    fig.legend(handles=handles, loc="lower left", bbox_to_anchor=(0.012, 0.785),
               fontsize=7.4, ncol=6, handletextpad=0.5, columnspacing=1.6)

    T.footnote(fig, "Diamonds mark the gate, not the deadline. Expansion into corridor 2 begins at month 8 only if the corridor-1 economics have repeated; "
                    "if they have not, months 8–12 are spent making corridor 1 work rather than adding a second place to be mediocre.")
    T.save(fig, "C5_gantt_12_month.png")


# ---------------------------------------------------------------- C6 -------
def fig_weekly_rhythm():
    """What a week actually looks like once the desk is running."""
    fig = plt.figure(figsize=(11.2, 6.2))
    ax = fig.add_axes([0.075, 0.085, 0.60, 0.655])
    T.titleblock(fig, "The operating week — month 6 onwards",
                 "The plan has to survive contact with a calendar. This is one steady-state week: 55 committed hours, with the blocks that\n"
                 "produce revenue protected from the blocks that merely feel productive.")

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    # (day index, start hour, duration, workstream, label)
    blocks = [
        (0, 9, 3, "research", "Registered-price\nsweep (IGR)"),
        (0, 13, 3, "demand", "Referral &\nchannel calls"),
        (0, 17, 2, "deal", "Client follow-up"),
        (1, 9, 4, "field", "Site visits —\npocket A"),
        (1, 14, 3, "deal", "Accompanied\nclient visits"),
        (1, 18, 1.5, "system", "CRM update"),
        (2, 9, 3, "research", "MahaRERA &\nproject register"),
        (2, 13, 3, "deal", "Negotiation /\ndocumentation"),
        (2, 17, 2, "demand", "Pocket brief\nwriting"),
        (3, 9, 4, "field", "Site visits —\npocket B"),
        (3, 14, 3, "deal", "Offers &\ncounterparties"),
        (3, 18, 1.5, "system", "CRM update"),
        (4, 9, 3, "research", "Infra, risk &\nrental refresh"),
        (4, 13, 3, "demand", "Brief send-out\n& inbound"),
        (4, 17, 2, "compliance", "Books, filings,\nevidence"),
        (5, 10, 5, "deal", "Client site visits\n— highest-conversion\nslot of the week"),
        (5, 16, 2, "field", "Broker network"),
        (6, 10, 3, "system", "Data health, conflicts,\nweekly review"),
    ]
    ax.set_xlim(-0.5, 6.5); ax.set_ylim(20.5, 8.5)
    for d in range(7):
        ax.axvspan(d - 0.44, d + 0.44, color="#f6f6f4" if d < 5 else "#f1f4f8",
                   zorder=0, lw=0)
    for b in blocks:
        d, s, dur, ws, lab = b
        c = WS_COL[ws]
        ax.add_patch(FancyBboxPatch((d - 0.42, s), 0.84, dur,
                                    boxstyle="round,pad=0,rounding_size=0.05",
                                    fc=c, ec=SURFACE, lw=1.4, zorder=3))
        ax.text(d, s + dur / 2, lab, ha="center", va="center", fontsize=6.2,
                color="white", fontweight="600", linespacing=1.4, zorder=4)
    ax.set_xticks(range(7)); ax.set_xticklabels(days, fontsize=8.4)
    ax.xaxis.set_ticks_position("top")
    ax.set_yticks(range(9, 21, 2))
    ax.set_yticklabels([f"{h:02d}:00" for h in range(9, 21, 2)], fontsize=7.2)
    T.clean(ax, ygrid=False, xgrid=False, bottom=False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.tick_params(length=0)

    # rail
    tot = {}
    for d, s, dur, ws, lab in blocks:
        tot[ws] = tot.get(ws, 0) + dur
    fig.text(0.700, 0.742, "COMMITTED HOURS THIS WEEK", fontsize=7.8, fontweight="700",
             color=INK, va="top")
    y = 0.700
    for k, _, _, _ in E.WORKSTREAMS:
        v = tot.get(k, 0)
        fig.patches.append(Rectangle((0.700, y - 0.005), 0.013, 0.019, fc=WS_COL[k],
                                     ec="none", transform=fig.transFigure))
        fig.text(0.722, y, WS_LAB[k], fontsize=7.2, color=INK2, va="baseline")
        fig.text(0.900, y, f"{v:.1f} h", fontsize=7.2, color=INK, va="baseline",
                 ha="right", fontweight="600")
        y -= 0.036
    fig.text(0.700, y, "Scheduled", fontsize=7.4, fontweight="700", color=INK, va="baseline")
    fig.text(0.900, y, f"{sum(tot.values()):.1f} h", fontsize=7.4, fontweight="700",
             color=INK, va="baseline", ha="right")
    y -= 0.036
    fig.text(0.700, y, "Unscheduled reserve", fontsize=7.4, fontweight="700",
             color=ORANGE, va="baseline")
    fig.text(0.900, y, f"{55 - sum(tot.values()):.1f} h", fontsize=7.4, fontweight="700",
             color=ORANGE, va="baseline", ha="right")

    fig.text(0.700, y - 0.055,
             T.wrap("The reserve is not slack. Mumbai traffic, a seller who reschedules, a bank that "
                    "wants one more document, a client who calls at 21:00 — these consume it every "
                    "single week. A plan that schedules 55 of 55 hours fails in week one.", 44),
             fontsize=6.6, color=INK2, va="top", linespacing=1.65)
    fig.text(0.700, y - 0.185,
             T.wrap("Saturday is not optional. It is the highest-conversion slot in Indian residential "
                    "real estate, because it is when both spouses can see a flat together.", 44),
             fontsize=6.6, color=INK2, va="top", linespacing=1.65, fontweight="500")

    T.footnote(fig, "An illustrative steady-state week [model]. The structural rules it encodes are the transferable part: site visits are batched by pocket "
                    "to cut travel; deal work is never scheduled after research on the same day, because research expands to fill whatever it is given; and "
                    "the CRM is updated the same day, twice a week, or it is not updated at all.")
    T.save(fig, "C6_operating_week.png")


# ---------------------------------------------------------------- C7 -------
def fig_decision_gates():
    """Day 30 / 60 / 90 and the month-8 expansion gate, as a decision flow."""
    fig = plt.figure(figsize=(11.2, 7.5))
    ax = fig.add_axes([0.012, 0.045, 0.976, 0.760]); T.blank(ax)
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    T.titleblock(fig, "Decision gates — the four moments the plan is allowed to change",
                 "Each gate has a written test, a pass route and a fail route. The fail routes are the important half: a plan without a\n"
                 "defined way to stop is a plan that will be continued past the point of evidence.")

    gates = [
        ("DAY 30", 8, BLUE,
         ["MahaRERA application filed", "Certificate programme booked", "Schema v1 frozen",
          "Corridor and 20–30 pockets locked"],
         "PASS → proceed to field",
         "FAIL → do not start field work. The\nresearch unit is undefined; fix that first."),
        ("DAY 60", 31, AQUA,
         ["≥80% source completeness", "≥3 field inputs per locality", "Client-fit model runs end to end",
          "Certificate of Competency issued"],
         "PASS → switch on the lead engine",
         "FAIL → hold marketing. Publishing on\nthin data destroys the only asset you have."),
        ("DAY 90", 54, ORANGE,
         ["30+ qualified leads, tagged by source", "5+ site-visit cycles run",
          "First closure or evidenced pipeline", "Objections and gaps written down"],
         "PASS → deepen, do not widen",
         "FAIL → change the corridor or the offer.\nDo not add geography to fix conversion."),
        ("MONTH 8", 77, VIOLET,
         ["Corridor-1 economics repeat", "Closures without founder at every step",
          "Referral coefficient > 0.5", "12 months of runway intact"],
         "PASS → open corridor 2",
         "FAIL → stay. A second mediocre corridor\ncosts twice and proves nothing."),
    ]

    for name, x, c, tests, ok, no in gates:
        ax.add_patch(FancyBboxPatch((x, 46), 20, 46,
                                    boxstyle="round,pad=0,rounding_size=0.8",
                                    fc=SURFACE, ec=c, lw=1.6, zorder=3))
        ax.add_patch(FancyBboxPatch((x, 84.6), 20, 7.4,
                                    boxstyle="round,pad=0,rounding_size=0.8",
                                    fc=c, ec="none", zorder=4))
        ax.add_patch(Rectangle((x, 84.6), 20, 1.2, fc=c, ec="none", zorder=4))
        ax.text(x + 10, 88.3, name, ha="center", va="center", fontsize=9.2,
                fontweight="700", color="white", zorder=5)
        yy = 81.0
        for t in tests:
            wrapped = T.wrap(t, 26)
            ax.add_patch(Rectangle((x + 1.5, yy - 2.2), 1.5, 1.5, fc="none",
                                   ec=c, lw=0.9, zorder=5))
            ax.text(x + 4.0, yy - 1.4, wrapped, fontsize=6.8, color=INK2, va="top",
                    zorder=5, linespacing=1.45)
            yy -= 4.6 * (1 + wrapped.count("\n"))

        # pass
        T.arrow(ax, (x + 10, 45.5), (x + 10, 40.5), color=GOOD, lw=1.6, ms=8)
        ax.add_patch(FancyBboxPatch((x, 31.5), 20, 8.6,
                                    boxstyle="round,pad=0,rounding_size=0.6",
                                    fc="#eaf7ea", ec=GOOD, lw=1.1, zorder=3))
        ax.text(x + 10, 35.8, ok, ha="center", va="center", fontsize=7.2,
                fontweight="700", color="#0a7a0a", zorder=5)
        # fail
        T.arrow(ax, (x + 10, 31.0), (x + 10, 26.0), color=CRITICAL, lw=1.6, ms=8)
        ax.add_patch(FancyBboxPatch((x, 12.0), 20, 13,
                                    boxstyle="round,pad=0,rounding_size=0.6",
                                    fc="#fdeeee", ec=CRITICAL, lw=1.1, zorder=3))
        ax.text(x + 10, 22.2, "IF NOT", ha="center", va="center", fontsize=6.8,
                fontweight="700", color=CRITICAL, zorder=5)
        ax.text(x + 10, 17.0, no, ha="center", va="center", fontsize=6.6,
                color=INK2, zorder=5, linespacing=1.55)
        if x < 70:
            T.arrow(ax, (x + 20.4, 69), (x + 22.6, 69), color=BASELINE, lw=1.4, ms=7)

    ax.add_patch(FancyBboxPatch((8, 0.5), 89, 9.5,
                                boxstyle="round,pad=0,rounding_size=0.8",
                                fc="#f4f7fc", ec=BLUE_RAMP[1], lw=1.0, zorder=3))
    ax.text(52.5, 8.2, "THE QUESTION AT EVERY GATE", ha="center", fontsize=7.6,
            fontweight="700", color=BLUE_RAMP[10])
    ax.text(52.5, 4.2,
            "Not \"how much of Mumbai is in the database?\" but: does deeper intelligence produce better client trust, faster shortlists,\n"
            "more site visits, stronger negotiation and a repeatable route to revenue? If the honest answer is no, the database is a hobby.",
            ha="center", va="center", fontsize=7.6, color=INK, linespacing=1.6)

    T.footnote(fig, "Gate tests are management targets [model], not market statistics. Write the date and the answer against every checkbox — a gate that "
                    "is assessed from memory is a gate that always passes.")
    T.save(fig, "C7_decision_gates.png")


if __name__ == "__main__":
    T.apply()
    for f in [fig_operating_flow, fig_wbs, fig_workload, fig_pilot_gantt,
              fig_gantt_12m, fig_weekly_rhythm, fig_decision_gates]:
        f(); print("ok", f.__name__)
