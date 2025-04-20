# 📦 Tupel - Die unveränderbare Liste

## 🔍 Was ist ein Tupel? 
Ein Tupel ist eine unveränderbare (immutable) Folge von Werten. Es ist wie eine Liste – aber fest.

**Beispiel**:

```
farben = ("rot", "grün", "blau")
```
✅ Vorteile:

* Datensicherheit (kann nicht verändert werden)
* Schneller als Listen
* Ideal für feste Daten (z. B. Koordinaten, Konstanten)

## 🔧 Tupel erstellen & verwenden
```python
koordinaten = (10, 20)
farben = ("rot", "grün", "blau")
einer = (42,)  # wichtig: Komma macht es zu einem Tupel!
keinTupel = (42) # ⚠️ Das ist kein Tupel!
info = ("Max", 25, True)

print(farben[1])  # → grün
```

## ⚙️ Unpacking
Tupel können automatisch entpackt werden
```python
x, y, z = (3, 4, 5)
print(x + y + z)
```

Wenn bestimmte Elemente nicht benötigt werden können diese durch einen Unterstrich ignoriert werden
```python
studenten = [("Anna", 982939), 
             ("Beate", 992112),
             ("Carla", 878922),
             ("Denise", 938772),
             ("Erika", 1087732),
             ("Frauke", 1132934)]

for name, _ in studenten:
  print(name)             
```

## ✨ Die ``enumerate``-Funktion
Mit der [enumerate](https://www.w3schools.com/python/ref_func_enumerate.asp) Funktion können Listen oder Tupel aufgezählt werden. Dabei liefert der Iterator in jedem Schritte in Tupel bestehend aus dem Index sowie dem eigentlichen Element. 

```python
A = ["Anna", "Beate", "Carla", "Denise", "Erika", "Frauke"]
for index, name in enumerate(A):
  print(f"Hallo {name}. Du bist auf Platz {index} der Liste!")
```

## 🎓 Mini-Projekt
Schreibe ein kleines Programm welches den Nutzer verschiedene Meßgrößen $x_i$ (als Fließkommazahl abfragt).
Zu jeder Zahl soll ebenfalls erfasst werden wie häufig diese Meßgröße gemessen wurden $\omega_i$. 

Erzeuge eine Liste deren Elemente
Tupel bestehend aus der Meßgröße und deren Häufigkeit ist. Die Eingabe endet sobald der Nutzer eine leere Antwort gibt (also keine Zahlen eingibt).

Berechne dann den gewichteten arithmetischen Mittelwert der Meßgrößen, also 

$$E = \frac{\sum_i \omega_i x_i}{\sum_i\omega i}$$

**Beispielausgabe des Programms**:
```
Gib die Meßgröße ein:3
Gib die Häufigkeit der Meßgröße ein:3
Gib die Meßgröße ein:8
Gib die Häufigkeit der Meßgröße ein:2
Gib die Meßgröße ein:
Das arithmetische Mittel ist 5.0
```

Die Liste sieht dann so aus
```python
[(3.0, 3), (8.0, 2)]
```
<!--- ```python
elemente = []
while True:
  zahl = input("Gib die Meßgröße ein:")
  if zahl == "":
    break
  gewicht = input("Gib die Häufigkeit der Meßgröße ein:")
  if gewicht == "":
    break
  elemente.append((float(zahl), int(gewicht)))

summeX, summeW = 0, 0
for x, w in elemente:
  summeX = summeX + x * w
  summeW = summeW + w

print(f"Das arithmetische Mittel ist {summeX / summeW}") 
``` --->
