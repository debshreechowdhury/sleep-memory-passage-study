# Script workflow

Run from repository root with the `make` targets in the README. Use Python 3.10+ and requirements.txt. Data collection is manual Google Forms; no automated collection code was used. CSV header mapping is intentionally explicit rather than guessed, because duplicated question labels and revisions can swap passage columns.

| Folder | Owner | Scripts | Still to add |
|---|---|---|---|
| `data/` | Kuba | `xlsx_to_csv.py`, `import_forms.py`, `clean.py` | |
| `quality/` | Kuba | `power.py`, `quality.py`, `hypothesis_tests.py`, `regression.py`, `figures.py`, `build_slides.py`, `check_quality.py` | |
| `detection/` | Debshree | `detection.py`, `build_design_slides.py` | `check_stimuli.py` |

The scripts at the top level of `scripts/` produced the earlier 54-response snapshot, which the report keeps as a sensitivity analysis; [report/REPRODUCE.md](../report/REPRODUCE.md) lists how to run them. The steps below are the folder pipeline.

1. Copy config/export_manifest.example.json to config/export_manifest.local.json. Replace the example path and exact expected header list with those of a privately reviewed real export kept in data/private/, and confirm the zero-based column positions; the example has the positions of the current form. Include one source per verified order/version. Optional absent fields must be omitted. The example is deliberately not executable against real data.
2. `make data` converts the private workbook with xlsx_to_csv.py, runs import_forms.py to discard identifiers and attach order, then clean.py to score and apply the study rule. `make quality` and `make detection` run the core statistics.
3. Review all decisions before interpreting results. Current cleaning is retrospective, not a registered protocol: missing comprehension is held out for review, non-students and anyone with a wrong check are excluded, quality uses complete triples, and detection uses available answers among included rows. No age or duplicate-person verification is automated. Missing AI-use/English fields are not imputed.
4. Diagnostic plots, exact detection power and exploratory models are outstanding work, not completed analyses. Their owners add them once actual data and assumptions are known.
