"""report_css.py — print stylesheet for the master playbook (A4 landscape)."""

CSS = """
@page { size: A4 landscape; margin: 0; }

:root{
  --surface:#fcfcfb; --plane:#f4f4f1; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --grid:#e1e0d9; --base:#c3c2b7; --rule:#eceae3;
  --blue:#2a78d6; --blue-d:#184f95; --blue-l:#cde2fb; --blue-w:#f2f6fd;
  --orange:#eb6834; --aqua:#1baf7a; --yellow:#eda100; --magenta:#e87ba4;
  --green:#008300; --violet:#4a3aa7; --red:#e34948;
  --good:#0ca30c; --warn:#fab219; --serious:#ec835a; --critical:#d03b3b;
}

*{ box-sizing:border-box; }
html,body{ margin:0; padding:0; background:#fff; }
body{
  font-family:"Inter","Liberation Sans",sans-serif;
  color:var(--ink); font-size:9.6pt; line-height:1.55;
  -webkit-print-color-adjust:exact; print-color-adjust:exact;
}

.page{
  position:relative; width:297mm; height:210mm; overflow:hidden;
  page-break-after:always; break-after:page;
  background:var(--surface);
  padding:13mm 15mm 16mm 15mm;
}
.page:last-child{ page-break-after:auto; }

/* ---------- running furniture ---------- */
.runhead{
  position:absolute; top:6.5mm; left:15mm; right:15mm;
  display:flex; justify-content:space-between; align-items:baseline;
  font-size:6.6pt; letter-spacing:.10em; text-transform:uppercase;
  color:var(--muted); border-bottom:.4pt solid var(--rule); padding-bottom:2mm;
}
.runhead .sec{ font-weight:600; color:var(--ink2); }
.runfoot{
  position:absolute; bottom:6mm; left:15mm; right:15mm;
  display:flex; justify-content:space-between; align-items:baseline;
  font-size:6.6pt; color:var(--muted); border-top:.4pt solid var(--rule); padding-top:2mm;
}
.pageno{ font-variant-numeric:tabular-nums; font-weight:600; color:var(--ink2); }

/* ---------- typography ---------- */
h1,h2,h3,h4{ margin:0; font-weight:600; }
h1{ font-size:26pt; line-height:1.12; letter-spacing:-.015em; }
h2{ font-size:16pt; line-height:1.2; letter-spacing:-.01em; margin-bottom:2.5mm; }
h3{ font-size:10.5pt; line-height:1.3; margin:0 0 1.6mm 0; }
h4{ font-size:8.6pt; line-height:1.3; margin:0 0 1.2mm 0;
    text-transform:uppercase; letter-spacing:.07em; color:var(--ink2); }
p{ margin:0 0 2.6mm 0; }
.lead{ font-size:11pt; line-height:1.5; color:var(--ink2); margin-bottom:4mm; }
.deck{ font-size:9.2pt; line-height:1.5; color:var(--ink2); margin:0 0 4mm 0; max-width:250mm; }
strong{ font-weight:600; }
em{ font-style:italic; }
.small{ font-size:7.8pt; line-height:1.5; color:var(--ink2); }
.tiny{ font-size:6.9pt; line-height:1.5; color:var(--muted); }
.kicker{ font-size:7pt; letter-spacing:.14em; text-transform:uppercase;
         font-weight:700; color:var(--blue); margin-bottom:2.5mm; }

/* ---------- columns ---------- */
.cols2{ column-count:2; column-gap:9mm; column-rule:.4pt solid var(--rule); }
.cols3{ column-count:3; column-gap:8mm; column-rule:.4pt solid var(--rule); }
.cols2 > *, .cols3 > *{ break-inside:avoid; }
.nobreak{ break-inside:avoid; }

/* ---------- figure pages ---------- */
.figwrap{ text-align:center; margin:1mm 0 2.5mm 0; }
.figwrap img{ max-width:100%; max-height:132mm; object-fit:contain; }
.figwrap.tall img{ max-height:140mm; }
.figwrap.xtall img{ max-height:146mm; }
.fignote{ font-size:7.4pt; line-height:1.55; color:var(--ink2);
          column-count:2; column-gap:9mm; }

/* ---------- callouts ---------- */
.callout{ border:.7pt solid var(--blue-l); background:var(--blue-w);
          border-radius:2mm; padding:3mm 4mm; margin:0 0 3mm 0; }
.callout .h{ font-size:7.4pt; font-weight:700; letter-spacing:.08em;
             text-transform:uppercase; color:var(--blue-d); margin-bottom:1.5mm; }
.callout.warn{ border-color:#f6dfae; background:#fdf8ee; }
.callout.warn .h{ color:#8a6100; }
.callout.crit{ border-color:#f3c2c2; background:#fdefef; }
.callout.crit .h{ color:var(--critical); }
.callout.good{ border-color:#bfe6bf; background:#f0f9f0; }
.callout.good .h{ color:#0a7a0a; }

.rule{ border:0; border-top:.5pt solid var(--rule); margin:3mm 0; }

/* ---------- tables ---------- */
table{ width:100%; border-collapse:collapse; font-size:7.5pt; line-height:1.42; }
th{ text-align:left; font-weight:700; font-size:6.8pt; letter-spacing:.06em;
    text-transform:uppercase; color:var(--ink2);
    border-bottom:.8pt solid var(--base); padding:1.6mm 2mm 1.4mm 0; vertical-align:bottom; }
td{ padding:1.5mm 2mm 1.5mm 0; border-bottom:.4pt solid var(--rule); vertical-align:top; }
tr:last-child td{ border-bottom:none; }
td.num, th.num{ text-align:right; font-variant-numeric:tabular-nums; padding-right:3mm; }
.tbl-compact td, .tbl-compact th{ padding:1.1mm 2mm 1.1mm 0; }
.tbl-compact{ font-size:7pt; }
.src{ font-size:6.4pt; color:var(--muted); font-variant-numeric:tabular-nums;
      white-space:nowrap; }
code,.mono{ font-family:"Liberation Mono",monospace; font-size:6.9pt;
            background:#f2f2ef; padding:.3mm 1mm; border-radius:.8mm; color:var(--ink2); }

/* ---------- badges ---------- */
.badge{ display:inline-block; font-size:6.2pt; font-weight:700; letter-spacing:.05em;
        text-transform:uppercase; padding:.7mm 1.6mm; border-radius:1mm;
        color:#fff; vertical-align:middle; }
.b-high{ background:var(--good); } .b-med{ background:var(--warn); color:#4a3800; }
.b-low{ background:var(--serious); } .b-model{ background:var(--violet); }
.b-blue{ background:var(--blue); } .b-crit{ background:var(--critical); }

/* ---------- stat tiles ---------- */
.tiles{ display:flex; gap:3mm; margin:0 0 4mm 0; }
.tile{ flex:1; border:.7pt solid var(--base); border-radius:2mm; padding:3mm 3.5mm;
       border-left:1.6mm solid var(--blue); background:#fff; }
.tile .v{ font-size:16pt; font-weight:600; line-height:1.1; letter-spacing:-.01em; }
.tile .l{ font-size:7.2pt; color:var(--ink2); margin-top:1mm; }
.tile .d{ font-size:6.6pt; margin-top:1.2mm; font-weight:600; }

/* ---------- cover ---------- */
.cover{ background:#0e1a2b; color:#fff; padding:0; }
.cover .inner{ position:absolute; inset:0; padding:22mm 24mm; display:flex;
               flex-direction:column; justify-content:space-between; }
.cover h1{ font-size:40pt; line-height:1.06; letter-spacing:-.022em; font-weight:600; }
.cover .sub{ font-size:12.5pt; line-height:1.45; color:#a9bdd6; max-width:190mm;
             margin-top:6mm; font-weight:400; }
.cover .meta{ display:flex; gap:14mm; font-size:8pt; color:#8ea6c4; }
.cover .meta .k{ font-size:6.6pt; letter-spacing:.14em; text-transform:uppercase;
                 color:#5f7housing; }
.cover .metak{ font-size:6.4pt; letter-spacing:.14em; text-transform:uppercase;
               color:#61799a; margin-bottom:1.5mm; }
.cover .metav{ font-size:9pt; color:#dbe6f2; font-weight:500; }
.cover .eyebrow{ font-size:7.4pt; letter-spacing:.24em; text-transform:uppercase;
                 color:var(--orange); font-weight:700; }
.cover .band{ height:1.4mm; background:linear-gradient(90deg,
  var(--blue) 0%, var(--blue) 17%, var(--aqua) 17%, var(--aqua) 34%,
  var(--orange) 34%, var(--orange) 50%, var(--yellow) 50%, var(--yellow) 66%,
  var(--magenta) 66%, var(--magenta) 83%, var(--violet) 83%, var(--violet) 100%);
  margin:8mm 0; }

/* ---------- part dividers ---------- */
.divider{ background:var(--plane); }
.divider .inner{ position:absolute; inset:0; padding:26mm 24mm;
                 display:flex; flex-direction:column; justify-content:center; }
.divider .num{ font-size:64pt; font-weight:600; line-height:1;
               color:var(--blue); letter-spacing:-.03em; opacity:.22; }
.divider h1{ font-size:30pt; margin-top:-6mm; }
.divider .sub{ font-size:11.5pt; color:var(--ink2); max-width:180mm; margin-top:5mm;
               line-height:1.5; }
.divider .toc{ margin-top:9mm; column-count:2; column-gap:12mm; font-size:8.4pt;
               color:var(--ink2); max-width:210mm; }
.divider .toc div{ padding:1.3mm 0; border-top:.4pt solid var(--base);
                   break-inside:avoid; }
.divider .toc b{ color:var(--ink); font-weight:600; }

/* ---------- contents ---------- */
.tocgrid{ column-count:4; column-gap:7mm; font-size:7.1pt; }
.tocgrid .row{ padding:.7mm 0; }
.tocgrid .grp{ break-inside:avoid; margin-bottom:4mm; }
.tocgrid .grp h4{ color:var(--blue); margin-bottom:1.6mm; }
.tocgrid .row{ display:flex; justify-content:space-between; gap:2mm;
               padding:.85mm 0; border-bottom:.35pt solid var(--rule); }
.tocgrid .row span:last-child{ color:var(--muted); font-variant-numeric:tabular-nums; }

/* ---------- misc ---------- */
ul,ol{ margin:0 0 2.6mm 0; padding-left:4.5mm; }
li{ margin-bottom:1.3mm; }
ul.tight li{ margin-bottom:.7mm; }
ul.clean{ list-style:none; padding-left:0; }
ul.clean li{ padding-left:4mm; position:relative; }
ul.clean li:before{ content:"—"; position:absolute; left:0; color:var(--base); }
.q{ font-size:11pt; line-height:1.45; font-weight:500; color:var(--ink);
    border-left:1.2mm solid var(--blue); padding-left:4mm; margin:0 0 4mm 0; }
.grid2{ display:grid; grid-template-columns:1fr 1fr; gap:4mm 7mm; }
.grid3{ display:grid; grid-template-columns:1fr 1fr 1fr; gap:4mm 6mm; }
.grid4{ display:grid; grid-template-columns:repeat(4,1fr); gap:3mm 5mm; }
.box{ border:.6pt solid var(--grid); border-radius:2mm; padding:3mm 3.5mm; background:#fff; }
.box h4{ color:var(--blue); }
.box.o h4{ color:var(--orange); } .box.a h4{ color:var(--aqua); }
.box.v h4{ color:var(--violet); } .box.y h4{ color:#9a6a00; }
.box.r h4{ color:var(--critical); } .box.g h4{ color:#0a7a0a; }
"""
