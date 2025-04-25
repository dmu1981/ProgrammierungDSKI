# 🔢 Einführung in NumPy – Das Fundament der numerischen Programmierung in Python
## 🧠 Was ist NumPy?
NumPy steht für Numerical Python und ist eine der wichtigsten und leistungsfähigsten Bibliotheken in der wissenschaftlichen Programmierung mit Python.

NumPy ist vor allem bekannt für sein zentrales Objekt: das n-dimensionale Array (ndarray). Es ist das Rückgrat vieler weiterer Pakete – z. B. Pandas, SciPy, scikit-learn, TensorFlow – und bildet die Grundlage für alle numerischen und datengetriebenen Aufgaben in Python.

## ✅ Warum NumPy statt Python-Listen?
| Python-Listen | NumPy-Arrays
| - | -
Langsam bei Berechnungen | Sehr schnell (C-basiert)
Unterschiedliche Typen | Einheitlicher Datentyp (homogen)
Kein Broadcasting | Rechnen ohne Schleifen
Kein echtes Multidimensional | Beliebig viele Dimensionen möglich

### ⚙️ Was kann NumPy?
Mit NumPy kannst du:

* große, mehrdimensionale Datenarrays effizient speichern und verarbeiten

* mathematische Operationen auf ganze Arrays gleichzeitig ausführen (Vektorisierung)

* Matrix- und lineare Algebra berechnen

* statistische Auswertungen durchführen

* Zufallszahlen erzeugen (für Simulationen oder Data Science)

## 🔧 NumPy installieren
```bash
pip install numpy
```

Dann
```python
import numpy as np
```

## 🧪 Mini-Beispiel:
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)        # [5 7 9]
print(a * b)        # [ 4 10 18]
```
➡️ Du musst keine Schleifen schreiben – NumPy übernimmt das für dich!

## 🧭 Übersicht: Themenplan

### 📘 Abschnitt 1 – Einführung in NumPy & Arrays
* NumPy Arrays: Erstellen mit np.array()
* Unterschiede zu Listen
* Array-Eigenschaften: shape, ndim, dtype, size
* Übung: Erstelle ein 1D- und 2D-Array, gib Form, Dimension, Datentyp aus

### 📘 Abschnitt 2 – Array-Erzeugung & Grundoperationen
* Erzeugen mit np.zeros(), np.ones(), np.arange(), np.linspace(), np.eye()
* Zufallsarrays mit np.random
* Indexing und Slicing (1D, 2D)
* Broadcast-Prinzip
* Mathematische Operationen: +, *, **, np.sqrt(), np.sum(), np.mean()
* Übung: Erzeuge ein 3×3 Array mit Zufallswerten und berechne Zeilensummen

### 📘 Abschnitt 3 – Indexierung, Slicing & Boolean-Masken
* Fortgeschrittenes Slicing in 2D/3D Arrays
* Teilarrays vs. Kopien
* Bedingte Auswahl (array[array > 5])
* Änderungen über Boolean-Masken
* Übung: Finde alle Werte > Mittelwert, setze sie auf 0

### 📘 Abschnitt 4 – Rechnen mit Arrays & Broadcasting
* Elementweise Operationen
* Vektor- und Matrixrechnung
* Broadcasting-Regeln (z. B. Array + Skalar, Array + Array mit anderer Form)
* Aggregationsfunktionen: sum, mean, std, axis=...
* Vergleich mit Schleifen → Warum NumPy effizient ist
* Übung: Vergleiche Laufzeit für Summe mit Schleife vs. NumPy-Operation

### Abschnitt 5 – Mehrdimensionale Arrays & Reshape
* `reshape()`, `flatten()`, `ravel()`
* Transponieren mit `.T`
* Stacken von Arrays: `np.vstack()`, `np.hstack()`, `np.concatenate()`, `np.split()`, `np.array_split()`
* Übung: Forme ein 1D-Array zu 3×3 Matrix, transponiere es, teile es in zwei Hälften

### 📘 Abschnitt 6 – Lineare Algebra mit NumPy
* np.dot() vs. @-Operator
* Matrix-Multiplikation
* Determinante, Inverse, Transponieren
* Eigenwerte, Lösen von Gleichungssystemen: `np.linalg.solve()`, `np.linalg.inv()`
* Übung: Löse ein lineares Gleichungssystem (Ax = b)

