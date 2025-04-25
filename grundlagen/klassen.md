# 🧱 Klassen - Objektorientierte Programmierung in Python


## 🚀 Warum brauchen wir objektorientierte Programmierung?
In einfachen Programmen reicht es oft aus, einzelne Variablen und Funktionen zu verwenden. Doch je größer und komplexer ein Programm wird, desto schwieriger wird es, den Überblick zu behalten:

* Was gehört logisch zusammen?
* Wo werden Daten gespeichert, wie verarbeitet?
* Wie kann ich Code mehrfach verwenden, ohne alles zu kopieren?

Hier kommt objektorientierte Programmierung ins Spiel – ein Konzept, das hilft, komplexe Programme besser zu strukturieren.

## 🧩 Was ist objektorientierte Programmierung?
Objektorientierung bedeutet, dass wir Programme in kleine, eigenständige Bausteine unterteilen: Objekte.

* Ein Objekt ist ein „Ding“ mit Eigenschaften und Fähigkeiten, zum Beispiel:
* Ein Hund hat: einen Namen, ein Alter, ein Gewicht
* Ein Hund kann: bellen(), fressen(), laufen()

In der OOP modellieren wir diese Dinge als Klassen – das sind Baupläne für Objekte.

## 🔑 Zentrale Vorteile von OOP

| Vorteil | Erklärung
| - | -
🔄 Wiederverwendbarkeit | Einmal geschriebene Klassen können für viele Objekte genutzt werden
🧱 Struktur & Ordnung | Programmteile werden logisch gekapselt
🔒 Kapselung | Daten und Methoden sind zusammengefasst – keine globalen Variablen
📈 Erweiterbarkeit | Neue Funktionen lassen sich einfach hinzufügen
👀 Lesbarkeit | Klarere, selbstbeschreibende Programme
🤝 Zusammenarbeit im Team | Jeder arbeitet an eigenen Klassen – weniger Konflikte im Code

## 🔧 Wie sieht objektorientierter Code aus?
```python
class Hund:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def bellen(self):
        print(f"{self.name} bellt!")

hund1 = Hund("Bello", 3)
hund1.bellen()
```

➡️ Hier passiert viel automatisch:

* `__init__()` erzeugt das Objekt
* `self` speichert die Eigenschaften im Objekt
* Methoden (wie bellen()) sind an das Objekt gebunden

 ## 🔹 Objekte erstellen (Instanziierung)
```python
mein_hund = Hund("Bello", 3)
dein_hund = Hund("Luna", 5)

mein_hund.bellen()     # Bello bellt!
print(dein_hund.name)  # Luna
```

## 🔹 Was ist `self`?
`self` verweist immer auf das aktuelle Objekt. Es ist notwendig, um innerhalb der Klasse auf eigene Attribute oder Methoden zuzugreifen.

Muss explizit im Methodenkopf stehen, wird aber beim Aufruf automatisch übergeben

## 🔹 Weitere Methoden hinzufügen
```python
class Hund:
    def __init__(self, name, gewicht):
        self.name = name
        self.gewicht = gewicht

    def wiegen(self):
        print(f"{self.name} wiegt {self.gewicht} kg.")

    def fuettern(self, futtermenge):
        self.gewicht += futtermenge * 0.1
```

## ✨ Dunder-Methoden für Python-Klassen
|Methode | Zweck (automatisch aufgerufen, wenn…)
| - | -
`__init__` | …ein Objekt erstellt wird (obj = Klasse(...))
`__str__` | …print(obj) oder str(obj) verwendet wird
`__repr__` | …das Objekt im Interpreter dargestellt wird
`__len__` | …len(obj) aufgerufen wird
`__eq__` | …zwei Objekte verglichen werden (obj1 == obj2)
`__lt__`, `__gt__`, `__le__`, `__ge__` | …Vergleiche wie <, >, <=, >=
`__add__` | …mit + gerechnet wird (obj1 + obj2)
`__getitem__` | …Zugriff mit obj[index] erfolgt
`__setitem__` | …Eintrag geändert wird obj[index] = wert

## 🧱 Codebeispiel:
```python
class Datum:
    def __init__(self, tag, monat, jahr):
        self.tag = tag
        self.monat = monat
        self.jahr = jahr

    def __repr__(self):
        return f"{self.tag:02d}.{self.monat:02d}.{self.jahr}"

    def __eq__(self, other):
        return (self.tag == other.tag) and (self.monat == other.monat) and (self.jahr == other.jahr)

    def __lt__(self, other):
        if self.jahr < other.jahr:
          return True

        if self.jahr > other.jahr:
          return False

        if self.monat < other.monat:
          return True
        
        if self.monat > other.monat:
          return False

        if self.tag < other.Tag:
          return True

        return False

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

d1 = Datum(1, 1, 2023)
d2 = Datum(15, 3, 2023)
d3 = Datum(1, 1, 2023)

print(d1 == d3)   # → True
print(d1 < d2)    # → True
print(d2 > d1)    # → True
print(sorted([d2, d1, d3]))  # → [01.01.2023, 01.01.2023, 15.03.2023]

```
