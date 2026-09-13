# God City, Sindhudurg — project and promoter research report

A 40-page independent research report on **God City LLP (LLPIN ACF-3634)** and its proposed
~150-acre integrated township in the Sindhudurg growth corridor, Maharashtra.

**Deliverable:** [`God_City_Sindhudurg_Research_Report.pdf`](God_City_Sindhudurg_Research_Report.pdf)
— A3 portrait, 40 pages, 19 original figures.

## What's in it

| Part | Covers |
|---|---|
| Opening | Seven findings; method and evidence grading |
| I — The proposition | What is offered; the LLP; the promoters; the Winsten Park / VHR Group lineage; the master planner; the disclosure ledger |
| II — The place | District fundamentals and seasonality; orientation; access by road, rail, sea and air; the catalyst pipeline graded by evidence; tourism and industry |
| III — The market | The land-value ladder; the entry ticket and competitive set; India's second-home market |
| IV — Law and land | MahaRERA; the Integrated Township Policy; s.63 and N.A. conversion; Konkan tenure traps; CRZ and the Western Ghats ESA; the ten-gate approval pathway |
| V — Economics | What "150 acres" actually contains; developer capital vs. entity capitalisation; the buyer's all-in cost and break-even |
| VI — Risk | An 18-item risk register; capability profile; SWOT |
| VII — The work | A nine-gate decision tree; a 26-task, six-workstream, six-month diligence plan; the full information request |
| VIII — Conclusion | Six verdicts by participant type; the triggers that would change them |
| Appendices | Fact register with source and grade for every material claim; glossary; sources; method and limitations |

## Figures

1. Sindhudurg orientation map — corridor assets
2. Travel-time compression by mode
3. Chipi airport traffic — growth rate vs. absolute base
4. Infrastructure catalyst Gantt, graded by evidence class
5. Land-value heatmap — taluka × product tier
6. Entry-ticket comparison — the same 600 sq yd, six ways
7. Disclosure evidence ledger
8. Corporate structure and the missing counterparty
9. Capability radar vs. what a 150-acre township demands
10. Risk register — likelihood × impact
11. SWOT
12. The ten-gate regulatory approval pathway
13. Nine-gate buyer decision tree
14. Six-month diligence work plan (Gantt)
15. Land budget behind the "150 acres"
16. Capital requirement waterfall vs. LLP contribution
17. Buyer arithmetic — all-in cost and break-even scenarios
18. District fundamentals and rainfall seasonality
19. Verdict scorecard by participant type

## Rebuilding

```bash
pip install matplotlib numpy playwright
python3 src/f01_map.py            # ... and each other f*.py, writing into figs/
python3 src/render.py God_City_Sindhudurg_Research_Report.pdf
```

`src/style.py` holds the shared figure design system. `report.html` + `report.css` are the
document; `src/render.py` prints it to PDF via headless Chromium with page footers.

## Scope

Public-domain sources only, compiled February 2026. No site visit, no interviews, no document
inspection — because no site has been publicly identified. Every material claim carries a source
and an evidence grade in Appendix A. "Not found in the public domain" means a search returned
nothing; it is not a finding that a document does not exist. This is research, not investment,
legal or tax advice. See Appendix D for the full limitations.
