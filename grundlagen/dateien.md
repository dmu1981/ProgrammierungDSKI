# 🗂️ Dateien öffnen, lesen und schreiben in Python
Motivation:


* Daten dauerhaft speichern
* Ergebnisse auswerten, weiterverarbeiten
* Programme mit externen Daten „füttern“
* Typische Anwendungsfälle:
    Log-Dateien, Konfigurationsdateien, CSVs, Benutzerlisten
    
## 🔹 Dateien öffnen: open() und with
```python
  with open("datei.txt", "r") as f:
    inhalt = f.read()
```    

Modi
| Modus | Bedeutung
| - | -
"r" | lesen (default)
"w" | schreiben (überschreibt!)
"a" | anhängen
"x" | neu erstellen (Fehler bei Existenz)

## Datei lesen (verschiedene Methoden)
```python
with open("beispiel.txt", "r") as f:
    text = f.read()         # Ganze Datei als String
    zeilen = f.readlines()  # Liste mit Zeilen
    f.seek(0)               # zurück zum Anfang
    for zeile in f:         # zeilenweise iterieren
        print(zeile.strip())
```

## 🔹 Datei schreiben
```python
with open("ausgabe.txt", "w") as f:
    f.write("Das ist eine Zeile.\n")
    f.write("Noch eine Zeile.\n")
```

## 🔹 Anhängen an Datei
```python
with open("log.txt", "a") as f:
    f.write("Neue Eintragung\n")
```

## Fehlerbehandlung beim Datei-Zugriff
```python
try:
    with open("daten.txt", "r") as f:
        daten = f.read()
except FileNotFoundError:
    print("❌ Datei nicht gefunden.")
```

## ✍️ Übungsaufgaben
🔸 **Aufgabe 1**: Lesen & Zählen
Erstelle eine Datei text.txt mit mehreren Zeilen.
Lies die Datei zeilenweise ein und gib jede Zeile nummeriert aus. Gib auch die Anzahl der Zeichen pro Zeile aus.

    [Eingabedatei]
    Dies ist ein einfacher Test.
    Diese Datei enthält mehrere Zeilen
    Wieviele Zeilen es sind weiß man erst wenn man die Datei wirklich liest.
    Das hier ist die letzte Zeile

    [Ausgabe]
    1 (   29): Dies ist ein einfacher Test.
    2 (   36): Diese Datei enthÃ¤lt mehrere Zeilen
    3 (   74): Wieviele Zeilen es sind weiÃŸ man erst wenn man die Datei wirklich liest.
    4 (   29): Das hier ist die letzte Zeile

[Lösung](dateilesensolution.md)


🔸 **Aufgabe 2**: Notendurchschnitt berechnen

Erstelle ein Programm, das Noten zusammen mit Schülernamen aus einer Datei liest. Eine Zeile enthält dabei mit Komma getrennt Name und Note des Schülers. Berechne dann den Klassendurchschnitt. Gib auch den Namen des Schülers mit der besten und der schlechtesten Note aus. 
  
    [Eingabedatei]
    Anne, 1.3
    Beate, 2.7
    Clara, 2.0
    Denise 1.0
    Erika, 3.3

    [Ausgabe]
    Der Durschnitt beträgt 2.06.
    Anne hat die beste Note mit 1.3 geschrieben.
    Erika hat die schlechteste Note mit 3.3 geschrieben.

[Lösung](notensolution.md)