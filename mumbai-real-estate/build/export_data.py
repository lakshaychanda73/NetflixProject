"""export_data.py — regenerate the machine-readable repository from evidence.py.

Everything in ../data/ is generated. Edit evidence.py, never the CSVs.
"""

import csv, os
import evidence as E

OUT = "../data/"
os.makedirs(OUT, exist_ok=True)


def write(name, header, rows):
    with open(OUT + name, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    print(f"  {name:34s} {len(rows):3d} rows")


def main():
    print("Regenerating data repository:")

    write("source_registry.csv",
          ["source_id", "category", "source", "url", "key_fact_or_use", "refresh",
           "confidence", "accessed"],
          [[*s, E.RESEARCH_DATE] for s in E.SOURCES])

    write("public_market_snapshot.csv",
          ["metric", "value", "unit", "source_id", "observed_date", "confidence", "note"],
          [[k, f.value, f.unit, f.src, f.observed, f.confidence, f.note]
           for k, f in E.MARKET.items()])

    write("monthly_registrations_2026.csv",
          ["month", "registrations", "stamp_duty_rs_crore", "basis", "source_id"],
          [[m, r, d, b, "SRC-006" if b == "reported" else "SRC-005"]
           for m, r, d, b in E.MONTHLY_REGISTRATIONS])

    write("market_priority_model.csv",
          ["region"] + [k for k, _, _, _ in E.CRITERIA] + ["weighted_score", "rank"],
          [[r] + [E.REGION_SCORES[r][k] for k, _, _, _ in E.CRITERIA] + [sc, i + 1]
           for i, (r, sc) in enumerate(E.ranked_regions())])

    write("market_priority_weights.csv",
          ["criterion_key", "criterion", "weight", "rationale"],
          [[k, l, w, note] for k, l, w, note in E.CRITERIA])

    write("micro_markets.csv",
          ["micro_market", "corridor", "asking_psf_low", "asking_psf_high",
           "rent_2bhk_month", "gross_yield_low_pct", "gross_yield_high_pct",
           "infra_score", "note", "confidence", "source_id"],
          [[*r, "low", "SRC-027/SRC-028"] for r in E.MICRO_MARKETS])

    write("infrastructure_register.csv",
          ["asset", "catchment", "status", "milestone", "target", "confidence",
           "source_id", "scoring_weight"],
          [list(r) for r in E.INFRASTRUCTURE])

    write("geo_hierarchy.csv",
          ["level", "level_name", "example", "analysis_role"],
          [list(r) for r in E.GEO_LEVELS])

    write("data_domains.csv",
          ["domain", "phase1_minimum_fields", "refresh", "stale_after_days",
           "primary_sources", "granularity"],
          [list(r) for r in E.DOMAINS])

    write("roadmap_90_day.csv",
          ["week", "workstream", "primary_goal", "output", "gate_or_kpi", "planned_hours"],
          [list(r) for r in E.PILOT_90])

    write("roadmap_12_month.csv",
          ["workstream_label", "workstream", "start_month", "end_month", "closing_gate"],
          [list(r) for r in E.GANTT])

    write("workload_model.csv",
          ["workstream", "label"] + [f"M{i}" for i in range(1, 13)] + ["year1_hours_per_week_total"],
          [[k, l] + E.WORKLOAD[k] + [sum(E.WORKLOAD[k])] for k, l, _, _ in E.WORKSTREAMS])

    write("compliance_obligations.csv",
          ["obligation", "trigger", "cost_or_penalty", "cadence", "source_id", "criticality_1_3"],
          [list(r) for r in E.COMPLIANCE])

    write("risk_register.csv",
          ["risk", "likelihood_1_5", "impact_1_5", "severity", "early_warning",
           "control", "owner_phase"],
          [[r[0], r[1], r[2], r[1] * r[2], r[3], r[4], r[5]] for r in E.RISKS])

    write("funnel_scenarios.csv",
          ["stage", "conservative", "base", "stretch"],
          [list(r) for r in E.FUNNEL_STAGES])

    write("ticket_mix_model.csv",
          ["segment", "share_of_closures", "avg_consideration_rs", "commission_rate",
           "payout_lag_days"],
          [list(r) for r in E.TICKET_MIX])

    write("cost_base.csv",
          ["line_item", "one_off_rs", "monthly_rs", "note"],
          [list(r) for r in E.COST_BASE])

    write("corrections_ledger.csv",
          ["area", "v1_position", "v2_position", "why_it_matters", "source_id"],
          [list(r) for r in E.CORRECTIONS])

    write("data_dictionary.csv",
          ["table", "field", "type", "required", "description"],
          [
              ("geo", "geo_id", "text", "yes", "Immutable geography identifier (L0–L6)"),
              ("geo", "parent_geo_id", "text", "no", "Parent geography id"),
              ("geo", "level", "enum", "yes", "L0 / L1 / L2 / L3 / L4 / L5 / L6"),
              ("geo", "boundary_ref", "text", "no", "Verified GIS boundary reference"),
              ("pricing", "price_type", "enum", "yes", "asking / registered / ready_reckoner / launch"),
              ("pricing", "area_basis", "enum", "yes", "carpet / built_up / saleable"),
              ("pricing", "price_psf", "number", "yes", "Price per sq ft on the declared area basis"),
              ("pricing", "sample_size", "integer", "yes", "Observations behind the aggregate; n=1 is a single instrument"),
              ("rental", "monthly_rent", "number", "yes", "Monthly asking or closed rent"),
              ("rental", "configuration", "text", "yes", "1BHK / 2BHK / 3BHK etc."),
              ("rental", "furnishing", "enum", "yes", "bare / semi / full"),
              ("project", "rera_id", "text", "yes", "MahaRERA project registration id, or NOT_REGISTERED"),
              ("project", "possession_date", "date", "no", "Declared possession date from the RERA filing"),
              ("project", "qpr_ref", "text", "no", "Quarterly progress report reference"),
              ("infra", "status", "enum", "yes", "operational / commissioning / under_construction / approved / proposed / rumoured"),
              ("infra", "slippage_months", "number", "no", "Cumulative delay against the earliest published target"),
              ("infra", "last_verified", "date", "yes", "When the status was last checked against the source"),
              ("risk", "risk_type", "text", "yes", "flood / title / CRZ / environment / litigation / oversupply / infra"),
              ("risk", "severity", "enum", "yes", "low / medium / high"),
              ("fact", "source_ref", "text", "yes", "Source registry id — no fact exists without one"),
              ("fact", "observed_date", "date", "yes", "Date the fact applies to, not the date it was copied"),
              ("fact", "confidence", "enum", "yes", "high / medium / low"),
              ("fact", "stale_after_days", "integer", "yes", "Domain refresh rule, drives the freshness display"),
              ("fact", "conflict_flag", "boolean", "yes", "Marks an unresolved disagreement between sources"),
              ("lead", "lead_id", "text", "yes", "Lead identifier"),
              ("lead", "source_channel", "text", "yes", "Tagged at capture — never reconstructed later"),
              ("lead", "qualified", "boolean", "yes", "True only if budget, timeline, authority and area fit all pass"),
              ("lead", "consent_ref", "text", "yes", "DPDP notice and consent record reference"),
              ("deal", "client_id", "text", "yes", "Client identifier"),
              ("deal", "stage", "enum", "yes", "lead / qualified / visit / negotiation / closure / lost"),
              ("deal", "closed_price", "number", "no", "Actual registered consideration"),
              ("deal", "commission_expected", "number", "no", "Expected commission"),
              ("deal", "commission_realised", "number", "no", "Realised commission, net of TDS"),
              ("deal", "payout_days", "integer", "no", "Days from closure milestone to cash receipt"),
              ("deal", "lost_reason", "text", "no", "Mandatory on any deal marked lost"),
          ])

    write("repository_catalogue.csv",
          ["repository", "owner", "use_in_system", "granularity", "refresh",
           "acquisition_position", "caution"],
          [
              ("MahaRERA", "Maharashtra RERA", "Projects, promoters, status, possession, QPRs, agent registry",
               "Project / agent", "Monthly / on change", "Public portal — permitted",
               "Track modifications and extensions, not only the initial registration"),
              ("IGR / Registration & Stamps", "Government of Maharashtra",
               "Registered instruments, Ready Reckoner, e-Search", "Transaction / locality",
               "Monthly / annual", "Free e-Search — permitted; certified copies from the SRO",
               "e-Search results are explicitly uncertified; Mumbai coverage from 1985"),
              ("MMRDA", "MMRDA", "Metro, roads, regional infrastructure status",
               "Corridor / pocket", "Quarterly / on change", "Public portal — permitted",
               "Use status and slippage, never the headline completion date alone"),
              ("MSRDC", "MSRDC", "Expressways, corridors, tunnels", "Corridor",
               "Quarterly / on change", "Public portal — permitted",
               "Clearance is not commencement; commencement is not completion"),
              ("BMC / MCGM", "Brihanmumbai Municipal Corporation",
               "Development plan, roads, civic infrastructure, ward data", "Ward / pocket",
               "Quarterly / on change", "Public portal — permitted",
               "Verify against the latest sanctioned plan, not a news summary"),
              ("CIDCO / NMMC", "CIDCO, Navi Mumbai Municipal Corporation",
               "Navi Mumbai planning, land, node development", "Node / sector",
               "Quarterly", "Public portal — permitted",
               "Different jurisdiction and field definitions from BMC"),
              ("Census of India", "Registrar General of India", "Population and demographics",
               "Ward / district", "Low frequency", "Public portal — permitted",
               "Vintage is the problem, not access; state the census year on every use"),
              ("Institutional research", "Knight Frank / CBRE / ANAROCK / JLL / Colliers",
               "Sales, launches, inventory, QTS, absorption, office context", "City / zone",
               "Quarter / half-year", "Cite and attribute; do not republish tables",
               "Methodologies and geographic definitions differ between houses — never mix"),
              ("Developer filings and price sheets", "Promoters",
               "Price, inventory, specification, construction status", "Project / unit",
               "Weekly / monthly", "Provided material — permitted",
               "Marketing material is not a statutory filing; reconcile to the RERA record"),
              ("Property portals", "99acres / Magicbricks / Housing / NoBroker",
               "Asking price and rent, listing age, active supply", "Project / pocket / unit",
               "Daily / weekly", "Manual or permitted feed only — terms of use bind",
               "Deduplicate, age listings, and never treat asking as transacted"),
              ("Field intelligence", "Own network",
               "Negotiability, society rules, maintenance, true commute, quality", "Pocket / project / unit",
               "Continuous", "Yours — record it the same day",
               "Triangulate across three independent inputs; label estimate versus verified"),
              ("Own CRM and closures", "Own business",
               "True lead source, conversion, closed price, commission, objections", "Client / deal / unit",
               "Real time", "Yours — subject to DPDP notice, consent and retention",
               "The highest-value dataset in the system, and the only one that compounds"),
          ])

    print("\nDone.")


if __name__ == "__main__":
    main()
