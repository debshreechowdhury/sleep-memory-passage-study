PYTHON ?= python3
MANIFEST ?= config/export_manifest.local.json
RAW = data/raw/responses_deidentified.csv
CLEAN = data/clean/analysis.csv

.PHONY: all test data power quality detection report check

all: data power quality detection report

test:
	$(PYTHON) -m unittest discover -s tests -t . -v

data:
	$(PYTHON) scripts/data/import_forms.py --manifest $(MANIFEST) --output $(RAW)
	$(PYTHON) scripts/data/clean.py --input $(RAW) --output $(CLEAN)

power:
	$(PYTHON) scripts/quality/power.py --n 30 --output results/quality/power_scenarios.csv

quality:
	$(PYTHON) scripts/quality/quality.py --input $(CLEAN) --output results/quality/quality.json

detection:
	$(PYTHON) scripts/detection/detection.py --input $(CLEAN) --output results/detection/detection.json

report:
	$(PYTHON) scripts/assemble_report.py

check: report
	$(PYTHON) scripts/check_report.py
	$(PYTHON) scripts/check_debshree.py
