# Work allocation and submission tracker

Split by research question. [AGENTS.md](../AGENTS.md) has the exact file list.

## Debshree: design and detection (`debshree/report-design`)
Owns the background, H2/H3, experimental design, H2/H3 power, detection/group/confidence analysis, detection interpretation, stimulus/sampling limitations and reference-list sections in report/sections/. These sections and presentation/design_detection.pptx are prepared. H3 provisionally means international/domestic detection and needs team confirmation. The title/abstract and conclusion sections are joint-review drafts. Review Kuba’s mapping/results PR when available.

## Kuba: data and quality (`kuba/data-analysis`)
Owns the H1, H1 power, collection/cleaning, quality/item tests and supported regression, quality interpretation and ratings/data limitations sections in report/sections/. Existing report content was migrated there as a review baseline; it does not constitute Kuba’s authored contribution. Create presentation/data_quality.pptx and review Debshree’s PR.

First data tasks: assign passage order per response rather than per file, since the form flipped on October 31; keep the form version and the international/domestic answer, which the importer currently drops and H3 needs; then regenerate the synthetic fixture.

## Together
Analysis plan and multiplicity policy, list of deviations from the original design, title, abstract, conclusion and recommendations, rehearsal and final submission.

## Shared milestones
1. Verify actual collection and form versions; record changes without calling retrospective decisions preregistered.
2. Review cleaning decisions and co-primary testing policy before inspecting condition differences where still possible.
3. Validate export mapping and preserve originals privately; document missing fields, exclusions and duplicates.
4. Generate real results and diagnostics; cross-review substantive PRs.
5. Integrate reviewed work, reproduce from a fresh checkout and submit report through Byline plus GitHub link.

Each member must commit their own substantive contribution and open their own PR. Branch creation alone does not satisfy that requirement. Record actual PR links and reviewer outcomes below only after they exist.

| Member | Branch | PR | Review |
|---|---|---|---|
| Debshree | debshree/report-design | [PR #3](https://github.com/debshreechowdhury/sleep-memory-passage-study/pull/3) | Peer review pending |
| Kuba | kuba/data-analysis | Pending member contribution | Pending |

Existing docs/pilot-protocol work and open PRs are preserved; reconcile with the actual study before merging. The debshree/report-design and kuba/data-analysis branches predate this layout, so start new work from main after this layout merges.

## Shared setup review
The shared scaffold was merged to main in [PR #2](https://github.com/debshreechowdhury/sleep-memory-passage-study/pull/2). Do not count the shared setup as either member’s substantive contribution.

## November 2 ownership revision

The section split follows the supplied section and slide assignments. `make report` assembles the course order from report/sections.json. All charts and chart inputs live in results/. Shared title/abstract and conclusion are joint-review drafts to finalize last. No final.pptx or Byline submission is claimed. Debshree’s own sections and eight-slide member deck are prepared; Kuba’s independent contribution and both members’ substantive peer review remain pending.
