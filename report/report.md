# Perceived writing quality and AI detection in a sleep and memory passage study

Debshree Chowdhury and Jakub Romańczuk

AIPI 510 Term 2 Project

Response snapshot analyzed November 2, 2026

## Abstract

We compared perceived writing quality and AI identification for an original NIH News in Health passage and an AI rewrite about sleep and memory. Participants read both versions, rated clarity, engagement, and overall writing on seven-point scales, answered comprehension checks, and identified the AI passage. The circulated form presented AI first and the original second. Of 54 submissions, five failed both comprehension checks, leaving 49 complete paired responses. Mean composite quality was 5.83 for the original and 5.41 for the AI rewrite. The original-minus-AI difference was 0.415 points, 95% confidence interval [0.167, 0.663], t(48) = 3.369, p = .00149, Cohen dz = 0.481. AI detection accuracy was 36.7% (18/49), with an exact 95% confidence interval of [23.4%, 51.7%]; the exact binomial test did not reject chance performance, p = .0854. Quality findings were stable in legacy-response and nonparametric sensitivity analyses, whereas detection depended on one response's uncertain version. Fixed order, one passage pair, convenience sampling, and questionnaire changes during collection limit generalization. The results support a quality-rating difference for this pair, while leaving detection performance uncertain.

## Background and motivation

Readers encounter AI-assisted prose in educational and scientific communication. Two questions arise: whether a rewrite changes perceived quality and whether readers can recognize its origin. These outcomes need separate measurement. A passage can be judged clear or engaging while its authorship is misclassified; neither judgment alone establishes factual accuracy or learning.

Prior work provides reasons to avoid assuming reliable human detection. Jakesch, Hancock, and Naaman (2023) found that judgments of AI-generated self-presentations relied on imperfect linguistic heuristics. Gao et al. (2023) examined scientific abstracts using blinded reviewers and found both missed generated texts and false accusations against original texts. Their tasks and materials differ from this study, so their detection rates are not directly comparable with a forced choice between two closely related passages.

We used an excerpt from NIH News in Health's April 2013 article Sleep On It and an AI rewrite of the same content (National Institutes of Health, 2013). Keeping the topic and principal information similar supports a focused comparison of prose. This study evaluates perceived writing and source identification; it does not test the underlying sleep science or memory performance.

## Null and alternative hypotheses

### H1: Perceived quality

H0: among current students, the population mean original-minus-AI composite quality difference equals zero. H1: the difference is nonzero. The test is two-sided.

### H2: Detection against chance

H0: the probability of correctly identifying the AI passage is .50. H2: that probability differs from .50. This is a two-sided question; the data do not justify choosing a one-sided direction after inspection. It is separate from H1, the quality comparison.

### H3: Detection by student background

For this draft, H0: detection correctness is independent of self-reported international versus domestic student background (population odds ratio = 1). H3: correctness differs between these backgrounds (odds ratio ≠ 1). The original instrument included this grouping question, but no numbered H3 was recorded in the existing plan. This operational definition is provisional pending team confirmation and is a retrospective exploratory analysis, not a new confirmatory claim. Respondents answering Not applicable do not enter this comparison. Background labels are self-reports, not verified citizenship or English proficiency.

### Testing policy

H1 and H2 retain the originally proposed nominal .05 threshold, with a retrospective two-test Bonferroni sensitivity threshold of .025. H3, the participant-status comparison and confidence analyses are exploratory; their p-values are descriptive and unadjusted, not additional confirmatory discoveries. If the team elects to treat all three hypotheses as one confirmatory family in a future study, it should prospectively specify that policy and plan sample size at .05/3. All displayed 95% intervals are marginal, not simultaneous familywise intervals.

## Description of experimental design

This was a within-person paired comparison. The independent variable was passage version: original or AI rewrite. The original was the comparison condition. Dependent variables were clarity, engagement, and overall writing ratings, each from 1 (Not at all) to 7 (Extremely); their mean formed the quality composite. Detection correctness was coded 1 or 0, and confidence ranged from 1 to 5. Participant status and student background described the sample. Optional names were collected separately from the analytic variables.

The form introduced two short science-news passages without announcing AI authorship. Each passage page contained the three ratings and the same comprehension question about the approximately 90-minute sleep cycle. A later page disclosed that one text had been rewritten and requested a forced choice, confidence, and an optional explanation. The answer key, source, rationale for initial nondisclosure, and study contacts appeared after submission. Response editing was disabled.

The circulated form presented AI as Passage 1 and the original as Passage 2. No evidence supports randomized order or balanced allocation in these responses. Consequently, version and position are confounded. Both passages used the same plain-text presentation without separate source branding, but textual NIH references and the shared scientific quotation remained. The rewrite's model, model version, and complete original generation prompt were not preserved in the analyzed export, limiting stimulus reproducibility.

Participation was voluntary through a shared online link, yielding a convenience sample. Eligibility changed from graduate students to students, working professionals, and others aged at least 18. The adult restriction was an instruction; the export contains no recorded age verification. One retained record still has the older affirmative status answer. The report evaluates the downloaded snapshot rather than asserting that collection had closed.

For detection, each person contributed one forced-choice outcome and one confidence response. The paired structure applies to passage ratings, not two independent detection observations. Background and employment/student status were observed characteristics rather than randomized treatments. Group comparisons therefore describe associations and cannot establish a causal effect of background. The presentation and report use the same November 2 snapshot; collection was not stopped by this analysis.

## Power analysis

### H1: Paired quality planning

Power calculations were prepared after collection began. They are planning sensitivities under assumed effects, not prospective justification, observed power, or evidence of preregistration. The initial n = 30 scenario refers to complete pairs. We used Python 3.10 and SciPy 1.15.3. The paired-t calculation uses the noncentral t distribution: the noncentrality is the assumed standardized paired difference multiplied by the square root of the number of complete pairs, with n minus one degrees of freedom. Cohen dz uses the standard deviation of within-person differences, not the pooled standard deviation of the two passages.

| Assumed absolute dz | Pairs for 80% power at .05 | Power with 30 pairs at .05 | Pairs for 80% power at .025 |
|---|---:|---:|---:|
| 0.30 | 90 | 35.5% | 109 |
| 0.50 | 34 | 75.4% | 41 |
| 0.80 | 15 | 98.8% | 18 |

No attrition allowance was specified prospectively. For illustration, 34 usable pairs with a 10% allowance would require 38 recruits, calculated by dividing 34 by .90 and rounding up. This is a planning example, not a claim about the actual recruitment target. The report does not compute power from the observed effect.

### H1: Sensitivity at the achieved sample

The analyzed sample has 26 complete pairs, below both the initial n = 30 scenario and the 34 pairs needed for 80% power at an assumed dz of 0.50. With 26 pairs and 80% power, the smallest detectable standardized paired difference is about dz = 0.57 at .05 and dz = 0.64 at the retrospective .025 threshold. Power at .05 and .025 is 31.3% and 21.6% for an assumed dz of 0.30, 68.8% and 57.1% for 0.50, and 97.5% and 94.8% for 0.80. These values use assumed effects at the achieved sample size, not the observed effect, so they describe what the design could detect and not the strength of the observed result. They were calculated with the same SciPy version under Python 3.13. The study is therefore poorly placed to detect small differences, and a nonsignificant follow-up in this sample does not show that a difference is absent.

### H2: Detection planning

All power calculations were made after collection began and are illustrative planning sensitivities, not prospective justification or observed power. Python 3.10, NumPy 2.2.6 and SciPy 1.15.3 were used. For H2, scripts/report_power.py sums exact binomial alternative probabilities in the two-sided rejection region of a test against .50. Independent, identically distributed participant choices are assumed. Target power is .80; complete cases, rather than recruits, determine n.

| Assumed true accuracy | First n with 80% power at .05 | Power at n = 30, .05 | First n with 80% power at .025 |
|---|---:|---:|---:|
| .60 | 199 | 17.7% | 240 |
| .70 | 49 | 58.9% | 58 |
| .80 | 20 | 93.9% | 24 |

These rates are assumed alternatives, not estimates used to calculate post hoc observed power. Exact rejection regions change discretely: the first qualifying n does not imply that every larger n attains the target. The .025 column corresponds to the retrospective H1/H2 sensitivity policy.

### H3: Between-group detection planning

scripts/group_power.py enumerates independent binomial counts for two equally sized groups and sums their joint probabilities whenever the two-sided probability-ordered Fisher exact p-value is at most .05. Conditional hypergeometric probabilities define the Fisher rejection region; the alternative counts are sampled from assumed group-specific binomial rates. This calculation uses actual Fisher rejection rules rather than a large-sample chi-square approximation.

| Assumed accuracies | Power: 15 per group | Power: 30 per group | Power: 50 per group | Power: 100 per group |
|---|---:|---:|---:|---:|
| .40 vs .60 | 9.5% | 25.7% | 46.2% | 78.7% |
| .30 vs .60 | 22.7% | 56.1% | 82.9% | 98.9% |
| .30 vs .70 | 43.4% | 83.8% | 97.9% | >99.9% |

For an assumed 30-percentage-point gap, 50 complete respondents in each group reach .80 power in this scenario table. This is an example for a future study, not a retrospective recruitment target. The present background groups (11 and 6 under the broad self-report definition) are much smaller and unbalanced. Balanced future recruitment, an attrition allowance, and any multiplicity adjustment should be specified before recruitment. Power planning cannot correct fixed-order confounding or convenience sampling.

## Data collection and cleaning procedures

The analyzed Google Forms workbook contained 64 submissions dated October 31 to November 2, 2026 in the export's timestamp labels. All 64 affirmed consent. Status was Working professional for 36, Student for 25, Other for two, and the legacy Yes for one. Student background was international for 15, domestic for 14, and not applicable for 35. Thirty-six names and 21 optional explanations were supplied. Ten of the 64 arrived after the earlier 54-response snapshot, within about 15 minutes on November 2; all ten were students.

We preserved the downloaded workbook unchanged in local restricted storage and recorded its SHA-256 checksum in the aggregate results. A script converts it to a private CSV, and the importer then keeps only reviewed columns by position, because both passage blocks use the same question labels. Names, timestamps, and participant explanations are discarded at that step and appear in no repository output. Ratings, comprehension responses, confidence, consent, and detection were complete. No missing values were imputed.

We applied two exclusion rules. First, we kept only respondents who reported being an international or domestic student, because the comparison of interest is between those groups; the 35 who answered "Not applicable — not currently a student" were removed. Second, we required the correct answer, 90 minutes, on both comprehension checks, treating any wrong answer as evidence that the passage may not have been read carefully. Of the 29 student-background respondents, two missed both checks and one missed one, leaving 26 for analysis: 14 international and 12 domestic. By stated status, these were 23 Student, two Working professional, and the one legacy Yes. Status and student background did not align exactly, and we used the student-background answer for the rule.

| Step | Removed | Remaining |
|---|---:|---:|
| Submissions | | 64 |
| Not currently a student | 35 | 29 |
| Both comprehension checks wrong | 2 | 27 |
| One comprehension check wrong | 1 | 26 |

These rules are retrospective. They were adopted on November 2, after the 54-response results had been seen, and they replace a proposed rule that removed a respondent only if both checks were wrong. We therefore also report the earlier rule as a sensitivity analysis. Across all 64 submissions, six missed the first check, six missed the second, and five missed both, so the earlier rule retains 59.

No timing exclusion was applied because Google Forms did not collect passage-page times. No verified pilot or duplicate-person labels were available, so no such records were removed. Four answer patterns repeated across the 64 submissions, two of them among the 26 retained; matching answers do not establish repeated participation.

The primary mapping assumes the current AI-first version for all retained responses. The legacy record's version cannot be verified from the export alone, so we report analyses omitting it and reversing its version mapping, rather than selecting a treatment based on statistical significance. Any request to identify a submitted response would require a separately protected record. Questionnaire revisions and the lack of a verified prospective registration are documented as limitations.

## Statistical analysis

### H1: Quality analysis

For each participant and version, quality was the arithmetic mean of all three ratings. We calculated the original-minus-AI paired difference, its standard deviation, a two-sided paired t-test, a t-based 95% confidence interval, and Cohen dz. A paired t-test fits because each participant rated both versions, so the differences within people are the unit of analysis. We summarized how closely the three ratings agreed using descriptive pairwise correlations within each version. A two-level paired comparison needs no post hoc test between versions; item-level follow-ups are reported below.

We examined the distribution of paired differences with a histogram, a quantile plot, and Shapiro-Wilk. Independence depends on recruitment and duplicate review and cannot be established by this test. Shapiro-Wilk did not reject normality, W = .938, p = .119, although with 26 pairs it has limited power, and the bounded scales and eight tied differences warranted a Wilcoxon signed-rank sensitivity analysis. Mathematical ties were preserved by rounding differences to ten decimal places; its p-value uses a normal approximation with zeros omitted. This test has different assumptions and does not directly test the identical population-mean hypothesis.

![Paired difference histogram and normal quantile plot](../results/quality/difference_diagnostics.png)

Figure 1a. Diagnostic views of the 26 original-minus-AI composite differences. Eight respondents rated the two versions equally.

### Quality results

| Outcome | AI mean | Original mean | Original minus AI |
|---|---:|---:|---:|
| Clarity | 5.923 | 6.423 | 0.500 |
| Engagement | 5.154 | 5.692 | 0.538 |
| Overall writing | 5.346 | 5.769 | 0.423 |
| Composite quality | 5.474 | 5.962 | 0.487 |

Composite standard deviations were 0.828 for AI and 0.568 for the original. The standard deviation of paired differences was 0.773. The paired test gave t(25) = 3.213, p = .0036, with 95% confidence interval [0.175, 0.799] for the original advantage and dz = 0.630. The p-value also meets the retrospective two-test Bonferroni threshold of .025. Original quality was higher for 15 participants, AI quality was higher for three, and eight tied. The Wilcoxon sensitivity agreed, W = 22.5, p = .00579.

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

Figure 1b. Original-minus-AI differences for the composite and each item, with unadjusted 95% confidence intervals.

Only clarity stayed below the corrected threshold. These tests follow up H1 and are not additional primary hypotheses. Because the same respondents rated all three correlated items, Bonferroni is conservative here.

### Student-background subgroup check

We compared the paired difference between groups to check that the combined result was not hiding opposing patterns, as in Simpson's paradox. The original advantage was 0.405 for international students (n = 14; 95% CI [-0.125, 0.934]; p = .123) and 0.583 for domestic students (n = 12; 95% CI [0.210, 0.957]; p = .00557), so both groups point in the same direction. The groups did not differ reliably: Welch t(22.4) = 0.599, p = .555, with a 95% confidence interval for the international-minus-domestic difference of [-0.796, 0.439]. Levene's test did not indicate unequal variances, p = .477, and Mann-Whitney gave U = 103, p = .333. Subgroups this small cannot show that the groups respond alike.

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

Figure 1c. Residual diagnostics for the exploratory regression.

### Sensitivity analyses

| Analysis | n | Original minus AI | 95% CI | t | p | dz |
|---|---:|---:|---:|---:|---:|---:|
| Primary: students, both checks correct | 26 | 0.487 | [0.175, 0.799] | 3.213 | .0036 | 0.630 |
| Omitting the legacy record | 25 | 0.507 | [0.184, 0.830] | 3.238 | .00351 | 0.648 |
| Earlier rule, all 64 submissions | 59 | 0.390 | [0.178, 0.602] | 3.676 | .00052 | 0.479 |
| Earlier rule, 54-response snapshot | 49 | 0.415 | [0.167, 0.663] | 3.369 | .00149 | 0.481 |

Reversing the legacy record's version labels did not change the composite comparison because its two composite scores were equal. The direction and significance of the composite difference are therefore stable across the exclusion rules and version sensitivities, while the estimate ranges from 0.390 to 0.507.

The item-level pattern was not stable. In the earlier 49-response analysis, engagement and overall writing met the corrected threshold and clarity did not, the reverse of the primary result, so no individual item should be singled out. That analysis also gave W = 94.0, p = .00242 for the composite Wilcoxon sensitivity. We reproduced its 49 retained responses, composite difference and detection counts independently from the first 54 rows of the workbook.

### H2: Detection methods and results

One forced choice per retained respondent was coded correct under the current AI-first mapping. The proposed chi-square goodness-of-fit test compares correct/incorrect counts with n/2 in each cell; both expected counts are 24.5. We also use the two-sided exact binomial test, its Clopper-Pearson 95% interval, and Cohen w = sqrt(chi-square/n). These tests assume independent participant responses. They test detection against .50 rather than compare passage ratings. There is no pairwise post hoc test for this binary outcome.

Eighteen of 49 respondents correctly selected Passage 1 under the current mapping, while 31 selected Passage 2. Accuracy was 36.7%, exact 95% confidence interval [23.4%, 51.7%]. The exact binomial p-value was .0854. The chi-square test gave chi-square(1) = 3.449, p = .0633, with Cohen w = 0.265. Neither test rejected the chance null at .05.

| Version sensitivity | n | Correct | Exact detection p | Chi-square p |
|---|---:|---:|---:|---:|
| Current mapping | 49 | 18 | .0854 | .0633 |
| Omit legacy response | 48 | 17 | .0595 | .0433 |
| Legacy response original first | 49 | 17 | .0444 | .0321 |

Detection is sensitive to the legacy record and test choice. None of these detection p-values meets .025. The unfiltered exact p-value of .0402 from 54 submissions is not the result after the planned comprehension exclusion. It would be misleading to report that unfiltered finding as the cleaned analysis.


![Detection accuracy and chance reference](../results/figures/detection.png)

Figure 2. AI-identification accuracy and exact 95% interval from the retained snapshot. The dashed line is chance; the interval includes it.

### H3: Student-background comparison

The broad comparison uses the background question as answered, regardless of a respondent’s separate current-status answer. Eleven retained respondents selected international and six domestic; 32 selected Not applicable. Because some cells are sparse, we use a two-sided Fisher exact test, not a large-sample chi-square independence test. The table columns are correct and incorrect. We report the conditional odds ratio for the first group relative to the second, with exact conditional 95% limits, and each accuracy with an exact binomial interval. These are associations in a convenience sample. H3 is retrospective and its label awaits team confirmation.

| Background | Correct | Incorrect | Accuracy | Exact 95% CI |
|---|---:|---:|---:|---|
| International | 7 | 4 | 63.6% | 30.8%–89.1% |
| Domestic | 1 | 5 | 16.7% | 0.4%–64.1% |

Fisher p = .1312; conditional odds ratio = 7.63, exact 95% CI [0.56, 471.48]. The descriptive risk difference is 47.0 percentage points. The very wide interval includes odds ratio 1, so this is not reliable evidence of a background difference. Background is not a measured language-proficiency scale.

A stricter sensitivity includes only respondents who also selected Student as their current status: 4/8 international and 1/5 domestic, Fisher p = .5649, conditional odds ratio = 3.60, 95% CI [0.21, 245.34]. One of the 14 students answered Not applicable. The broad background comparison includes four respondents outside this strict student subset; this illustrates the ambiguity of overlapping work/study roles and the changed instrument. Omitting the legacy response yields Fisher p = .1451; reversing its detection mapping yields p = .3043. Neither resolves the small-sample uncertainty.

### Other group comparison

The separate Student versus Working professional comparison gives 5/14 (35.7%) versus 11/33 (33.3%) correct. The Other response and legacy Yes response are omitted from this specific comparison, not from the full study. Fisher p = 1.000; conditional odds ratio = 1.11, 95% CI [0.23, 4.85]; the descriptive difference is 2.4 percentage points. This explicitly defined two-group comparison does not collapse Other into an arbitrary category or apply Fisher’s 2-by-2 procedure to a three-category table.

![Detection accuracy by reported background and status](../results/figures/detection_groups.png)

Figure 3. Group accuracies with exact marginal 95% intervals. Background and current-status panels use overlapping respondents and different denominators; they are not four independent groups.

### Confidence

Confidence is ordinal from 1 (Just guessing) to 5 (Extremely confident), not a probability estimate. Mean confidence was 3.16, with a median of 3. Correct respondents (n = 18) averaged 3.06, and incorrect respondents (n = 31) averaged 3.23; both medians were 3. A two-sided Mann-Whitney comparison, using the tie-corrected asymptotic distribution and continuity correction, gave U = 253.0, p = .5487. The rank-biserial effect for correct minus incorrect confidence was -.093. This test compares confidence distributions and is not presented as a direct test of mean equality.

Spearman rho between confidence and correctness was -.0883 (asymptotic p = .5465). Because the sample is small and heavily tied, we also permuted correctness labels 99,999 times with seed 510; the two-sided absolute-rho p-value, with a plus-one correction, was .5378. This permutation assumes exchangeability under the null. The two summaries describe the same underlying relationship and are not independent confirmations. Omitting or reversing the legacy response left the confidence conclusion unchanged (Mann-Whitney p = .5842/.6086; permutation p = .5975/.6216). No probability-calibration claim can be made from this verbal five-point scale.

Optional explanations were not formally coded or treated as validated authorship cues. All added group and confidence tests are exploratory with unadjusted p-values. Failure to reject does not establish equivalence, particularly for the small background groups. The aggregate evidence and chart inputs are in results/debshree_statistics.json; no names or free text are published.

## Interpretation of results

### Quality findings

The original passage received higher quality ratings among the student respondents, with a mean advantage of about half a scale point and a standardized paired difference of 0.63. The result kept its direction and significance under the earlier, broader exclusion rule, where the estimate was somewhat smaller. Both passages still received relatively high ratings. Statistical significance does not establish that every reader preferred the original: 15 of 26 rated it higher and eight rated the versions equally. Nor does it show that this magnitude would matter in every application.

We would not single out one rating as the source of the difference. Clarity alone survived correction here, but a different pair of items did so under the earlier rule, which suggests that the item-level pattern depends on who is included. Clarity was also only weakly related to overall writing, so readers may treat being easy to understand and being well written as different qualities, although these data cannot establish why. The student-background comparison and the regression found no reliable differences, but their small samples leave wide intervals, so they do not show that those factors are irrelevant.

The result does not establish that human authorship caused the higher ratings. Every verified response saw the AI rewrite first and the original second, so version and position are confounded. Readers met the same information a second time when rating the original, and familiarity or contrast could have shifted those ratings regardless of who wrote the text. The supported claim is narrower: in this order, with this passage pair, student respondents rated the second passage (the original) higher.

### Detection, group and confidence findings

Respondents more frequently identified the original as AI-written under the current mapping. Yet the cleaned exact interval includes .50, and the legacy-version sensitivities change nominal detection significance. The appropriate conclusion is uncertain detection performance for this pair, not demonstrated equivalence to chance or universal inability to detect AI. The lower unfiltered p-value must not replace the comprehension-filtered result.

The international-background group had higher descriptive accuracy, but the small cells, wide conditional odds-ratio interval, and sensitivity to group definition prevent a firm population claim. The employment/student comparison likewise supplies no clear evidence of different detection rates. Neither analysis identifies a causal effect or measures English proficiency. A difference between one significant and one nonsignificant within-group test would not establish a between-group difference; the direct Fisher comparisons answer that question here.

Confidence did not meaningfully separate correct and incorrect choices in this snapshot. Respondents with greater confidence were not reliably more accurate, but the uncertainty does not prove the absence of an association. These results support keeping perceived writing quality, authorship judgments and confidence conceptually separate. All conclusions concern this particular passage pair under fixed presentation order.

## Limitations

### Ratings and data

The fixed order bears directly on H1 because the quality difference cannot be separated from the effect of rating a passage second. The exclusion rules were adopted retrospectively, after earlier results had been seen, so they cannot be treated as prospective decisions even though the composite result did not depend on them. They also reduced the sample from 64 to 26, which lowers power, widens intervals and limits conclusions to the student respondents. The three ratings agreed only partly, especially clarity and overall writing, so the composite combines qualities that readers may judge differently. We kept it because H1 was defined on it, and the item-level results are reported alongside it.

The three bounded rating items are subjective, and the t-test treats seven-point ratings and their averages as interval measures. Scores near the top of the scale can compress differences between versions. The nonparametric sensitivity is relevant but does not test exactly the same mean hypothesis. The item-level tests, subgroup check and regression are retrospective and exploratory, and they share the position confound.

Duplicate-person, pilot and test-response status could not be verified; repeated answer patterns were retained. Ten responses arrived within a short window, so some respondents may have been recruited together and their answers may not be fully independent. Age, passage-page timing, AI-use and English proficiency were not collected in the export, preventing the proposed timing exclusion and the proposed covariate regression. Optional names made some responses identifiable, and early anonymous and later identified records followed different notices.

### Stimulus, design and sampling

Fixed AI-first order confounds version with presentation position and permits carryover, familiarity and contrast effects. Both passages repeat the same information, so the second exposure may benefit comprehension or familiarity irrespective of authorship. One science topic and one rewrite do not represent human or AI prose generally. The texts share a direct scientific quotation, and the model, version and full generation prompt were not preserved in the export. Plain formatting reduced external source cues but did not remove textual NIH references.

Recruitment was voluntary through a shared link, with a convenience sample dominated by working professionals. The sample cannot estimate population-wide detection performance. Eligibility and the name question changed during launch, and one record lacks verified passage assignment. Student-background and current-status answers did not align exactly; broad and strict subgroup definitions lead to different denominators. Groups are small, unbalanced and nonrandomized; their wide intervals preclude strong claims about international/domestic backgrounds or work/student status. Background must not be used as a proxy for citizenship, nationality or language proficiency.

The snapshot does not establish that collection ended. Hypothesis numbering, the added H3 group comparison, power sensitivities and multiplicity handling are retrospective. The draft H3 definition requires team confirmation and cannot be described as preregistered. Instructor or ethics approval for initial nondisclosure is not established by the available records and is not claimed. These limits should remain visible in both the written report and presentation.

## Conclusion and recommendations

In this response snapshot, the original sleep-and-memory passage received higher composite quality ratings than its AI rewrite, and this difference persisted across the examined sensitivities. Cleaned detection accuracy was below .50 numerically but did not provide stable evidence of a difference from chance. These findings concern this fixed-order passage pair and sampled respondents.

A follow-up should randomize passage order, use multiple independently selected passage pairs, preserve model and prompt provenance, and freeze eligibility, exclusions, and the testing policy before recruitment. If reading-time exclusions or order blocking are essential, use a platform that records those features. Keep names separate from analytical data when participation tracking is needed. Verify the legacy response and any known pilot records before the team signs off on the final dataset, and report any resulting changes transparently.

The exploratory background and confidence results remain inconclusive. A future study should predefine the group comparison, recruit enough participants within each group, and distinguish background from reading proficiency.

## References

Gao, C. A., Howard, F. M., Markov, N. S., Dyer, E. C., Ramesh, S., Luo, Y., & Pearson, A. T. (2023). Comparing scientific abstracts generated by ChatGPT to real abstracts with detectors and blinded human reviewers. npj Digital Medicine, 6, 75. https://doi.org/10.1038/s41746-023-00819-6

Jakesch, M., Hancock, J. T., & Naaman, M. (2023). Human heuristics for AI-generated language are flawed. Proceedings of the National Academy of Sciences, 120(11), e2208839120. https://doi.org/10.1073/pnas.2208839120

National Institutes of Health. (2013, April). Sleep On It. NIH News in Health. https://newsinhealth.nih.gov/2013/04/sleep-it

SciPy developers. (n.d.). Statistical functions and distribution documentation for ttest_rel, binomtest, chisquare, shapiro, wilcoxon, nct, binom, fisher_exact, mannwhitneyu, spearmanr, and contingency.odds_ratio. https://docs.scipy.org/doc/scipy/reference/stats.html

SciPy developers. (n.d.). Fisher exact test. https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.fisher_exact.html

SciPy developers. (n.d.). Mann-Whitney U test. https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html

SciPy developers. (n.d.). Spearman rank correlation. https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html

## Reproducibility and contribution note

Statistical calculations use Python 3.10, NumPy 2.2.6, and SciPy 1.15.3. The repository includes executable report-evidence and power scripts, aggregate JSON outputs, the expected export headers, and reproduction instructions. Identifiable CSV exports are withheld from GitHub. The report records a November 2 snapshot and does not imply live collection was stopped. AI assistance was used to prepare code and report text; the project members are responsible for reviewing the analysis, references, and final submission.

Owner-folder files are stitched in the course order by make report. Kuba’s files were migrated from the pre-existing draft to preserve content; their presence does not establish that he wrote, reviewed or submitted them. Debshree’s assigned sections and exploratory detection/group/confidence analyses are prepared for review. Shared abstract and conclusion remain joint-review drafts.
