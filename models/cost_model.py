#!/usr/bin/env python3
"""
Cost, affordability and return model for the Hines x Sumitomo Chandivali/Powai project.

Every default below is an ASSUMPTION drawn from the Master Report. Change the ones you
can replace with the developer's written cost sheet, then re-run.

    python3 models/cost_model.py                 # full report at the default Rs 55,000/sqft
    python3 models/cost_model.py --rate 52000    # sensitivity
    python3 models/cost_model.py --female        # 5% stamp duty
"""
import argparse

# ── ASSUMPTIONS ───────────────────────────────────────────────────────────────
STAMP_MALE, STAMP_FEMALE = 0.06, 0.05      # [V] Mumbai, 2026
REG_PCT, REG_CAP = 0.01, 30_000            # [V]
GST_PCT = 0.05                             # [V] under-construction, no ITC
CLUB_INFRA = 1_500_000                     # [E] get the real number: Part 10 Q.31
MAINT_PSF_MONTH, MAINT_MONTHS = 10, 24     # [E]
CORPUS_PSF = 150                           # [E]
METERS = 250_000                           # [E]
LEGAL_DOC = 75_000                         # [E]
SOCIETY = 100_000                          # [E]
LOAN_LTV, LOAN_RATE, LOAN_YEARS = 0.75, 7.5, 20   # [V] rate band 7.10-7.75
EXIT_FEE = 0.02                            # [E] brokerage on resale

UNITS = [  # (label, RERA carpet sq ft, deck sq ft)   [S] from the partner briefing
    ("3 BHK standard A", 1120, 55),
    ("3 BHK standard B", 1180, 55),
    ("3 BHK large",      1560, 200),
    ("4 BHK standard",   1740, 200),
    ("4 BHK XL",         2360, 200),
]


def cr(x):  return f"Rs {x/1e7:,.2f} Cr"
def lk(x):  return f"Rs {x/1e5:,.2f} L"


def cost_sheet(carpet, rate, female=False, floor_rise=0, view_premium=0):
    agreement = carpet * rate + floor_rise + view_premium
    stamp = agreement * (STAMP_FEMALE if female else STAMP_MALE)
    reg = min(REG_CAP, agreement * REG_PCT)
    gst = agreement * GST_PCT
    other = {
        "Club / infrastructure":  CLUB_INFRA,
        "Advance maintenance":    carpet * MAINT_PSF_MONTH * MAINT_MONTHS,
        "Corpus / sinking fund":  carpet * CORPUS_PSF,
        "Meters & deposits":      METERS,
        "Legal & documentation":  LEGAL_DOC,
        "Society formation":      SOCIETY,
    }
    all_in = agreement + stamp + reg + gst + sum(other.values())
    return dict(carpet=carpet, rate=rate, agreement=agreement, stamp=stamp, reg=reg,
                gst=gst, other=other, other_total=sum(other.values()),
                all_in=all_in, eff_psf=all_in / carpet,
                loading=100 * (all_in / (carpet * rate) - 1))


def emi(principal, annual_rate, years):
    r = annual_rate / 12 / 100
    n = years * 12
    return principal * r * (1 + r) ** n / ((1 + r) ** n - 1)


def breakeven_cagr(sheet, years):
    """Resale CAGR on the headline rate needed to recover all-in cost after exit fee."""
    needed = sheet["all_in"] / (1 - EXIT_FEE)
    return ((needed / sheet["agreement"]) ** (1 / years) - 1) * 100


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rate", type=int, default=55000)
    ap.add_argument("--female", action="store_true", help="5%% stamp duty")
    a = ap.parse_args()

    print(f"\n{'='*104}\nALL-IN COST LADDER  @ Rs {a.rate:,}/sq ft carpet"
          f"   (stamp duty {'5% female' if a.female else '6% male'})\n{'='*104}")
    print(f"{'UNIT':<20}{'CARPET':>8}{'AGREEMENT':>14}{'SD+REG':>12}{'GST':>12}"
          f"{'OTHER':>12}{'ALL-IN':>14}{'EFF/SQFT':>11}{'LOAD':>7}")
    sheets = []
    for label, carpet, _deck in UNITS:
        s = cost_sheet(carpet, a.rate, a.female); sheets.append((label, s))
        print(f"{label:<20}{carpet:>8}{s['agreement']:>14,.0f}{s['stamp']+s['reg']:>12,.0f}"
              f"{s['gst']:>12,.0f}{s['other_total']:>12,.0f}{s['all_in']:>14,.0f}"
              f"{s['eff_psf']:>11,.0f}{s['loading']:>6.1f}%")

    print(f"\n{'='*104}\nAFFORDABILITY   loan {LOAN_LTV:.0%} LTV @ {LOAN_RATE}% for "
          f"{LOAN_YEARS} yrs\n{'='*104}")
    print(f"{'UNIT':<20}{'ALL-IN':>12}{'LOAN':>12}{'EMI/MONTH':>14}"
          f"{'NET INCOME @45% FOIR':>24}{'CASH NEEDED':>14}")
    for label, s in sheets:
        loan = s["agreement"] * LOAN_LTV
        e = emi(loan, LOAN_RATE, LOAN_YEARS)
        cash = s["all_in"] - loan
        print(f"{label:<20}{cr(s['all_in']):>12}{cr(loan):>12}{lk(e):>14}"
              f"{lk(e/0.45):>24}{cr(cash):>14}")

    print(f"\n{'='*104}\nINVESTMENT REALITY\n{'='*104}")
    print(f"{'UNIT':<20}{'YIELD @Rs85':>13}{'@Rs110':>10}{'@Rs135':>10}"
          f"{'BE-CAGR 5y':>13}{'7y':>8}{'10y':>8}")
    for label, s in sheets:
        ys = [s["carpet"] * r * 12 / s["all_in"] * 100 for r in (85, 110, 135)]
        print(f"{label:<20}{ys[0]:>12.2f}%{ys[1]:>9.2f}%{ys[2]:>9.2f}%"
              f"{breakeven_cagr(s,5):>12.2f}%{breakeven_cagr(s,7):>7.2f}%"
              f"{breakeven_cagr(s,10):>7.2f}%")
    print("\n  Powai micro-market average yield: 3.0-3.5% [V].  This asset yields BELOW it.")
    print("  Historical Powai/Hiranandani CAGR: 3.50% (10y) / 4.96% (5y) / 5.85% (3y) [V].")

    print(f"\n{'='*104}\n7-YEAR EXIT SCENARIOS  (net of a {EXIT_FEE:.0%} exit fee)\n{'='*104}")
    label, s = sheets[0]
    print(f"  Base: {label}, all-in {cr(s['all_in'])}, entry Rs {a.rate:,}/sqft, "
          f"effective Rs {s['eff_psf']:,.0f}/sqft")
    for g in (0.03, 0.05, 0.07, 0.09, 0.12):
        px = a.rate * (1 + g) ** 7
        net = px * s["carpet"] * (1 - EXIT_FEE)
        flag = "  <-- PLAN AROUND THIS" if g == 0.05 else ""
        print(f"    CAGR {g:>5.0%}  ->  Rs {px:>8,.0f}/sqft   net {cr(net):>12}   "
              f"{net/s['all_in']:.2f}x on all-in{flag}")

    print(f"\n{'='*104}\nCHANNEL PARTNER ECONOMICS\n{'='*104}")
    avg = sum(s["agreement"] for _, s in sheets) / len(sheets)
    print(f"  Average agreement value across the mix: {cr(avg)}")
    print(f"  {'SLAB':<8}{'PER UNIT':>14}{'6 UNITS':>14}{'8 UNITS':>14}{'10 UNITS':>14}")
    for pct in (0.010, 0.015, 0.020):
        print(f"  {pct:<8.1%}{lk(avg*pct):>14}{cr(6*avg*pct):>14}"
              f"{cr(8*avg*pct):>14}{cr(10*avg*pct):>14}")
    print(f"\n  The gap between a 1.0% and a 2.0% slab over 8 units is "
          f"{cr(8*avg*0.01)}. Negotiate properly.")
    print("  Note: 18% GST on brokerage; 2% TDS u/s 194H deducted by the payer. [V]\n")


if __name__ == "__main__":
    main()
