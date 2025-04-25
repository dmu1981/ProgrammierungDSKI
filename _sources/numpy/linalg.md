# 🔢 Lineare Algebra mit NumPy

## 🧮 Matrixmultiplikation: `np.dot()` vs. `@`
```python
import numpy as np

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

# Variante 1:
print(np.dot(A, B))

# Variante 2:
print(A @ B)
```

➡️ Beide Varianten führen zur Matrixmultiplikation, aber @ ist moderner und lesbarer (ab Python 3.5)

## 🔁 Transponieren
```python
print(A.T)
```

➡️ Vertauscht Zeilen und Spalten

## 🧠 Determinante & Inverse
```python
# Determinante:
det = np.linalg.det(A)
print("Determinante:", det)

# Inverse berechnen:
A_inv = np.linalg.inv(A)
print("Inverse:\n", A_inv)
```

### ⚠️ Nur möglich, wenn die Matrix quadratisch und nicht singulär ist

## 📌 Gleichungssystem lösen: `np.linalg.solve()`
Gegeben:
Ax = b
Finde: x

```python
A = np.array([[2, 1],
              [1, 3]])
b = np.array([8, 13])

x = np.linalg.solve(A, b)
print("Lösung x:", x)
```

➡️ Liefert exakte Lösung (schneller und stabiler als inv(A) @ b)

### 🧮 Eigenwerte und Eigenvektoren
```python
A = np.array([[4, 2],
              [1, 3]])

eigwerte, eigvektoren = np.linalg.eig(A)

print("Eigenwerte:", eigwerte)
print("Eigenvektoren:\n", eigvektoren)
```
➡️ Wichtig z. B. in:

* PCA (Hauptkomponentenanalyse)
* Schwingungssystemen
* Differentialgleichungen

## ✅ Zusammenfassung

Funktion | Bedeutung
| - | -
`@`, `np.dot()` | Matrixmultiplikation
`.T` | Transponieren
`np.linalg.det()` | Determinante
`np.linalg.inv()` | Inverse
`np.linalg.solve(A, b)` | Gleichungssystem lösen (Ax = b)
`np.linalg.eig()` | Eigenwerte & -vektoren

## ✍️ Übung: Löse ein lineares Gleichungssystem
Gegeben ist das System:

```python
3x + 2y = 16  
4x -  y =  9
```

* Stelle die Koeffizientenmatrix A und den Vektor b auf

* Löse das Gleichungssystem mit np.linalg.solve()

* Überprüfe die Lösung mit Einsetzen

### ✅ Beispiel-Lösung:
```{admonition} 💡 Lösung anzeigen
:class: dropdown

```python
A = np.array([[3, 2],
              [4, -1]])

b = np.array([16, 9])

x = np.linalg.solve(A, b)
print("Lösung [x, y]:", x)

# Kontrolle:
print("Kontrolle: A @ x =", A @ x)
```