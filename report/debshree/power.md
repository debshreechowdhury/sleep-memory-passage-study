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
