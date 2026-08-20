"""build_deck.py — assembles the exactly-12-slide Brickrock Realty pitch deck.

Rebuilt from the 60-page master playbook, not from the earlier deck.

The rule this deck is written under: do not exaggerate what Brickrock is today.
It is a micro-market real-estate advisory and brokerage business. Revenue is
brokerage and advisory commission. The intelligence system exists to win the
mandate, sharpen the shortlist and hold the line in a negotiation — and, as a
by-product, to capture transaction evidence that compounds. It is not a portal,
not data SaaS, not an AI platform and not a technology company.
"""

import sys, os
sys.path.insert(0, os.path.abspath("../../build"))
from deck_css import CSS
import evidence as E
import founder as F
import images as IM

# Photographs are optional. Every slot that is filled is placed; every slot that
# is empty falls back to the typography-led layout, so the deck always builds.
IM.place_all()

L, CR = 100_000, 10_000_000
RATE_L = E.BLENDED_RATE_LABEL
CONSID = E.BLENDED_CONSIDERATION

SLIDES = []


def slide(body, cls="", foot=""):
    SLIDES.append((body, cls, foot))


def fig(name, cls=""):
    return f'<div class="fig {cls}"><img src="../figures/{name}"></div>'


def photo(slot, cls, caption=None, sub=None):
    """A photo panel, or an empty string when the slot has no file in ../images/."""
    if not IM.have(slot):
        return ""
    cap = ""
    if caption:
        cap = (f'<div class="cap">{caption}'
               + (f' <em>{sub}</em>' if sub else '') + '</div>')
    return (f'<div class="photo {cls}">'
            f'<img src="../figures/{IM.placed(slot)}">{cap}</div>')


def head(kick, title, lede=None):
    return (f'<div class="head"><div class="kick">{kick}</div><h2>{title}</h2>'
            + (f'<div class="lede">{lede}</div>' if lede else '') + '</div>')


# ══════════════════════════════════════════════════════ 1 · THE OPENING
slide(f"""
  <div class="head" style="margin-bottom:5mm">
    <div class="kick">Brickrock Realty · Mumbai</div>
    <h2 style="max-width:250mm">Mumbai has no shortage of property data.
    It has a shortage of decision-grade advice.</h2>
  </div>

  <div class="grid4" style="margin-bottom:5mm">
    <div class="stat"><div class="v">80,221</div>
      <div class="l">property registrations, H1 2026</div>
      <div class="d">+6% YoY · best half-year since 2013</div></div>
    <div class="stat b"><div class="v">₹6,968 cr</div>
      <div class="l">stamp duty collected in the same half</div>
      <div class="d" style="color:var(--dmuted)">every one a dated public instrument</div></div>
    <div class="stat g"><div class="v">1,57,410</div>
      <div class="l">unsold units — the largest pool in India</div>
      <div class="d" style="color:var(--warn)">6.5 quarters to clear at current velocity</div></div>
    <div class="stat p"><div class="v">42,865</div>
      <div class="l">registered agents in Maharashtra</div>
      <div class="d" style="color:var(--dmuted)">almost none work from the registered record</div></div>
  </div>

  {photo("s1_corridor", "wide", "The Eastern &amp; Central corridor",
         "&middot; Powai, where the pilot starts")}

  <div class="row" style="align-items:flex-start">
    <div class="col" style="flex:1.5">{fig("s1_pulse.png", "c62" if IM.have("s1_corridor") else "")}</div>
    <div class="col" style="flex:1; padding-top:1mm">
      <h4>What Brickrock is</h4>
      <div class="body" style="margin-bottom:3mm">
        A <strong>micro-market advisory and brokerage desk</strong> working one Mumbai
        corridor at pocket level. We are paid a commission when a client transacts.
      </div>
      <ul class="tight">
        <li>The market is busy <em>and</em> oversupplied at the same time. That is
        precisely the condition in which advice is worth paying for.</li>
        <li class="b">Every registration is public, dated and addressable. IGR e-Search
        is free and covers Mumbai back to 1985.</li>
        <li class="g">The gap is not access to data. It is the work of turning it into
        a recommendation someone can act on.</li>
      </ul>
    </div>
  </div>
""", cls="dark",
     foot="Knight Frank India H1 2026 · Knight Frank/IGR registration releases · MahaRERA agent registry")


# ══════════════════════════════════════════════════════ 2 · THE CUSTOMER'S PROBLEM
slide(f"""
  {head("The customer's problem",
        "A ₹2.3 crore decision, made on an asking price and a brochure.")}
  {fig("s2_problem.png")}
  <div class="grid3" style="margin-top:1mm">
    <div class="note"><strong>The mistake stays invisible for years.</strong> A bad pocket
    or a wrong area basis only surfaces at resale.</div>
    <div class="note b"><strong>Nobody is paid to prevent it.</strong> Portals are paid per
    listing, channel partners per project, developers per unit.</div>
    <div class="note g"><strong>This is what we sell.</strong> Not access to inventory — a
    defensible answer to those six questions, in writing.</div>
  </div>
""", foot="Question set drawn from the diligence and negotiation protocols in the master playbook, Parts C and G")


# ══════════════════════════════════════════════════════ 3 · WHAT BRICKROCK IS
slide(f"""
  {head("What Brickrock is",
        "One business. One revenue line. One by-product that compounds.")}
  {fig("s3_definition.png")}
  <div class="row" style="margin-top:3mm; gap:8mm">
    <div class="col">
      <h4 style="color:var(--green)">What it is</h4>
      <div class="small">A micro-market real-estate <strong>advisory and brokerage</strong>
      business, run by one founder in one corridor, earning <strong>{RATE_L} blended
      commission</strong> on resale, primary and rental transactions.</div>
    </div>
    <div class="col">
      <h4 style="color:var(--muted)">What it is not</h4>
      <div class="small" style="color:var(--muted)">Not a property portal. Not a data or
      SaaS product. Not an AI platform. Not a technology company. Not a large brokerage.
      Nothing here is sold by subscription or licensed to anyone.</div>
    </div>
    <div class="col">
      <h4 style="color:var(--orange)">Why the record matters anyway</h4>
      <div class="small">Because it is the only asset in this business that a
      better-funded competitor cannot simply buy. It is generated by transacting,
      and there is no other way to get it.</div>
    </div>
  </div>
""")


# ══════════════════════════════════════════════════════ 4 · HOW IT WORKS
slide(f"""
  {head("How it works",
        "Seven steps, one loop, and an evidence layer that is a working tool — not a product.")}
  {fig("s4_system.png")}
""", foot="Operating model and evidence schema from the master playbook, Parts B and C")


# ══════════════════════════════════════════════════════ 5 · WHY EASTERN & CENTRAL
slide(f"""
  {head("Where we start",
        "Six localities on one spine, chosen by a model that survives being wrong.")}
  <div class="row" style="gap:6mm; align-items:stretch">
    <div class="col" style="flex:1">{fig("s5_corridor.png")}</div>
    {'<div class="col" style="flex:0 0 44mm">' + photo("s5_corridor", "rail",
       "Powai", "&middot; the head of the spine") + '</div>' if IM.have("s5_corridor") else ''}
  </div>
""", foot="Micro-market asking bands and rents: portal-derived, medium confidence · entry model: analyst")


# ══════════════════════════════════════════════════════ 6 · CUSTOMER–MARKET FIT
slide(f"""
  {head("Customer–market fit",
        "The buyer is already in the corridor — and 25% of closures pay 43% of the bills.")}
  {fig("s6_customer.png")}
""", foot=f"81% of Mumbai registrations are flats of 1,000 sq ft or less; homes above ₹1 crore have gone from 49% to 54% of sales in a year")


# ══════════════════════════════════════════════════════ 7 · COMPETITIVE POSITIONING
slide(f"""
  {head("Competitive positioning",
        "Everyone competes on inventory. Nobody competes on the decision.")}
  {fig("s7_positioning.png")}
""")


# ══════════════════════════════════════════════════════ 8 · THE MOAT
slide(f"""
  {head("The moat",
        "It is not the software. It is the transaction record that only we will hold.")}
  {fig("s8_moat.png")}
  <div class="grid4" style="margin-top:2mm">
    <div><h4 style="color:var(--orange)">Closed prices, not asking prices</h4>
      <div class="tiny">What a flat actually registered for, normalised to one area
      basis, pocket by pocket. Portals hold the asking price and nothing else.</div></div>
    <div><h4 style="color:var(--blue)">Why deals failed</h4>
      <div class="tiny">Eleven buyers who walked away and the reason each one gave.
      No public source records a transaction that did not happen.</div></div>
    <div><h4 style="color:var(--green)">The society file</h4>
      <div class="tiny">Rules, resolutions, real maintenance, parking reality, tenant
      restrictions. Collected building by building, on foot.</div></div>
    <div><h4 style="color:var(--purple)">A referral base that answers</h4>
      <div class="tiny">People who transacted through us once and pick up the phone.
      That is earned across a hundred deals, not bought in a round.</div></div>
  </div>
""")


# ══════════════════════════════════════════════════════ 9 · BUSINESS MODEL & ECONOMICS
slide(f"""
  {head("Business model and economics",
        f"One revenue line at {RATE_L} blended — and almost no capital at risk.")}
  {fig("s9_economics.png")}
""", foot="Planning model — conversion rates, segment mix and commission rates are assumptions the 90-day pilot exists to replace")


# ══════════════════════════════════════════════════════ 10 · GO TO MARKET
slide(f"""
  {head("Go to market",
        "The first hundred conversations come from work, not from spend.")}
  {fig("s10_gtm.png")}
""")


# ══════════════════════════════════════════════════════ 11 · CAPITAL & 90-DAY PROOF
slide(f"""
  {head("Capital and the proof",
        f"₹{E.CAPITAL/L:,.1f} lakh, twelve months, and a ninety-day test that replaces the assumptions in this deck.")}
  {fig("s11_capital.png")}
""", foot="MahaRERA agent registration, Certificate of Competency (mandatory from January 2026) and advertising-disclosure requirements")


# ══════════════════════════════════════════════════════ 12 · FOUNDER & THE LONG ARC
b = F.BRICKROCK
slide(f"""
  <div class="head" style="margin-bottom:5mm">
    <div class="kick">The founder, and where this goes</div>
    <h2 style="max-width:252mm">I have already built a business from zero.
    Brokerage in Mumbai is how I earn the right to build.</h2>
  </div>

  <div class="row" style="align-items:flex-start; margin-bottom:4mm">
    {'<div class="col" style="flex:0 0 38mm">' + photo("s12_founder", "port")
     + ('<div style="height:4mm"></div>' + photo("s12_jaipur", "port", "Jaipur",
        "&middot; where the arc ends") if IM.have("s12_jaipur") else '')
     + '</div>' if IM.have("s12_founder") or IM.have("s12_jaipur") else ''}
    <div class="col" style="flex:1.16">
      {fig("s12_founder.png")}
      <div class="attr"><span class="tag own">My own business</span>
        <span>₹17.1 L net profit · ₹58,807 average invoice · 183 invoices</span></div>
    </div>

    <div class="col" style="flex:0.94">
      <div class="card">
        <h3>Already operating in real estate</h3>
        <div class="grid3" style="gap:3mm; margin:3mm 0">
          <div><div style="font-size:14pt;font-weight:700">{b["followers"]:,}</div>
               <div class="tiny">followers</div></div>
          <div><div style="font-size:14pt;font-weight:700;color:var(--orange)">366k</div>
               <div class="tiny">views, top reel</div></div>
          <div><div style="font-size:14pt;font-weight:700">≈480k</div>
               <div class="tiny">total reel views</div></div>
        </div>
        <div class="small"><strong>@brickrockrealty</strong> — buyer education and property
        walkthroughs: <em>what is RERA</em>, <em>spotting an overvalued property</em>,
        <em>the parking scam</em>. An audience built by explaining, which is the same act
        the business sells.</div>
        <div class="attr"><span class="tag own">My own presence</span>
          <span>19 posts · distribution capability that already exists</span></div>
      </div>
    </div>

    <div class="col" style="flex:0.94">
      <div class="card tint">
        <h3>Twenty-four years of family context</h3>
        <ul class="tight" style="margin-top:2.5mm">
          <li class="b"><strong>Chanda Properties</strong> — the family real-estate firm
          in Jaipur, trusted realtors since 2002.</li>
          <li class="b"><strong>~310 acres</strong> of family land inheritance.</li>
          <li class="b"><strong>124 acres</strong> owned by my father and being developed
          by him as a scheme.</li>
        </ul>
        <div class="attr"><span class="tag fam">Family context — not my assets</span>
          <span>Context and access — not a balance sheet I own.</span></div>
      </div>
    </div>
  </div>

  {fig("s12_arc.png")}
""", cls="dark",
     foot="Sheesham.in incubation deck, July 2026 · @brickrockrealty profile, August 2026")


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
