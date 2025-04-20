# 📝 Strings in Python – Zeichenketten meistern

Ein String ist eine Folge von Zeichen. In Python wird ein String in Anführungszeichen geschrieben:

```python
text = "Hallo Welt"
```

| Methode | Bedeutung | Beispiel
| - | - | -
lower() | Alles in Kleinbuchstaben | "Python".lower() → 'python'
upper() | Alles in Großbuchstaben | "abc".upper() → 'ABC'
strip() | Entfernt Leerzeichen am Anfang/Ende | "  Hallo  ".strip() → 'Hallo'
replace(a, b) | Ersetzt Teilstrings | "Apfel".replace("A", "B") → 'Bpfel'
split(sep) | Zerlegt String in Liste | "a,b,c".split(",") → ['a', 'b', 'c']
join(list) | Verbindet Liste zu String | ",".join(["a", "b", "c"]) → 'a,b,c'
find(sub) | Gibt Index des ersten Vorkommens zurück | "Test".find("s") → 2
startswith(s) | Prüft, ob der String mit s beginnt | "Hallo".startswith("H") → True
endswith(s) | Prüft, ob der String mit s endet | "Test.py".endswith(".py") → True
isdigit() | Prüft, ob nur Ziffern enthalten sind | "123".isdigit() → True
count() | Zählt, wie ohne ein Teilstring in dem String vorkommt | "Hallo Wellt".count("ll") → 2

## 🔢 Zugriff auf einzelne Zeichen & Slicing

```python
text = "Python"
print(text[0])      # 'P'
print(text[-1])     # 'n'
print(text[1:4])    # 'yth'
```

## 🧪 Typische Anwendungsbeispiele
### 📌 Groß-/Kleinschreibung normalisieren:
```python
eingabe = input("Name: ").strip().lower()
``` 

### 📌 Worte zählen:
```python
satz = "Das ist ein Test"
anzahl = len(satz.split())
```

### 📌 Zeichen ersetzen:
```python
text = "Python ist toll!"
text = text.replace("toll", "super")
```

## 🎓 Übungsaufgabe: Textanalyse "Mini-Statistik"
Schreibe ein Programm, das vom Benutzer einen beliebigen Text einliest (mehrere Sätze) und dann folgende Informationen berechnet:

* Gesamtanzahl der Zeichen (inkl. Leerzeichen)
* Anzahl der Wörter
* Anzahl der Vokale (a, e, i, o, u)
* Wie oft ein bestimmtes Wort vorkommt (Benutzer wählt Wort)
* Gib die Eingabe rückwärts aus (komplett gespiegelt)
