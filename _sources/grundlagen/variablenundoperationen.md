# 🧠 Variablen in Python

In Python sind **Variablen** Speicherorte für Daten. Sie ermöglichen es, Werte zwischenzuspeichern, zu verarbeiten und weiterzugeben.

---

## 📝 1. Was ist eine Variable?

Eine Variable ist ein **Name**, der auf einen bestimmten **Wert** zeigt.

```python
name = "Anna"
alter = 25
```
 
## 🔤 2. Wichtige Datentypen

Python erkennt den Typ einer Variable automatisch anhand des Werts. Hier sind die häufigsten:

Datentyp | Beispiel | Beschreibung 
-- | -- | ---
int | 42 | Ganze Zahl 
float | 3.14 | Kommazahl 
str | "Hallo" | Zeichenkette / Text 
bool | True, False | Wahrheitswerte 
list | [1, 2, 3] | Liste von Werten 

**Beispiele:**
```python
x = 10           # int
pi = 3.14        # float
text = "Hi!"     # str
ist_wahr = True  # bool
zahlen = [1, 2, 3]  # list
```

Für längere Texte (Strings) eignet sich die `"""`-Notation:

```python
langerText = """
Dies ist ein langer Text. 
Er kann mehrere Zeilenumbrüche enthalten. Der Text endet erst mit dem nächsten
dreifachen Anführungszeichen. 
"""
```


## ➕ 3. Einfache Operationen mit Variablen
### 🔢 Mit Zahlen (int, float):
```python
a = 5
b = 3

summe = a + b        # 8
differenz = a - b    # 2
produkt = a * b      # 15
quotient = a / b     # 1.666...
ganzzahl = a // b    # 1
potenz = a ** 2      # 25
rest = 17 % 3        # 2
```

### Mit Strings
```python
a = "Hallo"
b = "Welt"

ausgabe = a + " " + b # Hallo Welt
```

### Umwandlung 
```python
a = "5"              # str "5"
pi = 3.14            # float
a = int(a)           # int (5)
b = int(pi)          # int (3)
```

### 📏 Mit Listen (list):
```python
zahlen = [1, 2, 3]
zahlen.append(4)       # [1, 2, 3, 4]
laenge = len(zahlen)   # 4
```

### 🎯 Boolsche Variablen
Boolsche Variablen sind solche, die nur zwei Zustände annehmen können: Wahr oder Falsch. Mit diesen können einfach logische Operationen durchgeführt werden.

```python
x = True
y = False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False
```

### ⚠️ 4. Dynamische Typisierung
Python ist dynamisch typisiert, das heißt: Der Typ einer Variable kann sich ändern.
```python
x = 10      # int
x = "zehn"  # jetzt ist x ein str
```

✅ 5. Namenskonventionen für Variablen
* Keine Leerzeichen, keine Sonderzeichen außer _
* Nicht mit Zahlen beginnen
* Keine reservierten Wörter wie if, class, def als Namen verwenden

### 5. `None` als besonderer Wert
Um anzuzeigen das eine Variable (noch) nicht gesetzt ist bzw. ihr (noch) kein Wert zugewiesen wurde kann das besondere Keyword `None` verwendet werden. 

```python
x = None
```

### 6. 🧠 Tipp: Du kannst mit der Funktion type(variable) jederzeit den Datentyp prüfen:
```python
x = 42
print(type(x))  # <class 'int'>
```

## 🎓 Übungsaufgabe:
### 1. 📌 Begrüßung mit Name
Frage den Benutzer nach seinem Namen und gib eine personalisierte Begrüßung aus.
 Nutze [input](https://www.w3schools.com/python/ref_func_input.asp)() und [print](https://www.w3schools.com/python/ref_func_print.asp)()

Beispielausgabe:

    Wie heißt du? → Maria
    Hallo, Maria!

### 2. 🌡️ Celsius nach Fahrenheit
Frage eine Temperatur in Celsius ab und rechne sie in Fahrenheit um.
Nutze [input](https://www.w3schools.com/python/ref_func_input.asp)() und [float](https://www.w3schools.com/python/ref_func_float.asp).

Formel: F = C * 1.8 + 32    

Beispielausgabe:

    Welche Temperatur soll ich umrechnen (Grad Celsius)? -> 37.5
    37.5°C entspricht 99.5° Fahrenheit