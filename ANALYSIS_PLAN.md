# Analysis plan — draft; not preregistered

Updated November 2, 2026 to reflect chat-documented form changes. Collection had already begun at least to the extent of one observed response; these decisions must not be represented as prospectively preregistered. Team review and actual exports remain necessary.

## Design and hypotheses

Within-person comparison of AI and original quality (mean of clarity, engagement and writing items, each 1–7). H0: mean AI-minus-original difference = 0; H1: difference ≠ 0. Detection H0: correctness probability = .5; H1: probability ≠ .5. Nominal alpha .05; two co-primary tests currently have unadjusted p-values. Decide and document a multiplicity policy before interpreting them; report deviations transparently.

Last circulated link is fixed AI first, so Passage 1 maps to *_AI, Passage 2 to *_O, and Passage 1 is the correct detection answer. Importer supports Original first only for a source with verified assignment evidence. Fixed order confounds version with position; no claim of randomized or balanced presentation is justified.

## Cleaning baseline for member review

- Affirmative consent required; participation instructions restrict to 18+. Actual age check was absent in the last observed form, so do not claim verified age eligibility. Student / Working professional / Other are all allowed.
- Exclude both comprehension checks incorrect. Hold missing comprehension out pending review. Do not implement the proposed under-30-second rule: page times are not collected.
- Compute each quality score only with all three ratings; paired analysis requires both scores. Detection uses available responses among included records; use a separate denominator.
- Preserve unchanged exports privately and retain exclusion reasons. Resolve duplicate submissions through a documented rule; generated row IDs do not identify duplicate people. Do not remove identical rating patterns automatically.
- Optional names are identifiable and excluded from analysis exports. Retain any private withdrawal crosswalk separately and record withdrawals without disclosing names in Git.
- Record form revisions and pilot inclusion rules; do not pool incompatible records silently. Missing AI-use or English items are not recoverable by imputation from other questions.

## Analyses

Paired t-test on AI-minus-original composite differences; report mean difference, SD, 95% CI, t, df, p and Cohen dz. Inspect difference distribution and outliers; recruitment/duplicate review informs independence. Compute Cronbach alpha separately by version on complete paired data and state its denominator. Diagnostics and a justified sensitivity analysis remain work to complete.

Detection: chi-square goodness-of-fit against 50/50 only if expected cell counts are at least 5. Also report exact two-sided binomial p and exact 95% CI, accuracy and accuracy-minus-chance. No post hoc pairwise test is needed for two versions.

Exploratory status analysis has three categories; do not apply a 2×2 Fisher test directly. A declared student versus non-student collapse or an appropriate multi-category method needs justification. Logistic regression on AI use/English is possible only if both were actually collected and sample/outcome variation supports estimation. Document any omission or instability.

Power: scripts/power.py uses the noncentral t distribution for a two-sided one-sample test of within-person differences, dz = mean difference / SD differences. Default n=30, target .8, alpha .05 and dz .3/.5/.8 are scenarios, not established sample facts. Include exact detection-power planning separately if retaining detection as co-primary. Do not report observed power as evidence for a null result.

## November 2 completed-analysis amendment

The snapshot contained 54 consenting responses; five failed both checks, leaving 49 complete pairs. See [the report](report/report.md) and [reproduction instructions](report/REPRODUCE.md). These are retrospective analyses, not preregistration. Nominal co-primary p-values are accompanied by a retrospective Bonferroni threshold of .025. Distribution diagnostics, a tie-preserving Wilcoxon sensitivity, exact detection-power scenarios, and omission/reversal sensitivities for the first legacy response are complete. No duplicate-pattern exclusion was applied; pilot membership and legacy assignment remain unverified. AI-use/English regression and the time exclusion are unavailable because the required fields were not collected. The report supersedes unfinished-task wording above while preserving the original planning record.

## November 2 ownership and exploratory-analysis amendment

The supplied work split assigns H2/H3, group comparisons and confidence to Debshree. The old plan did not define numbered H3. Pending team confirmation, the new draft uses international versus domestic student-background detection and explicitly treats it as retrospective/exploratory. Broad self-report and strict Student-only definitions are both reported; Student versus Working professional is a separate exploratory comparison. Fisher exact tests handle sparse 2-by-2 tables; confidence uses tie-corrected Mann-Whitney and a fixed-seed permutation of Spearman rho. No confirmatory family is enlarged retrospectively. Assumed-rate Fisher power scenarios are in results/group_power.json. The complete owner split is in report/README.md.
