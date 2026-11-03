### H3: Overall detection planning

Power is the binomial probability of a correct-response count falling in the rejection region of the specified chi-square goodness-of-fit test against .50. Participant choices are assumed independent with a common underlying accuracy. These are retrospective calculations under assumed rates, not power calculated from the observed accuracy. The target is .80 power, with complete analyzed responses determining n.

| Assumed true accuracy | First n with 80% power at .05 | Power at n = 26, .05 | Power at n = 26, .0167 | First n with 80% power at .0167 |
|---|---:|---:|---:|---:|
| .60 | 187 | 22.8% | 5.6% | 257 |
| .70 | 43 | 62.7% | 29.7% | 61 |
| .80 | 19 | 94.1% | 74.7% | 24 |

At the corrected threshold, the current sample does not reach .80 power even in the assumed .80-accuracy scenario. Thus, failure to reject H3 does not establish chance-level performance. Rejection regions change discretely, so the first qualifying n is not a guarantee that every larger n attains the target. The assumed-rate results are recorded in results/quality/hypothesis_tests.json, H3_power_assumed_rates. The assumptions do not address possible first-passage response tendencies or uncertainty about participant independence.
