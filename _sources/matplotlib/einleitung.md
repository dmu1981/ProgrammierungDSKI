# 🎨 Erste Schritte mit MatPlotLib

## 🔧 pyplot vs. objektorientiert
Matplotlib kann auf zwei Arten verwendet werden:


| Stil | Beschreibung | Typischer Kontext
| - | - | - 
pyplot (imperativ) | einfach & schnell, wie bei MATLAB | schnelle Einzellinien
Objektorientiert | sauber, modular, besser für Subplots & Layouts | komplexere Diagramme

In dieser Vorlesung verwenden wir erstmal pyplot, das einfache Interface:
``` python
import matplotlib.pyplot as plt
```

## 📈 Erste Linie zeichnen: plt.plot()
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.show()
```
➡️ x-Achse: 1–5, y-Achse: 2–10 → einfaches Liniendiagramm

## ✏️ Titel & Achsenbeschriftungen
```python
plt.plot(x, y)
plt.title("Wachstum über Zeit")
plt.xlabel("Tage")
plt.ylabel("Größe (cm)")
plt.show()
```
➡️ Die Achsen sind jetzt beschriftet, das Diagramm hat einen Titel.

## 🖼️ Diagramm speichern mit plt.savefig()
```python
plt.plot(x, y)
plt.title("Wachstum über Zeit")
plt.xlabel("Tage")
plt.ylabel("Größe (cm)")
plt.savefig("wachstum.png")  # speichert als PNG
plt.show()
```
⚠️ `plt.savefig()` immer vor `plt.show()` aufrufen – danach wird das Bild „freigegeben“

## ✅ Zusammenfassung
| Funktion | Zweck
| - | - 
`plt.plot()` | Linie zeichnen
`plt.title()` | Titel setzen
`plt.xlabel()` | X-Achse beschriften
`plt.ylabel()` | Y-Achse beschriften
`plt.show()` | Plot anzeigen
`plt.savefig()` | Plot als Datei speichern

## 🧠 Bonus: Anpassung
```python
plt.plot(x, y, color="green", linestyle="--", marker="o")
```
➡️ Zeigt grüne gestrichelte Linie mit Kreismarkern an den Punkten

## ✍️ Übung: Wachstum visualisieren

* Erstelle zwei Listen `tage = [1, 2, 3, 4, 5]` und `groesse = [10, 12, 15, 19, 24]`

* Erstelle mit plt.plot() ein Liniendiagramm

* Beschrifte die x-Achse mit "Tage" und die y-Achse mit "Größe in cm"

* Gib dem Diagramm den Titel "Pflanzenwachstum"

* Speichere das Diagramm als "pflanze.png"

✅ Beispiellösung:
```{admonition} 💡 Lösung anzeigen
:class: dropdown
```python
tage = [1, 2, 3, 4, 5]
groesse = [10, 12, 15, 19, 24]

plt.plot(tage, groesse)
plt.title("Pflanzenwachstum")
plt.xlabel("Tage")
plt.ylabel("Größe in cm")
plt.savefig("pflanze.png")
plt.show()
```