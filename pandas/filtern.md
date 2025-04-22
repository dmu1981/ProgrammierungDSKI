# 🐼 Arbeiten mit DataFrames – Filtern, Berechnen, Erweitern

## 🔄 Wiederholung: Was ist ein DataFrame?
Ein DataFrame ist eine Tabelle mit Zeilen (Index) und Spalten (Labels). Man kann damit sehr einfach rechnen, filtern, kombinieren und analysieren – so wie mit Excel, nur programmierbar und effizient.

```python
import pandas as pd

daten = {
    "Name": ["Anna", "Ben", "Clara", "David", "Ella"],
    "Alter": [22, 23, 21, 24, 20],
    "Stadt": ["Berlin", "Hamburg", "München", "Berlin", "Köln"],
    "Note": [1.7, 2.3, 1.3, None, 2.0]
}

df = pd.DataFrame(daten)
``` 

## 🔍 Daten filtern (Bedingungen)
### 🔸 Nur Personen mit Alter > 21
```python
df[df["Alter"] > 21]
```
### 🔸 Mehrere Bedingungen (mit &, |)
```python
df[(df["Alter"] > 21) & (df["Stadt"] == "Berlin")]
```
### 🔸 Nur bestimmte Werte (isin())
```python
df[df["Stadt"].isin(["Berlin", "Köln"])]
```

## ➕ Neue Spalten berechnen
```python
df["Geburtsjahr"] = 2024 - df["Alter"]
```

## 📊 Sortieren
Nach einer Spalte:
```python
df.sort_values("Alter")
```

Nach mehreren Spalten:
```python
df.sort_values(["Stadt", "Note"])
```

Absteigend:
```python
df.sort_values("Note", ascending=False)
```

## 🚫 Fehlende Werte (NaN) erkennen und behandeln

Fehlenden Werten erkennen:
```python
df.isnull()         # True/False für jede Zelle
df["Note"].isnull() # nur für eine Spalte
df.isnull().sum()   # Anzahl pro Spalte
df[df["Note"].isnull()] # Zeilen, wo Note NaN ist
```

Fehlende Werte ersetzen:
```python
df["Note"].fillna(0)
```

Oder mit dem Durchschnitt:

```python
df["Note"].fillna(df["Note"].mean())
```

Zeilen mit fehlenden Werten löschen:
```python
df.dropna()
```

## ➗ 5. Arithmetische Operationen auf Spalten
```python
df["Note"] * 2
df["Alter"] + 1
```

➡️ Funktioniert automatisch elementweise auf jede Zeile

## 🧬 Datentypen in Pandas und Umwandlung (astype, to_numeric)
Jede Spalte in einem DataFrame hat einen Datentyp – z. B. int64, float64, object (für Strings).

### 📌 Datentypen anzeigen:
```python
print(df.dtypes)
```

## 🔄 Umwandlung in numerische Typen
Variante 1: `astype()`
```python
df["Alter"] = df["Alter"].astype(int)
df["Größe"] = df["Größe"].astype(float)
```
Variante 2: `pd.to_numeric()` (sicherer bei Fehlern)
```python
df["Alter"] = pd.to_numeric(df["Alter"], errors="coerce")
```
→ Falls Umwandlung fehlschlägt: NaN wird gesetzt statt Fehler

✅ Zusammenfassung

| Technik | Beispiel
| - | -
Filtern | df[df["Alter"] > 21]
Neue Spalte | df["x"] = df["y"] + 1
Sortieren | df.sort_values("Spalte")
Fehlende Werte ersetzen | fillna()
Logik & Bedingungen | &, `

## 🔧 Übung: Berechne BMI und entferne unvollständige Zeilen
In einem Fitnessstudio wurde von verschiedenen Teilnehmer eines Kurses die Größe und das Gewicht abgefragt. Da die Angaben freiwillig waren haben nicht alle immer auch geantwortet. Berechnen Sie BMI für alle Teilnehmer, die vollständig geantwortet haben

$$ BMI = Gewicht / Größe² $$

sowie durchschnittlichen BMI aller Teilnehmer.
### 📄 Beispiel-DataFrame:
```python
import pandas as pd 

df = pd.DataFrame({
    "Name": ["Anna", "Ben", "Clara", "David"],
    "Größe_m": [1.70, 1.82, None, 1.76],
    "Gewicht_kg": [65, 85, 59, None]
})
```

## ✅ Lösung:
```{admonition} 💡 Lösung anzeigen
:class: dropdown

```python
df = df.dropna()
df["BMI"] = df["Gewicht_kg"] / (df["Größe_m"] ** 2)
print(df[["Name", "BMI"]])
```