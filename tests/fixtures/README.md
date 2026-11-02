# Synthetic test data

`synthetic_analysis.csv` is randomly generated. It is **not participant data**, and no number from it may appear in the report or slides. Its IDs all start with `SYNTHETIC-`.

It has the same columns as `data/clean/analysis.csv`, so detection and quality code can be built before the real data is ready. `tests/data/test_fixture.py` fails if the two formats drift apart. After changing the columns in `scripts/data/clean.py`, regenerate it:

```sh
python tests/fixtures/make_synthetic_analysis.py
```
