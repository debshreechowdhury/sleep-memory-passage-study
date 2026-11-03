# Contributing and review

## Ownership

Each member owns specific files. Change the other member's files only after agreeing it with them, and agree changes to shared files together.

| Owner | Files and folders |
|---|---|
| Kuba (data and quality) | `config/`, `data/`, `scripts/data/`, `scripts/quality/`, `results/quality/`, `report/sections/*_quality.md`, `report/sections/05_data_collection_cleaning.md`, `report/sections/08_limitations_ratings_data.md`, `presentation/data_quality.pptx`, `tests/data/`, `tests/quality/`, `tests/fixtures/` |
| Debshree (design and detection) | `study/`, `scripts/detection/`, `results/detection/`, `report/sections/*_group.md`, `report/sections/01_background.md`, `report/sections/03_design.md`, `report/sections/08_limitations_stimulus_sampling.md`, `presentation/design_detection.pptx`, `tests/detection/` |
| Shared | `README.md`, `CONTRIBUTING.md`, `Makefile`, `requirements.txt`, `requirements-report.txt`, `docs/`, `report/sections/00_title_abstract.md`, `report/sections/02_testing_policy.md`, `report/sections/09_conclusion.md`, `report/sections/10_references.md`, `report/sections/11_contribution_note.md`, `report/sections.json`, `report/report.md`, `report/README.md`, `report/REPRODUCE.md`, `report/REVIEW_NOTES.md`, top-level files in `scripts/` and `results/`, `presentation/template.pptx`, `presentation/final.pptx`, `tests/test_pipeline.py` |

## Rules

- Never invent results, citations, counts or study facts, and take every report and slide number from `results/`.
- Label synthetic data clearly, and never use its numbers in the report or slides.
- Use methods from the course material. The earlier 54-response scripts keep some others as a record only.
- Use "fail to reject", never "accept the null". Do not describe this study as preregistered, randomized or counterbalanced.

## Pull requests

1. Make a branch for one focused change, for example `docs/consent-review`, `data/import`, or `analysis/paired-tests`.
2. Open a pull request to `main` and fill out the PR template. Every group member should author at least one substantive PR.
3. Request a review from another group member. The reviewer should check the change against the instrument, analysis plan, privacy constraints, and reproduction instructions as relevant.
4. Resolve comments in the PR and rerun the documented checks. The author should not approve their own PR or merge it without another member's review.
5. Keep original exports out of PRs; only the two de-identified files in `data/` belong in the repository. Never place credentials, names or responder email addresses in the repository.

Record each member's PR link in `docs/project_plan.md` once it exists. Do not create placeholder PR links or imply that reviews occurred before they did.
