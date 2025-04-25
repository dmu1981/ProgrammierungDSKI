# 🔢 Mehrdimensionale Arrays & Reshape
## 🧱 Umformen mit reshape()
```python
a = np.arange(9)
a2 = a.reshape((3, 3))
print(a2)
```
➡️ Macht aus [0 1 2 3 4 5 6 7 8] eine 3×3-Matrix

⚠️ Voraussetzung: Anzahl der Elemente muss stimmen

⚠️ Ausnahme: Eine Dimension darf unbestimmt bleiben wenn der Rest passt
```python
a = np.arange(10)
a2 = a.reshape((-1, 5))
print(a2) 

# [[1,2,3,4,5], 
#  [6,7,8,9,10]]
```

## 🔄 Unterschied: `reshape()` vs. `flatten()` vs. `ravel()`
```python
b = a2.reshape(9)         # neue Form
f = a2.flatten()          # flache Kopie
r = a2.ravel()            # flache Ansicht (keine Kopie)
```

Methode | Rückgabe | Veränderung des Originals
| - | - | -
reshape() | neues Array | nein
flatten() | Kopie | nein
ravel() | Ansicht | ja (bei Änderungen am Original sichtbar)

## 🔁 Transponieren mit .T
```python
a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a.T)

# [[1, 4], 
#  [2, 5],
#  [3, 6]]
```
➡️ Spalten werden Zeilen, Zeilen werden Spalten

## 🧱 Arrays stapeln & kombinieren
### 🔹 Vertikal stapeln – `np.vstack()`
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.vstack([a, b])
# → [[1 2 3]
#    [4 5 6]]
```

### 🔹 Horizontal stapeln – `np.hstack()`
```python
np.hstack([a, b])
#  → [1 2 3 4 5 6]
```

### 🔹 Allgemein: `np.concatenate()`
```python
np.concatenate([a, b], axis=0)  # → [1 2 3 4 5 6]
```
➡️ Für 2D-Arrays auch mit axis=1 möglich

## ✂️ Arrays aufteilen
```python
x = np.arange(12).reshape(3, 4)
print(x)
```

```python
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
```

### 🔹 Spaltenweise teilen mit `np.split()`
```python
np.split(x, 2, axis=1)
```

➡️ Teilt in zwei Arrays mit jeweils 2 Spalten

### 🔹 Alternativ: `np.array_split()` – toleranter
```python
np.array_split(x, 3, axis=1)
```
➡️ Teilt Spalten auch bei ungerader Teilung

## ✅ Zusammenfassung
Funktion | Zweck
| - | - 
`reshape()` | Form ändern (z. B. 1D → 2D)
`flatten()` / `ravel()` | Array „flach“ machen
`.T` | Transponieren
`vstack()` / `hstack()` | Vertikal / horizontal stapeln
`split()` / `array_split()` | Arrays teilen entlang einer Achse

## ✍️ Übung
Aufgabe:

* Erzeuge ein 1D-Array mit 9 aufeinanderfolgenden Zahlen
* Forme es zu einer 3×3 Matrix
* Transponiere das Array mit .T
* Teile das transponierte Array in zwei gleich große Hälften (spaltenweise)
* Gib alle Zwischenschritte aus

## ✅ Beispiel-Lösung:
```{admonition} 💡 Lösung anzeigen
:class: dropdown

```python
a = np.arange(9)
print("🔢 1D-Array:\n", a)

a2 = a.reshape((3, 3))
print("\n🧱 3×3-Matrix:\n", a2)

aT = a2.T
print("\n🔄 Transponiert:\n", aT)

hälften = np.split(aT, 2, axis=1)
print("\n✂️ Gesplittet (zwei Hälften):")
for i, teil in enumerate(hälften, 1):
    print(f"Hälfte {i}:\n{teil}")
```