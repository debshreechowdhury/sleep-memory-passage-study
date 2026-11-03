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
