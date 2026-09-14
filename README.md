# Mumbai Real Estate — Master Report & Execution Blueprint

**Subject:** the Hines × Sumitomo boutique residential project at Chandivali / Powai, off JVLR, Mumbai.
**Purpose:** two jobs in one document — (A) assess and sell *this* asset, (B) build a Mumbai
real-estate practice around it.
**Compiled:** 14 September 2026.

---

## Start here

| File | What it is |
|---|---|
| **[`MASTER_REPORT.md`](MASTER_REPORT.md)** | ⭐ **The blueprint.** 13 parts, ~3,200 lines. Read Part 0 (the Evidence Ladder), then Part 2 (Source Reconciliation), then Part 10 (the question bank). Everything else is reference. |
| [`docs/transcript_digest.md`](docs/transcript_digest.md) | Every extractable claim from the 72-minute partner briefing, indexed by timestamp and cross-referenced to the report |
| [`docs/transcript_full.md`](docs/transcript_full.md) | The full transcript, with an ASR error key |
| [`models/cost_model.py`](models/cost_model.py) | Runnable cost / affordability / return model — change the assumptions, re-run |
| [`data/`](data/) | Comparables, appreciation history, unit economics as CSV |

```bash
python3 models/cost_model.py              # full output at Rs 55,000/sq ft
python3 models/cost_model.py --rate 48000 # what the channel says it should be
python3 models/cost_model.py --female     # 5% stamp duty
```

---

## The three things this document exists to tell you

**1. Get licensed before you get excited.**
MahaRERA agent registration takes 6–10 weeks: 20-hour training → competency exam → online filing.
Marketing a project without it, or before *the project's* own RERA number exists, carries a penalty of
₹10,000 per day capped at 5% of the property's cost — roughly ₹30.8 lakh on a ₹6.16 Cr flat.
**Nothing else in this report matters until Part 7A.3 is done.**

**2. The ₹55,000 is a specification argument, not a market argument.**
The JVLR reference rate is ₹40,000. Channel partners in the briefing said it should be ₹45–48,000.
The ask is ₹55,000. That gap is bridged — or not — by a 10-ft clear ceiling, a ~160 sq ft curved
floating deck plus a second deck off the master, conventional (not stack) resident parking, 250
neighbours instead of 2,000, a plot with no rehab/EWS/MHADA component and no reservation, 50 metres to
JVLR, and a Japanese institutional balance sheet. Part 5.3 breaks it down block by block.

**3. Your edge is not access. It is honesty.**
Thirty other partners will have the same renders. You will be the one who says: there is a building
between this plot and Powai Lake so there is no lake view below the 10th floor; the gross rental yield
is about 1.8%; plan for 2031 not 2030; and here is the informal settlement on the boundary. In a
₹7 crore sale to someone who prices risk for a living, that is the entire business.

---

## What is settled, and what is not

**Verified from public record.** The SPV is Powai Lake Residential Private Limited — Sumitomo
Corporation 90%, Hines 10%, with Hines as development manager. ~3.82 lakh sq ft saleable on a
~3.4-acre (≈13,000 sq m) Chandivali–Powai parcel. Metro Line 3 (Aqua Line) is fully operational to
Aarey JVLR; Metro Line 6 with Rambaug station is under construction on JVLR; the GMLR tunnel follows.
Powai area rates run ₹42,650; Hiranandani Gardens ₹43,930–58,350; Chandivali ₹33,200–34,050.

**Open — do not repeat these as fact.** The RERA registration (not on record at the time of writing).
Whether the scheme is 3 towers / 17 floors / 250 homes or 6 / 20 / 321. Whether ₹55,000 applies to
RERA carpet or something else. Which specific units get which view. Whether total open space is
1.5 acres or 2.42. The full all-in cost sheet. **Part 10 is the 45-question list that closes all of it.**

**Corrected in this report.** 1,560 sq ft is a *3 BHK large*, not a 4 BHK. The ~200 sq ft "balcony" is
two decks (150–160 living + 40–50 master). "Vastu complaint" in the field notes means Vastu
*compliance* — a stated design driver. "Ram borg" is *Rambaug*, a real Metro 6 station. The ticket band
is ₹6–13 Cr on agreement value, which is ₹7.1–14.7 Cr all-in.

---

## ⚠ Standing compliance rule

No public marketing of this project — named, anonymised, or via a micro-site — until **both** your
MahaRERA agent registration number **and** the project's MahaRERA registration number exist. The
developer's instruction to market it as "an international and global developer" without naming Hines
addresses *their* brand exposure; it does not address your statutory exposure under s.3 of RERA.
Until then, run micro-market content that names no project. Part 7C.1.

---

## Method

The 72-minute briefing audio was transcribed locally (Whisper-small ONNX with Silero VAD, offline).
Market, regulatory and competitor research was drawn from public sources, all linked in Part 13.4.
Financial figures were modelled in `models/cost_model.py` from stated inputs.

Every claim carries a provenance tag: `[V]` verified from public record · `[S]` stated by the sales
team, unverified · `[E]` estimated or modelled here · `[?]` sources contradict.
**Never repeat an `[S]` or `[E]` claim to a client as fact.**

*This is a research and planning document. It is not legal, tax or investment advice.*
