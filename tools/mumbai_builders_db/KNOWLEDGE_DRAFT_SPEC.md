# Knowledge-draft spec (web access is exhausted in this session – DO NOT use WebSearch or WebFetch)

The user approved this fallback: build the rest of the Mumbai/MMR developer universe from model knowledge (training data up to ~mid-2026). Every row you write will be shown in the Excel with the label **"Model knowledge – unverified"** and will be re-verified later when web access is restored. Your job is to be broad AND accurate.

## Accuracy rules (most important)
- Include a company only if you are confident it is a real developer that has been active in the MMR (projects launched/under construction 2022-2026). Add `"confidence": "High"` or `"Medium"`. Skip anything you would rate Low.
- Include a person only if you are confident of the name–company–role association. NEVER invent a person. If you know the company but not its people, write the company record only.
- Roles change: set `"role_verified": "Model knowledge (as last known, pre-mid-2026) – unverified"` and mention in notes if a role may have changed (e.g. succession to next generation).
- CONTACT DETAILS: do NOT write any email, phone number or LinkedIn URL from memory. Set `mobile`, `email`, `office_phone`, `general_email`, `cp_channel_contact` to exactly `Not verified yet` and `linkedin` to `Not found`.
- `website`: include only if you are highly confident of the exact official domain; otherwise empty string.
- `sources`: `["Model knowledge – unverified"]`.
- Do not duplicate what web researchers already verified: first read the existing `*_companies.jsonl` and `*_people.jsonl` files in the folder for your segment (read-only, never modify them). You MAY add missing people for a company that already exists in those files – use the exact same company string they used. For such companies do not write a new company record.
- If you believe a company in the existing files is wrong/defunct/insolvent, note it in your .md, don't edit their files.

## Levels (same as _SPEC.md)
L1 national/listed majors & top-tier Mumbai groups; L2 large established MMR developers (~₹750–3,000 cr/yr or ~10+ active projects); L3 mid-size regional (4–10 active projects, 1–3 micro-markets); L4 small/boutique & redevelopment/SRA specialists (1–4 active projects); L5 emerging/first-generation/single-project/new entrants; Connector = associations.

## Output (write with Python, json.dumps(ensure_ascii=False), one object per line)
Folder: /home/user/NetflixProject/research_notes/Mumbai MMR builders outreach database/
- `kb_<segment>_companies.jsonl` – fields exactly as in _SPEC.md companies schema + `"confidence"` + `"basis": "Model knowledge – unverified"`.
  Fill `geography`, `active_projects` (known projects with locations; say "as last known"), `scale_indicators`, `level_rationale`, `accessibility` (best entry point & who to approach), `notes`.
- `kb_<segment>_people.jsonl` – fields exactly as in _SPEC.md people schema + `"confidence"` + `"basis": "Model knowledge – unverified"`.
  Aim to cover Promoters/Founders, Chairman, MD/CEO, next-gen family in the business, and known heads of BD / land / redevelopment / sales / channel sales / strategy / marketing / CFO where confidently known. Give an outreach `priority` (High/Medium/Low + reason).
- `kb_<segment>.md` – short notes: what you added, confidence caveats, names you considered but skipped as low-confidence (as leads to verify later).
