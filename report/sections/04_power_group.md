### H1: Between-group detection planning

These calculations were prepared after collection began. They describe power at assumed underlying accuracies, not observed power or a prospective sample-size justification. The committed implementation uses NumPy and SciPy and enumerates independent binomial outcomes for two groups. For each outcome table it applies the two-sided Fisher rejection rule, then sums alternative probabilities over the rejected tables. The current group sizes are 14 and 12. The table uses the study's α = .05.

| Assumed accuracies | Power at 14 vs 12, .05 |
|---|---:|
| .50 vs .70 | 12.1% |
| .30 vs .60 | 27.3% |
| .50 vs .80 | 27.3% |
| .10 vs .60 | 75.4% |

Even the assumed .10 versus .60 scenario falls short of the .80 power target. Moderate underlying gaps would often be missed with groups this small. A statistically significant result in a small study can also overestimate the magnitude of the underlying difference; the observed gap should not be used alone to plan a replication.

For group sizes n1 and n2 and assumed probabilities p1 and p2, power is the sum of Binomial(a; n1, p1) × Binomial(b; n2, p2) over every possible success-count pair (a, b) for which the two-sided Fisher p-value is at most .05. This calculation assumes independent Bernoulli responses within and between groups and fixed sample sizes. The reproducible implementation is scripts/group_power.py, called by scripts/quality/hypothesis_tests.py. Its search finds the first balanced group size reaching .80 power under the specified alternative; this is a model-based planning calculation, not evidence that the recruited sample was adequate.

The table comes from results/quality/hypothesis_tests.json, H1_power_assumed_rates. A future study should choose a practically relevant group difference before recruitment, calculate the sample size at the intended threshold, allow for exclusions, and balance recruitment where possible. For a gap of 30% versus 60%, about 48 respondents per group would reach .80 power at α = .05. More participants would improve precision but would not repair fixed-order confounding or convenience sampling.
