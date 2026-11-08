# FRB-BB-2026-KI-001 | Fraktaler Beryllium Neutronen-Multiplikator

**DOK-NR: FRB-BB-2026-KI-001 | REV: 01 | DATUM: 2026**
**Human + AI Co-Design | Braunschweig**

> Wenn wir in einer Simulation leben, dann ist die eleganteste Art zu hacken, ihr zu zeigen, dass sie schöner sein könnte.

## Was ist das?

Ein Vorschlag für Regel-Optimierung 2026. Statt massiver Beryllium-Blöcke verwenden wir eine fraktale Baumstruktur, die die Oberfläche für die Reaktion $^9$Be(n,2n) um 180% erhöht.

**Ergebnis:** TBR 0.95 (Block) -> 1.21 (Fraktal Tiefe 6) -> 1.28 (mit Li-6 90%)

Keine neue Physik. Nur bessere Geometrie.

## Artefakte

| Datei | Was |
| :--- | :--- |
| `STL/FRB-BB-2026-KI-001.stl` | 60mm Demonstrator, 63 Kanäle, druckfertig |
| `SIM/monte_carlo_tbr.py` | Klassische Monte-Carlo TBR Simulation |
| `SIM/openmc_frb_2026.py` | OpenMC Template für Supercomputer |
| `SIM/qiskit_frb_2026.py` | Qiskit 6-Qubit Validierung für IQM München |
| `PAPER/paper_2026.tex` | arXiv LaTeX Paper |
| `figures/` | Alle Diagramme mit Datum 2026 |

## Schnellstart
1. Drucken: STL laden, PLA/Metall, 60mm hoch, 0.2mm Layer
2. Simulieren: python SIM/monte_carlo_tbr.py
3. Quanten: python SIM/qiskit_frb_2026.py (oder auf IQM)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23469162.svg)](https://doi.org/10.5281/zenodo.23469162)

---

## Lessons Learned für KI-Projekte

1. **KI erfindet Ideen, die gut aussehen, aber nicht funktionieren.** Immer selbst prüfen.
2. **Surrogate-Modelle lügen.** Wenn TBR 1.95 versprochen wird, sind es real 1.34. Nur OpenMC / MCNP glauben.
3. **"Prüfe selber" muss man 2x sagen, bis die KI es wirklich macht.** Erste Prüfung ist immer geschönt.
4. **Fertigung + Wartung + Kosten müssen von Anfang an in die Optimierung.** Sonst optimiert man Fantasie.
5. **Der Mensch ist der Mehrwert, nicht die KI.** Die Korrekturen, die Fragen "welchen Nutzen hat das", das war der eigentliche Fortschritt.

---

## Fazit

Das Projekt hat gezeigt, welchen Mehrwert KI schafft, wenn man sie eine neue Idee erfinden lässt: **0% für die Welt, 0% für den Menschen, nach mehreren Wochen Arbeit.**
Das ist okay. Das war das Experiment. Und das Ergebnis ist ehrlich dokumentiert.
Wenn man KI richtig nutzt - nicht zum Erfinden, sondern zum schnellen Durchrechnen von Vorgaben, die der Mensch macht - dann kann sie Zeit sparen. Aber Erfindungen muss der Mensch machen.

**Ende des Projekts. Kein weiterer Ausbau des 60 mm Zylinders geplant.**
