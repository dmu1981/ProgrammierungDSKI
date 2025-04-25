# 📂 Arbeiten mit CSV- und JSON-Dateien in Python
## 🔍 CSV vs. JSON – Was ist was?
| Format | Beschreibung | Typisches Einsatzgebiet
| - | - | -
CSV | „Comma-Separated Values“, tabellenartig | Tabellen, Excel-Export, Messdaten
JSON | „JavaScript Object Notation“, strukturiert | APIs, Konfigurationsdaten, Objekte

## 🟨 Teil 1: CSV-Dateien lesen & schreiben
### 📄 Beispiel-Datei: personen.csv
```python
Name,Alter,Stadt
Anna,25,Berlin
Ben,30,Hamburg
Clara,22,München
```

### ✅ Lesen mit csv.reader
```python
import csv

with open("personen.csv", newline="") as f:
    reader = csv.reader(f)
    for zeile in reader:
        print(zeile)
```

➡️ Ausgabe:
```python
['Name', 'Alter', 'Stadt']
['Anna', '25', 'Berlin']
['Ben', '30', 'Hamburg']
['Clara', '22', 'München']
```

### ✅ Lesen mit csv.DictReader (Spalten als Schlüssel)
```python
with open("personen.csv", newline="") as f:
    reader = csv.DictReader(f)
    for person in reader:
        print(person["Name"], person["Stadt"])
```

### 📝 Schreiben mit csv.writer
```python
daten = [["Name", "Alter"], ["Eva", 29], ["Max", 35]]

with open("neue_personen.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(daten)
```

## 🟦 Teil 2: JSON-Dateien lesen & schreiben
### 📄 Beispiel-Datei: personen.json
```json
[
    {"name": "Anna", "alter": 25, "stadt": "Berlin"},
    {"name": "Ben", "alter": 30, "stadt": "Hamburg"}
]
```

## ✅ Einlesen mit json.load
```python
import json

with open("personen.json", "r") as f:
    daten = json.load(f)

for person in daten:
    print(person["name"], person["stadt"])
```

## 📝 Schreiben mit json.dump
```python
personen = [
    {"name": "Lena", "alter": 28},
    {"name": "Paul", "alter": 34}
]

with open("personen_neu.json", "w") as f:
    json.dump(personen, f, indent=2)
```

### ➕ Von String nach JSON (und zurück)
```python
# String → Python-Datenstruktur
json_str = '{"name": "Anna", "alter": 25}'
daten = json.loads(json_str)

# Python-Datenstruktur → String
neuer_str = json.dumps(daten, indent=2)
```

## 🎓 Mini-Projekt: Analyse von Umfragedaten aus einer CSV-Datei
Analysieren Sie Umfrageergebnisse aus einer .CSV Datei. 
Ziel ist es, einfache statistische Auswertungen durchzuführen und die Daten sinnvoll zu interpretieren.

### 📁 Beispielhafte Datei: umfrage.csv
```css
Name,Alter,Studiengang,Schlafstunden,Stresslevel,Bildschirmzeit
Anna,22,Informatik,6,4,7.5
Ben,23,BWL,7,2,6.0
Clara,21,Informatik,5,5,8.0
David,24,Psychologie,6,3,5.5
Ella,20,Informatik,8,1,4.0
```

### 🧠 Ziele des Projekts
* CSV-Datei einlesen mit csv.DictReader
* Umwandlung von Werten in passende Datentypen (z. B. int, float)
* Einfache Berechnungen (Durchschnitt, Maximalwerte, Filterungen)
* Zählen, Filtern und Gruppieren nach Kriterien (Studiengang, Stresslevel…)

### 🔧 Aufgabenstellung:
* Datei einlesen und alle Zeilen als Dictionary verarbeiten
* Berechne den Durchschnitt der Schlafstunden aller Teilnehmenden
* Finde die Person mit der höchsten Bildschirmzeit
* Zähle, wie viele Personen aus dem Fach Informatik kommen
* Filtere alle, deren Stresslevel größer als 3 ist
* Berechne den Durchschnitt der Bildschirmzeit pro Studiengang

[Lösung](umfragesolution.md)