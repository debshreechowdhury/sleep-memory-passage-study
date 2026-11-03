# Sleep and memory passage study

Paired comparison of an NIH science-news passage and an AI rewrite. Each participant rates both passages and attempts to identify the AI version. The main question is whether international and domestic students differ in identifying the AI version. The November 2 workbook has 64 responses, and 26 students remain after the documented exclusions.

## Hypotheses

| | Question | H0 | Test | Status |
|---|---|---|---|---|
| **H1** | Do international and domestic students differ in identifying the AI passage? | The proportion correct is equal in both groups | Fisher's exact | Main question |
| **H2** | Do students rate the original and the AI rewrite differently? | The mean original-minus-AI quality difference is 0 | Paired t-test | Secondary |
| **H3** | Do students identify the AI passage better or worse than chance? | The proportion correct is 50% | Chi-square goodness-of-fit | Secondary |

All tests are two-sided at .05/3 = .0167. The group comparison, its H0 and its test were written down before collection, and that plan labelled it exploratory; we report it first because it is our main interest. Because the AI passage was always second, a correct answer always means choosing Passage 2. Results are in `results/quality/hypothesis_tests.json`.

## Current evidence and remaining work

Report sections are in [report/](report/README.md). Run `make report` to assemble `report/report.md` in the course order. Debshree’s slides and the shared theme are in [presentation/](presentation/README.md); charts and aggregate inputs all live in `results/`.

The team confirms that the form used for collection presented the original as Passage 1 and the AI rewrite as Passage 2 from the start; earlier documentation recorded the reverse because a team member mixed up the passages. Recruitment changes were published on October 31, 2026. Recruitment eligibility was broadened to adults who are students, working professionals or other. Names are optional; responses with names are identifiable. Debrief is shown after Submit and response editing is off. See [form setup](study/google_forms.md) and [revision log](study/revision_log.md). Live collection status and final form contents need verification; older instrument documentation is historical.

The report's results are in `results/quality/`. De-identified data are in `data/raw/` and `data/clean/`; original exports are withheld because names and free text may identify participants. The completed [report](report/report.md) describes actual results, uncertainty and retrospective decisions. Power outputs are assumption-based planning scenarios.

## Reproduction

Use Python 3.10 to 3.13, which the pinned packages require; the current results were run on 3.13. Commands run from this directory:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-report.txt
make test
make analysis    # results, figures, slides and report from the committed de-identified data
make check       # checks report numbers against the results
```

Rebuilding the de-identified data needs the private workbook, so most readers can skip this step.

After obtaining authorized response exports, review the exact headers and create an ignored local manifest as described in [scripts/README.md](scripts/README.md). Example columns must be replaced; never assume they match the actual form.

```sh
make data        # original export in data/private/ -> data/raw/responses_deidentified.csv -> data/clean/analysis.csv
make quality     # results/quality/quality.json
make detection   # results/detection/detection.json
make report      # report/report.md
```

Original exports stay unchanged in restricted storage and in the ignored `data/private/` folder. Git only accepts the two de-identified files, which the team chose to commit; see [data policy and dictionary](data/README.md). Names, emails, timestamps and free text are not imported. Keep any withdrawal crosswalk separately.

See [report reproduction](report/REPRODUCE.md) for the completed snapshot analysis and [peer-review notes](report/REVIEW_NOTES.md) for outstanding team verification. Core outputs: paired composite difference, 95% CI, paired t statistic and p-value, Cohen dz, item-level tests and correlations; detection counts, chi-square when expected counts permit, Fisher's exact test for the group comparison. Scripts report missing-data denominators and do not fabricate absent covariates or page times. The report includes distribution diagnostics, a Wilcoxon sensitivity analysis and exact detection-power scenarios. Uncollected AI-use and English measures cannot support the proposed regression.

## Repository layout

| Folder | Contents | Owner |
|---|---|---|
| `config/`, `data/`, `scripts/data/` | Export mapping, data files, import and cleaning | Kuba |
| `scripts/quality/`, `results/quality/` | Rating analysis (H2), regression, and the three hypothesis tests | Kuba |
| `study/` | Instrument, form records, stimulus archive | Debshree |
| `scripts/detection/`, `results/detection/` | Group comparison (H1) and overall detection (H3) | Debshree |
| Top level of `scripts/` and `results/` | Analysis, figures and slide builder behind the completed report | Both |
| `report/sections/` | Report sections in the course's required order | Both |
| `presentation/` | One deck per part, and the combined `final.pptx` | Both |
| `docs/` | Analysis plan and work plan | Both |
| `tests/` | Tests by owner, plus labeled synthetic data in `tests/fixtures/` | Both |

[CONTRIBUTING.md](CONTRIBUTING.md) has the full ownership list and project rules.

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
- [SciPy Fisher's exact test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.fisher_exact.html).

Validation data in tests are explicitly synthetic and are never analyzed as participant responses.
