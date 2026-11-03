### H1: Student-background comparison

We compare the background answers as reported, rather than substituting the separate current-status field. Each respondent contributes one binary source choice. Under the current coding, a correct answer is Passage 2. The groups do not overlap, but independence between respondents is an assumption of the test, not a fact established by the export. The smallest expected count under independence is 4.62, for incorrect domestic respondents, so the chi-square approximation is questionable; we use the specified two-sided Fisher's exact test for the sparse table. The descriptive effect size is the domestic-minus-international difference in proportions. Its 95% interval uses a Welch t calculation on the 0/1 outcomes; it is approximate, is not an exact Fisher interval, and is not adjusted for multiplicity.

| Background | Correct | Incorrect | Accuracy |
|---|---:|---:|---:|
| International | 5 | 9 | 35.7% |
| Domestic | 11 | 1 | 91.7% |

The observed choices were 5/14 versus 11/12. The difference was 56.0 percentage points in favor of domestic respondents, 95% confidence interval [23.4, 88.5], Fisher's exact p = .0053. This p-value is below .0167, so H0 is rejected under the current specification. It is evidence of a difference in choices for this sample and coding, not proof that student background causes better AI recognition. The retrospective analysis decisions remain relevant despite the corrected p-value.

![Detection accuracy by student background](../results/quality/group_detection.png)

Figure 1. Proportion of each group selecting the passage coded as AI. Under the original-first mapping, this is also the proportion selecting Passage 2.

| Sensitivity | International | Domestic | Fisher p |
|---|---:|---:|---:|
| Planned both-wrong check rule | 5/15 | 11/12 | .0047 |
| Omitting the legacy record | 5/13 | 11/12 | .0112 |
| Reversing the legacy record | 6/14 | 11/12 | .0145 |
| Stated status Student only | 5/12 | 10/11 | .0272 |
| Without the last ten responses | 4/10 | 5/6 | .145 |
| Planned check rule, first 54 responses | 4/11 | 5/6 | .1312 |

The direction is the same across these subsets and mappings. The first three sensitivity p-values are below .0167, while the stated-Student-only and earlier-response subsets are not. These analyses change the sample or coding; comparing their p-values is not a formal test that the underlying effects differ.

The last ten analyzed responses arrived within approximately 15 minutes; their counts were 1/4 correct for international-background and 6/6 for domestic-background respondents. The team reports that these were different people, not a single class or group. Timing alone is not evidence that participants discussed answers or that responses were dependent. Removing them is a sensitivity analysis, not evidence that they are invalid observations. All values come from results/quality/hypothesis_tests.json.
