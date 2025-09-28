# 🧠 Variablen in Python

In Python sind **Variablen** Speicherorte für Daten. Sie ermöglichen es, Werte zwischenzuspeichern, zu verarbeiten und weiterzugeben.

---

## 📝 1. Was ist eine Variable?

Eine Variable ist ein **Name**, der auf einen bestimmten **Wert** zeigt.

```python
name = "Anna"
alter = 25
```

Variablen speichern ihre Werte und belegen Speicherplatz im Computer.
Python wählt eine geeignete interne Repräsentation um diese Werte zu speichern. Der Wert einer Variable kann überschrieben werden

```python
alter = 25
alter = 27
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
x = 10           # integer (Ganzzahl)
pi = 3.14        # float (Gleitkommazahl)
text = "Hi!"     # str (Zeichenkette)
ist_wahr = True  # bool (Boolsche Variable)
zahlen = [1, 2, 3]  # list (Liste)
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

### Direkte Rückzuweisung (Kurzformen)
```python
a = 5
a += 3 # 8
a *= 2 # 16
a /= 4 # 4
```

## 🔁 Übung: Kurzformen und ausführliche Zuweisungen

### 🧠 Aufgabe A: Kürzen

Schreibe die folgenden Zuweisungen als **Kurzform**:

```python
a = a + 5
b = b * 2
c = c - 1
d = d / 4
e = e % 3
```

### 🧠 Aufgabe B: Ausschreiben

Schreibe die folgenden Zuweisungen als **Kurzform**:

```python
x += 7
y //= 2
z **= 3
n -= 4
k *= 10
```

### 🧠 Quiz: Welchen Wert haben x und y nach diesen Operationen?

```python
x = 2                   
y = 5
x = (2*x - y) + 1
y = (2*y - x) - 1
x += y
y -= x  
```
<details>
<summary>Klicke hier, um die Lösung anzuzeigen</summary>

```python
x = 2                   # x=2
y = 5                   # x=2, y=5
x = (2*x - y) + 1       # x=0, y=5
y = (2*y - x) - 1       # x=0, y=9
x += y                  # x=9, y=9
y -= x                  # x=9, y=0
```
</details>

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
a = int(a)           # 5 (integer)
b = int(pi)          # 3 (integer)
c = float("3.14")    # 3.14 (float)
```

⚠️ Achtung: Die Umwandlung von beliebigen Strings in Zahlendatentypen kann scheitern:

```python
a = "fünf"            
a = int(a)           # int (5)
    # Traceback (most recent call last):
    # File "<stdin>", line 1, in <module>
    # valueError: invalid literal for int() with base 10: 'fünf'
```

### 🧠 Übung: Umwandlung von Datentypen
Fordern Sie den Benutzer auf eine beliebige Gleitkommazahl einzugeben 
(verwenden Sie [input](https://www.w3schools.com/python/ref_func_input.asp)). Wandeln Sie die Zahl zunächst in eine Gleitkommazahl um. 

Überlegen Sie dann wie sie die Zahl runden können und geben Sie das gerundete Ergebniss aus. 

<details>
<summary>Klicke hier, um die Lösung anzuzeigen</summary>

```python
x = float(input("Geben Sie eine Gleitkommazahl ein"))
print(int(x + 0.5))
```
</details>


## 🔢 Ungenauigkeiten bei Gleitkommazahlen (`float`)

Python (wie viele andere Programmiersprachen) verwendet zur Darstellung von Dezimalzahlen den **Binär-Gleitkomma-Standard (IEEE 754)**. Dabei können **kleine Rundungsfehler** entstehen, da **nicht alle Dezimalzahlen exakt binär darstellbar sind**.

### Beispiel

```python
a = 0.1
b = 0.2
c = a + b

print("Ergebnis von 0.1 + 0.2:", c)
print("Ist das Ergebnis genau 0.3?", c == 0.3)
```

### 🔢 Andere Basen
Wir stellen Zahlen im s.g. Zehnersystem da, d.h. wir verwenden Ziffern von 0 bis 9 und ein Stellenwertsystem welches mit jeder Stelle um den Faktor 10 wächst. Konkret:

$$ 372 = 3 * 100 + 7 * 10 + 2$$

Das Binärsystem verwendet nur die Ziffern 0 und 1 und jede Stelle verdoppelt sich im Wert. Konkret:

$$101101 = 1 * 32 + 0 * 16 + 1 * 8 + 1 * 4 + 0 * 2 + 1 = 45$$

Python kann diese Basenumrechnung für uns machen:

```python
    # Dezimal nach Binär:
    print(bin(45))
    # 0b101101

    # Binär nach Dezimal:
    print(int("101101",2))
    45
```

Neben dem Binärsystem findet das s.g. Hexadezimalsystem oft Verwendung in Computeranwendung. Dabei verwenden wir 16 Ziffern (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F). 

$$ 0xAE = 10 * 16 + 14 = 174$$

```python
    # Dezimal nach Hexadezimal:
    print(hex(108))
    # 0x6c

    # Hexadezimal nach Dezimal:
    print(int("6c",16))
    108
```

## Formatierungsmöglichkeiten mit f-Strings

| Typ              | Beispiel           | Ausgabe       |
| ---------------- | ------------------ | ------------- |
| Ganzzahl         | `f"{42}"`          | `42`          |
| Float            | `f"{3.14159:.2f}"` | `3.14`        |
| Ausrichtung      | `f"{'Text':>10}"`  | `'     Text'` |
| Wissenschaftlich | `f"{12345:.2e}"`   | `1.23e+04`    |
| Prozent          | `f"{0.75:.0%}"`    | `75%`         |
| Boolesch         | `f"{True}"`        | `True`        |
| Ausdruck         | `f"{2 + 3}"`       | `5`           |


## 🧪 Übung: Formatierte Strings mit verschiedenen Datentypen

Du lernst, wie du mit **f-Strings (`f""`)** in Python verschiedene Datentypen **formatiert und leserlich** darstellen kannst. Dazu gehören:

- Ganzzahlen (`int`)
- Kommazahlen (`float`)
- Strings
- Wahrheitswerte (`bool`)
- Runden, Ausrichten und Padding

---

### 🔢 Aufgabe A: Werte definieren und einsetzen

1. Definiere folgende Variablen:

```python
name = "Lena"
alter = 27
größe = 1.6754
ist_studentin = True
```

Gib folgenden Satz mittels eines f-Strings aus:

        Name: Lena | Alter: 27 | Größe: 1.68 m | Studentin: Ja



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