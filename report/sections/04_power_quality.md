### H2: Paired quality planning

Power calculations were prepared after collection began. They are planning sensitivities under assumed effects, not prospective justification, observed power, or evidence of preregistration. The initial n = 30 scenario refers to complete pairs. We used Python 3.10 and SciPy 1.15.3. The paired-t calculation uses the noncentral t distribution: the noncentrality is the assumed standardized paired difference multiplied by the square root of the number of complete pairs, with n minus one degrees of freedom. Cohen dz uses the standard deviation of within-person differences, not the pooled standard deviation of the two passages.

| Assumed absolute dz | Pairs for 80% power at .05 | Power with 30 pairs at .05 |
|---|---:|---:|
| 0.30 | 90 | 35.5% |
| 0.50 | 34 | 75.4% |
| 0.80 | 15 | 98.8% |

No attrition allowance was specified prospectively. For illustration, 34 usable pairs with a 10% allowance would require 38 recruits, calculated by dividing 34 by .90 and rounding up. This is a planning example, not a claim about the actual recruitment target. The report does not compute power from the observed effect.

### H2: Sensitivity at the achieved sample

The analyzed sample has 26 complete pairs, below both the initial n = 30 scenario and the 34 pairs needed for 80% power at an assumed dz of 0.50. With 26 pairs and 80% power, the smallest detectable standardized paired difference is about dz = 0.57 at .05. Power at .05 is 31.3% for an assumed dz of 0.30, 68.8% for 0.50, and 97.5% for 0.80. These values use assumed effects at the achieved sample size, not the observed effect, so they describe what the design could detect and not the strength of the observed result. They were calculated with the same SciPy version under Python 3.13. The study is therefore poorly placed to detect small differences, and a nonsignificant follow-up in this sample does not show that a difference is absent.
