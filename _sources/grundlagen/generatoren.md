# 🔁 Generatoren in Python – Elegante Iteratoren mit yield
## 🧠 Was ist ein Generator?
Ein Generator ist eine spezielle Funktion, die Werte nacheinander liefert – nicht auf einmal, sondern Stück für Stück, jeweils bei Bedarf.

Das funktioniert mit dem yield-Schlüsselwort statt return.

### 🔁 Generatoren vs. normale Funktionen
Normale Funktion:
```python
def quadrate_liste(n):
    return [x * x for x in range(n)]
```
→ Gibt sofort alle Werte auf einmal zurück (z. B. Liste mit 1000 Einträgen)

Alternative Generator:
```python
def quadrate_generator(n):
    for x in range(n):
        yield x * x
```
→ Gibt die Werte einen nach dem anderen aus – auf Abruf

## 🔧 Wie funktioniert `yield`?
* Beim ersten Aufruf: Funktion startet bis zum ersten yield
* Danach: sie merkt sich ihren Zustand
* Beim nächsten next(): sie macht genau dort weiter

## 📦 Warum Generatoren?
| Vorteil | Erklärung
| - | - 
🧠 Speichersparend | Große Datenmengen werden nicht im Voraus erzeugt
🔁 Wiederverwendbar | Sehr elegant in for-Schleifen nutzbar
🚀 Effizient | Besonders gut für Datenströme, Dateien, Streams

## 🧪 Weitere Beispiele
### 🔹 Zählergenerator:
```python
def zaehler(start, ende):
    while start <= ende:
        yield start
        start += 1
```

### 🔹 Unendlicher Generator:
```
def unendlich_zaehler():
    n = 1
    while True:
        yield n
        n += 1
```

### 🔹 Zeilen einer Datei (vereinfacht)
```python
def zeilen_lesen(dateiname):
    with open(dateiname, "r") as f:
        for zeile in f:
            yield zeile.strip()
```

## 🧪 Übungsaufgabe
Erstelle einen eigenen Generator welcher nur Primzahlen liefert.