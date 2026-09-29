# Shared data spec for all researchers (READ FULLY BEFORE STARTING)

Project: Mumbai / MMR builders & developers outreach database (business development & relationship building).
Reference date: September 2026. Current roles must be verified against the most recent sources available (prefer 2025–2026).

## Level definitions (use consistently; proposed level is your judgement, explain it)
- **L1 – National/listed majors & top-tier Mumbai groups**: listed large-caps or groups with very large MMR sales (roughly ≥ ₹3,000 cr/yr MMR pre-sales) and/or large land banks across several MMR micro-markets. Access is formal (via BD, land, redevelopment, channel-sales teams).
- **L2 – Large established Mumbai/MMR developers**: roughly ₹750–3,000 cr/yr sales OR ~10+ active MahaRERA projects, multi-micro-market, promoter-led with professional teams.
- **L3 – Mid-size regional developers**: roughly ₹150–750 cr/yr OR ~4–10 active projects, concentrated in 1–3 micro-markets; promoters reachable.
- **L4 – Small/boutique developers & redevelopment/SRA specialists**: 1–4 active projects, mostly society redevelopment / SRA / single-location; promoter-run; highly accessible.
- **L5 – Emerging / first-generation / single-project builders & new entrants** (incl. JV/development-management platforms entering MMR).
- **Connector** – industry associations & office bearers (CREDAI-MCHI, NAREDCO, etc.) who can provide introductions.
For private companies where sales figures are unavailable, use proxies: count of MahaRERA-registered projects, size of projects, number of micro-markets, years active, media coverage.

## Whom to find (per company, as many as are publicly identifiable, current as of 2025–2026)
Promoters/Founders, Chairman, MD/CEO, Business Development head, Land Acquisition head, Redevelopment head, Sales head, Channel Sales / Channel Partner (CP) head, Strategy head, Marketing head. For small builders, the promoter(s)/partners are usually enough. For large companies aim for 5–10 people.
Also useful: CFO, Investor Relations and Company Secretary (listed cos publish their contacts), Liaison/Approvals heads.

## CONTACT DETAIL RULES (critical – the user explicitly forbids guessing)
- Record an email or phone ONLY if it appears verbatim on a public source you actually saw: official company/project website, annual report / stock-exchange filing, MahaRERA registration record/certificate, CREDAI-MCHI / NAREDCO / association directory, press release media contact, government document, or the person's own public professional page.
- NEVER construct an email from a pattern (e.g. firstname@company.com) and NEVER use predicted/masked emails from data-broker sites (RocketReach, ContactOut, Apollo, Lusha, SignalHire, ZoomInfo, Leadiq, etc.). Do not use them as sources for contact details at all.
- Business directories (Justdial, IndiaMART, Sulekha) may be used only for a COMPANY office line, flagged as "business listing – unverified".
- If an individual's personal email/mobile is not public, write exactly: `Not publicly available`. Put the company board line / sales / corporate email in the company record instead (and you may reference it in the person's notes as "reach via company line").
- Professional contact channels only: no residential addresses, no personal social media, no family details.
- For every contact detail, the `sources` field must contain the URL where it was seen.

## LinkedIn
Record the person's LinkedIn profile URL only if the search result clearly matches the same person AND company. If not found: `Not found`. You may note "URL from search index" if you could not open the page.

## OUTPUT FILES (write with Python so JSON escaping is correct – e.g. build a list of dicts and `json.dumps(obj, ensure_ascii=False)` per line)
Write to the folder: `/home/user/NetflixProject/research_notes/Mumbai MMR builders outreach database/`

1. `<topic>_companies.jsonl` – one JSON object per line, one per company:
```
{"level": "L1|L2|L3|L4|L5|Connector",
 "company": "Legal name (Brand)",
 "website": "https://...",
 "hq_address": "Corporate office address as published",
 "office_phone": "exact published number(s) or 'Not publicly available'",
 "general_email": "exact published email(s) (info/sales/IR/CS) or 'Not publicly available'",
 "cp_channel_contact": "channel-partner portal / email / phone if published, else 'Not publicly available'",
 "geography": "main MMR micro-markets",
 "active_projects": "key current/under-construction/recently launched MMR projects (2024-2026) with locations; semicolon-separated",
 "scale_indicators": "listed? FY25/FY26 pre-sales, # MahaRERA projects, land bank, years active, etc.",
 "level_rationale": "why this level",
 "accessibility": "how approachable / best entry point / which person to approach first and why",
 "notes": "recent news 2025-2026: launches, JDAs, redevelopment wins, fund raises, leadership changes, controversies/insolvency if any",
 "sources": ["url1", "url2"],
 "last_verified": "2026-09"}
```
2. `<topic>_people.jsonl` – one JSON object per line, one per person:
```
{"company": "same string as in companies file",
 "person": "Full name",
 "designation": "exact current title",
 "role_category": "Promoter/Founder|Chairman|MD/CEO|Director/Board|Business Development|Land Acquisition|Redevelopment|Sales|Channel Sales|Strategy|Marketing|CFO/Finance|Investor Relations|Company Secretary|Liaison/Approvals|Association Office Bearer|Other",
 "mobile": "exact published number or 'Not publicly available'",
 "email": "exact published email or 'Not publicly available'",
 "linkedin": "URL or 'Not found'",
 "role_verified": "e.g. 'Company website leadership page, accessed 2026-09' or 'ET Realty article Mar 2026'",
 "priority": "High|Medium|Low – with 1-line reason (who can give introductions, mandates, channel partnerships, redevelopment deals)",
 "notes": "useful context (e.g. next-gen promoter handling redevelopment; CREDAI-MCHI office bearer; recently joined from X)",
 "sources": ["url1", "url2"]}
```
3. `<topic>.md` – narrative notes: summary of the segment, level rationale per company, notable gaps, list of companies considered but excluded (and why), data-quality caveats.

Save progressively (append as you go) so work is not lost if you run long. Quality over quantity for people, but breadth matters for companies: the user explicitly wants the broader ecosystem, not just famous names.

## Tools
If WebSearch / WebFetch are not in your tool list, load them first with ToolSearch (query: `select:WebSearch,WebFetch`). Useful sources: official company websites (About/Leadership/Contact/Investor pages), MahaRERA (maharera.maharashtra.gov.in – project search / promoter details), CREDAI-MCHI (mchi.net), NAREDCO Maharashtra, BSE/NSE filings & annual reports, Economic Times Realty, Moneycontrol, Hindustan Times Real Estate, Mid-day, Free Press Journal, Business Standard, Construction World, Realty+ (realty.economictimes / realtyplusmag), 99acres/Magicbricks/Housing.com developer pages (for project lists only), LinkedIn search results, Tofler/Zauba (director names only, not contacts).
Do not spend more than a few searches per person on contacts – when not findable, mark `Not publicly available` and move on.
