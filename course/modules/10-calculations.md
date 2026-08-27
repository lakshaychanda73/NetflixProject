# Module 10 — Real Estate Calculations

> **Official syllabus:** MATP Module 10 — 10.1 Taxation/Government Fees and Levies (10.1.1 GST · 10.1.2 TDS · 10.1.3 Registration charge · 10.1.4 Stamp duty · 10.1.5 External Development Charges) · 10.2 Cost Sheet Sample and Component details.
> **Exam weight:** 🔴 High — and numerical questions are the easiest marks to secure.
> **Time:** 4–5 hours. Do the arithmetic by hand at least once.

---

## ⏱ Read this before anything else

**Every rate in this module changes.** Stamp duty moves with state budgets, GST with the GST
Council, TDS with the Union Budget, LTV with RBI circulars, ready reckoner rates annually.

The rates used here reflect the position at the time of writing and are **illustrative for
learning the method**. Before you quote a number to a client:

| Item | Verify at |
|---|---|
| Stamp duty, registration, ready reckoner | [IGR Maharashtra](https://igrmaharashtra.gov.in/) · [e-ASR](https://igrmaharashtra.gov.in/Home/asr_about) |
| GST | [CBIC](https://www.cbic.gov.in/) / GST Council |
| TDS | [Income Tax Department](https://www.incometax.gov.in/) |
| LTV | [RBI Master Circular — Housing Finance](https://www.rbi.org.in/commonman/Upload/English/Notification/PDFs/46MS250915FA.pdf) |

**Learn the method. Look up the rate.** That is the professional habit.

---

## 🏠 The master example — one flat, all the maths

Everything below runs through a single flat so the numbers connect.

> **Flat A — Goregaon East, Mumbai. Under construction.**
> **RERA carpet area: 750 sq ft** · Saleable quoted: **1,050 sq ft** · Quoted rate: **₹20,000/sq ft on saleable**
> **Agreement value: 1,050 × ₹20,000 = ₹2,10,00,000**

---

## 1. Carpet area and loading

**Concept →** Under **s.2(k)** you must sell on **carpet area**. "Saleable" or "super built-up"
is a marketing number with no statutory definition. **Loading** is the gap.

**Formula →**
```
Loading %  =  (Saleable area − Carpet area) ÷ Carpet area × 100
Effective rate on carpet  =  Agreement value ÷ Carpet area
```

**Example →** Loading = (1,050 − 750) ÷ 750 × 100 = **40%**
Effective rate = ₹2,10,00,000 ÷ 750 = **₹28,000 per carpet sq ft**

**Mumbai reality 💼 →** Loading commonly runs 30–45%. Two flats quoted at "₹20,000/sq ft" with
loadings of 30% and 45% differ by roughly **₹3,000 per carpet sq ft** in real terms. **Always
re-quote on carpet before comparing anything.**

> ⚠️ 60 sq m = **645.8 sq ft**. Keep that conversion handy — the GST affordable-housing test uses
> square metres of carpet area.

**Practice →** Flat B: carpet 620 sq ft, saleable 930 sq ft, agreement value ₹1,58,10,000.
Loading? Effective carpet rate? Which is better value, A or B?
<details><summary>Answer</summary>
Loading = (930−620)/620 = **50%**. Effective = 1,58,10,000 ÷ 620 = **₹25,500/carpet sq ft**.
**B is better value on carpet** (₹25,500 vs ₹28,000) despite the far worse loading — which is
exactly why you compare on carpet, not on loading and not on the quoted rate.
</details>

---

## 2. Stamp duty ⏱ (syllabus 10.1.4)

**Concept →** A state tax on the instrument, payable to Maharashtra, levied on the **higher of the
agreement value and the ready reckoner (ASR) value**.

**⏱ Mumbai rates (illustrative — verify at IGR):**

| Buyer | Base | Metro cess | **Total** |
|---|---|---|---|
| Male / joint (with a male) | 5% | 1% | **6%** |
| **Female sole owner** | 4% | 1% | **5%** |

The 1% **Metro Cess** funds metro rail expansion and applies within Mumbai municipal limits.
The women's concession applies where a woman is the **sole owner**; joint ownership with a male
co-owner attracts the blended rate.

**Formula →** `Stamp duty = Applicable % × HIGHER of (Agreement value, ASR value)`

**Example →**
- Male buyer: 6% × ₹2,10,00,000 = **₹12,60,000**
- Female sole buyer: 5% × ₹2,10,00,000 = **₹10,50,000** *(saves ₹2,10,000)*

**The ready reckoner trap 🚩 →** If the **ASR value is ₹2,25,00,000** while the agreement value is
₹2,10,00,000, stamp duty is charged on **₹2,25,00,000**:
6% × 2,25,00,000 = **₹13,50,000** — **₹90,000 more** than the buyer budgeted.
**Always check e-ASR before quoting stamp duty.**

**Practice →** Female sole buyer, agreement value ₹95,00,000, ASR value ₹1,02,00,000. Stamp duty?
<details><summary>Answer</summary>
Higher value = ₹1,02,00,000. 5% × 1,02,00,000 = **₹5,10,000**.
</details>

---

## 3. Registration charge ⏱ (syllabus 10.1.3)

**Concept →** The fee for registering the instrument under the Registration Act, 1908.

**⏱ Maharashtra (illustrative):**
```
Property value > ₹30 lakh  →  ₹30,000 (capped)
Property value ≤ ₹30 lakh  →  1% of value
```

**Example →** Flat A: value ₹2.1 crore > ₹30 lakh → **₹30,000**

**Practice →** Agreement value ₹28,00,000. Registration charge?
<details><summary>Answer</summary>1% × 28,00,000 = **₹28,000** (below the ₹30 lakh threshold, so 1% applies, not the cap).</details>

---

## 4. GST ⏱ (syllabus 10.1.1)

**Concept →** GST applies **only to under-construction** property sold by a promoter. A completed
unit with an **Occupancy Certificate is outside GST entirely** — it's a transfer of immovable property.

**⏱ Rates (illustrative — verify at CBIC):**

| Category | Rate | ITC |
|---|---|---|
| **Affordable** residential | **1%** | **No ITC** |
| **Other** residential (under construction) | **5%** | **No ITC** |
| **Ready with OC / resale** | **0%** | — |

**Affordable housing test — both conditions must hold:**
- Consideration **≤ ₹45 lakh**, **and**
- Carpet area **≤ 60 sq m in metros** (≤ 90 sq m non-metro). *Mumbai is a metro.*

**ITC note:** Input Tax Credit is **not available** to residential buyers — blocked under
s.17(5)(d) of the CGST Act. Even a GST-registered business buyer cannot claim the 1% or 5% back.

**Example →** Flat A: 750 sq ft = 69.7 sq m (>60) and ₹2.1 crore (>₹45 lakh) → **not affordable**.
GST = 5% × ₹2,10,00,000 = **₹10,50,000**

**Practice →** Flat in Mumbai: carpet 58 sq m, agreement value ₹43,00,000. GST?
<details><summary>Answer</summary>
Both tests pass (≤60 sq m **and** ≤₹45 lakh) → **1%** = **₹43,000**. If either failed, it would be 5%.
</details>

---

## 5. TDS ⏱ (syllabus 10.1.2)

### 5.1 On the purchase — s.194-IA
**1%** of consideration where consideration is **₹50 lakh or more**. Buyer deducts, files
**Form 26QB**, issues **Form 16B**. **On the whole amount, not the excess over ₹50 lakh.**

**Example →** 1% × ₹2,10,00,000 = **₹2,10,000**
The buyer pays ₹2,07,90,000 to the promoter and ₹2,10,000 to the government.

> **This is not an extra cost.** It is part of the consideration, routed to the government.
> Agents confuse buyers constantly on this point.

### 5.2 On brokerage — s.194H ⏱
**2%** (from 1 Oct 2024), threshold **₹20,000** per financial year, **20%** without PAN.

**Example — your own fee on Flat A at 2% brokerage:**

| Line | Amount |
|---|---|
| Brokerage (2% of ₹2,10,00,000) | ₹4,20,000 |
| GST @18% (if you're registered) | ₹75,600 |
| Gross invoice | ₹4,95,600 |
| Less TDS u/s 194H @2% on ₹4,20,000 | (₹8,400) |
| **Received in bank** | **₹4,87,200** |
| Less GST to remit | (₹75,600) |
| **Retained (before your costs)** | **₹4,11,600** |

The ₹8,400 TDS is **not lost** — it's credit against your income tax liability.

**Practice →** Brokerage ₹1,80,000, you are GST-registered. What do you receive and what's the TDS?
<details><summary>Answer</summary>
GST 18% = ₹32,400 → invoice ₹2,12,400. TDS 2% × 1,80,000 = **₹3,600**. Received = ₹2,08,800. Remit ₹32,400 GST. Retained ₹1,76,400, plus ₹3,600 TDS credit.
</details>

---

## 6. External Development Charges (syllabus 10.1.5) 💼

**Concept →** Charges levied by a development/planning authority to fund external infrastructure —
roads, water, sewerage, drainage — outside the project boundary. Related levies include
Infrastructure Development Charges, betterment charges, premium FSI charges and open-space
deficiency charges.

**Important Maharashtra note:** "EDC" as a named, standardised levy is most prominent in states
like Haryana. In Maharashtra and especially Greater Mumbai, the equivalent burden appears as
**development charges, premiums (including premium FSI), and various planning-authority levies**
under the MRTP Act and DCPR 2034, varying by authority — MCGM, MMRDA, CIDCO, and municipal
corporations in the MMR.

**What matters to you:** these are **developer costs that end up in your buyer's price**, and they
sometimes appear as separate line items in a cost sheet. If a cost sheet has an
"infrastructure charge" or "development charge" line, ask what it is and whether it is already in
the agreement value or on top. ⏱ Rates are authority-specific — verify with the planning authority.

---

## 7. 📋 The cost sheet (syllabus 10.2) — Flat A, fully built up

This is the single most useful table in the module. **This is what a real cost sheet should look like.**

| # | Component | Basis | Amount (₹) |
|---|---|---|---|
| **A** | **Agreement value** | 1,050 saleable × ₹20,000 | **2,10,00,000** |
| B | GST @ 5% (under construction) | 5% of A | 10,50,000 |
| C | Stamp duty @ 6% (male buyer) | 6% of higher of A / ASR | 12,60,000 |
| D | Registration charge | capped | 30,000 |
| E | Club / amenities membership 💼 | one-time | 3,00,000 |
| F | Maintenance advance 💼 | 12 months | 2,50,000 |
| G | Legal & documentation 💼 | one-time | 50,000 |
| | **TOTAL ACQUISITION COST** | A+B+C+D+E+F+G | **₹2,39,40,000** |

> ⚠️ GST may also apply to items E–G depending on how they are structured. Ask.
> TDS of ₹2,10,000 is **within** A, not additional.

**The two numbers to show every client:**

```
Headline quoted        ₹20,000 / saleable sq ft
Actual all-in cost     ₹2,39,40,000 ÷ 750 carpet sq ft  =  ₹31,920 / carpet sq ft
```

**The all-in cost is 14% above the headline agreement value, and the true per-square-foot cost is
about 60% above the quoted rate.** Neither number is a trick — both are real. An agent who leads
with this builds trust permanently; one who hides it gets found out at registration.

---

## 8. Home loan mathematics

### 8.1 LTV and down payment ⏱

| Loan | Max LTV |
|---|---|
| ≤ ₹30 lakh | 90% |
| ₹30–75 lakh | 80% |
| > ₹75 lakh | **75%** |

🔴 **Stamp duty, registration and documentation charges are excluded from "cost" for LTV**
(except where the unit costs ≤ ₹10 lakh). The buyer funds those from their own pocket.

**Flat A cash requirement:**

| Line | Amount (₹) |
|---|---|
| Property value | 2,10,00,000 |
| Loan @ 75% LTV | 1,57,50,000 |
| **Down payment (25%)** | **52,50,000** |
| GST | 10,50,000 |
| Stamp duty | 12,60,000 |
| Registration | 30,000 |
| Other (club, maintenance, legal) | 6,00,000 |
| **TOTAL CASH NEEDED** | **₹81,90,000** |

> 💼 **This is where Mumbai deals die.** The buyer budgeted ₹52.5 lakh and needs **₹81.9 lakh** —
> a **₹29.4 lakh gap**. Run this calculation at **qualification**, not at booking.

### 8.2 EMI

**Formula →**
```
            P × r × (1 + r)^n
EMI  =  ─────────────────────────
             (1 + r)^n − 1

P = principal   r = monthly rate (annual ÷ 12 ÷ 100)   n = months
```

**Example →** P = ₹1,57,50,000 · 8.5% p.a. · 20 years
r = 0.085 ÷ 12 = 0.0070833 · n = 240 · (1+r)^240 ≈ 5.4412

EMI = (1,57,50,000 × 0.0070833 × 5.4412) ÷ (5.4412 − 1) = **≈ ₹1,36,700 per month**

| | Amount |
|---|---|
| Total repaid over 20 years | ₹3,28,00,000 (approx.) |
| Principal | ₹1,57,50,000 |
| **Total interest** | **≈ ₹1,70,50,000** |

**The interest exceeds the principal.** Say this to every buyer. Then show them what a shorter
tenure does — it is the highest-value financial advice you can give for free.

**Practice →** P = ₹80,00,000, 9% p.a., 15 years. Estimate the EMI.
<details><summary>Answer</summary>
r = 0.0075, n = 180, (1.0075)^180 ≈ 3.838.
EMI = (80,00,000 × 0.0075 × 3.838) ÷ 2.838 = 2,30,280 ÷ 2.838 ≈ **₹81,140/month**.
</details>

### 8.3 FOIR 💼
`FOIR = All monthly obligations ÷ Net monthly income`. Lenders typically cap around **50–60%**.
An EMI of ₹1,36,700 at a 55% FOIR implies a net monthly income around **₹2.5 lakh** — before any
other loan. Check this at qualification.

---

## 9. Investment metrics

### 9.1 Rental yield
```
Gross yield = Annual rent ÷ Total acquisition cost × 100
Net yield   = (Annual rent − maintenance − property tax − vacancy) ÷ Total acquisition cost × 100
```
**Example →** Flat A rents at ₹65,000/month → ₹7,80,000/year.
Gross (on all-in ₹2,39,40,000) = **3.26%** · Gross (on agreement value) = 3.71%
Net, after ₹90,000 outgoings = **2.88%**

💼 **Mumbai residential gross yields typically run ~2.5–3.5%.** Commercial runs materially higher.
A client told to expect 6% residential yield in Mumbai has been misled — and if you said it, you
have a **s.10(c)** problem.

### 9.2 Capital appreciation and CAGR
```
CAGR = ((Final ÷ Initial)^(1 ÷ years) − 1) × 100
```
**Example →** All-in ₹2,39,40,000; sold after 5 years at ₹2,95,00,000.
Ratio 1.2322 → **CAGR ≈ 4.27%**

### 9.3 ROI
```
Simple ROI = (Sale price − Total acquisition cost) ÷ Total acquisition cost × 100
```
= (2,95,00,000 − 2,39,40,000) ÷ 2,39,40,000 = **23.2% over 5 years**

> 🚩 **The honest version:** this ignores the interest paid, the rent received, brokerage on exit,
> and capital gains tax. Comparing a *gross sale price* against an *all-in cost* is the most common
> way property returns get overstated. Total return = rental income **+** appreciation **−** all
> costs **−** financing **−** tax.

**Practice →** Bought all-in ₹1,20,00,000, sold at ₹1,85,00,000 after 7 years. CAGR? Simple ROI?
<details><summary>Answer</summary>
Ratio = 1.5417. CAGR = 1.5417^(1/7) − 1 ≈ **6.4% p.a.** Simple ROI = 65,00,000/1,20,00,000 = **54.2% over 7 years**.
</details>

---

## 10. 📖 Official sources 🏛

| Item | Official source |
|---|---|
| Stamp duty, registration, **ready reckoner (ASR)** | [IGR Maharashtra](https://igrmaharashtra.gov.in/) · [About the ASR / e-ASR](https://igrmaharashtra.gov.in/Home/asr_about) |
| GST rates and notifications | [CBIC](https://www.cbic.gov.in/) |
| TDS — 194-IA, 194H, Form 26QB | [Income Tax Department](https://www.incometax.gov.in/) |
| LTV and housing finance norms | [RBI Master Circular — Housing Finance](https://www.rbi.org.in/commonman/Upload/English/Notification/PDFs/46MS250915FA.pdf) |
| Carpet area definition | [RERA Act s.2(k) — India Code](https://www.indiacode.nic.in/bitstream/123456789/2158/1/A201616.pdf) |
| Development charges / premiums | MCGM · MMRDA · CIDCO · relevant planning authority |

---

## 11. 🎥 Videos ▶️

| Order | Video | Covers |
|---|---|---|
| 1 🔴 | [Understanding Carpet Area — Built up & Super Built up \| Calculation, Loading & RERA](https://www.youtube.com/watch?v=DPj2x6cwsT4) | Loading maths, worked |
| 2 🔴 | [Carpet Area (RERA) — Calculation, Formula & Measurement (Hindi)](https://www.youtube.com/watch?v=sjv7XMUQzgE) | Measurement, step by step |
| 3 🟠 | [Carpet area, Built-up, Super Built-up as per RERA](https://www.youtube.com/watch?v=9jhQL-lOxwA) | A second explanation of the same distinctions |
| 4 🟢 | [Calculating NPV and IRR in Excel — step by step](https://www.youtube.com/watch?v=oMbpBVciS-o) | Spreadsheet technique, feeds Module 12 |

---

## 12. Practical exercise ✍️

**Build the cost-sheet calculator (2 hours).**

Make a spreadsheet with inputs: carpet area, saleable area, rate, buyer gender, ASR value,
under-construction Y/N, affordable Y/N, LTV band, interest rate, tenure.

Outputs: loading %, effective carpet rate, GST, stamp duty (on the higher value), registration,
**total acquisition cost**, **all-in cost per carpet sq ft**, loan, **total cash required**, EMI,
total interest.

Then run **three real Mumbai listings** through it. You will find at least one where the all-in
cost is more than 15% above the headline. **That spreadsheet, shown to a client on a phone, is
worth more than any brochure.**

---

## 13. Case study 📋 — the two flats that look identical

> Two 2BHKs, same building, same floor, listed the same week.
> **Flat X:** carpet 700 sq ft, saleable 1,000 sq ft, quoted ₹21,000/sq ft saleable. Ready, **OC received**.
> **Flat Y:** carpet 700 sq ft, saleable 980 sq ft, quoted ₹20,500/sq ft saleable. **Under construction**, possession in 18 months.
> Buyer is a **woman purchasing in her sole name**. ASR value for both: ₹2,00,00,000.

Which is cheaper, all in?

<details><summary>Full working</summary>

**Flat X (ready, OC received):**
- Agreement value = 1,000 × 21,000 = **₹2,10,00,000**
- GST = **₹0** (OC received — outside GST)
- Stamp duty = 5% (female sole) × higher of (2,10,00,000 / 2,00,00,000) = 5% × 2,10,00,000 = **₹10,50,000**
- Registration = **₹30,000**
- **Total ≈ ₹2,20,80,000** · per carpet sq ft = 2,20,80,000 ÷ 700 = **₹31,543**

**Flat Y (under construction):**
- Agreement value = 980 × 20,500 = **₹2,00,90,000**
- GST @5% = **₹10,04,500**
- Stamp duty = 5% × higher of (2,00,90,000 / 2,00,00,000) = 5% × 2,00,90,000 = **₹10,04,500**
- Registration = **₹30,000**
- **Total ≈ ₹2,21,29,000** · per carpet sq ft = 2,21,29,000 ÷ 700 = **₹31,613**

**Result: they cost almost exactly the same — within ₹49,000, about 0.2%.**

**But they are not the same deal:**

| | Flat X | Flat Y |
|---|---|---|
| Possession | Immediate | 18 months |
| 18 months of rent saved / paid | Saves ~₹11.7 lakh at ₹65k/month | Pays it |
| Delay risk | **None** | **Real** — s.18 is a remedy, not a guarantee |
| GST | Nil | ₹10 lakh, no ITC |
| Construction risk | None | Full |

**Conclusion:** at an identical all-in price, **Flat X is decisively better** — the buyer avoids
₹11.7 lakh of rent, all completion risk, and gets the asset today. Flat Y's slightly lower headline
rate (₹20,500 vs ₹21,000) is *entirely* an illusion created by the smaller saleable-area figure and
the GST that the buyer forgot to add.

**The lesson:** the headline rate told you the wrong answer. **Carpet + all-in + time** told you
the right one. This is the single most valuable calculation an agent can do.
</details>

---

## 14. Quiz — 10 questions

1. Carpet 800, saleable 1,120. Loading?
2. Stamp duty is charged on which value?
3. Mumbai stamp duty for a female sole buyer, including metro cess?
4. Registration charge on a ₹1.4 crore flat?
5. Both conditions for the 1% GST affordable rate in a metro?
6. Is GST payable on a ready flat with an OC?
7. Flat at ₹62 lakh. TDS u/s 194-IA — on what amount, and how much?
8. Current TDS rate on brokerage, and from when?
9. Maximum LTV on a ₹1.2 crore property, and is stamp duty included in "cost"?
10. Annual rent ₹6,00,000, all-in cost ₹1,80,00,000. Gross yield?

<details><summary>Answers</summary>

1. (1,120 − 800) ÷ 800 = **40%**
2. The **higher** of agreement value and **ready reckoner (ASR)** value.
3. **5%** — 4% base + 1% metro cess (sole female owner). ⏱ verify.
4. **₹30,000** (capped, above ₹30 lakh).
5. Consideration **≤ ₹45 lakh** **and** carpet area **≤ 60 sq m**. Both required.
6. **No** — zero GST once the OC is received.
7. On the **whole ₹62,00,000** (threshold crossed), 1% = **₹62,000**.
8. **2%** under s.194H, from **1 October 2024** (reduced from 5%). ⏱ verify.
9. **75%** (above ₹75 lakh). Stamp duty, registration and documentation charges are **excluded** from cost for LTV.
10. 6,00,000 ÷ 1,80,00,000 = **3.33%** gross.
</details>

---

## 15. Interview questions 🎤

- *"A flat is quoted at ₹25,000 a square foot. What do you need to know before that number means anything?"*
- *"Walk me through the all-in cost of a ₹2 crore Mumbai flat."*
- *"When does GST apply and when doesn't it?"*
- *"A buyer has ₹60 lakh. What can they actually afford?"*
- *"What rental yield should I expect on a Mumbai 2BHK?"*
- *"Explain why the interest on a 20-year loan exceeds the principal."*

---

## 16. Key terms

**Carpet / saleable / loading** · **Effective carpet rate** · **ASR / ready reckoner** ·
**Metro cess** · **Registration cap** · **Affordable housing test** · **ITC block** ·
**Form 26QB / 16B** · **194-IA / 194H** · **LTV** · **FOIR** · **EMI** · **Pre-EMI** ·
**Gross vs net yield** · **CAGR** · **Total acquisition cost**

---

## 17. One-page revision sheet

> **Loading** = (Saleable − Carpet) ÷ Carpet. **Always re-quote on carpet.**
>
> **⏱ Stamp duty (Mumbai):** male/joint **6%**, female sole **5%** (incl. 1% metro cess),
> on the **HIGHER of agreement value and ASR**.
> **⏱ Registration:** **₹30,000** above ₹30 lakh; else 1%.
> **⏱ GST:** **1%** affordable (≤₹45L **and** ≤60 sq m metro) · **5%** other under-construction · **0%** with OC. **No ITC.**
> **⏱ TDS:** **194-IA** 1% on the **whole** consideration ≥₹50L (Form 26QB → 16B) ·
> **194H** **2%** on brokerage (from 1 Oct 2024), threshold ₹20,000/FY.
> **⏱ LTV:** ≤30L **90%** · 30–75L **80%** · >75L **75%**. **Stamp duty excluded from cost.**
>
> ```
> EMI = P·r·(1+r)^n / ((1+r)^n − 1)
> Gross yield = Annual rent ÷ Total acquisition cost
> CAGR = (Final/Initial)^(1/years) − 1
> ```
>
> **Total acquisition cost** = Agreement value + GST + Stamp duty + Registration + club + maintenance + legal.
> **Total cash needed** = Down payment + GST + stamp duty + registration + other. *Run this at qualification.*
>
> **Mumbai residential gross yields ≈ 2.5–3.5%.** Never promise more.
> **Learn the method. Look up the rate.**
