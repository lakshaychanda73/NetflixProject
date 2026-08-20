# Brickrock Realty — 12-slide pitch deck

`out/Brickrock_Realty_Pitch_Deck.pdf` — exactly 12 slides, true 16:9 (960 × 540 pt).

Compressed from the 60-page *Mumbai Real Estate Master Playbook* in `../report/`.
The playbook is the research database; this deck is the story.

## Slide order

| # | Slide | Answers |
|---|---|---|
| 1 | The Opportunity | Why Mumbai real estate, why now |
| 2 | The Founder | Why Lakshay can execute this |
| 3 | The Vision | Brokerage → development → Jaipur |
| 4 | The Opportunity, Sized Honestly | Large market, reachable slice |
| 5 | Where We Start | Eastern & Central Suburbs |
| 6 | Why This Corridor | The 7-metric framework |
| 7 | The Scorecard | Why it beats the alternatives |
| 8 | The Operating Model | How the market gets captured |
| 9 | The Economics | Hours → transactions → revenue |
| 10 | First 90 Days | Zero to first transactions |
| 11 | Months 3 to 12 | Build the engine, then widen |
| 12 | The End Game | Mumbai → development → Jaipur |

## Attribution discipline

The founder slide separates three things visually and in the copy, and the
distinction is enforced in `build/founder.py`:

| Claim | Attribution |
|---|---|
| ₹1.08 Cr revenue, ₹17.1 L PAT, 183 invoices, 100% bootstrapped | **Lakshay's own business** (Sheesham.in) |
| @brickrockrealty, 1,055 followers, 366k top reel | **Lakshay's own presence** |
| ~310 acres | **Family inheritance** — not his personal asset |
| 124 acres + township | **His father's** land and development |

Family holdings are never presented as personal achievements.

## One item needs confirmation

`founder.py` carries `EDUCATION = ("IIM Mumbai", "INFERRED")`. This was inferred
from an "IIM MUMBAI" highlight and a pinned campus post on @brickrockrealty. It is
**not currently used on any slide.** Confirm it before adding it.

## Sources

- **Founder numbers** — Sheesham.in incubation deck (July 2026); @brickrockrealty profile (Aug 2026)
- **Market numbers** — the verified evidence base at `../build/evidence.py`, 33 registered sources
- **Model outputs** — entry model, funnel, unit economics and roadmap all read from the same evidence file as the playbook, so the deck and the report cannot disagree

## Rebuilding

```bash
cd build
python3 fig_deck.py      # -> ../figures/s*.png
python3 build_deck.py    # -> ../out/deck.html
cd ../out && chromium --headless --no-pdf-header-footer \
  --allow-file-access-from-files --print-to-pdf=Brickrock_Realty_Pitch_Deck.pdf deck.html
```

`build_deck.py` asserts the deck is exactly 12 slides and fails the build otherwise.

## Design notes

- Dark slides (1, 3, 12) carry the narrative moments; light slides carry the analysis
- Categorical palette validated for colour-vision separation on the light ground:
  orange `#E8722C` · blue `#2D6FCB` · green `#0E9E5E` · purple `#7B4FD6`
- One idea per slide, full-sentence headlines, no TAM/SAM/SOM pyramid
- No ask or use-of-funds slide — the brief specified ending on the vision. Add a
  13th slide if this is going to investors.
