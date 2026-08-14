"""fig_strategy.py — Part B: business design and market selection."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Polygon, Circle
import theme as T
from theme import (SURFACE, INK, INK2, MUTED, GRID, BASELINE, BLUE, ORANGE, AQUA,
                   YELLOW, MAGENTA, GREEN, VIOLET, RED, GOOD, WARN, SERIOUS, CRITICAL,
                   SEQ_BLUE, BLUE_RAMP, DIVERGING)
import evidence as E


# ---------------------------------------------------------------- B1 -------
def fig_business_model():
    """Six-layer operating stack: what each layer does, what it earns, what it protects."""
    fig = plt.figure(figsize=(11.2, 7.4))
    ax = fig.add_axes([0.015, 0.055, 0.97, 0.735]); T.blank(ax)
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    T.titleblock(fig, "The six-layer operating stack",
                 "Layers 1 and 2 are the licence to operate and the reason to be believed. Layer 4 pays the bills in Year 1.\n"
                 "Layer 5 is the only one that compounds — and it is a by-product of layer 4, which is why transactions cannot wait for the database.")

    layers = [
        ("6", "PRODUCTISATION", VIOLET,
         "Locality briefs · compare tools · alerts · B2B research",
         "Secondary revenue", "Year 2+",
         "Only after the system has proprietary observations used repeatedly in live deals"),
        ("5", "PROPRIETARY FEEDBACK", MAGENTA,
         "Closed prices · objections · society rules · true commute · deal duration",
         "The moat", "Compounds",
         "A by-product of doing layer 4 properly — it cannot be bought, scraped or hired"),
        ("4", "BROKERAGE EXECUTION", ORANGE,
         "Site visits · negotiation · documentation · developer & seller coordination",
         "Year-1 revenue", "Month 4+",
         "The only layer that produces cash in Year 1. Everything above it is funded by this"),
        ("3", "CLIENT ADVISORY", YELLOW,
         "Budget · commute · configuration · horizon · end-user vs investor objectives",
         "Converts data to a shortlist", "Month 3+",
         "Turns the intelligence layer into something a client will actually pay for"),
        ("2", "MICRO-MARKET INTELLIGENCE", AQUA,
         "Registered / asking / RR separation · rental · projects · infrastructure · risk",
         "Differentiation", "Month 1+",
         "Prevents bad comparisons; this is what makes the advice trustworthy rather than opinionated"),
        ("1", "COMPLIANCE & LEGITIMACY", BLUE,
         "MahaRERA registration + Certificate of Competency · entity · GST/TDS · DPDP",
         "Licence to operate", "Week 1–6",
         "Existential. Nothing above this layer is lawful revenue until it is complete"),
    ]

    h, gap = 13.6, 2.4
    for i, (num, name, c, work, role, when, why) in enumerate(layers):
        y = 100 - (i + 1) * (h + gap) + gap
        ax.add_patch(FancyBboxPatch((6, y), 88, h,
                                    boxstyle="round,pad=0,rounding_size=0.9",
                                    fc=SURFACE, ec=c, lw=1.5, zorder=3))
        ax.add_patch(FancyBboxPatch((6, y), 5.4, h,
                                    boxstyle="round,pad=0,rounding_size=0.9",
                                    fc=c, ec="none", zorder=4))
        ax.add_patch(Rectangle((9.6, y), 1.8, h, fc=c, ec="none", zorder=4))
        ax.text(8.7, y + h / 2, num, ha="center", va="center", fontsize=13,
                fontweight="700", color="white", zorder=6)
        ax.text(13.5, y + h - 3.4, name, fontsize=9.4, fontweight="700", color=c, va="center")
        ax.text(13.5, y + h - 8.0, work, fontsize=7.9, color=INK2, va="center")
        ax.text(13.5, y + 2.6, why, fontsize=7.0, color=MUTED, va="center", style="italic")
        # right rail
        ax.add_patch(Rectangle((75.5, y + 1.2), 0.9, h - 2.4, fc=GRID, ec="none", zorder=4))
        ax.text(78.5, y + h - 4.6, role, fontsize=8.2, fontweight="600", color=INK, va="center")
        ax.text(78.5, y + 4.6, when, fontsize=7.4, color=MUTED, va="center")

    # build-order arrow
    ax.annotate("", xy=(3.0, 96), xytext=(3.0, 4),
                arrowprops=dict(arrowstyle="-|>,head_width=0.28,head_length=0.5",
                                color=BASELINE, lw=1.4))
    ax.text(1.4, 50, "B U I L D   O R D E R", rotation=90, ha="center", va="center",
            fontsize=7.2, color=MUTED, fontweight="600")

    T.footnote(fig, "The sequencing correction that matters: layers 1, 2 and 4 are built in parallel from week 1, not in series. "
                    "A brokerage that completes its database before taking a client learns nothing about whether the database helps, "
                    "and runs out of money finding out. Compliance [SRC-001, SRC-002, SRC-023] gates only the marketing and closure steps, not the research.")
    T.save(fig, "B1_business_model_stack.png")


# ---------------------------------------------------------------- B2 -------
def fig_entry_model():
    """The corrected weighted model: score, rank, contribution and what changed."""
    ranked = E.ranked_regions()
    weights = {k: w for k, _, w, _ in E.CRITERIA}
    labels = {k: l for k, l, _, _ in E.CRITERIA}
    order = [k for k, _, _, _ in E.CRITERIA]

    fig = plt.figure(figsize=(11.2, 6.9))
    T.titleblock(fig, "Market entry priority — the corrected model",
                 "Seven weighted criteria, one weight vector, one score table. Bars are stacked by contribution, so it is always visible\n"
                 "which criterion is carrying a corridor — and where two corridors are genuinely inseparable.")

    ax = fig.add_axes([0.185, 0.145, 0.545, 0.615])
    palette = [BLUE, AQUA, ORANGE, BLUE_RAMP[2], VIOLET, YELLOW, MAGENTA]
    names = [r for r, _ in ranked]
    for i, (region, total) in enumerate(ranked):
        left = 0.0
        for j, k in enumerate(order):
            contrib = E.REGION_SCORES[region][k] * weights[k]
            ax.barh(i, contrib, left=left, height=0.62, color=palette[j],
                    edgecolor=SURFACE, linewidth=1.4, zorder=3)
            if contrib > 0.72:
                ax.text(left + contrib / 2, i, f"{contrib:.2f}", ha="center", va="center",
                        fontsize=6.8, color="white", fontweight="600", zorder=4)
            left += contrib
        ax.text(left + 0.10, i, f"{total:.2f}", va="center", fontsize=10.5,
                color=INK, fontweight="600")

    ax.set_yticks(range(len(names)))
    ax.set_yticklabels([f"{i+1}.   {n}" for i, n in enumerate(names)], fontsize=9)
    for i, lab in enumerate(ax.get_yticklabels()):
        lab.set_color(INK if i == 0 else INK2)
        lab.set_fontweight("600" if i == 0 else "400")
    ax.invert_yaxis()
    ax.set_xlim(0, 9.3); ax.set_ylim(len(names) - 0.4, -0.6)
    ax.set_xlabel("weighted priority score  (max 10)", fontsize=8.6)
    T.clean(ax, ygrid=False, xgrid=True)

    handles = [plt.Line2D([], [], marker="s", ls="", color=palette[j], ms=7,
                          label=f"{labels[k]}  ({weights[k]:.2f})") for j, k in enumerate(order)]
    fig.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.752, 0.735),
               fontsize=7.6, handletextpad=0.5, labelspacing=0.85,
               title="criterion (weight)", title_fontproperties={"size": 7.8, "weight": "600"})

    # the tie, stated openly
    # The tie, called out in the figure margin so it can be read at full size.
    ax.plot([8.42, 8.42], [1.72, 3.28], color=ORANGE, lw=1.5, zorder=6)
    for yy in (1.72, 3.28):
        ax.plot([8.28, 8.42], [yy, yy], color=ORANGE, lw=1.5, zorder=6)
    ax.annotate("", xy=(9.28, 3.9), xytext=(8.42, 2.5), zorder=6,
                arrowprops=dict(arrowstyle="-", color=ORANGE, lw=1.0,
                                ls=(0, (3, 2)), connectionstyle="arc3,rad=-0.25"))
    fig.patches.append(FancyBboxPatch((0.752, 0.150), 0.233, 0.150,
                                      boxstyle="round,pad=0,rounding_size=0.012",
                                      fc="#fdf3ee", ec=ORANGE, lw=1.0,
                                      transform=fig.transFigure, zorder=2))
    fig.text(0.766, 0.284, "A GENUINE TIE — SHOWN, NOT HIDDEN", fontsize=7.0,
             fontweight="700", color=ORANGE, va="top", zorder=6)
    fig.text(0.766, 0.256, zorder=6, s=
             T.wrap("Navi Mumbai and the Western Suburbs both score 7.48. "
                    "The tie breaks toward Navi Mumbai on whitespace (7 vs 4) — "
                    "the criterion that decides whether a new entrant is heard at all.", 46),
             fontsize=6.8, color=INK2, va="top", linespacing=1.65)

    T.footnote(fig, "THIS IS AN ANALYST MODEL, NOT A MARKET STATISTIC. Scores are 1–10 judgements informed by the evidence in Part A; the weights encode "
                    "one specific strategy — a single founder, limited capital, needing a first closure inside two quarters. Change that strategy and the "
                    "weights should change with it. Whitespace scores are re-based against the 42,865 registered agents in Maharashtra [SRC-025].")
    T.save(fig, "B2_entry_priority_model.png")


# ---------------------------------------------------------------- B3 -------
def fig_sensitivity():
    """Does the recommendation survive being wrong about the weights?"""
    weights = {k: w for k, _, w, _ in E.CRITERIA}
    labels = {k: l for k, l, _, _ in E.CRITERIA}
    order = [k for k, _, _, _ in E.CRITERIA]
    base = dict(E.ranked_regions())
    top = "Eastern/Central Suburbs"

    fig, axes = plt.subplots(1, 2, figsize=(11.2, 5.2))
    fig.subplots_adjust(top=0.62, bottom=0.16, left=0.20, right=0.975, wspace=0.42)
    T.titleblock(fig, "Does the recommendation survive being wrong?",
                 "Two stress tests on the entry model. Left: each weight is doubled and halved in turn. Right: 5,000 random weight vectors.\n"
                 "A recommendation that only holds at one exact set of weights is not a recommendation — it is an accident.")

    # --- tornado
    ax = axes[0]
    rows = []
    for k in order:
        for mult, tag in ((0.5, "lo"), (2.0, "hi")):
            w = dict(weights); w[k] = weights[k] * mult
            tot = sum(w.values()); w = {a: b / tot for a, b in w.items()}
            r = E.ranked_regions(weights=w)
            gap = r[0][1] - r[1][1] if r[0][0] == top else -(dict(r)[top] - r[0][1])
            rows.append((k, tag, gap))
    gaps = {k: (0, 0) for k in order}
    for k, tag, g in rows:
        lo, hi = gaps[k]
        gaps[k] = (g, hi) if tag == "lo" else (lo, g)
    ordk = sorted(order, key=lambda k: -(abs(gaps[k][0]) + abs(gaps[k][1])))
    for i, k in enumerate(ordk):
        lo, hi = gaps[k]
        for v, c in ((lo, BLUE_RAMP[3]), (hi, BLUE)):
            ax.barh(i, v, height=0.30 if c == BLUE else 0.30,
                    left=0, color=c, zorder=3,
                    align="edge" if c == BLUE else "edge")
        ax.barh(i - 0.16, lo, height=0.30, color=BLUE_RAMP[3], zorder=3)
        ax.barh(i + 0.16, hi, height=0.30, color=BLUE, zorder=3)
    ax.cla()
    for i, k in enumerate(ordk):
        lo, hi = gaps[k]
        ax.barh(i - 0.17, lo, height=0.31, color=BLUE_RAMP[3], zorder=3, label="_")
        ax.barh(i + 0.17, hi, height=0.31, color=BLUE, zorder=3, label="_")
    ax.axvline(0, color=BASELINE, lw=1.0, zorder=2)
    ax.set_yticks(range(len(ordk)))
    ax.set_yticklabels([labels[k] for k in ordk], fontsize=8.2)
    ax.invert_yaxis()
    ax.set_xlabel("lead of Eastern/Central over the runner-up", fontsize=8.2)
    ax.set_xlim(0, 0.62)
    T.clean(ax, ygrid=False, xgrid=True)
    ax.set_title("Weight doubled / halved, one at a time", fontsize=9.4, color=INK,
                 loc="left", pad=8, fontweight="600")
    ax.plot([], [], "s", color=BLUE, ms=7, label="weight doubled")
    ax.plot([], [], "s", color=BLUE_RAMP[3], ms=7, label="weight halved")
    ax.legend(loc="lower right", fontsize=7.4, handletextpad=0.5)

    # --- monte carlo
    ax = axes[1]
    rng = np.random.default_rng(7)
    base_w = np.array([weights[k] for k in order])
    wins = {r: 0 for r in E.REGION_SCORES}
    N = 5000
    for _ in range(N):
        w = base_w * rng.uniform(0.5, 1.5, len(order))
        w = w / w.sum()
        wd = {k: w[i] for i, k in enumerate(order)}
        wins[E.ranked_regions(weights=wd)[0][0]] += 1
    ws = sorted(wins.items(), key=lambda x: -x[1])
    ws = [(k, v) for k, v in ws if v > 0]
    for i, (r, v) in enumerate(ws):
        pct = 100 * v / N
        T.rbar(ax, 0, i - 0.30, pct, 0.60, BLUE if i == 0 else BLUE_RAMP[3], r=0.9)
        ax.text(pct + 1.8, i, f"{pct:.1f}%", va="center", fontsize=8.6,
                color=INK, fontweight="600" if i == 0 else "400")
    ax.set_yticks(range(len(ws))); ax.set_yticklabels([r for r, _ in ws], fontsize=8.2)
    ax.invert_yaxis(); ax.set_xlim(0, 108)
    ax.set_xticks([0, 25, 50, 75, 100]); ax.set_xticklabels(["0", "25", "50", "75", "100%"])
    ax.set_xlabel("share of 5,000 random weight vectors won", fontsize=8.2)
    T.clean(ax, ygrid=False, xgrid=True)
    ax.set_title("Every weight jittered ±50% simultaneously", fontsize=9.4, color=INK,
                 loc="left", pad=8, fontweight="600")

    T.footnote(fig, "Reading: Eastern/Central stays first under every single-weight perturbation tested, and wins a large majority of randomised weight vectors. "
                    "The corridors that displace it are those that win when transaction depth alone is weighted very heavily — which is precisely the strategy a "
                    "well-capitalised incumbent should run, and precisely the one a single founder cannot.")
    T.save(fig, "B3_sensitivity.png")


# ---------------------------------------------------------------- B4 -------
def fig_corridor_heatmap():
    """Corridor x criterion heatmap — sequential, one hue, values printed."""
    order = [k for k, _, _, _ in E.CRITERIA]
    labels = [l for _, l, _, _ in E.CRITERIA]
    weights = [w for _, _, w, _ in E.CRITERIA]
    ranked = E.ranked_regions()
    regions = [r for r, _ in ranked]
    M = np.array([[E.REGION_SCORES[r][k] for k in order] for r in regions], dtype=float)

    fig = plt.figure(figsize=(11.2, 5.6))
    ax = fig.add_axes([0.205, 0.250, 0.615, 0.442])
    T.titleblock(fig, "Corridor scorecard — where each corridor is strong and where it is not",
                 "The same 1–10 judgements as the model, laid out so the shape of each corridor is visible rather than collapsed into one number.\n"
                 "Read the rows for a corridor's profile; read the columns for who wins each criterion.")

    im = ax.imshow(M, cmap=SEQ_BLUE, vmin=1, vmax=10, aspect="auto")
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            v = M[i, j]
            ax.text(j, i, f"{int(v)}", ha="center", va="center", fontsize=9.4,
                    color="white" if v >= 6.5 else INK, fontweight="600")
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels([T.wrap(l, 13) for l in labels], fontsize=7.8, linespacing=1.35)
    ax.set_yticks(range(len(regions)))
    ax.set_yticklabels([f"{i+1}.  {r}" for i, r in enumerate(regions)], fontsize=8.6)
    ax.tick_params(length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xticks(np.arange(-0.5, len(labels), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(regions), 1), minor=True)
    ax.grid(which="minor", color=SURFACE, linewidth=2.4)
    ax.tick_params(which="minor", length=0)

    # weight strip
    axw = fig.add_axes([0.205, 0.112, 0.615, 0.042]); T.blank(axw)
    axw.set_xlim(-0.5, len(labels) - 0.5); axw.set_ylim(0, 1)
    for j, w in enumerate(weights):
        axw.add_patch(Rectangle((j - 0.42, 0.30), 0.84, 0.45 * w / max(weights),
                                fc=MUTED, ec="none"))
        axw.text(j, 0.10, f"{w:.2f}", ha="center", fontsize=7.2, color=INK2)
    axw.text(-0.62, 0.42, "weight", ha="right", fontsize=7.6, color=MUTED)

    cax = fig.add_axes([0.845, 0.250, 0.016, 0.442])
    cb = fig.colorbar(im, cax=cax)
    cb.set_ticks([1, 4, 7, 10])
    cb.ax.tick_params(labelsize=7.4, length=0)
    cb.outline.set_visible(False)
    cb.set_label("score (1–10)", fontsize=7.6, color=INK2)

    T.footnote(fig, "Analyst judgements, not measurements [model]. Read alongside B2: a corridor can lead a heavily weighted column and still lose overall. "
                    "The Western Suburbs win transaction depth outright with a 10 and still finish fourth, because a 4 on whitespace is what a new entrant "
                    "actually experiences on their first day of calling.")
    T.save(fig, "B4_corridor_heatmap.png")


# ---------------------------------------------------------------- B5 -------
def fig_radar():
    """Profile comparison of the four corridors that are actually in contention."""
    order = [k for k, _, _, _ in E.CRITERIA]
    labels = [l for _, l, _, _ in E.CRITERIA]
    picks = ["Eastern/Central Suburbs", "Thane–Ghodbunder", "Navi Mumbai"]
    cols = [BLUE, ORANGE, AQUA]

    ang = np.linspace(0, 2 * np.pi, len(order), endpoint=False).tolist()
    ang += ang[:1]

    fig = plt.figure(figsize=(11.2, 6.3))
    ax = fig.add_axes([0.305, 0.115, 0.365, 0.575], polar=True)
    T.titleblock(fig, "Corridor profiles — the three corridors actually in contention",
                 "The shape matters more than the area. Eastern/Central has no weak axis; Navi Mumbai is a spike on one axis;\n"
                 "Thane is the balanced value option. A single founder should prefer the shape with no hole in it.")

    for name, c in zip(picks, cols):
        vals = [E.REGION_SCORES[name][k] for k in order]
        vals += vals[:1]
        ax.plot(ang, vals, color=c, lw=2.0, zorder=4, label=name)
        ax.fill(ang, vals, color=c, alpha=0.11, zorder=3)
        ax.scatter(ang[:-1], vals[:-1], color=c, s=26, zorder=5,
                   edgecolor=SURFACE, linewidth=1.2)

    ax.set_xticks(ang[:-1])
    ax.set_xticklabels([T.wrap(l, 14) for l in labels], fontsize=7.6, color=INK2)
    ax.set_ylim(0, 10)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(["2", "4", "6", "8", "10"], fontsize=6.8, color=MUTED)
    ax.grid(color=GRID, lw=0.7)
    ax.spines["polar"].set_color(GRID)
    ax.set_facecolor(SURFACE)
    ax.tick_params(pad=13)

    notes = [
        (BLUE, "EASTERN / CENTRAL", "No axis below 7. Nothing about it is\nspectacular and nothing about it will\nstop you. That is the correct profile\nfor a first corridor."),
        (ORANGE, "THANE", "Best entry cost in the region (9) and\nequally strong whitespace, held back\nonly by execution friction and thinner\ndata coverage."),
        (AQUA, "NAVI MUMBAI", "A 10 on infrastructure and a 6 on\nexecution. The highest-upside corridor\nand the one most likely to consume a\nfounder's calendar."),
    ]
    for i, (c, head, body) in enumerate(notes):
        x = 0.735
        y = 0.665 - i * 0.185
        fig.add_artist(plt.Line2D([x - 0.012, x - 0.012], [y - 0.135, y + 0.022],
                                  color=c, lw=2.4))
        fig.text(x, y + 0.010, head, fontsize=7.8, fontweight="700", color=c, va="top")
        fig.text(x, y - 0.020, body, fontsize=7.0, color=INK2, va="top", linespacing=1.55)

    T.footnote(fig, "Analyst judgements [model]. The Western Suburbs, Harbour and South Mumbai are omitted here because the model does not place them in "
                    "contention for a first corridor — their profiles appear in full in B4.")
    T.save(fig, "B5_corridor_radar.png")


# ---------------------------------------------------------------- B6 -------
def fig_positioning():
    """Competitive positioning — where a one-person evidence-led desk can actually win."""
    fig = plt.figure(figsize=(11.2, 6.6))
    ax = fig.add_axes([0.075, 0.085, 0.63, 0.665])
    T.titleblock(fig, "Competitive positioning — the gap a new desk can occupy",
                 "Two axes decide who wins a Mumbai buyer: how much evidence sits behind the advice, and how deep the geographic focus goes.\n"
                 "Scale players own the top-left. Traditional local brokers own the bottom-right. The top-right is thinly held.")

    players = [
        # name, x, y, bubble, colour, sub-label, label x, label y, ha, va
        ("National portals\n99acres · Magicbricks · Housing", 2.0, 8.6, 1500, MUTED,
         "Listing breadth, no closing depth", 2.0, 7.52, "center", "top"),
        ("Scale brokerages\nSquare Yards · ANAROCK · PropTiger", 4.9, 6.9, 1050, MUTED,
         "Process and reach; thin at pocket level", 4.9, 6.00, "center", "top"),
        ("Institutional advisory\nKnight Frank · CBRE · JLL", 8.5, 8.8, 780, MUTED,
         "Institutional tickets, not retail buyers", 8.5, 7.98, "center", "top"),
        ("Developer channel partners", 2.3, 4.7, 700, MUTED,
         "Primary inventory only; conflicted", 3.05, 4.40, "left", "top"),
        ("Traditional local brokers\n≈42,865 registered in Maharashtra", 2.4, 1.5, 1700, MUTED,
         "Deep pocket knowledge, undocumented", 2.4, 2.72, "center", "bottom"),
        ("THE POSITION\nEvidence-led micro-market desk", 8.3, 2.5, 900, BLUE,
         "Pocket depth, documented and sourced", 8.3, 3.42, "center", "bottom"),
    ]
    for name, x, y, sz, c, sub, lx, ly, ha, va in players:
        target = c == BLUE
        ax.scatter([x], [y], s=sz, color=c, alpha=1.0 if target else 0.17, zorder=4,
                   edgecolor=SURFACE if target else "none", linewidth=1.6)
        head, _, tail = name.partition("\n")
        rows = [(head, 8.2, INK if target else INK2, "700" if target else "600")]
        if tail:
            rows.append((tail, 7.2, INK2, "400"))
        rows.append((sub, 6.8, MUTED, "400"))
        step = 0.36
        # always render top-to-bottom in reading order, whichever edge we anchor to
        y0 = ly if va == "top" else ly + step * (len(rows) - 1)
        for r, (txt, fs, col, fw) in enumerate(rows):
            ax.text(lx, y0 - r * step, txt, ha=ha, va="top" if va == "top" else "center",
                    fontsize=fs, color=col, fontweight=fw, zorder=5)

    ax.axvline(5.5, color=GRID, lw=1.0, zorder=1)
    ax.axhline(5.5, color=GRID, lw=1.0, zorder=1)
    ax.add_patch(Rectangle((5.5, 0), 5.5, 5.5, fc=BLUE, alpha=0.045, ec="none", zorder=0))
    ax.text(10.6, 0.35, "THINLY HELD", ha="right", fontsize=7.6, color=BLUE,
            fontweight="700", zorder=2, alpha=0.8)

    ax.set_xlim(0, 11); ax.set_ylim(0, 11)
    ax.set_xlabel("evidence behind the advice   →   sourced, dated, sample-sized", fontsize=8.6)
    ax.set_ylabel("geographic breadth   →   city-wide and national", fontsize=8.6)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ("left", "bottom"):
        ax.spines[s].set_color(BASELINE)
    T.clean(ax, ygrid=False, xgrid=False)

    # right rail
    fig.text(0.735, 0.735, "WHY THIS POSITION IS OPEN", fontsize=8.4,
             fontweight="700", color=BLUE, va="top")
    body = [
        ("Portals monetise listings, not outcomes.",
         "Their incentive is inventory volume and lead resale. Neither rewards knowing which tower floods."),
        ("Scale brokerages optimise for throughput.",
         "A consultant carrying 40 live leads across five suburbs cannot hold pocket-level detail."),
        ("Local brokers know it but never write it down.",
         "The knowledge dies with the relationship, cannot be audited by a client, and never compounds."),
        ("Institutional research stops above retail.",
         "Knight Frank and CBRE publish city and zone data of real quality. Nobody serves the L4 pocket."),
        ("The catch, stated plainly.",
         "This gap is open because it is hard and slow, not because nobody thought of it. It is defended by patience, not capital."),
    ]
    y = 0.690
    for head, sub in body:
        h = T.wrap(head, 44)
        fig.text(0.735, y, h, fontsize=7.5, fontweight="700", color=INK,
                 va="top", linespacing=1.4)
        y -= 0.0245 * (1 + h.count("\n")) + 0.006
        b = T.wrap(sub, 50)
        fig.text(0.735, y, b, fontsize=6.9, color=INK2, va="top", linespacing=1.65)
        y -= 0.0235 * (1 + b.count("\n")) + 0.021

    T.footnote(fig, "Positions are analyst judgements [model]; bubble size is indicative of market presence, not measured share. "
                    "Agent count [SRC-025]; proptech market structure [SRC-026].")
    T.save(fig, "B6_positioning.png")


if __name__ == "__main__":
    T.apply()
    for f in [fig_business_model, fig_entry_model, fig_sensitivity,
              fig_corridor_heatmap, fig_radar, fig_positioning]:
        f(); print("ok", f.__name__)
