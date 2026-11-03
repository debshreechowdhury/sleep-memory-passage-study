### H1: Between-group detection planning

All power calculations were made after collection began and are illustrative planning sensitivities, not prospective justification or observed power. New calculations use NumPy 2.2.6 and SciPy 1.15.3 under Python 3.13. scripts/group_power.py enumerates independent binomial counts for two groups and sums their joint probabilities whenever the two-sided Fisher's exact p-value is at or below the threshold. The alternative counts are sampled from assumed group-specific rates.

| Assumed accuracies | Power at 14 vs 12, .05 | Power at 14 vs 12, .0167 |
|---|---:|---:|
| .50 vs .70 | 12.1% | 6.0% |
| .30 vs .60 | 27.3% | 15.3% |
| .50 vs .80 | 27.3% | 15.6% |
| .10 vs .60 | 75.4% | 59.4% |

The achieved groups could reliably detect only very large gaps. The plan flagged very low power for this comparison at 15 versus 15. In a study this small, a result that reaches significance may overstate the true difference, so the observed gap should not be used as an effect-size estimate for planning.

| Assumed accuracies | Power: 15 per group | Power: 30 per group | Power: 50 per group | Power: 100 per group |
|---|---:|---:|---:|---:|
| .40 vs .60 | 9.5% | 25.7% | 46.2% | 78.7% |
| .30 vs .60 | 22.7% | 56.1% | 82.9% | 98.9% |
| .30 vs .70 | 43.4% | 83.8% | 97.9% | >99.9% |

At .05, an assumed 30-percentage-point gap reaches .80 power with 50 complete respondents in each group in this table. This is an example for a future study, not a retrospective recruitment target. Balanced future recruitment and an attrition allowance should be specified before recruitment. Power planning cannot correct fixed-order confounding or convenience sampling.
