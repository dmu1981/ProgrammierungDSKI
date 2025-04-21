# 🐼 Pandas?
Pandas ist eine Open-Source-Bibliothek für Datenanalyse und Datenmanipulation in Python. Sie ermöglicht das Arbeiten mit tabellarischen Daten (ähnlich wie Excel, CSV, SQL oder DataFrames in R) – aber viel mächtiger.

Mit Pandas kannst du:

Daten einlesen, sortieren, filtern, gruppieren, zusammenfassen, berechnen, plotten und exportieren
komplexe Datenanalysen elegant und effizient durchführen

## 🧭 Übersicht: Themenplan „Pandas – Grundlagen der Datenanalyse“
### 📘 Abschnitt 1 – Einführung in Pandas
* Was ist Pandas? Warum braucht man es?
* Series und DataFrame: die zentralen Objekte
* Einlesen von CSV-Dateien mit pd.read_csv()
* Erste Methoden: .head(), .tail(), .info(), .describe()
* Zugriff auf Spalten & Zeilen: df["Spalte"], df.loc[], df.iloc[]
* 🔧 Übung: Lade personen.csv ein, gib nur die Spalten „Name“ und „Stadt“ aus

### 📘 Abschnitt 2 – Arbeiten mit DataFrames
* Auswahl & Filterung von Daten (df[df["Spalte"] > 10])
* Neue Spalten berechnen (df["BMI"] = ...)
* Datentypen, Umwandlungen (astype, to_numeric)
* Fehlende Werte: isnull(), fillna(), dropna()
* 🔧 Übung: Berechne aus „Größe“ und „Gewicht“ die BMI-Spalte, entferne unvollständige Zeilen

### 📘 Abschnitt 3 – Gruppieren, Aggregieren & Statistiken
* Gruppierung mit groupby()
* Aggregation: .mean(), .sum(), .count(), .agg()
* Pivot-Tabellen
* Häufigkeiten mit value_counts()
* 🔧 Übung: Analysiere Durchschnittsalter nach Studiengang, häufigste Werte

### 📘 Abschnitt 4 – Sortieren, Filtern, Kombinieren
* Sortieren mit .sort_values()
* Logische Filter & Kombination (&, |)
* Kombinieren von DataFrames mit merge() und concat()
* Beispiel: CSV mit Personen und CSV mit Studiengängen verbinden
* 🔧 Übung: Füge Datensätze aus zwei CSV-Dateien sinnvoll zusammen

### 📘 Abschnitt 5 – Zeitreihen & Daten speichern
* Datumsangaben als datetime verarbeiten (pd.to_datetime())
* Zeitreihen analysieren: .resample(), .dt.year, .dt.month
* Export nach CSV, Excel, JSON (.to_csv(), .to_excel(), .to_json())
* 🔧 Übung: Lade Wetterdaten, berechne monatliche Durchschnittstemperatur

### 📘 Abschnitt 6 – Projekt & Visualisierung (Bonus)
* Abschlussprojekt: Freie Datenanalyse mit echten Daten (z. B. OpenData, Umfrage, Klima)
* Einführung in matplotlib oder pandas.plot()
* Präsentation & Interpretation der Ergebnisse
* 🔧 Projektideen:
  Schlaf- & Stressauswertung
  Öffentliche Verkehrsdaten analysieren
  Fußballstatistiken vergleichen

