# 🔢 Einstieg in Arrays
## 🐍 NumPy importieren
```python
import numpy as np
```
✅ Best Practice: np als Alias verwenden

## 🔢 NumPy Arrays erstellen
```python
a = np.array([1, 2, 3])
print(a)
```
➡️ a ist jetzt ein 1D NumPy Array mit den Werten 1, 2, 3

## 🧱 Mehrdimensionale Arrays:
```python
b = np.array([[1, 2, 3],
              [4, 5, 6]])
```
➡️ b ist ein 2D Array (Matrix)

## 🔁 Unterschied zu Python-Listen
| Python-Liste | NumPy Array
| - | - 
`[1, 2, 3]` | `np.array([1, 2, 3])`
beliebige Datentypen | homogener Datentyp (z. B. int)
langsam bei Schleifen | schnell durch Vektorisierung

## ⚠️ Beispiel: mathematischer Unterschied
```python
liste = [1, 2, 3]
array = np.array([1, 2, 3])

print(liste * 2)   # → [1, 2, 3, 1, 2, 3]
print(array * 2)   # → [2, 4, 6]
```

## 🔍 3. Eigenschaften von Arrays
Sei
```python
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3],
              [4, 5, 6]])
```

### 📐 shape – Form (z. B. Zeilen × Spalten)
```python
print(a.shape)  # (3,)
print(b.shape)  # (2, 3)
```

### 📏 ndim – Anzahl Dimensionen
```python
print(a.ndim)   # 1
print(b.ndim)   # 2
```

### 📊 dtype – Datentyp der Elemente
```python
print(a.dtype)  # int64 oder int32 (je nach System)
```

### 🔢 size – Anzahl aller Elemente
```python
print(a.size)   # 3
print(b.size)   # 6
```

## ✅ Zusammenfassung
| Attribut | Bedeutung
| - | - 
`.shape` | Form des Arrays (z. B. (3, 2))
`.ndim` | Dimensionen (1D, 2D, 3D, …)
`.dtype` | Datentyp der Elemente (int, float…)
`.size` | Gesamtzahl der Elemente