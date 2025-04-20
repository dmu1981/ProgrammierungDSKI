# 🔷 Sets in Python – Mengen ohne Duplikate
Ein Set (Menge) ist eine **ungeordnete Sammlung einzigartiger** Elemente – also keine Duplikate erlaubt!

Sets können direkt erstellt werden (geschweifte statt eckige Klammern):
```python
farben = {"rot", "grün", "blau"}
```

Vorhandene Listen können mit dem [Set-Konstruktur](https://www.w3schools.com/python/python_sets.asp) erzeugt werden
```python
farben = set(["rot", "grün", "grün", "blau"])
print(farben)  # → {'rot', 'grün', 'blau'}
```

## 🔧 Wichtige Set-Operationen
| Operation | Beispiel | Ergebnis / Wirkung
 | - | - | - 
Hinzufügen | s.add("neu") | Element wird eingefügt (falls nicht da)
Entfernen | s.remove("rot") | Element wird gelöscht
Sicheres Entfernen | s.discard("rot") | Kein Fehler, falls Element nicht da
Anzahl Elemente | len(s) | Anzahl der einzigartigen Elemente
Duplikate entfernen | set(liste) | Liste → Set (ohne Duplikate)

🔁 Sets iterieren
Sets können genau wie Listen iteriert werden
```python
farben = set(["rot", "grün", "grün", "blau"])
for farbe in farben:
    print(f"{farbe} ist eine schöne Farbe")
```    

🔀 Mengenoperationen

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a & b) # Schnittmenge {3}
print(a | b) # Vereinigungsmenge {1, 2, 3, 4, 5}
print(a - b) # Differenzmenge {1, 2}
print(a ^ b) # Symmetrische Differenz {1, 2, 4, 5}
```

## 🎓 Mini-Projekt

Programmiere ein einfaches "Ich packe meinen Koffer" Spiel. 
Frage den Spieler in einer Endloßschleife nach den Gegenständen, die er in seinen Koffer packen möchte. Der Einfachheithalber soll der Spieler eine mit Kommas separierte Liste eingeben. 

Zu Beginn ist der Koffer leer, du kannst ein leeres Set mit 
```python
koffer = set()
```
erzeugen. 

Beachte die Regeln des Spiels: Der Spieler muß in jeder Runde alle Gegenstände auflisten die bereits im Koffer sind sowie **genau** einen neuen benennen. Wenn der Spieler einen Gegenstand vergisst bzw. keinen neuen hinzufügt oder mehrere neue auf einmal hinzufügt ist das Spiel beendet. Verwende Mengenoperationen um zu entscheiden ob diese Bedingungen erfüllt wurden. 

💡 Tipps: Du kannst die [split](https://www.w3schools.com/jsref/jsref_split.asp)() Funktion benutzen um den eingegebenen String nach jedem Komma in eine Liste zu splitten. Ausserdem kannst Du die [strip](https://www.w3schools.com/python/ref_string_strip.asp)() Funktion benutzen um überflüssige Leerzeichen am Anfang und am Ende eines jeden Wortes zu entfernen. 

[Lösung](koffersolution.md)

<!---
```python
koffer =  set()
while True:
  # Alle Items abfragen
  item = input("Ich packe meinen Koffer und nehme mit: ")

  # Am "," splitten
  items = item.split(",")
  items = [item.strip() for item in items]
  
  # Doppelte entfernen
  items = set(items)

  # Wurde etwas vergessen?
  vergessen = koffer - items
  if len(vergessen) > 0:
    print("Du hast", vergessen, "vergessen")
    exit()

  # Wurde mehr als ein neuer Gegenstand hingezufügt?
  neue = items - koffer
  if len(neue) != 1:
    print("Du musst genau einen neuen Gegenstand hinzufügen.")
    exit()

  koffer = koffer | items
```--->