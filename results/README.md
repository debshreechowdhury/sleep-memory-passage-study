# Outputs

Pipeline outputs go in results/quality/ and results/detection/. The completed report's aggregates are at the top level of results/.

quality/power_scenarios.csv is an assumption-based calculation, not participant data. Generated with Python 3.10, NumPy 2.2.6 and SciPy 1.15.3 using scripts/quality/power.py --n 30. Two-sided alpha .05, target power .80; required complete pairs for dz .3/.5/.8 are 90/34/15. At 30 complete pairs, a dz of about .5292 is detectable with .80 power. Recruitment allowance for exclusions is not included. These calculations were prepared after the form launch and are not evidence of prospective preregistration.

Aggregate participant results are committed in report_statistics.json (54 exported responses, 49 retained). report_power.json contains retrospective planning scenarios at alpha .05 and .025. The report figures summarize these results and the paired-difference distribution. No row-level participant data are committed. Core pipeline validation uses temporary synthetic CSVs and checks mapping, de-identification, mean difference, detection counts, chi-square, exact binomial p-value and changed-header rejection. Synthetic records are deleted with their temporary directory after each test.

Debshree’s exploratory group/confidence aggregates are in debshree_statistics.json; group_power.json gives exact Fisher planning scenarios under assumed rates. presentation_chart_data.json supplies all native slide charts. Figures now live in results/figures, shared by the report and presentation. All aggregate participant outputs identify the same private-source checksum. No identities, free text or row-level responses are included.
