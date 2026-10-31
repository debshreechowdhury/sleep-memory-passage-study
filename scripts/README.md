# Scripts

No data collection, cleaning, or analysis script has been used yet. Data collection is through the two Google Forms documented in `forms/`.

After collecting responses, add **scripts, not notebooks** for:

1. Importing both unchanged Google Forms CSV exports and attaching the passage-order variable.
2. Cleaning responses and applying the preregistered exclusion rules.
3. Building version-specific rating variables and the detection-correctness variable.
4. Computing quality scores, reliability, primary tests, and exploratory analyses.
5. Producing tables or figures from the cleaned dataset.

Scripts should accept input and output paths as arguments, declare dependency versions, avoid absolute personal paths, and run from a fresh checkout. Add a small validation dataset or test only when it checks a real risk in the mapping or scoring logic. Document exact commands in the top-level README.
