# 🧩 Listen - Mehrere Elemente verwalten
Eine Liste ist eine geordnete Sammlung von Werten. Diese dürfen unterschiedliche Datentypen haben.
Mit Listen kann man mehrere Werte in einer Variablen speichern. Die Reihenfolge der Elemente spielt eine Rolle.

```python
namen = ["Anna", "Ben", "Clara"]
zahlen = [1, 2, 3, 4, 5]
gemischt = ["Hallo", 42, True]
````

## 🔍 Zugriff auf Elemente 
Zugriff per Index (startet bei 0)

```python
namen = ["Anna", "Ben", "Clara"]
print(namen[0])   # Anna
print(namen[-1])  # Clara (von hinten)
namen[1] = "Benny"
```

## Eine Liste mit Bubble-Sort sortieren

**Bubble Sort** ist ein einfacher Sortieralgorithmus, der Listen schrittweise sortiert, indem er **benachbarte Elemente vergleicht und vertauscht**, falls sie in der falschen Reihenfolge stehen.

> 💡 Der Name „Bubble“ kommt daher, dass größere Werte beim Sortieren **wie Luftblasen nach oben steigen** (ans Ende der Liste).


### 🧠 Funktionsprinzip

- Der Algorithmus durchläuft die Liste **mehrfach von vorn bis hinten**.
- Bei jedem Durchlauf vergleicht er **jeweils zwei benachbarte Elemente**:
  - Wenn sie in der falschen Reihenfolge sind, werden sie vertauscht.
- Der größte Wert „wandert“ dabei ans Ende – deshalb kann man nach jedem Durchlauf **einen Vergleich weniger** machen.
- Der Vorgang wird wiederholt, **bis keine Vertauschungen mehr nötig sind**.

### 🔢 Beispiel

Gegeben: `[5, 2, 4, 1]`

1. **Erster Durchlauf**:
   - 5 und 2 → vertauschen → `[2, 5, 4, 1]`
   - 5 und 4 → vertauschen → `[2, 4, 5, 1]`
   - 5 und 1 → vertauschen → `[2, 4, 1, 5]`

2. **Zweiter Durchlauf**:
   - 2 und 4 → ok
   - 4 und 1 → vertauschen → `[2, 1, 4, 5]`

3. **Dritter Durchlauf**:
   - 2 und 1 → vertauschen → `[1, 2, 4, 5]`

4. **Fertig** – die Liste ist sortiert.

### 🧪 Übungsaufgabe:
Implementieren Sie Bubble-Sort mit der Liste `[6,3,5,2,4,1]`

<details>
<summary>Lösung anzeigen</summary>

```python
#sortieren mit Bubble-Sort
daten = [6,3,5,2,4,1]
anzahl = len(daten)
for j in range(0,anzahl):
    for i in range(0,anzahl-1):
        if daten[i] > daten[i+1]:
            h = daten[i]
            daten[i] = daten[i+1]
            daten[i+1] = h
```

</details>


## 🛠️ Arbeiten mit Listen

```python
liste.append("Neues Element")   # hinzufügen
liste.remove("Wert")            # löschen (ersten Treffer)
liste.insert(1, "Wert")         # an bestimmter Position einfügen
liste.sort()                    # sortieren
liste.reverse()                 # umdrehen
liste.index("Element")          # Liefert den (ersten) Index, an dem "Element" steht
liste.count("Element")          # Zählt, wie oft "Element" in der Liste vorkommt
len(liste)                      # liefert Anzahl Elemente in der Liste
"x" in liste                    # True, falls "x" in der Liste ist
```

## 🔢 `sum()` – Summe berechnen
```python
zahlen = [4, 7, 10]
print(sum(zahlen))  # → 21
```
➡️ Addiert alle Elemente in der Liste

### ➕ Mit Startwert:
```python
print(sum(zahlen, 100))  # → 121
```

## 📉 `min()` – Kleinster Wert
```python
temperaturen = [18.2, 16.5, 19.0, 14.8]
print(min(temperaturen))  # → 14.8
```

➡️ Gibt den kleinsten Wert in der Liste zurück

## 📈 `max()` – Größter Wert
```python
punkte = [10, 30, 25, 40]
print(max(punkte))  # → 40
```

➡️ Gibt den größten Wert in der Liste zurück

## 🧑‍🏆 Größter Eintrag nach Länge eines Namens:
```python
namen = ["Anna", "Beate", "Christoph"]
print(max(namen, key=len))  # → Christoph
```

## 💡 Kombiniert mit `sum()` – Durchschnitt berechnen
```python
zahlen = [3, 4, 5, 6]
durchschnitt = sum(zahlen) / len(zahlen)
print(durchschnitt)  # → 4.5
```

## 🔁 Über Listen iterieren

```python
namen = ["Anna", "Ben", "Clara"]
for name in namen:
    print("Hallo,", name)

for name in reversed(namen):
    print("Hallo,", name)
```

## 💡 List-Comprehension
Python erlaubt s.g. List-Comprehension, damit lassen sich Listen sehr ähnlich zur mathematischen Schreibweise definieren. 

🧱 Syntax:
```python
[ausdruck for element in iterable if bedingung]
```

**Beispiel 1:** Quadrate von Primzahlen

Es sei $$A = \{2, 3, 5, 7, 11, 13, 17\}$$ und $$B = \{ x^2 | x \in A \}$$
```python
A = [2, 3, 5, 7, 11, 13, 17]
B = [x**2 for x in primzahlen]
print(B)

[4, 9, 25, 49, 121, 169, 289]
```

**Beispiel 2:** Begruessung bestimmter Namen
```python
A = ["Anna", "Beate", "Carla", "Denise", "Erika", "Frauke"]
B = ["Hallo " + name for name in A if len(name) <= 4]
print(B)

["Hallo Anna"]
```

**Beispiel 3:** Länge von Wörtern
```python
woerter = ["Hallo", "Python", "Welt"]
laengen = [len(w) for w in woerter]
print(laengen)
```

## Verschachtelte List-Comprehension
```python
tabelle = [[i * j for j in range(1, 6)] for i in range(1, 6)]
for zeile in tabelle:
    print(zeile)

[1, 2, 3, 4, 5]
[2, 4, 6, 8, 10]
[3, 6, 9, 12, 15]
[4, 8, 12, 16, 20]
[5, 10, 15, 20, 25]
```

## ✂️ List Slicing
Mit Slicing kann man Teile einer Liste herausnehmen – ganz ohne Schleifen. Man verwendet dazu eine spezielle Syntax mit Doppelpunkten:
```python
liste[start:stop:step]
```

| Ausdruck | Bedeutung
| - | -
| liste[:] | komplette Kopie der Liste
| liste[2:5] | Elemente von Index 2 bis 4 (5 ist exklusiv)
| liste[:3] | Elemente von Anfang bis Index 2
| liste[4:] | Elemente ab Index 4 bis zum Ende
| liste[::2] | jedes zweite Element
| liste[::-1] | Liste rückwärts

**📦 Beispiele**:

```python
zahlen = [10, 20, 30, 40, 50, 60, 70]
```

| Slice | Ergebnis | Erklärung
| - | - | -
| zahlen[1:4] | [20, 30, 40] | von Index 1 bis 3
| zahlen[:3] | [10, 20, 30] | Anfang bis Index 2
| zahlen[3:] | [40, 50, 60, 70] | ab Index 3 bis Ende
| zahlen[::2] | [10, 30, 50, 70] | jedes zweite Element
| zahlen[::-1] | [70, 60, 50, 40, 30, 20, 10] | umgedreht

## 🧪 Übungsaufgaben
```python
obst = ["Apfel", "Banane", "Kirsche", "Melone", "Birne"]
```

* Gib nur die ersten 3 Früchte aus
* Gib die letzten 2 Früchte aus
* Gib die Liste rückwärts aus
* Überprüfe ob "Tomate" in der Liste ist

## 🎓 Mini-Projekt
Schreibe ein kleines Programm welches den Nutzer verschiedene Zahlen eingeben läßt. Füge solange die eingegebenen Zahlen einer Liste hinzu bis der Benutzer "fertig" eingibt. Sobald der Benutzer fertig ist berechne den **Median** der Liste. Dazu musst Du die Liste zunächst sortieren und dann das mittlere Element herausgreifen. Wenn die Anzahl der Elemente gerade ist musst Du die beiden Elemente links und rechts der Mitte nehmen, addieren und durch zwei teilen. 

[Lösung](mediansolution.md)
<!--- ```python
elemente = []
while True:
  zahl = input("Nächste Zahl bitte:")
  if zahl == "fertig":
    break
  elemente.append(int(zahl))

elemente.sort()
print(elemente)

anzahl = len(elemente)
if anzahl % 2 == 1:
  print(f"Der Median ist {elemente[anzahl//2]}")
else:
  a = elemente[anzahl//2-1]
  b = elemente[anzahl//2]
  print(f"Der Median ist {(a+b)/2}")
``` --->