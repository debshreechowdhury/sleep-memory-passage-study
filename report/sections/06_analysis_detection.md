### H3: Overall detection

For the same 26 student-background respondents, we compare correct and incorrect counts with the 50/50 null using chi-square goodness-of-fit. Both expected counts are 13. The test assumes independent choices and adequate expected counts. This is a single detection response per person, not a paired comparison of two detection scores. We report an approximate t-based 95% interval on the binary scores; it is marginal, not adjusted to match the three-test threshold. No post hoc pairwise test is required.

Ten of 26 respondents selected Passage 1, which the analysis codes as correct, while 16 selected Passage 2. Accuracy was 38.5%, 95% confidence interval [18.4%, 58.5%], or 11.5 percentage points below chance. The test gave chi-square(1) = 1.385, p = .239. At .0167, we do not reject H0. The interval and the limited sample do not support an equivalence claim.

![Overall detection accuracy against chance](../results/quality/overall_detection.png)

Figure 3. Overall accuracy with an approximate t-based 95% interval. The dashed reference is chance; the interval includes it.

| Sensitivity | n | Correct | Chi-square p |
|---|---:|---:|---:|
| Omitting the legacy record | 25 | 9 | .162 |
| Reversing the legacy record | 26 | 9 | .117 |
| Planned check rule, students | 27 | 11 | .336 |
| Planned check rule, all respondents | 59 | 21 | .0269 |
| Planned check rule, 54-response snapshot | 49 | 18 | .0633 |

None of these p-values is below .0167. The all-respondent sensitivity includes non-students, so it answers a different population question and should not replace the student result. Mapping uncertainty for the legacy response is disclosed rather than resolved by choosing the most favorable p-value.

### Confidence (exploratory)

The confidence scale runs from 1 (Just guessing) to 5 (Extremely confident). Its labels are ordinal, not numerical probabilities. Mean confidence was 3.31 and the median was 3. Correct respondents (n = 10) averaged 3.00, compared with 3.50 among incorrect respondents (n = 16). The two-sided Mann-Whitney comparison gave U = 55.5, p = .141. With these sample sizes and tied responses, the implementation uses the tie-corrected asymptotic distribution and a continuity correction. The test concerns confidence distributions, not equality of the displayed means.

This analysis supplies no clear evidence that confidence separates correct from incorrect choices. It does not establish that confidence is unrelated to accuracy in the population, and it cannot assess probability calibration. Optional explanations were not systematically coded. Current results are from results/quality/hypothesis_tests.json; the earlier snapshot remains a historical sensitivity record, not the current headline analysis.
