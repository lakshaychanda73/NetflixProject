"""build_workbook.py — the corrected operating workbook, generated from evidence.py.

Supersedes Mumbai_Real_Estate_Operating_System.xlsx v1. Every sheet is generated,
so the workbook, the CSVs and the PDF can never disagree with one another.
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, ColorScaleRule
import evidence as E

INK, INK2, MUTED = "FF0B0B0B", "FF52514E", "FF898781"
BLUE, ORANGE, AQUA, VIOLET, MAGENTA, YELLOW = ("FF2A78D6", "FFEB6834", "FF1BAF7A",
                                               "FF4A3AA7", "FFE87BA4", "FFEDA100")
CRIT, GOOD, WARN = "FFD03B3B", "FF0CA30C", "FFFAB219"
HDR_FILL = PatternFill("solid", fgColor="FF0E1A2B")
BAND = PatternFill("solid", fgColor="FFF4F4F1")
NOTE_FILL = PatternFill("solid", fgColor="FFF2F6FD")
THIN = Side(style="thin", color="FFE1E0D9")
BORDER = Border(bottom=THIN)

F_TITLE = Font(name="Inter", size=14, bold=True, color=INK)
F_SUB = Font(name="Inter", size=9, color=INK2)
F_HDR = Font(name="Inter", size=8.5, bold=True, color="FFFFFFFF")
F_BODY = Font(name="Inter", size=9, color=INK)
F_SMALL = Font(name="Inter", size=8, color=INK2)
F_TINY = Font(name="Inter", size=7.5, color=MUTED)

WRAP = Alignment(wrap_text=True, vertical="top")
TOPL = Alignment(vertical="top", horizontal="left")


def sheet(wb, name, title, subtitle, widths, headers, rows, freeze="A5",
          number_formats=None, first=False):
    ws = wb.active if first else wb.create_sheet()
    ws.title = name
    ws.sheet_view.showGridLines = False
    ws["A1"] = title
    ws["A1"].font = F_TITLE
    ws["A2"] = subtitle
    ws["A2"].font = F_SUB
    ws.row_dimensions[1].height = 22
    ws.row_dimensions[2].height = 30
    ws["A2"].alignment = Alignment(wrap_text=True, vertical="center")
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=max(len(headers), 4))

    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

    r = 4
    for c, h in enumerate(headers, 1):
        cell = ws.cell(row=r, column=c, value=h)
        cell.font = F_HDR
        cell.fill = HDR_FILL
        cell.alignment = Alignment(wrap_text=True, vertical="center")
    ws.row_dimensions[r].height = 26

    for j, row in enumerate(rows):
        r += 1
        for c, v in enumerate(row, 1):
            cell = ws.cell(row=r, column=c, value=v)
            cell.font = F_BODY
            cell.alignment = WRAP
            cell.border = BORDER
            if j % 2:
                cell.fill = BAND
            if number_formats and c in number_formats:
                cell.number_format = number_formats[c]
    if freeze:
        ws.freeze_panes = freeze
    return ws


def build():
    wb = openpyxl.Workbook()

    # ---------------------------------------------------------- 1. README
    ws = wb.active
    ws.title = "README"
    ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width = 3
    ws.column_dimensions["B"].width = 34
    ws.column_dimensions["C"].width = 96
    ws["B2"] = "MUMBAI REAL ESTATE OPERATING SYSTEM"
    ws["B2"].font = Font(name="Inter", size=16, bold=True, color=INK)
    ws["B3"] = (f"Version {E.REPORT_VERSION} · generated {E.RESEARCH_DATE} · supersedes v1.0. "
                "Every sheet in this workbook is generated from a single evidence file, so this "
                "workbook, the CSV repository and the PDF report cannot disagree with each other.")
    ws["B3"].font = F_SUB
    ws["B3"].alignment = Alignment(wrap_text=True, vertical="top")
    ws.merge_cells("B3:C3")
    ws.row_dimensions[3].height = 30

    rows = [
        ("HOW TO USE THIS WORKBOOK", ""),
        ("Reference sheets", "Market_Snapshot, Sources, Micro_Markets, Infrastructure, "
         "Repositories, Compliance, Risk_Register, Data_Schema. Read-only reference — "
         "regenerate rather than edit."),
        ("Model sheets", "Entry_Model, Workload, Unit_Economics. The weights and assumptions are "
         "yours to change; the arithmetic updates itself."),
        ("Working sheets", "CRM_Pipeline, Deal_Underwriting, Locality_Scorecard, Data_Health. "
         "These are the ones you fill in daily."),
        ("Plan sheets", "Roadmap_90_Day, Roadmap_12_Month. Put a date against every gate as it closes."),
        ("", ""),
        ("THE FOUR RULES THIS WORKBOOK ENFORCES", ""),
        ("1 · Provenance", "No fact without source_ref + observed_date + confidence. If you cannot "
         "fill those three, you do not have a fact, you have a rumour."),
        ("2 · Area basis", "Every price declares carpet / built_up / saleable. Never compare across "
         "bases — a saleable-area price understates the true rate by 25–35%."),
        ("3 · Price type", "asking / registered / ready_reckoner / launch are four separate fields. "
         "Blending them produces a number describing no transaction that ever happened."),
        ("4 · Sample size", "Every aggregate shows n. Below the domain minimum, mark it low "
         "confidence and say so on the client-facing screen."),
        ("", ""),
        ("WHAT CHANGED FROM V1", ""),
        ("Certificate of Competency", "Mandatory since January 2026 and now the critical path. "
         "See the Compliance sheet."),
        ("Yield mechanics", "The v1 Locality_Scorecard used a 650 sq ft carpet placeholder against "
         "a ₹75,000 rent, producing 4.2–5.8% gross yields for Powai. Observed Eastern-corridor "
         "yields are 2.5–3.5%. The placeholder is now labelled and inside a plausible band."),
        ("Entry model", "One weight vector and one score table now drive the workbook, the CSVs "
         "and the report. In v1 all three disagreed."),
        ("Unsold inventory", "v1 recorded it as down 4%. It rose 4% YoY to 525,695 across the top "
         "eight markets. Mumbai holds 157,410."),
        ("New sheets", "Workload, Unit_Economics, Compliance, Risk_Register, Infrastructure, "
         "Micro_Markets — none of which existed in v1."),
        ("", ""),
        ("DISCLAIMER", "Not legal, tax or investment advice. Confirm every regulatory and tax "
         "position with a qualified professional. Every market figure carries a source id and a "
         "date — re-verify before relying on it."),
    ]
    r = 5
    for k, v in rows:
        if k and not v:
            ws.cell(row=r, column=2, value=k).font = Font(name="Inter", size=9.5, bold=True,
                                                          color=BLUE)
        elif k:
            ws.cell(row=r, column=2, value=k).font = Font(name="Inter", size=9, bold=True, color=INK)
            c = ws.cell(row=r, column=3, value=v)
            c.font = F_SMALL
            c.alignment = Alignment(wrap_text=True, vertical="top")
            ws.row_dimensions[r].height = max(14, 11 * (1 + len(v) // 95))
        r += 1

    # ---------------------------------------------------- 2. MARKET SNAPSHOT
    sheet(wb, "Market_Snapshot", "Public market snapshot",
          "Verified figures as at 14 August 2026. Every row carries its source id, the date it "
          "applies to and a confidence grade. These are published statistics, not estimates.",
          [30, 16, 16, 12, 14, 60],
          ["Metric", "Value", "Unit", "Source", "Observed", "Note"],
          [[k.replace("_", " ").title(), f.value, f.unit, f.src, f.observed, f.note]
           for k, f in E.MARKET.items()],
          number_formats={2: "#,##0.00"})

    # ------------------------------------------------------- 3. ENTRY MODEL
    keys = [k for k, _, _, _ in E.CRITERIA]
    labels = [l for _, l, _, _ in E.CRITERIA]
    ws = wb.create_sheet("Entry_Model")
    ws.sheet_view.showGridLines = False
    ws["A1"] = "Market entry priority model"
    ws["A1"].font = F_TITLE
    ws["A2"] = ("ANALYST MODEL — NOT A MARKET STATISTIC. Change the weights in row 4 to encode a "
                "different strategy; the scores and ranks recalculate. Weights must sum to 1.00 "
                "(checked in K4).")
    ws["A2"].font = F_SUB
    ws["A2"].alignment = Alignment(wrap_text=True, vertical="center")
    ws.merge_cells("A2:J2")
    ws.row_dimensions[2].height = 30
    ws.column_dimensions["A"].width = 30
    for i in range(2, 12):
        ws.column_dimensions[get_column_letter(i)].width = 13

    ws.cell(row=4, column=1, value="WEIGHTS →").font = Font(name="Inter", size=8.5, bold=True,
                                                            color=BLUE)
    for c, k in enumerate(keys, 2):
        cell = ws.cell(row=4, column=c, value=[w for kk, _, w, _ in E.CRITERIA if kk == k][0])
        cell.font = Font(name="Inter", size=9, bold=True, color=BLUE)
        cell.number_format = "0.00"
        cell.fill = NOTE_FILL
    n = len(keys)
    last = get_column_letter(1 + n)
    ws.cell(row=4, column=2 + n, value=f"=SUM(B4:{last}4)").font = Font(
        name="Inter", size=9, bold=True, color=INK)
    ws.cell(row=4, column=2 + n).number_format = "0.00"
    ws.cell(row=4, column=3 + n,
            value='=IF(ABS(SUM(B4:' + last + '4)-1)<0.001,"weights OK","WEIGHTS MUST SUM TO 1.00")'
            ).font = Font(name="Inter", size=8.5, bold=True, color=GOOD)

    hdr = ["Region"] + labels + ["Weighted score", "Rank"]
    for c, h in enumerate(hdr, 1):
        cell = ws.cell(row=5, column=c, value=h)
        cell.font = F_HDR
        cell.fill = HDR_FILL
        cell.alignment = Alignment(wrap_text=True, vertical="center")
    ws.row_dimensions[5].height = 30

    regions = [r for r, _ in E.ranked_regions()]
    for i, region in enumerate(regions):
        r = 6 + i
        ws.cell(row=r, column=1, value=region).font = F_BODY
        for c, k in enumerate(keys, 2):
            cell = ws.cell(row=r, column=c, value=E.REGION_SCORES[region][k])
            cell.font = F_BODY
            cell.alignment = Alignment(horizontal="center")
        sc = ws.cell(row=r, column=2 + n,
                     value=f"=SUMPRODUCT(B{r}:{last}{r},$B$4:${last}$4)")
        sc.font = Font(name="Inter", size=9, bold=True, color=INK)
        sc.number_format = "0.00"
        col = get_column_letter(2 + n)
        rk = ws.cell(row=r, column=3 + n,
                     value=f"=RANK({col}{r},${col}$6:${col}${5+len(regions)})")
        rk.font = Font(name="Inter", size=9, bold=True, color=BLUE)
        rk.alignment = Alignment(horizontal="center")
    ws.conditional_formatting.add(
        f"B6:{last}{5+len(regions)}",
        ColorScaleRule(start_type="num", start_value=1, start_color="FFCDE2FB",
                       end_type="num", end_value=10, end_color="FF2A78D6"))
    ws.freeze_panes = "B6"

    r = 7 + len(regions)
    ws.cell(row=r, column=1, value="Criterion rationale").font = Font(
        name="Inter", size=9.5, bold=True, color=BLUE)
    for k, l, w, note in E.CRITERIA:
        r += 1
        ws.cell(row=r, column=1, value=l).font = Font(name="Inter", size=8.5, bold=True, color=INK)
        c = ws.cell(row=r, column=2, value=note)
        c.font = F_SMALL
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=9)

    # ---------------------------------------------------------- 4. WORKLOAD
    ws = sheet(wb, "Workload", "Year-1 hour budget",
               "One founder, 55 hours a week, 52 weeks. This is a BUDGET, not a description — its "
               "purpose is to be violated visibly. Any week after month 5 with zero deal-execution "
               "hours is a week the plan has failed.",
               [26, 40] + [7] * 12 + [11],
               ["Workstream", "What it covers"] + [f"M{i}" for i in range(1, 13)] + ["Hrs/wk total"],
               [[l, d] + E.WORKLOAD[k] + [sum(E.WORKLOAD[k])]
                for k, l, _, d in E.WORKSTREAMS],
               freeze="C5")
    r = 5 + len(E.WORKSTREAMS)
    ws.cell(row=r, column=1, value="TOTAL").font = Font(name="Inter", size=9, bold=True, color=INK)
    for c in range(3, 15):
        col = get_column_letter(c)
        cell = ws.cell(row=r, column=c, value=f"=SUM({col}5:{col}{r-1})")
        cell.font = Font(name="Inter", size=9, bold=True, color=INK)
        cell.alignment = Alignment(horizontal="center")
    ws.cell(row=r, column=15, value=f"=SUM(C{r}:N{r})").font = Font(
        name="Inter", size=9, bold=True, color=INK)
    ws.conditional_formatting.add(
        f"C{r}:N{r}",
        CellIsRule(operator="greaterThan", formula=[str(E.FOUNDER_CAPACITY_HRS)],
                   fill=PatternFill("solid", fgColor="FFFDEFEF"),
                   font=Font(name="Inter", size=9, bold=True, color=CRIT)))
    ws.cell(row=r + 2, column=1,
            value=f"Capacity is {E.FOUNDER_CAPACITY_HRS} h/week. Any month total above that turns "
                  f"red — it means the plan does not fit inside a week and something must be cut, "
                  f"deliberately, now.").font = F_TINY
    ws.merge_cells(start_row=r + 2, start_column=1, end_row=r + 2, end_column=12)

    # --------------------------------------------------- 5. UNIT ECONOMICS
    ws = wb.create_sheet("Unit_Economics")
    ws.sheet_view.showGridLines = False
    ws["A1"] = "Unit economics and capital requirement"
    ws["A1"].font = F_TITLE
    ws["A2"] = ("ILLUSTRATIVE PLANNING MODEL. Change the blue input cells; everything else "
                "recalculates. Replace every assumption here with your own observations after "
                "30–50 qualified leads.")
    ws["A2"].font = F_SUB
    ws["A2"].alignment = Alignment(wrap_text=True, vertical="center")
    ws.merge_cells("A2:F2")
    ws.row_dimensions[2].height = 28
    for col, w in zip("ABCDEF", [38, 16, 12, 16, 16, 52]):
        ws.column_dimensions[col].width = w

    def block(title, r):
        c = ws.cell(row=r, column=1, value=title)
        c.font = Font(name="Inter", size=9.5, bold=True, color=BLUE)
        return r + 1

    r = block("SEGMENT MIX  (blue cells are inputs)", 4)
    for c, h in enumerate(["Segment", "Share", "Avg consideration ₹", "Commission %",
                           "Payout lag (days)", "Note"], 1):
        cell = ws.cell(row=r, column=c, value=h)
        cell.font = F_HDR
        cell.fill = HDR_FILL
        cell.alignment = Alignment(wrap_text=True, vertical="center")
    mix_start = r + 1
    for i, (seg, share, consid, rate, lag) in enumerate(E.TICKET_MIX):
        rr = mix_start + i
        ws.cell(row=rr, column=1, value=seg).font = F_BODY
        for c, v, fmt in [(2, share, "0%"), (3, consid, "#,##0"),
                          (4, rate, "0.00%"), (5, lag, "0")]:
            cell = ws.cell(row=rr, column=c, value=v)
            cell.font = Font(name="Inter", size=9, color=BLUE, bold=True)
            cell.number_format = fmt
            cell.fill = NOTE_FILL
    mix_end = mix_start + len(E.TICKET_MIX) - 1
    ws.cell(row=mix_end + 1, column=1, value="Blended").font = Font(
        name="Inter", size=9, bold=True, color=INK)
    ws.cell(row=mix_end + 1, column=2, value=f"=SUM(B{mix_start}:B{mix_end})").number_format = "0%"
    ws.cell(row=mix_end + 1, column=3,
            value=f"=SUMPRODUCT(B{mix_start}:B{mix_end},C{mix_start}:C{mix_end})"
            ).number_format = "#,##0"
    ws.cell(row=mix_end + 1, column=4,
            value=f"=SUMPRODUCT(B{mix_start}:B{mix_end},C{mix_start}:C{mix_end},"
                  f"D{mix_start}:D{mix_end})/C{mix_end+1}").number_format = "0.00%"
    for c in range(2, 5):
        ws.cell(row=mix_end + 1, column=c).font = Font(name="Inter", size=9, bold=True, color=INK)

    r = block("COST BASE", mix_end + 3)
    for c, h in enumerate(["Line item", "One-off ₹", "Monthly ₹", "", "", "Note"], 1):
        cell = ws.cell(row=r, column=c, value=h)
        cell.font = F_HDR
        cell.fill = HDR_FILL
    cost_start = r + 1
    for i, (line, one, mon, note) in enumerate(E.COST_BASE):
        rr = cost_start + i
        ws.cell(row=rr, column=1, value=line).font = F_BODY
        for c, v in [(2, one), (3, mon)]:
            cell = ws.cell(row=rr, column=c, value=v)
            cell.font = Font(name="Inter", size=9, color=BLUE, bold=True)
            cell.number_format = "#,##0"
            cell.fill = NOTE_FILL
        ws.cell(row=rr, column=6, value=note).font = F_TINY
    cost_end = cost_start + len(E.COST_BASE) - 1
    ws.cell(row=cost_end + 1, column=1, value="TOTAL").font = Font(
        name="Inter", size=9, bold=True, color=INK)
    for c, col in [(2, "B"), (3, "C")]:
        cell = ws.cell(row=cost_end + 1, column=c,
                       value=f"=SUM({col}{cost_start}:{col}{cost_end})")
        cell.font = Font(name="Inter", size=9, bold=True, color=INK)
        cell.number_format = "#,##0"

    r = block("YEAR-1 OUTCOME", cost_end + 3)
    outs = [
        ("Closures in Year 1", E.FUNNEL_STAGES[-1][2], "#,##0", True),
        ("Gross commission ₹", f"=B{r}*C{mix_end+1}*D{mix_end+1}", "#,##0", False),
        ("Operating cost ₹ (excl. drawings)", f"=(C{cost_end+1}-C{cost_start+9})*12", "#,##0", False),
        ("One-off setup ₹", f"=B{cost_end+1}", "#,##0", False),
        ("Business profit ₹", f"=B{r+1}-B{r+2}-B{r+3}", "#,##0", False),
        ("Founder hours in Year 1", int(sum(sum(v) for v in E.WORKLOAD.values()) * 52 / 12),
         "#,##0", True),
        ("Profit per founder hour ₹", f"=B{r+4}/B{r+5}", "#,##0", False),
    ]
    for i, (lab, val, fmt, is_input) in enumerate(outs):
        rr = r + i
        ws.cell(row=rr, column=1, value=lab).font = F_BODY
        cell = ws.cell(row=rr, column=2, value=val)
        cell.number_format = fmt
        cell.font = (Font(name="Inter", size=9, color=BLUE, bold=True) if is_input
                     else Font(name="Inter", size=10, bold=True, color=INK))
        if is_input:
            cell.fill = NOTE_FILL
    ws.cell(row=r + len(outs) + 1, column=1,
            value="Income tax is NOT modelled here — it depends on entity, regime and other income. "
                  "Take the business-profit figure to a CA. GST at 18% is an output tax collected "
                  "from the client, and TDS at 2% under 194H is withheld on receipt and creditable; "
                  "neither is a cost.").font = F_TINY
    ws.merge_cells(start_row=r + len(outs) + 1, start_column=1,
                   end_row=r + len(outs) + 1, end_column=6)
    ws.row_dimensions[r + len(outs) + 1].height = 26

    # ---------------------------------------------------- 6. WORKING SHEETS
    ws = sheet(wb, "CRM_Pipeline", "CRM pipeline",
               "One row per deal. Every live lead must carry a next action and a date. "
               "lost_reason is mandatory on anything marked lost — a blank lost_reason is a lesson "
               "thrown away.",
               [11, 11, 18, 15, 24, 8, 13, 30, 13, 10, 16, 16, 24, 30],
               ["Deal_ID", "Client_ID", "Lead_source", "Budget ₹", "Preferred pockets", "BHK",
                "Stage", "Next action", "Next date", "Prob %", "Expected comm ₹",
                "Weighted comm ₹", "Lost reason", "Notes"],
               [[None] * 14 for _ in range(200)],
               number_formats={4: "#,##0", 9: "yyyy-mm-dd", 10: "0%",
                               11: "#,##0", 12: "#,##0"})
    for i in range(5, 205):
        ws.cell(row=i, column=12, value=f"=IF(AND(ISNUMBER(K{i}),ISNUMBER(J{i})),K{i}*J{i},\"\")")
        ws.cell(row=i, column=12).number_format = "#,##0"
        ws.cell(row=i, column=12).font = F_BODY
    dv = DataValidation(type="list",
                        formula1='"lead,qualified,visit,negotiation,closure,lost"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f"G5:G204")
    dv2 = DataValidation(type="list",
                         formula1='"referral,existing client,co-broking,developer channel,'
                                  'whatsapp brief,search content,corporate rental,portal listing"',
                         allow_blank=True)
    ws.add_data_validation(dv2)
    dv2.add("C5:C204")

    ws = sheet(wb, "Deal_Underwriting", "Deal underwriting",
               "All-in cost, yield and EMI for a specific unit. Carpet area only. The all-in cost "
               "includes stamp duty, registration, TDS and brokerage — roughly 8% above the "
               "agreement value in Mumbai.",
               [11, 15, 15, 11, 13, 13, 12, 9, 11, 11, 13, 11, 15, 9, 8, 13, 18],
               ["Client_ID", "Budget ₹", "Agreement value ₹", "Carpet sqft", "Monthly rent ₹",
                "Maintenance/mo ₹", "Prop tax/yr ₹", "Vacancy %", "Gross yield", "Net yield",
                "All-in cost ₹", "Price/rent yrs", "Down payment %", "Interest %", "Years",
                "EMI ₹", "Decision"],
               [["C-0001", 30000000, 25000000, 650, 75000, 12000, 30000, 0.05,
                 None, None, None, None, 0.25, 0.085, 20, None, "Review / shortlist"]] +
               [[None] * 17 for _ in range(99)],
               number_formats={2: "#,##0", 3: "#,##0", 5: "#,##0", 6: "#,##0", 7: "#,##0",
                               8: "0%", 9: "0.00%", 10: "0.00%", 11: "#,##0", 12: "0.0",
                               13: "0%", 14: "0.00%", 16: "#,##0"})
    for i in range(5, 105):
        ws.cell(row=i, column=9, value=f"=IF(C{i}>0,E{i}*12/C{i},\"\")").number_format = "0.00%"
        ws.cell(row=i, column=10,
                value=f"=IF(C{i}>0,(E{i}*12*(1-H{i})-F{i}*12-G{i})/C{i},\"\")"
                ).number_format = "0.00%"
        ws.cell(row=i, column=11,
                value=f"=IF(C{i}>0,C{i}*1.07+MIN(C{i}*0.01,30000),\"\")").number_format = "#,##0"
        ws.cell(row=i, column=12, value=f"=IF(E{i}>0,C{i}/(E{i}*12),\"\")").number_format = "0.0"
        ws.cell(row=i, column=16,
                value=f"=IF(AND(C{i}>0,N{i}>0),PMT(N{i}/12,O{i}*12,-C{i}*(1-M{i})),\"\")"
                ).number_format = "#,##0"
        for c in (9, 10, 11, 12, 16):
            ws.cell(row=i, column=c).font = F_BODY
    ws.cell(row=106, column=1,
            value="All-in cost formula assumes 6% stamp duty + 1% TDS (above ₹50 lakh) + 1% "
                  "registration capped at ₹30,000. Use 5% stamp duty for a sole female owner. "
                  "Confirm current rates before quoting — see the Compliance sheet.").font = F_TINY
    ws.merge_cells("A106:K106")

    ws = sheet(wb, "Locality_Scorecard", "Locality and pocket scorecard",
               "One row per POCKET (L4), not per locality. Registered and asking prices are "
               "separate columns and must never be merged. Sample size is mandatory on every "
               "aggregate.",
               [16, 22, 14, 14, 11, 11, 13, 12, 11, 9, 9, 9, 10, 13, 13, 12],
               ["Locality", "Pocket (L4)", "Registered ₹/sqft", "Asking ₹/sqft", "Area basis",
                "Sample n", "Observed date", "2BHK rent ₹", "Gross yield", "Liquidity",
                "Infra", "Risk", "Client fit", "Source ref", "Confidence", "Overall"],
               [["Powai", "Hiranandani Gardens", 25850, 28700, "carpet", 12, "2026-08-14",
                 78000, None, 7, 8, 6, 8, "SRC-015", "medium", None],
                ["Powai", "Emerald Isle / Saki Vihar", 25850, 33000, "carpet", 8, "2026-08-14",
                 75000, None, 7, 9, 6, 8, "SRC-015", "medium", None],
                ["Powai", "IIT Powai fringe", 22400, 20810, "carpet", 5, "2026-08-14",
                 65000, None, 7, 8, 7, 6, "SRC-015", "low", None]] +
               [[None] * 16 for _ in range(120)],
               number_formats={3: "#,##0", 4: "#,##0", 8: "#,##0", 9: "0.00%"})
    for i in range(5, 128):
        ws.cell(row=i, column=9,
                value=f"=IF(AND(C{i}>0,H{i}>0),H{i}*12/(C{i}*900),\"\")").number_format = "0.00%"
        ws.cell(row=i, column=16,
                value=f"=IF(COUNT(J{i}:M{i})=4,ROUND(AVERAGE(J{i}:M{i}),1),\"\")"
                ).number_format = "0.0"
        ws.cell(row=i, column=9).font = F_BODY
        ws.cell(row=i, column=16).font = F_BODY
    dv3 = DataValidation(type="list", formula1='"carpet,built_up,saleable"', allow_blank=True)
    ws.add_data_validation(dv3); dv3.add("E5:E127")
    dv4 = DataValidation(type="list", formula1='"high,medium,low"', allow_blank=True)
    ws.add_data_validation(dv4); dv4.add("O5:O127")
    ws.conditional_formatting.add("F5:F127", CellIsRule(
        operator="lessThan", formula=["5"],
        fill=PatternFill("solid", fgColor="FFFDF8EE"),
        font=Font(name="Inter", size=9, bold=True, color="FF8A6100")))
    ws.cell(row=129, column=1,
            value="Gross yield uses a 900 sqft carpet placeholder in the divisor purely so the "
                  "formula runs — REPLACE it with the verified carpet area of the specific unit "
                  "before showing any yield to a client. A sample size below 5 is flagged amber: "
                  "publish it as low confidence or not at all.").font = F_TINY
    ws.merge_cells("A129:L129")

    ws = sheet(wb, "Data_Health", "Data health and freshness",
               "One row per fact. age_days and stale_flag compute themselves. If the stale count "
               "is rising faster than you are adding facts, the corridor is too big.",
               [12, 16, 16, 26, 14, 12, 12, 10, 12, 10, 11, 11, 34],
               ["Record_ID", "geo_id", "domain", "metric", "observed_date", "source_ref",
                "confidence", "sample n", "stale_after", "age_days", "stale?", "conflict?", "Notes"],
               [[None] * 13 for _ in range(200)],
               number_formats={5: "yyyy-mm-dd"})
    for i in range(5, 205):
        ws.cell(row=i, column=10, value=f"=IF(E{i}=\"\",\"\",TODAY()-E{i})").number_format = "0"
        ws.cell(row=i, column=11,
                value=f"=IF(OR(E{i}=\"\",I{i}=\"\"),\"\",IF(J{i}>I{i},\"STALE\",\"ok\"))")
        for c in (10, 11):
            ws.cell(row=i, column=c).font = F_BODY
    ws.conditional_formatting.add('K5:K204', CellIsRule(
        operator="equal", formula=['"STALE"'],
        fill=PatternFill("solid", fgColor="FFFDEFEF"),
        font=Font(name="Inter", size=9, bold=True, color=CRIT)))

    # ------------------------------------------------------- 7. REFERENCE
    sheet(wb, "Roadmap_90_Day", "The 90-day pilot",
          "Put a date against every gate as it closes. Do not tick a box you cannot evidence. "
          "The compliance gate at week 6 is absolute.",
          [7, 20, 34, 62, 56, 10, 14, 16],
          ["Wk", "Workstream", "Primary goal", "Output", "Gate / KPI", "Hours",
           "Status", "Date closed"],
          [[w, dict((k, l) for k, l, _, _ in E.WORKSTREAMS)[ws_], g, o, gt, h, "Not started", None]
           for w, ws_, g, o, gt, h in E.PILOT_90])

    sheet(wb, "Roadmap_12_Month", "Twelve-month schedule",
          "Every bar ends at a gate, not a date. Expansion is conditional on the corridor-1 "
          "economics repeating without the founder in every step.",
          [40, 20, 9, 9, 74, 14, 16],
          ["Workstream", "Category", "Start M", "End M", "Closing gate", "Status", "Date closed"],
          [[lab, dict((k, l) for k, l, _, _ in E.WORKSTREAMS)[w], s, e, g, "Not started", None]
           for lab, w, s, e, g in E.GANTT])

    sheet(wb, "Compliance", "Compliance obligations",
          "Criticality 3 obligations can end the venture, not merely delay it. Every row is a diary "
          "entry with a named owner and an evidence file, from week 1.",
          [38, 44, 44, 20, 14, 10, 14, 16],
          ["Obligation", "Trigger", "Cost / penalty", "Cadence", "Source", "Crit.",
           "Status", "Next due"],
          [[o, t, c, cad, s, cr, "Not started", None] for o, t, c, cad, s, cr in E.COMPLIANCE],
          number_formats={8: "yyyy-mm-dd"})

    sheet(wb, "Risk_Register", "Risk register",
          "Re-score at every decision gate. Risks 1 and 6 fall away once compliance is complete; "
          "risks 4 and 8 rise sharply the moment real money is in play.",
          [34, 10, 9, 10, 46, 56, 16],
          ["Risk", "Likelihood", "Impact", "Severity", "Early warning", "Control", "Owner phase"],
          [[r[0], r[1], r[2], r[1] * r[2], r[3], r[4], r[5]] for r in E.RISKS])

    sheet(wb, "Micro_Markets", "MMR micro-market reference",
          "CONFIDENCE: LOW. Portal asking aggregates with undeclared area basis. For corridor "
          "triage only — never for client advice. Re-derive from IGR registered instruments before "
          "any number here reaches a client.",
          [24, 18, 13, 13, 14, 11, 11, 8, 50],
          ["Micro-market", "Corridor", "Ask low ₹/sqft", "Ask high ₹/sqft", "2BHK rent ₹",
           "Yield low %", "Yield high %", "Infra", "Note"],
          [list(r) for r in E.MICRO_MARKETS],
          number_formats={3: "#,##0", 4: "#,##0", 5: "#,##0", 6: "0.0", 7: "0.0"})

    sheet(wb, "Infrastructure", "Infrastructure register",
          "Weight by what is running, not by what is announced. An asset whose target date has "
          "moved twice is downgraded a rung regardless of how prominent it is in developer marketing.",
          [30, 26, 20, 54, 16, 12, 11, 12],
          ["Asset", "Catchment", "Status", "Milestone", "Target", "Confidence", "Source", "Weight"],
          [list(r) for r in E.INFRASTRUCTURE],
          number_formats={8: "0.00"})

    sheet(wb, "Data_Schema", "Data schema",
          "Required fields are NOT NULL constraints, not documentation. A data-quality rule that "
          "depends on remembering it at 22:00 on a Friday is not a rule.",
          [16, 24, 12, 10, 78],
          ["Domain", "Phase-1 minimum fields", "Refresh", "Stale (d)", "Primary sources"],
          [[d[0], d[1], d[2], d[3], d[4]] for d in E.DOMAINS])

    sheet(wb, "Sources", "Source registry",
          "Thirty-three sources. Every fact in this workbook, the CSV repository and the PDF "
          "report resolves to one of these ids. All accessed 14 August 2026.",
          [11, 16, 42, 66, 62, 18, 12, 13],
          ["ID", "Category", "Source", "URL", "Key fact or use", "Refresh", "Confidence", "Accessed"],
          [[s[0], s[1], s[2], s[3], s[4], s[5], s[6], E.RESEARCH_DATE] for s in E.SOURCES])

    sheet(wb, "Corrections", "What changed from version 1",
          "Fourteen substantive corrections. Three are regulatory changes that post-date the "
          "original research; the rest are analytical errors, internal contradictions or material "
          "omissions.",
          [26, 56, 62, 62, 14],
          ["Area", "Version 1 position", "Version 2 position", "Why it matters", "Source"],
          [list(r) for r in E.CORRECTIONS])

    out = "../Mumbai_Real_Estate_Operating_System_v2.xlsx"
    wb.save(out)
    print(f"workbook written · {len(wb.sheetnames)} sheets · {', '.join(wb.sheetnames)}")


if __name__ == "__main__":
    build()
