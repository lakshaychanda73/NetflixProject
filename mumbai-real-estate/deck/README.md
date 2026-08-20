# Brickrock Realty — 12-slide pitch deck

| File | What it is |
|---|---|
| `out/Brickrock_Realty_Pitch_Deck.pdf` | **The deck.** Exactly 12 slides, true 16:9 (960 × 540 pt). |
| `out/Brickrock_Deck_Diligence_Index.pdf` | 3-page appendix mapping every claim on every slide to its page in the playbook. |

Both are compressed from the 60-page *Mumbai Real Estate Master Playbook* in
`../report/`. The playbook is the research database; the deck is the argument.

## The rule this deck is written under

**Do not exaggerate what Brickrock is today.**

It is a micro-market real-estate advisory and brokerage business. Revenue is
brokerage and advisory commission — one line, nothing else. The intelligence
system exists to win the mandate, sharpen the shortlist and hold the line in a
negotiation, and as a by-product to capture transaction evidence that compounds.

It is **not** a property portal, not data SaaS, not an AI platform, not a
technology company and not a large brokerage. Slide 3 says this in as many words,
and no other slide contradicts it.

The thesis: *Mumbai has no shortage of property data. It has a shortage of
decision-grade advice.*

## Slide order

| # | Slide | The one thing it has to land |
|---|---|---|
| 1 | Opening | The market clears every month, and nobody is advising it from the record |
| 2 | The customer's problem | Six questions decide a ₹2.3 cr purchase; none are answered by a listing |
| 3 | What Brickrock is | One business, one revenue line, one by-product that compounds |
| 4 | How it works | Seven steps, one loop, an evidence layer that is a tool and not a product |
| 5 | Where we start | Six localities on one spine, chosen by a model that survives being wrong |
| 6 | Customer–market fit | 25% of closures pay 43% of the bills; rental is a lead nursery |
| 7 | Competitive positioning | Everyone competes on inventory; nobody competes on the decision |
| 8 | The moat | The transaction record only we will hold, and cannot be bought |
| 9 | Business model and economics | One revenue line at 1.32%, almost no capital at risk |
| 10 | Go to market | The cheap, defensible channels are the slow ones — so build them first |
| 11 | Capital and the proof | ₹11.3 L, twelve months, and a 90-day test that replaces the assumptions |
| 12 | Founder and the long arc | Already built a business from zero; brokerage earns the right to build |

`build_deck.py` asserts the deck is exactly 12 slides and fails the build otherwise.

## The founder arc, on slide 12

> BROKERAGE → PROPRIETARY TRANSACTION INTELLIGENCE → NETWORK, CAPITAL AND
> EXECUTION CAPABILITY → DEVELOPMENT AND JOINT VENTURE → BUILDER, JAIPUR

Each stage funds and de-risks the next. Nothing requires a leap — only that the
previous stage actually worked.

## Attribution discipline

Enforced in `build/founder.py` and never blurred on a slide:

| Claim | Attribution |
|---|---|
| ₹1.08 Cr revenue, +108% YoY, ₹17.1 L PAT, 183 invoices, 100% bootstrapped | **Lakshay's own business** (Sheesham.in) |
| @brickrockrealty, 1,055 followers, 366k top reel, ≈480k total views | **Lakshay's own presence** |
| ~310 acres | **Family inheritance** — not his personal asset |
| 124 acres + township | **His father's** land and development |

`founder.py` also carries `EDUCATION = ("IIM Mumbai", "INFERRED")`, inferred from a
profile highlight and a pinned campus post. It is **not used on any slide.** Confirm
it before adding it.

## Numbers cannot drift

Every quantity on every slide is read from `../../build/evidence.py` at build time —
including the blended commission rate, the average consideration, the funnel, the
cost base, the cash trough and the capital requirement. The playbook, the figures,
the CSVs, the workbook and the deck all read the same file, so a correction made
once propagates everywhere.

Two corrections were made at source in this round:

- **"Six localities", not five.** Powai, Kanjurmarg, Vikhroli, Bhandup, Mulund and
  Ghatkopar is six. The count was wrong in both the playbook and the deck.
- **1.32%, not 1.33%.** The model always computed 1.3231%; two figures had the
  rounded value typed in as a literal string. The rate is now derived everywhere
  from `E.BLENDED_RATE`.

## Rebuilding

```bash
cd build
make all        # figures + deck PDF + diligence index PDF
```

or individually:

```bash
python3 fig_deck.py      # -> ../figures/s*.png
python3 build_deck.py    # -> ../out/deck.html
python3 build_index.py   # -> ../out/diligence_index.html
```

## Design notes

- Dark slides (1 and 12) carry the narrative moments; light slides carry the analysis
- Categorical palette validated for colour-vision separation on the light ground:
  orange `#E8722C` · blue `#2D6FCB` · green `#0E9E5E` · purple `#7B4FD6`
- One idea per slide, full-sentence headlines, no TAM/SAM/SOM pyramid
- Every estimate is labelled as an estimate on the slide it appears on
- No use-of-funds ask beyond the ₹11.3 L runway figure on slide 11 — the brief
  specified ending on the founder and the vision
