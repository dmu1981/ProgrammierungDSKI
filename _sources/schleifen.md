# 🔁 Schleifen – Wiederholungen meistern
Schleifen erlauben es bestimmte Code-Abschnitte kontrolliert zu wiederholen. 

## `for`-Schleife
Die s.g. `for`-Schleife *iteriert* über Elemente einer Liste (oder eines Generators, dazu später mehr). Eine s.g. *Schleifenvariable* nimmt dabei in jedem Durchlauf das aktuelle Element der Liste an. Dann wird der *Schleifenkörper* ausgeführt. 

In diesem Beispiel benutzen wir [range](https://www.w3schools.com/python/ref_func_range.asp)() um einen solchen Generator zu erzeugen. 
```python
for i in range(5):
    print("Durchlauf:", i)
```

Die [range](https://www.w3schools.com/python/ref_func_range.asp)()-Funktion kann parameterisiert werden um zu kontrollieren welche Elemente ausgegeben werden:

```python
for i in range(3,9):
    print(i) # 3, 4, 5, 6, 7, 8

for i in range(3,9,2):
    print(i) # 3, 5, 7

for i in range(9,3,-1):
    print(i) # 9, 8, 7, 6, 5, 4
```

## 🧪 Übungsaufgabe:
Gib alle gerade Zahlen zwischen 2 und 20 (inklusive) aus.

## Über einen String iterieren
```python
name = "Dennis"
for buchstabe in name:
    print(buchstabe)
```

## `while`-Schleife - Wiederhole solange eine Bedingung `True` ist

```python
x = 0
while x < 5:
    print(x)
    x += 1
```    

## 🧪 Übungsaufgabe:
Frage den Benutzer nach seinem Passwort. Wiederhole die Frage solange bis er das korrekte Passwort eingibt. 

## 🧪 Übungsaufgabe:
Frage den Benutzer nach einer natürlichen Zahl. Gib die Summe aller natürlichen Zahlen von 1 bis zur gegebenen Zahl aus. 

## `break` und `continue`.
Mit dem `break`-Keyword kann die Schleife vorzeitig verlassen werden. 

```python
for x in range(10):
    print(f"{x} hoch 2 ist {x**2}")
    if x ** 2 >= 36:
      break
```    

Mit dem `continue`-Keyword kann der aktuellen Schleifendurchlauf abgebrochen und mit dem nächsten Element fortgeführt werden. 

```python
for zahl in range(1, 11):
    if zahl % 2 == 0:
        continue  # gerade Zahl? überspringen!
    print(zahl)
```    

## Verschachtelte Schleifen
Schleifen können verschachtelt werden. Das `break` und `continue`-Keyword bezieht sich stets nur auf den aktuellen Schleifenkörper.
```python
for zahl in range(2, 100):
  istPrim = True
  
  for teiler in range(2, zahl):
    if zahl % teiler == 0:
      istPrim = False
      break

  if istPrim:
    print(f"{zahl} ist prim!")
```
## 🧪 Mini-Projekt - Benutzerverwaltung:
Zur Anmeldung an einem Terminal müssen Nutzer sich mit Benutzername und Passwort registrieren. Es gibt aktuell drei Benutzer mit Namen "Anna", "Beate" und "Clara". Ihre jeweiligen Passwörter lauten "Aquamarin", "Beige" und "Cyan". Erstelle ein kleines Projekt wo Du zuerst nach dem Benutzernamen fragst. Stelle sicher das sich nur die drei bekannten Nutzer anmelden können. Brich das Program ab wenn sich andere Nutzer anmelden möchten. Ein bekannter Benutzer muß sich mit dem korrekten Passwort anmelden. Erlaube maximal drei Fehlversuche bei der Eingabe des Passwortes. Brich das Programm ab wenn ein bekannter Benutzer sein Passwort zum dritten mal falsch eingibt. 

