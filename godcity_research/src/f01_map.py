import sys; sys.path.insert(0, "/home/user/NetflixProject/godcity_research/src")
from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, FancyArrow, FancyBboxPatch

# ------------------------------------------------ stylised district outline
coast = [(73.33,16.62),(73.34,16.52),(73.37,16.42),(73.385,16.36),(73.41,16.27),
         (73.435,16.18),(73.445,16.11),(73.46,16.05),(73.485,15.98),(73.52,15.93),
         (73.575,15.89),(73.605,15.85),(73.618,15.79),(73.635,15.72),(73.66,15.66)]
east  = [(73.66,15.66),(73.80,15.655),(73.93,15.665),(74.00,15.72),(74.05,15.80),
         (74.09,15.90),(74.11,16.02),(74.14,16.14),(74.17,16.28),(74.13,16.40),
         (74.06,16.50),(73.92,16.58),(73.74,16.63),(73.56,16.645),(73.43,16.64),(73.33,16.62)]
poly = coast + east

TOWNS = [  # lon, lat, name, kind
 (73.822,15.902,"Sawantwadi","town"),
 (73.688,16.010,"Kudal","town"),
 (73.676,16.058,"Oros / Sindhudurgnagari\n(District HQ)","hq"),
 (73.712,16.268,"Kankavli","town"),
 (73.792,16.512,"Vaibhavwadi","town"),
 (73.383,16.381,"Devgad","town"),
 (73.468,16.060,"Malvan","town"),
 (73.632,15.862,"Vengurla","town"),
 (73.958,15.752,"Dodamarg","town"),
]
ASSETS = [
 (73.529,15.999,"Sindhudurg Airport\n(Chipi · SDW)","air"),
 (73.862,15.744,"Manohar Intl. Airport\n(Mopa · GOX), Goa","air2"),
 (73.470,16.020,"Tarkarli / Sindhudurg Fort","tour"),
 (73.505,15.930,"Nivati Rocks — Ex-INS Guldar\nunderwater museum + submarine","tour"),
 (73.618,15.782,"Shiroda–Velagar\nIHCL / Taj site","hosp"),
 (73.330,16.560,"Vijaydurg — Ro-Ro\nferry terminal","port"),
 (73.874,15.872,"Adali MIDC\n(proposed Pharma Hub)","ind"),
 (73.905,15.828,"Nandos — proposed\n200-acre Film City","film"),
]
RAIL = [(73.795,16.62),(73.760,16.46),(73.735,16.30),(73.712,16.16),
        (73.700,16.04),(73.720,15.95),(73.800,15.90),(73.868,15.80),(73.905,15.70)]
NH66 = [(73.735,16.62),(73.712,16.44),(73.695,16.27),(73.678,16.10),(73.690,15.99),
        (73.760,15.93),(73.840,15.87),(73.900,15.78),(73.940,15.69)]

fig = plt.figure(figsize=(9.9, 7.6))
ax = fig.add_axes([0.028, 0.050, 0.585, 0.790])
rail = fig.add_axes([0.640, 0.050, 0.348, 0.790]); rail.axis("off")
ax.set_facecolor(SEA)

ax.add_patch(Polygon(poly, closed=True, facecolor=LAND, edgecolor=TEAL_D,
                     lw=1.5, zorder=2))
# Western Ghats hatch band along the east
ghat = [(73.98,15.70),(74.05,15.80),(74.09,15.90),(74.11,16.02),(74.14,16.14),
        (74.17,16.28),(74.13,16.40),(74.06,16.50),(73.92,16.58),
        (73.93,16.44),(73.96,16.26),(73.96,16.08),(73.94,15.92),(73.93,15.78)]
ax.add_patch(Polygon(ghat, closed=True, facecolor=GREEN_L, edgecolor="none",
                     alpha=0.75, zorder=3))
ax.text(74.045,16.22,"WESTERN GHATS\n(Eco-Sensitive Area)", fontsize=6.7,
        color="#2F5C41", rotation=-74, ha="center", va="center",
        fontweight="bold", zorder=4, linespacing=1.4)

# Arabian Sea + CRZ 200 m NDZ indication
ax.text(73.365,15.86,"ARABIAN  SEA", fontsize=9.6, color="#5D8A98",
        fontweight="bold", rotation=-62, ha="center", va="center", zorder=3)
cx = [(p[0]-0.028, p[1]) for p in coast]
ax.plot(*zip(*cx), color=RED, lw=1.0, ls=(0,(3,2)), zorder=5, alpha=0.85)
ax.text(73.398,16.30,"CRZ-III B · 200 m No-Development Zone", fontsize=6.4,
        color=RED, rotation=-73, ha="center", va="center", zorder=6,
        fontweight="bold")

# Goa border
ax.plot([73.655,73.79,73.90,73.99],[15.655,15.648,15.660,15.712],
        color=PLUM, lw=1.8, zorder=5)
ax.text(73.80,15.605,"GOA  ▸  (state border · Patradevi)", fontsize=7.0,
        color=PLUM, fontweight="bold", ha="center", zorder=5)
ax.text(73.62,16.66,"◂  RATNAGIRI  district", fontsize=7.0, color=INK_SOFT,
        ha="center", zorder=5)

# corridors
ax.plot(*zip(*NH66), color=TERRA, lw=3.0, zorder=6, solid_capstyle="round")
ax.plot(*zip(*NH66), color="#FFFFFF", lw=0.8, ls=(0,(4,4)), zorder=7)
ax.text(73.678,16.57,"NH-66\n4-lane", fontsize=6.8, color=TERRA,
        fontweight="bold", ha="center", va="center", zorder=8,
        bbox=dict(boxstyle="round,pad=0.22", fc=PAPER, ec=TERRA, lw=0.6))
ax.plot(*zip(*RAIL), color=INK, lw=1.6, zorder=6)
ax.plot(*zip(*RAIL), color=PAPER, lw=0.7, ls=(0,(2.2,2.2)), zorder=7)
ax.text(73.845,16.60,"Konkan\nRailway", fontsize=6.8, color=INK,
        fontweight="bold", ha="center", va="center", zorder=8,
        bbox=dict(boxstyle="round,pad=0.22", fc=PAPER, ec=INK, lw=0.6))

# ferry arrow from north-west (Mumbai)
ax.annotate("", xy=(73.345,16.552), xytext=(73.175,16.660),
            arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.8,
                            connectionstyle="arc3,rad=0.18"), zorder=6)
ax.text(73.172,16.700,"Ro-Ro ferry\nfrom Mumbai", fontsize=6.8, color=BLUE,
        fontweight="bold", ha="center", va="bottom", zorder=8, linespacing=1.4)

MARK = {"town":(dict(marker="o", ms=5.2, mfc=PAPER, mec=TEAL_D, mew=1.4), INK),
        "hq":  (dict(marker="s", ms=6.4, mfc=TEAL_D, mec=TEAL_D, mew=1.0), TEAL_D),
        "air": (dict(marker="^", ms=8.0, mfc=TERRA, mec=PAPER, mew=1.0), TERRA),
        "air2":(dict(marker="^", ms=8.0, mfc=PLUM, mec=PAPER, mew=1.0), PLUM),
        "tour":(dict(marker="D", ms=5.4, mfc=BLUE, mec=PAPER, mew=0.9), BLUE),
        "hosp":(dict(marker="*", ms=10.5, mfc=GOLD, mec="#8A6A16", mew=0.7), "#8A6A16"),
        "port":(dict(marker="P", ms=7.6, mfc=BLUE, mec=PAPER, mew=0.9), BLUE),
        "ind": (dict(marker="H", ms=7.2, mfc=GREEN, mec=PAPER, mew=0.9), GREEN),
        "film":(dict(marker="p", ms=8.0, mfc=RED, mec=PAPER, mew=0.9), RED)}

OFF = {"Sawantwadi":(0.030,0.016,"left"),"Kudal":(-0.026,0.012,"right"),
       "Oros / Sindhudurgnagari\n(District HQ)":(0.026,0.020,"left"),
       "Kankavli":(0.028,0.006,"left"),"Vaibhavwadi":(0.028,0.006,"left"),
       "Devgad":(0.026,0.010,"left"),"Malvan":(-0.024,-0.030,"right"),
       "Vengurla":(-0.026,-0.026,"right"),"Dodamarg":(0.028,0.004,"left")}

for lon, lat, name, kind in TOWNS:
    st, col = MARK[kind]
    ax.plot([lon],[lat], zorder=10, **st)
    dx, dy, ha = OFF[name]
    halo(ax.text(lon+dx, lat+dy, name, fontsize=7.4, color=col, ha=ha,
                 va="center", fontweight="bold" if kind=="hq" else "normal",
                 zorder=11, linespacing=1.35))

AOFF = {"air":(0.0,-0.062,"center"),"air2":(0.030,-0.030,"left"),
        "tour":(-0.028,0.020,"right"),"hosp":(-0.028,-0.008,"right"),
        "port":(0.030,0.014,"left"),"ind":(0.030,0.014,"left"),
        "film":(0.032,-0.024,"left")}
for lon, lat, name, kind in ASSETS:
    st, col = MARK[kind]
    ax.plot([lon],[lat], zorder=10, **st)
    dx, dy, ha = AOFF[kind]
    if name.startswith("Tarkarli"): dx, dy, ha = -0.030, 0.030, "right"
    if name.startswith("Nivati"):   dx, dy, ha = -0.030, -0.036, "right"
    halo(ax.text(lon+dx, lat+dy, name, fontsize=6.8, color=col, ha=ha,
                 va="center", fontweight="bold", zorder=11, linespacing=1.35))

# ---- indicative catchment rings around the Chipi / Mopa axis
for r, lab in [(0.18,"~20 km"), (0.36,"~40 km")]:
    ax.add_patch(Circle((73.70,15.94), r, fill=False, ec=TEAL, lw=0.8,
                        ls=(0,(2,3)), alpha=0.55, zorder=4))
ax.text(73.70+0.255,15.94+0.255,"indicative\n20 / 40 km\ncatchment", fontsize=6.2,
        color=TEAL, ha="center", va="center", zorder=5, linespacing=1.4)

# ---- "site not disclosed" callout over the Kudal–Sawantwadi corridor
ax.add_patch(FancyBboxPatch((73.206,16.258), 0.116, 0.286,
            boxstyle="round,pad=0.010", fc="#FFF6E8", ec=AMBER, lw=1.0, zorder=12))
ax.text(73.264,16.487,"?", fontsize=15, color=AMBER, fontweight="bold",
        ha="center", va="center", zorder=13)
ax.text(73.264,16.414,"site not\nplottable\nfrom public\nrecord", fontsize=6.1,
        color="#8A5F0B", ha="center", va="top", fontweight="bold",
        zorder=13, linespacing=1.5)

ax.set_xlim(73.20, 74.26); ax.set_ylim(15.55, 16.78)
ax.set_aspect(1/np.cos(np.deg2rad(16.1)))
ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_color(RULE)

# north arrow + scale bar
ax.annotate("", xy=(74.205,16.71), xytext=(74.205,16.580),
            arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.3), zorder=12)
ax.text(74.205,16.735,"N", fontsize=8.4, fontweight="bold", ha="center", zorder=12)
ax.plot([73.985,73.985+0.2088],[15.600,15.600], color=INK, lw=2.2, zorder=12)
ax.text(74.089,15.622,"≈ 20 km", fontsize=6.6, ha="center", color=INK, zorder=12)

handles = [
 plt.Line2D([],[],ls="none",marker="^",ms=7,mfc=TERRA,mec=PAPER,label="Sindhudurg (Chipi) airport"),
 plt.Line2D([],[],ls="none",marker="^",ms=7,mfc=PLUM,mec=PAPER,label="Mopa airport (Goa)"),
 plt.Line2D([],[],ls="none",marker="s",ms=6,mfc=TEAL_D,mec=TEAL_D,label="District HQ"),
 plt.Line2D([],[],ls="none",marker="o",ms=5,mfc=PAPER,mec=TEAL_D,label="Taluka town"),
 plt.Line2D([],[],ls="none",marker="*",ms=10,mfc=GOLD,mec="#8A6A16",label="IHCL / Taj hotel site"),
 plt.Line2D([],[],ls="none",marker="D",ms=5,mfc=BLUE,mec=PAPER,label="Marine / heritage tourism"),
 plt.Line2D([],[],ls="none",marker="H",ms=6.5,mfc=GREEN,mec=PAPER,label="MIDC industrial area"),
 plt.Line2D([],[],ls="none",marker="p",ms=7,mfc=RED,mec=PAPER,label="Proposed Film City"),
 plt.Line2D([],[],ls="none",marker="P",ms=7,mfc=BLUE,mec=PAPER,label="Ro-Ro ferry terminal"),
 plt.Line2D([],[],color=TERRA,lw=3,label="NH-66 (Mumbai–Goa)"),
 plt.Line2D([],[],color=INK,lw=1.6,label="Konkan Railway"),
 plt.Line2D([],[],color=RED,lw=1.0,ls=(0,(3,2)),label="CRZ 200 m NDZ (indicative)"),
]
rail.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.0, 1.0),
            ncol=1, fontsize=7.4, handletextpad=0.7, labelspacing=0.74,
            frameon=False)
rail.text(0.0, 0.585, "WHY THIS CORRIDOR IS BEING MARKETED",
          fontsize=7.6, fontweight="bold", color=TEAL_D, transform=rail.transAxes)
rail.plot([0.0, 1.0], [0.566, 0.566], color=RULE, lw=0.8,
          transform=rail.transAxes, clip_on=False)
rows = [
 ("Mopa (GOX) intl. airport", "≈14 km from Sawantwadi"),
 ("Chipi (SDW) airport", "in-district, Vengurla tal."),
 ("NH-66 four-laning", "district stretch ~99% done"),
 ("Konkan Rly stations", "Kudal · Sindhudurg · Kankavli"),
 ("Ro-Ro ferry (Vijaydurg)", "live since 1 Mar 2026"),
 ("IHCL/Taj · Shiroda", "tripartite pact signed"),
 ("Submarine + reef museum", "Ex-INS Guldar sunk 19 May 2026"),
 ("Film City · Nandos", "proposed, ~200 acres"),
 ("Adali MIDC pharma hub", "proposed, infra laid"),
]
y = 0.527
for k, v in rows:
    rail.text(0.0, y, "▪", fontsize=5.6, color=TERRA, transform=rail.transAxes)
    rail.text(0.045, y, k, fontsize=7.0, color=INK, transform=rail.transAxes,
              fontweight="bold", va="baseline")
    rail.text(0.520, y, v, fontsize=6.7, color=INK_SOFT,
              transform=rail.transAxes, va="baseline")
    y -= 0.0385
rail.add_patch(mpatches.FancyBboxPatch((0.0, 0.012), 1.0, 0.178,
    boxstyle="round,pad=0.010", fc="#FFF6E8", ec=AMBER, lw=0.9,
    transform=rail.transAxes, clip_on=False))
rail.text(0.028, 0.176,
  "Every item above is a real, separately sourced development — and not\n"
  "one is an approval held by, or a commitment made by, God City LLP.\n"
  "They are the regional backdrop the sales narrative borrows. Project-\n"
  "level diligence is a different exercise, and as of February 2026 there\n"
  "is no public village, survey number, layout, price list or MahaRERA\n"
  "registration to run it against.",
  fontsize=6.5, color="#7A5409", transform=rail.transAxes, va="top",
  linespacing=1.62)

titleblock(fig, "Figure 1 · Sindhudurg district — orientation and the growth-corridor assets that frame God City",
  "Schematic map. Positions are approximate and indicative only — this is an orientation aid, not a survey or "
  "cadastral document.\nGod City is marketed as sitting in the “Sindhudurg growth corridor”; the promoter has "
  "not published a village, gat/survey number or site plan, so\nthe site itself cannot be plotted. The "
  "Kudal–Sawantwadi–Mopa axis shown is where the corridor narrative points.")
source(fig, "Sources: Sindhudurg district administration and Census 2011 for administrative geography; NHAI/MSRDC and Konkan Railway for corridors; MTDC/IHCL, MIDC and "
            "Maharashtra Tourism for project sites; CRZ Notification 2019 and the\nSindhudurg CZMP (approved 2023) for the No-Development Zone concept. Compiled Feb 2026. "
            "CRZ line is conceptual — the statutory line is fixed by the approved CZMP map read against the High Tide Line, survey number by survey number.")
save(fig, "f01_orientation_map")
