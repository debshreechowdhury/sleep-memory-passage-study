# Report ownership and assembly

Edit one Markdown file per section inside your owner folder. Run `make report` from the repo root to stitch them into **report/report.md** in the course order specified by sections.json. Paste the approved assembled text into Byline and check image placement there. The owner files are authoritative; do not edit the generated file directly. The former uppercase report filename has been replaced by report.md.

| Section | Kuba | Debshree / shared |
|---|---|---|
| Title & Abstract | Joint review | shared/title_abstract.md |
| Background & Motivation | — | debshree/background.md |
| Hypotheses | kuba/hypotheses.md (H1) | debshree/hypotheses.md (H2/H3) |
| Experimental Design | — | debshree/experimental_design.md |
| Power Analysis | kuba/power.md (H1) | debshree/power.md (H2/H3) |
| Data Collection & Cleaning | kuba/data_collection_cleaning.md | — |
| Statistical Analysis | kuba/statistical_analysis.md | debshree/statistical_analysis.md |
| Interpretation | kuba/interpretation.md (quality) | debshree/interpretation.md (detection) |
| Limitations | kuba/limitations.md (ratings/data) | debshree/limitations.md (stimulus/sampling) |
| Conclusion & Recommendations | Joint review | shared/conclusion.md |
| References | Adds sources via PR | debshree/references.md maintains list |

Kuba’s files were migrated from the previous combined draft to preserve useful work, not to claim a contribution or review on his behalf. His item-level tests and regression decisions remain his work; the missing AI-use/English fields prevent the originally proposed regression. Shared abstract and conclusion are joint-review drafts and should be finalized last after both members’ sections are agreed. H3 is provisionally an international/domestic detection comparison; the old plan did not define it, so confirm the label and keep its retrospective/exploratory status.

All chart assets and aggregate inputs live in ../results/. Image links in owner fragments are written relative to the assembled report directory. Statistical source files include a common private-export checksum; names, free text and row-level exports stay private. See REPRODUCE.md and REVIEW_NOTES.md.
