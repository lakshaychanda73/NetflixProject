"""
theme.py — one design system for every figure in the playbook.

Print target: light surface only. Palette values and the ordering are the
validated reference instance (validator: adjacent + all-pairs, light mode).
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch
from matplotlib.colors import LinearSegmentedColormap

# ---------------------------------------------------------------- palette ---
SURFACE   = "#fcfcfb"
PLANE     = "#f9f9f7"
INK       = "#0b0b0b"
INK2      = "#52514e"
MUTED     = "#898781"
GRID      = "#e1e0d9"
BASELINE  = "#c3c2b7"
BORDER    = "#0b0b0b1a"

# Categorical — fixed order, never cycled.
BLUE, ORANGE, AQUA, YELLOW, MAGENTA, GREEN, VIOLET, RED = (
    "#2a78d6", "#eb6834", "#1baf7a", "#eda100",
    "#e87ba4", "#008300", "#4a3aa7", "#e34948",
)
SERIES = [BLUE, ORANGE, AQUA, YELLOW, MAGENTA, GREEN, VIOLET, RED]
SLOT = dict(blue=BLUE, orange=ORANGE, aqua=AQUA, yellow=YELLOW,
            magenta=MAGENTA, green=GREEN, violet=VIOLET, red=RED)

# Status — reserved, never a series colour. Always paired with a label.
GOOD, WARN, SERIOUS, CRITICAL = "#0ca30c", "#fab219", "#ec835a", "#d03b3b"

# Sequential blue ramp (100 -> 700)
BLUE_RAMP = ["#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7",
             "#3987e5", "#2a78d6", "#256abf", "#1c5cab", "#184f95", "#104281", "#0d366b"]
SEQ_BLUE = LinearSegmentedColormap.from_list("seq_blue", BLUE_RAMP)
# Ordinal floor on light: never lighter than step 250 (#86b6ef)
SEQ_BLUE_ORD = LinearSegmentedColormap.from_list("seq_blue_ord", BLUE_RAMP[3:])
# Diverging blue <-> red through neutral gray
DIVERGING = LinearSegmentedColormap.from_list(
    "div_br", ["#104281", "#2a78d6", "#9ec5f4", "#f0efec", "#f3b0af", "#e34948", "#8f1f1e"])

FONT = "Inter"

# ------------------------------------------------------------------ rcparams
def apply():
    mpl.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": [FONT, "Liberation Sans", "DejaVu Sans"],
        "font.size": 9.5,
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "savefig.facecolor": SURFACE,
        "savefig.dpi": 200,
        "figure.dpi": 200,
        "axes.edgecolor": BASELINE,
        "axes.linewidth": 0.8,
        "axes.labelcolor": INK2,
        "axes.titlecolor": INK,
        "axes.grid": False,
        "grid.color": GRID,
        "grid.linewidth": 0.7,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "xtick.labelcolor": INK2,
        "ytick.labelcolor": INK2,
        "xtick.major.width": 0.8,
        "ytick.major.width": 0.8,
        "xtick.major.size": 3,
        "ytick.major.size": 3,
        "legend.frameon": False,
        "legend.fontsize": 8.5,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "pdf.fonttype": 42,
        "svg.fonttype": "none",
    })


# ------------------------------------------------------------------ helpers
def titleblock(fig, title, subtitle=None, x=0.012, y=0.975, size=13.5, sub_size=9.4):
    """Consistent left-aligned figure title + deck."""
    fig.text(x, y, title, ha="left", va="top", fontsize=size,
             fontweight="600", color=INK)
    if subtitle:
        fig.text(x, y - (size + 8) / (fig.get_size_inches()[1] * 72), subtitle,
                 ha="left", va="top", fontsize=sub_size, color=INK2, linespacing=1.35)


def footnote(fig, text, x=0.012, y=0.016, size=7.4, width=None):
    """Wrap each authored line to the figure width so nothing overflows the canvas."""
    import textwrap
    if width is None:
        usable_in = fig.get_size_inches()[0] * (1 - 2 * x)
        width = int(usable_in / (size * 0.0072))   # ~0.52 em average advance
    lines = []
    for para in text.split("\n"):
        lines.extend(textwrap.wrap(para, width) or [""])
    fig.text(x, y, "\n".join(lines), ha="left", va="bottom", fontsize=size,
             color=MUTED, linespacing=1.45)


def clean(ax, xgrid=False, ygrid=True, left=True, bottom=True):
    ax.set_axisbelow(True)
    if ygrid:
        ax.yaxis.grid(True, color=GRID, linewidth=0.7)
    if xgrid:
        ax.xaxis.grid(True, color=GRID, linewidth=0.7)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(left)
    ax.spines["bottom"].set_visible(bottom)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(BASELINE)
    ax.tick_params(length=3, width=0.8)


def rbar(ax, x, y, w, h, color, r=None, horizontal=False, alpha=1.0, z=3, ec="none", lw=0):
    """Bar anchored to the baseline.

    A rounded data-end is only safe when both axes are in comparable units — a
    FancyBboxPatch applies its rounding in DATA units on both axes, so a radius
    chosen for a 200,000-wide x-axis silently explodes a 0.6-tall bar. The radius
    is therefore derived from the bar's own geometry and capped, and `r` is
    accepted only as a hint. Correct geometry beats a rounded corner.
    """
    rs = min(abs(w), abs(h)) * 0.16
    if r is not None:
        rs = min(rs, abs(r))
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={rs}",
        linewidth=lw, edgecolor=ec, facecolor=color, alpha=alpha, zorder=z,
    )
    ax.add_patch(box)
    return box


def node(ax, x, y, w, h, label, fc=SURFACE, ec=BASELINE, tc=INK, fs=8.6,
         weight="500", r=0.10, lw=1.0, z=3, ha="center", pad_top=0.0, linespacing=1.3):
    """Rounded diagram node with wrapped label."""
    box = FancyBboxPatch((x, y), w, h,
                         boxstyle=f"round,pad=0,rounding_size={r}",
                         linewidth=lw, edgecolor=ec, facecolor=fc, zorder=z)
    ax.add_patch(box)
    ax.text(x + w / 2, y + h / 2 + pad_top, label, ha="center", va="center",
            fontsize=fs, color=tc, fontweight=weight, zorder=z + 1,
            linespacing=linespacing)
    return box


def arrow(ax, p0, p1, color=BASELINE, lw=1.2, style="-|>", ms=7, rad=0.0, z=2, ls="-"):
    a = FancyArrowPatch(p0, p1, arrowstyle=f"{style},head_width={ms/2.6},head_length={ms/2.2}",
                        connectionstyle=f"arc3,rad={rad}", color=color,
                        linewidth=lw, zorder=z, linestyle=ls,
                        shrinkA=2, shrinkB=2, joinstyle="round")
    ax.add_patch(a)
    return a


def blank(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_facecolor(SURFACE)


OUTDIR = "../figures/"


def save(fig, name):
    """Fixed-canvas save. No tight bbox — every figure controls its own margins,
    so figure-coordinate text (titles, footnotes) never drifts."""
    fig.savefig(OUTDIR + name, facecolor=SURFACE)
    plt.close(fig)


def inr(v, crore=False):
    """Indian-format number."""
    if crore:
        return f"₹{v:,.0f} cr"
    s = f"{int(round(v)):,}"
    # convert to lakh/crore grouping
    n = str(int(round(v)))
    if len(n) > 3:
        last3, rest = n[-3:], n[:-3]
        parts = []
        while len(rest) > 2:
            parts.insert(0, rest[-2:]); rest = rest[:-2]
        if rest:
            parts.insert(0, rest)
        s = ",".join(parts + [last3])
    return s


def wrap(text, width):
    import textwrap
    return "\n".join(textwrap.wrap(text, width))
