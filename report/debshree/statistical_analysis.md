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
