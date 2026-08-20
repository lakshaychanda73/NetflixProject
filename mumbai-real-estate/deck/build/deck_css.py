"""deck_css.py — 16:9 slide stylesheet for the Brickrock Realty pitch deck."""

CSS = """
@page { size: 338.667mm 190.5mm; margin: 0; }

:root{
  --light:#FAFAF7; --dark:#0F1621; --dark2:#18202D; --card:#FFFFFF; --cardalt:#F2F1EC;
  --ink:#10131A; --ink2:#4C5361; --muted:#8C93A0; --hair:#E4E3DC; --rule:#CFCEC5;
  --dink:#FFFFFF; --dink2:#A9B4C4; --dmuted:#6B7889; --dhair:#242E3D;
  --orange:#E8722C; --orange-d:#B8511A; --blue:#2D6FCB; --green:#0E9E5E; --purple:#7B4FD6;
  --good:#0E9E5E; --warn:#E0A32E; --bad:#C93F2E;
}

*{ box-sizing:border-box; }
html,body{ margin:0; padding:0; background:#fff; }
body{
  font-family:"Inter","Liberation Sans",sans-serif;
  color:var(--ink); font-size:11pt; line-height:1.5;
  -webkit-print-color-adjust:exact; print-color-adjust:exact;
}

.slide{
  position:relative; width:338.667mm; height:190.5mm; overflow:hidden;
  page-break-after:always; break-after:page;
  background:var(--light); padding:15mm 17mm 13mm 17mm;
}
.slide:last-child{ page-break-after:auto; }
.slide.dark{ background:var(--dark); color:var(--dink); }

/* ---------- furniture ---------- */
.num{ position:absolute; top:11mm; right:17mm; font-size:8pt; font-weight:700;
      color:var(--muted); letter-spacing:.08em; }
.dark .num{ color:var(--dmuted); }
.brand{ position:absolute; bottom:8mm; left:17mm; font-size:7.4pt; font-weight:700;
        letter-spacing:.16em; color:var(--muted); }
.dark .brand{ color:var(--dmuted); }
.foot{ position:absolute; bottom:8mm; right:17mm; font-size:6.8pt; color:var(--muted);
       max-width:210mm; text-align:right; }
.dark .foot{ color:var(--dmuted); }

/* ---------- type ---------- */
.eyebrow{ font-size:7.6pt; font-weight:800; letter-spacing:.20em; text-transform:uppercase;
          color:var(--orange); margin-bottom:4mm; }
h1{ margin:0; font-size:30pt; line-height:1.1; letter-spacing:-.022em; font-weight:700; }
h2{ margin:0; font-size:21pt; line-height:1.15; letter-spacing:-.018em; font-weight:700; }
h3{ margin:0 0 2mm 0; font-size:11.5pt; line-height:1.25; font-weight:700; }
h4{ margin:0 0 1.6mm 0; font-size:7.6pt; font-weight:800; letter-spacing:.12em;
    text-transform:uppercase; color:var(--muted); }
.dark h4{ color:var(--dmuted); }
.sub{ margin:4mm 0 0 0; font-size:12pt; line-height:1.45; color:var(--ink2); max-width:210mm; }
.dark .sub{ color:var(--dink2); }
.body{ font-size:9.4pt; line-height:1.6; color:var(--ink2); }
.dark .body{ color:var(--dink2); }
.small{ font-size:8.2pt; line-height:1.55; color:var(--ink2); }
.dark .small{ color:var(--dink2); }
.tiny{ font-size:7pt; line-height:1.5; color:var(--muted); }
.dark .tiny{ color:var(--dmuted); }
strong{ font-weight:700; color:var(--ink); }
.dark strong{ color:var(--dink); }
.hl{ color:var(--orange); font-weight:700; }

/* ---------- title block ---------- */
.head{ margin-bottom:6mm; }
.head h2{ max-width:250mm; }
.head .kick{ font-size:7.6pt; font-weight:800; letter-spacing:.18em; text-transform:uppercase;
             color:var(--orange); margin-bottom:3mm; }
.head .lede{ margin-top:3mm; font-size:10.5pt; line-height:1.45; color:var(--ink2);
             max-width:238mm; }
.dark .head .lede{ color:var(--dink2); }

/* ---------- layout ---------- */
.row{ display:flex; gap:7mm; }
.col{ flex:1; min-width:0; }
.grid2{ display:grid; grid-template-columns:1fr 1fr; gap:6mm; }
.grid3{ display:grid; grid-template-columns:1fr 1fr 1fr; gap:6mm; }
.grid4{ display:grid; grid-template-columns:repeat(4,1fr); gap:5mm; }
.grid5{ display:grid; grid-template-columns:repeat(5,1fr); gap:4mm; }

/* ---------- figures ---------- */
.fig{ text-align:center; }
.fig img{ max-width:100%; display:block; margin:0 auto; }
.fig.c100 img{ max-height:100mm; }
.fig.c104 img{ max-height:104mm; }
.fig.c112 img{ max-height:112mm; }
.fig.c62 img{ max-height:62mm; }

/* ---------- stat tiles ---------- */
.stat{ background:var(--card); border:0.8pt solid var(--hair); border-radius:2.4mm;
       padding:4.5mm 5mm; border-left:1.8mm solid var(--orange); }
.dark .stat{ background:var(--dark2); border-color:var(--dhair); }
.stat .v{ font-size:20pt; font-weight:700; line-height:1.05; letter-spacing:-.02em; }
.stat .l{ font-size:8.2pt; color:var(--ink2); margin-top:1.8mm; line-height:1.35; }
.dark .stat .l{ color:var(--dink2); }
.stat .d{ font-size:7.2pt; margin-top:1.4mm; font-weight:700; color:var(--good); }
.stat.b{ border-left-color:var(--blue); } .stat.g{ border-left-color:var(--green); }
.stat.p{ border-left-color:var(--purple); } .stat.n{ border-left-color:var(--rule); }

/* ---------- cards ---------- */
.card{ background:var(--card); border:0.8pt solid var(--hair); border-radius:2.4mm;
       padding:5mm 5.5mm; }
.dark .card{ background:var(--dark2); border-color:var(--dhair); }
.card.tint{ background:var(--cardalt); }
.dark .card.tint{ background:#141D2B; border-color:var(--dhair); }
.card .rule{ height:1mm; margin:-5mm -5.5mm 4mm -5.5mm; border-radius:2.4mm 2.4mm 0 0; }
.card h3{ font-size:10.5pt; }

/* ---------- lists ---------- */
ul{ margin:0; padding-left:0; list-style:none; }
li{ position:relative; padding-left:4.6mm; margin-bottom:2.2mm; font-size:8.6pt;
    line-height:1.5; color:var(--ink2); }
.dark li{ color:var(--dink2); }
li:before{ content:""; position:absolute; left:0; top:1.7mm; width:1.5mm; height:1.5mm;
           border-radius:50%; background:var(--orange); }
li.b:before{ background:var(--blue); } li.g:before{ background:var(--green); }
li.p:before{ background:var(--purple); } li.n:before{ background:var(--rule); }
ul.tight li{ margin-bottom:1.4mm; font-size:8.2pt; }

/* ---------- chips ---------- */
.chip{ display:inline-block; font-size:6.8pt; font-weight:800; letter-spacing:.08em;
       text-transform:uppercase; padding:1.1mm 2.4mm; border-radius:6mm; color:#fff;
       background:var(--orange); }
.chip.b{ background:var(--blue); } .chip.g{ background:var(--green); }
.chip.p{ background:var(--purple); } .chip.n{ background:var(--muted); }
.chip.o-out{ background:transparent; color:var(--orange); border:0.8pt solid var(--orange); }

/* ---------- callout ---------- */
.note{ border-left:1.4mm solid var(--orange); padding:2mm 0 2mm 4.5mm;
       font-size:9pt; line-height:1.5; color:var(--ink2); }
.dark .note{ color:var(--dink2); }
.note.b{ border-left-color:var(--blue); } .note.g{ border-left-color:var(--green); }

/* ---------- attribution bar (founder slide) ---------- */
.attr{ display:flex; gap:2.4mm; align-items:baseline; flex-wrap:wrap; font-size:6.8pt;
       color:var(--muted); margin-top:2.8mm; line-height:1.5; }
.attr .tag{ font-weight:800; letter-spacing:.08em; text-transform:uppercase;
            padding:.8mm 2mm; border-radius:1mm; background:var(--cardalt); color:var(--ink2);
            white-space:nowrap; }
.attr .tag.own{ background:#FDEDE2; color:var(--orange-d); }
.attr .tag.fam{ background:#EDF1F8; color:var(--blue); }

/* ---------- cover ---------- */
.cover{ display:flex; flex-direction:column; justify-content:space-between; }
.cover h1{ font-size:44pt; letter-spacing:-.03em; }
.cover .tag{ font-size:13pt; color:var(--dink2); margin-top:7mm; max-width:200mm;
             line-height:1.45; }
.band{ height:1.6mm; width:64mm; background:linear-gradient(90deg,
       var(--orange) 0 25%, var(--blue) 25% 50%, var(--green) 50% 75%, var(--purple) 75% 100%);
       margin-bottom:8mm; }

/* ---------- photographs ---------- */
.photo{ position:relative; overflow:hidden; border-radius:2.4mm; background:var(--cardalt); }
.dark .photo{ background:var(--dark2); }
.photo img{ display:block; width:100%; height:100%; object-fit:cover; }
.photo.wide{ width:100%; height:23mm; margin-bottom:4.5mm; }
.photo.rail{ height:100%; }
.photo.port{ width:100%; }
.photo .cap{ position:absolute; left:0; right:0; bottom:0; padding:3mm 4mm 2.4mm 4mm;
             font-size:6.6pt; font-weight:700; letter-spacing:.10em; text-transform:uppercase;
             color:#fff; background:linear-gradient(180deg, rgba(15,22,33,0) 0%,
             rgba(15,22,33,.82) 68%, rgba(15,22,33,.92) 100%); }
.photo .cap em{ font-style:normal; font-weight:500; letter-spacing:.02em;
                text-transform:none; color:rgba(255,255,255,.78); }
"""
