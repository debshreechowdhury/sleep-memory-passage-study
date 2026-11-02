# Perceived writing quality and AI detection in a sleep-and-memory passage pair

Working report outline — results pending; do not submit placeholders.

## Abstract
Write last: motivation, actual design, final analyzed sample, paired estimate and CI, detection estimate and CI, main limitation and conclusion. No invented results.

## Background and motivation
Explain why perceived quality and AI detection matter. Distinguish judgments of writing from factual accuracy and learning outcomes. Cite the NIH source and verified research added by the team.

## Null and alternative hypotheses
Rating H0: population mean within-person quality difference (AI minus original) = 0; H1: difference ≠ 0.
Detection H0: probability of correctly identifying the AI passage = .50; H1: probability ≠ .50. Two-sided tests, nominal alpha .05. State the final co-primary multiplicity policy.

## Experimental design
Within-person comparison: each participant rates both versions. IV: passage version. DVs: clarity, engagement and writing quality (1–7), their mean composite, detection correctness and confidence. Original text is the comparison condition. The circulated link is fixed AI-first; do not claim randomization or 15/15 counterbalancing without assignment evidence. Recruitment is convenience sampling; status categories are student, working professional, other. Document form revisions and dates because versions changed during launch. One passage pair limits generalization and repeated content can create carryover.

## Power analysis
Run `scripts/power.py`. Define dz = expected paired mean difference / SD of within-person differences, not pooled passage SD. Show assumed dz .3/.5/.8, two-sided alpha .05, target .80 and complete pairs required. Planned n=30 is a scenario, not confirmed enrollment. State attrition assumption and recruitment target separately. If collection already started, label this a planning/sensitivity calculation performed after launch, not a preregistered power analysis. Add a detection-power calculation if detection is retained as co-primary.

## Data collection and cleaning
Document actual recruitment, collection dates, consent, 18+ instruction, optional names, CSV exports, storage and access. Names make responses identifiable. Describe header mapping, fixed order, exclusions for both checks wrong, missing-data handling, duplicate review and withdrawal handling. No page-time exclusion is possible in native Google Forms. Separate pilot from main responses with documented evidence. See data/README.md.

## Statistical analysis
Report participant flow and denominators separately for ratings and detection. Use paired t-test on composite scores; inspect within-person differences for outliers and normality, and discuss independence. Include mean difference, SD, t(df), p, 95% CI and Cohen dz. Report Cronbach alpha separately for both three-item scales; it is not evidence of validity by itself. Chi-square detection GOF requires adequate expected counts; exact binomial test and exact proportion CI are also produced. Add diagnostic figures and a prespecified sensitivity analysis if warranted. No post hoc comparisons are needed for a two-level paired primary comparison. Exploratory status analysis and regression require sufficient observations; the three-category status variable is not a simple 2×2 Fisher test.

## Interpretation of results
Pending real data. Separate statistical significance, effect magnitude, uncertainty and practical importance. A nonsignificant result does not establish equivalence. Distinguish exploratory from confirmatory findings.

## Limitations
Fixed order, carryover, convenience sample, single passage pair, small sample, no page timing, revisions after launch, optional identifiers, possible duplicates, missing AI-use/English items, and absence of verified preregistration. Verify these against actual exports and collection records.

## Conclusion and recommendations
Pending results. Limit claims to this sample and passage pair; recommend a larger randomized multi-passage replication where justified.

## References
- NIH News in Health (2013). Sleep On It. https://newsinhealth.nih.gov/2013/04/sleep-it
- SciPy paired t-test documentation: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html
- SciPy exact binomial test documentation: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binomtest.html
- Add peer-reviewed background and final software versions used.

## Submission checklist
- [ ] Every rubric section completed and all placeholders removed.
- [ ] Tables/figures reproduced from scripts and numbers checked against outputs.
- [ ] Actual sample sizes, exclusions, p-values, CIs and effect sizes supplied.
- [ ] Instructor requirements and references checked.
- [ ] Submit final written report via the course Byline link; submit repository URL separately.
