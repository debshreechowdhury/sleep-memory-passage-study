# Work allocation and submission tracker

## Debshree — `debshree/report-design`
Own report/REPORT.md, forms documentation, recruitment/revision log and study-design interpretation. Verify current form, actual consent/eligibility and collection dates; complete background, hypotheses, power assumptions, limitations and final report narrative. Review Kuba's mapping and results PR.

## Kuba — `kuba/data-analysis`
Own export mapping, scripts, diagnostics, cleaned-data dictionary, statistical tables and figures. Verify CSV headers privately, run cleaning/analysis, add exploratory work only if fields and sample support it. Review Debshree's report/design PR.

## Shared milestones
1. Verify actual collection and form versions; record changes without calling retrospective decisions preregistered.
2. Review cleaning decisions and co-primary testing policy before inspecting condition differences where still possible.
3. Validate export mapping and preserve originals privately; document missing fields, exclusions and duplicates.
4. Generate real results and diagnostics; cross-review substantive PRs.
5. Integrate reviewed work, reproduce from a fresh checkout and submit report through Byline plus GitHub link.

Each member must commit their own substantive contribution and open their own PR. Branch creation alone does not satisfy that requirement. Record actual PR links and reviewer outcomes below only after they exist.

| Member | Branch | PR | Review |
|---|---|---|---|
| Debshree | debshree/report-design | Pending member contribution | Pending |
| Kuba | kuba/data-analysis | Pending member contribution | Pending |

Existing docs/pilot-protocol work and open PRs are preserved; reconcile with the actual study before merging.

## Shared setup review
The project scaffold lives on project/setup and must be reviewed before merging to main. Member branches include that baseline. Merge the setup first, then base member PRs on main; do not count the shared setup as either member's substantive contribution.
