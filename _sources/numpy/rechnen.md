 # 🔢 Rechnen mit Arrays & Broadcasting

## ➕ Elementweise Rechenoperationen
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)      # [5 7 9]
print(a * b)      # [4 10 18]
print(a ** 2)     # [1 4 9]
print(np.sqrt(b)) # [2.0 2.24 2.45]
```

➡️ Alle Operationen sind elementweise – keine Schleifen nötig!

## 🧮 Vektor- und Matrixrechnung
```python
v = np.array([1, 2])
m = np.array([[1, 2],
              [3, 4]])

# Matrix-Vektor-Multiplikation:
print(m @ v)       # [5 11]

# Matrix-Matrix-Produkt:
print(m @ m)       # np.dot(m, m)
```

## 🔄 Broadcasting – automatische Formanpassung
NumPy erlaubt Rechnungen zwischen unterschiedlich großen Arrays – wenn die Formen kompatibel sind

### 🔹 Array + Skalar:
```python
a = np.array([1, 2, 3])
print(a + 10)  # [11 12 13]
```
### 🔹 2D-Array + 1D-Zeile:
```python
m = np.array([[1, 2, 3],
              [4, 5, 6]])

v = np.array([10, 20, 30])
print(m + v)
# [[11 22 33]
#  [14 25 36]]
```

### ⚠️ Broadcasting-Regeln:
Vergleiche von rechts nach links: z. B. (2, 3) mit (3,) → passt!

Fehlt eine Dimension → wird „gestreckt“ (broadcasted)

### 📊 Aggregationsfunktionen
```python
a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(np.sum(a))           # Gesamtsumme → 21
print(np.sum(a, axis=0))   # Spaltensummen → [5 7 9]
print(np.sum(a, axis=1))   # Zeilensummen → [6 15]

print(np.mean(a))          # Mittelwert → 3.5
print(np.std(a))           # Standardabweichung
```

## ⚡ 5. Warum ist NumPy schneller als Python-Schleifen?
* NumPy ist in C implementiert
* Rechenoperationen sind vektorisiert, keine for-Schleifen nötig
* Speicher liegt kontinuierlich vor (contiguous memory)

### 🔧 Beispiel: Summe von 1 Million Zahlen
```python
import time

# Python-Schleife
l = list(range(1_000_000))
start = time.time()
total = 0
for x in l:
    total += x
end = time.time()
print("Python-Schleife:", end - start, "Sekunden")

# NumPy
a = np.arange(1_000_000)
start = time.time()
total = np.sum(a)
end = time.time()
print("NumPy:", end - start, "Sekunden")
```

➡️ Typischerweise ist NumPy 10x–100x schneller!

## ✅ Zusammenfassung
| Funktion / Konzept | Beispiel
| - | - 
Elementweise Rechenoperation | `a + b`, `a * b`, `a ** 2`
Matrixrechnung | `A @ B`, `np.dot()`
Broadcasting | array + skalar, 2D + 1D
Aggregation | `sum()`, `mean()`, `std()`, axis=...
Effizienz | NumPy ist deutlich schneller als Python-Schleifen