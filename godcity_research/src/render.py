import os, sys
from playwright.sync_api import sync_playwright

HTML = os.path.abspath("report.html")
OUT  = sys.argv[1] if len(sys.argv) > 1 else "God_City_Sindhudurg_Research_Report.pdf"

FOOT = """
<div style="width:100%;font-family:'DejaVu Sans',Arial,sans-serif;font-size:7pt;
            color:#8A948F;padding:0 16mm;-webkit-print-color-adjust:exact;">
  <div style="border-top:0.5pt solid #D8D2C6;padding-top:2.2mm;
              display:flex;justify-content:space-between;align-items:baseline;">
    <span>God City, Sindhudurg &nbsp;·&nbsp; project and promoter research report &nbsp;·&nbsp; February 2026</span>
    <span style="color:#0E3B39;font-weight:bold;font-size:8pt;">
      <span class="pageNumber"></span> / <span class="totalPages"></span>
    </span>
  </div>
</div>"""
HEAD = "<div style='display:none'></div>"

with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
                           args=["--no-sandbox", "--disable-gpu"])
    pg = b.new_page()
    pg.goto("file://" + HTML, wait_until="networkidle")
    pg.emulate_media(media="print")
    pg.pdf(path=OUT, width="297mm", height="420mm", print_background=True,
           display_header_footer=True, header_template=HEAD, footer_template=FOOT,
           margin={"top": "18mm", "right": "16mm", "bottom": "20mm", "left": "16mm"},
           prefer_css_page_size=False)
    b.close()
print("wrote", OUT, os.path.getsize(OUT), "bytes")
