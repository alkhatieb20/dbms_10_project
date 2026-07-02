# ============================================================
#  Makefile – DBMS_10 · Projektvorschlag für die Ausarbeitung
#  THGA Bochum · Stephan Bökelmann
#
#  Voraussetzung: TeX Live mit latexmk (apt install latexmk texlive-full)
# ============================================================

LATEXMK  := latexmk
OUTDIR   := out

# -cd: latexmk wechselt vor dem Kompilieren ins Verzeichnis der
#      Quelldatei (src/), damit \input und der Stil-Suchpfad greifen.
# output-directory ist relativ zur Quelldatei, also ../out.
LMKFLAGS := -pdf -interaction=nonstopmode -halt-on-error \
            -cd -output-directory=../$(OUTDIR)

TEXENV   := TEXINPUTS="$(CURDIR)/style:.:$$TEXINPUTS"

STYLE    := style/thga-db.sty

## Hier alle Dokumente auflisten (ohne .tex):
DOCS     := dbms_10

ALL_PDF  := $(addprefix $(OUTDIR)/, $(addsuffix .pdf, $(DOCS)))
SRCS     := $(addprefix src/, $(addsuffix .tex, $(DOCS)))

# ---- Hauptziele ---------------------------------------------

.PHONY: all clean distclean help

all: $(ALL_PDF)

# out/-Verzeichnis anlegen falls nicht vorhanden
$(OUTDIR):
	mkdir -p $(OUTDIR)

# Generische Regel: src/*.tex → out/*.pdf
$(OUTDIR)/%.pdf: src/%.tex $(STYLE) | $(OUTDIR)
	$(TEXENV) $(LATEXMK) $(LMKFLAGS) $<

# ---- Aufräumen ----------------------------------------------

# Hilfsdateien entfernen, PDFs behalten
clean:
	$(TEXENV) $(LATEXMK) -c $(LMKFLAGS) $(SRCS)

# Alles entfernen, auch PDFs
distclean:
	$(TEXENV) $(LATEXMK) -C $(LMKFLAGS) $(SRCS)
	rm -rf $(OUTDIR)

# ---- Hilfe --------------------------------------------------

help:
	@echo "Verfügbare Targets:"
	@echo "  all        – Projektvorschlag-Dokument bauen  (→ $(OUTDIR)/)"
	@echo "  clean      – Hilfsdateien entfernen (PDFs bleiben)"
	@echo "  distclean  – alles entfernen inkl. PDFs und $(OUTDIR)/"
