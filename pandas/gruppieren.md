# 🐼 Gruppieren, Aggregieren & Statistiken mit Pandas
## 📦 Beispiel-DataFrame
```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["Anna", "Ben", "Clara", "David", "Ella", "Felix"],
    "Alter": [22, 23, 21, 24, 20, 23],
    "Studiengang": ["Informatik", "BWL", "Informatik", "Psychologie", "Informatik", "BWL"],
    "Note": [1.7, 2.3, 1.3, 2.0, 1.9, 2.7]
})
```

## 🔁 1. Gruppierung mit groupby()
Durchschnittsalter pro Studiengang:
```python
df.groupby("Studiengang")["Alter"].mean()
```

➡️ Gruppiert nach Studiengang und berechnet Mittelwert in jeder Gruppe

## ➕ Weitere Aggregationen

| Methode | Bedeutung
| - | -
`.mean()` | Mittelwert
`.sum()` | Summe aller Werte
`.count()` | Anzahl der Einträge
`.agg()` | Mehrere Aggregationen kombinieren

Anzahl Studierender pro Fachrichtung:
```python
df.groupby("Studiengang")["Name"].count()
```
➡️ Wie viele Personen gibt es je Gruppe?

## 🔹 Mehrere Aggregationen mit .agg():
```python
df.groupby("Studiengang").agg({
    "Alter": ["mean", "min", "max"],
    "Note": ["mean"]
})
```

## 🔄 3. Pivot-Tabellen
Pivot-Tabellen sind eine alternative Form von groupby, besonders praktisch für zweidimensionale Auswertungen.

Eine Pivot-Tabelle fasst Werte einer Tabelle nach Kategorien zusammen – z. B. Durchschnittsnoten pro Studiengang, Umsätze pro Region und Monat, u. v. m.

Du kannst damit:

* Daten nach Gruppen sortieren
* Werte zusammenfassen (mean, sum, count, etc.)
* mehrere Kennzahlen gleichzeitig analysieren

### 📦 Syntax
```python
pd.pivot_table(data, values=..., index=..., columns=..., aggfunc=...)
```
| Parameter | Bedeutung
| - | - 
`data` | dein DataFrame
`values` | Spalte(n), deren Werte du aggregieren willst
`index` | Zeile(n), nach denen gruppiert wird
`columns` | (optional) Spalte für Spaltenüberschriften
`aggfunc` | Aggregationsfunktion, z. B. mean, sum, count

### 🧪 Beispiel:
```python
import pandas as pd

df = pd.DataFrame({
    "Studiengang": ["Informatik", "BWL", "Informatik", "Psychologie", "Informatik", "BWL"],
    "Semester": [1, 1, 2, 1, 2, 2],
    "Note": [1.7, 2.3, 1.3, 2.0, 1.9, 2.7],
})
```

### 🔹 Durchschnittsnote je Studiengang
```
pd.pivot_table(df, values="Note", index="Studiengang", aggfunc="mean")

                 Note
Studiengang         
BWL              2.5
Informatik       1.633
Psychologie      2.0
```

### 🔹 Durchschnittsnote pro Studiengang und Semester:
```python
pd.pivot_table(df, values="Note", index="Studiengang", columns="Semester", aggfunc="mean")

Semester       1      2
Studiengang             
BWL          2.3    2.7
Informatik   1.7    1.6
Psychologie  2.0    NaN
```

### 🔹 Anzahl Studierender je Kombination (statt Mittelwert):
```python
pd.pivot_table(df, values="Note", index="Studiengang", columns="Semester", aggfunc="count")
```

### 🔹 Pivot-Tabellen mit mehreren Aggregationen
```python
pd.pivot_table(df, index="Studiengang", aggfunc={"Note": ["mean", "count"]})
```

### ✅ Wann ist pivot_table() besonders nützlich?
Wenn du mehr als eine Gruppierungsebene brauchst (z. B. nach Fach UND Semester)

Wenn du mehrere Spalten gleichzeitig analysieren willst

Wenn du Ergebnisse als Matrix brauchst (ähnlich wie Kreuztabelle)

### 🧠 Vergleich: `groupby()` vs. `pivot_table()`
| `groupby()` | `pivot_table()`
| - | -
gibt Series/DataFrame zurück | gibt Matrix-artige Tabelle zurück
ideal für 1-dimensionale Gruppen | ideal für 2D-Zusammenfassungen
einfach zu lesen | mächtiger, aber mehr Parameter

## 📊 4. Häufigkeiten zählen mit value_counts()
### Wie oft kommt jeder Studiengang vor?
```python
df["Studiengang"].value_counts()
```
➡️ Gibt die Häufigkeit jedes Werts in einer Spalte aus – sehr nützlich!

## 🧰 Zusammenfassung: Was geht mit `groupby()`
| Was du willst… | Code
| - | - 
Mittelwert je Gruppe | `df.groupby("Kategorie")["Wert"].mean()`
Anzahl je Gruppe | `df.groupby("Kategorie").count()`
Mehrere Kennzahlen | `.agg({"Spalte": ["mean", "max"]})`
2D-Auswertung (Pivot) | `pd.pivot_table(...)`
Häufigkeiten von Werten | `df["Spalte"].value_counts()`

## 🔧 Übung: Analysiere Durchschnittsalter nach Studiengang & häufigste Werte
### 📄 Datensatz (studierende.csv):
```csv
Name,Alter,Studiengang,Note
Anna,22,Informatik,1.7
Ben,23,BWL,2.3
Clara,21,Informatik,1.3
David,24,Psychologie,2.0
Ella,20,Informatik,1.9
Felix,23,BWL,2.7
```

### 🧠 Aufgaben:
Gib den Durchschnitt des Alters je Studiengang aus

Wie viele Personen studieren jeweils welchen Studiengang?

Berechne die Durchschnittsnote pro Studiengang als Pivot-Tabelle

Welche Note kommt am häufigsten vor? (value_counts())

## ✅ Lösung:
```{admonition} 💡 Lösung anzeigen
:class: dropdown

```python
df.groupby("Studiengang")["Alter"].mean()

df["Studiengang"].value_counts()

df.pivot_table(values="Note", index="Studiengang", aggfunc="mean")

df["Note"].value_counts()
```