# 🐼 Zeitreihenanalyse & Daten speichern mit Pandas

## 📅 Datumsangaben verarbeiten mit `pd.to_datetime()`
Wenn eine Spalte ein Datum enthält, solltest du sie in ein datetime-Objekt umwandeln:

```python
import pandas as pd

df = pd.DataFrame({
    "Datum": ["2024-01-15", "2024-01-20", "2024-02-05"],
    "Temperatur": [2.1, 3.4, 5.0]
})

df["Datum"] = pd.to_datetime(df["Datum"])
```
➡️ Jetzt kann Pandas mit den Werten als Zeitstempel rechnen und gruppieren.

## 📆 Zeitwerte extrahieren: `.dt.year`, `.dt.month`, `.dt.day`
```python
df["Monat"] = df["Datum"].dt.month
df["Jahr"] = df["Datum"].dt.year
```
➡️ Nützlich für Gruppierungen, Visualisierung oder Filterung

## 📈 Zeitreihen analysieren mit `.resample()`
`.resample()` funktioniert wie `groupby()` – nur auf Zeitachsen!

Dafür muss das Datum im Index stehen:

```python
df.set_index("Datum", inplace=True)

# Durchschnitt pro Monat:
df_monatlich = df.resample("M").mean()
```

Kürzel | Bedeutung
-|-
"D" | täglich
"W" | wöchentlich
"M" | monatlich
"Y" | jährlich
Kürzel | Bedeutung
'Q' | Quartal
'Y' | jährlich
'H' | stündlich
'T' | minütlich (T = "minute")

## 🧪 Beispiel: Temperatur-Zeitreihe analysieren mit `resample()` 
Wir erstellen eine kleine tägliche Zeitreihe über mehrere Wochen und berechnen den Wochendurchschnitt der Temperatur mit .resample("W").

```python
import pandas as pd

# Beispieldaten: Tägliche Temperaturen im Januar
daten = {
    "Datum": pd.date_range(start="2024-01-01", periods=15, freq="D"),
    "Temperatur": [2.3, 2.8, 3.1, 1.9, 2.5, 3.0, 3.2,
                   2.9, 2.6, 3.4, 2.8, 3.0, 2.7, 3.1, 3.3]
}

df = pd.DataFrame(daten)
df.set_index("Datum", inplace=True)

print("📅 Tagesdaten:")
print(df.head())
```

### 📈 Wöchentliche Durchschnittstemperatur:
```python
woechentlich = df.resample("W").mean()
print("\n📊 Wöchentliche Durchschnittstemperatur:")
print(woechentlich)
```

### 💡 Erklärung:
`.resample("W")` → gruppiert die Zeitreihe wochenweise (Sonntag-Sonntag)

`.mean()` → berechnet den Durchschnitt pro Woche

Weitere Aggregationen sind möglich: `.sum()`, `.max()`, `.agg(...)`

### 🔍 Beispiel-Ausgabe:
```yaml
📅 Tagesdaten:
            Temperatur
Datum                
2024-01-01        2.3
2024-01-02        2.8
2024-01-03        3.1
2024-01-04        1.9
2024-01-05        2.5

📊 Wöchentliche Durchschnittstemperatur:
            Temperatur
Datum                 
2024-01-07     2.685714
2024-01-14     2.942857
2024-01-21     3.300000
```

## 📤 Daten exportieren
### 🔸 Als CSV:
```python
df.to_csv("auswertung.csv", index=False)
```

### 🔸 Als Excel:
```python
df.to_excel("auswertung.xlsx", index=False)
🔧 Voraussetzung: pip install openpyxl
```

### 🔸 Als JSON:
```python
df.to_json("auswertung.json", orient="records", indent=2)
```

## ✅ Zusammenfassung
Thema | Beispiel
| - | -
Datum konvertieren | `pd.to_datetime()`
Zeitwerte extrahieren | `.dt.month`, `.dt.year`
Zeitlich gruppieren | `.resample("M").mean()`
Ergebnisse speichern | `.to_csv()`, `.to_excel()`, `.to_json()`

## 🔧 Übung: Wetterdaten analysieren
### 📄 Beispielhafte CSV-Datei wetter.csv:
```
Datum,Temperatur
2024-01-01,2.3
2024-01-02,3.1
2024-01-15,1.8
2024-02-01,4.5
2024-02-15,5.1
2024-03-01,7.2
```

### ✅ Aufgaben:
* Lade die Datei wetter.csv mit `pd.read_csv()`

* Wandle die "Datum"-Spalte in datetime-Format um

* Setze "Datum" als Index

* Berechne die monatliche Durchschnittstemperatur

* Exportiere die Ergebnisse als monatstemperatur.csv

## ✅ Lösung:
```{admonition} 💡 Lösung anzeigen
:class: dropdown

```python
df = pd.read_csv("wetter.csv")
df["Datum"] = pd.to_datetime(df["Datum"])
df.set_index("Datum", inplace=True)

monatlich = df.resample("M").mean()
monatlich.to_csv("monatstemperatur.csv")
```