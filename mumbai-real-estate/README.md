# Mumbai Real Estate — Entry, Intelligence & Execution System (v2.0)

A corrected, re-researched and considerably expanded replacement for the uploaded
*Mumbai Real Estate Final Strategy Report* (v1.0), its Excel workbook, CSV repository,
graphs pack and heatmaps pack.

**Research date: 14 August 2026.** Every market and regulatory fact was re-verified
against a primary or major-consultancy source on that date.

---

## Deliverables

| File | What it is |
|---|---|
| `report/Mumbai_Real_Estate_Master_Playbook_2026.pdf` | **The main deliverable.** 60 pages, A4 landscape, 33 figures. |
| `report/report.html` | The same document as HTML (source for the PDF). |
| `Mumbai_Real_Estate_Operating_System_v2.xlsx` | 18-sheet operating workbook — reference, model and working sheets, with live formulas and validation. |
| `figures/` | 33 publication-quality figures at 200 dpi. |
| `data/` | 20 machine-readable CSVs — the full evidence base. |
| `build/` | Everything above is generated from source. |

## The single-source-of-truth rule

`build/evidence.py` holds every fact, weight, score and assumption used anywhere in
this pack, each carried with its source id, observation date and confidence grade.
The report, the figures, the CSVs and the workbook are all generated from it.

This exists because the v1 pack contradicted itself: the PDF narrative, the Excel
workbook and the CSV repository disagreed on both the priority scores and the
recommended entry corridor. Three artefacts disagreeing on the headline recommendation
destroys the credibility of the whole system.

**Never edit the CSVs, the figures or the workbook directly. Edit `evidence.py` and rebuild.**

## Rebuilding

```bash
cd build
make all          # data + figures + workbook + report + pdf
```

Or individually:

```bash
python3 export_data.py       # -> ../data/*.csv
python3 fig_market.py        # -> ../figures/A*.png
python3 fig_strategy.py      # -> ../figures/B*.png
python3 fig_work.py          # -> ../figures/C*.png
python3 fig_econ.py          # -> ../figures/D*.png
python3 fig_system.py        # -> ../figures/E*.png
python3 build_workbook.py    # -> ../Mumbai_Real_Estate_Operating_System_v2.xlsx
python3 build_report.py      # -> ../report/report.html
make pdf                     # -> ../report/*.pdf  (headless Chromium)
```

Requirements: `python3`, `matplotlib`, `numpy`, `openpyxl`, `Pillow`, the Inter font,
and a Chromium binary for the PDF step.

## What changed from version 1

Fourteen substantive corrections, set out in full on pages 5–6 of the report and in
`data/corrections_ledger.csv`. The material ones:

**Regulatory changes that post-date the original research**

- **Certificate of Competency is now mandatory** (January 2026). A MahaRERA agent cannot
  register or renew without completing a 20-hour programme and passing an examination
  through NAREDCO, REMI or RAGC. This is a six-week critical path and the longest-lead
  item in the venture.
- **Advertisement disclosure order** — QR code, registration number and website must
  appear top-right on every advertisement, at ₹10,000–50,000 per violation. A WhatsApp
  pocket brief is an advertisement.
- **Half-yearly agent compliance reporting** is now required, with penalties for delay
  and possible suspension.
- **DPDP Rules** were notified on 13 November 2025 and phase in to approximately
  mid-May 2027. There is no small-business exemption.

**Analytical corrections**

- Unsold inventory direction was inverted in v1 ("down 4%"); it rose 4% YoY to 525,695
  units across the top eight markets, with Mumbai holding 157,410.
- Absorption metrics (QTS 6.5 quarters, inventory age 13.5 quarters) were missing entirely.
- Infrastructure was scored without regard to status; an announced asset and an operating
  one carried equal weight. A status-weighted ladder now replaces that.
- The priority model's weights and scores disagreed across three artefacts. One weight
  vector and one score table now generate all of them, with sensitivity testing.
- Workbook yield mechanics used a 650 sq ft placeholder producing 4.2–5.8% gross yields
  for Powai, roughly 40% above the observable band.

**Material additions**

- A workload model: 2,860 founder-hours allocated across six workstreams and twelve months.
- A work breakdown structure of 24 assignable packages.
- A funnel model in three scenarios, unit economics, and a cash-runway model that states
  the capital requirement (₹11.3 lakh against the conservative case).
- A quantified risk register, a KPI tree, lead-channel economics and five operating playbooks.

## Headline recommendation

Enter through the **Eastern & Central Suburbs** — Powai, Kanjurmarg, Vikhroli, Bhandup,
Mulund, Ghatkopar. Five localities, 20–30 pockets, frozen for ninety days. It scores 8.00
of 10 on the corrected model and stays first under 99% of randomised weightings, winning
not by leading any single criterion but by having no weak one.

Expansion order thereafter: Thane, then Navi Mumbai, then the Western Suburbs — and only
at month 8, and only if corridor-1 closures happen without the founder present at every step.

## Confidence grading

| Grade | Meaning |
|---|---|
| **high** | Primary, statutory, or published major-consultancy figure |
| **medium** | Reputable secondary reporting, or a consultancy figure via press |
| **low** | Portal or asking-price aggregate — directional only, never client-facing |
| **model** | Analyst construct or planning assumption — **not** a market statistic |

Every figure states its confidence in the footnote. Every fact carries a `[SRC-nnn]` tag
resolving to the registry in appendix G1 of the report and in `data/source_registry.csv`.

## Disclaimer

This is not legal, tax or investment advice. Regulatory, tax and compliance positions must
be confirmed with a qualified professional before you act on them. Market figures move —
re-verify each against its source before relying on it.
