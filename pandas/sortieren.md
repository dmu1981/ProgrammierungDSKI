# 🐼  Sortieren, Filtern & Kombinieren von DataFrames

## 🔁 Sortieren mit sort_values()
```python
df.sort_values("Alter")
```
➡️ Sortiert aufsteigend nach einer Spalte

```python
df.sort_values("Note", ascending=False)
```
➡️ Sortiert absteigend

### 🔹 Nach mehreren Spalten sortieren:
```python
df.sort_values(["Studiengang", "Note"])
```

## 🔍 Logische Filter & Kombinationen

### 🔸 Einfache Filter:
```python
df[df["Note"] < 2.0]
```

### 🔸 Mehrere Bedingungen kombinieren:
```python
df[(df["Note"] < 2.0) & (df["Studiengang"] == "Informatik")]
```

Wichtig: Immer Klammern um jede Bedingung und & statt and, | statt or

## 🔗 Kombinieren von DataFrames
### 🔸 Methode 1: `pd.concat()`
Zum aneinanderhängen von Tabellen (wie Zeilen kopieren)

```python
df_neu = pd.concat([df1, df2])
```
* Option `axis=0` (Standard): Zeilen anhängen
* Option `axis=1`: Spalten nebeneinanderstellen

### 🔸 Methode 2: `pd.merge()`
Zum Verknüpfen von Tabellen nach Spalte, ähnlich wie JOIN in SQL

```python
df_gesamt = pd.merge(df1, df2, on="Name")
```
* Kombiniert beide Tabellen, wo die Spalte "Name" übereinstimmt

* Andere Modi: how="inner", how="left", how="outer" (wie SQL-Joins)

## 📄 Beispiel: Zwei CSV-Dateien verbinden
### 🔹 personen.csv
```
Name,Alter
Anna,22
Ben,23
Clara,21
```
### 🔹 studiengang.csv
```
Name,Studiengang
Anna,Informatik
Ben,BWL
Clara,Informatik
```

### 🧱 Schrittweise Lösung:
```python
import pandas as pd

# CSV-Dateien laden
personen = pd.read_csv("personen.csv")
studiengaenge = pd.read_csv("studiengang.csv")

# Tabellen zusammenführen
df = pd.merge(personen, studiengaenge, on="Name")
print(df)
```
➡️ Ergebnis:

```
    Name  Alter  Studiengang
0   Anna     22  Informatik
1    Ben     23        BWL
2  Clara     21  Informatik
```

## ✅ Zusammenfassung

| Technik | Beispiel
| - | -
Sortieren | `df.sort_values("Spalte")`
Filtern mit Bedingung | `df[df["Spalte"] > 1000]`
Kombination mit merge | `pd.merge(df1, df2, on="ID")`
Kombination mit concat | `pd.concat([df1, df2])`
Mehrere Bedingungen | (A) & (B) mit Klammern

## 🔧 Übung: Daten sinnvoll verbinden
### 📄 Gegeben:
mitarbeiter.csv mit "ID", "Name", "Abteilung"

```
ID,Name,Abteilung
101,Anna Schulz,IT
102,Ben Meier,HR
103,Clara Lange,IT
104,David Koch,Marketing
105,Ella Frank,HR
106,Felix Nowak,Finanzen
```

gehaelter.csv mit "ID", "Gehalt"
```
ID,Gehalt
101,4500
102,3900
103,4800
104,4100
105,3700
106,5300
```

### ✅ Aufgabe:
* Lade beide Dateien mit pd.read_csv()

* Füge sie mit merge() anhand der ID-Spalte zusammen

* Filtere alle Personen mit Gehalt > 4000

* Sortiere nach Abteilung und dann nach Gehalt

* Optional: Speichere das Ergebnis als auswertung.csv

## ✅ Lösung:
```{admonition} 💡 Lösung anzeigen
:class: dropdown

```python
# Zusammenfügen
df = pd.merge(mitarbeiter, gehaelter, on="ID")

# Filtern und sortieren
df = df[df["Gehalt"] > 4000].sort_values(["Abteilung", "Gehalt"], ascending=[True, False])
```