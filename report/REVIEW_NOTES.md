# Member review and submission status

## Current structure

H1 is the international versus domestic detection comparison at α = .05, and H2 is exploratory quality, on the 26 students who answered both checks correctly. Overall detection against chance was dropped as a hypothesis, and its result is disclosed under the testing policy. Debshree agreed to the main question but has not reviewed the passage-order correction or this change.

## Passage order correction

Kuba confirmed that Passage 1 was the original and Passage 2 the AI rewrite from the start, and that the reverse labeling came from a team member mixing up the passages. Every direction in the report was reversed to match, with p-values unchanged. **Debshree has not reviewed this correction**, and some review text below predates it. A form read through the link in `study/google_forms.md` shows the rewrite's wording as Passage 1; the report discloses this as unreconciled.

## Confirmed by the team

No pilot responses were collected. The last ten responses came from different people and not a single class or group. The rewrite used ChatGPT-6.1 Sol over two prompts, with the second output used. The instructor accepted the initial nondisclosure. The form is closed.

## Still unverified

The legacy response's passage version and the rewrite's generation date. The report discloses both.

## Before submission

- Each member reviews and signs off the other's PR; the review below was Codex-assisted and is not a member's own sign-off. Record the PR links and outcomes in `docs/project_plan.md`.
- Finalize the abstract and conclusion together.
- Review the combined draft `presentation/final.pptx` together and rehearse.
- Rebuild the Word report with `python scripts/build_report_docx.py` and check its layout.
- Send NIH News in Health a copy of the final report, as its reuse policy asks.
- Submit the report through the course Byline link and the repository URL through the required route; no submission has been made yet.

## Debshree review revision after PR #6

A Codex-assisted review checked the assigned design/group/detection sections against results/quality/hypothesis_tests.json and the October 30 plan. That review predates the removal of H3 and the .05/3 policy. Wording now separates rejection under the current analysis from prospective confirmation, describes the approximate marginal intervals, and avoids treating changes in subset p-values as a formal test of changing effects. The supplied team confirmations above remain incorporated as reported facts, not invented independent verification.

The requested short review was posted on [Kuba's PR #6](https://github.com/debshreechowdhury/sleep-memory-passage-study/pull/6#issuecomment-6592999381). This comment is not a claim that a human member's final sign-off or an ethics-board review has occurred.

The stimulus archive is complete and its passage bodies were checked against the live editor on November 2. It records the supplied two-prompt sequence, reported GPT-6.1 SOL label and second-output selection; the generation date and legacy response order remain unknown. NIH's publication-specific reuse policy was checked and linked in provenance.md. The archive preserves the observed unmatched final quote, while study/instrument.md corrects only the reference text. The current form's introduction still asks for graduate students despite the broader status options; this mismatch is disclosed in the design and sampling limitations. The live form and participant records were not edited.

The abstract and conclusion are drafts for joint review. final.pptx is a combined draft for joint review. Kuba's owned sections, scripts/quality/, results/quality/, data/ and member deck are unchanged by this review branch. A publication copy has not been sent to NIH by this task.
