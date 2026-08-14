CHROME ?= /opt/pw-browsers/chromium-1194/chrome-linux/chrome
PDF    := ../report/Mumbai_Real_Estate_Master_Playbook_2026.pdf

.PHONY: all data figures workbook report pdf clean

all: data figures workbook pdf

data:
	python3 export_data.py

figures:
	python3 fig_market.py
	python3 fig_strategy.py
	python3 fig_work.py
	python3 fig_econ.py
	python3 fig_system.py

workbook:
	python3 build_workbook.py

report:
	python3 build_report.py

pdf: report
	cd ../report && $(CHROME) --headless --disable-gpu --no-sandbox \
	  --no-pdf-header-footer --allow-file-access-from-files \
	  --run-all-compositor-stages-before-draw --virtual-time-budget=30000 \
	  --print-to-pdf=Mumbai_Real_Estate_Master_Playbook_2026.pdf report.html
	@pdfinfo $(PDF) | grep -E "^(Pages|Page size)" || true

clean:
	rm -f ../figures/*.png ../data/*.csv ../report/report.html $(PDF)
