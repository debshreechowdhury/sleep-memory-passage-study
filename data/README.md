# Participant data and dictionary

No participant exports have been downloaded into this repository. A response was visible during form editing on October 31; the present sample size is unverified. Do not describe collection as not started.

Names are now optional and linked to responses. Raw exports and free text may identify people and must remain in approved access-controlled storage. Local data/raw, data/interim and data/cleaned CSVs are ignored by Git. Do not commit the manifest with raw headers if they contain private details. Only release de-identified data after the team confirms permission; a private repository still exposes data to collaborators.

For withheld data, record approved storage location, access contact/procedure, export date, form revision, SHA-256 checksum, row count and reason for withholding. These entries are pending actual exports. Retain original exports unchanged; retain any identifier-to-response crosswalk separately if needed for withdrawals. Do not publish names.

## Canonical fields
The importer retains only configured fields; response_id is a generated row identifier, not a person identifier. It does not resolve duplicate submissions.

- order: verified AI first or Original first for each source file.
- consent: actual affirmative consent text; status: Student, Working professional, Other (older exports may use an earlier eligibility question).
- clear_1/2, engage_1/2, write_1/2: passage-position ratings, integers 1–7.
- check_1/2: 30, 60, 90, 120 minutes; 90 is correct.
- detect: Passage 1 or Passage 2; confidence: 1–5.
- ai_use: 1–5 and english: 1–7 only if actually collected; leave absent fields empty.
- cleaned *_AI/*_O: version-mapped items; quality_AI/O: complete three-item means.
- detect_correct: 0/1; included: 0/1; exclusion_reason: auditable rule flags.

Ages, names, timestamps, free text and emails are not exported by the importer. Verify adult eligibility from collection records; the current form's 18+ statement is an instruction rather than a recorded age check. Do not infer age from status.
