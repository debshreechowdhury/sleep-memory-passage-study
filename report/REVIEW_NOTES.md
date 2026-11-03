# Member review and submission status

Debshree's report and design work is complete for the November 2 response snapshot and awaits peer review. The report contains all requested sections and actual results; it does not claim that unresolved factual details have been verified.

Before submission, the team must verify the first response's passage version and any known pilot/test submissions, confirm instructor/ethics requirements, and check that the snapshot is the intended final dataset. The report already discloses those uncertainties and presents version sensitivities. Do not choose exclusions or a version mapping to obtain a preferred p-value. The fixed-order limitation cannot be repaired retrospectively.

Kuba should independently review column mapping, exclusion counts, calculations, and interpretation. His separate analysis PR and the actual peer-review history remain his contribution. This branch does not mark that work or either member's review as complete. Submit the approved report through the course Byline link and the repository URL through the required submission route; no course submission has been made by this task.

No raw participant data, names, free-text responses, or private crosswalks belong in this PR. The aggregate report evidence is derived from the local private CSV and identified by its SHA-256 checksum in results/report_statistics.json. A fresh data export requires rerunning the evidence script and updating the report numbers and figures together.

## Hypothesis update

H1 is the international versus domestic detection comparison, H2 is quality and H3 is overall detection, all two-sided at .05/3 = .0167, on the 26 students who answered both checks correctly. Kuba's branch updated all report sections, `presentation/design_detection.pptx` and the checks to this structure, including Debshree's sections. **Debshree has not yet reviewed these changes**, so they remain a proposal until that review. Please check that:

- `sections/02_hypotheses_group.md` describes the plan accurately, including that it labelled this comparison exploratory.
- `sections/01_background.md` and `sections/03_design.md` still say what you intended.
- `sections/06_analysis_detection.md` and the deck can drop the exact binomial test, odds ratio, Cohen's w and Spearman permutation test; the 54-response analysis keeps them in `results/debshree_statistics.json` as a record.
- `scripts/build_debshree_slides.mjs` is no longer needed. `make slides` now builds the deck with python-pptx.

Still open for the team: verify the first response's passage version and any pilot or test submissions, find out whether the last ten responses came from one group, confirm the model name and date for the rewrite and archive the prompt in `study/stimuli/`, and confirm instructor or ethics requirements.
