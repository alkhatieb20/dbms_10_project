# DBMS_10 – Projektvorschlag für die Ausarbeitung

**Modul:** Einführung in Datenbankmanagementsysteme · THGA Bochum
**Dozent:** Stephan Bökelmann · <sboekelmann@ep1.rub.de>
**Voraussetzungen:** Vorlesungen 01–10, Übungen DBMS_01–DBMS_09

Diese Übung ist **anders aufgebaut** als die bisherigen: Sie schreiben keinen
Code, sondern **entwerfen** ein eigenes datenbankgestütztes System und reichen
dazu einen **Projektvorschlag** beim Dozenten ein. Der Vorschlag ist die
Grundlage Ihrer **Ausarbeitung** (Prüfungsleistung), in der Sie über das
Semester ein vollständiges System bauen:

**Frontend → FastAPI (REST) → PostgreSQL**, orchestriert durch **Docker Compose**.

Die vollständige Aufgabenstellung inklusive Vorlage, Bewertungskriterien und
einem durchgängigen Beispiel steht im gesetzten Handout.

## Build

Voraussetzung: `latexmk` und TeX Live (`apt install latexmk texlive-full`).

```bash
make          # baut out/dbms_10.pdf
make clean    # Hilfsdateien entfernen, PDF behalten
make distclean# alles entfernen inkl. out/
```

## Struktur

```
src/dbms_10.tex     # Aufgabenstellung (LaTeX-Quelle)
style/thga-db.sty   # THGA-Corporate-Design (Kopie aus dem Kurs-Repo)
Makefile            # Build über latexmk
out/                # generiertes PDF (nicht eingecheckt)
```
