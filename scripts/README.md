# Script workflow

Run from repository root with the `make` targets in the README. Use Python 3.10+ and requirements.txt. Data collection is manual Google Forms; no automated collection code was used. CSV header mapping is intentionally explicit rather than guessed, because duplicated question labels and revisions can swap passage columns.

| Folder | Owner | Scripts | Still to add |
|---|---|---|---|
| `data/` | Kuba | `import_forms.py`, `clean.py` | |
| `quality/` | Kuba | `power.py`, `quality.py` | `regression.py`, diagnostics and figures |
| `detection/` | Debshree | `detection.py` | `check_stimuli.py`, `power.py`, `groups.py`, figures |

The scripts at the top level of `scripts/` produced the completed report's evidence, figures and slides; [report/REPRODUCE.md](../report/REPRODUCE.md) lists how to run them. The steps below are the folder pipeline.

1. Copy config/export_manifest.example.json to config/export_manifest.local.json. Replace the example path, exact expected header list, and zero-based column positions with a privately reviewed real export kept in data/private/. Include one source per verified order/version. Optional absent fields must be omitted. The example is deliberately not executable against real data.
2. `make data` runs import_forms.py to discard identifiers and attach order, then clean.py to score. `make quality` and `make detection` run the core statistics.
3. Review all decisions before interpreting results. Current cleaning is a proposed baseline, not a registered protocol: missing comprehension is held out for review, both incorrect is excluded, quality uses complete triples, and detection uses available answers among included rows. No age or duplicate-person verification is automated. Missing AI-use/English fields are not imputed.
4. Diagnostic plots, exact detection power and exploratory models are outstanding work, not completed analyses. Their owners add them once actual data and assumptions are known.
