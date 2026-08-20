"""
founder.py — verified founder facts for the Brickrock Realty pitch deck.

SOURCING RULE
Every item below traces to a document Lakshay supplied. Nothing is inferred except
where marked INFERRED, and inferred items are flagged for confirmation before use.

Attribution discipline (explicit instruction from the founder):
  - Sheesham.in / House Sutra numbers  -> LAKSHAY'S OWN business
  - @brickrockrealty                   -> LAKSHAY'S OWN operating presence
  - 310 acres                          -> FAMILY inheritance, NOT his personal asset
  - 124 acres + township               -> HIS FATHER's individual land and development
Never present family holdings as personal achievements.
"""

# ---------------------------------------------------------------------------
# 1. SHEESHAM.IN — Lakshay's own business  [src: Sheesham.in Incubation Deck, Jul 2026]
# ---------------------------------------------------------------------------
SHEESHAM = {
    "revenue_fy26":     ("₹1.08 Cr", "Sales, FY 2025-26"),
    "revenue_fy25":     ("₹51.8 L", "Sales, FY 2024-25"),
    "growth_yoy":       ("+108%", "year on year"),
    "pat":              ("₹17.1 L", "Net profit (PAT), 16% margin"),
    "invoices":         ("183", "invoices issued from the showroom"),
    "avg_invoice":      ("₹58,807", "average invoice value"),
    "return_ratio":     ("0.5%", "return ratio vs 3% industry standard"),
    "monthly_avg":      ("₹9 L", "average monthly sales"),
    "funding":          ("100%", "bootstrapped — no outside capital"),
    "location":         "Vaishali Nagar showroom, Jaipur",
    "structure":        "Showroom combined with House Sutra (online channels and parent company)",
}

# Quarterly progression, ₹ lakh  [src: Sheesham deck p5]
SHEESHAM_QUARTERS = {
    "FY 2024-25": [7, 16, 18, 10],      # total ₹51.8 L
    "FY 2025-26": [24, 30, 31, 22],     # total ₹1.08 Cr
}

# Revenue concentration by ticket band  [src: Sheesham deck p7]
SHEESHAM_TICKETS = [
    ("Up to ₹50k",   58, 25),
    ("₹50k – ₹1 L",  28, 36),
    ("Above ₹1 L",   14, 39),
]

# ---------------------------------------------------------------------------
# 2. BRICKROCK REALTY — Lakshay's own real-estate presence  [src: Instagram, Aug 2026]
# ---------------------------------------------------------------------------
BRICKROCK = {
    "handle":     "@brickrockrealty",
    "name":       "Lakshay Chanda · Chanda Properties",
    "bio":        "Helping you invest in top properties · Trusted Realtors Since 2002",
    "followers":  1055,
    "posts":      19,
    "top_reel":   366_000,
    "reels_20k":  3,          # reels above 20k views
    "total_views": 480_000,   # sum of views on reels visible on the profile
}

# Content mix observed on the profile — this is the point, not the follower count.
BRICKROCK_CONTENT = [
    ("Educational", ["What is RERA?", "How to spot an overvalued property",
                     "The parking scam explained", "Why rent agreements run 11 months",
                     "3 things to check before buying a flat"]),
    ("Property walkthroughs", ["Jaipur's most premium villa — The Padmavati",
                               "Most exclusive house in Mansarovar, Jaipur",
                               "Site visits and project tours"]),
    ("Market commentary", ["Mall rent economics — why Zara pays less than you think",
                           "Big regulatory update for Rajasthan"]),
]

# ---------------------------------------------------------------------------
# 3. FAMILY REAL-ESTATE ECOSYSTEM — context, explicitly NOT Lakshay's assets
# ---------------------------------------------------------------------------
FAMILY = {
    "firm":        ("Chanda Properties", "family real-estate firm, Jaipur — trusted realtors since 2002"),
    "inheritance": ("~310 acres", "family land inheritance — family asset, not Lakshay's personally"),
    "father":      ("124 acres", "owned and being developed by Lakshay's father as a scheme/township"),
    "years":       ("24 years", "of family operating history in Jaipur real estate"),
}

# ---------------------------------------------------------------------------
# 4. EDUCATION / AFFILIATION
# ---------------------------------------------------------------------------
# INFERRED from the @brickrockrealty profile: a highlight titled "IIM MUMBAI" and a
# pinned post at the IIM Mumbai campus sign. Confirm before circulating the deck.
EDUCATION = ("IIM Mumbai", "INFERRED — confirm before use")

# ---------------------------------------------------------------------------
# 5. THE THREE-STAGE VISION
# ---------------------------------------------------------------------------
STAGES = [
    ("01", "MUMBAI", "Advisory & brokerage", "Years 1–3",
     "Enter the hardest, deepest, most data-rich residential market in India and learn it "
     "at pocket level.",
     ["Micro-market intelligence no competitor holds",
      "Developer and channel-partner relationships",
      "A transaction track record with registered evidence",
      "Broker network across an operating corridor",
      "Working capital from commission, not from family"]),
    ("02", "DEVELOPMENT", "Move closer to the asset", "Years 3–6",
     "Convert market knowledge and relationships into a position in the project itself, "
     "where the economics are far larger.",
     ["Advisory on land and project feasibility",
      "Joint development and partnership positions",
      "Co-investment in small projects",
      "Own first project as developer",
      "Construction and delivery capability"]),
    ("03", "JAIPUR", "Build at home", "Years 6+",
     "Take Mumbai-grade execution and developer capability into a market the family "
     "has worked for 24 years.",
     ["Mumbai underwriting standards applied to Jaipur land",
      "Family ecosystem as distribution, not as a crutch",
      "Development capability that Jaipur's market lacks",
      "Brand built on evidence rather than relationships alone",
      "Scale that a brokerage alone can never reach"]),
]

# ---------------------------------------------------------------------------
# 6. WHY MUMBAI FIRST — the argument for the detour
# ---------------------------------------------------------------------------
WHY_MUMBAI = [
    ("Hardest market teaches fastest",
     "Mumbai has the deepest transaction volume, the strictest regulator and the most "
     "sophisticated buyers in India. Capability built here transfers down-market; the "
     "reverse is not true."),
    ("Capital without dilution",
     "Brokerage converts knowledge into cash inside twelve months with almost no capital "
     "at risk. Development needs capital. This is how it gets funded."),
    ("The network is the asset",
     "Developers, channel partners, lenders, lawyers and brokers — the relationships that "
     "make a first project possible are made across a hundred transactions, not in a meeting."),
    ("Jaipur will still be there",
     "The family ecosystem is 24 years old and is not going anywhere. What is scarce is "
     "the capability to build, and that is not available in Jaipur."),
]
