# 🎨 Achsen, Layout & Subplots

## 🔁 Achsenskalen und Ticks
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y)
plt.xlim(0, 6)
plt.ylim(0, 60)
plt.xticks([1, 3, 5])
plt.yticks(range(0, 61, 10))
plt.title("Manuelle Achsenskalierung")
plt.show()
```

## 📉 2. Logarithmische Skala
```python
import numpy as np

x = np.linspace(1, 100, 100)
y = np.log(x)

plt.plot(x, y)
plt.xscale("log")
plt.title("Logarithmische X-Achse")
plt.xlabel("X (log)")
plt.ylabel("log(X)")
plt.grid(True)
plt.show()
```

### ⚠️ Funktioniert nur bei positiven Werten!

## 🔳 3. Subplots: `plt.subplot()` vs. `plt.subplots()`
### **Variante 1**: Einfacher Aufbau mit `subplot()`
```python
plt.subplot(2, 2, 1)  # 2 Zeilen, 2 Spalten, Plot 1
plt.plot([1, 2, 3])

plt.subplot(2, 2, 2)
plt.bar(["A", "B"], [5, 7])

plt.subplot(2, 2, 3)
plt.hist(np.random.randn(100))

plt.subplot(2, 2, 4)
plt.boxplot(np.random.normal(100, 10, size=50))

plt.tight_layout()
plt.show()
```

### **Variante 2**: Mehr Kontrolle mit `subplots()`
```python
fig, axes = plt.subplots(2, 2, figsize=(10, 6))

axes[0, 0].plot([1, 2, 3])
axes[0, 0].set_title("Linie")

axes[0, 1].bar(["A", "B"], [5, 7])
axes[0, 1].set_title("Balken")

axes[1, 0].hist(np.random.randn(100))
axes[1, 0].set_title("Histogramm")

axes[1, 1].boxplot(np.random.normal(100, 10, size=50))
axes[1, 1].set_title("Boxplot")

plt.tight_layout()
plt.show()
```

## 🧰 Layout verbessern mit `tight_layout()`
Verhindert Überlappung von:

* Achsentiteln
* Beschriftungen
* Diagrammrahmen

### 👉 Immer vor plt.show() oder plt.savefig() aufrufen!

## ✅ Zusammenfassung

Funktion | Zweck
| - | -
`xlim()`, `ylim()` | Achsenbereiche setzen
`xticks()`, `yticks()` | Tick-Werte anpassen
`xscale("log")` | Logarithmische Skala
`subplot()` | mehrere Plots in einem Raster (einfach)
`subplots()` | mehrere Plots mit mehr Kontrolle
`tight_layout()` | automatisches Layout verbessern

## ✍️ Übung: Erstelle ein 2×2 Grid mit 4 Diagrammtypen
Aufgabe:

* Erzeuge ein 2×2-Raster mit plt.subplots()
* Fülle es mit folgenden Diagrammen:
    * Linienplot (z. B. sin(x))
    * Balkendiagramm (fiktive Umfrageergebnisse)
    * Histogramm (zufällige Werte)
    * Boxplot (z. B. Notenverteilung)

* Beschrifte jeden Plot sinnvoll

## ✅ Beispiel-Lösung:
```{admonition} 💡 Lösung anzeigen
:class: dropdown

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
werte = np.random.normal(50, 15, 200)

fig, axs = plt.subplots(2, 2, figsize=(10, 6))

# 1. Linienplot
axs[0, 0].plot(x, np.sin(x), color="blue")
axs[0, 0].set_title("Sinuskurve")

# 2. Balkenplot
kategorien = ["Ja", "Nein", "Vielleicht"]
anzahl = [45, 30, 25]
axs[0, 1].bar(kategorien, anzahl, color="orange")
axs[0, 1].set_title("Umfrage")

# 3. Histogramm
axs[1, 0].hist(werte, bins=15, color="green", edgecolor="black")
axs[1, 0].set_title("Histogramm")

# 4. Boxplot
axs[1, 1].boxplot(werte, patch_artist=True, boxprops=dict(facecolor="lightblue"))
axs[1, 1].set_title("Boxplot")

plt.tight_layout()
plt.show()
```