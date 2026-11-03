# AI rewrite identification and writing quality by student background

Debshree Chowdhury and Jakub Romańczuk · AIPI 510 · November 2, 2026

## Abstract

We compared international- and domestic-background respondents’ identification of an AI rewrite and explored their writing-quality ratings. Of 64 submissions, 26 student-background respondents passed both comprehension checks. Under the final original-first coding, domestic respondents selected the AI passage more often than international respondents (11/12 versus 5/14; Fisher p = .0053). The rewrite received higher paired quality ratings (difference 0.487/7, 95% CI [0.175, 0.799], p = .0036, dz = 0.630). Fixed passage order, contradictory historical assignment evidence and retrospective analysis decisions prevent general claims about AI-recognition ability or authorship effects.

## Background and motivation

AI-assisted science writing raises two distinct questions: how readers judge its quality and whether they recognize its source. Studies of self-presentations and scientific abstracts show that human source judgments can be unreliable (Jakesch et al., 2023; Gao et al., 2023), although those tasks do not establish a benchmark for ours. We used an NIH News in Health passage about sleep and memory (NIH, 2013) and one AI rewrite to compare source choices by student background and explore perceived quality. Background is not a measure of English proficiency or AI experience.

## Null and alternative hypotheses

H1, the final main question: H0 states that the probability of selecting the passage coded as AI is equal for international- and domestic-background respondents; HA states that it differs. We use a two-sided Fisher’s exact test at α = .05. H2, exploratory: H0 states that the population mean within-person AI-minus-original quality difference is zero; HA states that it is nonzero. We use a two-sided paired t-test at .05.

The October 30 plan labelled the group comparison exploratory. Its later promotion, the stricter comprehension rule and the final testing policy were adopted after earlier results had been examined; the study was not preregistered. The originally listed overall chance test was dropped after results were seen. For transparency, its result was χ²(1) = 1.385, p = .239 (16/26 correct); it is not a current primary hypothesis. Exploratory item tests have a separate three-test Bonferroni correction.

## Experimental design

H1 is a between-person observational comparison: reported student background is the grouping variable and coded source-choice correctness is the binary dependent variable. H2 is within-person: passage version is the factor and the mean of clarity, engagement and overall-writing ratings (each 1–7) is the outcome. Every respondent read both versions; the NIH original served as the reference condition. Topic, factual content, four-paragraph structure, quotation, plain formatting, rating scales and comprehension question were shared.

The team reports original first and AI second throughout collection, so selecting Passage 2 is always coded correct. A November 2 form read displayed the reverse; historical order is not independently resolved. We retain the final repository mapping and make directions conditional on it. Planned order randomization was not verified; version and position are confounded. Background was not assigned, and recruitment used a voluntary convenience link. The rewrite used the reported GPT-6.1 SOL label and the second of two supplied prompts; texts and prompts are archived. Initial AI nondisclosure was followed by a source choice and confidence rating, with debrief after submission. Instructor acceptance is team-reported, not evidence of separate ethics-board approval.

<!-- pagebreak -->

## Power analysis

Calculations were prepared after collection began and are assumed-effect planning sensitivities, not prospective justification or observed power. Python/SciPy enumerates independent binomial success counts for both groups and sums their joint probabilities whenever the two-sided Fisher test rejects at .05. With groups of 14 and 12, power is 12.1% for assumed probabilities .50/.70, 27.3% for .30/.60 and 75.4% for .10/.60. The balanced search first reaches 80% power at 48 analyzable respondents per group for .30/.60. These assumptions require independent Bernoulli responses and fixed sample sizes.

Paired-t power uses a noncentral t distribution with df = n − 1 and noncentrality dz√n, where dz is the assumed mean paired difference divided by its standard deviation. At two-sided .05, assumed dz = .50 requires 34 complete pairs for 80% power; 26 pairs provide 68.8% power. The achieved sample therefore has limited sensitivity to modest effects. Exclusions require additional recruitment. Scripts and outputs are in scripts/group_power.py and scripts/quality/ and results/quality/; current results used Python 3.13, NumPy 2.2.6 and SciPy 1.15.3, with statsmodels for regression.

## Data collection and cleaning

The November 2 workbook contained 64 consenting submissions collected October 31–November 2. We removed 35 respondents reporting no student background and required both sleep-cycle comprehension answers to be 90 minutes: two students missed both and one missed one, leaving 26 (14 international, 12 domestic). Eligibility used background, not current employment/status: retained respondents included 23 selecting Student, two Working professional and one legacy Yes. The both-correct rule retrospectively replaced the planned exclusion of only both-wrong responses, which retains 27 students.

Original exports remain private. Import scripts remove names, timestamps and free text; the repository holds de-identified data and aggregate outputs. Ratings, checks, source choice and confidence were complete, with no imputation. Duplicate people could not be verified; matching answer patterns were retained. No page-time exclusion was possible. The team reports no pilot responses and closed collection. One legacy record’s assignment is uncertain, so omission and reversal sensitivities were retained.

## Statistical analysis

| Comparison | Estimate and 95% CI | Test and effect |
|---|---|---|
| H1 domestic minus international | 91.7% − 35.7% = 56.0 percentage points [23.4, 88.5] | Two-sided Fisher p = .0053 |
| H2 AI minus original quality | 5.962 − 5.474 = 0.487 points [0.175, 0.799] | t(25) = 3.213, p = .0036; dz = 0.630 |

Fisher’s test fits the sparse H1 table (smallest expected count 4.62). Its displayed proportion-difference interval is an approximate Welch-t interval on binary scores, not an exact Fisher interval. H2 uses paired differences, SD = 0.773. Shapiro–Wilk did not reject normality (W = .938, p = .119); limited power, bounded ratings and eight ties motivated a Wilcoxon sensitivity (W = 22.5, p = .00579). These tests assume independent respondents; Wilcoxon does not test exactly the same mean hypothesis. All intervals are marginal, not simultaneous.

Post hoc paired item tests gave clarity +0.500 (95% CI [0.264, 0.736], dz = 0.857; raw p = .00019, Bonferroni p = .00057), engagement +0.538 (adjusted p = .0710) and writing +0.423 (adjusted p = .306). Only clarity met .05/3; item differences were nonnormal, with Wilcoxon sensitivities reported in the full analysis. No further pairwise test is needed for a two-version composite comparison.

<!-- pagebreak -->

## Statistical analysis continued

H1 sensitivity p-values were .0047 under the planned check rule, .0112 omitting the legacy record, .0145 reversing it and .0272 restricting current status to Student. Without the final ten submissions, H1 was p = .145. Changing subset p-values is not a formal test of changing effects. H2 stayed positive under reported sensitivities, with estimates 0.390–0.507, but the item-level pattern changed.

Exploratory confidence means were 3.50 for correct and 3.00 for incorrect choices; tie-corrected Mann–Whitney U = 104.5, p = .141. This compares distributions, not probability calibration. Quality differences did not clearly differ by background (Welch p = .555). Regression on background, correct choice and confidence gave F(3,22) = 1.262, p = .312, R² = .147. Residual Shapiro–Wilk p = .376 and Breusch–Pagan p = .181 indicated no clear violations but cannot establish assumptions in a small sample. AI use and English proficiency were uncollected, so their planned regression was not possible. These analyses are exploratory, not evidence that nonsignificant associations are absent.

## Interpretation of results

Under the final coding, H1 rejects equal source-choice probabilities, and exploratory H2 favors the rewrite by approximately half a scale point. Neither establishes causation. Choosing AI is identical to choosing Passage 2, and quality differences may reflect repeated exposure, familiarity or contrast. The defensible finding is a difference in choices and ratings for this fixed-order pair and sample. The order contradiction means authorship directions depend on the team’s mapping; reversing the mapping reverses those directions while leaving the principal two-sided p-values unchanged. The result does not establish that domestic students are generally better at recognizing AI.

## Limitations

One topic, one selected rewrite, fixed order, convenience recruitment and small unequal groups limit generalization and precision. Historical order/debrief evidence conflicts with the reported collection order. A mislabelled debrief would give participants the wrong answer, although it appeared after submission with editing off. An unmatched quote in the original may have provided a cue. Eligibility/status wording changed; age was instructed rather than verified, optional names made some responses identifiable, and page times, language proficiency and AI use were unavailable. Retrospective hypothesis emphasis, exclusions and removal of the chance test introduce selection risk. The final ten responses affect H1’s rejection, but timing alone does not establish dependence or justify exclusion; the team reports different people, not one class/group. The generation date remains unknown, and supplied prompts do not guarantee regeneration.

## Conclusion and recommendations

The findings support a prospectively specified replication, not a ranking of student groups or proof of AI writing superiority. Randomize and balance passage order within groups, use multiple independently selected passage pairs, verify eligibility and archive respondent-level assignment and exact form versions. Choose meaningful effects and a testing policy before collection; the illustrative 48-per-group target assumes .30/.60, α = .05 and independent responses, and must allow for exclusions. Measure proficiency and AI use directly, separate identifiers, provide an accurate debrief and pilot the complete flow. Additional observations alone will not resolve the position confound.

## References

Gao, C. A., et al. (2023). Comparing scientific abstracts generated by ChatGPT to real abstracts with detectors and blinded human reviewers. npj Digital Medicine, 6, 75. https://doi.org/10.1038/s41746-023-00819-6

Jakesch, M., Hancock, J. T., & Naaman, M. (2023). Human heuristics for AI-generated language are flawed. PNAS, 120(11), e2208839120. https://doi.org/10.1073/pnas.2208839120

NIH. (2013, April). Sleep On It. NIH News in Health. https://newsinhealth.nih.gov/2013/04/sleep-it

SciPy developers. Statistical functions documentation. https://docs.scipy.org/doc/scipy/reference/stats.html

statsmodels developers. Ordinary least squares and diagnostics. https://www.statsmodels.org/stable/
