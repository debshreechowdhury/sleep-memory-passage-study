# Report

Each section is a file in `report/sections/`, numbered in the course's required order. Sections covering all three hypotheses have one file for each, in the order H1, H2. Run `make report` from the repo root to stitch them into **report/report.md** in the course order specified by sections.json. Paste the approved assembled text into Byline and check image placement there. The section files are authoritative; do not edit the generated file directly. The former uppercase report filename has been replaced by report.md.

| Section | Kuba | Debshree / shared |
|---|---|---|
| Title & Abstract | Joint review | sections/00_title_abstract.md |
| Background & Motivation | — | sections/01_background.md |
| Hypotheses | sections/02_hypotheses_quality.md (H2) | sections/02_hypotheses_group.md (H1) |
| Experimental Design | — | sections/03_design.md |
| Power Analysis | sections/04_power_quality.md (H2) | sections/04_power_group.md (H1) |
| Data Collection & Cleaning | sections/05_data_collection_cleaning.md | — |
| Statistical Analysis | sections/06_analysis_quality.md (H2) | sections/06_analysis_group.md (H1) |
| Interpretation | sections/07_interpretation_quality.md (H2) | sections/07_interpretation_group.md (H1) |
| Limitations | sections/08_limitations_ratings_data.md (ratings/data) | sections/08_limitations_stimulus_sampling.md (stimulus/sampling) |
| Conclusion & Recommendations | Joint review | sections/09_conclusion.md |
| References | Adds sources via PR | sections/10_references.md maintains list |
| Reproducibility & contribution note | Joint review | sections/11_contribution_note.md |

Shared abstract and conclusion are joint-review drafts and should be finalized last after both members’ sections are agreed. H1 is the international versus domestic detection comparison; report that the written plan labelled it exploratory.

All chart assets and aggregate inputs live in ../results/. Image links in section files are written relative to the assembled report directory. Statistical source files include a common private-export checksum; names, free text and row-level exports stay private. See REPRODUCE.md and REVIEW_NOTES.md.

Take every number from `results/`. Do not type numbers from memory.

## Submission checklist
- [ ] Every rubric section completed and all placeholders removed.
- [ ] Tables/figures reproduced from scripts and numbers checked against outputs.
- [ ] Actual sample sizes, exclusions, p-values, CIs and effect sizes supplied.
- [ ] Instructor requirements and references checked.
- [ ] Submit final written report via the course Byline link; submit repository URL separately.
