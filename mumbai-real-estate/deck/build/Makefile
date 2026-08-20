CHROME ?= /opt/pw-browsers/chromium-1194/chrome-linux/chrome
DECK   := ../out/Brickrock_Realty_Pitch_Deck.pdf
INDEX  := ../out/Brickrock_Deck_Diligence_Index.pdf

.PHONY: all figures deck index clean

all: figures deck index brief

figures:
	python3 fig_deck.py

deck:
	python3 build_deck.py
	cd ../out && $(CHROME) --headless --disable-gpu --no-sandbox \
	  --no-pdf-header-footer --allow-file-access-from-files \
	  --run-all-compositor-stages-before-draw --virtual-time-budget=30000 \
	  --print-to-pdf=Brickrock_Realty_Pitch_Deck.pdf deck.html
	@pdfinfo $(DECK) | grep -E "^(Pages|Page size)" || true

index:
	python3 build_index.py
	cd ../out && $(CHROME) --headless --disable-gpu --no-sandbox \
	  --no-pdf-header-footer --allow-file-access-from-files \
	  --run-all-compositor-stages-before-draw --virtual-time-budget=30000 \
	  --print-to-pdf=Brickrock_Deck_Diligence_Index.pdf diligence_index.html
	@pdfinfo $(INDEX) | grep -E "^(Pages|Page size)" || true

clean:
	rm -f ../figures/s*.png ../out/deck.html ../out/diligence_index.html $(DECK) $(INDEX)

BRIEF  := ../out/Brickrock_Presenter_Brief.pdf

.PHONY: brief

brief:
	python3 build_notes.py
	cd ../out && $(CHROME) --headless --disable-gpu --no-sandbox \
	  --no-pdf-header-footer --allow-file-access-from-files \
	  --run-all-compositor-stages-before-draw --virtual-time-budget=30000 \
	  --print-to-pdf=Brickrock_Presenter_Brief.pdf presenter_brief.html
	@pdfinfo $(BRIEF) | grep -E "^(Pages|Page size)" || true
