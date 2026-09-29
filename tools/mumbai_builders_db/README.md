# Mumbai / MMR builders outreach database – tooling

Method and build tooling for the Mumbai/MMR builders & developers outreach database.
The database itself (names, designations and contact details of individuals) is **not**
committed here because this repository is public; it is delivered to the requester directly.

- `RESEARCH_SPEC.md` – level definitions (L1–L5, Connector), people to target, contact-detail rules
  (verbatim public sources only; no guessed or data-broker emails), and the JSONL record schema.
- `KNOWLEDGE_DRAFT_SPEC.md` – rules for the flagged, unverified knowledge-draft rows.
- `build_xlsx.py` – merges the researchers' JSONL files, de-duplicates companies (name keys,
  website domain, manual alias file) and people, tags each row's data basis, and writes the
  formatted Excel workbook (Read Me, Outreach Database, Company Directory, Connectors, Level Summary).
