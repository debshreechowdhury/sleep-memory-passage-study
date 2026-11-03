### H2: Quality analysis

For each participant and version, quality was the arithmetic mean of all three ratings. We calculated the original-minus-AI paired difference, its standard deviation, a two-sided paired t-test, a t-based 95% confidence interval, and Cohen dz. A paired t-test fits because each participant rated both versions, so the differences within people are the unit of analysis. We summarized how closely the three ratings agreed using descriptive pairwise correlations within each version. A two-level paired comparison needs no post hoc test between versions; item-level follow-ups are reported below.

We examined the distribution of paired differences with a histogram, a quantile plot, and Shapiro-Wilk. Independence depends on recruitment and duplicate review and cannot be established by this test. Shapiro-Wilk did not reject normality, W = .938, p = .119, although with 26 pairs it has limited power, and the bounded scales and eight tied differences warranted a Wilcoxon signed-rank sensitivity analysis. Mathematical ties were preserved by rounding differences to ten decimal places; its p-value uses a normal approximation with zeros omitted. This test has different assumptions and does not directly test the identical population-mean hypothesis.

![Paired difference histogram and normal quantile plot](../results/quality/difference_diagnostics.png)

Figure 2a. Diagnostic views of the 26 original-minus-AI composite differences. Eight respondents rated the two versions equally.

### Quality results

| Outcome | AI mean | Original mean | Original minus AI |
|---|---:|---:|---:|
| Clarity | 5.923 | 6.423 | 0.500 |
| Engagement | 5.154 | 5.692 | 0.538 |
| Overall writing | 5.346 | 5.769 | 0.423 |
| Composite quality | 5.474 | 5.962 | 0.487 |

Composite standard deviations were 0.828 for AI and 0.568 for the original. The standard deviation of paired differences was 0.773. The paired test gave t(25) = 3.213, p = .0036, with 95% confidence interval [0.175, 0.799] for the original advantage and dz = 0.630. The p-value is below the Bonferroni threshold of .05/3 = .0167 for the three planned tests, so we reject H0. Original quality was higher for 15 participants, AI quality was higher for three, and eight tied. The Wilcoxon sensitivity agreed, W = 22.5, p = .00579.

| Correlation between | AI rewrite | Original |
|---|---:|---:|
| Clarity and engagement | .45 | .37 |
| Clarity and overall writing | .30 | .10 |
| Engagement and overall writing | .60 | .53 |

Engagement and overall writing moved together, while clarity was only weakly related to overall writing, especially for the original. The three ratings therefore do not behave as interchangeable measures, and the composite should be read alongside the items.

### Item-level post hoc tests

To see which ratings contributed to the composite difference, we compared each item with a paired t-test as a post hoc follow-up. Bonferroni correction for three tests sets the per-test threshold at .05/3 = .0167, which is equivalent to multiplying each p-value by three. Shapiro-Wilk rejected normality for all three item differences, which take few distinct values, so we also report Wilcoxon p-values.

| Item | Original minus AI | 95% CI | t(25) | p | Bonferroni p | dz | Wilcoxon p |
|---|---:|---:|---:|---:|---:|---:|---:|
| Clarity | 0.500 | [0.264, 0.736] | 4.372 | .00019 | .00057 | 0.857 | .00079 |
| Engagement | 0.538 | [0.078, 0.999] | 2.409 | .0237 | .0710 | 0.473 | .0253 |
| Overall writing | 0.423 | [-0.090, 0.936] | 1.698 | .102 | .306 | 0.333 | .133 |

![Item-level differences with confidence intervals](../results/quality/item_differences.png)

Figure 2b. Original-minus-AI differences for the composite and each item, with unadjusted 95% confidence intervals.

Only clarity stayed below the corrected threshold. These tests follow up H2 and are not additional planned hypotheses. Because the same respondents rated all three correlated items, Bonferroni is conservative here.

### Quality by student background (exploratory)

We compared the paired quality difference between groups to check that the combined result was not hiding opposing patterns, as in Simpson's paradox. The original advantage was 0.405 for international students (n = 14; 95% CI [-0.125, 0.934]; p = .123) and 0.583 for domestic students (n = 12; 95% CI [0.210, 0.957]; p = .00557), so both groups point in the same direction. The groups did not differ reliably: Welch t(22.4) = 0.599, p = .555, with a 95% confidence interval for the international-minus-domestic difference of [-0.796, 0.439]. Levene's test did not indicate unequal variances, p = .477, and Mann-Whitney gave U = 103, p = .333. Subgroups this small cannot show that the groups respond alike.

### Exploratory regression

AI-use and English reading proficiency were absent from the export, so the originally proposed regression cannot be fitted. They must not be inferred from student background or replaced with invented covariates. We instead fit an exploratory multiple linear regression of the original-minus-AI difference on predictors that were collected: international background (1 = international, 0 = domestic), correct detection (1 = correct), and detection confidence (1 to 5).

| Term | Estimate | SE | t(22) | p | 95% CI |
|---|---:|---:|---:|---:|---:|
| Intercept | 1.929 | 0.795 | 2.427 | .0239 | [0.281, 3.576] |
| International | -0.238 | 0.366 | -0.650 | .522 | [-0.998, 0.522] |
| Correct detection | -0.036 | 0.395 | -0.090 | .929 | [-0.855, 0.783] |
| Confidence | -0.393 | 0.220 | -1.784 | .0883 | [-0.850, 0.064] |

The model did not explain significant variation, F(3, 22) = 1.262, p = .312, R-squared = .147, adjusted R-squared = .031. Residual plots showed no clear pattern, Shapiro-Wilk on the residuals did not reject normality, W = .959, p = .376, and Breusch-Pagan did not indicate unequal residual variance, LM = 4.874, p = .181. With 26 respondents and three predictors the estimates are imprecise, so these nonsignificant coefficients do not show that the predictors are unrelated to the difference.

![Regression residuals versus fitted values and normal quantile plot](../results/quality/regression_residuals.png)

Figure 2c. Residual diagnostics for the exploratory regression.

### Sensitivity analyses

| Analysis | n | Original minus AI | 95% CI | t | p | dz |
|---|---:|---:|---:|---:|---:|---:|
| Primary: students, both checks correct | 26 | 0.487 | [0.175, 0.799] | 3.213 | .0036 | 0.630 |
| Omitting the legacy record | 25 | 0.507 | [0.184, 0.830] | 3.238 | .00351 | 0.648 |
| Planned check rule, all 64 submissions | 59 | 0.390 | [0.178, 0.602] | 3.676 | .00052 | 0.479 |
| Planned check rule, 54-response snapshot | 49 | 0.415 | [0.167, 0.663] | 3.369 | .00149 | 0.481 |

Reversing the legacy record's version labels did not change the composite comparison because its two composite scores were equal. The direction and significance of the composite difference are therefore stable across the exclusion rules and version sensitivities, while the estimate ranges from 0.390 to 0.507.

The item-level pattern was not stable. In the 49-response snapshot analysis, engagement and overall writing met the corrected threshold and clarity did not, the reverse of the primary result, so no individual item should be singled out. That analysis also gave W = 94.0, p = .00242 for the composite Wilcoxon sensitivity. We reproduced its 49 retained responses, composite difference and detection counts independently from the first 54 rows of the workbook.
