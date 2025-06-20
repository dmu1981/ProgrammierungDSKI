# 🗂️ Kontrollstrukturen – Entscheidungen im Code
Kontrollstrukturen erlauben es, den Programmfluß zu beinflussen.

```python
x = 10
if x > 5:
    print("x ist größer als 5")
```    

Der Block, welcher nur dann ausgeführt werden soll wenn die Bedingung wahr ist muß zwingend eingerückt werden. 
Der hinter dem if-keyword stehende Bedingung wird ausgewertet und, falls sie wahr ist, der eingerückte Code ausgeführt. Andernfalls setzt das Programm hinter diesem Block fort. 

## Vergleichsoperatoren
```python
a = 5
b = 8
c = 8

a == b # False
b == c # True
a >= b # False
b >= c # True
a > b  # False
b > c  # False
a <= b # True
b <= c # True
a < b  # True
b < c  # False
a != b # True
b != c # False
```

**Achtung**: = und == sind nicht dasselbe. Mit nur einem Gleichheitszeichen handelt es sich um eine Zuweisung. Einer Variable wird also ein neuer Wert zugewiesen. Mit zwei Gleichheitszeichen werden zwei Werte miteinander verglichen.

**Achtung**: Ggf. vorher die Datentypen umwandeln
```python
a = "5"
b = 5
print(a == b) # False
```

## Else und elif

Falls eine Bedingung nicht wahr ist kann im s.g. else: Block angebenen werden was stattdessen ausgeführt werden soll.
```python
x = 10
if x > 5:
    print("x ist größer als 5")
else:
    print("x ist nicht größer als 5")    
```    

Falls sich mehrere Bedingungen hintereinander anschließen können diesem mit elif geschrieben werden.
```python
note = 4
if note == 1:
    print("Sehr gut")
elif note == 2:
    print("Gut")
elif note == 3:
    print("Befriedigend")    
elif note == 4:
    print("Ausreichend")    
elif note == 5:
    print("Mangelhaft")    
elif note == 6:
    print("Ungenügend")    
else:
    print("Ungültige Note!)    
```    

 **Übungsaufgabe**
 Nutze [input](https://www.w3schools.com/python/ref_func_input.asp)() und [float](https://www.w3schools.com/python/ref_func_float.asp) um eine Zahl vom Benutzer abzufragen. Gib dann aus ob diese positiv oder negativ ist. 

Beispielausgabe:

    Welche Zahl soll ich überprüfen? -> 3.7
    3.7 ist positiv

##  Logische Operationen
Mehrere Bedingungen können mit logischen Operatoren verknüpft werden um komplexe Sachverhalte zu prüfen
```python
FSK = 16
alter = 15
mitEltern = True

if alter >= FSK or mitEltern:
  print("Zutritt erlaubt")
```

### 🧠 Aufgabe A: Vergleiche durchführen

Fülle die folgenden Codezeilen aus und überprüfe, ob die Aussagen **`True` oder `False`** ergeben.

```python
a = 5
b = 10

print(a < b)        # → ?
print(a == b)       # → ?
print(b != 5)       # → ?
print(a >= 3)       # → ?
print(a + b < 17)   # → ?
print(4*a > 3*b)    # → ?
print(b-a == a+b)   # → ?
```

### 🔄 Aufgabe B: Kombinierte Bedingungen
Verwende and, or und not, um die folgenden Aussagen zu überprüfen:

```python
x = 7
y = 12

# Ist x größer als 5 UND y kleiner als 15?
print(...)

# Ist x kleiner als 5 ODER y gleich 12?
print(...)

# Ist NICHT wahr, dass x größer als 10 ist?
print(...)

# Ist z negativ UND ungleich 0?
print(...)

# Ist y durch 3 teilbar ODER x eine gerade Zahl?
print(...)

# Ist status NICHT True?
print(...)

# Ist x im Bereich zwischen 5 und 10 (einschließlich)?
print(...)

```

### 🔄 Aufgabe C: Kombinierte Bedingungen
Verwende and, or und not, um die folgenden Aussagen zu überprüfen:

```python
x = 4
y = 9

print(True and False)          # → ?
print(True or False)           # → ?
print(False or False)          # → ?
print(not True)                # → ?
print((3 > 1) and (2 < 5))     # → ?
print((4 == 4) or (7 != 7))    # → ?
print(not (3 <= 3))            # → ?
print(x * 2 == y - 1)          # → ?
print(x + y > 12 and x < 10)   # → ?
print(x < 3 or y < 10)         # → ?
print(not (x == 4 and y == 9)) # → ?
```

## Das Programm vorzeitig beenden
Miit [exit](https://www.w3schools.com/c/ref_stdlib_exit.php)() kann das Programm vorzeitig beendet werden
```python
FSK = 16
alter = 15
mitEltern = True

if alter < FSK and not mitEltern:
  print("Zutritt verboten!")
  exit()

print("""
Die Galaktische Republik wird von Unruhen erschüttert. 
Die Besteuerung der Handelsrouten zu weit entfernten Sternensystemen ist der Auslöser.

In der Hoffnung, die Angelegenheit durch eine Blockade mit mächtigen Kampfschiffen zu beseitigen, hat die unersättliche Handelsföderation jeglichen Transport zu dem kleinen Planeten Naboo eingestellt.
""")
```

