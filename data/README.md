# Participant data and dictionary

The analysis uses a privately held workbook of 64 submissions downloaded November 2, 2026. Keeping only international or domestic students with both comprehension checks correct leaves 26 paired responses; 35 non-students and three check failures were removed. An earlier CSV of 54 of those submissions, with 49 retained under the planned check rule, is kept as a sensitivity analysis. Raw and row-level cleaned data are withheld from this repository because names and free text may identify participants. The owner holds the local CSV; request access from the repository owner. The checksum, aggregate results and reproduction procedure are in results/report_statistics.json and report/REPRODUCE.md. This snapshot does not establish that collection has closed.

Names are now optional and linked to responses. Raw exports and free text may identify people and must remain in approved access-controlled storage. Keep original exports in data/private/, which Git ignores. In data/raw and data/clean, Git only accepts `responses_deidentified.csv` and `analysis.csv`. Do not commit the manifest with raw headers if they contain private details. Only commit those de-identified files after the team confirms permission; a private repository still exposes data to collaborators.

For withheld data, record approved storage location, access contact/procedure, export date, form revision, SHA-256 checksum, row count and reason for withholding. These entries are pending actual exports. Retain original exports unchanged; retain any identifier-to-response crosswalk separately if needed for withdrawals. Do not publish names.

## Folders
- data/private/: unchanged original exports, the CSV converted from them and any withdrawal crosswalk (ignored).
- data/raw/responses_deidentified.csv: importer output, with identifiers removed.
- data/clean/analysis.csv: cleaner output and the handoff file for quality and detection analysis. tests/fixtures/synthetic_analysis.csv has the same columns.

## Canonical fields
The importer retains only configured fields; response_id is a generated row identifier, not a person identifier. It does not resolve duplicate submissions.

- order: verified AI first or Original first for each source file.
- consent: actual affirmative consent text; status: Student, Working professional, Other (older exports may use an earlier eligibility question); student_background: International, Domestic or Not applicable.
- clear_1/2, engage_1/2, write_1/2: passage-position ratings, integers 1–7.
- check_1/2: 30, 60, 90, 120 minutes; 90 is correct.
- detect: Passage 1 or Passage 2; confidence: 1–5.
- ai_use: 1–5 and english: 1–7 only if actually collected; leave absent fields empty.
- cleaned *_AI/*_O: version-mapped items; quality_AI/O: complete three-item means.
- detect_correct: 0/1; included: 0/1 under the study rule (student with both checks correct); included_both_wrong_rule: 0/1 under the earlier rule; exclusion_reason: auditable rule flags.

Ages, names, timestamps, free text and emails are not exported by the importer. Verify adult eligibility from collection records; the current form's 18+ statement is an instruction rather than a recorded age check. Do not infer age from status.
