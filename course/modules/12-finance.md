# Module 12 — Real Estate Finance

> **📌 Beyond the MATP syllabus.** Not examinable. This is the module that lets you understand what
> the person across the table is actually optimising for.
> **Time:** 5–6 hours. Build the model — don't just read it.

---

## 1. What I need to learn

How a developer makes money, where the risk sits, and why they behave the way they do — why they
launch before they're ready, why they discount at quarter-end, why they resist changing a payment
plan, why "the numbers don't work."

**Once you understand a developer's cash flow, their negotiating behaviour stops being mysterious.**

---

## 2. Developer economics — the basic equation

```
GDV (Gross Development Value)  =  Saleable area × Average realisation
Total Project Cost             =  Land + Construction + Approvals/Premiums
                                  + Marketing/Brokerage + Finance + Overheads
Development Profit             =  GDV − Total Project Cost
Development Margin             =  Profit ÷ GDV
Return on Cost                 =  Profit ÷ Total Project Cost
```

**The residual land value method** — how a developer decides what land is worth:
```
Residual Land Value = GDV − (all costs except land) − required developer profit
```
This is why land prices in a micro-market track achievable sale prices with a lag. **Land is the
residual, not the driver.**

### 2.1 The cost stack in Mumbai 💼

| Component | Typical share | Notes |
|---|---|---|
| **Land / rehab obligation** | 30–50% | In redevelopment, "land cost" is the rehab component + corpus + rent |
| **Construction** | 25–40% | Mumbai high-rise construction commonly ₹3,000–5,000/sq ft ⏱ |
| **Approvals & premiums** | 8–15% | Premium FSI, TDR, development charges, fungible FSI premiums |
| **Marketing & brokerage** | 3–6% | Your commission lives here |
| **Finance** | 6–12% | Construction finance; NBFC rates run well above bank rates |
| **Overheads & contingency** | 2–5% | |

> 🔴 **The insight that changes how you negotiate:** land and approvals are **sunk and fixed**.
> They are spent before a single flat is sold. Everything after launch is a race to convert
> inventory into cash fast enough to service finance. **That is why developers would rather give
> you a bigger brokerage than cut the headline price** — the headline price sets the benchmark for
> every remaining unit and for the lender's valuation; your commission is a one-off.

---

## 3. Capital structure

| Source | Cost | Security | Character |
|---|---|---|---|
| **Equity** | Highest (target 18–25%+ IRR) | Residual | Patient, takes first loss |
| **Structured / mezzanine** | 15–20% | Subordinated charge | Fills the gap between equity and senior debt |
| **Construction finance (senior debt)** | Bank or NBFC ⏱ | Mortgage on land + receivables | Drawn against milestones |
| **Customer advances** | "Free", but constrained | — | **70% ring-fenced by RERA** |

**Why RERA changed developer finance fundamentally:** before 2016, customer advances were the
cheapest capital in Indian real estate and could be moved between projects. The **s.4(2)(l)(D)
70% rule** ended that. Developers now need **real project finance**, which is why the sector
consolidated after RERA — smaller developers who relied on cross-funding could not raise it.

**The three-account structure** (Module 6) is the operational expression of this: collections in,
70% ring-fenced, up to 30% released.

---

## 4. The metrics

### 4.1 NPV
```
NPV = Σ [ Cash flow_t ÷ (1 + r)^t ]
```
Positive NPV at your required return = the project creates value. `r` is the discount rate —
for Indian residential development, equity discount rates of **15–20%** are common. ⏱

### 4.2 IRR
The discount rate at which NPV = 0. **IRR is time-sensitive** — the same profit earned two years
later is a much lower IRR. This is why **delay destroys developer returns faster than cost overruns**.

### 4.3 Break-even
```
Break-even sales (sq ft) = Total Project Cost ÷ Average realisation per sq ft
```

### 4.4 Sales velocity and absorption
```
Sales velocity = Units sold ÷ Month
Absorption rate = Units sold ÷ Total units available
Quarters-to-sell = Unsold inventory ÷ Average quarterly sales
```
**Sales velocity is the number a developer watches daily.** It determines whether collections
outpace construction spend — and whether they can service debt.

---

## 5. 🏗 Case study: a ₹500 crore Mumbai project

> **"Meridian Heights" — Goregaon East.** Greenfield, 2 towers, 5-year cycle.
> **Saleable area 3,50,000 sq ft · ~350 units · average realisation ₹20,000/sq ft**
> *(Constructed example, built to realistic Mumbai parameters, for teaching the structure.)*

### 5.1 The deal at a glance

| | ₹ crore |
|---|---|
| **Gross Development Value** (3,50,000 sq ft × ₹20,000) | **700.0** |
| Land | 200.0 |
| Approvals, premiums, TDR | 60.0 |
| Construction (3,50,000 sq ft × ₹4,500) | 157.5 |
| Marketing & brokerage (4% of GDV) | 28.0 |
| Finance cost | 40.0 |
| Overheads & contingency | 14.5 |
| **Total Project Cost** | **500.0** |
| **Development Profit** | **200.0** |

**Development margin** = 200 ÷ 700 = **28.6%**
**Return on cost** = 200 ÷ 500 = **40.0%**

### 5.2 The cash flow — where the story actually is

| Year | Land & approvals | Construction | Marketing | Finance | Overheads | **Outflow** | **Collections** | **Net** | Cumulative |
|---|---|---|---|---|---|---|---|---|---|
| **Y1** | 260.0 | — | 5.0 | 8.0 | 3.0 | **276.0** | — | **(276.0)** | (276.0) |
| **Y2** | — | 35.0 | 9.0 | 12.0 | 3.0 | **59.0** | 105.0 | **+46.0** | (230.0) |
| **Y3** | — | 50.0 | 8.0 | 11.0 | 3.0 | **72.0** | 180.0 | **+108.0** | (122.0) |
| **Y4** | — | 45.0 | 4.0 | 6.0 | 3.0 | **58.0** | 215.0 | **+157.0** | +35.0 |
| **Y5** | — | 27.5 | 2.0 | 3.0 | 2.5 | **35.0** | 200.0 | **+165.0** | **+200.0** |
| **Total** | **260.0** | **157.5** | **28.0** | **40.0** | **14.5** | **500.0** | **700.0** | **+200.0** | |

**Read the cumulative column.** The project is **cash-negative until sometime in Year 4**. Peak
funding requirement is **₹276 crore in Year 1**, before a single rupee of revenue.

### 5.3 The returns

| Metric | Value |
|---|---|
| **Project IRR** (on net cash flows) | **≈ 21.3%** |
| **NPV @ 15% discount rate** | **≈ +₹43 crore** |
| Profit ÷ GDV (margin) | 28.6% |
| Profit ÷ cost | 40.0% |

*(IRR is the rate where NPV = 0. At 21% NPV is +₹1.4 cr; at 22% it is −₹4.8 cr — so IRR sits just above 21%.)*

### 5.4 Funding and break-even

**Funding:** equity ~₹120 crore + construction finance ~₹160 crore covers the ₹276 crore Year-1
peak; debt is repaid from Year 3–4 collections.

**Break-even:**
```
500 crore ÷ ₹20,000 per sq ft  =  2,50,000 sq ft
```
**The developer must sell 2,50,000 of 3,50,000 sq ft — 71.4% of the project — simply to break even.**
All the profit lives in the **last 29%**.

**Required sales velocity:** 3,50,000 sq ft over 4 selling years ≈ **7.3 units per month**, every
month, for 48 months.

> 🔴 **This single fact explains most developer behaviour you will ever encounter.** The last 29%
> of inventory carries 100% of the profit. That is why developers protect headline pricing on the
> final phase, why they'd rather pay you 3% than cut 5%, and why a stalled sales month is a
> genuine emergency rather than a slow patch.

### 5.5 Sensitivity — why this business is fragile

| Scenario | Profit | Project IRR | Comment |
|---|---|---|---|
| **Base case** | ₹200 cr | **≈21.3%** | |
| **Price −10%** (₹18,000/sq ft) | ₹130 cr | **≈14.3%** | A 10% price cut removes **7 points of IRR** |
| **Construction cost +15%** | ₹176 cr | ≈19.9% | Painful but survivable |
| **12-month delay** | ~₹185 cr | ≈17.5% | Extra finance + overheads, *and* profit arrives a year later |
| **Sales velocity halves** | — | Falls sharply | Collections stop funding construction; debt service becomes the binding constraint |

**Operating leverage is brutal.** A 10% fall in price cuts profit by 35% and IRR by a third,
because costs are almost entirely fixed once land is bought. **This is why developers discount
through freebies, furniture, stamp-duty offers and higher brokerage rather than headline price** —
those don't reset the benchmark for the remaining 71% of inventory.

### 5.6 What this means for you as an agent 💼

| Developer's position | Your opportunity |
|---|---|
| Cash-negative until Y4 | Early-phase buyers have the most negotiating leverage |
| Break-even at 71% | Late-phase inventory is where they're least flexible on price |
| Fixed cost, variable revenue | Ask for **non-price** concessions — parking, floor rise waiver, payment plan, stamp duty |
| Velocity is the metric | A broker who delivers **consistent monthly volume** is worth more than one who brings occasional big deals — price your services accordingly |
| Quarter/year-end | Recognition and collection targets create real windows. **This is practice, not law** — don't promise a client a discount that may not come |

---

## 6. 📖 Read first

| Priority | Resource | Read | Why |
|---|---|---|---|
| 🔴 | [Knight Frank — India Real Estate H1 2026 (PDF)](https://content.knightfrank.com/research/3116/documents/en/india-real-estate-office-and-residential-market-h1-2026-12927.pdf) | Sales, launches, unsold inventory, QTS | The demand side of every developer model |
| 🔴 | [RBI Master Circular — Housing Finance](https://www.rbi.org.in/commonman/Upload/English/Notification/PDFs/46MS250915FA.pdf) | LTV, risk weights | The rules that govern the buyer's leverage |
| 🔴 | [MahaRERA — Bank Account Order](https://maharera.maharashtra.gov.in/sites/default/files/Orders_and_circulars/BANK_ACCOUNT_ORDER.pdf) | Whole order | How the 70% rule constrains developer cash |
| 🟠 | [Real Estate Project Development Life Cycle — R.Estate Fin](https://restatefin.com/real-estate-project-development-life-cycle/) | Whole page | Cost and cash-flow stages laid out |
| 🟠 | [Colliers — 2026 India Office Outlook](https://www.colliers.com/en-in/research/2026-india-office_unlocking-agility-vitality-and-flight-to-quality) | Demand/supply | Commercial development economics differ — worth contrasting |

---

## 7. 🎥 Watch ▶️

| Order | Video | Covers |
|---|---|---|
| 1 🔴 | [Investment Analysis for Commercial Real Estate — an Introduction to NPV & IRR](https://www.youtube.com/watch?v=pEU237QgVak) | The cleanest introduction to NPV and IRR for property |
| 2 🔴 | [Residual Land Value](https://www.youtube.com/watch?v=G_3Gq3eA3Ro) | How land is valued backwards from GDV |
| 3 🟠 | [Residual Land Value module — All-in-One Model walkthrough](https://www.youtube.com/watch?v=JKuWeWS2v5c) | The same, inside a real feasibility model |
| 4 🟠 | [Calculating NPV and IRR in Excel — step by step](https://www.youtube.com/watch?v=oMbpBVciS-o) | The spreadsheet mechanics you need for the exercise |

> These are US/UK-oriented. The **mechanics are universal**; the Indian specifics — premiums, TDR,
> the 70% rule, rehab components — are in this module and Module 11.

---

## 8. 📑 Deep dive 🟢

**IIM Bangalore Working Paper No. 477 — Housing Price Indices in India**
🔗 https://www.iimb.ac.in/sites/default/files/2018-08/WP%20No.%20477.pdf
**Read:** methodology.
**Why:** every revenue line in a feasibility model rests on an assumed price path. This shows how
fragile price measurement itself is.

**Impact of RERA Act 2016 — ResearchGate**
🔗 https://www.researchgate.net/publication/369038845_Impact_of_Real_Estate_Regulatory_Authority_RERA_Act_2016
**Read:** the sections on developer consolidation and funding.
**Why:** documents the financing shift this module describes.

---

## 9. Practical exercise ✍️

**Build the feasibility model (3 hours).**

Recreate the Meridian Heights model in a spreadsheet with these inputs: saleable area, realisation
per sq ft, land cost, construction cost per sq ft, approvals %, marketing %, finance %, and a
5-year phasing of construction spend and collections.

Outputs: GDV, total cost, profit, margin, return on cost, annual net cash flow, cumulative cash
flow, **NPV at 15%**, **IRR**, **break-even sq ft** and **break-even %**.

Then run the four sensitivities in §5.5 and add one of your own: **what happens if collections slip
by six months but construction spend doesn't?**

That last one is the scenario that actually kills projects — and now you'll be able to see it coming
in a QPR.

---

## 10. Quiz — 10 questions

1. Write the residual land value formula.
2. Why does RERA's 70% rule change developer financing?
3. In Meridian Heights, what is peak funding requirement and in which year?
4. In which year does the project turn cash-positive cumulatively?
5. Break-even sales area and percentage?
6. Development margin vs return on cost — which is higher and why?
7. A 10% price fall does what to profit and IRR?
8. Why do developers prefer freebies and higher brokerage to a headline price cut?
9. Why does delay hurt IRR more than a comparable cost overrun?
10. What is quarters-to-sell, and where would you find it?

<details><summary>Answers</summary>

1. **RLV = GDV − (all costs except land) − required developer profit.**
2. Customer advances were previously the cheapest, most flexible capital and could be moved between projects. Ring-fencing 70% in a project-specific account forces developers to raise genuine project finance — a major driver of post-RERA consolidation.
3. **₹276 crore, in Year 1** — before any revenue.
4. Cumulative cash flow turns positive during **Year 4** (+₹35 crore at year-end).
5. **2,50,000 sq ft**, which is **71.4%** of the 3,50,000 sq ft saleable area.
6. **Return on cost (40%)** is higher than **margin (28.6%)** — margin divides by revenue, return on cost divides by the smaller cost base.
7. Profit falls from **₹200 cr to ₹130 cr** (−35%); IRR falls from **~21.3% to ~14.3%**. Operating leverage: costs are fixed once land is committed.
8. A headline price cut resets the benchmark for **all remaining inventory** (71% of the project, where all the profit sits) and affects lender valuations. Freebies and brokerage are one-off costs that don't reset the price benchmark.
9. IRR is time-weighted — the same profit received later is a lower IRR — and a delay adds finance and overhead cost **on top**. A cost overrun only reduces the numerator.
10. Unsold inventory ÷ average quarterly sales — an inventory overhang measure. Published in **Knight Frank**, ANAROCK and JLL market reports.
</details>

---

## 11. Interview questions 🎤

- *"How does a developer decide what to pay for land?"*
- *"Where does a residential project's profit actually sit?"*
- *"Why won't a developer just cut price when sales are slow?"*
- *"What does the 70% rule do to a developer's balance sheet?"*
- *"You see a project with flat QPR progress for three quarters. What's the financial diagnosis?"*
- *"Walk me through the difference between margin, return on cost and IRR."*

---

## 12. Key terms

**GDV** · **Residual land value** · **Development margin** · **Return on cost** · **NPV** · **IRR** ·
**Hurdle rate** · **Break-even** · **Sales velocity** · **Absorption** · **Quarters-to-sell** ·
**Construction finance** · **Mezzanine** · **Operating leverage** · **Rehab component** ·
**Peak funding requirement**

---

## 13. One-page revision sheet

> **GDV** = saleable × realisation. **Profit** = GDV − total cost.
> **Margin** = profit ÷ GDV. **Return on cost** = profit ÷ cost. **RLV** = GDV − costs − required profit.
>
> **Meridian Heights (₹500 cr cost / ₹700 cr GDV):**
> profit **₹200 cr** · margin **28.6%** · return on cost **40%** · **IRR ≈ 21.3%** · **NPV@15% ≈ +₹43 cr**
> peak funding **₹276 cr in Y1** · cash-positive in **Y4** · **break-even 2,50,000 sq ft = 71.4%**
> required velocity **~7.3 units/month for 48 months**
>
> **Sensitivity:** price −10% → profit −35%, **IRR 21.3% → 14.3%**. Costs are fixed; revenue isn't.
>
> **Therefore:** all the profit is in the last ~29% of inventory · developers protect headline price
> and pay in freebies/brokerage · **velocity is the metric** · delay hurts IRR more than overruns ·
> the 70% rule is why real project finance exists.
>
> **Your leverage:** early phase, non-price concessions, consistent monthly volume.
