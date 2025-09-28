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
* Gib alle gerade Zahlen zwischen 2 und 20 (inklusive) aus.

## 🧪 Übungsaufgabe:
Gib alle Zahlen zwischen 1 und 100 aus welche beide der folgenden Bedinungen erfüllt.

* Der Rest bei Division durch 7 ist kleiner als 3
* Der Rest bei Division durch 13 ist größer als 10

<details>
<summary>Lösung anzeigen</summary>

```python
for i in range(1,100):
    if (i % 7 < 3) and (i % 13 > 10):
        print(i)

37
50
51
63
64
77        
```

</details>



## Über einen String iterieren
```python
name = "Dennis"
for buchstabe in name:
    print(buchstabe)
```

## 🧪 Übungsaufgabe:
Fordere den Benutzer auf einen Text einzugeben. 
Iteriere dann über jeden Buchstaben des Textes und
gib ihn aus falls er doppelt vorkommt (sein Vorgänger also identisch ist zu diesem)

<details>
<summary>Lösung anzeigen</summary>

```python
text = input("Geben Sie einen Text ein: ")
vorgaenger = None
for buchstabe in text:
    if buchstabe == vorgaenger:
        print(buchstabe)
    
    vorgaenger = buchstabe       
```

</details>

## 🧪 Übungsaufgabe:
Frage den Benutzer nach einer natürlichen Zahl. Gib die Summe aller natürlichen Zahlen von 1 bis zur gegebenen Zahl aus. 

<details>
<summary>Lösung anzeigen</summary>

```python
zahl = int(input("Geben Sie eine Zahl ein"))

summe = 0
for i in range(zahl):
    summe += i

print(f"Die Summe von 1 bis {zahl} lautet {summe}")
```

</details>

## `while`-Schleife - Wiederhole solange eine Bedingung `True` ist

```python
x = 0
while x < 5:
    print(x)
    x += 1
```    

## 🧪 Übungsaufgabe:
Frage den Benutzer nach seinem Passwort. Wiederhole die Frage solange bis er das korrekte Passwort eingibt. 


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

## 🧪 Übungsaufgabe:
Iteriere über jeden Buchstaben eines Textes. 
Gib jeden Buchstaben aus der kein Vokal ist. 

<details>
<summary>Lösung anzeigen</summary>

```python
text = "Hallo Welt"
for buchstabe in text:
    if buchstabe == 'a' or buchstabe == 'A':
        continue
    if buchstabe == 'e' or buchstabe == 'E':
        continue
    if buchstabe == 'i' or buchstabe == 'I':
        continue
    if buchstabe == 'o' or buchstabe == 'O':
        continue
    if buchstabe == 'u' or buchstabe == 'U':
        continue
    print(buchstabe)
```

</details>


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
## 🎓 Mini-Projekt - Benutzerverwaltung:
Zur Anmeldung an einem Terminal müssen Nutzer sich mit Benutzername und Passwort registrieren. Es gibt aktuell drei Benutzer mit Namen "Anna", "Beate" und "Clara". Ihre jeweiligen Passwörter lauten "Aquamarin", "Beige" und "Cyan". Erstelle ein kleines Projekt wo Du zuerst nach dem Benutzernamen fragst. Stelle sicher das sich nur die drei bekannten Nutzer anmelden können. Brich das Program ab wenn sich andere Nutzer anmelden möchten. Ein bekannter Benutzer muß sich mit dem korrekten Passwort anmelden. Erlaube maximal drei Fehlversuche bei der Eingabe des Passwortes. Brich das Programm ab wenn ein bekannter Benutzer sein Passwort zum dritten mal falsch eingibt. 

[Lösung](benutzerverwaltungsolution.md)