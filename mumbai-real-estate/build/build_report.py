"""build_report.py — assembles the Mumbai Real Estate Master Playbook (HTML -> PDF)."""

import html as H
import evidence as E
from report_css import CSS
from fig_econ import commission_for, blended, ONE_OFF, OPEX, DRAWINGS, income_tax, L, CR

PAGES = []
_SECTION = [""]


def sec(name):
    _SECTION[0] = name


def page(body, cls="", section=None, label=None, group=None):
    sect = section if section is not None else _SECTION[0]
    PAGES.append({"body": body, "cls": cls, "section": sect,
                  "label": label, "group": group or sect})


def fig(name, height="tall"):
    return f'<div class="figwrap {height}"><img src="../figures/{name}"></div>'


def figpage(figname, title, deck, note, height="tall", label=None, group=None):
    page(f"""
      <h2>{title}</h2>
      <div class="deck">{deck}</div>
      {fig(figname, height)}
      <div class="fignote">{note}</div>
    """, label=label or title, group=group)


def tbl(header, rows, cls="", widths=None):
    cols = ""
    if widths:
        cols = "<colgroup>" + "".join(f'<col style="width:{w}">' for w in widths) + "</colgroup>"
    th = "".join(f"<th{' class=num' if h.startswith('#') else ''}>{h.lstrip('#')}</th>" for h in header)
    tr = ""
    for r in rows:
        tds = "".join(
            f"<td{' class=num' if str(h).startswith('#') else ''}>{c}</td>"
            for h, c in zip(header, r))
        tr += f"<tr>{tds}</tr>"
    return f'<table class="{cls}">{cols}<thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'


def rs(v, unit="L"):
    if unit == "L":
        return f"₹{v/L:,.1f} L"
    if unit == "Cr":
        return f"₹{v/CR:,.2f} cr"
    return f"₹{v:,.0f}"


# ============================================================ derived numbers
RANKED = E.ranked_regions()
CONSID, RATE = blended()
N_BASE = E.FUNNEL_STAGES[-1][2]
GROSS_BASE = commission_for(N_BASE)
PROFIT_BASE = GROSS_BASE - OPEX * 12 - ONE_OFF
TAX_BASE = income_tax(PROFIT_BASE)
POST_BASE = PROFIT_BASE - TAX_BASE
GROSS_CONS = commission_for(E.FUNNEL_STAGES[-1][1])
POST_CONS = GROSS_CONS - OPEX * 12 - ONE_OFF
POST_CONS -= income_tax(max(POST_CONS, 0))
TOTAL_HOURS = sum(sum(v) for v in E.WORKLOAD.values()) * 52 / 12


def _trough(closures, lag=1.5):
    """Cumulative-cash trough for a closure schedule — same model as figure D3."""
    import numpy as np
    per = commission_for(1)
    inflow = np.zeros(len(closures))
    for i, c in enumerate(closures):
        j = int(round(i + lag))
        if j < len(inflow):
            inflow[j] += c * per * 0.98
    outflow = np.full(len(closures), float(OPEX + DRAWINGS))
    outflow[0] += ONE_OFF
    return float(np.cumsum(inflow - outflow).min())


TROUGH_BASE = _trough([0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3,
                       3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5])
TROUGH_CONS = _trough([0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1,
                       1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3])
CAPITAL = abs(TROUGH_CONS) * 1.4


# ================================================================= 1. COVER
sec("Front matter")
page(f"""
  <div class="inner">
    <div>
      <div class="eyebrow">Final operating report · version {E.REPORT_VERSION}</div>
      <div class="band"></div>
      <h1>Mumbai Real&nbsp;Estate:<br>Entry, Intelligence<br>&amp; Execution System</h1>
      <div class="sub">
        How to enter the Mumbai/MMR residential market as a compliant, revenue-first
        micro-market advisory and brokerage desk — with the evidence re-verified to
        August&nbsp;2026, the analytical model corrected, the work broken down to
        assignable packages, and the capital requirement stated plainly.
      </div>
    </div>
    <div class="meta">
      <div><div class="metak">Research date</div><div class="metav">14 August 2026</div></div>
      <div><div class="metak">Supersedes</div><div class="metav">Final Strategy Report v1.0</div></div>
      <div><div class="metak">Horizon</div><div class="metav">90-day pilot + 12-month roadmap</div></div>
      <div><div class="metak">Figures</div><div class="metav">33 · all generated from one evidence file</div></div>
      <div><div class="metak">Sources</div><div class="metav">33 registered · every fact dated</div></div>
    </div>
  </div>
""", cls="cover", section="", label="Cover", group="Front matter")


# ============================================================== 2. CONTENTS
# (inserted after assembly, once real page numbers are known)
TOC_PLACEHOLDER = object()
page(TOC_PLACEHOLDER, label="Contents and how to read this", group="Front matter")


# ====================================================== 3. EXECUTIVE SUMMARY
page(f"""
  <h2>Executive summary</h2>
  <div class="deck">The recommendation is unchanged in shape from version 1 and materially different in substance:
  build a micro-market advisory and brokerage desk in one corridor, and build the compliance, demand and
  deal machinery alongside the data system rather than after it. What follows is why, and what it costs.</div>

  <div class="tiles">
    <div class="tile" style="border-left-color:var(--blue)">
      <div class="v">Eastern &amp; Central</div>
      <div class="l">recommended first corridor</div>
      <div class="d" style="color:var(--good)">score 8.00 of 10 · wins 99% of randomised weightings</div>
    </div>
    <div class="tile" style="border-left-color:var(--violet)">
      <div class="v">6 weeks</div>
      <div class="l">compliance critical path</div>
      <div class="d" style="color:var(--critical)">Certificate of Competency now mandatory</div>
    </div>
    <div class="tile" style="border-left-color:var(--orange)">
      <div class="v">{rs(abs(TROUGH_CONS))}</div>
      <div class="l">conservative cash trough</div>
      <div class="d" style="color:var(--ink2)">{rs(CAPITAL)} is the capital to actually raise</div>
    </div>
    <div class="tile" style="border-left-color:var(--aqua)">
      <div class="v">{rs(POST_BASE)}</div>
      <div class="l">base-case Year-1 income</div>
      <div class="d" style="color:var(--ink2)">on 15 closures and 2,860 founder-hours</div>
    </div>
  </div>

  <div class="cols2">
    <h3>The market is large enough, and it is not the constraint</h3>
    <p>Mumbai cleared <strong>47,355 residential sales</strong> and <strong>80,221 registrations</strong> in the
    first half of 2026 — the strongest half since 2013 — against <strong>₹6,968 crore</strong> of stamp duty
    <span class="src">[SRC-004, SRC-005]</span>. July continued it: 13,617 registrations and ₹1,223 crore, the
    highest July in fourteen years <span class="src">[SRC-006]</span>. Roughly thirteen to fourteen thousand
    addressable, dated, public transactions clear every single month.</p>
    <p>Against that, unsold inventory stands at <strong>157,410 units</strong>, the largest pool in India, and it
    rose 4% year on year across the top eight markets <span class="src">[SRC-032]</span>. Quarters-to-sell is 6.5
    <span class="src">[SRC-004]</span>. This is a market with deep flow and real overhang, which is precisely the
    condition under which <em>selection and negotiability</em> — not price forecasting — is the sellable skill.</p>

    <h3>The constraint is the founder's calendar and the compliance clock</h3>
    <p>The single most important change since version 1 is regulatory. From January 2026 a MahaRERA agent
    cannot register or renew without a <strong>Certificate of Competency</strong>, obtained through a twenty-hour
    programme and an examination via an empanelled partner <span class="src">[SRC-002]</span>. That is a
    six-week critical path that no amount of effort compresses, and no lawful revenue exists before it closes.
    Advertising rules now mandate a QR code and registration number on every advertisement, at
    ₹10,000–50,000 per violation <span class="src">[SRC-017]</span> — and a WhatsApp pocket brief is an
    advertisement. Registered agents also file a half-yearly compliance report <span class="src">[SRC-018]</span>,
    and the DPDP Rules, notified in November 2025, apply to a one-person business with no exemption
    <span class="src">[SRC-023]</span>.</p>

    <h3>Where to start, and why the model and the narrative now agree</h3>
    <p>The corrected entry model ranks the <strong>Eastern and Central Suburbs</strong> first at 8.00, ahead of
    Thane–Ghodbunder at 7.68, with Navi Mumbai and the Western Suburbs genuinely tied at 7.48. Eastern/Central
    wins not by leading any single criterion but by having no weak one: it is the only corridor combining real
    transaction depth with the highest execution simplicity in the region. Under 5,000 randomised weight
    vectors it stays first 99% of the time.</p>
    <p>In version 1 the narrative recommended Eastern/Central while the model ranked Navi Mumbai first, and the
    contradiction was noted but never resolved. It is resolved here.</p>

    <h3>What it earns, honestly</h3>
    <p>At the modelled mix — average consideration {rs(CONSID,'Cr')} at a blended {RATE*100:.2f}% commission —
    fifteen closures produce {rs(GROSS_BASE)} of gross commission and about {rs(POST_BASE)} post-tax against
    {TOTAL_HOURS:,.0f} founder-hours. That is roughly <strong>₹{POST_BASE/TOTAL_HOURS:,.0f} an hour</strong>.
    In the conservative case it is about a third of that. This is the honest comparator to a salaried
    alternative, and it is the number version 1 never produced.</p>

    <div class="callout">
      <div class="h">The one-sentence thesis</div>
      <p style="margin:0">Know twenty-five pockets better than anyone selling in them, transact inside those
      pockets, capture every observation and closure as structured evidence, and expand only when the economics
      repeat without you in every step.</p>
    </div>
  </div>
""", label="Executive summary — the decision", group="Front matter")


# ============================================================== 4. VERDICT
page(f"""
  <h2>The verdict — what this business is, and what it is not</h2>
  <div class="deck">Version 1's central instinct was right and its sequencing was wrong. The correction is not a
  change of strategy; it is a change of order.</div>
  <div class="grid2">
    <div>
      <div class="callout good">
        <div class="h">What this business is</div>
        <p style="margin:0 0 2mm 0"><strong>A brokerage that happens to have unusually good data.</strong>
        Revenue comes from transactions from month four onward. The intelligence layer exists to win trust,
        shorten shortlists and strengthen negotiation — all of which are inputs to closing, not substitutes
        for it.</p>
        <p style="margin:0"><strong>A twenty-five-pocket business, not a Mumbai business.</strong> The advantage
        is depth in a small geography that a scale competitor cannot economically match, and a local broker
        cannot document.</p>
      </div>
      <div class="callout crit">
        <div class="h">What it is not</div>
        <p style="margin:0 0 2mm 0"><strong>Not a property portal.</strong> The top five platforms hold roughly
        half of proptech revenue <span class="src">[SRC-026]</span>. Competing on listing breadth against a
        funded platform, from a standing start, with one person, is not a strategy.</p>
        <p style="margin:0 0 2mm 0"><strong>Not a data product, yet.</strong> Paid research has no buyer until
        the dataset contains proprietary observations that have survived live transactions. That is a Year-2
        conversation at the earliest.</p>
        <p style="margin:0"><strong>Not a passive-income business.</strong> It is a service business with a
        research habit, and the founder is the service for at least twelve months.</p>
      </div>
    </div>
    <div>
      <h3>The five decisions this document makes</h3>
      <table class="tbl-compact">
        <tbody>
        <tr><td style="width:26mm"><strong>Corridor</strong></td>
            <td>Eastern &amp; Central Suburbs — Powai, Kanjurmarg, Vikhroli, Bhandup, Mulund, Ghatkopar.
            Six localities, 20–30 pockets, frozen for ninety days.</td></tr>
        <tr><td><strong>Sequence</strong></td>
            <td>Compliance, data and demand built in parallel from week 1. Marketing gated at week 6 on the
            Certificate of Competency. First closure targeted month 5.</td></tr>
        <tr><td><strong>Revenue</strong></td>
            <td>Resale brokerage and rentals first; developer channel-partner work second; paid data products
            not before Year 2.</td></tr>
        <tr><td><strong>Capital</strong></td>
            <td>{rs(CAPITAL)} raised before starting — the conservative cash trough plus 40%. Founder drawings are
            the largest single line in the burn and the main lever on it.</td></tr>
        <tr><td><strong>Expansion</strong></td>
            <td>Thane second, then Navi Mumbai. Only at month 8, and only if corridor-1 closures happen without
            the founder present at every step.</td></tr>
        </tbody>
      </table>

      <h3 style="margin-top:4mm">The three ways this fails</h3>
      <ul class="tight small">
        <li><strong>The database becomes the business.</strong> Research is infinitely expandable and feels like
        progress. If deal-execution hours are still zero at month five, the plan has already failed — this is
        why the hour budget on page 27 is a budget, not a description.</li>
        <li><strong>Marketing starts before certification.</strong> The temptation at week 3, with a good pocket
        brief written and nobody to send it to, is enormous. It is also the one mistake that can end the venture
        rather than delay it.</li>
        <li><strong>Runway is shorter than the sales cycle.</strong> Mumbai residential deals routinely take
        60–120 days from first enquiry to registration. Capital sized to the base case rather than the
        conservative case turns a normal slow quarter into a forced exit.</li>
      </ul>
    </div>
  </div>
""", label="Verdict: what this business is, and is not", group="Front matter")


# ==================================================== 5-7. CORRECTIONS LEDGER
sec("Corrections")
chunks = [E.CORRECTIONS[0:7], E.CORRECTIONS[7:14]]
for ci, chunk in enumerate(chunks):
    rows = ""
    for area, v1, v2, why, src in chunk:
        srcs = " ".join(f'<span class="src">[{s.strip()}]</span>' for s in src.split(",")
                        if s.strip() != "model")
        if src == "model":
            srcs = '<span class="badge b-model">model</span>'
        rows += f"""
        <tr>
          <td style="width:34mm"><strong>{H.escape(area)}</strong><br>{srcs}</td>
          <td style="width:62mm"><span class="tiny" style="color:var(--critical);font-weight:700">
              WAS</span><br>{H.escape(v1)}</td>
          <td style="width:80mm"><span class="tiny" style="color:var(--good);font-weight:700">
              NOW</span><br>{H.escape(v2)}</td>
          <td><span class="tiny" style="color:var(--blue);font-weight:700">WHY IT MATTERS</span><br>{H.escape(why)}</td>
        </tr>"""
    head = ("Corrections ledger — what changed from version 1, and why"
            if ci == 0 else f"Corrections ledger <span style='color:var(--muted);font-weight:400'>· continued</span>")
    deck = ("""Fourteen substantive corrections. Three are regulatory changes that post-date the original
    research; the rest are analytical errors, internal contradictions between the PDF, the workbook and the CSVs,
    or material omissions. Each is stated with the failure it would have caused."""
            if ci == 0 else "")
    page(f"""
      <h2>{head}</h2>
      {f'<div class="deck">{deck}</div>' if deck else ''}
      <table class="tbl-compact">{rows}</table>
    """, label="Corrections ledger" + (" (continued)" if ci else ""), group="Front matter")


# ================================================================ PART A
sec("A · The market")
page(f"""
  <div class="inner">
    <div class="num">A</div>
    <h1>The market</h1>
    <div class="sub">What is verifiably true about Mumbai residential property in August 2026 — demand, supply,
    absorption, price, infrastructure — and what each fact implies for a desk with one person and no
    reputation.</div>
    <div class="toc">
      <div><b>A1</b> &nbsp;Market at a glance — H1 2026</div>
      <div><b>A2</b> &nbsp;The registration engine, month by month</div>
      <div><b>A3</b> &nbsp;Overhang and the shape of demand</div>
      <div><b>A4</b> &nbsp;Micro-market asking-price ladder</div>
      <div><b>A5</b> &nbsp;Price against yield across MMR</div>
      <div><b>A6</b> &nbsp;Infrastructure status ladder</div>
      <div><b>A7</b> &nbsp;MMR strategic coverage map</div>
      <div><b>A8</b> &nbsp;From market size to reachable pool</div>
    </div>
  </div>
""", cls="divider", label="Part A opener", group="__DIV__A")

figpage("A1_market_at_a_glance.png",
        "A1 · Mumbai residential market at a glance",
        """Six numbers define the operating environment. Read them as a pair of opposing forces: demand is
        stable and record-deep by registration count, while the unsold pool is the largest in the country and
        still growing. A market that is both busy and over-supplied is a market where the buyer needs help
        choosing — which is exactly the service being sold.""",
        """<strong>What to do with this.</strong> Do not use the ₹36,881 average price with a client; it is a
        city-wide weighted figure on the publisher's own area basis and it describes no actual flat. Use the
        volume and absorption figures to establish that the market is worth working, then move immediately to
        pocket-level evidence you have derived yourself. The gap between this page and a defensible pocket
        comparable is the entire product.""")

figpage("A2_registration_engine.png",
        "A2 · The registration engine",
        """Consultancy reports arrive twice a year. Registrations arrive every month, and each one is a dated,
        addressable, public instrument naming a property, a consideration and a date. This is the highest-value
        public dataset in the Mumbai market and it is free to search.""",
        """<strong>Operating implication.</strong> The IGR e-Search facility is free and covers Mumbai from 1985
        <span class="src">[SRC-015]</span>. Build the monthly sweep of your pocket set into the calendar from week
        4 and never miss one — twelve months of consistent collection produces a registered-price series for your
        twenty-five pockets that no competitor has bothered to build. Note that e-Search results are explicitly
        uncertified; for any number that will be used in a negotiation, obtain the certified copy from the
        sub-registrar office.""")

figpage("A3_inventory_and_demand_shape.png",
        "A3 · Overhang and the shape of demand",
        """Two facts that must be held together. Mumbai holds thirty per cent of the unsold stock of India's
        eight largest markets. At the same time the mix is moving upmarket — homes above ₹1 crore rose from 49%
        to 54% of sales in a year — while the size mix stays compact, with 81% of registrations at 1,000 sq ft
        or less.""",
        """<strong>The modal deal, and therefore the desk.</strong> A flat of 500–1,000 sq ft carpet, above
        ₹1 crore, in a suburb. That is what the client-fit engine should be tuned for, what the comparable set
        should cover, and what the pocket briefs should be about. Building capability for ₹8-crore sea-facing
        apartments is building for a market that will not call you for three years.""")

figpage("A4_price_ladder.png",
        "A4 · Micro-market asking-price ladder",
        """Eighteen MMR micro-markets by observed asking range. The width of each bar carries more information
        than its position: dispersion inside a single locality is routinely 30–50%, and explaining that
        dispersion is what a pocket-level advisor is paid for.""",
        """<strong>Confidence: LOW, and it matters.</strong> Every bar here is an asking price scraped from
        portal aggregates whose area basis is undeclared <span class="src">[SRC-027]</span>. Two of the sources
        consulted disagree about Chembur by roughly 40% — that conflict is retained and flagged rather than
        averaged away, per provenance rule 7. This chart is for corridor triage only. No number on it may reach a
        client without being re-derived from registered instruments on a declared carpet basis with the sample
        size shown.""", height="xtall")

figpage("A5_price_yield_map.png",
        "A5 · Price against yield",
        """Capital value and rental yield move in opposite directions across MMR with near-perfect consistency.
        Prime Mumbai yields 2–3%; Thane and Navi Mumbai reach 4–5% on asking figures
        <span class="src">[SRC-028]</span>. The line is not the insight — everyone knows the line exists.""",
        """<strong>The advisory proposition, stated precisely.</strong> Two flats in the same pocket, sitting on
        the same point of this line, can differ by 15% in realised price because of floor, view obstruction,
        society rules, sinking-fund position, maintenance burden and true door-to-door commute. Nobody publishes
        that. It has to be walked, asked and written down. Note also that these are gross yields on asking rent;
        net yield after maintenance, vacancy and property tax is materially lower, and net is the only figure
        that should ever be shown to an investor client.""")

figpage("A6_infrastructure_ladder.png",
        "A6 · Infrastructure status ladder",
        """Ten assets that developers cite in marketing, ranked by how real they are to a buyer deciding this
        quarter. Metro Line 3 is fully commissioned; NMIA has run around the clock since February 2026 and now
        carries international services; Metro 2B, 4/4A and 6 are all in 2026 commissioning windows; Metro 8 and
        the Virar–Alibaug corridor are approvals with a 2030+ horizon.""",
        """<strong>The most common analytical error in Indian real-estate research</strong> is scoring an
        announced asset and an operating asset identically. The weight column is the correction: an operational
        asset carries 1.00, a commissioning one 0.75, construction 0.45–0.60, and a mere approval 0.25–0.30. The
        schema enforces it by requiring <code>status</code>, <code>target_date</code>,
        <code>slippage_months</code> and <code>last_verified</code> on every infrastructure record, and by
        downgrading any asset whose target has moved twice.""")

figpage("A7_mmr_coverage_map.png",
        "A7 · MMR strategic coverage map",
        """A schematic of entry sequence, not geography. Relative position and adjacency carry meaning;
        distances and boundaries do not. Phase numbers follow the corrected entry model exactly, and each phase
        carries a trigger rather than a date.""",
        """<strong>On mapping honestly.</strong> This is deliberately drawn as a schematic because inventing
        boundary geometry is a data-integrity failure dressed up as a design decision. Production mapping — the
        kind that goes in front of a client — must use verified GIS boundaries and real coordinates from BMC,
        MMRDA or CIDCO sources. A hand-drawn polygon labelled 'Powai' will eventually be used to answer a
        question about whether a specific building is inside it, and it will answer wrongly.""",
        height="xtall")

figpage("A8_revenue_pool.png",
        "A8 · From market size to the pool one desk can reach",
        """The distance between the headline market and realistic Year-1 revenue is nearly four orders of
        magnitude. Eighty thousand city registrations become roughly fifteen reachable closures.""",
        """<strong>Four assumptions, and the plan to remove them.</strong> The corridor share, the pocket share,
        the intermediation rate and the reachable-closure count are all analyst estimates
        <span class="badge b-model">model</span>. Each can be measured directly: corridor and pocket share from
        IGR by sub-registrar office within the first month; intermediation rate from broker interviews and your
        own observed deals; reachable closures from your own funnel by day 90. Replacing these four numbers with
        observations is the single highest-value analytical task in the pilot.""")


# ================================================================ PART B
sec("B · The business")
page(f"""
  <div class="inner">
    <div class="num">B</div>
    <h1>The business</h1>
    <div class="sub">What is actually being built, how the layers depend on each other, which corridor to enter
    first, whether that recommendation survives being wrong about the weights, and what defensible position
    exists for a new entrant among 42,865 registered agents.</div>
    <div class="toc">
      <div><b>B1</b> &nbsp;The six-layer operating stack</div>
      <div><b>B2</b> &nbsp;Market entry priority — the corrected model</div>
      <div><b>B3</b> &nbsp;Sensitivity: does the recommendation survive?</div>
      <div><b>B4</b> &nbsp;Corridor scorecard</div>
      <div><b>B5</b> &nbsp;Corridor profiles — the three in contention</div>
      <div><b>B6</b> &nbsp;Competitive positioning</div>
    </div>
  </div>
""", cls="divider", label="Part B opener", group="__DIV__B")

figpage("B1_business_model_stack.png",
        "B1 · The six-layer operating stack",
        """Six layers, each with a distinct economic role. Layer 1 is the licence to operate, layer 2 is the
        reason to be believed, layer 4 pays for everything, and layer 5 is the only one that compounds.""",
        """<strong>The sequencing correction.</strong> Version 1 presented these as a ladder to be climbed.
        They are not. Layers 1, 2 and 4 are built simultaneously from week 1, with the compliance gate as the
        only hard dependency between them. A brokerage that completes its database before taking a client learns
        nothing about whether the database helps — and runs out of money finding out. Layer 5 deserves particular
        attention: it is a by-product of doing layer 4 properly, it cannot be bought or hired, and it is the only
        asset in this business that a better-funded competitor cannot simply purchase.""")

figpage("B2_entry_priority_model.png",
        "B2 · Market entry priority — the corrected model",
        """Seven weighted criteria, one weight vector, one score table, generating every artefact. Bars are
        stacked by contribution so it is always visible which criterion is carrying a corridor.""",
        """<strong>Three corrections from version 1.</strong> First, the workbook, the CSV and the PDF narrative
        disagreed with each other on both scores and rank; there is now one source. Second, execution simplicity
        is up-weighted from 0.09 to 0.14 — for a single founder with no team, travel time and site access are not
        a minor consideration, they are the binding constraint. Third, whitespace scores are re-based against the
        42,865 registered agents in Maharashtra <span class="src">[SRC-025]</span>, which moves the Western
        Suburbs down sharply. The tie between Navi Mumbai and the Western Suburbs at 7.48 is shown rather than
        hidden behind a third decimal place.""")

figpage("B3_sensitivity.png",
        "B3 · Does the recommendation survive being wrong?",
        """Two stress tests. Left: each weight doubled and halved in turn, showing Eastern/Central's remaining
        lead over the runner-up. Right: 5,000 weight vectors with every weight jittered ±50% simultaneously.""",
        """<strong>Why this page exists.</strong> A weighted scoring model with hand-chosen weights is an opinion
        with arithmetic attached. The only way to know whether it is a robust opinion is to break it deliberately.
        Eastern/Central survives every single-weight perturbation tested and wins 99% of randomised weightings.
        The corridors that displace it are those that win when transaction depth alone dominates — which is
        exactly the strategy a well-capitalised incumbent should run, and exactly the one a single founder
        cannot. That is a useful finding, not a caveat.""")

figpage("B4_corridor_heatmap.png",
        "B4 · Corridor scorecard",
        """The same 1–10 judgements as the model, laid out so the shape of each corridor is visible rather than
        collapsed into a single number. Read rows for a corridor's profile, columns for who wins each criterion.""",
        """<strong>The instructive row is the Western Suburbs.</strong> They win transaction depth outright with
        a 10 — the deepest deal flow in the region by a wide margin — and still finish fourth, because a 4 on
        competitive whitespace is what a new entrant actually experiences on their first day of calling. A
        corridor can lead the most heavily weighted column and still be the wrong place to start. That is the
        difference between a market assessment and an entry strategy.""")

figpage("B5_corridor_radar.png",
        "B5 · Corridor profiles — the three in contention",
        """Shape matters more than area. Eastern/Central has no axis below 7. Navi Mumbai is a spike — a 10 on
        infrastructure and a 6 on execution. Thane is the balanced value option, strongest on entry cost.""",
        """<strong>Prefer the shape with no hole in it.</strong> A single founder cannot compensate for a weak
        axis by allocating a specialist to it. Navi Mumbai's infrastructure story is the strongest in the region
        and genuinely observable rather than forecast — NMIA has been operating since December 2025 — but it sits
        behind a creek crossing and separate civic jurisdictions (CIDCO, NMMC, Panvel), each with different field
        definitions and record access. That is the 6 on execution, and for a one-person desk in Year 1 it is
        decisive.""")

figpage("B6_positioning.png",
        "B6 · Competitive positioning",
        """Two axes decide who wins a Mumbai buyer: how much evidence sits behind the advice, and how broad the
        geographic coverage is. Scale players own the top-left. Traditional brokers own the bottom-left. The
        bottom-right — deep evidence, narrow geography — is thinly held.""",
        """<strong>Why the gap is open, and why that is not comforting.</strong> Portals monetise listings rather
        than outcomes; scale brokerages cannot hold pocket-level detail across a 40-lead book; local brokers hold
        the knowledge but never write it down, so it dies with the relationship; institutional research stops
        above the retail buyer. The position is open. It is also open because it is hard and slow, not because
        nobody thought of it — it is defended by patience rather than by capital, which is a real moat but a
        cold one.""")


# ================================================================ PART C
sec("C · The work")
page(f"""
  <div class="inner">
    <div class="num">C</div>
    <h1>The work</h1>
    <div class="sub">The flow of work end to end, decomposed into twenty-four assignable packages, costed in
    hours against a real weekly capacity, and scheduled against gates rather than dates. This is the part of
    version 1 that existed only as a list of week numbers.</div>
    <div class="toc">
      <div><b>C1</b> &nbsp;The operating flow — six stages</div>
      <div><b>C2</b> &nbsp;Work breakdown structure — 24 packages</div>
      <div><b>C3</b> &nbsp;The Year-1 hour budget</div>
      <div><b>C4</b> &nbsp;The 90-day pilot, week by week</div>
      <div><b>C5</b> &nbsp;Twelve-month schedule</div>
      <div><b>C6</b> &nbsp;The operating week</div>
      <div><b>C7</b> &nbsp;Decision gates</div>
    </div>
  </div>
""", cls="divider", label="Part C opener", group="__DIV__C")

figpage("C1_operating_flow.png",
        "C1 · The operating flow",
        """Six stages from raw source to proprietary evidence. Each has a named input, a named output and a rule
        that must hold before work moves on. The loop from stage 6 back to stage 1 is the only part of the system
        that gets more valuable the longer it runs.""",
        """<strong>Where the compliance gate sits.</strong> Stages 1 to 4 — acquisition through interpretation —
        are lawful research from day one. Stages 5 and 6 involve dealing, advertising and brokerage of registered
        projects and cannot begin until MahaRERA registration and the Certificate of Competency are both in hand
        <span class="src">[SRC-001, SRC-002]</span>. This is the only hard dependency in the whole flow, and
        everything else runs concurrently.""")

figpage("C2_work_breakdown.png",
        "C2 · Work breakdown structure",
        """Six workstreams decomposed into twenty-four work packages, each small enough to be finished, dated and
        handed to someone else. Percentages are each workstream's share of the Year-1 hour budget, computed from
        the model on the next page rather than assigned by opinion.""",
        """<strong>Why granularity at this level matters.</strong> Work that cannot be named as a package cannot
        be scheduled, cannot be deliberately dropped when the week is short, and cannot be handed to a first hire.
        'Do market research' is not a work package; '2.3 Price truth engine — registered, asking and RR separated
        with basis and n' is. When month 7 arrives and deal execution needs sixteen hours a week, you will drop
        packages — and it matters enormously whether you drop 2.6 or 2.3.""", height="xtall")

figpage("C3_workload_budget.png",
        "C3 · The Year-1 hour budget",
        f"""One founder, 55 working hours a week, 52 weeks: {TOTAL_HOURS:,.0f} hours in total. That is the entire
        resource. The shape of the stack is the strategy — research-heavy at the start, deal-heavy by the middle,
        and never zero on compliance.""",
        """<strong>Read the three lines that matter.</strong> Desk research falls from 18 hours a week to 10 as
        the corridor is exhausted — if it does not fall, the corridor was too big. Deal execution rises from zero
        to sixteen hours and stays there. Compliance never reaches zero and spikes again at month 12 for the
        half-yearly filing and renewals <span class="src">[SRC-018]</span>.
        <strong>This is a budget, not a description.</strong> Its purpose is to be violated visibly: any week
        after month five where deal execution is zero is a week the plan has failed, and the chart exists so that
        failure is noticed in week one rather than quarter three.""")

figpage("C4_pilot_90_day.png",
        "C4 · The 90-day pilot, week by week",
        """Twenty-four scheduled items across twelve weeks, each carrying its expected hours, its concrete output
        and the gate that closes it. The compliance gate at week 6 is marked on every row.""",
        """<strong>On the unallocated remainder.</strong> Scheduled hours run well below 55 in most weeks, and
        that is deliberate. Mumbai traffic, a seller who reschedules, a bank that wants one more document, a
        client who calls at 21:00 — these consume the difference every week without exception. A plan that
        schedules 55 of 55 hours does not survive week one; it just fails invisibly and then gets abandoned as
        unrealistic when the failure was in the planning, not the market.""",
        height="xtall")

figpage("C5_gantt_12_month.png",
        "C5 · Twelve-month schedule",
        """Sixteen workstreams over twelve months. Every bar ends at a diamond, and the diamond is a gate — a
        written test — rather than a date.""",
        """<strong>The expansion bars are conditional and the chart should be read that way.</strong> Corridor 2
        opens at month 8 only if corridor-1 economics have repeated; if they have not, months 8–12 are spent
        making corridor 1 work rather than acquiring a second place to be mediocre. A Gantt chart that shows
        expansion as inevitable is a Gantt chart that will be followed off a cliff, which is why the gate text
        sits beside every single bar.""")

figpage("C6_operating_week.png",
        "C6 · The operating week",
        """A steady-state week from month 6 onward: 51 committed hours across six workstreams, with four hours
        held in reserve. This is what the hour budget looks like when it hits a calendar.""",
        """<strong>Three structural rules worth keeping even if the specific grid changes.</strong> Site visits
        are batched by pocket, because travel is the single largest hidden cost in an MMR desk. Deal work is never
        scheduled after research on the same day, because research expands to fill whatever it is given and will
        quietly eat the selling block. And the CRM is updated the same day, twice a week — a CRM updated weekly
        is a CRM updated from memory, and memory is where lost reasons go to die.
        Saturday is not optional: it is the highest-conversion slot in Indian residential real estate, because it
        is when both decision-makers in a household can see a flat together.""")

figpage("C7_decision_gates.png",
        "C7 · Decision gates",
        """Four moments at which the plan is allowed to change: day 30, day 60, day 90 and month 8. Each has a
        written test, a pass route and — more importantly — a fail route.""",
        """<strong>The fail routes are the point.</strong> A plan without a defined way to stop is a plan that
        gets continued past the point of evidence, because at every individual moment continuing feels cheaper
        than admitting the corridor was wrong. Write the date and the answer against every checkbox. A gate
        assessed from memory always passes.""")


# ================================================================ PART D
sec("D · Economics")
page(f"""
  <div class="inner">
    <div class="num">D</div>
    <h1>Economics &amp; control</h1>
    <div class="sub">What the funnel has to deliver, what a closure is actually worth after tax, how much capital
    the plan needs before it turns, which nine numbers to manage, what can go wrong, and where leads come from.
    None of this existed in version 1.</div>
    <div class="toc">
      <div><b>D1</b> &nbsp;The deal funnel — three scenarios</div>
      <div><b>D2</b> &nbsp;Unit economics — one closure, then a year</div>
      <div><b>D3</b> &nbsp;The cash curve and capital requirement</div>
      <div><b>D4</b> &nbsp;The KPI tree</div>
      <div><b>D5</b> &nbsp;Risk register</div>
      <div><b>D6</b> &nbsp;Lead channels</div>
    </div>
  </div>
""", cls="divider", label="Part D opener", group="__DIV__D")

figpage("D1_deal_funnel.png",
        "D1 · The deal funnel",
        """Five stages, three scenarios. The base case runs 900 raw enquiries to 15 closures across Year 1 — a
        1.7% end-to-end conversion, which is normal for residential brokerage and shocking to anyone who has not
        run one.""",
        """<strong>Two numbers govern everything downstream.</strong> The qualified-lead rate (27% in the base
        case) and site-visit conversion (46%). Both are assumptions here and both are measurable within ninety
        days. Note the definition being used: a lead is qualified only if budget, timeline, decision authority
        <em>and</em> area fit all pass. Loosening that definition is the most common way a founder hides a demand
        problem from themselves for two quarters, because the enquiry count keeps rising while the visit count
        does not.""")

figpage("D2_unit_economics.png",
        "D2 · Unit economics",
        f"""Left: the cash journey of one average closure — {rs(CONSID,'Cr')} consideration, {RATE*100:.2f}%
        blended commission, 18% GST added and remitted, 2% TDS withheld and recoverable. Right: the Year-1
        profit and loss with the founder's own time priced in.""",
        f"""<strong>The number this plan should be judged on.</strong> {rs(POST_BASE)} post-tax for
        {TOTAL_HOURS:,.0f} founder-hours is about <strong>₹{POST_BASE/TOTAL_HOURS:,.0f} an hour</strong>. In the
        conservative case it is roughly a third of that. Anyone considering this venture should compare those two
        figures honestly against their salaried alternative before week one, not after month nine. The upside
        argument is real — the asset being built compounds and the Year-3 economics look nothing like Year 1 —
        but it should be made against an honest Year-1 number rather than instead of one.
        Tax shown is indicative on FY2025-26 individual new-regime slabs for a proprietorship and is not advice
        <span class="src">[SRC-031]</span>.""")

figpage("D3_cash_runway.png",
        "D3 · The cash curve",
        """Cumulative cash from a standing start, in the base and conservative cases. The trough — not the
        break-even point — is the number that determines whether the plan is viable, because it is what must be
        in the bank on day one.""",
        """<strong>Raise against the conservative case.</strong> The difference between the two curves is a
        single assumption: whether the first closure lands in month 5 or month 7. That is not a wide range for a
        market where deals routinely take 60–120 days from first enquiry to registration, and the second case is
        at least as likely as the first. Founder drawings are the largest line in the burn at ₹60,000 a month, so
        the honest first question is not 'is the market good?' — it demonstrably is — but 'how long can this
        household run on less?'""")

figpage("D4_kpi_tree.png",
        "D4 · The KPI tree",
        """Revenue is not a lever; it is an outcome. Nine measurable quantities produce it, grouped into volume,
        value and efficiency, so a bad result at the top can be traced to the branch that caused it.""",
        """<strong>Two rules make the tree work.</strong> Every KPI is computed from the CRM rather than
        recalled, and the qualified-lead definition never moves. Watch the efficiency branch hardest: research
        hours per closure must fall across the year, or the intelligence layer is not paying for itself and is a
        hobby with a spreadsheet. The referral coefficient above 0.5 is the point at which the business starts
        compounding rather than being re-sold from scratch every quarter.""")

figpage("D5_risk_matrix.png",
        "D5 · Risk register",
        """Fourteen risks positioned by likelihood and impact, ranked by severity, each with the control that
        addresses it and the phase in which it bites.""",
        """<strong>Re-score this at every gate.</strong> The register is only useful if it moves. Risks 1 and 6 —
        marketing before certification, and DPDP non-compliance — fall away once compliance is complete. Risks 4
        and 8 — runway and commission disputes — rise sharply the moment real money is in play, and they are
        barely visible in month 1 when they are cheapest to control. The top three by severity all concern the
        founder's own behaviour rather than the market, which is the honest finding of this exercise.""",
        height="xtall")

figpage("D6_lead_channels.png",
        "D6 · Lead channels",
        """Eight channels by cost per qualified lead, close rate, and months to become productive. The cheapest
        channels are the slowest to build and the hardest for anyone to buy.""",
        """<strong>Build the slow ones first.</strong> A referral engine takes months to establish and cannot be
        outspent by a competitor; a portal listing works this afternoon and can be outbid by anyone, also this
        afternoon. All figures here are planning hypotheses <span class="badge b-model">model</span> — no
        channel-level acquisition data exists for a business that has not yet run. Tag every lead with its source
        at capture and redraw this chart at day 90 with real numbers. And note: every published brief and listing
        is an advertisement under the MahaRERA disclosure order and must carry the QR code and registration
        number <span class="src">[SRC-017]</span>.""")


# ================================================================ PART E
sec("E · The system")
page(f"""
  <div class="inner">
    <div class="num">E</div>
    <h1>The system</h1>
    <div class="sub">The data architecture that makes the advice defensible: seven geographic levels, twelve
    domains, a source stack with acquisition rules, the compliance path and calendar, the client-fit engine, and
    the eight provenance rules that hold it all together.</div>
    <div class="toc">
      <div><b>E1</b> &nbsp;Geographic hierarchy — L0 to L6</div>
      <div><b>E2</b> &nbsp;Data domains and staleness rules</div>
      <div><b>E3</b> &nbsp;The source stack and acquisition law</div>
      <div><b>E4</b> &nbsp;Compliance critical path and calendar</div>
      <div><b>E5</b> &nbsp;The client-fit engine</div>
      <div><b>E6</b> &nbsp;The eight provenance rules</div>
    </div>
  </div>
""", cls="divider", label="Part E opener", group="__DIV__E")

figpage("E1_geo_hierarchy.png",
        "E1 · Geographic hierarchy",
        """The uploaded blueprint's L0–L6 structure is kept unchanged, because it is correct. What is added is
        the explicit designation of L4 (pocket) as the research unit and L6 (unit) as the closure unit.""",
        """<strong>Two rules enforced in the schema.</strong> No fact may exist without a geo_id — a price
        belonging to 'Powai' in general rather than to a named pocket is not usable evidence. And aggregation
        only ever runs upward: an L4 pocket figure is built from L5 and L6 observations, never inherited downward
        from an L3 locality average. Downward inheritance is how a ₹28,000/sq ft locality average ends up quoted
        for a ground-floor flat facing a nullah, and it is the most common way an otherwise careful dataset
        starts producing confident nonsense.""")

figpage("E2_data_domains.png",
        "E2 · Data domains and staleness",
        """Twelve domains, each with the minimum fields that must exist before a record is accepted and the
        number of days after which the system marks it stale on every client-facing screen.""",
        """<strong>The four fields version 1 did not carry</strong> and which are now mandatory on every record:
        <code>sample_size</code>, <code>observed_date</code>, <code>stale_after_days</code> and
        <code>conflict_flag</code>. Together they answer the only question that matters when a client challenges
        a number in a negotiation — where did this come from, when was it true, how many observations support it,
        and what still disagrees with it? Being able to answer that in ten seconds is the entire difference
        between an advisor and a person with opinions.""", height="xtall")

figpage("E3_source_stack.png",
        "E3 · The source stack",
        """Four tiers. Statutory records establish what is true; institutional research establishes context at
        city and zone level; portals establish what is currently being asked; your own closed deals establish
        what actually transacted. They are not interchangeable, and confusing them is expensive.""",
        """<strong>On acquisition, practically.</strong> Government portals are published for public use.
        Institutional reports should be cited, not republished. Portal terms of use are enforceable as contract
        in India and clickwrap acceptance binds you <span class="src">[SRC-030]</span> — collect manually or
        through a permitted feed, and do not build the business on a scraper you would not describe to the portal
        in a meeting. Anything containing personal data falls under the DPDP Rules, which extend consent
        obligations even to personal data that is already public, with no small-business exemption
        <span class="src">[SRC-023]</span>.""")

figpage("E4_compliance_path.png",
        "E4 · Compliance path and calendar",
        """Above: the six-week critical path from application to the moment marketing may lawfully begin. Below:
        the recurring obligations across an Indian financial year, which do not stop once the path is complete.""",
        """<strong>This page is the one to print and pin up.</strong> The Certificate of Competency requirement
        that took effect in January 2026 is the longest-lead item in the venture and cannot be compressed by
        working harder <span class="src">[SRC-002]</span>. Book the training slot in week 1, before the market
        research, before the corridor is even chosen — the research can happen while you wait, but nothing can
        happen if you have not started the clock. Every item in the lower panel is a diary entry with a named
        owner and an evidence file from week 1; compliance discovered in month 9 is compliance already breached.""",
        height="xtall")

figpage("E5_client_fit_engine.png",
        "E5 · The client-fit engine",
        """A shortlist is produced by elimination and only then by scoring. Five hard filters remove units
        permanently; what survives is ranked on six weighted factors.""",
        """<strong>The all-in cost table is the cheapest credibility available to a new advisor.</strong> Most
        buyers arrive having budgeted for the agreement value alone. Stamp duty at 6% for a male buyer or 5% for a
        sole female owner — both including the 1% metro cess — plus 1% registration capped at ₹30,000, plus 1% TDS
        under section 194-IA above ₹50 lakh, plus brokerage with 18% GST, adds roughly 8% to the transaction
        <span class="src">[SRC-013, SRC-024, SRC-012]</span>. Getting this right on the first call, unprompted,
        does more for trust than any amount of market commentary. Note also that the 15-year resale lock-in
        formerly attached to the women's concession was removed in 2026.""")

figpage("E6_data_quality_rules.png",
        "E6 · The eight provenance rules",
        """The rules version 1 got right, preserved intact, each now paired with the specific failure it exists
        to prevent.""",
        """<strong>What is added is enforcement.</strong> Each rule is implemented as a NOT NULL constraint or a
        blocked operation in the workbook, not as a convention described in a document. A data-quality rule that
        depends on the founder remembering it at 22:00 on a Friday, three hours before a client meeting, is not a
        rule — it is an aspiration, and it will be the first thing to go.""")


# ================================================================ PART F
sec("F · Playbooks")
page(f"""
  <div class="inner">
    <div class="num">F</div>
    <h1>Playbooks</h1>
    <div class="sub">The five operating procedures that turn the system into a service: how to verify a pocket in
    the field, how to run a first client conversation, how to negotiate with evidence, what to check before
    closure, and how to convert a closed client into the next two.</div>
    <div class="toc">
      <div><b>F1</b> &nbsp;Field research protocol</div>
      <div><b>F2</b> &nbsp;The first client conversation</div>
      <div><b>F3</b> &nbsp;Negotiation playbook</div>
      <div><b>F4</b> &nbsp;Documentation and closure</div>
      <div><b>F5</b> &nbsp;Post-close and the referral flywheel</div>
    </div>
  </div>
""", cls="divider", label="Part F opener", group="__DIV__F")

FIELD = [
    ("True commute", "Three time windows: 08:15–09:30, 13:00, 19:00–20:30. Door to office door, by the mode "
     "the client will actually use. Record the route and the date, not just the minutes.",
     "Advertised distance systematically understates time. A 9 km commute in Mumbai can be 25 minutes or 75."),
    ("Society restrictions", "Society office and security, plus two independent broker confirmations. Ask "
     "specifically: non-vegetarian, pets, bachelors, unmarried couples, religion, parking allotment, guest policy.",
     "Restrictions invalidate client fit entirely and are rarely disclosed until the offer stage. Note that some "
     "restrictions raise legal and fair-dealing questions — record what the society states, advise the client "
     "factually, and do not become the instrument of an unlawful exclusion."),
    ("Maintenance and sinking fund", "A recent bill from an owner, cross-checked with a second owner and a "
     "broker. Ask about pending major repairs and any special levy under discussion.",
     "Maintenance changes affordability and destroys net yield. A ₹12,000 monthly charge on a ₹75,000 rent is "
     "16% of gross before vacancy and tax."),
    ("Inventory truth", "Developer, two brokers, portal listings and your own site observation, on the same day.",
     "Phantom and duplicated inventory is the norm on portals. A unit listed by four brokers is one unit."),
    ("Negotiability", "Initial ask, revised quote after a serious enquiry, incentives offered, and the last "
     "closed comparable from IGR. Log the date of each.",
     "Discount-to-close is the single most useful proprietary number you will build, and no public source has it."),
    ("Micro-pocket quality", "Walk it. Noise, access road width, waterlogging marks on compound walls, "
     "walkability to transit, view obstruction from the specific floor, afternoon sun.",
     "This explains most of the 30–50% price dispersion inside a single locality, and it cannot be desk-researched."),
    ("Developer execution", "Construction progress against the RERA quarterly progress report, plus the "
     "promoter's delivery record on prior projects.",
     "Possession delay is the largest single source of buyer regret in under-construction purchases."),
    ("Resident and tenant context", "Non-sensitive observation and voluntary conversation only: household "
     "composition patterns, commute destinations, school catchment use.",
     "Demand fit can be understood without unlawful profiling. Capture property-relevant facts, never protected "
     "characteristics, and never use them as filters."),
]
page(f"""
  <h2>F1 · Field research protocol</h2>
  <div class="deck">Eight things that must be verified on foot for every pocket in the set, the method for each,
  and the business reason it exists. Three independent inputs per locality is the standard; a single broker's
  word is a hypothesis, not a finding.</div>
  {tbl(["Verify", "Method and standard", "Why it exists"],
       [[f"<strong>{a}</strong>", b, c] for a, b, c in FIELD],
       widths=["34mm", "112mm", "121mm"])}
  <div class="callout warn" style="margin-top:3mm">
    <div class="h">The rule that makes field work compound</div>
    <p style="margin:0">Record it the same day, in the system, with the date and the method — not in a notebook,
    not in your head, not in a WhatsApp thread. Field intelligence that is not written down within twenty-four
    hours is field intelligence that will be re-collected in six months, at full cost, having in the meantime
    been unavailable to every client who needed it.</p>
  </div>
""", label="F1 Field research protocol")

page(f"""
  <h2>F2 · The first client conversation</h2>
  <div class="deck">Forty-five minutes, structured. The objective is not to show inventory — it is to establish
  the four qualification tests, surface the constraints the client has not thought about, and demonstrate in
  passing that you know things the last three brokers did not.</div>
  <div class="grid2">
    <div>
      <h3>The four qualification tests</h3>
      <table class="tbl-compact">
        <tr><td style="width:24mm"><strong>Budget</strong></td><td>All-in, not agreement value. Walk them through
        the 8% transaction stack on the spot — stamp duty, registration, TDS, brokerage and GST. Establish the
        funding split and whether the loan is sanctioned or assumed.</td></tr>
        <tr><td><strong>Timeline</strong></td><td>When do they need to move, and what is driving it — lease
        expiry, school admission, possession of a sold property? A client with no forcing event is a client who
        will look for eighteen months.</td></tr>
        <tr><td><strong>Authority</strong></td><td>Who else decides? Spouse, parents, a sibling abroad? Find the
        absent decision-maker in the first meeting, not at the offer stage.</td></tr>
        <tr><td><strong>Area fit</strong></td><td>Does the requirement actually intersect your pocket set? If it
        does not, say so and refer it out. A referral given honestly returns; a client dragged into the wrong
        corridor does not.</td></tr>
      </table>
      <div class="callout crit" style="margin-top:3mm">
        <div class="h">Say this out loud in the first meeting</div>
        <p style="margin:0" class="small">"I work six localities in depth rather than the whole city. If what
        you need is outside them, I will tell you and introduce you to someone better placed." It costs you one
        client in ten and buys the credibility that closes the other nine.</p>
      </div>
    </div>
    <div>
      <h3>What to bring, and what it signals</h3>
      <ul class="clean small">
        <li><strong>The all-in cost sheet</strong> for their stated budget, computed live. Signals: this person
        does arithmetic, not enthusiasm.</li>
        <li><strong>One pocket brief</strong> with registered comparables, sample sizes and dates — not asking
        prices. Signals: this person has sources.</li>
        <li><strong>The infrastructure status ladder</strong> for their corridor, with operational assets
        separated from announced ones. Signals: this person will not sell you a metro line that does not exist.</li>
        <li><strong>Two things you know that they cannot look up</strong> — a society's pet policy, a specific
        tower's afternoon sun, a maintenance figure. Signals: this person has walked the ground.</li>
      </ul>
      <h3 style="margin-top:4mm">What to record before you leave</h3>
      <ul class="tight small">
        <li>All four qualification answers, verbatim where possible</li>
        <li>Lead source, tagged at capture — never reconstructed later</li>
        <li>Stated hard filters and stated preferences, kept separate</li>
        <li>DPDP notice given, consent recorded, purpose stated
          <span class="src">[SRC-023]</span></li>
        <li>Next action and a date. Every lead has one, always</li>
      </ul>
      <p class="tiny" style="margin-top:2mm">Collect the minimum personal data necessary for the purpose, state
      that purpose, and delete it on the retention schedule. This is a legal obligation, not a courtesy, and it
      applies from the first conversation.</p>
    </div>
  </div>
""", label="F2 The first client conversation")

page(f"""
  <h2>F3 · Negotiation playbook</h2>
  <div class="deck">Negotiation in Mumbai residential resale is not adversarial theatre; it is the orderly
  presentation of evidence to a seller who has usually anchored on a number they heard from a neighbour in 2023.
  The desk's advantage is that it can show the workings.</div>
  <div class="grid3">
    <div class="box">
      <h4>Before the offer</h4>
      <ul class="tight small">
        <li>Pull every registered comparable in the building and the adjacent two, twelve months back, from IGR
        <span class="src">[SRC-015]</span></li>
        <li>Normalise all of them to carpet area — never negotiate across area bases</li>
        <li>Establish the Ready Reckoner floor for the address; note that RR is frozen for FY2026-27
        <span class="src">[SRC-014]</span></li>
        <li>Record days-on-market and any prior price revisions</li>
        <li>Check the society's transfer charges and NOC position before quoting an all-in figure</li>
      </ul>
    </div>
    <div class="box o">
      <h4>The four levers, in order</h4>
      <ul class="tight small">
        <li><strong>Evidence.</strong> Registered comparables with dates and carpet normalisation. This alone
        moves most sellers, because most have never seen them.</li>
        <li><strong>Certainty.</strong> A sanctioned loan and a clean timeline is worth real money to a seller
        with their own purchase pending.</li>
        <li><strong>Condition and cost.</strong> Pending society levies, deferred repairs, non-conforming
        alterations — priced, not complained about.</li>
        <li><strong>Terms.</strong> Possession date, token structure, who bears the society transfer fee. Often
        cheaper to trade than headline price.</li>
      </ul>
    </div>
    <div class="box r">
      <h4>What not to do</h4>
      <ul class="tight small">
        <li>Do not quote an asking-price average as if it were a market rate — the other side's broker will know.</li>
        <li>Do not offer an opinion on title. Flag the question and route it to counsel, in writing.</li>
        <li>Do not commit to a possession date the RERA quarterly progress report does not support.</li>
        <li>Do not discount your own brokerage to close. It re-prices every future deal and signals that the
        advice was never worth what you said it was.</li>
        <li>Do not proceed on a verbal fee understanding. Written terms before engagement, every time.</li>
      </ul>
    </div>
  </div>
  <div class="callout" style="margin-top:2mm">
    <div class="h">Capture, on the same day</div>
    <p style="margin:0" class="small">Initial ask · revised quote · incentives offered · final closed price ·
    days from first offer to agreement · who moved first · the reason the seller gave. Six months of this across
    twenty-five pockets is a discount-to-close dataset that does not exist anywhere else, and it makes every
    subsequent negotiation shorter and better. This is the compounding loop from C1, in its most concrete form.</p>
  </div>
""", label="F3 Negotiation playbook")

page(f"""
  <h2>F4 · Documentation and closure</h2>
  <div class="deck">The checklist below is an operating aid for a broker coordinating a transaction, not a legal
  opinion. Title verification, drafting and advice on any of these documents must come from a qualified advocate
  engaged by the client. The broker's job is to make sure nothing is missed and nothing is misrepresented.</div>
  <div class="grid2">
    <div>
      <h3>Before the agreement</h3>
      <table class="tbl-compact">
        <tr><td style="width:36mm"><strong>Title chain</strong></td><td>Advocate-led search. Prior conveyance,
        index-II extracts, mutation entries. Broker collects, counsel opines.</td></tr>
        <tr><td><strong>RERA position</strong></td><td>Project registration, promoter, status and quarterly
        progress report for under-construction; verify against the MahaRERA portal, not the brochure
        <span class="src">[SRC-016]</span>.</td></tr>
        <tr><td><strong>Society records</strong></td><td>Share certificate, NOC, transfer charges, no-dues,
        pending levies and any litigation the society is party to.</td></tr>
        <tr><td><strong>Encumbrance</strong></td><td>Existing mortgage and the release mechanism. Confirm which
        lender holds the original documents and the timeline to release.</td></tr>
        <tr><td><strong>Approvals</strong></td><td>Occupancy certificate, commencement certificate, sanctioned
        plan against as-built. Unauthorised alterations are a live risk.</td></tr>
        <tr><td><strong>Seller capacity</strong></td><td>Identity, ownership, power of attorney if any, and
        consent of all co-owners including absent ones.</td></tr>
      </table>
    </div>
    <div>
      <h3>At and after execution</h3>
      <table class="tbl-compact">
        <tr><td style="width:36mm"><strong>Stamp duty</strong></td><td>6% male buyer, 5% sole female owner, both
        including 1% metro cess. Computed on the higher of consideration and Ready Reckoner value
        <span class="src">[SRC-013]</span>.</td></tr>
        <tr><td><strong>Registration</strong></td><td>1% capped at ₹30,000. Within four months of execution.</td></tr>
        <tr><td><strong>TDS 194-IA</strong></td><td>Buyer deducts 1% where consideration is ₹50 lakh or more;
        Form 26QB within thirty days of the month end. Advise it early — buyers routinely miss it
        <span class="src">[SRC-024]</span>.</td></tr>
        <tr><td><strong>Handover</strong></td><td>Meter readings, society transfer, keys, original documents,
        pending dues settled and evidenced.</td></tr>
        <tr><td><strong>Your own file</strong></td><td>Written brokerage terms, introduction trail, invoice with
        18% GST, TDS at 2% under 194H reconciled to 26AS/AIS
        <span class="src">[SRC-012, SRC-024]</span>.</td></tr>
        <tr><td><strong>MahaRERA record</strong></td><td>Log the facilitated project for the half-yearly
        compliance report while the detail is fresh <span class="src">[SRC-018]</span>.</td></tr>
      </table>
    </div>
  </div>
  <div class="callout crit" style="margin-top:1mm">
    <div class="h">The line not to cross</div>
    <p style="margin:0" class="small">A broker may collect, organise and flag. A broker may not opine on title,
    draft the agreement, or reassure a client that a defect is immaterial. Where a document raises a question,
    the answer is "I don't know — let's put that to your advocate", in writing, that day. Overstating what the
    record supports is the fastest route to a claim you cannot defend, and it is risk 10 on the register.</p>
  </div>
""")

page(f"""
  <h2>F5 · Post-close and the referral flywheel</h2>
  <div class="deck">The closure is the beginning of the most valuable phase, and it is the phase almost every
  broker skips. Two things happen here: the client becomes a source of the next two clients, and the deal becomes
  permanent structured evidence.</div>
  <div class="grid2">
    <div>
      <h3>The ninety days after handover</h3>
      <table class="tbl-compact">
        <tr><td style="width:22mm"><strong>Week 1</strong></td><td>Handover confirmation, society introduction,
        utility transfers. Unpaid, unglamorous, and remembered for years.</td></tr>
        <tr><td><strong>Week 3</strong></td><td>Check-in call. Anything not working? This is where you learn what
        the building is actually like to live in — and that goes into the dataset.</td></tr>
        <tr><td><strong>Week 6</strong></td><td>The referral ask, made explicitly and once: "If anyone you know
        is looking in Powai or Kanjurmarg, I'd value the introduction." Scripted, not hinted.</td></tr>
        <tr><td><strong>Week 12</strong></td><td>Send them something useful and unrequested — the quarterly
        pocket brief for their building. Cost: nothing. Effect: you are still their broker in three years.</td></tr>
      </table>
      <div class="callout good" style="margin-top:3mm">
        <div class="h">Referral coefficient above 0.5</div>
        <p style="margin:0" class="small">Every two closed clients producing one new qualified referral is the
        threshold at which acquisition cost starts falling instead of rising. It is the cheapest channel on
        page 38 and the slowest to build. It is also the only one that cannot be bought by a competitor.</p>
      </div>
    </div>
    <div>
      <h3>What the closed deal contributes to the system</h3>
      <ul class="clean small">
        <li><strong>Closed price against asking</strong> — the discount-to-close observation that no public
        source holds</li>
        <li><strong>Days at each stage</strong> — enquiry to visit, visit to offer, offer to agreement, agreement
        to registration</li>
        <li><strong>Every objection raised</strong> and how it was answered, including the ones that were fatal</li>
        <li><strong>The society's actual rules</strong> as encountered, not as advertised</li>
        <li><strong>Real maintenance and transfer charges</strong>, from the bill</li>
        <li><strong>Counterparty response times</strong> — which brokers, developers and lenders actually move</li>
        <li><strong>Lost-deal post-mortems</strong>, which are worth more than the wins and are the first thing
        to get skipped</li>
      </ul>
      <div class="callout" style="margin-top:3mm">
        <div class="h">Why this is the moat</div>
        <p style="margin:0" class="small">A competitor can buy every portal subscription, hire consultants and
        read every published report. They cannot buy the record of what forty specific flats in your twenty-five
        pockets actually transacted at, why eleven buyers walked away, and which three societies quietly refuse
        pets. That dataset costs nothing extra to build — it costs the discipline not to skip stage 6 when the
        deal is done and the next client is calling.</p>
      </div>
    </div>
  </div>
""", label="F5 Post-close and the referral flywheel")


# ================================================================ PART G
sec("G · Appendices")
page(f"""
  <div class="inner">
    <div class="num">G</div>
    <h1>Appendices</h1>
    <div class="sub">The source registry with full URLs and access dates, the data dictionary, the 90-day
    checklist in operating form, a glossary, and the first week's instructions.</div>
    <div class="toc">
      <div><b>G1</b> &nbsp;Source registry — 33 sources</div>
      <div><b>G2</b> &nbsp;Data dictionary</div>
      <div><b>G3</b> &nbsp;The 90-day checklist</div>
      <div><b>G4</b> &nbsp;Glossary</div>
      <div><b>G5</b> &nbsp;What to do on Monday morning</div>
    </div>
  </div>
""", cls="divider", label="Part G opener", group="__DIV__G")

# --- G1 source registry, split across pages
BADGE = {"High": "b-high", "Medium": "b-med", "Low": "b-low"}
srows = []
for sid, cat, name, url, use, refresh, conf in E.SOURCES:
    short = url.replace("https://", "").replace("http://", "")
    if len(short) > 76:
        short = short[:73] + "…"
    srows.append([
        f'<span class="src" style="font-weight:700;color:var(--blue)">{sid}</span>',
        f"<strong>{H.escape(name)}</strong><br><span class='tiny'>{H.escape(cat)} · {H.escape(refresh)}</span>",
        H.escape(use),
        f'<span class="tiny">{H.escape(short)}</span>',
        f'<span class="badge {BADGE[conf]}">{conf.lower()}</span>',
    ])

for i, start in enumerate(range(0, len(srows), 12)):
    part = srows[start:start + 12]
    page(f"""
      <h2>G1 · Source registry{' <span style="color:var(--muted);font-weight:400">· continued</span>' if i else ''}</h2>
      {'<div class="deck">Thirty-three sources, each with the specific fact it supports, its refresh cadence and a confidence grade. Every source was accessed on 14 August 2026. Market and regulatory facts move — re-verify before relying on any of them.</div>' if i == 0 else ''}
      {tbl(["ID", "Source", "Key fact or use", "URL", "Conf."], part,
           cls="tbl-compact", widths=["13mm", "50mm", "108mm", "68mm", "14mm"])}
    """, label="G1 Source registry" + (" (continued)" if i else ""))

# --- G2 data dictionary
DD = [
    ("geo", "geo_id", "text", "yes", "Immutable geography identifier (L0–L6). No fact exists without one."),
    ("geo", "parent_geo_id", "text", "no", "Parent geography id — enforces the upward-only aggregation rule."),
    ("geo", "level", "enum", "yes", "L0 / L1 / L2 / L3 / L4 / L5 / L6"),
    ("geo", "boundary_ref", "text", "no", "Verified GIS boundary reference. Never a hand-drawn polygon."),
    ("pricing", "price_type", "enum", "yes", "asking / registered / ready_reckoner / launch — four fields, never blended"),
    ("pricing", "area_basis", "enum", "yes", "carpet / built_up / saleable. Comparison across bases is blocked."),
    ("pricing", "price_psf", "number", "yes", "Price per sq ft on the declared area basis"),
    ("pricing", "sample_size", "integer", "yes", "Observations behind the aggregate. Below the domain minimum, downgraded visually."),
    ("rental", "monthly_rent", "number", "yes", "Monthly asking or closed rent — price_type applies here too"),
    ("rental", "configuration", "text", "yes", "1BHK / 2BHK / 3BHK"),
    ("rental", "furnishing", "enum", "yes", "bare / semi / full"),
    ("rental", "deposit_months", "number", "no", "Security deposit expressed in months of rent"),
    ("project", "rera_id", "text", "yes", "MahaRERA project registration id, or the explicit value NOT_REGISTERED"),
    ("project", "possession_date", "date", "no", "Declared possession date from the RERA filing, not the brochure"),
    ("project", "qpr_ref", "text", "no", "Quarterly progress report reference and date"),
    ("developer", "avg_delay_months", "number", "no", "Observed delivery slippage across the promoter's prior projects"),
    ("infra", "status", "enum", "yes", "operational / commissioning / under_construction / approved / proposed / rumoured"),
    ("infra", "slippage_months", "number", "no", "Cumulative delay against the earliest published target"),
    ("infra", "last_verified", "date", "yes", "When the status was last checked against the source"),
    ("risk", "risk_type", "text", "yes", "flood / title / CRZ / environment / litigation / oversupply / infra"),
    ("risk", "severity", "enum", "yes", "low / medium / high — high is a hard filter, not a discount"),
    ("fact", "source_ref", "text", "yes", "Source registry id. Mandatory on every record without exception."),
    ("fact", "observed_date", "date", "yes", "Date the fact applies to — not the date it was copied"),
    ("fact", "confidence", "enum", "yes", "high / medium / low"),
    ("fact", "stale_after_days", "integer", "yes", "Domain refresh rule; drives the client-facing freshness display"),
    ("fact", "conflict_flag", "boolean", "yes", "Marks an unresolved disagreement between sources. Retained, not averaged."),
    ("lead", "lead_id", "text", "yes", "Lead identifier"),
    ("lead", "source_channel", "text", "yes", "Tagged at capture. Reconstructing it later produces fiction."),
    ("lead", "qualified", "boolean", "yes", "True only if budget, timeline, authority and area fit all pass"),
    ("lead", "consent_ref", "text", "yes", "DPDP notice and consent record reference"),
    ("lead", "retention_until", "date", "yes", "Deletion date under the stated retention policy"),
    ("deal", "stage", "enum", "yes", "lead / qualified / visit / negotiation / closure / lost"),
    ("deal", "closed_price", "number", "no", "Actual registered consideration, from the instrument"),
    ("deal", "commission_realised", "number", "no", "Realised commission, net of TDS under 194H"),
    ("deal", "payout_days", "integer", "no", "Days from closure milestone to cash receipt, per counterparty"),
    ("deal", "lost_reason", "text", "no", "Mandatory on any deal marked lost. No blank values accepted."),
]
page(f"""
  <h2>G2 · Data dictionary</h2>
  <div class="deck">Thirty-six fields across nine tables. Required fields are enforced as NOT NULL constraints,
  not as documentation. The full machine-readable dictionary, along with nineteen other data files, ships in
  <code>/data/</code>.</div>
  <div style="column-count:2;column-gap:9mm">
  {tbl(["Table", "Field", "Type", "Req", "Description"],
       [[f'<code>{t}</code>', f'<strong>{f}</strong>', ty,
         ('<span style="color:var(--critical);font-weight:700">yes</span>' if r == "yes" else "no"), d]
        for t, f, ty, r, d in DD],
       cls="tbl-compact", widths=["15mm", "26mm", "12mm", "9mm", "auto"])}
  </div>
""", label="G2 Data dictionary")

# --- G3 the 90-day checklist
for i, start in enumerate(range(0, len(E.PILOT_90), 8)):
    part = E.PILOT_90[start:start + 8]
    rows = []
    for wk, ws, goal, out, gate, hrs in part:
        col = {"compliance": "var(--violet)", "research": "var(--blue)", "field": "var(--aqua)",
               "demand": "var(--orange)", "deal": "#9a6a00", "system": "var(--magenta)"}[ws]
        rows.append([
            f'<strong style="color:{col}">W{wk}</strong>',
            f'<strong>{H.escape(goal)}</strong><br><span class="tiny" style="color:{col}">'
            f'{H.escape(dict((k,l) for k,l,_,_ in E.WORKSTREAMS)[ws])}</span>',
            H.escape(out),
            f'<span style="color:{col}">▪</span> {H.escape(gate)}',
            f'{hrs} h',
            '<span style="color:var(--base)">☐</span>',
        ])
    page(f"""
      <h2>G3 · The 90-day checklist{' <span style="color:var(--muted);font-weight:400">· continued</span>' if i else ''}</h2>
      {'<div class="deck">The pilot in operating form. Print it, put a date against every gate as it closes, and do not tick a box you cannot evidence. Total scheduled: 458 hours of a 660-hour capacity across twelve weeks — the balance is reserve, and it will be consumed.</div>' if i == 0 else ''}
      {tbl(["Wk", "Goal", "Output", "Gate", "#Hrs", "Done"], rows,
           cls="tbl-compact", widths=["9mm", "46mm", "94mm", "84mm", "12mm", "10mm"])}
    """, label="G3 The 90-day checklist" + (" (continued)" if i else ""))

# --- G4 glossary
GLOSS = [
    ("Absorption", "Units sold in a period. With QTS, the measure of whether a market is actually clearing."),
    ("Age of inventory", "How long the current unsold stock has been unsold, in quarters. Mumbai: 13.5, improved from 14.3."),
    ("All-in cost", "Agreement value plus stamp duty, registration, TDS, brokerage and GST. Roughly 8% above the headline in Mumbai."),
    ("Area basis", "Carpet, built-up or saleable. The single most common source of misleading price comparisons in India."),
    ("Carpet area", "Net usable floor area within walls, as defined under RERA. The only basis on which to advise."),
    ("Channel partner", "Registered intermediary selling a developer's primary inventory, paid by the developer."),
    ("Co-broking", "Two brokers splitting a transaction and its commission. Requires written terms in advance."),
    ("Discount-to-close", "The gap between initial ask and registered price. Proprietary, and available nowhere publicly."),
    ("DPDP", "Digital Personal Data Protection Act 2023 and its 2025 Rules. Applies to a one-person business."),
    ("Gross yield", "Annual rent divided by capital value, before costs. Always shown separately from net."),
    ("IGR", "Inspector General of Registration, Maharashtra. Source of registered instruments and Ready Reckoner rates."),
    ("Index-II", "Registration extract summarising a registered instrument — parties, property, consideration, date."),
    ("MahaRERA", "Maharashtra Real Estate Regulatory Authority. Registers projects and agents; issues the Certificate of Competency."),
    ("Metro cess", "1% levy added to stamp duty in Mumbai, Navi Mumbai and Thane to fund metro rail."),
    ("MMR", "Mumbai Metropolitan Region — the city plus Thane, Navi Mumbai, Kalyan, Vasai-Virar and Panvel."),
    ("Net yield", "Gross yield after maintenance, vacancy, property tax and management. The only yield to show an investor."),
    ("Pocket (L4)", "Sub-locality — the primary research unit in this system. Roughly 5–30 buildings."),
    ("QPR", "Quarterly progress report filed by a promoter with MahaRERA. The check on advertised possession dates."),
    ("QTS", "Quarters-to-sell: unsold inventory divided by quarterly absorption. Mumbai H1 2026: 6.5."),
    ("Qualified lead", "Passes all four of budget, timeline, decision authority and area fit. Not a synonym for enquiry."),
    ("Ready Reckoner", "Government-published minimum valuation, the floor for stamp duty. Frozen for FY2026-27."),
    ("Referral coefficient", "New qualified referrals per closed client. Above 0.5, acquisition cost falls."),
    ("Sinking fund", "Society reserve for major repairs. A large pending levy materially changes affordability."),
    ("Stale_after_days", "Per-domain rule for when a fact must be re-verified before it may be shown to a client."),
    ("TDS 194-IA", "1% deducted by the buyer on consideration of ₹50 lakh or more; Form 26QB within 30 days of month end."),
    ("TDS 194H", "2% deducted from commission and brokerage above ₹20,000 in a financial year."),
]
page(f"""
  <h2>G4 · Glossary</h2>
  <div class="deck">Twenty-six terms used precisely throughout this document. Where a term has a loose market
  usage and a technical one, the technical one is intended.</div>
  <div class="cols3">
  {"".join(f'<p style="margin-bottom:2.4mm"><strong>{t}</strong><br><span class="small">{d}</span></p>' for t, d in GLOSS)}
  </div>
""", label="G4 Glossary")

# --- G5 Monday morning
page(f"""
  <h2>G5 · What to do on Monday morning</h2>
  <div class="deck">Sixty pages compress to eleven actions in the first week. Nothing here requires capital,
  permission or a decision you have not already made by reading this far.</div>
  <div class="grid2">
    <div>
      <div class="callout crit">
        <div class="h">Do these first — they start clocks you cannot compress</div>
        <ol class="small" style="margin:0 0 0 4mm">
          <li><strong>Book the 20-hour Certificate of Competency programme</strong> with NAREDCO, REMI or RAGC.
          Today. It is the longest-lead item in the venture and everything commercial waits on it
          <span class="src">[SRC-002]</span>.</li>
          <li><strong>Start the MahaRERA agent registration application.</strong> ₹10,000 for an individual
          <span class="src">[SRC-003]</span>.</li>
          <li><strong>Engage a CA</strong> and settle entity structure, GST position and the bookkeeping method
          before any money moves <span class="src">[SRC-031]</span>.</li>
        </ol>
      </div>
      <div class="callout">
        <div class="h">Then, in the same week</div>
        <ol class="small" start="4" style="margin:0 0 0 4mm">
          <li><strong>Freeze the corridor in writing.</strong> Six localities, 20–30 named pockets, dated and
          signed by yourself. The written freeze is what stops the scope creep that kills this plan.</li>
          <li><strong>Create the schema.</strong> geo_id, price_type, area_basis, sample_size, observed_date,
          source_ref, confidence, stale_after_days, conflict_flag. All mandatory from record one.</li>
          <li><strong>Open the source registry</strong> and add a row before you use any source, not after.</li>
          <li><strong>Write the DPDP notice and consent text</strong> before the first client conversation, not
          after the first fifty <span class="src">[SRC-023]</span>.</li>
        </ol>
      </div>
    </div>
    <div>
      <div class="callout good">
        <div class="h">Before the end of month one</div>
        <ol class="small" start="8" style="margin:0 0 0 4mm">
          <li><strong>Pull the MahaRERA extract</strong> for every project in the pocket set. Promoter, RERA id,
          status, QPR, possession date. Flag anything unregistered explicitly
          <span class="src">[SRC-016]</span>.</li>
          <li><strong>Run the first IGR e-Search sweep</strong> and build the registered-price baseline. It is
          free, it covers Mumbai from 1985, and almost nobody competing with you does it systematically
          <span class="src">[SRC-015]</span>.</li>
          <li><strong>Walk five pockets.</strong> Not drive — walk. Note noise, access, waterlogging marks,
          walkability to transit and view obstruction. Write it up the same day.</li>
          <li><strong>Do the capital conversation honestly.</strong> {rs(CAPITAL)}, twelve months, drawings at
          ₹60,000. If that is not available, reduce the drawings or delay the start — do not start underfunded
          and hope.</li>
        </ol>
      </div>
      <hr class="rule">
      <div class="q">Know a small geography better than the market, transact inside it, capture every observation
      and closure as structured evidence, and expand only when the economics repeat without you in every step.</div>
      <p class="tiny">Version {E.REPORT_VERSION} · researched to 14 August 2026 · 33 figures and 20 data files generated from a
      single evidence file, so no two artefacts in this pack can disagree with each other. Regenerate with
      <code>make all</code> when the underlying facts move — and they will.</p>
    </div>
  </div>
""", label="G5 What to do on Monday morning")


# ================================================================== ASSEMBLE
GROUP_TITLES = {
    "Front matter": "Front matter", "A · The market": "A · The market",
    "B · The business": "B · The business", "C · The work": "C · The work",
    "D · Economics": "D · Economics", "E · The system": "E · The system",
    "F · Playbooks": "F · Playbooks", "G · Appendices": "G · Appendices",
}


def build_toc():
    """Contents page, generated from the real page numbers."""
    groups, order = {}, []
    for n, p in enumerate(PAGES, 1):
        if p["label"] is None:
            continue
        g = p["group"]
        if g.startswith("__DIV__"):
            g = p["section"]
        if g not in groups:
            groups[g] = []
            order.append(g)
        groups[g].append((p["label"], n))
    blocks = ""
    for g in order:
        rows = "".join(
            f'<div class="row"><span>{H.escape(lab)}</span><span>{num}</span></div>'
            for lab, num in groups[g])
        blocks += f'<div class="grp"><h4>{H.escape(GROUP_TITLES.get(g, g))}</h4>{rows}</div>'

    nfig = sum(1 for p in PAGES if "figwrap" in str(p["body"]))
    return f"""
      <h2>Contents</h2>
      <div class="deck">{len(PAGES)} pages, {nfig} figures, 20 machine-readable data files. Every figure and every
      table is generated from a single evidence file, so no two artefacts in this pack can disagree with each
      other.</div>
      <div class="tocgrid">{blocks}</div>
      <div class="grid4" style="margin-top:5mm">
        <div class="box">
          <h4>How to read a number</h4>
          <p class="tiny" style="margin:0">Every fact carries a source tag —
          <span class="src">[SRC-004]</span> — resolving to the registry in appendix G1. Every figure states its
          confidence in the footnote. Analyst constructs are labelled
          <span class="badge b-model">model</span> and must never be quoted as market data.</p>
        </div>
        <div class="box o">
          <h4>Confidence grades</h4>
          <p class="tiny" style="margin:0"><span class="badge b-high">high</span> primary, statutory or published
          consultancy figure. <span class="badge b-med">medium</span> reputable secondary reporting.
          <span class="badge b-low">low</span> portal or asking aggregate — directional only.
          <span class="badge b-model">model</span> analyst judgement.</p>
        </div>
        <div class="box a">
          <h4>New in version 2</h4>
          <p class="tiny" style="margin:0">Fourteen substantive corrections, all H1 and July 2026 data
          re-verified, the Certificate of Competency and DPDP obligations added, the entry model rebuilt with
          sensitivity testing, and full workload, funnel and capital models.</p>
        </div>
        <div class="box v">
          <h4>What this is not</h4>
          <p class="tiny" style="margin:0">Not legal, tax or investment advice. Confirm every regulatory position
          with a qualified professional, and re-verify every market number against its source — all of them
          move.</p>
        </div>
      </div>
    """


def render():
    for p in PAGES:
        if p["body"] is TOC_PLACEHOLDER:
            p["body"] = build_toc()
    out = ['<!doctype html><html><head><meta charset="utf-8">',
           f"<title>Mumbai Real Estate Master Playbook v{E.REPORT_VERSION}</title>",
           f"<style>{CSS}</style></head><body>"]
    for n, p in enumerate(PAGES, 1):
        plain = p["cls"] == "cover"
        divider = p["cls"] == "divider"
        head = ""
        if not plain and not divider:
            head = (f'<div class="runhead"><span class="sec">{H.escape(p["section"])}</span>'
                    f'<span>Mumbai Real Estate · Entry, Intelligence &amp; Execution System</span></div>')
        foot = "" if plain else (
            f'<div class="runfoot"><span>Version {E.REPORT_VERSION} · research date 14 August 2026 · '
            f'not legal, tax or investment advice</span>'
            f'<span class="pageno">{n}</span></div>')
        out.append(f'<div class="page {p["cls"]}">{head}{p["body"]}{foot}</div>')
    out.append("</body></html>")
    return "\n".join(out)


if __name__ == "__main__":
    html = render()
    with open("../report/report.html", "w", encoding="utf-8") as f:
        f.write(html)
    nfig = sum(1 for p in PAGES if "figwrap" in str(p["body"]))
    print(f"report.html written · {len(PAGES)} pages · {nfig} figure pages · {len(html)/1024:.0f} KB")
