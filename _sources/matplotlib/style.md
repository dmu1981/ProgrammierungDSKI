# 🎨 Stile, Farben & Design

## 🎨 Farben & benutzerdefinierte Paletten
### 🔹 Direkt per Name:
```python
plt.plot(x, y, color="red")
```
### 🔹 HEX-Code (Webfarbe):
```python
plt.plot(x, y, color="#1f77b4")  # ein schönes Blau
```

### 🔹 Benutzerdefinierte Liste:
```python
farben = ["#1f77b4", "#ff7f0e", "#2ca02c"]
for i in range(3):
    plt.plot(x, y[i], color=farben[i])
```

## 🔄 Linienstile, Marker & Transparenz
| Element | Code | Beschreibung
| - | - | -
Linienstil | `linestyle="--"` | gestrichelt
Marker | `marker="o"` | Kreise
Transparenz | `alpha=0.5` | 50 % durchsichtig

```python
plt.plot(x, y, linestyle="--", marker="s", alpha=0.7)
```

### 🧾 Design-Themes: `plt.style.use()`
Matplotlib hat eingebaute Design-Vorlagen:

```python
plt.style.available
```

Beispiele:
* "ggplot" (klassisch, freundlich)
* "seaborn" (harmonisch, lesbar)
* "fivethirtyeight" (medienfreundlich)
* "dark_background" (für Präsentationen)

```python
plt.style.use("seaborn-v0_8-darkgrid")
```
![Dark Grid](seaborn-v0_8-darkgrid.png)


```python
plt.style.use("dark_background")
```
![Dark Grid](dark_background.png)

```python
plt.style.use("fivethirtyeight")
```
![fivethirtyeight](fivethirtyeight.png)

```python
plt.style.use("seaborn-v0_8-pastel")
```
![seaborn-v0_8-pastel](seaborn-v0_8-pastel.png)

```python
plt.style.use("ggplot")
```
![ggplot](ggplot.png)

⚠️ Muss vor dem Plot gesetzt werden.

## ✅ Zusammenfassung
Element | Beispiel
| - | -
Farbe | `color="red"` oder `"#1f77b4"`
Linienstil | `linestyle="--"`
Marker | `marker="o"`
Transparenz | `alpha=0.5`
Stil verwenden | `plt.style.use("seaborn")`
Plot speichern | `plt.savefig(..., dpi=300)`

## ✍️ Übung: Mehrfarbiges Linien-Diagramm mit Stil
Aufgabe:

* Verwende `plt.style.use()` mit einem Stil deiner Wahl

* Erstelle 3 verschiedene Reihen von Daten (z. B. Sinuskurven)

* Verwende unterschiedliche Farben, Marker und Linienstile

* Füge eine Legende und Achsentitel hinzu

* Speichere den Plot als stildiagramm.png

### ✅ Beispiel-Lösung:
```{admonition} 💡 Lösung anzeigen
:class: dropdown

```python
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-darkgrid")

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(2 * x)

plt.plot(x, y1, label="sin(x)", color="blue", linestyle="-", marker="o", alpha=0.7)
plt.plot(x, y2, label="cos(x)", color="green", linestyle="--", marker="s", alpha=0.7)
plt.plot(x, y3, label="sin(2x)", color="red", linestyle=":", marker="^", alpha=0.7)

plt.title("Mehrfarbiges Linien-Diagramm")
plt.xlabel("x-Werte")
plt.ylabel("y-Werte")
plt.legend()
plt.tight_layout()
plt.savefig("stildiagramm.png", dpi=300)
plt.show()
```
