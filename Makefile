PYTHON ?= python3
MANIFEST ?= config/export_manifest.local.json
EXPORT ?= data/private/responses.xlsx
EXPORT_CSV = data/private/responses.csv
RAW = data/raw/responses_deidentified.csv
CLEAN = data/clean/analysis.csv

.PHONY: all test data power quality regression quality_figures slides detection report check

all: data power quality regression quality_figures slides detection report

test:
	$(PYTHON) -m unittest discover -s tests -t . -v

data:
	$(PYTHON) scripts/data/xlsx_to_csv.py --input $(EXPORT) --output $(EXPORT_CSV)
	$(PYTHON) scripts/data/import_forms.py --manifest $(MANIFEST) --output $(RAW)
	$(PYTHON) scripts/data/clean.py --input $(RAW) --output $(CLEAN)

power:
	$(PYTHON) scripts/quality/power.py --n 30 --output results/quality/power_scenarios.csv
	$(PYTHON) scripts/quality/power.py --n 26 --alpha .05 .025 --output results/quality/power_achieved.csv

quality:
	$(PYTHON) scripts/quality/quality.py --input $(CLEAN) --output results/quality/quality.json --source $(EXPORT)

regression:
	$(PYTHON) scripts/quality/regression.py --input $(CLEAN) --output results/quality/regression.json

quality_figures:
	$(PYTHON) scripts/quality/figures.py --input $(CLEAN) --statistics results/quality/quality.json --output-dir results/quality

detection:
	$(PYTHON) scripts/detection/detection.py --input $(CLEAN) --output results/detection/detection.json

slides:
	$(PYTHON) scripts/quality/build_slides.py --template presentation/template.pptx --output presentation/data_quality.pptx

report:
	$(PYTHON) scripts/assemble_report.py

check: report
	$(PYTHON) scripts/check_report.py
	$(PYTHON) scripts/check_debshree.py
	$(PYTHON) scripts/quality/check_quality.py
