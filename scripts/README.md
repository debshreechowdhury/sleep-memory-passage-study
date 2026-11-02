# Script workflow

Run from repository root. Use Python 3.10+ and requirements.txt. Data collection is manual Google Forms; no automated collection code was used. CSV header mapping is intentionally explicit rather than guessed, because duplicated question labels and revisions can swap passage columns.

1. Copy config/export_manifest.example.json to config/export_manifest.local.json. Replace the example path, exact expected header list, and zero-based column positions with a privately reviewed real export. Include one source per verified order/version. Optional absent fields must be omitted. The example is deliberately not executable against real data.
2. Run import_forms.py to discard identifiers and attach order, clean.py to score, analyze.py for core statistics. See README for commands.
3. Review all decisions before interpreting results. Current cleaning is a proposed baseline, not a registered protocol: missing comprehension is held out for review, both incorrect is excluded, quality uses complete triples, and detection uses available answers among included rows. No age or duplicate-person verification is automated. Missing AI-use/English fields are not imputed.
4. Add diagnostic plots, exact detection power and exploratory models through Kuba's substantive PR once actual data and assumptions are known. These are outstanding work, not completed analyses.
