### H1: Student-background comparison

We compare the background answers as reported, rather than substituting the separate current-status field. Each respondent contributes one binary source choice. Under the current coding, a correct answer is Passage 1. The groups do not overlap, but independence between respondents is an assumption of the test, not a fact established by the export. The expected domestic-correct count under independence is 4.62, so the chi-square approximation is questionable; we use the specified two-sided Fisher's exact test for the sparse table. The descriptive effect is the international-minus-domestic difference in proportions. Its 95% interval uses a Welch t calculation on the 0/1 outcomes; it is approximate, is not an exact Fisher interval, and is not adjusted for multiplicity.

| Background | Correct | Incorrect | Accuracy |
|---|---:|---:|---:|
| International | 9 | 5 | 64.3% |
| Domestic | 1 | 11 | 8.3% |

The observed choices were 9/14 versus 1/12. The difference was 56.0 percentage points, 95% confidence interval [23.4, 88.5], Fisher's exact p = .0053. This p-value is below .0167, so H0 is rejected under the current specification. It is evidence of a difference in choices for this sample and coding, not proof that student background causes better AI recognition. The retrospective analysis decisions remain relevant despite the corrected p-value.

![Detection accuracy by student background](../results/quality/group_detection.png)

Figure 1. Proportion of each group selecting the passage coded as AI. Under the fixed AI-first mapping, this is also the proportion selecting Passage 1.

| Sensitivity | International | Domestic | Fisher p |
|---|---:|---:|---:|
| Planned both-wrong check rule | 10/15 | 1/12 | .0047 |
| Omitting the legacy record | 8/13 | 1/12 | .0112 |
| Reversing the legacy record | 8/14 | 1/12 | .0145 |
| Stated status Student only | 7/12 | 1/11 | .0272 |
| Without the last ten responses | 6/10 | 1/6 | .145 |
| Planned check rule, 54-response snapshot | 7/11 | 1/6 | .1312 |

The direction is the same across these subsets and mappings. The first three sensitivity p-values are below .0167, while the stated-Student-only and earlier-response subsets are not. These analyses change the sample or coding; comparing their p-values is not a formal test that the underlying effects differ. The final historical row uses the archived 54-response results, rather than the current workbook.

The last ten analyzed responses arrived within approximately 15 minutes; their counts were 3/4 correct for international-background and 0/6 for domestic-background respondents. The team reports that these were different people, not a single class or group. Timing alone is not evidence that participants discussed answers or that responses were dependent. Removing them is a sensitivity analysis, not evidence that they are invalid observations. Primary and current-workbook sensitivity values come from results/quality/hypothesis_tests.json; the historical snapshot is retained in results/snapshot_group_statistics.json.
