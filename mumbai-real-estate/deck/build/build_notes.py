"""build_notes.py — the presenter's brief: what to say on each of the 12 slides.

One page per slide. Each page carries the job the slide has to do, a spoken
script written to be said rather than read, the single number to land, the two
questions most likely to come back, and the thing not to say.

The scripts are deliberately short sentences. Long sentences collapse when
spoken under pressure. Every figure is read from evidence.py, so the brief
cannot quote a number the deck does not.
"""

import sys, os
sys.path.insert(0, os.path.abspath("../../build"))
import evidence as E

L, CR = 100_000, 10_000_000
RATE_L = E.BLENDED_RATE_LABEL

# ---------------------------------------------------------------------------
# n, title, seconds, headline on the slide, the job, script paragraphs,
# (big number, its caption), [(question, answer), ...], never-say
# ---------------------------------------------------------------------------
SLIDES = [
(1, "Opening", 55,
 "Mumbai has no shortage of property data. It has a shortage of decision-grade advice.",
 "Establish that the market is real, liquid and badly served — in that order.",
 ["Mumbai registers about thirteen thousand property transactions a month.",
  "In the first half of this year: eighty thousand registrations. Six thousand nine "
  "hundred crore in stamp duty. The best half-year since 2013.",
  "Every one of those is a public document. Dated. Free to look up.",
  "At the same time — one lakh fifty-seven thousand unsold flats. The largest pile in "
  "India. Six and a half quarters to clear it.",
  "So the market is busy and oversupplied at the same time. That is exactly when advice "
  "is worth paying for.",
  "And there are forty-two thousand registered agents in Maharashtra. Almost none of "
  "them work from that record.",
  "Mumbai does not have a data problem. It has an advice problem."],
 ("42,865", "registered agents — almost none using the registered record"),
 [("Isn't an oversupplied market bad news for a broker?",
   "The opposite. In a market that clears in two quarters, anything sells and advice is "
   "worthless. At six and a half quarters, choosing correctly is the entire job."),
  ("Isn't all of this already on the portals?",
   "The asking price is. The registered price is not, and that is the number that "
   "settles a negotiation.")],
 "Do not say 'disrupt', 'platform' or 'tech-enabled'. You spend slide 3 killing that "
 "framing — do not hand it back on slide 1."),

(2, "The customer's problem", 60,
 "A ₹2.3 crore decision, made on an asking price and a brochure.",
 "Make the pain specific. Six real questions beat any amount of 'the market is opaque'.",
 ["Here is what actually happens.",
  "Someone is about to spend two point three crore. Six questions decide whether that is "
  "a good deal or a bad one.",
  "Is this asking price above or below what flats in this building actually registered for?",
  "Is that eleven-fifty square feet carpet, built-up or saleable? Get that wrong and your "
  "price per square foot is off by twenty to thirty percent.",
  "Has this builder ever delivered on time?",
  "Will the society clear my loan, my tenant, my renovation?",
  "What is the commute really like at nine on a Tuesday?",
  "And if I need to sell in three years — who buys this?",
  "A portal answers none of them.",
  "None of this is secret. All of it is public. It just never reaches the buyer before "
  "the cheque is written."],
 ("20–30%", "the error in ₹/sq ft from one wrong area basis"),
 [("Don't good brokers already do this?",
   "Some do it in their head. Almost none do it in writing, and none of them keep the "
   "record afterwards. That is the difference."),
  ("Which of the six matters most?",
   "The first one. Every other question changes the price by a few percent. The "
   "registered comparable changes whether you are overpaying at all.")],
 "Do not rush this slide. It is the only one where the investor pictures themselves as "
 "the customer. Ask the six questions slowly and let them land."),

(3, "What Brickrock is", 55,
 "One business. One revenue line. One by-product that compounds.",
 "Stop them mis-categorising you. Precision here buys credibility for everything after.",
 ["Let me be precise about what this is, because the temptation in this category is to "
  "oversell.",
  "Brickrock is a micro-market advisory and brokerage desk.",
  "I do the advisory work. Research, comparables, shortlists, diligence, site visits, "
  "negotiation. I am not paid for any of it.",
  "I am paid once — when the client transacts. One point three two percent, blended "
  "across resale, primary and rental.",
  "That is the only revenue line. No subscription. No retainer. No licence.",
  "What I keep is the record. Closed price against asking. Why offers failed. Society "
  "rules. The real commute.",
  "That costs nothing to capture, and it compounds.",
  "This is not a portal. Not a SaaS product. Not an AI platform. Not a technology "
  "company."],
 (RATE_L, "blended commission — the only revenue line"),
 [("Why not build the software and sell it to other brokers?",
   "Because the data has no value without the transactions that generate it, and every "
   "Indian real-estate data tool is competing on the same public sources. The commission "
   "is the business. The record is the moat."),
  ("So you're just a broker?",
   "Yes. A broker who does the work in writing and keeps the evidence. That is a smaller "
   "claim than most people in this category make, and it is one I can actually defend.")],
 "Never soften the 'what it is not' list to sound more ambitious. That list is why the "
 "rest of the deck is believed."),

(4, "How it works", 50,
 "Seven steps, one loop, and an evidence layer that is a working tool — not a product.",
 "Show this is an operating system you already know how to run, not an intention.",
 ["Seven steps. And the seventh feeds back into the first.",
  "Acquire. Qualify. Shortlist. Site visit. Negotiate. Transact. Capture.",
  "Capture is the step everyone skips. Closed price. Objections. The referral ask.",
  "Underneath sits the evidence layer.",
  "Registered prices from IGR, normalised to one area basis. The RERA project register, "
  "with each builder's real delivery record. A pocket file — society rules, timed "
  "commutes. Supply and rent. And my own deal record.",
  "Each one feeds specific steps in the loop.",
  "That layer is a spreadsheet and a CRM. It is never sold, never licensed, and never "
  "shown to anyone as a platform.",
  "It exists to win the mandate and hold the line in a negotiation. That is all."],
 ("7 → 1", "the loop closes; every deal makes the next shortlist better"),
 [("How is a spreadsheet a moat?",
   "The spreadsheet is not. What goes into it is — and the only way to fill it is to "
   "transact."),
  ("What happens when you have more work than one person can do?",
   "The loop is the training document. Step three and step five are the two that need "
   "judgement; the rest is process. That is what makes a second person hireable.")],
 "Do not walk all seven steps one by one — you will lose the room. Name them fast, then "
 "spend your time on capture and on the evidence layer."),

(5, "Where we start", 65,
 "Six localities on one spine, chosen by a model that survives being wrong.",
 "Prove the geography was chosen, not assumed. This is the slide that shows you think.",
 ["One corridor. Six localities. All on one spine.",
  "Mulund. Bhandup. Kanjurmarg. Powai. Vikhroli. Ghatkopar.",
  "The Eastern Express Highway and JVLR, with Metro Line 6 running through it.",
  "End to end inside an hour. For one person, travel time is the binding constraint — "
  "not market size.",
  "Entry runs from eighteen thousand a square foot in Bhandup to forty-two thousand in "
  "Powai. Gross yields two point six to three point eight.",
  "I chose it with seven weighted criteria, applied identically to every corridor in "
  "MMR. Eastern and Central scores eight point zero zero.",
  "Then I tested whether that survives being wrong. Five thousand randomised weightings, "
  "every weight moved fifty percent either way. It stays first ninety-nine percent of "
  "the time.",
  "Navi Mumbai and Western tie at seven point four eight. The model cannot separate "
  "them. So I say so, rather than invent a third decimal."],
 ("99%", "of 5,000 randomised weightings still rank it first"),
 [("Why not the Western suburbs? More transactions there.",
   "Western wins transaction depth outright with a ten — and still finishes fourth. It "
   "scores four on competitive whitespace. That four is what a new entrant actually "
   "experiences on their first day of calling."),
  ("Six localities is very narrow. Isn't that limiting?",
   "Deliberately. Twenty to thirty pockets is roughly what one person can know at flat "
   "level in a year. Knowing six localities properly beats knowing the city vaguely.")],
 "Do not say 'five localities'. It is six, and you name six. Getting your own corridor "
 "count wrong in the room undoes the whole slide."),

(6, "Customer–market fit", 55,
 "The buyer is already in the corridor — and 25% of closures pay 43% of the bills.",
 "Show you know who actually pays, and that you have read your own revenue mix.",
 ["The buyer is already living in this corridor.",
  "The upgrader moving from a 2BHK to a 3BHK. The first-time buyer priced into five "
  "hundred to a thousand square feet.",
  "That is not a guess. Eighty-one percent of Mumbai registrations are flats of a "
  "thousand square feet or less. And homes above one crore went from forty-nine to "
  "fifty-four percent of sales in a single year.",
  "Small and expensive at the same time. That is a selection problem.",
  "Now look at the mix.",
  "Primary is twenty-five percent of my closures — and forty-three percent of my "
  "commission. The developer pays two percent instead of one.",
  "Rental is fifteen percent of closures and four percent of revenue. It is not a "
  "revenue line. It is a lead nursery. Today's tenant is the buyer in eighteen months — "
  "and it pays the rent while I wait."],
 ("25% → 43%", "share of closures → share of commission, primary market"),
 [("If primary pays double, why not do only primary?",
   "Because primary is where the conflict of interest lives. Resale is where trust gets "
   "built, and the referrals come out of resale. Doing only primary turns me into a "
   "channel partner, which is the thing slide 7 says I am not."),
  ("Isn't rental a distraction?",
   "It is four percent of revenue and it covers fixed costs in month four, before the "
   "first resale closes. It buys time, and it fills the pipeline.")],
 "Do not present rental as a growth engine. Calling it a lead nursery is more honest and "
 "more persuasive."),

(7, "Competitive positioning", 55,
 "Everyone competes on inventory. Nobody competes on the decision.",
 "Pre-empt 'isn't this crowded?' before they ask it.",
 ["Two questions. How much of the market does someone show you. And how much of the "
  "decision do they carry.",
  "Portals show you everything and carry none of it. They are paid by the listing — so "
  "stale and duplicate inventory is income, not a defect.",
  "National brokerages have the primary inventory and the developer access. They are "
  "paid two to five percent by the developer. The buyer is never told which project pays "
  "best.",
  "Local brokers have real pocket knowledge — held in one person's head. No written "
  "record, no continuity. The knowledge dies with the deal.",
  "Brickrock sits deliberately narrow and high. Fewer properties. The decision carried.",
  "Same commission, earned the same way.",
  "What changes is that the recommendation comes with evidence — and a written reason "
  "for every property I rejected.",
  "My competition is not the portals. It is those forty-two thousand agents."],
 ("Narrow + high", "fewer properties shown, the whole decision carried"),
 [("What stops a large brokerage doing exactly this?",
   "Nothing, except their economics. They need volume, and their salespeople are paid on "
   "transactions closed, not on decisions improved. Writing down why you rejected a flat "
   "slows a volume business down."),
  ("Isn't 'the decision' just what every broker claims?",
   "Every broker claims it. Almost none put it in writing, and a written reason for "
   "rejection is checkable afterwards. That is the test.")],
 "Do not attack the portals. They are useful, and dismissing them makes you sound "
 "defensive. Say what they are good at first."),

(8, "The moat", 55,
 "It is not the software. It is the transaction record that only we will hold.",
 "Answer 'what is defensible here?' with something physical, not a slogan.",
 ["Advise. Transact. Capture. Sharpen. Back to advise.",
  "The loop costs nothing to run. It just requires doing the work.",
  "Here is what builds up.",
  "Closed prices — not asking prices — pocket by pocket, on one area basis.",
  "The reason eleven buyers walked away. No public source anywhere records a transaction "
  "that did not happen.",
  "The society file. Rules, real maintenance, parking reality. Collected building by "
  "building, on foot.",
  "And a referral base that picks up the phone.",
  "At month twelve that is fifteen closures and twenty-five pockets known at flat level. "
  "At year three it is a registered-price series for this corridor that nobody else "
  "built.",
  "Someone with ten times my capital still starts that curve at zero. Because it is "
  "generated by transacting. You cannot buy it, licence it or scrape it."],
 ("Year 3", "a price series for this corridor nobody else has built"),
 [("Couldn't someone just scrape the IGR records?",
   "Anyone can pull registered prices. Nobody can pull why a buyer walked away, or what "
   "the society actually said in its last resolution. That half is only produced by "
   "being in the room."),
  ("How big does this get before it matters?",
   "It matters from about deal twenty, which is month fifteen. Before that I am buying "
   "the data with my own time. That is the honest position.")],
 "Do not call it 'proprietary data' and stop there. Name the four things — closed "
 "prices, failed deals, the society file, the referral base. Specific beats grand."),

(9, "Business model and economics", 60,
 f"One revenue line at {RATE_L} blended — and almost no capital at risk.",
 "Prove you can count, and that you know which of your numbers are guesses.",
 ["Fifteen closures in the base case. Average deal two point three crore. One point "
  "three two percent blended.",
  "Forty-five point seven lakh gross commission in year one.",
  "Costs. Forty-nine thousand one-time — registration, certificate, entity, insurance. "
  "Thirty-five thousand a month to run the business. Sixty thousand a month drawings — "
  "the biggest line, and the fastest lever if runway gets tight.",
  "After cost and tax: thirty-two point six lakh.",
  "Conservative is seven closures — twenty-one lakh. Stretch is twenty-seven — "
  "eighty-two lakh.",
  "Two points of honesty. GST at eighteen percent is a tax I collect from the client. It "
  "is not my revenue. And TDS of two percent is withheld at source and credited back "
  "against income tax.",
  "And the conversion rates are assumptions. The ninety-day pilot exists to replace them "
  "with measured numbers."],
 ("₹45.7 L", "gross commission, base case · ₹32.6 L after cost and tax"),
 [("Is fifteen closures realistic for one person?",
   "It is a bit over one a month, out of nine hundred enquiries. The two numbers I am "
   "least sure of are qualified-lead rate and site-visit conversion — and those are the "
   "first two the pilot measures."),
  ("What if commission rates compress?",
   "A quarter-point off the blended rate takes about eight lakh off year one. It does "
   "not change the shape of the business, and it is the reason primary and rental are in "
   "the mix at all.")],
 "Volunteer the GST and TDS point before they raise it. Saying 'GST is not my revenue' "
 "unprompted is worth more than any slide on this deck."),

(10, "Go to market", 55,
 "The first hundred conversations come from work, not from spend.",
 "Show demand is solvable without a marketing budget you do not have.",
 ["Nine hundred enquiries. Two hundred and forty qualified. One hundred and ten site "
  "visits. Forty-five offers. Fifteen closures.",
  "Now the channels, ranked by what a competitor cannot buy.",
  "Referrals from closed clients: about three hundred rupees a qualified lead. But they "
  "take six to nine months to start.",
  "Content and pocket briefs: nine hundred. Three to six months.",
  "Society and RWA relationships: six hundred. Co-broking: twelve hundred.",
  "Portal listings: four thousand two hundred. Paid ads: six thousand eight hundred. "
  "Both immediate. Both buyable by anyone with a credit card.",
  "The cheap, defensible channels are the slow ones.",
  "That is exactly why the first ninety days go into building them instead of buying "
  "leads.",
  "And content is where the capability already exists. Four hundred and eighty thousand "
  "organic views on property explainers. Zero spend."],
 ("₹300 vs ₹6,800", "cost per qualified lead — referral against paid advertising"),
 [("So no leads for six months?",
   "No. Co-broking and society relationships produce inside four to eight weeks. The "
   "referral engine is what compounds after that, and it is why year two costs less to "
   "run than year one."),
  ("Why not just buy leads to get started?",
   "I will, selectively. But a business built on bought leads has no cost advantage in "
   "year three, and I would rather spend the ninety days on the channels that do.")],
 "The 480k views is the strongest founder proof on this slide. Say it as evidence of "
 "distribution capability, not as a vanity number."),

(11, "Capital and the proof", 65,
 "₹11.3 lakh, twelve months, and a ninety-day test that replaces the assumptions.",
 "Make the ask small, specific and — most importantly — testable.",
 ["The number that sets the raise is not annual profit. It is the cash trough.",
  "Base case bottoms at minus six point two lakh in month six. Conservative — only seven "
  "deals close all year — bottoms at minus eight point one lakh in month eight.",
  "I am raising against the conservative case plus forty percent headroom. Eleven point "
  "three lakh. Twelve months of runway.",
  "Seven point two lakh of that is my own drawings. Three point one, field and "
  "marketing. One point one, compliance and tools. Forty-nine thousand, setup.",
  "Now the test.",
  "Weeks one to two: RERA registration filed, Certificate of Competency booked. It has "
  "been mandatory since January. Six weeks of critical path that no amount of effort "
  "compresses — so it is booked before the research starts, and the research happens "
  "while the clock runs.",
  "Weeks two to four: corridor frozen, project register built.",
  "Weeks four to six: price baseline, society files, timed commutes.",
  "Weeks six to twelve: certificate issues, marketing opens. Thirty-plus qualified "
  "leads. Five accompanied visit cycles.",
  "No advertising, no listing, no client work before that certificate.",
  "In ninety days we will both know whether this deck is real."],
 ("₹11.3 L", "the conservative trough, plus 40% headroom"),
 [("Why is your own drawing the largest line?",
   "Because it is, and pretending otherwise would be dishonest. It is also the fastest "
   "lever I have — cutting it extends runway by roughly a month per ten thousand."),
  ("What happens if the ninety days fails?",
   "Then eleven point three lakh bought that answer in ninety days instead of three "
   "years. The pilot is designed so failure is legible: if qualified-lead rate or "
   "site-visit conversion come in well below plan, the funnel does not work, and I will "
   "say so rather than raise again.")],
 "Do not apologise for the size of the ask. Small and testable is the point — it is the "
 "strongest structural feature of this business."),

(12, "Founder and the long arc", 75,
 "I have already built a business from zero. Brokerage in Mumbai is how I earn the right to build.",
 "Make them believe you specifically. Then show where this ends.",
 ["I have already built a business from zero.",
  "Sheesham dot in. My own business. A hundred percent bootstrapped — no outside money.",
  "FY twenty-five: fifty-one point eight lakh. FY twenty-six: one point zero eight "
  "crore. Up a hundred and eight percent.",
  "Seventeen point one lakh net profit at a sixteen percent margin. A hundred and "
  "eighty-three invoices. Return rate zero point five percent, against an industry "
  "standard of three.",
  "I am also already selling real estate. At brickrockrealty. A thousand followers, top "
  "reel three hundred and sixty-six thousand views, about four hundred and eighty "
  "thousand in total. Built by explaining — which is the same act this business sells.",
  "Now, separately, and I want to be exact about this.",
  "My family has been in Jaipur real estate for twenty-four years, as Chanda Properties. "
  "There is roughly three hundred and ten acres of family land. My father owns and is "
  "developing a hundred and twenty-four acres as a scheme.",
  "That is context and access. It is not my balance sheet, and I am not asking you to "
  "underwrite it.",
  "I am asking you to underwrite the track record on the left.",
  "And the arc. Brokerage. Then the transaction intelligence. Then network, capital and "
  "execution capability. Then development. Then building in Jaipur.",
  "Each stage funds the next and de-risks it.",
  "Nothing here needs a leap. Only that the stage before it actually worked."],
 ("₹1.08 Cr", "FY26 revenue, +108%, 100% bootstrapped — his own business"),
 [("Why Mumbai first? Why not just build in Jaipur?",
   "Because Mumbai has the deepest transaction volume, the strictest regulator and the "
   "most sophisticated buyers in India. Capability built here transfers down-market. The "
   "reverse is not true. And Jaipur will still be there — the family ecosystem is "
   "twenty-four years old and it is not going anywhere."),
  ("You sell furniture. Why do you think you can do this?",
   "Sheesham proves I can build demand, hold a margin and run a P&L with no capital. "
   "Those transfer. And I have not walked in cold — twenty-four years of family context, "
   "and I am already producing real-estate content that reaches half a million people.")],
 "The attribution line is the most important sentence on the deck. Say 'that is not my "
 "balance sheet' out loud. Volunteering it is what makes everything else credible — "
 "never let anyone leave the room thinking you own 310 acres."),
]

HARD = [
 ("“This is a job, not a business. Where is the scale?”",
  "Agree with them first. Year one is a job — deliberately, because it is the cheapest "
  "way to buy corridor knowledge and a transaction record. The business is stage two "
  "and three. Slide 11 says exactly what must be true before I widen: corridor-one "
  "economics repeat, closures happen without me at every step, referral coefficient "
  "above zero point five, and twelve months of runway still intact."),
 ("“₹32 lakh in year one is less than a good salary.”",
  "Correct — and it is on the slide rather than hidden. Year one is not the case. The "
  "case is that eleven point three lakh and twelve months buys a registered-price "
  "series, a broker network and a transaction record that a developer relationship is "
  "built on. A salary does not buy any of those."),
 ("“What if you cannot get the closures?”",
  "Then the ninety-day pilot tells us in ninety days, not three years. The two numbers "
  "that would show it are qualified-lead rate and site-visit conversion, and both are "
  "measured before any money is spent on marketing."),
 ("“What exactly am I funding, and what do I get?”",
  "Be straight. This is currently framed as twelve months of runway against a testable "
  "ninety-day plan, not as a priced equity round. If they want a return structure, say "
  "that is the next conversation and that you would rather agree it after the pilot has "
  "produced real numbers than before."),
 ("“Why should the family not just fund this?”",
  "Because the entire point of stage one is to fund the next stage from commission "
  "rather than from family. Taking family money to do brokerage skips the thing the "
  "stage is for."),
]

CSS = """
@page { size: 297mm 210mm; margin: 0; }
:root{
  --light:#FAFAF7; --card:#FFFFFF; --cardalt:#F2F1EC;
  --ink:#10131A; --ink2:#4C5361; --muted:#8C93A0; --hair:#E4E3DC; --rule:#CFCEC5;
  --orange:#E8722C; --orange-d:#B8511A; --blue:#2D6FCB; --green:#0E9E5E; --purple:#7B4FD6;
  --dark:#0F1621; --dark2:#18202D; --dink:#FFFFFF; --dink2:#A9B4C4; --dmuted:#6B7889;
  --dhair:#242E3D;
}
*{ box-sizing:border-box; }
html,body{ margin:0; padding:0; background:#fff; }
body{ font-family:"Inter","Liberation Sans",sans-serif; color:var(--ink);
      font-size:9pt; line-height:1.5;
      -webkit-print-color-adjust:exact; print-color-adjust:exact; }
.page{ position:relative; width:297mm; height:210mm; overflow:hidden;
       page-break-after:always; break-after:page;
       background:var(--light); padding:12mm 14mm 11mm 14mm; }
.page:last-child{ page-break-after:auto; }
.page.dark{ background:var(--dark); color:var(--dink); }
.kick{ font-size:7pt; font-weight:800; letter-spacing:.18em; text-transform:uppercase;
       color:var(--orange); margin-bottom:2.5mm; }
h1{ margin:0; font-size:15.5pt; line-height:1.2; letter-spacing:-.015em; font-weight:700;
    max-width:250mm; }
.dark h1{ color:var(--dink); }
.job{ margin:2.6mm 0 0 0; font-size:8.6pt; line-height:1.45; color:var(--ink2); }
.job b{ color:var(--orange-d); font-weight:800; letter-spacing:.08em;
        text-transform:uppercase; font-size:6.8pt; margin-right:2mm; }
.rule{ height:0.8pt; background:var(--rule); margin:4.5mm 0 4.5mm 0; }
.page:first-child .rule{ margin:3.4mm 0 3.4mm 0; }
.brand{ position:absolute; bottom:6mm; left:14mm; font-size:6.4pt; font-weight:700;
        letter-spacing:.16em; color:var(--muted); }
.dark .brand{ color:var(--dmuted); }
.pnum{ position:absolute; bottom:6mm; right:14mm; font-size:6.4pt; color:var(--muted); }
.dark .pnum{ color:var(--dmuted); }

.row{ display:flex; gap:9mm; }
.col{ flex:1; min-width:0; }
h4{ margin:0 0 2.4mm 0; font-size:6.8pt; font-weight:800; letter-spacing:.14em;
    text-transform:uppercase; color:var(--muted); }

/* the script */
.say p{ margin:0 0 3.1mm 0; font-size:10.2pt; line-height:1.52; color:var(--ink); }
.say p:first-child{ font-weight:600; }

/* right rail */
.big{ background:var(--card); border:0.8pt solid var(--hair); border-left:1.8mm solid var(--orange);
      border-radius:2.4mm; padding:4mm 4.5mm; margin-bottom:5mm; }
.big .v{ font-size:22pt; font-weight:700; line-height:1.05; letter-spacing:-.02em; }
.big .l{ font-size:7.4pt; color:var(--ink2); margin-top:1.8mm; line-height:1.4; }
.qa{ margin-bottom:4mm; }
.qa .q{ font-size:8pt; font-weight:700; color:var(--ink); line-height:1.4;
        margin-bottom:1.4mm; }
.qa .q:before{ content:"Q  "; color:var(--blue); font-weight:800; }
.qa .a{ font-size:7.6pt; line-height:1.5; color:var(--ink2); padding-left:4.4mm;
        border-left:0.8pt solid var(--hair); }
.trap{ background:#FCF3EC; border:0.8pt solid var(--orange); border-radius:2.4mm;
       padding:3.4mm 4mm; font-size:7.6pt; line-height:1.5; color:var(--ink2); }
.trap b{ display:block; font-size:6.6pt; font-weight:800; letter-spacing:.14em;
         text-transform:uppercase; color:var(--orange-d); margin-bottom:1.6mm; }

/* cover */
.lede{ font-size:10pt; line-height:1.45; color:var(--ink2); max-width:200mm;
       margin:3mm 0 0 0; }
.dark .lede{ color:var(--dink2); }
.card{ background:var(--card); border:0.8pt solid var(--hair); border-radius:2.4mm;
       padding:5mm 5.5mm; }
.dark .card{ background:var(--dark2); border-color:var(--dhair); }
.card h3{ margin:0 0 2.6mm 0; font-size:10pt; font-weight:700; }
.dark .card h3{ color:var(--dink); }
.card p{ margin:0 0 2.4mm 0; font-size:8.2pt; line-height:1.5; color:var(--ink2); }
.dark .card p{ color:var(--dink2); }
.quote{ font-size:11.5pt; line-height:1.35; font-weight:600; color:var(--ink);
        border-left:1.6mm solid var(--orange); padding-left:5mm; margin:0 0 4mm 0; }
.dark .quote{ color:var(--dink); }
table{ width:100%; border-collapse:collapse; }
td{ padding:1.05mm 2mm 1.05mm 0; font-size:8pt; line-height:1.45; color:var(--ink2);
    border-bottom:0.5pt solid var(--hair); vertical-align:top; }
.dark td{ color:var(--dink2); border-bottom-color:var(--dhair); }
td.n{ width:9mm; font-weight:800; color:var(--orange); }
td.t{ width:52mm; font-weight:700; color:var(--ink); }
.dark td.t{ color:var(--dink); }
td.s{ width:16mm; color:var(--muted); white-space:nowrap; }
.hq{ margin-bottom:5mm; }
.hq .q{ font-size:10pt; font-weight:700; color:var(--ink); margin-bottom:1.8mm; }
.hq .a{ font-size:8.4pt; line-height:1.55; color:var(--ink2); padding-left:5mm;
        border-left:1.2mm solid var(--blue); }
"""


def cover():
    total = sum(s[2] for s in SLIDES)
    rows = "".join(
        f'<tr><td class="n">{n:02d}</td><td class="t">{t}</td>'
        f'<td class="s">~{sec}s</td><td>{job}</td></tr>'
        for n, t, sec, _hl, job, *_ in SLIDES)
    return f"""
  <div class="kick">Presenter's brief · Brickrock Realty</div>
  <h1>What to say on each of the twelve slides</h1>
  <div class="lede">One page per slide. The script is written to be spoken, not read —
  short sentences, because long ones collapse under pressure. Say it in your own words;
  the job is to land the one number and the one idea on each page.</div>
  <div class="rule"></div>
  <div class="row">
    <div class="col" style="flex:1.35">
      <h4>The twelve slides &middot; {total//60} min {total%60} s of speaking</h4>
      <table>{rows}</table>
    </div>
    <div class="col">
      <h4>Open with this</h4>
      <div class="quote">&ldquo;Mumbai has no shortage of property data. It has a shortage
      of decision-grade advice. I am going to show you a business that sells the second
      thing.&rdquo;</div>
      <h4>Close with this</h4>
      <div class="quote">&ldquo;I am not asking you to believe a forecast. I am asking you
      to fund ninety days that will tell us both whether the forecast is real.&rdquo;</div>
      <div class="card">
        <h3>Three rules for the room</h3>
        <p><strong>1. Never upgrade the business.</strong> No &lsquo;platform&rsquo;, no
        &lsquo;AI&rsquo;, no &lsquo;tech-enabled&rsquo;. Slide 3 spends its whole life
        killing that framing — do not hand it back verbally.</p>
        <p><strong>2. Never claim the family land.</strong> If anyone says
        &lsquo;so you have 310 acres&rsquo;, the answer is: <em>my family does, I do not.
        That is context, not my balance sheet.</em></p>
        <p><strong>3. Volunteer the weak numbers.</strong> Say GST is not revenue. Say
        drawings are the biggest cost. Say which figures are assumptions. Every one of
        those buys credibility you cannot get any other way.</p>
      </div>
    </div>
  </div>

  <div class="rule"></div>
  <div class="row">
    <div class="col"><h4>If you have five minutes</h4>
      <div class="job">Slides <b style="color:var(--ink)">1 · 3 · 5 · 9 · 12</b>.
      The problem, what the business is, why this corridor, the economics, and you.</div></div>
    <div class="col"><h4>If you have fifteen</h4>
      <div class="job">All twelve, roughly a minute each. Do not over-run slide 4 —
      it is the easiest one to lose the room on.</div></div>
    <div class="col"><h4>If they want to go deep</h4>
      <div class="job">Hand them the 3-page diligence index. Every claim on every slide
      maps to a page in the 60-page playbook.</div></div>
  </div>
"""


def slide_page(n, title, sec, headline, job, script, big, qa, trap):
    paras = "".join(f"<p>{p}</p>" for p in script)
    qas = "".join(f'<div class="qa"><div class="q">{q}</div>'
                  f'<div class="a">{a}</div></div>' for q, a in qa)
    v, l = big
    return f"""
  <div class="kick">Slide {n:02d} &middot; {title} &middot; about {sec} seconds</div>
  <h1>&ldquo;{headline}&rdquo;</h1>
  <div class="job"><b>The job</b>{job}</div>
  <div class="rule"></div>
  <div class="row">
    <div class="col" style="flex:1.42">
      <h4>Say this</h4>
      <div class="say">{paras}</div>
    </div>
    <div class="col">
      <h4>Land this number</h4>
      <div class="big"><div class="v">{v}</div><div class="l">{l}</div></div>
      <h4>If they ask</h4>
      {qas}
      <div class="trap"><b>Watch out</b>{trap}</div>
    </div>
  </div>
"""


def hard_page():
    half = (len(HARD) + 1) // 2
    left = "".join(f'<div class="hq"><div class="q">{q}</div>'
                   f'<div class="a">{a}</div></div>' for q, a in HARD[:half])
    right = "".join(f'<div class="hq"><div class="q">{q}</div>'
                    f'<div class="a">{a}</div></div>' for q, a in HARD[half:])
    return f"""
  <div class="kick">Presenter's brief &middot; the five hardest questions</div>
  <h1>The questions that decide the meeting</h1>
  <div class="lede">None of these are unfair. Answer each one by agreeing with the part
  that is true first — that is what makes the rest of the answer land.</div>
  <div class="rule"></div>
  <div class="row">
    <div class="col">{left}</div>
    <div class="col">{right}
      <div class="trap" style="margin-top:1mm"><b>The one-line fallback</b>
      If a question goes somewhere you cannot answer, say so and say when you will know:
      &ldquo;I do not have that yet — it is one of the things the ninety days is designed
      to measure.&rdquo; That is a strong answer, not a weak one, because it is the same
      answer the deck gives.</div>
    </div>
  </div>
"""


def render():
    pages = [("", cover())]
    for n, title, sec, hl, job, script, big, qa, trap in SLIDES:
        pages.append(("", slide_page(n, title, sec, hl, job, script, big, qa, trap)))
    pages.append(("", hard_page()))
    out = ['<!doctype html><html><head><meta charset="utf-8">',
           "<title>Brickrock Realty · Presenter's brief</title>",
           f"<style>{CSS}</style></head><body>"]
    for i, (cls, body) in enumerate(pages, 1):
        out.append(f'<div class="page {cls}">{body}'
                   f'<div class="brand">BRICKROCK REALTY &middot; PRESENTER’S BRIEF</div>'
                   f'<div class="pnum">{i} / {len(pages)}</div></div>')
    out.append("</body></html>")
    return "\n".join(out)


if __name__ == "__main__":
    assert len(SLIDES) == 12, f"brief must cover exactly 12 slides, got {len(SLIDES)}"
    html = render()
    os.makedirs("../out", exist_ok=True)
    with open("../out/presenter_brief.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"presenter_brief.html written · {len(SLIDES) + 2} pages · {len(html)/1024:.0f} KB")
