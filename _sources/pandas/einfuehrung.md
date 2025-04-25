# 🐼 Einführung in Pandas
## 📦 Pandas installieren 
```python
pip install pandas
```

## 🧱 Datenstrukturen in Pandas
```python
import pandas as pd

s = pd.Series([10, 20, 30])
print(s)
```

➡️ Eine 1-dimensionale Liste mit Index

## 🔹 DataFrame – eine Tabelle
```python
daten = {
    "Name": ["Anna", "Ben", "Clara"],
    "Alter": [22, 23, 21]
}

df = pd.DataFrame(daten)
print(df)
```

➡️ Mehrere Spalten mit Beschriftung

## 📄 Daten aus CSV-Datei laden
```python
# personen.csv
Name,Alter,Stadt
Anna,22,Berlin
Ben,23,Hamburg
Clara,21,München
```

```python
df = pd.read_csv("personen.csv")
print(df)
```
## 🧰 Nützliche Methoden zum Einstieg
| Methode | Bedeutung
| - | -
`df.head()` | Erste 5 Zeilen
`df.tail()` | Letzte 5 Zeilen
`df.info()` | Übersicht: Spalten, Typen, Nullwerte
`df.describe()` | Statistische Kennzahlen (für Zahlen)
`df.columns` | Liste aller Spaltennamen
`df.shape` | Anzahl Zeilen und Spalten

## 🔍 Zugriff auf Daten
**Spalte auswählen**:
```python
df["Name"]
```

**Mehrere Spalten auswählen**:
```python
df[["Name", "Stadt"]]
```

**Zeile nach Index:**
```python
df.iloc[0]    # Zeile 0
df.loc[1]     # Zeile mit Index 1
```

## 🔍 `loc` vs. `iloc` – Was ist der Unterschied?
Pandas bietet zwei Methoden, um auf Zeilen oder Ausschnitte eines DataFrames zuzugreifen:

| Zugriffsmethode | Zugriff über… | Was es bedeutet
| - | - | -
`iloc` | position (Indexnummer) | Zugriff auf Zeilen/Spalten nach Reihenfolge
`loc` | label (Indexwert) | Zugriff über explizite Bezeichnung

```python
import pandas as pd

daten = {
    "Name": ["Anna", "Ben", "Clara"],
    "Alter": [22, 23, 21]
}
df = pd.DataFrame(daten, index=["a", "b", "c"])
```

### 🔸 df.iloc[0] → Zugriff auf erste Zeile (Position 0)
```python
print(df.iloc[0])

Name     Anna
Alter      22
Name: a, dtype: object
```

### 🔸 df.loc["a"] → Zugriff auf Zeile mit Index-Label "a"
```python
print(df.loc["a"])

Name     Anna
Alter      22
Name: a, dtype: object
```
| Ausdruck | Bedeutung
| - | - 
`df.iloc[0]` | Erste Zeile im DataFrame
`df.loc["a"]` | Zeile mit explizitem Label "a"
`df.iloc[1:3]` | Zeilen 1 bis 2 (Position 1–2)
`df.loc["b":"c"]` | Zeilen von "b" bis "c" (inkl.)

### ⚠️ Achtung: Wenn kein benannter Index gesetzt wurde (z. B. durch CSV-Datei), sind loc und iloc oft gleichwertig – aber konzeptionell verschieden.

## ➕ Neue Spalte berechnen
```python
df["Geburtsjahr"] = 2024 - df["Alter"]
```
✍️ übungsaufgabe:
* Lade die Datei personen.csv mit pd.read_csv()

* Gib die ersten zwei Zeilen aus

* Liste nur die Namen aller Personen

* Wie viele Personen sind insgesamt erfasst?

* Füge eine Spalte Volljährig hinzu mit True/False je nach Alter

* Speichere das Ergebnis als personen_neu.csv mit df.to_csv()