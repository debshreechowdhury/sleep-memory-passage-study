# Sleep and memory passage study

Paired comparison of an NIH science-news passage and an AI rewrite. Each participant rates both passages and attempts to identify the AI version. This repository contains the report and reproducible analysis of a 54-response snapshot, with 49 responses retained after the documented comprehension exclusions.

## Current evidence and remaining work

Report sections are in [report/](report/README.md). Run `make report` to assemble `report/report.md` in the course order. Debshree’s slides and the shared theme are in [presentation/](presentation/README.md); charts and aggregate inputs all live in `results/`.

The circulated form was changed to fixed **AI first** on October 31, 2026, and published. Recruitment eligibility was broadened to adults who are students, working professionals or other. Names are optional; responses with names are identifiable. Debrief is shown after Submit and response editing is off. See [form setup](study/google_forms.md) and [revision log](study/revision_log.md). Live collection status and final form contents need verification; older instrument documentation is historical.

Aggregate report results are in results/report_statistics.json; raw exports are withheld because names and free text may identify participants. The completed [report](report/report.md) describes actual results, uncertainty and retrospective decisions. Power outputs are assumption-based planning scenarios.

## Reproduction

Python 3.10+; commands run from this directory:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
make test
make power
```

After obtaining authorized response exports, review the exact headers and create an ignored local manifest as described in [scripts/README.md](scripts/README.md). Example columns must be replaced; never assume they match the actual form.

```sh
make data        # original export in data/private/ -> data/raw/responses_deidentified.csv -> data/clean/analysis.csv
make quality     # results/quality/quality.json
make detection   # results/detection/detection.json
make report      # report/report.md
```

Original exports stay unchanged in restricted storage and in the ignored `data/private/` folder. Git only accepts the two de-identified files, and they should be committed only after the team confirms sharing is permitted; see [data policy and dictionary](data/README.md). Names, emails, timestamps and free text are not imported. Keep any withdrawal crosswalk separately.

See [report reproduction](report/REPRODUCE.md) for the completed snapshot analysis and [peer-review notes](report/REVIEW_NOTES.md) for outstanding team verification. Core outputs: paired composite difference, 95% CI, paired t statistic and p-value, Cohen dz, item-level tests and correlations; detection counts, chi-square when expected counts permit, exact binomial p-value and exact CI. Scripts report missing-data denominators and do not fabricate absent covariates or page times. The report includes distribution diagnostics, a Wilcoxon sensitivity analysis and exact detection-power scenarios. Uncollected AI-use and English measures cannot support the proposed regression.

## Repository layout

| Folder | Contents | Owner |
|---|---|---|
| `config/`, `data/`, `scripts/data/` | Export mapping, data files, import and cleaning | Kuba |
| `scripts/quality/`, `results/quality/` | Rating analysis (H1) and regression | Kuba |
| `study/` | Instrument, form records, stimulus archive | Debshree |
| `scripts/detection/`, `results/detection/` | Detection (H2), group comparisons (H3) | Debshree |
| Top level of `scripts/` and `results/` | Analysis, figures and slide builder behind the completed report | Both |
| `report/sections/` | Report sections in the course's required order | Both |
| `presentation/` | One deck per part, combined at the end | Both |
| `docs/` | Analysis plan and work plan | Both |
| `tests/` | Tests by owner, plus labeled synthetic data in `tests/fixtures/` | Both |

[AGENTS.md](AGENTS.md) has the full ownership list and the rules AI tools follow.

## Report and collaboration

- [Written report](report/report.md) covers every supplied rubric section; final report is submitted via the course Byline link.
- [Work allocation and PR tracker](docs/project_plan.md).
- [Analysis plan](docs/analysis_plan.md) is a draft; decisions made after launch must be dated as amendments.
- Follow [CONTRIBUTING.md](CONTRIBUTING.md) and the [PR template](.github/pull_request_template.md). Each member authors a substantive PR and the other reviews it before merging. Branch creation is not evidence of a member contribution or review.

The shared scaffold was merged in [PR #2](https://github.com/debshreechowdhury/sleep-memory-passage-study/pull/2). Member contributions are reviewed separately against main.

Preserve existing branches/PRs; reconcile their proposed changes with the current study before merging. Final submission includes this repository link, scripts, reproducible instructions, reviewed PR history and approved data or a clear withholding description.

## Sources

- [NIH News in Health: Sleep On It](https://newsinhealth.nih.gov/2013/04/sleep-it).
- [SciPy paired t-test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html).
- [SciPy exact binomial test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binomtest.html).

Validation data in tests are explicitly synthetic and are never analyzed as participant responses.
