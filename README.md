# Sleep and memory passage study

Paired comparison of an NIH science-news passage and an AI rewrite. Each participant rates both passages and attempts to identify the AI version. This repository contains the report and reproducible analysis of a 54-response snapshot, with 49 responses retained after the documented comprehension exclusions.

## Current evidence and remaining work

Owner sections are in [report/](report/README.md). Run `make report` to assemble `report/report.md` in the course order. Debshree’s slides and the shared theme are in [presentation/](presentation/README.md); charts and aggregate inputs all live in `results/`.

The circulated form was changed to fixed **AI first** on October 31, 2026, and published. Recruitment eligibility was broadened to adults who are students, working professionals or other. Names are optional; responses with names are identifiable. Debrief is shown after Submit and response editing is off. See [form setup](forms/google-forms.md) and [revision log](forms/REVISION_LOG.md). Live collection status and final form contents need verification; older instrument documentation is historical.

Aggregate report results are in results/report_statistics.json; raw exports are withheld because names and free text may identify participants. The completed [report](report/report.md) describes actual results, uncertainty and retrospective decisions. Power outputs are assumption-based planning scenarios.

## Reproduction

Python 3.10+; commands run from this directory:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python scripts/power.py --n 30 --output results/power_scenarios.csv
```

After obtaining authorized response exports, review the exact headers and create an ignored local manifest as described in [scripts/README.md](scripts/README.md). Example columns must be replaced; never assume they match the actual form.

```sh
python scripts/import_forms.py --manifest config/export_manifest.local.json --output data/interim/mapped.csv
python scripts/clean.py --input data/interim/mapped.csv --output data/cleaned/analysis.csv
python scripts/analyze.py --input data/cleaned/analysis.csv --output results/analysis.json
```

Raw exports stay unchanged in restricted storage. Raw/interim/cleaned CSVs are ignored by default; see [data policy and dictionary](data/README.md) for how to describe withheld data and release only approved de-identified data. Names, emails, timestamps and free text are not imported. Keep any withdrawal crosswalk separately.

See [report reproduction](report/REPRODUCE.md) for the completed snapshot analysis and [peer-review notes](report/REVIEW_NOTES.md) for outstanding team verification. Core outputs: paired composite difference, 95% CI, paired t statistic and p-value, Cohen dz, per-version Cronbach alpha; detection counts, chi-square when expected counts permit, exact binomial p-value and exact CI. Scripts report missing-data denominators and do not fabricate absent covariates or page times. The report includes distribution diagnostics, a Wilcoxon sensitivity analysis and exact detection-power scenarios. Uncollected AI-use and English measures cannot support the proposed regression.

## Report and collaboration

- [Written report](report/report.md) covers every supplied rubric section; final report is submitted via the course Byline link.
- [Work allocation and PR tracker](PROJECT_PLAN.md): Debshree works on `debshree/report-design`; Kuba on `kuba/data-analysis`.
- [Analysis plan](ANALYSIS_PLAN.md) is a draft; decisions made after launch must be dated as amendments.
- Follow [CONTRIBUTING.md](CONTRIBUTING.md) and the [PR template](.github/pull_request_template.md). Each member authors a substantive PR and the other reviews it before merging. Branch creation is not evidence of a member contribution or review.

The shared scaffold was merged in [PR #2](https://github.com/debshreechowdhury/sleep-memory-passage-study/pull/2). Member contributions are reviewed separately against main. To begin:

```sh
git fetch origin
git switch --track origin/debshree/report-design
# Kuba instead uses: git switch --track origin/kuba/data-analysis
# Make your own substantive changes, commit, push, then open a PR to main.
```

Preserve existing branches/PRs; reconcile their proposed changes with the current study before merging. Final submission includes this repository link, scripts, reproducible instructions, reviewed PR history and approved data or a clear withholding description.

## Sources

- [NIH News in Health: Sleep On It](https://newsinhealth.nih.gov/2013/04/sleep-it).
- [SciPy paired t-test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html).
- [SciPy exact binomial test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binomtest.html).

Validation data in tests are explicitly synthetic and are never analyzed as participant responses.
