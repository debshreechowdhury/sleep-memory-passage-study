# Do international and domestic students differ in identifying an AI rewrite? A sleep and memory passage study

Debshree Chowdhury and Jakub Romańczuk

AIPI 510 Term 2 Project

Responses downloaded November 2, 2026

## Abstract

Our main question was whether international and domestic students differ in identifying an AI rewrite of a science passage. Participants read an original NIH News in Health passage about sleep and memory and an AI rewrite, rated each for clarity, engagement, and overall writing on seven-point scales, answered comprehension checks, and identified the AI passage. The circulated form presented AI first and the original second. Of 64 submissions, we analyzed the 26 students who answered both checks correctly: 14 international and 12 domestic. The three planned tests used a Bonferroni threshold of .05/3 = .0167. International students identified the AI passage more often than domestic students, 9/14 (64.3%) versus 1/12 (8.3%), a difference of 56.0 percentage points, 95% confidence interval [23.4, 88.5], Fisher's exact p = .0053. The written plan labelled this comparison exploratory, and it does not reach the threshold without the last ten responses (p = .145). Because the AI passage was always first, a correct answer always meant choosing Passage 1, so the difference cannot be separated from a preference for the first passage. Students also rated the original higher, by 0.487 points, 95% confidence interval [0.175, 0.799], t(25) = 3.213, p = .0036, dz = 0.630; this also cannot be separated from position. Overall detection accuracy, 10/26 (38.5%), did not differ reliably from chance, chi-square(1) = 1.385, p = .239. These results justify a randomized follow-up and do not establish that either group detects AI better.

## Background and motivation

Readers encounter AI-assisted prose in educational and scientific communication, and students read this prose from different educational backgrounds. Our main question is whether international and domestic students differ in recognizing an AI rewrite. We also ask whether a rewrite changes perceived quality and whether students overall can recognize its origin. These outcomes need separate measurement. A passage can be judged clear or engaging while its authorship is misclassified; neither judgment alone establishes factual accuracy or learning.

Prior work provides reasons to avoid assuming reliable human detection. Jakesch, Hancock, and Naaman (2023) found that judgments of AI-generated self-presentations relied on imperfect linguistic heuristics. Gao et al. (2023) examined scientific abstracts using blinded reviewers and found both missed generated texts and false accusations against original texts. Their tasks and materials differ from this study, so their detection rates are not directly comparable with a forced choice between two closely related passages.

We used an excerpt from NIH News in Health's April 2013 article Sleep On It and an AI rewrite of the same content (National Institutes of Health, 2013). Keeping the topic and principal information similar supports a focused comparison of prose. We had no directional prediction about which student group would identify the rewrite more often, so the group comparison is two-sided. This study evaluates perceived writing and source identification; it does not test the underlying sleep science or memory performance.

## Null and alternative hypotheses

### H1: Detection by student background (main question)

H0: the proportion who correctly identify the AI passage is equal for international and domestic students. Alternative: the proportions differ. The test is two-sided. Respondents answering Not applicable do not enter this comparison. Background labels are self-reports, not verified citizenship or English proficiency.

This comparison, its null hypothesis, and Fisher's exact test were written down before the first response, and the form asked about student background for this purpose. The written plan labelled it exploratory because of low expected power and listed quality and overall detection as primary. We report it first because it is our main interest; that change of emphasis was made on November 2, after earlier results had been seen.

### H2: Perceived quality (secondary)

H0: among current students, the population mean original-minus-AI composite quality difference equals zero. Alternative: the difference is nonzero. The test is two-sided, using the .05/3 = .0167 threshold shared by the three planned tests.

### H3: Overall detection against chance (secondary)

H0: the proportion of students correctly identifying the AI passage is .50. Alternative: that proportion differs from .50. This is a two-sided question; the data do not justify choosing a one-sided direction after inspection. It is separate from H2, the quality comparison.

### Testing policy

All three hypotheses were specified before collection, so they share a Bonferroni threshold of .05/3 = .0167. This replaces the earlier plan's nominal .05 threshold and retrospective .025 sensitivity threshold. The study was not preregistered, and this policy was set on November 2. Item-level, subgroup, regression, and confidence analyses are exploratory. All displayed 95% intervals are marginal, not simultaneous familywise intervals.

## Description of experimental design

The main comparison was between groups: the independent variable was self-reported student background, international or domestic, which was observed and not randomized, and the dependent variable was detection correctness, coded 1 or 0. The secondary quality comparison was within-person: the independent variable was passage version, original or AI rewrite, with the original as the comparison condition, and the dependent variables were clarity, engagement, and overall writing ratings, each from 1 (Not at all) to 7 (Extremely); their mean formed the quality composite. Confidence ranged from 1 to 5, and participant status described the sample. Optional names were collected separately from the analytic variables.

The form introduced two short science-news passages without announcing AI authorship. Each passage page contained the three ratings and the same comprehension question about the approximately 90-minute sleep cycle. A later page disclosed that one text had been rewritten and requested a forced choice, confidence, and an optional explanation. The answer key, source, rationale for initial nondisclosure, and study contacts appeared after submission. Response editing was disabled.

The plan called for randomized order, but the circulated form presented AI as Passage 1 and the original as Passage 2. No evidence supports randomized order or balanced allocation in these responses. Consequently, version and position are confounded, and a correct detection answer always meant choosing Passage 1. Both passages used the same plain-text presentation without separate source branding, but textual NIH references and the shared scientific quotation remained. The rewrite was produced with ChatGPT-6.1 Sol over two prompts, and the second output was used; the plan had called for using the first output. The generation date was not recorded.

Participation was voluntary through a shared online link, yielding a convenience sample. Eligibility changed from graduate students to students, working professionals, and others aged at least 18. The adult restriction was an instruction; the export contains no recorded age verification. One retained record still has the older affirmative status answer. The report evaluates a workbook downloaded on November 2, with the last response at 19:03 in the export's timestamp labels. The form has since been closed.

For detection, each person contributed one forced-choice outcome and one confidence response. The paired structure applies to passage ratings, not two independent detection observations. Background and employment/student status were observed characteristics rather than randomized treatments. Group comparisons therefore describe associations and cannot establish a causal effect of background. The presentation and report use the same November 2 workbook.

## Power analysis

### H1: Between-group detection planning

All power calculations were made after collection began and are illustrative planning sensitivities, not prospective justification or observed power. New calculations use NumPy 2.2.6 and SciPy 1.15.3 under Python 3.13. scripts/group_power.py enumerates independent binomial counts for two groups and sums their joint probabilities whenever the two-sided Fisher's exact p-value is at or below the threshold. The alternative counts are sampled from assumed group-specific rates.

| Assumed accuracies | Power at 14 vs 12, .05 | Power at 14 vs 12, .0167 |
|---|---:|---:|
| .50 vs .70 | 12.1% | 6.0% |
| .30 vs .60 | 27.3% | 15.3% |
| .50 vs .80 | 27.3% | 15.6% |
| .10 vs .60 | 75.4% | 59.4% |

The achieved groups could reliably detect only very large gaps. The plan flagged very low power for this comparison at 15 versus 15. In a study this small, a result that reaches significance may overstate the true difference, so the observed gap should not be used as an effect-size estimate for planning.

| Assumed accuracies | Power: 15 per group | Power: 30 per group | Power: 50 per group | Power: 100 per group |
|---|---:|---:|---:|---:|
| .40 vs .60 | 9.5% | 25.7% | 46.2% | 78.7% |
| .30 vs .60 | 22.7% | 56.1% | 82.9% | 98.9% |
| .30 vs .70 | 43.4% | 83.8% | 97.9% | >99.9% |

At .05, an assumed 30-percentage-point gap reaches .80 power with 50 complete respondents in each group in this table. This is an example for a future study, not a retrospective recruitment target. Balanced future recruitment and an attrition allowance should be specified before recruitment. Power planning cannot correct fixed-order confounding or convenience sampling.

### H2: Paired quality planning

Power calculations were prepared after collection began. They are planning sensitivities under assumed effects, not prospective justification, observed power, or evidence of preregistration. The initial n = 30 scenario refers to complete pairs. We used Python 3.10 and SciPy 1.15.3. The paired-t calculation uses the noncentral t distribution: the noncentrality is the assumed standardized paired difference multiplied by the square root of the number of complete pairs, with n minus one degrees of freedom. Cohen dz uses the standard deviation of within-person differences, not the pooled standard deviation of the two passages.

| Assumed absolute dz | Pairs for 80% power at .05 | Power with 30 pairs at .05 | Pairs for 80% power at .0167 |
|---|---:|---:|---:|
| 0.30 | 90 | 35.5% | 120 |
| 0.50 | 34 | 75.4% | 45 |
| 0.80 | 15 | 98.8% | 20 |

No attrition allowance was specified prospectively. For illustration, 34 usable pairs with a 10% allowance would require 38 recruits, calculated by dividing 34 by .90 and rounding up. This is a planning example, not a claim about the actual recruitment target. The report does not compute power from the observed effect.

### H2: Sensitivity at the achieved sample

The analyzed sample has 26 complete pairs, below both the initial n = 30 scenario and the 34 pairs needed for 80% power at an assumed dz of 0.50. With 26 pairs and 80% power, the smallest detectable standardized paired difference is about dz = 0.57 at .05 and dz = 0.67 at the .0167 threshold. Power at .05 and .0167 is 31.3% and 17.1% for an assumed dz of 0.30, 68.8% and 50.4% for 0.50, and 97.5% and 92.6% for 0.80. These values use assumed effects at the achieved sample size, not the observed effect, so they describe what the design could detect and not the strength of the observed result. They were calculated with the same SciPy version under Python 3.13. The study is therefore poorly placed to detect small differences, and a nonsignificant follow-up in this sample does not show that a difference is absent.

### H3: Overall detection planning

The calculation sums binomial probabilities over the correct counts that the chi-square goodness-of-fit test rejects against .50. Independent, identically distributed participant choices are assumed. Target power is .80; complete cases, rather than recruits, determine n.

| Assumed true accuracy | First n with 80% power at .05 | Power at n = 26, .05 | First n with 80% power at .0167 |
|---|---:|---:|---:|
| .60 | 187 | 22.8% | 257 |
| .70 | 43 | 62.7% | 61 |
| .80 | 19 | 94.1% | 24 |

These rates are assumed alternatives, not estimates used to calculate post hoc observed power. Rejection regions change discretely: the first qualifying n does not imply that every larger n attains the target.

## Data collection and cleaning procedures

The analyzed Google Forms workbook contained 64 submissions dated October 31 to November 2, 2026 in the export's timestamp labels. All 64 affirmed consent. Status was Working professional for 36, Student for 25, Other for two, and the legacy Yes for one. Student background was international for 15, domestic for 14, and not applicable for 35. Thirty-six names and 21 optional explanations were supplied. Ten of the 64 arrived after the earlier 54-response snapshot, within about 15 minutes on November 2; all ten were students, and the team reports that they came from different people and not a single class or group.

We preserved the downloaded workbook unchanged in local restricted storage and recorded its SHA-256 checksum in the aggregate results. A script converts it to a private CSV, and the importer then keeps only reviewed columns by position, because both passage blocks use the same question labels. Names, timestamps, and participant explanations are discarded at that step and appear in no repository output. Ratings, comprehension responses, confidence, consent, and detection were complete. No missing values were imputed.

We applied two exclusion rules. First, we kept only respondents who reported being an international or domestic student, because the main comparison is between those groups and the study was originally designed for graduate students; the 35 who answered "Not applicable — not currently a student" were removed. Second, we required the correct answer, 90 minutes, on both comprehension checks, treating any wrong answer as evidence that the passage may not have been read carefully. Of the 29 student-background respondents, two missed both checks and one missed one, leaving 26 for analysis: 14 international and 12 domestic. By stated status, these were 23 Student, two Working professional, and the one legacy Yes. Status and student background did not align exactly, and we used the student-background answer for the rule.

| Step | Removed | Remaining |
|---|---:|---:|
| Submissions | | 64 |
| Not currently a student | 35 | 29 |
| Both comprehension checks wrong | 2 | 27 |
| One comprehension check wrong | 1 | 26 |

The student restriction follows from the planned international versus domestic comparison, which was written down before collection began. The stricter check rule is retrospective: it was adopted on November 2, after the 54-response results had been seen, and it replaces the planned rule that removed a respondent only if both checks were wrong. We therefore also report the planned check rule as a sensitivity analysis. Across all 64 submissions, six missed the first check, six missed the second, and five missed both, so the planned check rule retains 59 of the 64 submissions and 27 of the 29 students.

No timing exclusion was applied because Google Forms did not collect passage-page times. The team reports that no pilot responses were collected. No verified duplicate-person labels were available, so no such records were removed. Four answer patterns repeated across the 64 submissions, two of them among the 26 retained; matching answers do not establish repeated participation.

The primary mapping assumes the current AI-first version for all retained responses. The legacy record's version cannot be verified from the export alone, so we report analyses omitting it and reversing its version mapping, rather than selecting a treatment based on statistical significance. Any request to identify a submitted response would require a separately protected record. Questionnaire revisions and the lack of a verified prospective registration are documented as limitations.

## Statistical analysis

### H1: Student-background comparison

The comparison uses the background question as answered, regardless of a respondent's separate current-status answer. The two groups are independent, and the outcome is a two-category count, so the natural test is chi-square of independence. The expected count for correct domestic students is 4.62, below the usual minimum of 5, so we use a two-sided Fisher's exact test, which does not rely on the chi-square approximation. Fisher's test assumes independent responses. We report the difference in proportions as the effect size, with a Welch t-based 95% confidence interval on the 0/1 scores. With counts this small, that interval is approximate.

| Background | Correct | Incorrect | Accuracy |
|---|---:|---:|---:|
| International | 9 | 5 | 64.3% |
| Domestic | 1 | 11 | 8.3% |

The difference was 56.0 percentage points, 95% confidence interval [23.4, 88.5], Fisher's exact p = .0053. This is below the .0167 threshold, so we reject H0.

![Detection accuracy by student background](../results/quality/group_detection.png)

Figure 1. Share of each student group choosing the AI passage. Because the AI passage was always first, this is also the share choosing Passage 1.

| Sensitivity | International | Domestic | Fisher p |
|---|---:|---:|---:|
| Planned both-wrong check rule | 10/15 | 1/12 | .0047 |
| Omitting the legacy record | 8/13 | 1/12 | .0112 |
| Reversing the legacy record | 8/14 | 1/12 | .0145 |
| Stated status Student only | 7/12 | 1/11 | .0272 |
| Without the last ten responses | 6/10 | 1/6 | .145 |
| Planned check rule, 54-response snapshot | 7/11 | 1/6 | .1312 |

The direction was the same in every row, with international students correct more often. The result stayed below .0167 under the planned check rule and both legacy-record analyses, but not when restricted to stated Student status or without the last ten responses. Those ten arrived within about 15 minutes, with international students correct 3/4 times and domestic students 0/6 times. The team reports that they came from different people and not a single class or group, so we kept them, but the result leans on them.

### H2: Quality analysis

For each participant and version, quality was the arithmetic mean of all three ratings. We calculated the original-minus-AI paired difference, its standard deviation, a two-sided paired t-test, a t-based 95% confidence interval, and Cohen dz. A paired t-test fits because each participant rated both versions, so the differences within people are the unit of analysis. We summarized how closely the three ratings agreed using descriptive pairwise correlations within each version. A two-level paired comparison needs no post hoc test between versions; item-level follow-ups are reported below.

We examined the distribution of paired differences with a histogram, a quantile plot, and Shapiro-Wilk. Independence depends on recruitment and duplicate review and cannot be established by this test. Shapiro-Wilk did not reject normality, W = .938, p = .119, although with 26 pairs it has limited power, and the bounded scales and eight tied differences warranted a Wilcoxon signed-rank sensitivity analysis. Mathematical ties were preserved by rounding differences to ten decimal places; its p-value uses a normal approximation with zeros omitted. This test has different assumptions and does not directly test the identical population-mean hypothesis.

![Paired difference histogram and normal quantile plot](../results/quality/difference_diagnostics.png)

Figure 2a. Diagnostic views of the 26 original-minus-AI composite differences. Eight respondents rated the two versions equally.

### Quality results

| Outcome | AI mean | Original mean | Original minus AI |
|---|---:|---:|---:|
| Clarity | 5.923 | 6.423 | 0.500 |
| Engagement | 5.154 | 5.692 | 0.538 |
| Overall writing | 5.346 | 5.769 | 0.423 |
| Composite quality | 5.474 | 5.962 | 0.487 |

Composite standard deviations were 0.828 for AI and 0.568 for the original. The standard deviation of paired differences was 0.773. The paired test gave t(25) = 3.213, p = .0036, with 95% confidence interval [0.175, 0.799] for the original advantage and dz = 0.630. The p-value is below the Bonferroni threshold of .05/3 = .0167 for the three planned tests, so we reject H0. Original quality was higher for 15 participants, AI quality was higher for three, and eight tied. The Wilcoxon sensitivity agreed, W = 22.5, p = .00579.

| Correlation between | AI rewrite | Original |
|---|---:|---:|
| Clarity and engagement | .45 | .37 |
| Clarity and overall writing | .30 | .10 |
| Engagement and overall writing | .60 | .53 |

Engagement and overall writing moved together, while clarity was only weakly related to overall writing, especially for the original. The three ratings therefore do not behave as interchangeable measures, and the composite should be read alongside the items.

### Item-level post hoc tests

To see which ratings contributed to the composite difference, we compared each item with a paired t-test as a post hoc follow-up. Bonferroni correction for three tests sets the per-test threshold at .05/3 = .0167, which is equivalent to multiplying each p-value by three. Shapiro-Wilk rejected normality for all three item differences, which take few distinct values, so we also report Wilcoxon p-values.

| Item | Original minus AI | 95% CI | t(25) | p | Bonferroni p | dz | Wilcoxon p |
|---|---:|---:|---:|---:|---:|---:|---:|
| Clarity | 0.500 | [0.264, 0.736] | 4.372 | .00019 | .00057 | 0.857 | .00079 |
| Engagement | 0.538 | [0.078, 0.999] | 2.409 | .0237 | .0710 | 0.473 | .0253 |
| Overall writing | 0.423 | [-0.090, 0.936] | 1.698 | .102 | .306 | 0.333 | .133 |

![Item-level differences with confidence intervals](../results/quality/item_differences.png)

Figure 2b. Original-minus-AI differences for the composite and each item, with unadjusted 95% confidence intervals.

Only clarity stayed below the corrected threshold. These tests follow up H2 and are not additional planned hypotheses. Because the same respondents rated all three correlated items, Bonferroni is conservative here.

### Quality by student background (exploratory)

We compared the paired quality difference between groups to check that the combined result was not hiding opposing patterns, as in Simpson's paradox. The original advantage was 0.405 for international students (n = 14; 95% CI [-0.125, 0.934]; p = .123) and 0.583 for domestic students (n = 12; 95% CI [0.210, 0.957]; p = .00557), so both groups point in the same direction. The groups did not differ reliably: Welch t(22.4) = 0.599, p = .555, with a 95% confidence interval for the international-minus-domestic difference of [-0.796, 0.439]. Levene's test did not indicate unequal variances, p = .477, and Mann-Whitney gave U = 103, p = .333. Subgroups this small cannot show that the groups respond alike.

### Exploratory regression

AI-use and English reading proficiency were absent from the export, so the originally proposed regression cannot be fitted. They must not be inferred from student background or replaced with invented covariates. We instead fit an exploratory multiple linear regression of the original-minus-AI difference on predictors that were collected: international background (1 = international, 0 = domestic), correct detection (1 = correct), and detection confidence (1 to 5).

| Term | Estimate | SE | t(22) | p | 95% CI |
|---|---:|---:|---:|---:|---:|
| Intercept | 1.929 | 0.795 | 2.427 | .0239 | [0.281, 3.576] |
| International | -0.238 | 0.366 | -0.650 | .522 | [-0.998, 0.522] |
| Correct detection | -0.036 | 0.395 | -0.090 | .929 | [-0.855, 0.783] |
| Confidence | -0.393 | 0.220 | -1.784 | .0883 | [-0.850, 0.064] |

The model did not explain significant variation, F(3, 22) = 1.262, p = .312, R-squared = .147, adjusted R-squared = .031. Residual plots showed no clear pattern, Shapiro-Wilk on the residuals did not reject normality, W = .959, p = .376, and Breusch-Pagan did not indicate unequal residual variance, LM = 4.874, p = .181. With 26 respondents and three predictors the estimates are imprecise, so these nonsignificant coefficients do not show that the predictors are unrelated to the difference.

![Regression residuals versus fitted values and normal quantile plot](../results/quality/regression_residuals.png)

Figure 2c. Residual diagnostics for the exploratory regression.

### Sensitivity analyses

| Analysis | n | Original minus AI | 95% CI | t | p | dz |
|---|---:|---:|---:|---:|---:|---:|
| Primary: students, both checks correct | 26 | 0.487 | [0.175, 0.799] | 3.213 | .0036 | 0.630 |
| Omitting the legacy record | 25 | 0.507 | [0.184, 0.830] | 3.238 | .00351 | 0.648 |
| Planned check rule, all 64 submissions | 59 | 0.390 | [0.178, 0.602] | 3.676 | .00052 | 0.479 |
| Planned check rule, 54-response snapshot | 49 | 0.415 | [0.167, 0.663] | 3.369 | .00149 | 0.481 |

Reversing the legacy record's version labels did not change the composite comparison because its two composite scores were equal. The direction and significance of the composite difference are therefore stable across the exclusion rules and version sensitivities, while the estimate ranges from 0.390 to 0.507.

The item-level pattern was not stable. In the 49-response snapshot analysis, engagement and overall writing met the corrected threshold and clarity did not, the reverse of the primary result, so no individual item should be singled out. That analysis also gave W = 94.0, p = .00242 for the composite Wilcoxon sensitivity. We reproduced its 49 retained responses, composite difference and detection counts independently from the first 54 rows of the workbook.

### H3: Overall detection

One forced choice per retained respondent was coded correct under the current AI-first mapping. The chi-square goodness-of-fit test compares correct and incorrect counts with n/2 in each cell; both expected counts are 13. The test assumes independent participant responses, and it tests detection against .50 instead of comparing passage ratings. There is no post hoc test for this binary outcome. We report a t-based 95% confidence interval on the 0/1 scores, which is approximate with a binary outcome at this sample size.

Ten of 26 students correctly selected Passage 1, while 16 selected Passage 2. Accuracy was 38.5%, 95% confidence interval [18.4%, 58.5%], or 11.5 percentage points below chance. The test gave chi-square(1) = 1.385, p = .239, so we fail to reject H0.

![Overall detection accuracy against chance](../results/quality/overall_detection.png)

Figure 3. Overall detection accuracy with a t-based 95% confidence interval. The dashed line is chance, and the interval includes it.

| Sensitivity | n | Correct | Chi-square p |
|---|---:|---:|---:|
| Omitting the legacy record | 25 | 9 | .162 |
| Reversing the legacy record | 26 | 9 | .117 |
| Planned check rule, students | 27 | 11 | .336 |
| Planned check rule, all respondents | 59 | 21 | .0269 |
| Planned check rule, 54-response snapshot | 49 | 18 | .0633 |

No analysis of students approached the .0167 threshold. The all-respondent analysis, which includes non-students, had accuracy below chance, 35.6%, at a p-value above that threshold.

### Confidence (exploratory)

Confidence is ordinal from 1 (Just guessing) to 5 (Extremely confident), not a probability estimate. Mean confidence was 3.31, with a median of 3. Correct respondents (n = 10) averaged 3.00, and incorrect respondents (n = 16) averaged 3.50. A two-sided Mann-Whitney comparison gave U = 55.5, p = .141. This test compares confidence distributions and is not presented as a direct test of mean equality. No probability-calibration claim can be made from this verbal five-point scale.

Optional explanations were not formally coded or treated as validated authorship cues. Failure to reject does not establish equivalence. The aggregate results are in results/quality/hypothesis_tests.json; no names or free text are published.

## Interpretation of results

### H1: Student-background findings

In this sample, international students chose the AI passage far more often than domestic students. The result supports a difference between these groups in what they chose, and it is the most interesting finding of the study, but it does not establish that international students are better at detecting AI.

Three things limit that claim. First, the AI passage was always first, so a correct answer was the same as choosing Passage 1; the groups may differ in their tendency to pick the first passage and not in their ability to recognize AI. Second, the groups are small, and the result weakens without the last ten responses, which arrived close together, although the team reports that they came from different people. Third, the written plan labelled this comparison exploratory, so it is better treated as a strong lead for a randomized follow-up than as a settled result.

Student background was observed and not assigned, so the comparison cannot establish that background caused the difference. Background also does not measure English proficiency, which was not collected.

### H2: Quality findings

The original passage received higher quality ratings among the student respondents, with a mean advantage of about half a scale point and a standardized paired difference of 0.63. The result kept its direction and significance under the planned, broader exclusion rule, where the estimate was somewhat smaller. Both passages still received relatively high ratings. Statistical significance does not establish that every reader preferred the original: 15 of 26 rated it higher and eight rated the versions equally. Nor does it show that this magnitude would matter in every application.

We would not single out one rating as the source of the difference. Clarity alone survived correction here, but a different pair of items did so in the 49-response snapshot, which suggests that the item-level pattern depends on who is included. Clarity was also only weakly related to overall writing, so readers may treat being easy to understand and being well written as different qualities, although these data cannot establish why. The student-background comparison and the regression found no reliable differences, but their small samples leave wide intervals, so they do not show that those factors are irrelevant.

The result does not establish that human authorship caused the higher ratings. Every verified response saw the AI rewrite first and the original second, so version and position are confounded. Readers met the same information a second time when rating the original, and familiarity or contrast could have shifted those ratings regardless of who wrote the text. The supported claim is narrower: in this order, with this passage pair, student respondents rated the second passage (the original) higher.

### H3: Overall detection and confidence findings

Students more often identified the original as AI-written, but the interval includes .50. The appropriate conclusion is uncertain detection performance for this pair, not demonstrated equivalence to chance or a universal inability to detect AI. With 26 students, the test could detect only large departures from chance.

Confidence did not reliably separate correct and incorrect choices. Respondents with greater confidence were not reliably more accurate, but this uncertainty does not prove the absence of an association. These results support keeping perceived writing quality, authorship judgments, and confidence conceptually separate. All conclusions concern this particular passage pair under fixed presentation order.

## Limitations

### Ratings and data

The fixed order bears directly on H2 because the quality difference cannot be separated from the effect of rating a passage second. The stricter comprehension rule was adopted after earlier results had been seen, so it cannot be treated as a prospective decision, even though the composite result did not depend on it. Restricting the sample to students reduced it from 64 to 26, which lowers power, widens intervals and limits conclusions to the student respondents. The three ratings agreed only partly, especially clarity and overall writing, so the composite combines qualities that readers may judge differently. We kept it because H2 was defined on it, and the item-level results are reported alongside it.

The three bounded rating items are subjective, and the t-test treats seven-point ratings and their averages as interval measures. Scores near the top of the scale can compress differences between versions. The nonparametric sensitivity is relevant but does not test exactly the same mean hypothesis. The item-level tests, subgroup check and regression are retrospective and exploratory, and they share the position confound.

Duplicate-person status could not be verified, and repeated answer patterns were retained. The team reports that no pilot responses were collected. Age, passage-page timing, AI-use and English proficiency were not collected in the export, preventing the proposed timing exclusion and the proposed covariate regression. Optional names made some responses identifiable, and early anonymous and later identified records followed different notices.

### Stimulus, design and sampling

The most important limitation is fixed order. Because the AI passage was always first, detection correctness is the same as choosing Passage 1, so the H1 group difference cannot be separated from a group difference in preferring the first passage. Fixed AI-first order also confounds version with presentation position and permits carryover, familiarity and contrast effects. Both passages repeat the same information, so the second exposure may benefit comprehension or familiarity irrespective of authorship. One science topic and one rewrite do not represent human or AI prose generally. The texts share a direct scientific quotation. The rewrite took two prompts rather than the single first output the plan called for, and its generation date was not recorded. Plain formatting reduced external source cues but did not remove textual NIH references.

Recruitment was voluntary through a shared link, with a convenience sample, and the student groups are small and were not randomized. Ten of the 26 analyzed responses arrived within about 15 minutes, and H1 does not reach the threshold without them. The team reports that these were different people and not a single class or group, but the anonymous data cannot verify this, and respondents who discussed the study would violate independence. The sample cannot estimate population-wide detection performance. Eligibility and the name question changed during launch, and one record lacks verified passage assignment. Student-background and current-status answers did not align exactly, and analyses restricted to stated Student status have different denominators. Background must not be used as a proxy for citizenship, nationality or language proficiency.

The group comparison and its test were specified before collection, but the written plan labelled it exploratory, and the decision to report it first, the three-test threshold, and the power sensitivities are retrospective and cannot be described as preregistered. The team reports that the instructor accepted the initial nondisclosure; no separate ethics review is documented. These limits should remain visible in both the written report and presentation.

## Conclusion and recommendations

International students in this sample identified the AI passage far more often than domestic students, 9/14 versus 1/12. Because the AI passage was always first, this may reflect a preference for the first passage, and the result weakens without the last ten responses, so we do not conclude that international students are better at detecting AI. Students rated the original higher than the rewrite, a result that held across the examined exclusion rules but is also confounded with position. Overall detection did not differ reliably from chance. These findings concern this fixed-order passage pair and sampled respondents.

The priority for a follow-up is to retest the group difference with randomized passage order, so that a correct answer no longer means choosing the same position. It should recruit enough students in each group, roughly 50 per group for a 30-point gap at .05, use multiple independently selected passage pairs, preserve model and prompt provenance, and freeze eligibility, exclusions, and the testing policy before recruitment. It should also measure English proficiency, so that background and reading proficiency can be distinguished. If reading-time exclusions or order blocking are essential, use a platform that records those features. Keep names separate from analytical data when participation tracking is needed. Record each respondent's passage order with the response, so that no record's version is left unverified as one was here.

## References

Gao, C. A., Howard, F. M., Markov, N. S., Dyer, E. C., Ramesh, S., Luo, Y., & Pearson, A. T. (2023). Comparing scientific abstracts generated by ChatGPT to real abstracts with detectors and blinded human reviewers. npj Digital Medicine, 6, 75. https://doi.org/10.1038/s41746-023-00819-6

Jakesch, M., Hancock, J. T., & Naaman, M. (2023). Human heuristics for AI-generated language are flawed. Proceedings of the National Academy of Sciences, 120(11), e2208839120. https://doi.org/10.1073/pnas.2208839120

National Institutes of Health. (2013, April). Sleep On It. NIH News in Health. https://newsinhealth.nih.gov/2013/04/sleep-it

SciPy developers. (n.d.). Statistical functions and distribution documentation for ttest_rel, ttest_ind, chisquare, shapiro, levene, wilcoxon, nct, binom, fisher_exact, and mannwhitneyu. https://docs.scipy.org/doc/scipy/reference/stats.html

SciPy developers. (n.d.). Fisher exact test. https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.fisher_exact.html

SciPy developers. (n.d.). Mann-Whitney U test. https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html

statsmodels developers. (n.d.). statsmodels documentation: ordinary least squares and regression diagnostics. https://www.statsmodels.org/stable/index.html

## Reproducibility and contribution note

The earlier 54-response snapshot used Python 3.10, NumPy 2.2.6, and SciPy 1.15.3; the current analyses use the same NumPy and SciPy versions under Python 3.13. The repository includes executable analysis and power scripts, aggregate JSON outputs, de-identified data, and reproduction instructions. Original exports with names and free text are withheld from GitHub. The report records a November 2 download, and the form has since been closed. AI assistance was used to prepare code and report text; the project members are responsible for reviewing the analysis, references, and final submission.

Section files are stitched in the course order by make report. AGENTS.md lists which member owns each section.
