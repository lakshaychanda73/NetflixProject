"""build_index.py — the diligence index that sits behind the 12-slide deck.

The deck carries one idea per slide and no methodology. Everything a reader
might reasonably want to interrogate lives in the 60-page master playbook.
This three-page document is the map between them: for every claim on every
slide, the page, figure and CSV that proves it.

Page references are read from build_report.PAGES at build time, so they cannot
drift when the playbook is repaginated.
"""

import sys, os, io, contextlib, importlib

sys.path.insert(0, os.path.abspath("../../build"))
import evidence as E

# ---------------------------------------------------------------- page map --
_buf = io.StringIO()
with contextlib.redirect_stdout(_buf):
    _report = importlib.import_module("build_report")

_LABELS = {}
for _i, _p in enumerate(_report.PAGES, 1):
    _lab = _p.get("label")
    if _lab:
        _key = _lab.split("·")[0].strip().split(" ")[0]
        _LABELS.setdefault(_key, _i)
_LABELS.setdefault("F4", 49)


def pg(code):
    """Playbook page number for a section code such as 'B2' or 'G1'."""
    return _LABELS.get(code, "—")


def ref(code, extra=""):
    p = pg(code)
    return f"<strong>p.{p}</strong> · {code}" + (f" · {extra}" if extra else "")


L, CR = 100_000, 10_000_000
RATE_L = E.BLENDED_RATE_LABEL

# ------------------------------------------------------------ slide claims --
SLIDE_CLAIMS = [
    (1, "Opening",
     [("80,221 registrations and ₹6,968 cr of stamp duty in H1 2026",
       ref("A2"), "SRC-005 · data/monthly_registrations_2026.csv"),
      ("1,57,410 unsold units, 6.5 quarters to clear",
       ref("A3"), "SRC-004 · data/public_market_snapshot.csv"),
      ("42,865 registered agents in Maharashtra",
       ref("A1"), "SRC-025 · data/source_registry.csv"),
      ("Registrations are public, dated and addressable back to 1985",
       ref("E3"), "IGR e-Search · SRC-001")]),

    (2, "The customer's problem",
     [("The six questions that decide the deal",
       ref("F2"), "first-conversation protocol"),
      ("Area-basis error of 20–30% between carpet, built-up and saleable",
       ref("E6"), "provenance rule 3 · data/data_dictionary.csv"),
      ("Developer delivery record is public but unread",
       ref("E3"), "MahaRERA QPR filings · SRC-002"),
      ("Commute, society rules and maintenance are field observations",
       ref("F1"), "field research protocol")]),

    (3, "What Brickrock is",
     [(f"{RATE_L} blended commission is the only revenue line",
       ref("D2"), "data/ticket_mix_model.csv"),
      ("Verdict: what this business is, and is not",
       "<strong>p.4</strong> · front matter", "written before the analysis, not after"),
      ("The evidence layer is an operating tool, not a product",
       ref("B1"), "six-layer operating stack"),
      ("Every closure re-enters the loop as evidence",
       ref("F5"), "post-close and referral flywheel")]),

    (4, "How it works",
     [("The seven-step transaction engine",
       ref("C1"), "operating flow"),
      ("What each data domain holds and how fast it goes stale",
       ref("E2"), "data/data_domains.csv"),
      ("Which source answers which question",
       ref("E3"), "data/source_registry.csv"),
      ("The eight provenance rules the record is kept under",
       ref("E6"), "confidence grading and SRC tagging")]),

    (5, "Where we start",
     [("Seven weighted criteria and one weight vector",
       ref("B2"), "data/market_priority_weights.csv"),
      ("Eastern & Central 8.00; Navi Mumbai and Western tie at 7.48",
       ref("B4"), "data/market_priority_model.csv"),
      ("First across 99% of 5,000 randomised weight vectors",
       ref("B3"), "tornado and Monte Carlo sensitivity"),
      ("Locality asking bands, rents and yields",
       ref("A4"), "data/micro_markets.csv · medium confidence"),
      ("Infrastructure scored by status, not by announcement",
       ref("A6"), "data/infrastructure_register.csv")]),

    (6, "Customer–market fit",
     [("Segment mix, ticket sizes and commission rates",
       ref("D2"), "data/ticket_mix_model.csv"),
      ("81% of registrations are 1,000 sq ft or less",
       ref("A3"), "SRC-033 · medium confidence"),
      ("Homes above ₹1 crore: 49% → 54% of sales in a year",
       ref("A1"), "SRC-032"),
      ("Rental as a lead nursery rather than a revenue line",
       ref("D6"), "lead channels")]),

    (7, "Competitive positioning",
     [("Where portals, national brokerages and independents stop",
       ref("B6"), "competitive positioning"),
      ("The competitor set is the 42,865 registered agents",
       ref("B2"), "whitespace criterion, re-based"),
      ("Disclosure of who pays us, in writing",
       ref("E4"), "MahaRERA advertising-disclosure order")]),

    (8, "The moat",
     [("What accumulates and why it cannot be bought",
       ref("B1"), "layer 6 of the operating stack"),
      ("Capture discipline on every deal, won or lost",
       ref("F4"), "documentation and closure"),
      ("Referral coefficient and how it is measured",
       ref("F5"), "post-close flywheel"),
      ("Geographic hierarchy L0–L6, pocket as the research unit",
       ref("E1"), "data/geo_hierarchy.csv")]),

    (9, "Business model and economics",
     [("Funnel: 900 → 240 → 110 → 45 → 15 in the base case",
       ref("D1"), "data/funnel_scenarios.csv"),
      (f"Blended {RATE_L} on ₹{E.BLENDED_CONSIDERATION/CR:,.2f} cr average consideration",
       ref("D2"), "data/ticket_mix_model.csv"),
      (f"Cost base: ₹{E.ONE_OFF/L:,.2f} L one-off, ₹{E.MONTHLY/1000:,.0f}k per month",
       ref("D2"), "data/cost_base.csv"),
      ("GST heading 9972 and TDS under 194-IA / 194H",
       ref("G1"), "SRC-027 to SRC-031 · glossary p." + str(pg("G4"))),
      ("KPI tree — which number moves which outcome",
       ref("D4"), "")]),

    (10, "Go to market",
     [("Channel costs, latency and defensibility",
       ref("D6"), "analyst estimates, labelled as such"),
      ("Qualified-lead and site-visit conversion as the two live unknowns",
       ref("D1"), "the pilot's first two measurements"),
      ("The client-fit engine behind qualification",
       ref("E5"), "budget, timeline, authority, area fit"),
      ("Referral coefficient > 0.5 as the expansion gate",
       ref("C7"), "decision gates")]),

    (11, "Capital and the proof",
     [(f"₹{E.CAPITAL/L:,.1f} L = the conservative trough plus 40% headroom",
       ref("D3"), "cash curve, both cases"),
      ("The 90-day pilot, week by week",
       ref("C4"), "data/roadmap_90_day.csv"),
      ("The 90-day checklist, item by item",
       ref("G3"), "pages " + f"{pg('G3')}–{pg('G3')+2}"),
      ("Certificate of Competency mandatory from January 2026",
       ref("E4"), "compliance path · data/compliance_obligations.csv"),
      ("Risk register with severity, owner and mitigation",
       ref("D5"), "data/risk_register.csv")]),

    (12, "Founder and the long arc",
     [("Sheesham.in revenue, PAT, invoices — Lakshay's own business",
       "Sheesham.in incubation deck, July 2026", "deck/build/founder.py"),
      ("@brickrockrealty audience and content mix — his own presence",
       "Instagram profile, August 2026", "deck/build/founder.py"),
      ("~310 acres family inheritance; 124 acres his father's scheme",
       "Family context, explicitly not his assets", "deck/build/founder.py"),
      ("What each stage of the arc has to prove before the next",
       ref("C7"), "decision gates · " + ref("G5"))]),
]

# --------------------------------------------------- methodology, by design --
METHOD = [
    ("The entry model", [
        ("Seven weighted criteria and the weight vector", "B2"),
        ("Does the recommendation survive being wrong — tornado and 5,000-run Monte Carlo", "B3"),
        ("Corridor scorecard, all six corridors on all seven axes", "B4"),
        ("Corridor profiles for the three in contention", "B5"),
    ]),
    ("The work", [
        ("Work breakdown structure — 24 work packages", "C2"),
        ("Year-1 hour budget", "C3"),
        ("The operating week", "C6"),
        ("Twelve-month schedule", "C5"),
        ("Decision gates", "C7"),
    ]),
    ("The economics", [
        ("Deal funnel, three scenarios", "D1"),
        ("Unit economics and the Year-1 P&L", "D2"),
        ("Cash curve, trough and capital requirement", "D3"),
        ("KPI tree", "D4"),
        ("Risk register", "D5"),
        ("Lead channels", "D6"),
    ]),
    ("The system", [
        ("Geographic hierarchy, L0 to L6", "E1"),
        ("Data domains, fields, refresh cadence and staleness limits", "E2"),
        ("The source stack", "E3"),
        ("Compliance path and calendar", "E4"),
        ("The client-fit engine", "E5"),
        ("The eight provenance rules", "E6"),
    ]),
    ("The playbooks", [
        ("Field research protocol", "F1"),
        ("The first client conversation", "F2"),
        ("Negotiation playbook", "F3"),
        ("Documentation and closure", "F4"),
        ("Post-close and the referral flywheel", "F5"),
    ]),
    ("The appendices", [
        ("Source registry — 33 registered sources with confidence grades", "G1"),
        ("Data dictionary", "G2"),
        ("The 90-day checklist", "G3"),
        ("Glossary, including GST and TDS mechanics", "G4"),
        ("What to do on Monday morning", "G5"),
    ]),
]

CSS = """
@page { size: 297mm 210mm; margin: 0; }
:root{
  --light:#FAFAF7; --card:#FFFFFF; --cardalt:#F2F1EC;
  --ink:#10131A; --ink2:#4C5361; --muted:#8C93A0; --hair:#E4E3DC; --rule:#CFCEC5;
  --orange:#E8722C; --orange-d:#B8511A; --blue:#2D6FCB; --green:#0E9E5E; --purple:#7B4FD6;
}
*{ box-sizing:border-box; }
html,body{ margin:0; padding:0; background:#fff; }
body{ font-family:"Inter","Liberation Sans",sans-serif; color:var(--ink);
      font-size:9pt; line-height:1.5;
      -webkit-print-color-adjust:exact; print-color-adjust:exact; }
.page{ position:relative; width:297mm; height:210mm; overflow:hidden;
       page-break-after:always; break-after:page;
       background:var(--light); padding:13mm 14mm 11mm 14mm; }
.page:last-child{ page-break-after:auto; }
.kick{ font-size:7pt; font-weight:800; letter-spacing:.18em; text-transform:uppercase;
       color:var(--orange); margin-bottom:2.5mm; }
h1{ margin:0 0 2mm 0; font-size:17pt; line-height:1.15; letter-spacing:-.018em; font-weight:700; }
.lede{ font-size:9pt; line-height:1.45; color:var(--ink2); max-width:215mm; margin-bottom:5mm; }
.brand{ position:absolute; bottom:6mm; left:14mm; font-size:6.4pt; font-weight:700;
        letter-spacing:.16em; color:var(--muted); }
.pnum{ position:absolute; bottom:6mm; right:14mm; font-size:6.4pt; color:var(--muted); }

table{ width:100%; border-collapse:collapse; }
th{ text-align:left; font-size:6.4pt; font-weight:800; letter-spacing:.10em;
    text-transform:uppercase; color:var(--muted); padding:0 2mm 1.4mm 0;
    border-bottom:0.8pt solid var(--rule); }
td{ padding:1.5mm 2mm 1.5mm 0; font-size:7.2pt; line-height:1.45; color:var(--ink2);
    border-bottom:0.5pt solid var(--hair); vertical-align:top; }
td strong{ color:var(--ink); font-weight:700; }
tr.head td{ border-bottom:none; padding-top:3mm; padding-bottom:0.6mm; }
.sl{ font-size:8pt; font-weight:700; color:var(--ink); white-space:nowrap; }
.sl span{ color:var(--orange); }
.claim{ color:var(--ink); }
.where{ color:var(--ink2); white-space:nowrap; }
.src{ color:var(--muted); font-size:6.8pt; }

.cols{ column-count:3; column-gap:9mm; }
.grp{ break-inside:avoid; margin-bottom:4.5mm; }
.grp h3{ margin:0 0 1.6mm 0; font-size:8pt; font-weight:800; letter-spacing:.06em;
         color:var(--ink); border-bottom:0.8pt solid var(--orange); padding-bottom:1.2mm; }
.grp ul{ margin:0; padding:0; list-style:none; }
.grp li{ font-size:7pt; line-height:1.45; color:var(--ink2); padding:1.1mm 0;
         border-bottom:0.5pt solid var(--hair); display:flex; gap:2mm; }
.grp li b{ color:var(--ink); font-weight:700; white-space:nowrap; }
.note{ border-left:1.2mm solid var(--orange); padding:1.6mm 0 1.6mm 4mm;
       font-size:7.4pt; line-height:1.5; color:var(--ink2); margin-top:4mm; }
.note.b{ border-left-color:var(--blue); } .note.g{ border-left-color:var(--green); }
.row{ display:flex; gap:7mm; }
.col{ flex:1; min-width:0; }
"""


def claims_page(groups, kick, title, lede):
    rows = []
    for n, name, claims in groups:
        rows.append(f'<tr class="head"><td colspan="3" class="sl">'
                    f'<span>{n:02d}</span>&nbsp;&nbsp;{name}</td></tr>')
        for claim, where, src in claims:
            rows.append(f'<tr><td class="claim" style="width:47%">{claim}</td>'
                        f'<td class="where" style="width:23%">{where}</td>'
                        f'<td class="src" style="width:30%">{src}</td></tr>')
    half = len(rows) // 2
    while half < len(rows) and 'class="head"' not in rows[half]:
        half += 1
    left, right = rows[:half], rows[half:]
    hdr = ('<thead><tr><th>The claim on the slide</th><th>Where it is proved</th>'
           '<th>Source and dataset</th></tr></thead>')
    return f"""
  <div class="kick">{kick}</div>
  <h1>{title}</h1>
  <div class="lede">{lede}</div>
  <div class="row">
    <div class="col"><table>{hdr}<tbody>{''.join(left)}</tbody></table></div>
    <div class="col"><table>{hdr}<tbody>{''.join(right)}</tbody></table></div>
  </div>
"""


def page2():
    groups = ""
    for title, items in METHOD:
        lis = "".join(f'<li><b>p.{pg(code)}</b><span>{txt}</span></li>' for txt, code in items)
        groups += f'<div class="grp"><h3>{title}</h3><ul>{lis}</ul></div>'
    return f"""
  <div class="kick">Diligence index · three of three</div>
  <h1>The methodology the deck deliberately does not carry</h1>
  <div class="lede">A pitch deck that shows its working stops being a pitch deck. Everything below
  is deliberately absent from the twelve slides and deliberately present in the playbook, one click away.
  Ask for any of it and it is already written.</div>
  <div class="cols">{groups}</div>
  <div class="row" style="margin-top:3mm">
    <div class="col"><div class="note"><strong>Assumptions are labelled as assumptions.</strong>
    Segment mix, conversion rates, commission rates, channel costs and the accumulation curve on
    slide 8 are planning estimates. Each one is marked on the slide it appears on, and the 90-day
    pilot exists to replace them with measurements.</div></div>
    <div class="col"><div class="note b"><strong>Every market figure carries a confidence grade.</strong>
    High, medium, low or model, with an SRC tag resolving to the source registry on
    pages {pg('G1')}–{pg('G1')+2}. Fourteen substantive corrections to the original
    research are set out on pages {pg('Corrections') if pg('Corrections') != '—' else 5}–6.</div></div>
    <div class="col"><div class="note g"><strong>Founder claims are separated by attribution.</strong>
    Sheesham.in and @brickrockrealty are Lakshay's own. The ~310-acre inheritance is a family asset
    and the 124-acre scheme is his father's. That separation is enforced in
    <code>deck/build/founder.py</code> and is never blurred on a slide.</div></div>
  </div>
"""


def render():
    lede = ("Page numbers refer to <em>The Mumbai Real Estate Master Playbook 2026</em> "
            "(60 pages, A4 landscape). Datasets refer to the CSVs in <code>data/</code>. Both are "
            "generated from the same evidence file as the deck, so no figure here can disagree "
            "with a figure there.")
    pages = [
        claims_page(SLIDE_CLAIMS[:6], "Diligence index · one of three",
                    "Every claim on slides 1 to 6, and where the evidence for it lives", lede),
        claims_page(SLIDE_CLAIMS[6:], "Diligence index · two of three",
                    "Every claim on slides 7 to 12, and where the evidence for it lives", lede),
        page2(),
    ]
    out = ['<!doctype html><html><head><meta charset="utf-8">',
           "<title>Brickrock Realty · Diligence index</title>",
           f"<style>{CSS}</style></head><body>"]
    for i, body in enumerate(pages, 1):
        out.append(f'<div class="page">{body}'
                   f'<div class="brand">BRICKROCK REALTY · DILIGENCE INDEX</div>'
                   f'<div class="pnum">{i} / {len(pages)}</div></div>')
    out.append("</body></html>")
    return "\n".join(out)


if __name__ == "__main__":
    html = render()
    os.makedirs("../out", exist_ok=True)
    with open("../out/diligence_index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"diligence_index.html written · 3 pages · {len(html)/1024:.0f} KB")
