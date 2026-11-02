PYTHON ?= python3
.PHONY: report check test
report:
	$(PYTHON) scripts/assemble_report.py
check: report
	$(PYTHON) scripts/check_report.py
	$(PYTHON) scripts/check_debshree.py
test:
	$(PYTHON) -m unittest discover -s tests -v
