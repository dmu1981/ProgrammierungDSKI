# 🔢 Array-Erzeugung, Indexierung & Rechnen

## 🛠️ Arrays gezielt erzeugen
### 🔹 Leere/Initialisierte Arrays:
```python
np.zeros((2, 3))      # 2x3 mit Nullen
np.ones((3, 2))       # 3x2 mit Einsen
np.eye(3)             # 3x3 Einheitsmatrix
```

### 🔹 Zahlenreihen:
```python
np.arange(0, 10, 2)   # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)  # 5 gleichmäßige Werte von 0 bis 1
```

## 🎲 Zufallszahlen mit np.random
```python
np.random.seed(42)            # für reproduzierbare Ergebnisse
np.random.rand(2, 3)          # gleichverteilte Zufallszahlen [0, 1)
np.random.randint(0, 10, size=(3, 3))  # ganzzahlige Zufallszahlen
```
## 🔎 3. Indexing und Slicing
### 🔸 1D-Array:
```python
a = np.array([10, 20, 30, 40, 50])
a[0]       # erstes Element
a[1:4]     # von Index 1 bis 3 → [20 30 40]
```
### 🔸 2D-Array:
```python
b = np.array([[1, 2, 3],
              [4, 5, 6]])

b[0, 1]    # 1. Zeile, 2. Spalte → 2
b[:, 0]    # alle Zeilen, 1. Spalte → [1 4]
b[1, :]    # 2. Zeile → [4 5 6]
```

## 🧠 Das Broadcasting-Prinzip
NumPy „passt“ kleinere Arrays automatisch an größere an, wenn möglich.

```python
a = np.array([1, 2, 3])
a + 10    # → [11 12 13]

m = np.array([[1, 2, 3],
              [4, 5, 6]])

m + a     # → [1+1, 2+2, 3+3] usw.
```

➡️ NumPy „broadcastet“ das kleinere Array über die passende Dimension

## ➕ Mathematische Operationen
```python
a = np.array([1, 2, 3])

a + 2          # → [3 4 5]
a * 2          # → [2 4 6]
a ** 2         # → [1 4 9]
np.sqrt(a)     # → [1.0 1.41 1.73]
np.sum(a)      # → 6
np.mean(a)     # → 2.0
```

### Auf 2D-Arrays:
```python
b = np.array([[1, 2, 3],
              [4, 5, 6]])

np.sum(b, axis=0)  # Spaltensumme → [5 7 9]
np.sum(b, axis=1)  # Zeilensumme → [6 15]
```

## ✅ Zusammenfassung
| Funktion | Beschreibung
| - | - 
`np.zeros()`, `np.ones()` | leere oder gefüllte Arrays
`np.arange()`, `linspace()` | Zahlenreihen
`np.random` | Zufallszahlen
`a[1:3], a[:,0]` | Indexing & Slicing
`+`, `*`, `np.sqrt()` | Mathematische Operationen
`np.sum(..., axis=...)` | Aggregation über Achsen
Broadcasting | Automatische Anpassung von Array-Formen