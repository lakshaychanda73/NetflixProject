"""
deck_theme.py — slide design system for the Brickrock Realty pitch deck.

Modern investor-deck aesthetic: light analytical slides, dark narrative slides,
one hero accent, big numbers, charts everywhere. Sans-only, tight tracking.

Categorical palette validated on the light ground (adjacent + all-pairs):
  orange #E8722C · blue #2D6FCB · green #0E9E5E · purple #7B4FD6
Orange sits below 3:1 on the light surface, so every orange mark carries a
visible direct label — which a pitch deck wants anyway.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch, Circle, Polygon
from matplotlib.colors import LinearSegmentedColormap

# ------------------------------------------------------------------ grounds
LIGHT    = "#FAFAF7"      # analytical slides
DARK     = "#0F1621"      # narrative slides
DARK_2   = "#18202D"      # dark card
CARD     = "#FFFFFF"
CARD_ALT = "#F2F1EC"

INK      = "#10131A"
INK2     = "#4C5361"
MUTED    = "#8C93A0"
HAIR     = "#E4E3DC"
RULE     = "#CFCEC5"

# on dark
D_INK    = "#FFFFFF"
D_INK2   = "#A9B4C4"
D_MUTED  = "#6B7889"
D_HAIR   = "#242E3D"

# ------------------------------------------------------------------ palette
ORANGE  = "#E8722C"       # hero accent
BLUE    = "#2D6FCB"
GREEN   = "#0E9E5E"
PURPLE  = "#7B4FD6"
SERIES  = [ORANGE, BLUE, GREEN, PURPLE]

# lighter/darker steps for stacks and ramps
ORANGE_L, ORANGE_D = "#F3A876", "#B8511A"
BLUE_L,   BLUE_D   = "#8FB4E8", "#1D4C90"
GREEN_L,  GREEN_D  = "#7FD0A9", "#0A6E42"

GOOD, WARN, BAD = "#0E9E5E", "#E0A32E", "#C93F2E"

ORANGE_RAMP = ["#FDF0E6", "#FADBC4", "#F6C09A", "#F2A470", "#EE8A4B",
               "#E8722C", "#CC5F1F", "#A94D18", "#853A12"]
SEQ_ORANGE = LinearSegmentedColormap.from_list("seq_orange", ORANGE_RAMP)

SANS = "Inter"


def apply():
    mpl.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": [SANS, "Liberation Sans", "DejaVu Sans"],
        "font.size": 10,
        "figure.facecolor": LIGHT,
        "axes.facecolor": LIGHT,
        "savefig.facecolor": LIGHT,
        "savefig.dpi": 200,
        "figure.dpi": 200,
        "axes.edgecolor": RULE,
        "axes.linewidth": 0.9,
        "axes.labelcolor": INK2,
        "axes.grid": False,
        "grid.color": HAIR,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "xtick.labelcolor": INK2,
        "ytick.labelcolor": INK2,
        "xtick.major.size": 0,
        "ytick.major.size": 0,
        "legend.frameon": False,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "pdf.fonttype": 42,
    })


OUTDIR = "../figures/"


def save(fig, name, dark=False):
    fig.savefig(OUTDIR + name, facecolor=DARK if dark else LIGHT)
    plt.close(fig)


def canvas(w, h, dark=False):
    """A full-bleed slide-figure canvas in 0-100 x 0-100 space."""
    fig = plt.figure(figsize=(w, h))
    fig.patch.set_facecolor(DARK if dark else LIGHT)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_facecolor(DARK if dark else LIGHT)
    return fig, ax


def blank(ax, dark=False):
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_facecolor(DARK if dark else LIGHT)


def clean(ax, xgrid=False, ygrid=True, left=False, bottom=True, dark=False):
    hair = D_HAIR if dark else HAIR
    rule = D_HAIR if dark else RULE
    ax.set_axisbelow(True)
    if ygrid:
        ax.yaxis.grid(True, color=hair, linewidth=0.9)
    if xgrid:
        ax.xaxis.grid(True, color=hair, linewidth=0.9)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_visible(left)
    ax.spines["bottom"].set_visible(bottom)
    ax.spines["bottom"].set_color(rule)
    ax.spines["left"].set_color(rule)
    ax.tick_params(length=0, pad=5)


def card(ax, x, y, w, h, fc=CARD, ec=HAIR, lw=1.0, r=1.0, z=2, alpha=1.0):
    b = FancyBboxPatch((x, y), w, h,
                       boxstyle=f"round,pad=0,rounding_size={r}",
                       facecolor=fc, edgecolor=ec, linewidth=lw, zorder=z, alpha=alpha)
    ax.add_patch(b)
    return b


def bar(ax, x, y, w, h, color, r=None, alpha=1.0, z=3, ec="none", lw=0):
    """Rectangle-safe bar; radius derived from the bar's own geometry."""
    rs = min(abs(w), abs(h)) * 0.13
    if r is not None:
        rs = min(rs, abs(r))
    b = FancyBboxPatch((x, y), w, h,
                       boxstyle=f"round,pad=0,rounding_size={rs}",
                       facecolor=color, edgecolor=ec, linewidth=lw, alpha=alpha, zorder=z)
    ax.add_patch(b)
    return b


def arrow(ax, p0, p1, color=RULE, lw=1.4, ms=9, rad=0.0, z=2, ls="-"):
    a = FancyArrowPatch(p0, p1,
                        arrowstyle=f"-|>,head_width={ms/2.8},head_length={ms/2.3}",
                        connectionstyle=f"arc3,rad={rad}", color=color,
                        linewidth=lw, zorder=z, linestyle=ls,
                        shrinkA=2, shrinkB=2, joinstyle="round")
    ax.add_patch(a)
    return a


def chip(ax, x, y, text, fc=ORANGE, tc="white", size=6.6, pad=1.5, h=4.2, z=6):
    """Small pill label."""
    w = len(text) * size * 0.078 + pad * 2
    card(ax, x, y - h / 2, w, h, fc=fc, ec="none", r=h / 2, z=z)
    ax.text(x + w / 2, y, text, ha="center", va="center", fontsize=size,
            color=tc, fontweight="700", zorder=z + 1)
    return w


def stat(ax, x, y, w, h, value, label, sub=None, delta=None,
         accent=ORANGE, dark=False, vsize=25, fc=None):
    """Big-number stat card. The workhorse of this deck."""
    ink = D_INK if dark else INK
    ink2 = D_INK2 if dark else INK2
    muted = D_MUTED if dark else MUTED
    if fc is None:
        fc = DARK_2 if dark else CARD
    card(ax, x, y, w, h, fc=fc, ec=D_HAIR if dark else HAIR)
    ax.add_patch(Rectangle((x, y), 0.7, h, facecolor=accent, edgecolor="none", zorder=3))
    top = y + h
    ax.text(x + 3.0, top - 4.6, value, fontsize=vsize, color=ink,
            fontweight="600", va="center", zorder=4)
    yy = top - 9.4
    if delta:
        ax.text(x + 3.0, yy, delta, fontsize=7.4, color=accent,
                fontweight="700", va="center", zorder=4)
        yy -= 3.6
    ax.text(x + 3.0, yy, label, fontsize=8.0, color=ink2, va="center", zorder=4)
    if sub:
        ax.text(x + 3.0, yy - 3.8, sub, fontsize=6.8, color=muted,
                va="top", zorder=4, linespacing=1.5)


def wrap(text, width):
    import textwrap
    return "\n".join(textwrap.wrap(text, width))


def track(s, spacing="  "):
    """Letter-spaced caps for eyebrows."""
    return spacing.join(s.upper())
