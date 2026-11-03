### H1: Between-group detection planning

These calculations were prepared after collection began. They describe power at assumed underlying accuracies, not observed power or a prospective sample-size justification. The committed implementation uses NumPy and SciPy and enumerates independent binomial outcomes for two groups. For each outcome table it applies the two-sided Fisher rejection rule, then sums alternative probabilities over the rejected tables. The current group sizes are 14 and 12. Both the nominal .05 level and the study's .05/3 threshold are shown for comparison; the latter determines the current testing decisions.

| Assumed accuracies | Power at 14 vs 12, .05 | Power at 14 vs 12, .0167 |
|---|---:|---:|
| .50 vs .70 | 12.1% | 6.0% |
| .30 vs .60 | 27.3% | 15.3% |
| .50 vs .80 | 27.3% | 15.6% |
| .10 vs .60 | 75.4% | 59.4% |

Even the assumed .10 versus .60 scenario falls short of the .80 power target at the corrected threshold. Moderate underlying gaps would often be missed with groups this small. A statistically significant result in a small study can also overestimate the magnitude of the underlying difference; the observed gap should not be used alone to plan a replication.

The table comes from results/quality/hypothesis_tests.json, H1_power_assumed_rates. A future study should choose a practically relevant group difference before recruitment, calculate the sample size at the intended familywise threshold, allow for exclusions, and balance recruitment where possible. The current table does not establish that a particular larger recruitment target is sufficient. More participants would improve precision but would not repair fixed-order confounding or convenience sampling.
