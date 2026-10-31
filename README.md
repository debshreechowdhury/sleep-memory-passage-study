# Sleep and memory passage study

This repository documents a paired comparison of an original NIH News in Health passage and an AI rewrite. Participants rate both passages, answer a comprehension check after each, and then identify the AI rewrite. The Google Forms are drafted but **not published**.

## Current status

| Component | Status |
| --- | --- |
| Google Forms | Two seven-section drafts, one for each passage order |
| Pilot and participant responses | Not started |
| Raw and cleaned data | Not available yet; see [data/README.md](data/README.md) |
| Cleaning and analysis scripts | To be written after the export format is known; see [scripts/README.md](scripts/README.md) |
| Preregistration | Draft only; finalize before collecting responses |

## Reproduce the data collection setup

1. Read the full [instrument](forms/instrument.md) and [form setup](forms/google-forms.md).
2. Open the [original-first draft](https://docs.google.com/forms/d/1Q65UDgX-x9PvnkmanHsWrMa9MXg_I2Uhwi6J7-UVCAQ/edit) and [AI-first draft](https://docs.google.com/forms/d/1g33aG8Z6tIRb-glQeaP0DlqJ3O-1-y5ycDqjkkdvM0w/edit). Edit access depends on the form owner's Google permissions. The instrument file allows recreation if access is unavailable.
3. Check the passage order, required questions, debrief, and response settings in each form. Use Preview on desktop and phone.
4. Resolve any instructor or ethics review of the brief nondisclosure, finalize the [analysis plan](ANALYSIS_PLAN.md), and follow the [pilot protocol](PILOT_PROTOCOL.md) with 3–4 people before publishing.
5. Assign participants to the two responder links using a documented alternating or randomly generated assignment list. Record which version each respondent received. Google Forms does not balance the two links automatically.

The forms do not collect email addresses or require Google sign-in. The free-text explanation could still contain identifying details, so treat responses as potentially sensitive.

## Reproduce cleaning and analysis after collection

1. Export responses from both forms as CSV. Keep an unchanged copy of each export in approved storage and record export date and form order.
2. Add the scripts used to combine, clean, exclude, score, and analyze responses under `scripts/` through reviewed pull requests. Commit exact dependency versions and command-line instructions in this README.
3. Place publishable, de-identified raw and cleaned files under `data/` only after checking institutional rules and the consent language. If sharing is not permitted, update [data/README.md](data/README.md) with the storage location, access procedure, schema, and reasons for withholding files.
4. Record the final sample counts, exclusions, outputs, software versions, and exact reproduction commands here.

There is currently no response export and no cleaning or analysis code to run. This README will be updated when those materials exist; empty or simulated results are not presented as collected data.

## Collaboration

Use a separate branch and pull request for each change. Each group member should author at least one substantive PR and request review from another member. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [PR template](.github/pull_request_template.md). Do not merge your own PR without another member's review.

## Source

Original passage: [NIH News in Health, “Sleep On It”](https://newsinhealth.nih.gov/2013/04/sleep-it). The supplied excerpt is reproduced exactly in the instrument, including its unusual final quotation mark.
