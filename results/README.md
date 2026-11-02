# Outputs

power_scenarios.csv is an assumption-based calculation, not participant data. Generated with Python 3.10, NumPy 2.2.6 and SciPy 1.15.3 using scripts/power.py --n 30. Two-sided alpha .05, target power .80; required complete pairs for dz .3/.5/.8 are 90/34/15. At 30 complete pairs, a dz of about .5292 is detectable with .80 power. Recruitment allowance for exclusions is not included. These calculations were prepared after the form launch and are not evidence of prospective preregistration.

No participant analysis outputs are committed. Core pipeline validation uses temporary synthetic CSVs and checks mapping, de-identification, mean difference, detection counts, chi-square, exact binomial p-value and changed-header rejection. Synthetic records are deleted with their temporary directory after each test.
