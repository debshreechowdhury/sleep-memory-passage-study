# Written report coverage

The assembled `report.md` and its Word copy contain the following course requirements. This checklist documents content coverage; it is not an instructor grade or a claim of human approval.

| Requirement | Location and evidence |
|---|---|
| Title and abstract | Opening title, authors, course and abstract; states the sample, principal estimates and limits |
| Background and motivation | Science-writing context, prior human-identification studies, specific research question |
| Null and alternative hypotheses | H1 group proportions and H2 paired mean difference; two-sided tests and retrospective testing-policy disclosure |
| Experimental design | Between-person background comparison, within-person passage comparison, variables/control table, reference condition and absence of counterbalancing |
| Power analysis | Independent-binomial enumeration for Fisher power; noncentral-t assumptions for paired quality; software, rates/effects, alpha, target and achieved-sample sensitivity |
| Collection and cleaning | 64 submissions to 26 retained, missingness, consent, exclusions, private original export, retrospective rule change and legacy-record sensitivities |
| Statistical analysis | Fisher test, paired t-test, assumptions/diagnostics, p-values, approximate marginal intervals, proportion difference and Cohen dz |
| Post hoc analyses | Three item-level comparisons with Bonferroni correction; Wilcoxon sensitivity, subgroups, confidence and exploratory regression |
| Interpretation | Separates observed choices/ratings from authorship ability or causal claims |
| Limitations | Fixed position, contradictory historical order evidence, sample size, convenience sampling, retrospective choices and missing covariates |
| Conclusion and recommendations | Conditional findings, prospectively specified counterbalanced replication and assumption-based recruitment guidance |
| References | Research articles, NIH source and reuse guidance, SciPy and statsmodels |

## Verification on November 2 2026

- Recomputed hypothesis tests, quality summaries and regression to temporary files from the committed de-identified data. Numerical values matched the current results within floating-point tolerance.
- `make check PYTHON=.venv/bin/python` passed; 31 unit tests passed on the latest repository.
- The assembled Word report was rendered and its pages checked visually.
- No participant names, free text, raw original workbooks or analytical datasets were added or changed by this report revision.
- A scan of 429 unique historical file blobs found no credential-like patterns or CSV identifier-column flags. This is a bounded check, not a guarantee against all re-identification risks; committed survey rows remain de-identified individual responses.

## Submission boundaries

The report contains every requested section. Contradictory passage-order evidence cannot be resolved from the repository and remains disclosed. A shareable report link is separate from actual course submission. Human partner review, any course submission and sending NIH a publication copy must be recorded when they occur; none is inferred from automated checks.
