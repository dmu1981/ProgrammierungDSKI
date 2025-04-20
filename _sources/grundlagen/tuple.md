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

## 🔧 Tupel erstellen & verwenden (10 Min)
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

Wenn bestimmte Elemente nicht benötigt werden können diese durch einen unterstrich ignoriert werden
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

