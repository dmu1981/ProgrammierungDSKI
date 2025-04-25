# 🎨  Matplotlib – Daten sichtbar machen mit Python

## 🧠 Warum Visualisierung?
Daten sind oft Zahlenkolonnen, Tabellen oder Zeitreihen – informativ, aber schwer verständlich auf den ersten Blick.

Menschen denken visuell – wir sehen Trends, Muster, Ausreißer sofort, wo Tabellen uns nur Zahlen zeigen.

### 📊 Ein gutes Diagramm kann:

* komplexe Sachverhalte in Sekunden erfassbar machen

* Zusammenhänge oder Ausreißer aufdecken

* Modelle und Berechnungen erklärbar machen

* in Berichten, Präsentationen und Dashboards glänzen ✨

## 🐍 Was ist Matplotlib?
Matplotlib ist die Standardbibliothek für Datenvisualisierung in Python.
Sie ist extrem flexibel, weit verbreitet und für fast alle Diagrammarten geeignet:

| Diagrammtyp | Funktion
| - | - 
Liniendiagramm | `plt.plot()`
Streudiagramm | `plt.scatter()`
Balkendiagramm | `plt.bar() / barh()`
Histogramm | `plt.hist()`
Boxplot | `plt.boxplot()`
Kreisdiagramm | `plt.pie()`
Heatmap, Surface | `plt.imshow()`, `contour()` etc.

## 📌 Installation
MatPlotLib wird wie jedes andere Paket auch installiert
```bash
pip install matplotlib
```

Im Python-Code wird das Paket dann importiert. Da oft nicht alles gebraucht wird ist ein üblicher Weg so:

```python
from matplotlib import pyplot as plt
```

## 📘 Abschnitt 1 – Einführung & Grundlagen
* Was ist Matplotlib?
* pyplot vs. object-oriented interface
* Erste Plots: plt.plot(), plt.title(), plt.xlabel(), plt.ylabel()
* Achsen & einfache Beschriftung
* Diagramm anzeigen (plt.show()) und speichern (plt.savefig())

Übung: Erstelle eine einfache Linie (z. B. Wachstum über Zeit)

## 📘 Abschnitt 2 – Diagrammtypen I: Linien, Punkte, Balken
* plt.plot() – Linien
* plt.scatter() – Punktwolken
* plt.bar() / plt.barh() – Säulen- und Balkendiagramme

* Farben, Marker, Linientypen

Übung: Vergleich zweier Produktverkäufe mit Balken- und Liniendiagramm

## 📘 Abschnitt 3 – Diagrammtypen II: Histogramme, Boxplots, Torten
* plt.hist() – Histogramme für Häufigkeiten
* plt.boxplot() – Verteilung, Median, Ausreißer
* plt.pie() – Kreisdiagramme (mit Prozentangaben)

Übung: Erstelle ein Histogramm von Zufallszahlen & eine Boxplot-Auswertung

## 📘 Abschnitt 4 – Achsen, Layout & Subplots
* Achsenskalen: plt.xlim(), plt.ylim(), plt.xticks()
* Log-Skalen
* Mehrere Diagramme nebeneinander: plt.subplot(), plt.subplots()
* Layout verbessern mit tight_layout()

Übung: Erstelle ein 2×2 Grid mit vier unterschiedlichen Diagrammtypen

## 📘 Abschnitt 5 – Stile, Farben, Design
* Farben und benutzerdefinierte Farbpaletten
* Linienstile, Marker, Transparenz (alpha)
* plt.style.use() – vordefinierte Themes
* Design-Tipps für Präsentationen

Übung: Erstelle ein mehrfarbiges Linien-Diagramm mit Legende & angepasstem Stil

## 📘 Abschnitt 6 – Interaktion, Annotation, Beschriftung
Themen:
* plt.legend() – automatische & manuelle Legenden
* plt.annotate() – Text & Pfeile im Plot
* Tooltips, Cursor-Infos (optional interaktiv mit mplcursors)
* Speicherung in verschiedenen Formaten (PNG, SVG, PDF)

Übung: Markiere Extremwerte in einem Linienplot mit Annotationen

## 📘 Abschnitt 7 – Matplotlib mit Pandas & NumPy kombinieren
* Direktes Plotten von DataFrames (df.plot())
* Visualisierung von Zeitreihen
* Darstellung von Gruppenvergleichen
* Beispiel mit NumPy: mathematische Funktionen visualisieren
 
Übung: Lade CSV mit Temperaturdaten, zeige Verlauf + Monatsmittel im Plot