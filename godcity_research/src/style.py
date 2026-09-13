"""Shared design system for all God City research figures."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager, patheffects
import matplotlib.patches as mpatches

# ---------------------------------------------------------------- palette
INK       = "#14231F"   # near-black text
INK_SOFT  = "#4A5C58"   # secondary text
RULE      = "#D8D2C6"   # hairlines
PAPER     = "#FFFFFF"
PAPER_W   = "#FAF7F1"   # warm panel

TEAL_D    = "#0E3B39"   # primary deep
TEAL      = "#1C6E6B"
TEAL_L    = "#5FA8A2"
TEAL_XL   = "#BFDDDA"

TERRA     = "#C1622F"   # accent warm
TERRA_L   = "#E3A275"
GOLD      = "#C9992F"
GOLD_L    = "#EBD08A"

PLUM      = "#6B4A6E"
BLUE      = "#2F5E8C"
BLUE_L    = "#9DBBD6"
GREEN     = "#3E7D55"
GREEN_L   = "#A7C9B2"
RED       = "#A8352E"
RED_L     = "#E0A9A4"
AMBER     = "#D89A2E"
SEA       = "#CFE3EA"   # water fill
LAND      = "#F2EEE4"

CAT = [TEAL_D, TERRA, BLUE, GOLD, GREEN, PLUM, TEAL_L, RED]
SEQ = ["#EDF4F3", "#CFE4E1", "#A8CFCA", "#79B5AF", "#4E9993", "#2B7A74", "#14544F"]
DIV = ["#2B7A74", "#79B5AF", "#CFE4E1", "#F4EFE6", "#F0CFA8", "#DD9E62", "#C1622F"]

plt.rcParams.update({
    "figure.dpi": 150,
    "savefig.dpi": 150,
    "font.family": "DejaVu Sans",
    "font.size": 8.5,
    "text.color": INK,
    "axes.edgecolor": RULE,
    "axes.labelcolor": INK_SOFT,
    "axes.titlecolor": INK,
    "axes.linewidth": 0.7,
    "axes.grid": False,
    "xtick.color": INK_SOFT,
    "ytick.color": INK_SOFT,
    "xtick.labelsize": 7.8,
    "ytick.labelsize": 7.8,
    "legend.frameon": False,
    "legend.fontsize": 7.8,
    "svg.fonttype": "path",
    "figure.facecolor": PAPER,
    "axes.facecolor": PAPER,
})

OUT = "/home/user/NetflixProject/godcity_research/figs"

def frame(ax, left=True, bottom=True, grid="y", grid_alpha=1.0):
    """Minimal axis frame: hairline grid behind, only needed spines."""
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_visible(left)
    ax.spines["bottom"].set_visible(bottom)
    if grid in ("y", "both"):
        ax.yaxis.grid(True, color=RULE, lw=0.6, alpha=grid_alpha)
    if grid in ("x", "both"):
        ax.xaxis.grid(True, color=RULE, lw=0.6, alpha=grid_alpha)
    ax.set_axisbelow(True)
    ax.tick_params(length=0, pad=4)

def titleblock(fig, title, subtitle=None, x=0.012, y=0.975, tsize=12.2, ssize=8.4):
    fig.text(x, y, title, ha="left", va="top", fontsize=tsize,
             fontweight="bold", color=INK)
    if subtitle:
        fig.text(x, y - 0.052, subtitle, ha="left", va="top", fontsize=ssize,
                 color=INK_SOFT, linespacing=1.45)

def source(fig, text, x=0.012, y=0.016, size=6.6):
    fig.text(x, y, text, ha="left", va="bottom", fontsize=size,
             color="#8A948F", linespacing=1.45)

def halo(txt, lw=2.2, fg=PAPER):
    txt.set_path_effects([patheffects.withStroke(linewidth=lw, foreground=fg)])
    return txt

def save(fig, name, pad=0.30):
    p = f"{OUT}/{name}.svg"
    fig.savefig(p, format="svg", bbox_inches="tight", pad_inches=pad,
                facecolor=fig.get_facecolor())
    fig.savefig(p.replace(".svg", ".png"), format="png", bbox_inches="tight",
                pad_inches=pad, facecolor=fig.get_facecolor(), dpi=110)
    plt.close(fig)
    print("wrote", name)
    return p

def rupee(v, unit=""):
    return f"₹{v:,.0f}{unit}"
