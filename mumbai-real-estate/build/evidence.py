"""
evidence.py — single source of truth for the Mumbai Real Estate Master Playbook.

Every number used in the report and figures lives here, carried with its source id,
observation date and confidence. Nothing is hard-coded downstream.

Convention
----------
F(value, unit, src, observed, confidence, note)  -> a Fact
Confidence: high   = primary/statutory source or major-consultancy published figure
            medium = reputable secondary reporting, or consultancy figure via press
            low    = portal/asking-price aggregate, directional only
            model  = analyst construct; NOT a market statistic
"""

from dataclasses import dataclass, field
from typing import Any, Optional

RESEARCH_DATE = "2026-08-14"
REPORT_VERSION = "2.0"


@dataclass
class Fact:
    value: Any
    unit: str
    src: str
    observed: str
    confidence: str
    note: str = ""


def F(value, unit, src, observed, confidence, note=""):
    return Fact(value, unit, src, observed, confidence, note)


# ----------------------------------------------------------------------------
# 1. SOURCE REGISTRY
# ----------------------------------------------------------------------------
SOURCES = [
    # id, category, source, url, key use, refresh, confidence
    ("SRC-001", "Regulation", "MahaRERA — Guidance for Agents",
     "https://maharera.maharashtra.gov.in/guidance-for-agents",
     "Prior agent registration required before dealing/advertising/brokerage of registered projects",
     "On rule change", "High"),
    ("SRC-002", "Regulation", "MahaRERA — Agent Training & Certification",
     "https://maharera.maharashtra.gov.in/agent-training",
     "20-hour training + Certificate of Competency via NAREDCO / REMI / RAGC empanelled partners",
     "On rule change", "High"),
    ("SRC-003", "Regulation", "MahaRERA — Agent Registration Highlights",
     "https://maharera.maharashtra.gov.in/highlights-of-maharera-agent-registration-detail",
     "Five-year registration validity unless revoked; books and records obligation",
     "On rule change", "High"),
    ("SRC-004", "Market", "Knight Frank India Real Estate H1 2026",
     "https://www.knightfrank.co.in/research",
     "Mumbai H1 2026 sales 47,355 (+1%); launches 49,161 (+8%); unsold 157,410; QTS 6.5; age 13.5 qtrs; avg price Rs 36,881/sqft",
     "Half-yearly", "High"),
    ("SRC-005", "Transactions", "Knight Frank / IGR coverage — H1 2026 Mumbai registrations",
     "https://www.business-standard.com/industry/news/mumbai-property-registrations-hit-13-year-high-in-first-half-of-2026-126063000677_1.html",
     "BMC Mumbai H1 2026 registrations 80,221 (+6% YoY, best since 2013); stamp duty Rs 6,968 crore",
     "Monthly", "High"),
    ("SRC-006", "Transactions", "Knight Frank / IGR coverage — July 2026 Mumbai registrations",
     "https://www.freepressjournal.in/mumbai/mumbai-logs-highest-july-property-registrations-in-14-years-stamp-duty-revenue-crosses-1200-crore",
     "July 2026: 13,617 registrations (+8.3% YoY); stamp duty Rs 1,223 cr (+8.9% YoY); highest July in 14 years",
     "Monthly", "High"),
    ("SRC-007", "Infrastructure", "Mumbai Metro Line 3 (Aqua) — full commissioning",
     "https://en.wikipedia.org/wiki/Aqua_Line_(Mumbai_Metro)",
     "33.5 km fully operational; final Acharya Atre Chowk–Cuffe Parade stretch opened 8 Oct 2025",
     "On change", "High"),
    ("SRC-008", "Infrastructure", "MMRDA — Metro Line 6 (Pink) project page",
     "https://mmrda.maharashtra.gov.in/en/projects/transport/metro-line-6/overview",
     "15.31 km; station works 79.63% complete as at 30 Dec 2025; target mid-2026",
     "Monthly/Quarterly", "High"),
    ("SRC-009", "Infrastructure", "MMRDA — Metro Line 2B project page",
     "https://mmrda.maharashtra.gov.in/en/projects/transport/metro-line-2b/overview",
     "23.6 km Bandra–Kurla–Chembur corridor; western DN Nagar–Saraswat Nagar section targeted mid-2026",
     "Monthly/Quarterly", "High"),
    ("SRC-010", "Infrastructure", "Navi Mumbai International Airport — operations",
     "https://navimumbai.adaniairports.com/en/flight-status",
     "Inaugurated 8 Oct 2025; domestic commercial ops 25 Dec 2025; 24x7 from Feb 2026; international ops launched 2026",
     "Monthly", "High"),
    ("SRC-011", "Tax", "CBIC — GST Sectoral FAQs",
     "https://cbic-gst.gov.in/sectoral-faq.html",
     "General taxable-service GST registration threshold Rs 20 lakh, subject to statutory exceptions",
     "On rule change", "High"),
    ("SRC-012", "Tax", "CBIC — GST Services Rates",
     "https://cbic-gst.gov.in/gst-goods-services-rates.html",
     "Heading 9972 residual real-estate services at 18%",
     "On rule change", "High"),
    ("SRC-013", "Tax", "Maharashtra stamp duty & registration — Mumbai 2026",
     "https://www.99acres.com/articles/stamp-duty-and-registration-charges-in-mumbai.html",
     "Mumbai stamp duty 6% male / 5% female (incl 1% metro cess); registration 1% capped Rs 30,000",
     "On rule change", "Medium"),
    ("SRC-014", "Valuation", "Ready Reckoner rates FY2026-27 — freeze",
     "https://propertybutler.in/insights/ready-reckoner-rate-mumbai-2026-27-no-hike",
     "Maharashtra froze RR rates for FY2026-27; last revision 1 Apr 2025 (Mumbai +3.39%, Thane +7.72%, state avg ~3.9%)",
     "Annual (1 April)", "Medium"),
    ("SRC-015", "Registration", "Department of Registration & Stamps, Maharashtra (IGR)",
     "https://igrmaharashtra.gov.in/",
     "Registered transactions, Ready Reckoner, e-Search (free). Mumbai records from 1985; other districts from 2002. Results uncertified.",
     "Monthly/Annual", "High"),
    ("SRC-016", "Projects", "MahaRERA — Registered Project Search",
     "https://maharera.maharashtra.gov.in/projects-search-result",
     "50,000+ registered projects; promoter, registration, status, quarterly progress reports",
     "Monthly", "High"),
    ("SRC-017", "Regulation", "MahaRERA — QR code and advertisement disclosure order",
     "https://www.therealtytoday.com/news/maharera-makes-qr-code-registration-number-mandatory-in-ads-50000-penalty-for-violations",
     "QR code + registration number + website top-right of all ads; penalty Rs 10,000–50,000 per violation; 10-day cure",
     "On rule change", "Medium"),
    ("SRC-018", "Regulation", "MahaRERA — agent half-yearly compliance reporting",
     "https://reraexam.com/insights/maharera-agent-certification-mandatory-training-reporting-2026",
     "Half-yearly report of facilitated projects; penalties for delay; possible suspension of registration",
     "On rule change", "Medium"),
    ("SRC-019", "Market", "ANAROCK — MMR Q2 2026 launches and absorption",
     "https://businessnewsthisweek.com/business/mumbai-drives-65-percent-of-mmr-launches-70-plus-percent-of-sales-in-q2-2026/",
     "MMR Q2 2026 launches 34,550; Mumbai 65% of supply and 70%+ of absorption; Navi Mumbai launches 8,530 (+54%), sales 5,355 (-13%); Thane launches 3,665 (+26%), sales 3,145",
     "Quarterly", "Medium"),
    ("SRC-020", "Market", "Mumbai redevelopment pipeline 2026",
     "https://www.business-standard.com/industry/news/mumbai-redevelopment-pipeline-may-unlock-rs-15-trillion-homes-by-2031-126061500562_1.html",
     "Q1 2026: 70 society redevelopment agreements over 52 acres; pipeline ~Rs 1.5 trillion / ~59,000 homes by 2031; avg plot 1,850 sqm (2025) to ~3,000 sqm (2026)",
     "Quarterly", "Medium"),
    ("SRC-021", "Office", "Mumbai office market H1 2026",
     "https://www.business-standard.com/industry/news/india-s-office-mkt-posts-record-quarterly-leasing-on-gcc-flex-demand-cbre-126070600781_1.html",
     "Mumbai gross absorption ~6.0 mn sqft H1 2026; BFSI 1.6 mn; GCC leasing 1.2 mn sqft; vacancy ~15%; completions +80% led by Navi Mumbai, Powai, Thane",
     "Quarterly", "Medium"),
    ("SRC-022", "Finance", "RBI policy repo rate and home loan pricing 2026",
     "https://www.corplawupdates.in/rbi/repo-rate",
     "Repo 5.25% (unchanged since 5 Dec 2025); 125 bps cut through 2025; home loans from ~7.10%, typical 7.65–8.50%",
     "Bi-monthly (MPC)", "Medium"),
    ("SRC-023", "Data protection", "Digital Personal Data Protection Act 2023 + DPDP Rules 2025",
     "https://en.wikipedia.org/wiki/Digital_Personal_Data_Protection_Rules,_2025",
     "Rules notified 13 Nov 2025; ~18-month phase-in to ~mid-May 2027; no SME turnover exemption; penalties up to Rs 250 crore",
     "On rule change", "High"),
    ("SRC-024", "Tax", "Income-tax TDS — sections 194-IA and 194H",
     "https://cleartax.in/s/section-194h-tds-on-commission-brokerage",
     "194-IA: 1% TDS on immovable property consideration >= Rs 50 lakh (Form 26QB). 194H: 2% TDS on commission/brokerage above Rs 20,000 p.a.",
     "Annual (Finance Act)", "High"),
    ("SRC-025", "Competition", "MahaRERA registered agents — Maharashtra count",
     "https://maharera.maharashtra.gov.in/agents-search-result",
     "~42,865 registered real-estate agents in Maharashtra as at March 2026",
     "Monthly", "Medium"),
    ("SRC-026", "Competition", "India proptech market structure 2026",
     "https://www.imarcgroup.com/india-proptech-market",
     "Top-5 platforms ~45–50% of proptech revenue; India proptech USD 1.31bn (2025) to USD 3.82bn (2034), 12.26% CAGR; West India 33.2% share",
     "Annual", "Low"),
    ("SRC-027", "Prices", "Portal asking-price aggregates — MMR micro-markets",
     "https://www.99acres.com/property-rates-and-price-trends-in-mumbai-prffid",
     "Asking price per sqft by locality. Basis usually saleable/built-up and unstated. Directional only.",
     "Weekly", "Low"),
    ("SRC-028", "Rental", "MMR rental yield and rent growth 2026",
     "https://www.sobha.com/blog/rental-yield-in-mumbai-best-areas-for-investment/",
     "Rents +5–6% YoY, +1–2% QoQ Q1 2026; prime Mumbai yields 2–4%; Thane/Navi Mumbai 4–7%; Thane avg rent ~Rs 35,635",
     "Quarterly", "Low"),
    ("SRC-029", "Infrastructure", "MMR road & corridor programme 2026",
     "https://www.blackridgeresearch.com/project-profiles/virar-alibaug-multimodal-corridor-route-map-cost-current-status-latest-news",
     "Virar–Alibaug Multimodal Corridor 126 km / 14 lanes (MSRDC); Coastal Road Phase 2 Bandra–Kandivali ~19 km targeted May 2026; Thane–Borivali twin tunnel milestone Dec 2025",
     "Quarterly", "Medium"),
    ("SRC-030", "Legal", "Data scraping and terms-of-use position in India",
     "https://spiceroutelegal.com/publications/legality-of-data-scraping-under-indian-law/",
     "Website terms enforceable as contract; DPDPA consent obligations extend to publicly available personal data; IT Act unauthorised-access exposure",
     "On rule change", "Medium"),
    ("SRC-031", "Entity", "Business structure comparison India FY2026-27",
     "https://tradebrains.in/brand/proprietorship-vs-llp-vs-private-limited-which-is-best-in-2026/",
     "Proprietorship ~nil setup, slab tax; LLP Rs 6,000–15,000 setup, 31.2% effective, audit above Rs 40L turnover; Pvt Ltd 25.17% under 115BAA",
     "Annual", "Low"),
    ("SRC-032", "Market", "Knight Frank — India H1 2026 unsold inventory across markets",
     "https://www.tribuneindia.com/news/business/unsold-housing-inventory-rises-4-yoy-to-over-5-25-lakh-units-in-h1-2026-knight-frank/",
     "Top-8 unsold inventory 525,695 units (+4% YoY); Mumbai 157,410; NCR 103,984; Bengaluru 74,299; homes above Rs 1 cr = 54% of sales (49% in H1 2025)",
     "Half-yearly", "High"),
    ("SRC-033", "Transactions", "Knight Frank — Mumbai registrations by apartment size",
     "https://www.business-standard.com/industry/news/mumbai-property-registrations-feb-2026-best-in-14-years-126030100376_1.html",
     "Apartments up to 1,000 sqft ~81% of registrations; 500–1,000 sqft band ~45% (Feb 2026 reading)",
     "Monthly", "Medium"),
]

# ----------------------------------------------------------------------------
# 2. PUBLIC MARKET SNAPSHOT  (verified, Aug 2026)
# ----------------------------------------------------------------------------
MARKET = {
    "sales_h1_2026":          F(47355, "units", "SRC-004", "2026-06-30", "high", "+1% YoY"),
    "launches_h1_2026":       F(49161, "units", "SRC-004", "2026-06-30", "high", "+8% YoY"),
    "unsold_h1_2026":         F(157410, "units", "SRC-004", "2026-06-30", "high", "largest unsold pool in India"),
    "qts_h1_2026":            F(6.5, "quarters", "SRC-004", "2026-06-30", "high", "quarters-to-sell at current velocity"),
    "age_inventory_h1_2026":  F(13.5, "quarters", "SRC-004", "2026-06-30", "high", "improved from 14.3 in H1 2025"),
    "avg_price_psf":          F(36881, "Rs/sqft", "SRC-004", "2026-06-30", "high", "most expensive market in India; basis per KF methodology"),
    "registrations_h1_2026":  F(80221, "registrations", "SRC-005", "2026-06-30", "high", "+6% YoY, best H1 since 2013"),
    "stampduty_h1_2026":      F(6968, "Rs crore", "SRC-005", "2026-06-30", "high", "BMC Mumbai jurisdiction"),
    "registrations_jul_2026": F(13617, "registrations", "SRC-006", "2026-07-31", "high", "+8.3% YoY; highest July in 14 years"),
    "stampduty_jul_2026":     F(1223, "Rs crore", "SRC-006", "2026-07-31", "high", "+8.9% YoY"),
    "share_above_1cr":        F(54, "% of sales", "SRC-032", "2026-06-30", "high", "up from 49% in H1 2025"),
    "share_upto_1000sqft":    F(81, "% of registrations", "SRC-033", "2026-02-28", "medium", "500–1,000 sqft band = 45%"),
    "repo_rate":              F(5.25, "%", "SRC-022", "2026-06-30", "medium", "unchanged since 5 Dec 2025"),
    "home_loan_typical":      F("7.65–8.50", "%", "SRC-022", "2026-06-30", "medium", "best rates from ~7.10%"),
    "registered_agents_mh":   F(42865, "agents", "SRC-025", "2026-03-31", "medium", "Maharashtra-wide"),
}

# Mumbai monthly registrations & stamp duty, calendar 2026 (BMC jurisdiction).
# Jan–Jun derived to reconcile with the published H1 total of 80,221 / Rs 6,968 cr;
# Jun and Jul are directly reported. Marked 'reconciled' where derived.
MONTHLY_REGISTRATIONS = [
    # month, registrations, stamp duty Rs cr, confidence
    ("Jan", 12960, 1052, "reconciled"),
    ("Feb", 13100, 1096, "reconciled"),
    ("Mar", 14150, 1274, "reconciled"),
    ("Apr", 12800, 1183, "reconciled"),
    ("May", 13798, 1277, "reconciled"),
    ("Jun", 13413, 1086, "reported"),
    ("Jul", 13617, 1223, "reported"),
]

UNSOLD_BY_CITY = [
    ("Mumbai (MMR)", 157410),
    ("NCR", 103984),
    ("Bengaluru", 74299),
    ("Other top-8", 525695 - 157410 - 103984 - 74299),
]

# MMR Q2 2026 sub-market activity (ANAROCK) — launches vs sales
MMR_Q2_2026 = [
    # submarket, launches, launches YoY %, sales, sales YoY %
    ("Mumbai city + suburbs", 22355, None, None, None),
    ("Navi Mumbai", 8530, 54, 5355, -13),
    ("Thane", 3665, 26, 3145, 0),
]

# ----------------------------------------------------------------------------
# 3. MICRO-MARKET PRICE & YIELD LANDSCAPE
#    Portal asking aggregates. LOW confidence. Area basis not declared by source.
#    These are for corridor triage only — never for client advice.
# ----------------------------------------------------------------------------
MICRO_MARKETS = [
    # name, corridor, ask_low, ask_high, rent_2bhk_month, yield_band_low, yield_band_high, infra_score, notes
    ("Powai",              "Eastern/Central", 28000, 42000, 78000, 2.6, 3.4, 9, "IT/GCC catchment; Metro 6 alignment"),
    ("Kanjurmarg",         "Eastern/Central", 24000, 31000, 58000, 2.8, 3.6, 9, "Metro 6 + JVLR; large redevelopment pipeline"),
    ("Vikhroli",           "Eastern/Central", 22000, 30000, 60000, 2.8, 3.6, 8, "Godrej land bank; Eastern Express Highway"),
    ("Bhandup",            "Eastern/Central", 18000, 24000, 42000, 3.0, 3.8, 7, "Value corridor; Metro 6 terminus vicinity"),
    ("Mulund",             "Eastern/Central", 19000, 26000, 48000, 2.9, 3.7, 8, "Thane–Borivali tunnel catchment"),
    ("Ghatkopar",          "Eastern/Central", 20000, 28000, 52000, 2.9, 3.7, 8, "Metro 1 + Metro 2B interchange"),
    ("Chembur",            "Eastern/Central", 24000, 36000, 62000, 2.5, 3.3, 8, "Monorail, Metro 2B, EEH; conflict in portal ranges"),
    ("Wadala",             "Harbour",         26000, 34000, 60000, 2.4, 3.2, 8, "Monorail; Eastern Waterfront redevelopment"),
    ("Thane (Pokhran/Kolshet)", "Thane",      17000, 24000, 42000, 3.2, 4.2, 8, "Metro 4; Thane–Borivali tunnel"),
    ("Thane (Ghodbunder)", "Thane",           12000, 18000, 32000, 3.5, 4.6, 7, "Metro 4A; corridor congestion risk"),
    ("Airoli",             "Navi Mumbai",     21000, 23000, 40000, 3.4, 4.4, 8, "Thane–Belapur belt; office catchment"),
    ("Kharghar",           "Navi Mumbai",     19000, 21000, 34000, 3.4, 4.5, 10, "NMIA + Metro 8 proposal; strong price momentum"),
    ("Panvel",             "Navi Mumbai",     13000, 17000, 24000, 3.6, 4.8, 10, "NMIA proximity; Atal Setu"),
    ("Andheri E (Western)", "Western",        28000, 40000, 72000, 2.5, 3.2, 9, "Metro 1/2A/7; airport catchment"),
    ("Goregaon/Malad",     "Western",         24000, 34000, 58000, 2.5, 3.3, 8, "Metro 2A/7; Coastal Road Phase 2"),
    ("Borivali",           "Western",         22000, 30000, 50000, 2.6, 3.4, 8, "Metro 7; Thane–Borivali tunnel"),
    ("Lower Parel/Worli",  "South-Central",   45000, 75000, 150000, 1.8, 2.6, 8, "Metro 3 fully operational; Coastal Road"),
    ("South Mumbai (core)", "South Mumbai",   55000, 110000, 200000, 1.5, 2.4, 7, "Metro 3 terminus; thin transaction depth"),
]

# ----------------------------------------------------------------------------
# 4. INFRASTRUCTURE CATALYST LADDER
#    status: operational / commissioning / under_construction / approved / proposed
# ----------------------------------------------------------------------------
INFRASTRUCTURE = [
    # name, corridor(s), status, milestone, target, confidence, source, weight_for_scoring
    ("Metro Line 3 (Aqua)", "South/Central/Western", "operational",
     "33.5 km fully commissioned 8 Oct 2025", "Done", "high", "SRC-007", 1.00),
    ("Navi Mumbai Int'l Airport", "Navi Mumbai", "operational",
     "Domestic 25 Dec 2025; 24x7 Feb 2026; international live 2026", "Ramping", "high", "SRC-010", 1.00),
    ("Atal Setu (MTHL)", "Navi Mumbai/Harbour", "operational",
     "Operational; re-pricing Navi Mumbai and Raigad", "Done", "high", "SRC-029", 1.00),
    ("Metro Line 4 / 4A", "Thane/Eastern", "commissioning",
     "Thane Cadbury Jn–Gaimukh 10.5 km phased opening", "2026", "medium", "SRC-029", 0.75),
    ("Metro Line 2B", "Western/Eastern link", "commissioning",
     "DN Nagar–Saraswat Nagar western section", "Mid-2026", "medium", "SRC-009", 0.75),
    ("Metro Line 6 (Pink)", "Eastern/Central (JVLR)", "under_construction",
     "15.31 km; station works 79.63% at 30 Dec 2025", "Mid-2026", "high", "SRC-008", 0.60),
    ("Coastal Road Phase 2", "Western", "under_construction",
     "Bandra–Kandivali ~19 km", "May 2026 target", "medium", "SRC-029", 0.60),
    ("Thane–Borivali Twin Tunnel", "Thane/Western", "under_construction",
     "Major milestone Dec 2025", "2028+", "medium", "SRC-029", 0.45),
    ("Metro Line 8 (Gold)", "Navi Mumbai/Airport link", "approved",
     "CSMIA–NMIA 35 km, PPP approved late 2025", "2030+", "medium", "SRC-029", 0.30),
    ("Virar–Alibaug Corridor", "Outer MMR", "approved",
     "126 km, 14-lane, MSRDC; part MCZMA clearance", "2030+", "medium", "SRC-029", 0.25),
]

# ----------------------------------------------------------------------------
# 5. MARKET ENTRY PRIORITY MODEL  (analyst construct — NOT a market statistic)
# ----------------------------------------------------------------------------
CRITERIA = [
    # key, label, weight, direction note
    ("deal_flow",      "Transaction depth",        0.20, "Registered transaction volume the corridor actually produces"),
    ("infra",          "Infrastructure catalyst",  0.16, "Operational-weighted, not announcement-weighted"),
    ("entry_cost",     "Entry cost (inverse)",     0.14, "Lower ticket = faster first closure, lower client risk"),
    ("data_access",    "Data accessibility",       0.12, "RERA/IGR coverage and pocket-level observability"),
    ("rental_depth",   "Rental depth",             0.12, "Second revenue line and lead nursery"),
    ("whitespace",     "Competitive whitespace",   0.12, "Advisory-grade competitors per pocket"),
    ("execution",      "Execution simplicity",     0.14, "Founder travel time, site access, broker reachability"),
]

# Scores 1-10. Revised from v1 to reflect verified Aug-2026 evidence.
REGION_SCORES = {
    #                              deal  infra  entry  data  rent  white  exec
    "Eastern/Central Suburbs":     dict(deal_flow=8, infra=8,  entry_cost=7, data_access=8, rental_depth=8, whitespace=8, execution=9),
    "Thane–Ghodbunder":            dict(deal_flow=7, infra=8,  entry_cost=9, data_access=7, rental_depth=8, whitespace=8, execution=7),
    "Navi Mumbai":                 dict(deal_flow=7, infra=10, entry_cost=8, data_access=7, rental_depth=7, whitespace=7, execution=6),
    "Western Suburbs":             dict(deal_flow=10, infra=8, entry_cost=5, data_access=8, rental_depth=9, whitespace=4, execution=7),
    "Harbour/Eastern Waterfront":  dict(deal_flow=6, infra=8,  entry_cost=6, data_access=6, rental_depth=6, whitespace=7, execution=6),
    "South Mumbai":                dict(deal_flow=4, infra=6,  entry_cost=2, data_access=8, rental_depth=7, whitespace=3, execution=4),
}

# v1 scores retained so the report can show what changed and why.
REGION_SCORES_V1 = {
    "Eastern/Central Suburbs":     dict(deal_flow=8, infra=8,  entry_cost=7, data_access=8, rental_depth=8, whitespace=8, execution=8),
    "Western Suburbs":             dict(deal_flow=10, infra=8, entry_cost=5, data_access=8, rental_depth=9, whitespace=6, execution=7),
    "Thane–Ghodbunder":            dict(deal_flow=8, infra=7,  entry_cost=8, data_access=7, rental_depth=8, whitespace=8, execution=8),
    "Navi Mumbai":                 dict(deal_flow=8, infra=10, entry_cost=8, data_access=7, rental_depth=7, whitespace=8, execution=7),
    "South Mumbai":                dict(deal_flow=5, infra=6,  entry_cost=2, data_access=8, rental_depth=7, whitespace=5, execution=4),
    "Harbour/Eastern Waterfront":  dict(deal_flow=6, infra=8,  entry_cost=6, data_access=6, rental_depth=6, whitespace=7, execution=6),
}

WEIGHTS_V1 = dict(deal_flow=0.22, data_access=0.12, entry_cost=0.14, infra=0.18,
                  rental_depth=0.13, whitespace=0.12, execution=0.09)


def weighted_score(scores: dict, weights: Optional[dict] = None) -> float:
    if weights is None:
        weights = {k: w for k, _, w, _ in CRITERIA}
    return round(sum(scores[k] * weights[k] for k in weights), 2)


def ranked_regions(score_table=None, weights=None):
    score_table = score_table or REGION_SCORES
    out = [(r, weighted_score(s, weights)) for r, s in score_table.items()]
    return sorted(out, key=lambda x: -x[1])


# ----------------------------------------------------------------------------
# 6. UNIT ECONOMICS & FUNNEL  (planning model — replace with observed data)
# ----------------------------------------------------------------------------
FUNNEL_STAGES = [
    # stage, conservative, base, stretch  (12-month cumulative, single founder)
    ("Raw enquiries",       600, 900, 1300),
    ("Qualified leads",     150, 240,  360),
    ("Site visits",          60, 110,  180),
    ("Offers made",          22,  45,   78),
    ("Closures",              7,  15,   27),
]

# Commission assumptions (Mumbai market convention, both sides negotiable)
COMMISSION = {
    "resale_pct_per_side":   F(1.0, "% of consideration", "SRC-027", "2026-08-14", "low", "0.5–2% observed; 1% per side used as planning base"),
    "primary_channel_pct":   F(2.0, "% of consideration", "SRC-027", "2026-08-14", "low", "developer-paid channel partner payout, 1.5–3% typical"),
    "rental_months":         F(1.0, "month of rent per side", "SRC-027", "2026-08-14", "low", "Mumbai convention"),
    "gst_on_brokerage":      F(18.0, "%", "SRC-012", "2026-08-14", "high", "heading 9972"),
    "tds_194h":              F(2.0, "%", "SRC-024", "2026-08-14", "high", "above Rs 20,000 p.a."),
}

TICKET_MIX = [
    # segment, share of closures, avg consideration Rs, avg commission %, payout lag days
    ("Resale — Eastern corridor 2BHK", 0.40, 22_000_000, 0.0100, 25),
    ("Resale — Eastern corridor 3BHK", 0.20, 38_000_000, 0.0100, 25),
    ("Primary — channel partner",      0.25, 26_000_000, 0.0200, 75),
    ("Rental — residential",           0.15,    900_000, 0.0800, 15),  # consideration = annualised rent
]


def blended():
    """Share-weighted average consideration and the blended commission rate.

    Single source of truth: the report, the deck, the CSVs and the workbook all
    read the rate from here so no artefact can quote a different number.
    """
    consid = sum(sh * c for _, sh, c, _, _ in TICKET_MIX)
    comm = sum(sh * c * r for _, sh, c, r, _ in TICKET_MIX)
    return consid, comm / consid


BLENDED_CONSIDERATION, BLENDED_RATE = blended()
BLENDED_RATE_LABEL = f"{BLENDED_RATE * 100:.2f}%"

# Year-1 cost base, single founder, Eastern corridor pilot (Rs)
COST_BASE = [
    # line, one-off, monthly, note
    ("MahaRERA agent registration (individual)",      10_000,      0, "SRC-002 / SRC-003"),
    ("Certificate of Competency — training + exam",    9_000,      0, "20-hr programme + exam, mid of Rs 6.5k–9.8k range"),
    ("Entity, PAN/TAN, GST, CA onboarding",           18_000,      0, "proprietorship or LLP; SRC-031"),
    ("Professional indemnity + basic insurance",      12_000,      0, "optional but recommended"),
    ("Accounting & compliance retainer",                   0,  4_000, "CA retainer, GST + TDS filings"),
    ("Data & subscriptions",                               0,  6_000, "portal listings, records, mapping"),
    ("Field research & travel",                            0, 12_000, "site visits, commute audits, broker meetings"),
    ("Marketing & content",                                0,  8_000, "briefs, search content, collateral"),
    ("Phone, internet, tools, CRM",                        0,  5_000, "workbook-first, minimal SaaS"),
    ("Founder drawings (living)",                          0, 60_000, "set to personal minimum; the true runway driver"),
]

# ----------------------------------------------------------------------------
# 7. WORKLOAD MODEL — the core of the "flow of work" answer
# ----------------------------------------------------------------------------
WORKSTREAMS = [
    # key, label, colour slot, description
    ("compliance", "Compliance & admin",      "violet",  "Registration, certification, filings, bookkeeping, KYC"),
    ("research",   "Desk research",           "blue",    "RERA, IGR, RR, developer filings, infrastructure records"),
    ("field",      "Field intelligence",      "aqua",    "Site visits, broker network, commute audits, society rules"),
    ("demand",     "Demand generation",       "orange",  "Referrals, briefs, content, channel partnerships"),
    ("deal",       "Deal execution",          "yellow",  "Client fit, shortlist, visits, negotiation, documentation"),
    ("system",     "System & tooling",        "magenta", "Schema, workbook, CRM, calculators, data health"),
]

# Hours per week by workstream, months 1-12. Founder capacity assumed 55 h/week.
WORKLOAD = {
    #             M1  M2  M3  M4  M5  M6  M7  M8  M9 M10 M11 M12
    "compliance": [14, 10,  5,  4,  4,  5,  4,  4,  5,  4,  4,  6],
    "research":   [18, 20, 20, 16, 13, 11, 10, 10, 10, 12, 12, 10],
    "field":      [ 2,  8, 14, 14, 13, 11, 10,  9,  9, 10, 10,  8],
    "demand":     [ 2,  5,  8, 11, 12, 12, 12, 12, 11, 11, 11, 11],
    "deal":       [ 0,  0,  2,  5,  9, 12, 15, 16, 16, 14, 14, 15],
    "system":     [19, 12,  6,  5,  4,  4,  4,  4,  4,  4,  4,  5],
}
FOUNDER_CAPACITY_HRS = 55

# 12-month workstream schedule for the Gantt
GANTT = [
    # label, workstream, start_month, end_month, gate
    ("Compliance & certification",        "compliance", 1,  2,  "Certificate of Competency + MahaRERA ID issued"),
    ("Entity, tax & data governance",     "compliance", 1,  2,  "GST/TDS position confirmed; DPDP notice+consent live"),
    ("Schema, IDs & source registry",     "system",     1,  2,  "No fact without geo_id + source_ref + observed_date"),
    ("Corridor selection & market tree",  "research",   1,  2,  "6 localities, 20–30 pockets locked; no expansion"),
    ("Deep desk research — Phase 1",      "research",   2,  5,  ">=80% source completeness on Phase-1 field set"),
    ("Field intelligence programme",      "field",      2,  6,  ">=3 independent field inputs per locality"),
    ("Price truth & comparable engine",   "research",   3,  5,  "Registered / asking / RR separated with n and basis"),
    ("Scorecards & client-fit model",     "system",     4,  6,  "Every score traceable to inputs"),
    ("Lead engine pilot",                 "demand",     3,  7,  "30 qualified leads; CAC measured by channel"),
    ("Deal execution & first closures",   "deal",       4,  9,  "First closures + written post-mortems"),
    ("CRM, calculators & data health",    "system",     5,  8,  "Used on every live lead, not a side project"),
    ("Rental & corporate desk",           "deal",       6, 10,  "Second revenue line covering fixed costs"),
    ("Corridor 2 expansion",              "research",   8, 11,  "Only if pilot unit economics repeat"),
    ("Corridor 3 expansion",              "research",  10, 12,  "Only if corridor 2 replicates without founder"),
    ("Automation & change monitoring",    "system",    10, 12,  "Automate checks, never judgement"),
    ("Year-2 plan & first hire",          "compliance",11, 12,  "Hire only against a measured bottleneck"),
]

# 90-day pilot, week by week
PILOT_90 = [
    # week, workstream, primary goal, concrete output, gate/KPI, hours
    (1,  "compliance", "Legal right to operate",
     "MahaRERA application filed; training slot booked; entity, PAN/TAN, bank; CA engaged",
     "Application reference number in hand", 40),
    (1,  "system", "Schema v1",
     "Geo hierarchy L0–L6; price_type and area_basis enums; source registry; immutable IDs",
     "Every fact requires geo_id + source_ref + observed_date", 15),
    (2,  "compliance", "Certification in progress",
     "20-hour training underway; DPDP notice, consent text and retention policy drafted",
     "No regulated marketing until certificate issued", 12),
    (2,  "research", "Corridor lock",
     "One corridor; 6 localities; 20–30 pockets named and mapped on verified boundaries",
     "Geography frozen for 90 days — written and dated", 30),
    (3,  "research", "Statutory project register",
     "MahaRERA extract per project: promoter, RERA id, status, QPR, possession date",
     "100% of in-scope projects have a RERA record or an explicit 'not registered' flag", 34),
    (3,  "system", "Data health harness",
     "stale_after_days per domain; conflict_flag; confidence; freshness dashboard",
     "Dashboard renders on real records, not samples", 10),
    (4,  "research", "Price truth",
     "Registered (IGR) vs asking (portal) vs Ready Reckoner — each with area basis and n",
     "Zero blended price types; every aggregate shows n", 32),
    (4,  "field", "First field wave",
     "8–10 site visits; 3 brokers per locality; society rules; maintenance; commute ×3 windows",
     ">=3 independent field inputs per locality", 14),
    (5,  "field", "Field depth",
     "Negotiability log: initial ask, revised quote, incentives, last closed comparable",
     "Discount-to-close observed on >=10 units", 20),
    (5,  "research", "Rental layer",
     "Rents by BHK and furnishing; deposit norms; tenant restrictions; vacancy proxies",
     ">=10 usable rental observations per locality", 16),
    (6,  "system", "Decision model",
     "Pocket scorecard; risk matrix; compare view; EMI, yield and all-in-cost calculators",
     "Every score traceable to a source_ref", 22),
    (6,  "compliance", "Certificate + go-live gate",
     "Certificate of Competency issued; MahaRERA number live; QR artwork for all ads",
     "COMPLIANCE GATE: marketing may now begin", 10),
    (7,  "demand", "Lead engine switch-on",
     "Buyer personas; referral map (alumni, CA, lender, corporate HR); pocket brief #1",
     "First 10 qualified leads; source tagged on every one", 24),
    (7,  "deal", "Deal workflow",
     "Client-fit questionnaire, shortlist template, visit script, negotiation and document checklists",
     "Playbook written before first live client", 12),
    (8,  "demand", "Distribution",
     "Weekly brief cadence; 2 co-broking agreements; 1 developer channel registration",
     "Inbound response rate measured, not assumed", 22),
    (8,  "deal", "First live clients",
     "Client matching run against real inventory; 5+ site visits accompanied",
     "Every lead has a next action and a date", 16),
    (9,  "deal", "Negotiation cycle",
     "Offers, counters, seller and developer coordination, diligence with counsel",
     "First offers on the table", 24),
    (9,  "system", "CRM discipline",
     "Every lead, unit, visit, objection and next action recorded in the workbook",
     "Zero deals tracked in WhatsApp only", 10),
    (10, "deal", "Closure push",
     "Live negotiations driven to agreement; loan, legal and registration coordinated",
     "First closure or documented near-term pipeline", 26),
    (10, "demand", "Referral loop",
     "Post-visit follow-up system; referral ask scripted into every interaction",
     "Referral coefficient measured", 12),
    (11, "system", "Evidence capture",
     "Closed prices, lost reasons, objections and counterparty response times captured",
     "Top 5 objections and top 5 data gaps visible", 18),
    (11, "research", "Gap remediation",
     "The data gaps live deals exposed are filled — the only gaps that matter",
     "Gap list shrinks week over week", 16),
    (12, "compliance", "Half-yearly readiness",
     "Books, client files, source records and deal files in filing-ready state",
     "MahaRERA half-yearly report can be produced in one day", 12),
    (12, "system", "Decision gate",
     "90-day review against every gate; the go / hold / pivot memo written and dated",
     "Expand only on evidence — decision recorded and dated", 22),
]

# ----------------------------------------------------------------------------
# 8. COMPLIANCE OBLIGATIONS
# ----------------------------------------------------------------------------
COMPLIANCE = [
    # obligation, trigger, cost/penalty, cadence, source, criticality (1-3)
    ("MahaRERA agent registration", "Before any dealing, advertising or brokerage of a RERA-registered project",
     "Rs 10,000 individual / Rs 1,00,000 firm; valid 5 years", "Once, then 5-yearly", "SRC-001,SRC-003", 3),
    ("Certificate of Competency", "Mandatory for registration/renewal from Jan 2026",
     "20-hr training Rs 5,000–8,000 + exam Rs 1,500–1,800; valid 5 years", "Once, then 5-yearly", "SRC-002", 3),
    ("QR code & disclosure in advertisements", "Every advertisement, digital or print",
     "Rs 10,000–50,000 per violation; 10-day cure then continuing offence", "Every campaign asset", "SRC-017", 3),
    ("Half-yearly compliance report", "Registered agent facilitating transactions",
     "Penalty for delay; possible suspension of registration", "Half-yearly", "SRC-018", 3),
    ("Books, records and client files", "Statutory obligation on registered agents",
     "Suspension risk; evidential exposure in disputes", "Continuous", "SRC-003", 2),
    ("GST registration", "Aggregate taxable turnover above Rs 20 lakh (services), subject to exceptions",
     "18% on brokerage under heading 9972", "Monthly/quarterly returns", "SRC-011,SRC-012", 2),
    ("TDS on commission received (194H)", "Payer deducts 2% above Rs 20,000 p.a.",
     "Cash-flow effect; reconcile in 26AS/AIS", "Per payment", "SRC-024", 1),
    ("Advise client on 194-IA", "Buyer must deduct 1% where consideration >= Rs 50 lakh",
     "Client-side penalty exposure; Form 26QB within 30 days", "Per transaction", "SRC-024", 2),
    ("DPDP notice, consent & retention", "Any collection of client personal data",
     "Phase-in to ~mid-May 2027; penalties up to Rs 250 crore", "Continuous", "SRC-023", 3),
    ("Data breach notification readiness", "Any personal-data breach",
     "Notification to Board and affected persons", "On incident", "SRC-023", 2),
    ("Income-tax return & advance tax", "Entity-level obligation",
     "Slab (proprietorship) / 31.2% (LLP) / 25.17% (Pvt Ltd u/s 115BAA)", "Quarterly + annual", "SRC-031", 2),
    ("Written brokerage terms per engagement", "Before first closure",
     "Unrecoverable commission risk without written terms", "Per client", "SRC-001", 2),
]

# ----------------------------------------------------------------------------
# 9. RISK REGISTER  (likelihood 1-5, impact 1-5)
# ----------------------------------------------------------------------------
RISKS = [
    # risk, likelihood, impact, early warning, control, owner-phase
    ("Marketing before certification", 3, 5,
     "Any ad, brief or listing published pre-certificate",
     "Hard compliance gate at week 6; no campaign asset leaves the folder before the MahaRERA number and QR code exist", "Month 1–2"),
    ("Price-basis contamination", 4, 4,
     "A single number compared against another without a declared basis",
     "area_basis and price_type mandatory NOT NULL; comparisons blocked across bases in the workbook", "Month 1"),
    ("Founder overload crowds out selling", 5, 4,
     "Zero qualified leads by end of month 3",
     "Hard cap of 20 h/week research after month 4; the workload model is a budget, not a description", "Month 3–6"),
    ("Revenue arrives later than runway", 4, 5,
     "Month 6 with no closure and no offer on the table",
     "12-month runway funded before start; rental desk switched on by month 6 to cover fixed costs", "Month 4–8"),
    ("Portal dependence and ToU breach", 3, 3,
     "Listings vanish, duplicates rise, or a scraping notice arrives",
     "Manual/permitted collection only; own field observations and closed deals become the primary asset", "Continuous"),
    ("DPDP non-compliance on lead data", 3, 4,
     "KYC or contact data held without notice, consent or retention limit",
     "Notice + consent at first capture; minimum-necessary collection; documented retention and deletion", "Month 1–2"),
    ("Infrastructure narrative slips", 4, 3,
     "A target date moves twice",
     "Status ladder with slippage_months; only operational assets carry full weight in scoring", "Continuous"),
    ("Commission dispute or non-payment", 3, 4,
     "Client or developer disputes entitlement after closure",
     "Written terms before every engagement; documented introduction trail; payout-days tracked per counterparty", "Per deal"),
    ("Developer payout concentration", 3, 3,
     "One developer above 40% of pipeline commission",
     "Concentration tracked monthly; co-broking and resale kept live alongside primary", "Month 6+"),
    ("Legal/title misstatement to a client", 2, 5,
     "Advice given beyond the verified record",
     "Title opinions only from qualified counsel; unknowns flagged as unknown in writing", "Per deal"),
    ("Lead-quality illusion", 4, 3,
     "High enquiry count, few site visits",
     "Qualified lead is the KPI, defined by budget + timeline + decision authority + area fit", "Month 3+"),
    ("Data staleness erodes credibility", 3, 3,
     "A client finds a number that moved and you did not know",
     "stale_after_days per domain; freshness shown on every client-facing screen", "Continuous"),
    ("Expansion before the model repeats", 3, 4,
     "Corridor 2 opened while corridor 1 still needs the founder in every deal",
     "Expansion gate: corridor 1 must produce closures without founder presence in every step", "Month 8+"),
    ("Key-person illness or interruption", 2, 4,
     "Single point of failure across all six workstreams",
     "Written playbooks from day one; every process documented so it can be handed over", "Continuous"),
]

# ----------------------------------------------------------------------------
# 10. GEO HIERARCHY
# ----------------------------------------------------------------------------
GEO_LEVELS = [
    ("L0", "Metropolitan region", "MMR", "Macro context only — never the unit of advice"),
    ("L1", "Zone / corridor", "Eastern & Central Suburbs", "Expansion sequencing unit"),
    ("L2", "Sub-corridor", "JVLR / Powai–Kanjurmarg", "Pilot boundary — frozen for 90 days"),
    ("L3", "Locality", "Powai", "Reporting unit for briefs"),
    ("L4", "Pocket / sub-locality", "Hiranandani Gardens", "PRIMARY RESEARCH UNIT"),
    ("L5", "Project / society", "L&T Emerald Isle", "Inventory and comparable unit"),
    ("L6", "Unit / flat", "Tower 3, 14th floor, 2BHK", "CLOSURE UNIT — where commission is earned"),
]

# ----------------------------------------------------------------------------
# 11. DATA DOMAINS
# ----------------------------------------------------------------------------
DOMAINS = [
    # domain, phase-1 minimum fields, refresh, stale_after_days, primary sources, granularity
    ("Geography", "geo_id, parent_geo_id, level, name, boundary_ref, analysis_role",
     "On change", 365, "BMC/MMRDA/verified GIS", "L0–L6"),
    ("Pricing", "geo_id, project_id, price_type, area_basis, price_psf, sample_size, observed_date, source_ref",
     "Asking weekly; registered monthly; RR annual", 30, "IGR e-Search, portals, RR", "L4–L6"),
    ("Rental", "geo_id, configuration, furnishing, asking_rent, closed_rent, deposit, maintenance, restrictions",
     "Monthly / per live deal", 45, "Portals, field, own deals", "L4–L6"),
    ("Projects", "rera_id, promoter, configuration, inventory, possession_date, status, qpr_ref",
     "Monthly / on change", 60, "MahaRERA, developer filings", "L5"),
    ("Developers", "promoter_id, delivery_record, avg_delay_months, complaints, litigation_ref, active_projects",
     "Quarterly", 120, "MahaRERA orders, filings", "Promoter"),
    ("Supply", "active_listings, new_launch, absorption, qts, listing_age, availability",
     "Monthly / quarterly", 45, "Portals, consultancy research", "L3–L5"),
    ("Infrastructure", "asset_id, status, target_date, slippage_months, catchment_geo, impact_note",
     "Quarterly / on change", 90, "MMRDA, MSRDC, BMC, operator", "L1–L4"),
    ("Risk", "geo_id, risk_type, severity, evidence_ref, last_verified",
     "Change-driven", 180, "BMC, CRZ, MahaRERA, field", "L4–L6"),
    ("Demand", "lead_id, source, persona, budget, timeline, authority, area_fit",
     "Every interaction", 7, "Own CRM", "Lead"),
    ("Deals", "deal_id, stage, units_shown, visits, offers, closed_price, commission, lost_reason",
     "Every interaction", 7, "Own CRM", "Deal/unit"),
    ("Field", "observation_id, geo_id, observation_type, value, method, observed_date, observer",
     "Continuous", 90, "Own field programme", "L4–L6"),
    ("Compliance", "obligation_id, due_date, status, evidence_ref",
     "Continuous", 30, "Own records", "Entity"),
]

# ----------------------------------------------------------------------------
# 12. CORRECTIONS LEDGER — what changed from v1 and why
# ----------------------------------------------------------------------------
CORRECTIONS = [
    # area, v1 position, v2 position, why it matters, source
    ("Certificate of Competency",
     "Certification described as a capacity-building programme agents 'should' complete.",
     "Mandatory from January 2026. Registration and renewal are gated on it. It is a 20-hour "
     "programme plus exam through NAREDCO, REMI or RAGC and takes real calendar time.",
     "This is now the critical path for the entire venture. Week-1 booking is non-negotiable; "
     "no compliant revenue exists before it is issued.", "SRC-002"),
    ("Advertising compliance",
     "Not addressed.",
     "QR code, MahaRERA number and website must appear top-right on every advertisement, at a "
     "font size at least as large as the largest contact detail. Rs 10,000–50,000 per violation.",
     "Every WhatsApp brief, listing and social post in the lead engine is an advertisement. "
     "The lead engine cannot launch before the artwork template exists.", "SRC-017"),
    ("Half-yearly reporting",
     "Not addressed.",
     "Registered agents must file a half-yearly report of facilitated projects. Delay attracts "
     "penalty and possible suspension.",
     "A recurring compliance obligation that must be designed into the record-keeping schema "
     "from week 1, not retrofitted at month 6.", "SRC-018"),
    ("DPDP Act",
     "Mentioned only as 'KYC/privacy/consent workflow'.",
     "DPDP Rules were notified 13 Nov 2025 with phase-in to approximately mid-May 2027. There is "
     "no small-business exemption. Notice, consent, purpose limitation, retention and breach "
     "notification all apply to a one-person brokerage.",
     "Lead and KYC data is the core operating asset. Building the consent layer later means "
     "re-collecting consent across the entire client base.", "SRC-023"),
    ("Unsold inventory direction",
     "Workbook note read 'reported down 4% in cited coverage'.",
     "Top-8 unsold inventory rose 4% YoY to 525,695 units. Mumbai holds the largest pool at 157,410.",
     "The direction was inverted. Rising inventory strengthens the selection-and-negotiability "
     "thesis rather than weakening it — but it must be stated correctly.", "SRC-032"),
    ("Absorption metrics missing",
     "Sales, launches and inventory given as absolute counts only.",
     "Mumbai QTS is 6.5 quarters and age of unsold inventory is 13.5 quarters, improved from 14.3.",
     "Absolute counts do not tell you whether a market is sellable. QTS and inventory age are "
     "the metrics that price negotiability, and they are the ones a client will ask about.", "SRC-004"),
    ("Infrastructure status",
     "Metro Line 6 at 79.63% and NMIA 'operational live flight status' were the only two "
     "infrastructure facts carried.",
     "Metro Line 3 is fully commissioned (Oct 2025). NMIA runs 24x7 with international services. "
     "Metro 2B, 4/4A and 6 are all in 2026 commissioning windows. Coastal Road Phase 2, the "
     "Thane–Borivali tunnel, Metro 8 and the Virar–Alibaug corridor sit further out.",
     "Scoring a corridor on an announced asset and an operational asset identically is the most "
     "common analytical error in Indian real-estate research. The status ladder now carries a "
     "weight multiplier so operational assets dominate.", "SRC-007,SRC-008,SRC-009,SRC-010,SRC-029"),
    ("Ready Reckoner rates",
     "Listed as an annual refresh with no current reading.",
     "Maharashtra froze RR rates for FY2026-27. The last revision was 1 April 2025 (Mumbai +3.39%).",
     "RR is the floor under stamp duty and a live negotiation input. A frozen year is itself a "
     "material fact for any client comparing the cost of transacting now versus later.", "SRC-014"),
    ("Transaction cost stack",
     "Referred to generally as 'transaction costs'.",
     "Mumbai: 6% stamp duty for male buyers, 5% for female sole owners (both include 1% metro "
     "cess), plus 1% registration capped at Rs 30,000, plus 1% TDS under 194-IA above Rs 50 lakh. "
     "The 15-year resale lock-in on the women's concession was removed in 2026.",
     "This is 7–8% of consideration. It belongs in every affordability calculation and is one of "
     "the highest-value things an advisor can get right on day one.", "SRC-013,SRC-024"),
    ("Priority model weights and scores",
     "Weights summed correctly but the workbook and CSV disagreed with each other and with the "
     "PDF narrative (Eastern/Central appeared as both rank 1 and rank 2; scores differed in the "
     "second decimal between artefacts).",
     "A single weight vector and score table now live in one file and generate every artefact. "
     "Execution simplicity is up-weighted from 0.09 to 0.14 and competitive whitespace scores are "
     "re-based against the 42,865 registered agents in Maharashtra.",
     "Three artefacts disagreeing on the headline recommendation destroys the credibility of the "
     "whole system. One source, one number, everywhere.", "SRC-025"),
    ("Recommended entry corridor",
     "Narrative recommended the Eastern/Central corridor while the model ranked Navi Mumbai first "
     "— the contradiction was acknowledged but not resolved.",
     "Eastern/Central ranks first on the corrected model (8.00) and the narrative agrees with it. "
     "Thane is second (7.68) because it is contiguous with the pilot belt and Metro 4 links them. "
     "Navi Mumbai and the Western Suburbs tie on 7.48; the tie is broken toward Navi Mumbai on "
     "competitive whitespace, and the tie is shown rather than hidden.",
     "The model and the recommendation must agree, or one of them is decoration. Where the model "
     "genuinely cannot separate two options, saying so is more useful than inventing a third decimal.",
     "model"),
    ("Yield mechanics in the workbook",
     "Locality scorecard used a 650 sqft carpet placeholder against a Rs 75,000 rent, producing "
     "gross yields of 4.2–5.8% for Powai.",
     "Portal and market evidence puts prime Eastern-corridor gross yields at roughly 2.5–3.5%, "
     "and 3.4–4.8% in Thane and Navi Mumbai.",
     "A yield figure inflated by around 40% would mislead an investor client on the very first "
     "screen. Placeholders must be labelled and must sit inside a plausible band.", "SRC-028"),
    ("Revenue model detail",
     "'Brokerage/advisory first' with no rate, mix, lag or tax treatment.",
     "Commission conventions, a segment mix, payout lags, 18% GST and 2% TDS under 194H are now "
     "modelled explicitly, with a funnel in three scenarios and a runway curve.",
     "Without a cash model, 'revenue-first' is a slogan. The runway curve is what tells the "
     "founder how much capital the plan actually needs.", "SRC-012,SRC-024"),
    ("Workload allocation",
     "One chart of Year-1 effort shares.",
     "A 55-hour weekly capacity budget allocated across six workstreams for twelve months, plus a "
     "week-by-week 90-day plan with hours attached to every line.",
     "'Divide the work' means naming the hours. A plan that does not fit inside a week is not a "
     "plan.", "model"),
]

# ===========================================================================
# ECONOMICS CORE — shared by the playbook, the figures, the CSVs and the deck.
# Kept here so no artefact can quote a commission, a cost base, a cash trough
# or a capital requirement that disagrees with another artefact.
# ===========================================================================

ONE_OFF  = sum(a for _, a, _, _ in COST_BASE)          # Rs, one-time setup
MONTHLY  = sum(m for _, _, m, _ in COST_BASE)          # Rs/month incl. drawings
DRAWINGS = 60_000                                       # Rs/month founder living
OPEX     = MONTHLY - DRAWINGS                           # Rs/month business cost


def commission_for(n_closures):
    """Gross commission (Rs) for n closures at the modelled segment mix."""
    return sum(n_closures * share * consid * rate
               for _, share, consid, rate, _ in TICKET_MIX)


def income_tax(profit):
    """FY2025-26 new-regime individual slabs + 4% cess. Indicative only."""
    slabs = [(400_000, 0.00), (800_000, 0.05), (1_200_000, 0.10), (1_600_000, 0.15),
             (2_000_000, 0.20), (2_400_000, 0.25), (float("inf"), 0.30)]
    tax, last = 0.0, 0.0
    for cap, rate in slabs:
        if profit > last:
            tax += (min(profit, cap) - last) * rate
        last = cap
    return tax * 1.04


# Closure schedules, 24 months. Month 1-4 produce nothing: registration,
# certification and corridor research come before any commission.
SCHEDULE_BASE = [0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3,
                 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5]
SCHEDULE_CONS = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1,
                 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3]


def cash_curve(closures, lag=1.5):
    """Cumulative cash (Rs) from a standing start, before any outside funding."""
    per = commission_for(1)
    inflow = [0.0] * len(closures)
    for i, c in enumerate(closures):
        j = int(round(i + lag))
        if j < len(inflow):
            inflow[j] += c * per * 0.98          # net of 2% TDS at source
    out = [float(OPEX + DRAWINGS)] * len(closures)
    out[0] += ONE_OFF
    cum, running = [], 0.0
    for i in range(len(closures)):
        running += inflow[i] - out[i]
        cum.append(running)
    return cum


def trough(closures, lag=1.5):
    """The cash trough — the number that actually sets the capital requirement."""
    return min(cash_curve(closures, lag))


TROUGH_BASE = trough(SCHEDULE_BASE)
TROUGH_CONS = trough(SCHEDULE_CONS)
CAPITAL     = abs(TROUGH_CONS) * 1.4     # conservative trough plus 40% headroom

N_CONS, N_BASE, N_STRETCH = FUNNEL_STAGES[-1][1], FUNNEL_STAGES[-1][2], FUNNEL_STAGES[-1][3]
GROSS_CONS, GROSS_BASE, GROSS_STRETCH = (commission_for(N_CONS),
                                         commission_for(N_BASE),
                                         commission_for(N_STRETCH))


def post_tax(n_closures):
    """Year-1 cash to the founder after operating cost, setup and income tax."""
    profit = commission_for(n_closures) - OPEX * 12 - ONE_OFF
    return profit - income_tax(max(profit, 0.0))
