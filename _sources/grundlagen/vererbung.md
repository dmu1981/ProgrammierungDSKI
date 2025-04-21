# 🧬 Vererbung in Python – Gemeinsamkeiten wiederverwenden

## 🧠 Einführung & Motivation
### 🤔 Warum Vererbung?
Stell dir vor, du hast eine Klasse Tier, und möchtest viele spezifische Tierarten modellieren (Hund, Katze, Vogel…), ohne den gleichen Code immer wieder zu schreiben.

Vererbung bedeutet:

„Etwas ist eine Spezialisierung von etwas anderem.“

### 🧩 Hund ist ein Tier, Katze ist ein Tier
→ Sie erben alles von Tier, können aber auch eigene Fähigkeiten haben.

## 🧱 Grundlagen der Vererbung
### 🔧 Syntax:
```python
class Unterklasse(Oberklasse):
    ...
```

### 🐾 Beispiel: Basisklasse Tier
```python
class Tier:
    def __init__(self, name):
        self.name = name
    def beschreibung(self):
        print(f"Ich bin ein Tier und heiße {self.name}.")
``` 

### 🐶 Unterklasse Hund
```python
class Hund(Tier):
    def gibLaut(self):
        print(f"{self.name} bellt: Wuff!")
```

### 📌 Verwendung:
```python
bello = Hund("Bello")
bello.beschreibung()  # Von Tier geerbt
bello.gibLaut()        # Eigene Methode
```

➡️ Hund erbt beschreibung() von Tier, hat aber auch eigene Methode bellen().

## 🔄 Methoden überschreiben (Overriding)
```python
class Katze(Tier):
    def beschreibung(self):
        print(f"Ich bin eine Katze und heiße {self.name}.")

    def gibLaut(self):
        print(f"{self.name} miaut: Miao!")
```        

## 🪜 super() – Zugriff auf die Oberklasse
Mit super() kannst du die Oberklassenmethoden gezielt aufrufen:

```python
class Papagei(Tier):
    def __init__(self, name, spruch):
        super().__init__(name)  # ruft Tier.__init__ auf
        self.spruch = spruch
    def sprechen(self):
        print(f"{self.name} sagt: '{self.spruch}'")
```

## `isinstance` - Überprüfen ob ein Objekt eine bestimmten Klasse ist
```python
papagei = Papagei("Polly", "Polly will einen Keks")
isinstance(papagei, Papagei)  # True
isinstance(papagei, Tier)     # True
isinstance(papagei, Hund)     # False
```

## 🎓 Mini-Projekt: Gefängnissverwaltung
In einem Gefängniss gibt es verschiedene Zellentypen. Es gibt Einzelzellen mit genau einem Bett, Paarzellen mit genau zwei Betten und Gemeinschaftszellen mit einer Variablen Anzahl Betten zwischen 4 und 8. Jede Zelle hat genau

Darüberhinaus gibt es Wachen und Insassen im Gefängniss. Jeder hat einen Namen aber nur Insassen haben eine Straftat während Wachen eine Personalnummer ha#ben. 

Schreibe eine Klasse `Zelle` welche die Insassen verwaltet. 

Eine Zelle hat eine Methode `inhaftieren()` welche einen Insassen entgegennimmt und diesen in die Zelle sperrt. Dies ist jedoch nur möglich wenn die Zelle noch nicht voll ist. Ausserdem kann kein Personal inhaftiert werden. 

Eine Zelle hat auch eine Methode `wachwechsel()`, welche eine Wache entgegennimmt und sich merkt. Stelle sicher das es wirklich eine Wache ist und kein Insasse. 

Eine Zelle hat zusätzlich eine Methode `belegung()` welche die Namen und Strafttaten aller Insassen ausgibt, ausserdem die aktuell zuständige Wache inklusive ihrer Personalnummer. Leite entsprechende Kindklasse `Einzelzelle`, `Paarzelle`und `Gemeinschaftszelle` ab. 

Schreibe eine weitere Klasse `Person` welche den Namen der Person verwaltet. Leite davon die Klasse `Insasse` sowie `Wache` ab. Überschreibe die `__str__` Methoden um sinnvolle Beschreibungen der Personen zu erhalten. 

[Lösung](prisonsolution.md)
