# 🧩 Eigene Module in Python

## 📦 Was ist ein Modul?
Ein Modul ist einfach eine .py-Datei, die Funktionen, Klassen oder Variablen enthält und in anderen Dateien wiederverwendet werden kann.

```python
# Datei: mathetools.py

def quadrat(x):
    return x * x

def kubik(x):
    return x * x * x
```

Du kannst diese Datei jetzt in einem anderen Skript verwenden:
Dazu muß die Datei mathetools.py und die Datei main.py im selben Verzeichniss liegen!
```python
# Datei: main.py

import mathetools

print(mathetools.quadrat(3))  # → 9
```

## 📌 `` import`` im Detail

| Variante | Beschreibung
| - | -
`import modul` | Zugriff über `modul.funktion()`
`from modul import funktion` | Direktzugriff auf Funktion
`from modul import *` | (Nicht empfohlen) – importiert alles
`import modul as m` | Alias für kürzere Schreibweise

```python
from mathetools import quadrat
print(quadrat(5))  # → 25
```

## 🔍 Was bedeutet __name__ == "__main__"?
Jede Python-Datei hat eine besondere Variable namens __name__.
Wenn du eine Datei direkt ausführst, ist:
```python
__name__ == "__main__"
``` 

Wenn du die Datei aber **importierst**, ist:
```python
__name__ == "modulname"
```

### ✅ Typisches Beispiel:
```python
# Datei: mathetools.py

def quadrat(x):
    return x * x

if __name__ == "__main__":
    # Nur ausführen, wenn Datei direkt gestartet wird
    print("Test: quadrat(4) =", quadrat(4))
```

### ➕ Warum ist das sinnvoll?
So kannst du ein Modul wiederverwenden und testen gleichzeitig

Beim Importieren stört der Testcode nicht

Gute Praxis für größere Projekte

## ✍️ Übungsaufgaben
### 🔸 Aufgabe 1: Mathemodul
Erstelle ein Modul mathemodul.py mit `fakultaet(n)` und `ist_gerade(n)`

Verwende es in einem anderen Skript mit `import mathemodul`

### 🔸 Aufgabe 2: __main__-Test
Füge deinem Modul Testcode unter `if __name__ == "__main__"` hinzu

Teste durch direktes Ausführen und durch Import

## Module in eigene Ordner auslagern
### 📁 Beispielhafte Projektstruktur
```css
mein_projekt/
│
├── main.py
├── tools/
│   ├── __init__.py
│   ├── mathe.py
│   ├── strings.py
```` 
### 🔸 tools/mathe.py
```python
def quadrat(x):
    return x * x
```
### 🔸 tools/strings.py
```python
def umkehren(text):
    return text[::-1]
```
### 🔸 tools/__init__.py
```python
# Leeres Init erlaubt das Importieren von tools.mathe
# oder du kannst hier gezielt Dinge „exportieren“:

from .mathe import quadrat
from .strings import umkehren
```

### 🚀 Import in main.py
```python
# Variante 1: mit Modulnamen
from tools import mathe
from tools import strings

print(mathe.quadrat(5))
print(strings.umkehren("Hallo"))

# Variante 2: direkt aus __init__.py (wenn dort importiert)
from tools import quadrat, umkehren

print(quadrat(6))
print(umkehren("Welt"))
```

### ❓ Was macht `__init__.py` konkret?
* Macht einen Ordner zu einem importierbaren Paket
* Wird beim ersten Import des Pakets ausgeführt
* Kann Variablen, Funktionen, Klassen exportieren (siehe oben)
* Kann auch Initialisierungslogik enthalten (selten nötig bei einfachen Projekten)