# 🔢 Indexierung, Slicing & Boolean-Masken

## 🔁 Fortgeschrittenes Slicing in 2D/3D-Arrays
```python
import numpy as np

a = np.array([[ 1,  2,  3],
              [ 4,  5,  6],
              [ 7,  8,  9]])

a[0]        # [1 2 3], Erste Zeile
a[:, 0]     # [1 4 7], Erste Spalte
a[0:2, 1:3] # [[2 3], [5 6]], Submatrix
```

## 🧬 2. Teilarrays vs. Kopien
```python
sub = a[0:2, 0:2]  # TEILARRAY (VIEW!)
sub[0, 0] = 999
print(a)           # ⚠️ Das Original wurde verändert!
```
➡️ slicing gibt eine Referenz, keine Kopie

### ❗ Kopie erzeugen:
```python
kopie = a[0:2, 0:2].copy()
```

## 🎯 Bedingte Auswahl mit Boolean-Masken
```python
a = np.array([1, 3, 5, 7, 9])
maske = a > 4
print(maske)        # [False False True True True]
print(a[maske])     # [5 7 9]
```

➡️ Oder direkt:
```python
print(a[a > 4])     # [5 7 9]
```

## ✏️ Werte über Maske gezielt ändern
```python
a = np.array([1, 3, 5, 7, 9])
a[a > 5] = 0
print(a)  # → [1 3 5 0 0]
```
➡️ Sehr nützlich für Filtern, Maskieren, Säubern von Daten

## ✅ Zusammenfassung
| Technik | Beispiel
| - | - 
2D-Slicing | `a[0:2, 1:3]`
Teilansicht vs. Kopie | `.copy()` nötig, um Original zu erhalten
Bedingte Auswahl | `a[a > 5]`
Werte ändern per Maske | `a[a > 5] = 0`

## ✍️ Übung
Aufgabe:

* Erzeuge ein 4×4 Array mit Zufallszahlen von 0–9
* Berechne den Mittelwert aller Werte
* Setze alle Werte größer als der Mittelwert auf 0
* Gib das veränderte Array aus

✅ Lösung:
```{admonition} 💡 Lösung anzeigen
:class: dropdown

```python
np.random.seed(0)

a = np.random.randint(0, 10, size=(4, 4))
print("🔢 Ursprüngliches Array:\n", a)

mittelwert = a.mean()
print("📏 Mittelwert:", mittelwert)

a[a > mittelwert] = 0
print("🎯 Ergebnis nach Maskierung:\n", a)
```
