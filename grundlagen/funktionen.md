# 🧩 Funktionen in Python – Code wiederverwenden und strukturieren

## 🔹 Warum Funktionen? 
Motivation:

* Vermeide Wiederholung
* Mache Code verständlicher
* Ermögliche Wiederverwendung

```python
# Schlechter Stil: Wiederholung
print("Hallo, Max!")
print("Hallo, Lisa!")

# Besser:
def begruessung(name):
    print("Hallo,", name)

begruessung("Max")
begruessung("Lisa")
```

## 🔹 Funktionen definieren und aufrufen
```python
def quadrat(x):
    return x * x

ergebnis = quadrat(5)
print(ergebnis)  # 25
```

## 🔹 Funktionen ohne Rückgabewert
```python
def begruessung(name):
    print("Hallo", name)
```    

## 🔹 Funktionen mit mehreren Rückgabewerten
Du kannst eine Funktion ein Tupel zurückgeben lassen wenn Du mehrere Rückgabewerte hast
```python
def rechnung(a, b):
    return a + b, a * b

summe, produkt = rechnung(3, 4)
```    

## 🔹 Standardwerte für Funktionsparameter
```python
def hallo(name="Welt"):
    print("Hallo,", name)

hallo()           # → Hallo, Welt
hallo("Anna")     # → Hallo, Anna
```    

⚠️ Achtung: Parameter mit Standardwerten dürfen immer nur **nach** Parameter ohne solche stehen.

```python
def foo(a, b=3): # Das ist ok
    return a * b 

def bar(a=3, b): # Das ist nicht ok    
    return a * b 
```    

## 🔹 Globale vs. Lokale Variablen
```python
x = 5 # Dies ist eine globale Variable

def test():
    x = 10 # Dies ist eine lokale Variable
    print("In Funktion:", x)

test()
print("Außerhalb:", x)
```

Man kann eine globale Variable in den lokalen "scope" ziehen um sie zu verwenden. 
```python
x = 5 # Dies ist eine globale Variable

def test():
    global x # Hierdurch wird die globale Variable x verwendet
    x = 10   # Jetzt wird die globale Variable x überschrieben
    print("In Funktion:", x)

test()
print("Außerhalb:", x)
```

⚠️ Achtung: Da dies unerwünschte Nebeneffekte haben kann die schwer zu debuggen sind sollte dies, wo immer möglich, vermieden werden.

## 🔹Funktionen sind [First Class Citizens](https://en.wikipedia.org/wiki/First-class_citizen#:~:text=In%20a%20given%20programming%20language,and%20assigned%20to%20a%20variable.)

In Python sind Funktionen eigenständige Objekte die dann wiederum z.B. einer Variable zugewiesen werden können bzw. als Rückgabewert oder Parameter einer anderen Funktion verwendet werden können. 
```python
def add(a, b):
  return a + b

def sub(a, b):
  return a - b

def calc(a, b, func):
  return f"Das Ergebniss ist {func(a, b)}"

def auswahl():
  while True:
    wahl = input("Möchte Sie addieren (a) oder subtrahieren (s)?")
    if wahl == "a":
      return add

    if wahl == "s":
      return sub

func = auswahl()
print(calc(3,4, func))
``` 

## 🔹 `map` und `filter`
Die [map](https://www.w3schools.com/python/ref_func_map.asp)() Funktion iteriert über einen Iterator und ruft die angegebene Funktion für jedes Element auf. Sie liefert dann einen neuen Iterator, welche die entsprechenden Rückgabewerte enthält. 

```python
def count_vokale(text):
  vokale = ['a', 'e', 'i', 'o', 'u']
  text = text.lower()
  count = 0
  
  for vokal in vokale:
    count += text.count(vokal)
  
  return count

for x in map(count_vokale, ['apple', 'banana', 'cherry']):
  print(x)
```

Die [filter](https://www.w3schools.com/python/ref_func_filter.asp) Funktion iteriert über einen Iterator und ruft die angegebene Funktion für jedes Element auf. Sie liefert dann einen neuen Iterator, welcher nur diejenigen Elemente enthält für die die Funktion `True` liefert.

```python
def isPrim(zahl):
  for teiler in range(2, zahl):
    if zahl % teiler == 0:
      return False
    
  return True

for primzahlen in filter(isPrim, range(100)):
  print(primzahlen)
```

## 🔹 Anonyme `lambda`-Funktionen
Lambda-Funktionen sind anonyme, also namenlose Funktionen, die man direkt inline schreiben kann:
```python
lambda parameter: ausdruck
```

**Beispiel 1**: Nur Wörter mit mehr als 4 Buchstaben
```python
woerter = ["Apfel", "Ei", "Bananenbrot", "Hund"]
lange = list(filter(lambda w: len(w) > 4, woerter))
# → ['Apfel', 'Bananenbrot']
```

**Beispiel 2**: Quadrate berechnen
```python
zahlen = [2, 3, 5, 7, 11, 13, 17]
quadrate = map(lambda x: x * x, zahlen)
for zahl, quadrat in zip(zahlen, quadrate):
  print(f"Das Quadrat von {zahl} ist {quadrat}")
```

**Beispiel 3**: Schlüsselelement zum sortieren auswählen
```python
personen = [("Max", 20), ("Anna", 25), ("Ben", 19)]
personen.sort(key=lambda x: x[1])
# → [('Ben', 19), ('Max', 20), ('Anna', 25)]
```

## 🧪 Übungsaufgabe: Fakultät
Schreibe eine Funktion ``fakultaet`` welche rekursiv die Fakultaet berechnet, also 

$$ n! = n\cdot (n-1)! $$

für $n > 1$ und $1! = 1$ (Abbruchbedingung).

## 🎓 Mini-Projekt: Vektoren der Länge nach sortieren
Schreibe ein kleines Programm welches den Nutzer mehrere zwei-dimensionale Vektoren $\textbf{x} = (x_1, x_2)$ eingeben lässt. Schreibe dazu eine Funktion welche die $x_1$ und $x_2$ Komponente des Vektors abfragt. Der Nutzer soll die beiden Komponenten mit Komma getrennt eingeben können. Verwende wieder [split](https://www.w3schools.com/jsref/jsref_split.asp)()
und [strip](https://www.w3schools.com/python/ref_string_strip.asp)() um die Komponenten geeignet zu trennen und wandle die erhaltenen Strings mit [float](https://www.w3schools.com/python/ref_func_float.asp)() in Gleitkommazahlen um ()

Rufe diese Funktion aus der Hauptschleife auf und füge den Vektor einer ständig wachsenden Liste mit allen Eingaben zu. Gibt der Nutzer keine Zahl ein so soll die Funktion ``None`` liefern. Das ist das Signal für das Hauptprogramm, die Eingabe zu beenden und zum zweiten Teil überzugehen. 

Definiere im zweiten Teil eine geeignete Funktion welche die euklische Länge eines Vektor berechnet, also 

$$ ||\textbf{x}||_2 = \sqrt{x_1^2 + x_2^2} $$

und sortiere die Liste der Vektoren nach der Länge. Gib anschließend alle Vektoren in sortierter Reihenfolge auf, deren Länge kleiner oder gleich 1 ist. 

[Lösung](vektorsolution.md)
