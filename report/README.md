# Report

Each section is a file in `report/sections/`, numbered in the course's required order. Sections covering both research questions have one file for each. Run `make report` from the repo root to stitch them into **report/report.md** in the course order specified by sections.json. Paste the approved assembled text into Byline and check image placement there. The section files are authoritative; do not edit the generated file directly. The former uppercase report filename has been replaced by report.md.

| Section | Kuba | Debshree / shared |
|---|---|---|
| Title & Abstract | Joint review | sections/00_title_abstract.md |
| Background & Motivation | — | sections/01_background.md |
| Hypotheses | sections/02_hypotheses_quality.md (H1) | sections/02_hypotheses_detection.md (H2/H3) |
| Experimental Design | — | sections/03_design.md |
| Power Analysis | sections/04_power_quality.md (H1) | sections/04_power_detection.md (H2/H3) |
| Data Collection & Cleaning | sections/05_data_collection_cleaning.md | — |
| Statistical Analysis | sections/06_analysis_quality.md | sections/06_analysis_detection.md |
| Interpretation | sections/07_interpretation_quality.md (quality) | sections/07_interpretation_detection.md (detection) |
| Limitations | sections/08_limitations_ratings_data.md (ratings/data) | sections/08_limitations_stimulus_sampling.md (stimulus/sampling) |
| Conclusion & Recommendations | Joint review | sections/09_conclusion.md |
| References | Adds sources via PR | sections/10_references.md maintains list |
| Reproducibility & contribution note | Joint review | sections/11_contribution_note.md |

Kuba’s files were migrated from the previous combined draft to preserve useful work, not to claim a contribution or review on his behalf. His item-level tests and regression decisions remain his work; the missing AI-use/English fields prevent the originally proposed regression. Shared abstract and conclusion are joint-review drafts and should be finalized last after both members’ sections are agreed. H3 is provisionally an international/domestic detection comparison; the old plan did not define it, so confirm the label and keep its retrospective/exploratory status.

All chart assets and aggregate inputs live in ../results/. Image links in section files are written relative to the assembled report directory. Statistical source files include a common private-export checksum; names, free text and row-level exports stay private. See REPRODUCE.md and REVIEW_NOTES.md.

Take every number from `results/`. Do not type numbers from memory.

## Submission checklist
- [ ] Every rubric section completed and all placeholders removed.
- [ ] Tables/figures reproduced from scripts and numbers checked against outputs.
- [ ] Actual sample sizes, exclusions, p-values, CIs and effect sizes supplied.
- [ ] Instructor requirements and references checked.
- [ ] Submit final written report via the course Byline link; submit repository URL separately.
