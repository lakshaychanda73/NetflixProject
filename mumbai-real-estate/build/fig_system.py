"""fig_system.py — Part E: data architecture, provenance and compliance."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Polygon, Circle
import theme as T
from theme import (SURFACE, INK, INK2, MUTED, GRID, BASELINE, BLUE, ORANGE, AQUA,
                   YELLOW, MAGENTA, GREEN, VIOLET, RED, GOOD, WARN, SERIOUS, CRITICAL,
                   SEQ_BLUE, BLUE_RAMP)
import evidence as E


# ---------------------------------------------------------------- E1 -------
def fig_geo_hierarchy():
    """L0-L6 — and the two levels that actually matter."""
    fig = plt.figure(figsize=(11.2, 6.2))
    ax = fig.add_axes([0.012, 0.145, 0.976, 0.625]); T.blank(ax)
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    T.titleblock(fig, "Geographic hierarchy — seven levels, two that matter",
                 "The uploaded blueprint's L0–L6 structure is kept unchanged; it is correct. What is added is the explicit statement of which\n"
                 "level is the research unit and which is the closure unit, because everything else exists only to serve those two.")

    levels = E.GEO_LEVELS
    for i, (code, name, example, role) in enumerate(levels):
        y = 92 - i * 13.0
        primary = code in ("L4", "L6")
        c = BLUE if code == "L4" else (ORANGE if code == "L6" else BLUE_RAMP[max(1, 6 - i)])
        indent = 3 + i * 4.0
        w = 88 - i * 4.0
        ax.add_patch(FancyBboxPatch((indent, y - 10.2), w, 10.2,
                                    boxstyle="round,pad=0,rounding_size=0.6",
                                    fc=c if primary else "none",
                                    ec=c, lw=1.8 if primary else 1.1, zorder=3))
        if not primary:
            ax.add_patch(FancyBboxPatch((indent, y - 10.2), w, 10.2,
                                        boxstyle="round,pad=0,rounding_size=0.6",
                                        fc=c, ec="none", alpha=0.10, zorder=2))
        tc = "white" if primary else INK
        ax.text(indent + 2.2, y - 3.4, code, fontsize=9.2, fontweight="700",
                color=tc, va="center")
        ax.text(indent + 7.6, y - 3.4, name, fontsize=8.4,
                fontweight="700" if primary else "600", color=tc, va="center")
        ax.text(indent + 2.2, y - 7.6, f"e.g.  {example}", fontsize=7.0,
                color="white" if primary else INK2, va="center",
                alpha=0.9 if primary else 1.0)
        ax.text(indent + w - 2.2, y - 5.1, role, fontsize=7.6 if primary else 7.0,
                fontweight="700" if primary else "400",
                color=tc, va="center", ha="right", alpha=0.95)

    T.footnote(fig, "Two rules follow from this structure and are enforced in the schema. First, no fact may exist without a geo_id — a price that belongs "
                    "to 'Powai' generally, rather than to a named pocket, is not usable evidence. Second, aggregation only ever runs upward: an L4 pocket "
                    "figure is built from L5 and L6 observations and never inherited downward from an L3 locality average. Inheriting downward is how a "
                    "₹28,000/sq ft locality average ends up quoted for a ground-floor flat facing a nullah.")
    T.save(fig, "E1_geo_hierarchy.png")


# ---------------------------------------------------------------- E2 -------
def fig_data_domains():
    """The twelve domains, their minimum fields, and how fast each goes stale."""
    doms = E.DOMAINS
    fig = plt.figure(figsize=(11.2, 7.4))
    ax = fig.add_axes([0.232, 0.105, 0.080, 0.655])
    T.titleblock(fig, "Data domains — minimum fields and staleness rules",
                 "Twelve domains, each with the fields that must exist before a record is accepted and the number of days after which the system\n"
                 "marks that record stale on every client-facing screen. The red domains are where the work never stops.")

    ax.set_xlim(0, 1); ax.set_ylim(len(doms) - 0.5, -0.5)
    T.blank(ax)
    for i, d in enumerate(doms):
        v = d[3]
        c = CRITICAL if v <= 14 else (WARN if v <= 45 else (AQUA if v <= 90 else BLUE_RAMP[4]))
        ax.add_patch(FancyBboxPatch((0.06, i - 0.26), 0.88, 0.52,
                                    boxstyle="round,pad=0,rounding_size=0.10",
                                    fc=c, ec="none"))
        ax.text(0.50, i, f"{v} d", ha="center", va="center", fontsize=7.6,
                color="white", fontweight="700")
    fig.text(0.272, 0.772, "STALE AFTER", fontsize=7.2, fontweight="700",
             color=INK, va="bottom", ha="center")

    y_top, y_bot = 0.760, 0.105
    n = len(doms)
    fig.text(0.330, 0.772, "PHASE-1 MINIMUM FIELDS", fontsize=7.2, fontweight="700",
             color=INK, va="bottom")
    fig.text(0.742, 0.772, "PRIMARY SOURCES", fontsize=7.2, fontweight="700",
             color=INK, va="bottom")
    fig.text(0.892, 0.772, "REFRESH", fontsize=7.2, fontweight="700",
             color=INK, va="bottom")
    for i, (name, fields, refresh, stale_days, sources, gran) in enumerate(doms):
        yc = y_top - (i + 0.5) * (y_top - y_bot) / n
        fig.text(0.222, yc, name, fontsize=8.0, fontweight="600", color=INK,
                 va="center", ha="right")
        fig.text(0.330, yc + 0.006, T.wrap(fields, 82), fontsize=6.2, color=INK2,
                 va="center", linespacing=1.4)
        fig.text(0.330, yc - 0.014, f"granularity: {gran}", fontsize=5.9,
                 color=MUTED, va="center")
        fig.text(0.742, yc, T.wrap(sources, 26), fontsize=6.2, color=INK2,
                 va="center", linespacing=1.4)
        fig.text(0.892, yc, T.wrap(refresh, 20), fontsize=6.2, color=INK2,
                 va="center", linespacing=1.4)

    T.footnote(fig, "The four fields the uploaded blueprint did not carry, and which this schema makes mandatory on every record: sample_size, observed_date, "
                    "stale_after_days and conflict_flag. Together they answer the only question that matters when a client challenges a number — where did "
                    "this come from, when was it true, how many observations support it, and what still disagrees with it?")
    T.save(fig, "E2_data_domains.png")


# ---------------------------------------------------------------- E3 -------
def fig_source_stack():
    """Which sources establish truth, which give speed, and which are lawful to take."""
    fig = plt.figure(figsize=(11.2, 6.9))
    ax = fig.add_axes([0.012, 0.055, 0.50, 0.715]); T.blank(ax)
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    T.titleblock(fig, "The source stack — truth at the bottom, speed at the top",
                 "Sources are not interchangeable. The statutory layer is slow and authoritative; the observation layer is fast and\n"
                 "unreliable; the proprietary layer is the only one a competitor cannot also buy.")

    tiers = [
        ("PROPRIETARY", ORANGE, 78, 96, 62,
         ["Own closed deals & prices", "Client objections & lost reasons", "Field observations"],
         "Real time", "Unmatchable — and it only exists if you capture it"),
        ("HIGH-FREQUENCY SIGNAL", YELLOW, 58, 76, 76,
         ["Portal asking prices", "Listing age & churn", "Developer price sheets"],
         "Daily / weekly", "Fast, noisy, duplicated — never a statement of fact"),
        ("INSTITUTIONAL CONTEXT", AQUA, 38, 56, 88,
         ["Knight Frank / CBRE / ANAROCK", "Absorption, QTS, launches", "Office & rental context"],
         "Quarter / half-year", "Authoritative at city and zone level; silent below it"),
        ("STATUTORY TRUTH", BLUE, 6, 36, 98,
         ["MahaRERA project & agent registry", "IGR registered instruments & RR", "MMRDA / BMC / CIDCO records"],
         "Monthly / on change", "The floor under every number you will ever defend"),
    ]
    for name, c, y0, y1, w, items, refresh, note in tiers:
        x0 = 50 - w / 2
        ax.add_patch(FancyBboxPatch((x0, y0), w, y1 - y0,
                                    boxstyle="round,pad=0,rounding_size=0.7",
                                    fc=c, ec="none", alpha=0.13, zorder=2))
        ax.add_patch(FancyBboxPatch((x0, y0), w, y1 - y0,
                                    boxstyle="round,pad=0,rounding_size=0.7",
                                    fc="none", ec=c, lw=1.5, zorder=3))
        ax.text(x0 + 2.4, y1 - 3.6, name, fontsize=8.2, fontweight="700", color=c, va="center")
        ax.text(x0 + w - 2.4, y1 - 3.6, refresh, fontsize=6.8, color=MUTED,
                va="center", ha="right")
        ax.text(x0 + 2.4, y1 - 8.6, "  ·  ".join(items), fontsize=6.7, color=INK2, va="center")
        ax.text(x0 + 2.4, y1 - 13.4, note, fontsize=6.6, color=c, va="center",
                style="italic", fontweight="600")

    ax.annotate("", xy=(3.0, 6), xytext=(3.0, 96),
                arrowprops=dict(arrowstyle="-|>,head_width=0.28,head_length=0.5",
                                color=BASELINE, lw=1.3))
    ax.text(1.2, 51, "I N C R E A S I N G   S P E E D", rotation=90, ha="center",
            va="center", fontsize=6.4, color=MUTED, fontweight="600")
    ax.annotate("", xy=(97, 96), xytext=(97, 6),
                arrowprops=dict(arrowstyle="-|>,head_width=0.28,head_length=0.5",
                                color=BASELINE, lw=1.3))
    ax.text(98.8, 51, "I N C R E A S I N G   A U T H O R I T Y", rotation=90, ha="center",
            va="center", fontsize=6.4, color=MUTED, fontweight="600")

    # acquisition legality rail
    fig.text(0.545, 0.755, "HOW EACH SOURCE MAY LAWFULLY BE TAKEN", fontsize=8.0,
             fontweight="700", color=INK, va="top")
    rules = [
        ("Government portals — MahaRERA, IGR, MMRDA, BMC", GOOD,
         "Published for public use. IGR e-Search is free and covers Mumbai from 1985, "
         "but results are explicitly uncertified — for a contested fact, obtain the certified copy."),
        ("Institutional research reports", GOOD,
         "Cite and attribute. Do not republish tables wholesale, and never present a "
         "consultancy's city-level figure as if it described your pocket."),
        ("Property portals", WARN,
         "Terms of use are enforceable as contract in India, and clickwrap acceptance binds you. "
         "Collect manually or through a permitted feed or API. Do not build the business on a "
         "scraper you would not describe to the portal."),
        ("Anything containing personal data", CRITICAL,
         "The DPDP Rules were notified in November 2025 and phase in to roughly mid-May 2027. "
         "Consent obligations extend to personal data that is already public. There is no "
         "small-business exemption and penalties reach ₹250 crore."),
        ("Your own field notes and closed deals", GOOD,
         "Yours outright, and the only category that is. This is the argument for capturing "
         "every observation the moment it happens."),
    ]
    y = 0.715
    for head, c, body in rules:
        h = T.wrap(head, 56)
        b = T.wrap(body, 74)
        fig.patches.append(Rectangle((0.545, y - 0.020), 0.004, 0.024, fc=c, ec="none",
                                     transform=fig.transFigure))
        fig.text(0.557, y, h, fontsize=7.2, fontweight="700", color=INK,
                 va="top", linespacing=1.45)
        y -= 0.0175 * (1 + h.count("\n")) + 0.009
        fig.text(0.557, y, b, fontsize=6.5, color=INK2, va="top", linespacing=1.7)
        y -= 0.0178 * (1 + b.count("\n")) + 0.030

    T.footnote(fig, "Acquisition positions are practical guidance, not legal advice [SRC-015, SRC-023, SRC-030]. The operating rule that follows: the "
                    "statutory layer establishes what is true, the signal layer establishes what is currently being asked, and only the proprietary layer "
                    "establishes what actually closed. Confusing the three is the most expensive mistake in this business.")
    T.save(fig, "E3_source_stack.png")


# ---------------------------------------------------------------- E4 -------
def fig_compliance_path():
    """The compliance critical path and the recurring calendar."""
    fig = plt.figure(figsize=(11.2, 7.8))
    T.titleblock(fig, "Compliance — the critical path, then the calendar that never stops",
                 "The Certificate of Competency became mandatory in January 2026 and it is the longest-lead item in the entire venture.\n"
                 "Nothing that looks like marketing may happen before it is issued, and the obligations do not end when it is.")

    ax = fig.add_axes([0.012, 0.505, 0.976, 0.245]); T.blank(ax)
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    path = [
        ("Week 1", "Apply for MahaRERA\nagent registration", BLUE, "₹10,000 individual\n₹1,00,000 firm"),
        ("Week 1", "Book the 20-hour\ncertification programme", VIOLET, "NAREDCO / REMI / RAGC\n₹5,000–8,000"),
        ("Weeks 2–5", "Complete training\nand pass the exam", VIOLET, "100 marks, 50% to pass\nexam ₹1,500–1,800"),
        ("Week 5", "Certificate of\nCompetency issued", GOOD, "Valid 5 years"),
        ("Week 6", "MahaRERA number live\nQR artwork prepared", GOOD, "Top-right on every ad\n₹10k–50k per violation"),
        ("Week 6+", "Marketing and client\nengagement may begin", ORANGE, "The gate opens here"),
    ]
    bw, gp = 14.6, 2.4
    for i, (when, what, c, cost) in enumerate(path):
        x = 1.5 + i * (bw + gp)
        ax.add_patch(FancyBboxPatch((x, 16), bw, 68,
                                    boxstyle="round,pad=0,rounding_size=1.2",
                                    fc=SURFACE, ec=c, lw=1.5, zorder=3))
        ax.add_patch(FancyBboxPatch((x, 68), bw, 16,
                                    boxstyle="round,pad=0,rounding_size=1.2",
                                    fc=c, ec="none", zorder=4))
        ax.add_patch(Rectangle((x, 68), bw, 3, fc=c, ec="none", zorder=4))
        ax.text(x + bw / 2, 76, when, ha="center", va="center", fontsize=8.0,
                fontweight="700", color="white", zorder=5)
        ax.text(x + bw / 2, 52, what, ha="center", va="center", fontsize=7.4,
                color=INK, fontweight="600", linespacing=1.5, zorder=5)
        ax.text(x + bw / 2, 26, cost, ha="center", va="center", fontsize=6.4,
                color=MUTED, linespacing=1.5, zorder=5)
        if i < len(path) - 1:
            T.arrow(ax, (x + bw + 0.2, 50), (x + bw + gp - 0.2, 50),
                    color=BASELINE, lw=1.4, ms=7)
    fig.text(0.012, 0.762, "CRITICAL PATH  ·  roughly six weeks, and it cannot be compressed by working harder",
             fontsize=7.6, fontweight="700", color=INK, va="bottom")

    # recurring calendar heatmap
    obligations = [
        ("MahaRERA half-yearly report", [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0]),
        ("GST returns", [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),
        ("TDS reconciliation (26AS / AIS)", [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]),
        ("Advance tax instalment", [0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2]),
        ("Income-tax return", [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0]),
        ("Books & client-file review", [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
        ("Advertisement QR / disclosure audit", [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]),
        ("DPDP consent & retention review", [0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0]),
        ("Registration / certificate renewal", [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),
    ]
    ax2 = fig.add_axes([0.255, 0.115, 0.565, 0.285])
    M = np.array([o[1] for o in obligations], dtype=float)
    im = ax2.imshow(M, cmap=SEQ_BLUE, vmin=0, vmax=3.4, aspect="auto")
    months = ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar"]
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if M[i, j] > 0:
                ax2.text(j, i, ["", "•", "▲", "★"][int(M[i, j])], ha="center", va="center",
                         fontsize=8 if M[i, j] < 3 else 9,
                         color="white" if M[i, j] >= 2 else INK)
    ax2.set_xticks(range(12)); ax2.set_xticklabels(months, fontsize=7.4)
    ax2.set_yticks(range(len(obligations)))
    ax2.set_yticklabels([o[0] for o in obligations], fontsize=7.4)
    ax2.tick_params(length=0)
    for s in ax2.spines.values():
        s.set_visible(False)
    ax2.set_xticks(np.arange(-0.5, 12, 1), minor=True)
    ax2.set_yticks(np.arange(-0.5, len(obligations), 1), minor=True)
    ax2.grid(which="minor", color=SURFACE, linewidth=2.2)
    ax2.tick_params(which="minor", length=0)
    ax2.xaxis.set_ticks_position("top")
    fig.text(0.255, 0.425, "THE RECURRING CALENDAR  ·  Indian financial year, April to March",
             fontsize=7.6, fontweight="700", color=INK, va="bottom")
    fig.text(0.833, 0.395,
             "★   major filing\n▲   statutory deadline\n•   routine discipline",
             fontsize=7.0, color=INK2, va="top", linespacing=2.0)
    fig.text(0.833, 0.285,
             T.wrap("Every one of these is a diary entry with a named owner and an evidence "
                    "file, from week 1. Compliance discovered in month 9 is compliance "
                    "already breached.", 30),
             fontsize=6.6, color=MUTED, va="top", linespacing=1.7)

    T.footnote(fig, "Registration and certification [SRC-001, SRC-002, SRC-003]; advertisement QR and disclosure [SRC-017]; half-yearly agent reporting "
                    "[SRC-018]; GST registration threshold and rate [SRC-011, SRC-012]; TDS under sections 194-IA and 194H [SRC-024]; DPDP obligations "
                    "[SRC-023]. Timing is indicative and statutory dates change — confirm each with a CA and re-verify against the source before relying on it.")
    T.save(fig, "E4_compliance_path.png")


# ---------------------------------------------------------------- E5 -------
def fig_client_fit():
    """The client-fit engine as a decision flow: hard filters, then weights."""
    fig = plt.figure(figsize=(11.2, 6.8))
    ax = fig.add_axes([0.012, 0.055, 0.976, 0.715]); T.blank(ax)
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    T.titleblock(fig, "The client-fit engine — hard filters first, weights second",
                 "A shortlist is produced by elimination, not by scoring. Anything that fails a hard filter is removed and never re-ranked back in;\n"
                 "only what survives is scored. Reversing that order is how a broker talks a client into a flat they cannot legally or financially hold.")

    ax.add_patch(FancyBboxPatch((2, 82), 15, 14,
                                boxstyle="round,pad=0,rounding_size=0.8",
                                fc=BLUE_RAMP[1], ec="none", zorder=3))
    ax.text(9.5, 91.6, "ALL INVENTORY", ha="center", fontsize=7.6, fontweight="700",
            color=BLUE_RAMP[11])
    ax.text(9.5, 86.4, "in the pocket set", ha="center", fontsize=6.6, color=INK2)

    hard = [
        ("All-in budget", "Includes stamp duty (6% male / 5% female sole owner),\n1% registration capped at ₹30,000, brokerage and deposits"),
        ("Carpet area & configuration", "Carpet only — never built-up or saleable"),
        ("Possession horizon", "Ready versus under construction, against the client's actual move date"),
        ("Legal / title / RERA status", "Unresolved high-risk flags eliminate, they do not discount"),
        ("Commute ceiling", "Measured door-to-door in the client's own travel window"),
    ]
    y = 78
    for i, (name, why) in enumerate(hard):
        ax.add_patch(FancyBboxPatch((22, y - 9.4), 44, 9.4,
                                    boxstyle="round,pad=0,rounding_size=0.6",
                                    fc=SURFACE, ec=CRITICAL, lw=1.2, zorder=3))
        ax.add_patch(Rectangle((22, y - 9.4), 0.8, 9.4, fc=CRITICAL, ec="none", zorder=4))
        ax.text(24.2, y - 3.2, name, fontsize=7.6, fontweight="700", color=INK, va="center")
        ax.text(24.2, y - 7.0, why, fontsize=6.3, color=INK2, va="center", linespacing=1.45)
        T.arrow(ax, (66.4, y - 4.7), (70.5, y - 4.7), color=CRITICAL, lw=1.1, ms=6)
        ax.text(71.4, y - 4.7, "eliminated", fontsize=6.4, color=CRITICAL, va="center",
                style="italic")
        if i == 0:
            T.arrow(ax, (17.4, 89), (21.6, 76), color=BASELINE, lw=1.3, ms=7, rad=-0.15)
        y -= 11.6

    ax.text(22, 81.6, "HARD FILTERS  ·  fail one, and the unit is out", fontsize=7.4,
            fontweight="700", color=CRITICAL, va="bottom")

    # weighted layer
    ax.add_patch(FancyBboxPatch((22, 3), 44, 14.5,
                                boxstyle="round,pad=0,rounding_size=0.8",
                                fc=BLUE, ec="none", zorder=3))
    ax.text(44, 13.6, "WHAT SURVIVES IS THEN SCORED, NOT BEFORE", ha="center",
            fontsize=7.4, fontweight="700", color="white")
    ax.text(44, 7.4,
            "Net rental yield  ·  liquidity and days-on-market  ·  infrastructure by status weight\n"
            "society and lifestyle fit  ·  maintenance burden  ·  negotiability and discount-to-close",
            ha="center", fontsize=6.7, color="white", linespacing=1.7, alpha=0.95)
    T.arrow(ax, (44, 20.5), (44, 18.2), color=BLUE, lw=1.6, ms=8)

    # right rail
    ax.add_patch(FancyBboxPatch((70, 24), 28, 54,
                                boxstyle="round,pad=0,rounding_size=0.8",
                                fc="#f4f7fc", ec=BLUE_RAMP[1], lw=1.0, zorder=3))
    ax.text(72.2, 74.4, "THE ALL-IN COST A CLIENT", fontsize=7.4, fontweight="700",
            color=BLUE_RAMP[10], va="top")
    ax.text(72.2, 70.6, "ACTUALLY PAYS", fontsize=7.4, fontweight="700",
            color=BLUE_RAMP[10], va="top")
    rows = [
        ("Agreement value", "₹2,20,00,000", INK),
        ("Stamp duty 6%*", "₹13,20,000", INK2),
        ("Registration 1%, capped", "₹30,000", INK2),
        ("TDS 194-IA 1%†", "₹2,20,000", INK2),
        ("Brokerage 1% + 18% GST", "₹2,59,600", INK2),
        ("Total outlay", "₹2,38,29,600", INK),
        ("Above agreement value", "+8.3%", CRITICAL),
    ]
    yy = 63
    for lab, val, c in rows:
        bold = lab in ("Total outlay", "Above agreement value")
        if bold:
            ax.plot([72.2, 95.8], [yy + 3.6, yy + 3.6], color=BLUE_RAMP[1], lw=0.9)
        ax.text(72.2, yy, lab, fontsize=6.8, color=c, va="center",
                fontweight="700" if bold else "400")
        ax.text(95.8, yy, val, fontsize=7.2 if bold else 6.8, color=c, va="center",
                ha="right", fontweight="700" if bold else "600")
        yy -= 6.4
    ax.text(72.2, 25.6,
            "* 5% for a sole female owner\n† above ₹50 lakh consideration",
            fontsize=5.9, color=MUTED, va="bottom", linespacing=1.6)

    T.footnote(fig, "Transaction-cost rates: stamp duty and registration [SRC-013]; TDS under section 194-IA [SRC-024]; GST on brokerage [SRC-012]. "
                    "The worked example uses the modelled average consideration and is illustrative. Getting this table right on a client's first call is "
                    "the cheapest credibility available to a new advisor — most buyers arrive having budgeted for the agreement value alone.")
    T.save(fig, "E5_client_fit_engine.png")


# ---------------------------------------------------------------- E6 -------
def fig_data_quality():
    """The eight provenance rules, and the failure each one prevents."""
    fig = plt.figure(figsize=(11.2, 7.0))
    ax = fig.add_axes([0.012, 0.115, 0.976, 0.660]); T.blank(ax)
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    T.titleblock(fig, "The eight provenance rules — and the specific failure each one prevents",
                 "These are the rules the uploaded blueprint got right, kept intact, with the failure mode each one exists to stop written next to it.\n"
                 "A rule without a named failure mode gets negotiated away the first time it is inconvenient.")

    rules = [
        ("Area basis", "Every price declares carpet, built-up or saleable. Comparison across bases is blocked, not warned.",
         "A saleable-area price compared to a carpet price understates the true rate by 25–35%. This single error can "
         "make a bad flat look like the cheapest on the shortlist.", BLUE),
        ("Price type", "Asking, registered, Ready Reckoner and launch are four separate fields, never one column.",
         "Asking prices in Mumbai routinely sit 8–15% above registered values. Blending them produces a number that "
         "describes no transaction that has ever occurred.", AQUA),
        ("Provenance", "Every fact carries source_ref, observed_date and confidence. No exceptions, including your own notes.",
         "Without it you cannot answer 'where did that come from?' in a live negotiation, and the entire advantage "
         "of being evidence-led evaporates in one sentence.", VIOLET),
        ("Sample size", "Every aggregate shows n. Below the domain minimum it is visually downgraded, not hidden.",
         "A pocket 'average' built on two transactions is an anecdote wearing a decimal point.", MAGENTA),
        ("Status ladder", "Confirmed / approved / under construction / proposed / rumoured, with slippage_months tracked.",
         "An approved metro line and an operating one produce completely different buyer behaviour. Scoring them "
         "alike is the most common error in Indian micro-market research.", ORANGE),
        ("Missing data", "Display 'Data unavailable'. Never coerce to zero, never interpolate, never estimate silently.",
         "A zero propagates into every average downstream and is invisible once it does.", YELLOW),
        ("Conflicts", "Retain both values, flag the conflict, and show it until it is reconciled against a primary source.",
         "Two portals disagreeing by 30% on the same project is information about the market, not an error to be "
         "averaged away.", RED),
        ("Staleness", "Each domain has stale_after_days. Client-facing screens show freshness on every number.",
         "A price that was true in March, quoted in August, in a market moving 5–6% a year, is simply wrong.", GREEN),
    ]
    for i, (name, rule, why, c) in enumerate(rules):
        col, row = i % 2, i // 2
        x = 1.5 + col * 49.5
        y = 96 - row * 24.5
        ax.add_patch(FancyBboxPatch((x, y - 22), 47.5, 22,
                                    boxstyle="round,pad=0,rounding_size=0.7",
                                    fc=SURFACE, ec=GRID, lw=0.9, zorder=3))
        ax.add_patch(Rectangle((x, y - 22), 0.9, 22, fc=c, ec="none", zorder=4))
        ax.text(x + 2.6, y - 4.0, f"{i+1}.  {name.upper()}", fontsize=7.8,
                fontweight="700", color=c, va="center")
        ax.text(x + 2.6, y - 9.6, T.wrap(rule, 74), fontsize=6.5, color=INK,
                va="center", linespacing=1.5)
        ax.text(x + 2.6, y - 17.6, T.wrap("PREVENTS:  " + why, 78), fontsize=6.2,
                color=INK2, va="center", linespacing=1.55)

    T.footnote(fig, "Rules 1–8 are preserved from the uploaded blueprint, which had them right. What is added here is enforcement: each rule is a NOT NULL "
                    "constraint or a blocked operation in the workbook rather than a convention in a document. A data-quality rule that depends on the "
                    "founder remembering it at 22:00 on a Friday is not a rule.")
    T.save(fig, "E6_data_quality_rules.png")


if __name__ == "__main__":
    T.apply()
    for f in [fig_geo_hierarchy, fig_data_domains, fig_source_stack,
              fig_compliance_path, fig_client_fit, fig_data_quality]:
        f(); print("ok", f.__name__)
