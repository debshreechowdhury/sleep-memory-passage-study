# Analysis plan — draft, not preregistered

Finalize this plan before collecting responses. The Google Forms implementation cannot measure passage-page time, so the originally proposed exclusion for spending under 30 seconds on either passage page cannot be applied.

## Planned fields

Assign `order` from the form used (`Original first` or `AI first`). Each form exports passage-position ratings. Map the Passage 1 and Passage 2 columns to version-specific fields using the order:

| Analysis field | Original-first form | AI-first form |
| --- | --- | --- |
| `clear_O`, `engage_O`, `write_O` | Passage 1 ratings | Passage 2 ratings |
| `clear_AI`, `engage_AI`, `write_AI` | Passage 2 ratings | Passage 1 ratings |
| `check_1`, `check_2` | First and second check | First and second check |
| `detect_correct = 1` | Detection answer is Passage 2 | Detection answer is Passage 1 |

Also retain student status, confidence, optional explanation, AI-tool use, and English proficiency. Inspect actual export headers before implementing column mappings. Preserve raw values and document every transformation.

## Proposed rules and tests

- Include respondents who affirm age 18+, current graduate-student status, and consent. Exclude completed responses only if **both** comprehension checks are incorrect. Confirm this rule before collection and report exclusions by reason.
- For each version, compute quality as the mean of clarity, engagement, and overall writing ratings. Report Cronbach's alpha separately for the three original and three AI ratings.
- Primary rating comparison: two-sided paired t-test of AI versus original quality, alpha = .05. Report the paired mean difference, 95% confidence interval, effect size, and analyzed sample size.
- Primary detection comparison: two-category chi-square goodness-of-fit test of correct versus incorrect detection against 50/50, alpha = .05. Report counts.
- Exploratory: Fisher's exact test for student status by detection correctness; logistic regression of detection correctness on AI-tool use and English proficiency. Treat small-sample estimates cautiously.

The team should decide how to handle missing responses, duplicate submissions, and any post-collection withdrawal request before collecting data. Do not choose exclusions after inspecting outcome differences.
