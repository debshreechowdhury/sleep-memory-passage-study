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
