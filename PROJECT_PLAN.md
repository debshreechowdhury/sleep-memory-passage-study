# Work allocation and submission tracker

## Debshree — `debshree/report-design`
Own report/debshree/: background, H2/H3, experimental design, H2/H3 power, detection/group/confidence analysis, detection interpretation, stimulus/sampling limitations and reference-list maintenance. These sections and presentation/debshree.pptx are prepared. H3 provisionally means international/domestic detection and needs team confirmation. Joint-review drafts live in report/shared/. Review Kuba’s mapping/results PR when available.

## Kuba — `kuba/data-analysis`
Own report/kuba/: H1, H1 power, collection/cleaning, quality/item tests and supported regression, quality interpretation and ratings/data limitations. Existing report content was migrated there as a review baseline; it does not constitute Kuba’s authored contribution. Create presentation/kuba.pptx and review Debshree’s PR.

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

Existing docs/pilot-protocol work and open PRs are preserved; reconcile with the actual study before merging.

## Shared setup review
The shared scaffold was merged to main in [PR #2](https://github.com/debshreechowdhury/sleep-memory-passage-study/pull/2). Debshree’s branch includes that merged baseline. Do not count the shared setup as either member’s substantive contribution.

## November 2 ownership revision

The owner-folder split follows the supplied section and slide assignments. `make report` assembles the course order from report/sections.json. All charts and chart inputs live in results/. Shared title/abstract and conclusion are joint-review drafts to finalize last. No final.pptx or Byline submission is claimed. Debshree’s own sections and eight-slide member deck are prepared; Kuba’s independent contribution and both members’ substantive peer review remain pending.
