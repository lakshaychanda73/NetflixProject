"""build_deck.py — assembles the exactly-12-slide Brickrock Realty pitch deck."""

import sys, os
sys.path.insert(0, os.path.abspath("../../build"))
from deck_css import CSS
import founder as F

SLIDES = []


def slide(body, cls="", foot=""):
    SLIDES.append((body, cls, foot))


def fig(name, cls=""):
    return f'<div class="fig {cls}"><img src="../figures/{name}"></div>'


def head(kick, title, lede=None):
    return (f'<div class="head"><div class="kick">{kick}</div><h2>{title}</h2>'
            + (f'<div class="lede">{lede}</div>' if lede else '') + '</div>')


# ══════════════════════════════════════════════════════════ 1 · THE OPPORTUNITY
slide(f"""
  <div class="head">
    <div class="kick">The opportunity</div>
    <h2 style="max-width:230mm">India's largest housing market clears 13,000&nbsp;transactions
    a month — and almost none of them are advised by anyone who has read the record.</h2>
  </div>

  <div class="grid4" style="margin-bottom:6mm">
    <div class="stat"><div class="v">₹6,968 cr</div>
      <div class="l">stamp duty in H1 2026, Mumbai city</div>
      <div class="d">best half-year since 2013</div></div>
    <div class="stat b"><div class="v">80,221</div>
      <div class="l">property registrations, H1 2026</div>
      <div class="d">+6% year on year</div></div>
    <div class="stat g"><div class="v">1,57,410</div>
      <div class="l">unsold units — the largest pool in India</div>
      <div class="d" style="color:var(--warn)">buyers need help choosing</div></div>
    <div class="stat p"><div class="v">6.5 qtrs</div>
      <div class="l">to clear current inventory</div>
      <div class="d" style="color:var(--dmuted)">selection beats speculation</div></div>
  </div>

  <div class="row" style="align-items:flex-start">
    <div class="col" style="flex:1.55">{fig("s1_registrations.png")}</div>
    <div class="col" style="flex:1; padding-top:2mm">
      <h4>Why this is an opening, not a crowd</h4>
      <ul class="tight">
        <li>Every registration is a <strong>dated, public, addressable</strong> instrument.
        IGR e-Search is free and covers Mumbai back to 1985.</li>
        <li class="b">42,865 registered agents in Maharashtra — almost none of them work
        from the registered record.</li>
        <li class="g">The market is busy <em>and</em> oversupplied. That is precisely the
        condition where advice is worth paying for.</li>
      </ul>
    </div>
  </div>
""", cls="dark",
     foot="Knight Frank India H1 2026 · Knight Frank/IGR registration releases · MahaRERA agent registry")


# ══════════════════════════════════════════════════════════ 2 · THE FOUNDER
b = F.BRICKROCK
slide(f"""
  {head("The founder",
        "I have already built a business from zero, and I already sell real estate.",
        "Not a first-time entrant with a thesis. An operator with a P&amp;L, an audience and "
        "twenty-four years of family context to draw on.")}

  <div class="row" style="align-items:flex-start">
    <div class="col" style="flex:1.15">
      {fig("s2_sheesham.png")}
      <div class="grid3" style="margin-top:1mm">
        <div class="stat"><div class="v" style="font-size:15pt">₹17.1 L</div>
          <div class="l">net profit, 16% margin</div></div>
        <div class="stat"><div class="v" style="font-size:15pt">₹58,807</div>
          <div class="l">average invoice value</div></div>
        <div class="stat"><div class="v" style="font-size:15pt">100%</div>
          <div class="l">bootstrapped, no outside capital</div></div>
      </div>
      <div class="attr"><span class="tag own">My own business</span>
        <span>Sheesham.in · Vaishali Nagar showroom, Jaipur</span></div>
    </div>

    <div class="col" style="flex:0.85">
      <div class="card" style="margin-bottom:4mm">
        <h3>Already operating in real estate</h3>
        <div class="grid3" style="gap:3mm; margin:3mm 0">
          <div><div style="font-size:14pt;font-weight:700">1,055</div>
               <div class="tiny">followers</div></div>
          <div><div style="font-size:14pt;font-weight:700;color:var(--orange)">366k</div>
               <div class="tiny">views, top reel</div></div>
          <div><div style="font-size:14pt;font-weight:700">≈480k</div>
               <div class="tiny">total reel views</div></div>
        </div>
        <div class="small" style="margin-top:1mm">
          <strong>@brickrockrealty</strong> — property walkthroughs and buyer education:
          <em>what is RERA</em>, <em>how to spot an overvalued property</em>,
          <em>the parking scam</em>, <em>why rent agreements run 11 months</em>.
        </div>
        <div class="attr"><span class="tag own">My own presence</span>
          <span>19 posts · audience built on explanation, not listings</span></div>
      </div>

      <div class="card tint">
        <h3>Twenty-four years of family context</h3>
        <ul class="tight" style="margin-top:2.5mm">
          <li class="b"><strong>Chanda Properties</strong> — family real-estate firm in Jaipur,
          trusted realtors since 2002.</li>
          <li class="b"><strong>~310 acres</strong> of family land inheritance.</li>
          <li class="b"><strong>124 acres</strong> owned by my father, currently being developed
          as a scheme/township.</li>
        </ul>
        <div class="attr"><span class="tag fam">Family context — not my assets</span>
          <span>Context and access. The track record above is mine.</span></div>
      </div>
    </div>
  </div>
""", foot="Sheesham.in incubation deck, July 2026 · @brickrockrealty profile, August 2026")


# ══════════════════════════════════════════════════════════ 3 · THE VISION
slide(f"""
  <div class="head">
    <div class="kick">The vision</div>
    <h2 style="max-width:240mm">I am not trying to become a broker.
    I am trying to become a builder — and brokerage in Mumbai is the fastest way to earn
    the capability, the network and the capital to do it.</h2>
  </div>
  {fig("s3_vision.png")}
""", cls="dark")


# ══════════════════════════════════════════════════════════ 4 · MMR OPPORTUNITY
slide(f"""
  {head("The opportunity, sized honestly",
        "A large market — but we do not need the whole market.",
        "Every strategy document that stops at the top bar is selling optimism. "
        "The only number that matters is the one at the bottom.")}
  <div class="row" style="align-items:center">
    <div class="col" style="flex:1.5">{fig("s4_funnel.png")}</div>
    <div class="col" style="flex:0.72">
      <div class="card" style="margin-bottom:4mm">
        <h4>The modal transaction</h4>
        <div style="font-size:16pt;font-weight:700;line-height:1.15;margin-bottom:2mm">
          500–1,000 sq ft<br>above ₹1 crore</div>
        <div class="small">81% of registrations are flats of 1,000 sq ft or less.
        Homes above ₹1 crore have risen from 49% to 54% of sales in a year.</div>
      </div>
      <div class="note">The market is small and expensive at the same time. That is a
      <strong>selection</strong> problem, and selection is what an evidence-led desk sells.</div>
    </div>
  </div>
""", foot="Knight Frank India H1 2026 · registration base from Knight Frank/IGR H1 2026 coverage")


# ══════════════════════════════════════════════════════════ 5 · WHERE WE START
slide(f"""
  {head("Where we start",
        "One corridor. Five localities. Twenty-five pockets. Frozen for ninety days.")}
  <div class="row" style="align-items:flex-start">
    <div class="col" style="flex:1.02">{fig("s5_map.png")}</div>
    <div class="col" style="flex:0.98; padding-top:1mm">
      <h3 style="color:var(--orange); font-size:13pt">Eastern &amp; Central Suburbs</h3>
      <div class="body" style="margin:2.5mm 0 4mm 0">
        Powai · Kanjurmarg · Vikhroli · Bhandup · Mulund · Ghatkopar
      </div>
      <ul>
        <li>One contiguous belt, reachable end to end inside an hour — the binding constraint
        for a single founder is travel time, not market size.</li>
        <li>An operating employment catchment: Mumbai added 6.0 mn sq ft of office absorption
        in H1 2026, with fresh completions concentrated in Powai, Thane and Navi Mumbai.</li>
        <li>A live metro alignment (Line 6, JVLR) plus the Eastern Express Highway spine.</li>
        <li>Advisory whitespace the Western suburbs no longer offer.</li>
      </ul>
      <div class="note" style="margin-top:4mm">Expansion is sequenced and conditional —
      Thane, then Navi Mumbai — and only once corridor-1 closures happen
      <strong>without me present at every step</strong>.</div>
    </div>
  </div>
""", foot="Schematic — relative position and adjacency are meaningful; distances and boundaries are not")


# ══════════════════════════════════════════════════════════ 6 · SEVEN METRICS
slide(f"""
  {head("Why this corridor",
        "Seven weighted metrics, one weight vector, applied to every corridor in MMR.")}
  <div class="row" style="align-items:center">
    <div class="col" style="flex:0.95">{fig("s6_metrics.png")}</div>
    <div class="col" style="flex:1.05; padding-top:2mm">
      <div class="grid2" style="gap:4mm">
        <div class="card"><h4 style="color:var(--orange)">Weighted toward execution</h4>
          <div class="small">A single founder cannot compensate for a weak axis by hiring a
          specialist. <strong>Execution simplicity</strong> and <strong>entry cost</strong>
          together carry 0.28 — as much as transaction depth and infrastructure combined.</div></div>
        <div class="card"><h4 style="color:var(--blue)">Infrastructure by status</h4>
          <div class="small">An operating asset scores 1.00; a commissioning one 0.75; a mere
          approval 0.25. Scoring an <strong>announced</strong> metro like a running one is the
          most common error in Indian micro-market research.</div></div>
        <div class="card"><h4 style="color:var(--green)">Entry cost, inverted</h4>
          <div class="small">Lower ticket means a faster first closure and less client risk.
          It is scored as a benefit, not a penalty.</div></div>
        <div class="card"><h4 style="color:var(--purple)">Whitespace, re-based</h4>
          <div class="small">Measured against the <strong>42,865 registered agents</strong> in
          Maharashtra — not against a feeling about how competitive a suburb is.</div></div>
      </div>
    </div>
  </div>
""", foot="Analyst model — weights encode one strategy: a single founder needing a first closure inside two quarters")


# ══════════════════════════════════════════════════════════ 7 · SCORECARD
slide(f"""
  {head("The scorecard",
        "Eastern &amp; Central wins by having no weak axis — not by leading any single one.")}
  {fig("s7_scorecard.png", cls="c104")}
  <div class="grid3" style="margin-top:3mm">
    <div class="note"><strong>The Western Suburbs win transaction depth outright with a 10 —
    and still finish fourth.</strong> A 4 on whitespace is what a new entrant actually
    experiences on their first day of calling.</div>
    <div class="note b"><strong>Navi Mumbai and Western tie at 7.48.</strong> The tie breaks
    toward Navi Mumbai on whitespace. Where the model cannot separate two options, saying so
    is more useful than inventing a third decimal.</div>
    <div class="note g"><strong>The recommendation survives being wrong.</strong> Across 5,000
    randomised weight vectors — every weight jittered ±50% — Eastern &amp; Central stays first
    99% of the time.</div>
  </div>
""")


# ══════════════════════════════════════════════════════════ 8 · OPERATING MODEL
slide(f"""
  {head("The operating model",
        "Seven steps, one loop. The loop is the whole business.")}
  {fig("s8_operating.png")}
  <div class="grid4" style="margin-top:2mm">
    <div><h4>Acquire</h4><div class="tiny">Referral network and pocket briefs first —
    the cheapest channels are the slowest to build and the hardest for anyone to buy.</div></div>
    <div><h4>Qualify</h4><div class="tiny">Budget, timeline, decision authority and area fit.
    All four, or it is an enquiry, not a lead.</div></div>
    <div><h4>Transact</h4><div class="tiny">Registered comparables normalised to carpet area.
    Evidence moves sellers who have anchored on a neighbour's 2023 number.</div></div>
    <div><h4>Capture</h4><div class="tiny">Closed price against asking, objections, society
    rules, real maintenance. No public source has this.</div></div>
  </div>
""")


# ══════════════════════════════════════════════════════════ 9 · THE ECONOMICS
slide(f"""
  {head("The economics",
        "2,860 founder hours → 15 closures → ₹45.7 L gross → ₹32.6 L post-tax.")}
  {fig("s9_economics.png")}
  <div class="row" style="margin-top:2mm; gap:6mm">
    <div class="col"><div class="note"><strong>₹1,140 per founder hour, post-tax.</strong>
    That is the honest comparator to a salary, and it is what Year 1 is actually worth.
    The case for doing it anyway is Years 2–6, not Year 1.</div></div>
    <div class="col"><div class="note b"><strong>₹11.3 lakh of capital, raised against the
    conservative case.</strong> The trough is month 6–8. Founder drawings are the largest line
    in the burn and the main lever on it.</div></div>
    <div class="col"><div class="note g"><strong>Almost no capital at risk.</strong> Brokerage
    converts knowledge into cash inside twelve months without inventory, land or debt —
    which is exactly why it funds the next stage.</div></div>
  </div>
""", foot="Planning model — conversion rates, segment mix and commission rates are assumptions the 90-day pilot exists to replace")


# ══════════════════════════════════════════════════════════ 10 · FIRST 90 DAYS
slide(f"""
  {head("First 90 days",
        "From zero to first repeatable transactions — with one hard gate in the middle.")}
  {fig("s10_90days.png")}
  <div class="row" style="margin-top:3mm; gap:6mm">
    <div class="col" style="flex:1.6">
      <div class="note"><strong>The Certificate of Competency became mandatory in January
      2026.</strong> A MahaRERA agent cannot register or renew without a 20-hour programme and
      an examination. It is a six-week critical path that no amount of effort compresses —
      so it is booked in week 1, before the market research, and the research happens while
      the clock runs.</div>
    </div>
    <div class="col">
      <div class="grid2" style="gap:4mm">
        <div class="stat" style="padding:3.5mm 4mm"><div class="v" style="font-size:14pt">30+</div>
          <div class="l">qualified leads by day 90</div></div>
        <div class="stat b" style="padding:3.5mm 4mm"><div class="v" style="font-size:14pt">5+</div>
          <div class="l">accompanied site-visit cycles</div></div>
      </div>
    </div>
  </div>
""", foot="MahaRERA agent registration and certification requirements · advertising disclosure order")


# ══════════════════════════════════════════════════════════ 11 · SCALE
slide(f"""
  {head("Months 3 to 12",
        "Build the Mumbai engine, then widen — but only on evidence.")}
  {fig("s11_scale.png", cls="c112")}
  <div class="row" style="margin-top:2mm; gap:6mm">
    <div class="col"><div class="note"><strong>Deepen before widening.</strong> If corridor-1
    conversion is weak, adding a second corridor does not fix it — it buys a second place to
    be mediocre and doubles the travel.</div></div>
    <div class="col"><div class="note b"><strong>The expansion gate at month 8:</strong>
    corridor-1 economics repeat, closures happen without me at every step, referral coefficient
    above 0.5, and twelve months of runway still intact.</div></div>
    <div class="col"><div class="note g"><strong>What exists at month 12 that money cannot
    buy:</strong> twenty-five pockets known at unit level, a registered-price series nobody
    else built, and a record of why eleven buyers walked away.</div></div>
  </div>
""")


# ══════════════════════════════════════════════════════════ 12 · THE END GAME
slide(f"""
  <div class="head">
    <div class="kick">The end game</div>
    <h2 style="max-width:250mm">Build in Mumbai. Learn. Compound.
    Develop. Then build in Jaipur.</h2>
  </div>
  {fig("s12_endgame.png", cls="c100")}
  <div class="grid4" style="margin-top:4mm">
    <div><h4 style="color:var(--orange)">Hardest market teaches fastest</h4>
      <div class="tiny">Capability built against Mumbai's volume, regulator and buyers
      transfers down-market. The reverse is not true.</div></div>
    <div><h4 style="color:var(--blue)">Capital without dilution</h4>
      <div class="tiny">Brokerage converts knowledge into cash with almost nothing at risk.
      Development needs capital — this is how it gets funded.</div></div>
    <div><h4 style="color:var(--green)">The network is the asset</h4>
      <div class="tiny">Developers, lenders, lawyers, brokers. The relationships that make a
      first project possible are made across a hundred transactions.</div></div>
    <div><h4 style="color:var(--purple)">Jaipur will still be there</h4>
      <div class="tiny">The family ecosystem is 24 years old and is not going anywhere.
      What is scarce is the capability to build.</div></div>
  </div>
""", cls="dark")


# ══════════════════════════════════════════════════════════════════ ASSEMBLE
def render():
    out = ['<!doctype html><html><head><meta charset="utf-8">',
           "<title>Brickrock Realty · Mumbai Real Estate</title>",
           f"<style>{CSS}</style></head><body>"]
    for n, (body, cls, foot) in enumerate(SLIDES, 1):
        out.append(
            f'<div class="slide {cls}">'
            f'<div class="num">{n:02d} / 12</div>'
            f'{body}'
            f'<div class="brand">BRICKROCK REALTY</div>'
            + (f'<div class="foot">{foot}</div>' if foot else '')
            + '</div>')
    out.append("</body></html>")
    return "\n".join(out)


if __name__ == "__main__":
    assert len(SLIDES) == 12, f"deck must be exactly 12 slides, got {len(SLIDES)}"
    html = render()
    os.makedirs("../out", exist_ok=True)
    with open("../out/deck.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"deck.html written · {len(SLIDES)} slides · {len(html)/1024:.0f} KB")
