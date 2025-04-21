import csv
from collections import defaultdict

# Datei einlesen und in Dictionaries umwandeln
def lade_umfragedaten(pfad):
    daten = []
    with open(pfad, newline="") as f:
        reader = csv.DictReader(f)
        for zeile in reader:
            zeile["Alter"] = int(zeile["Alter"])
            zeile["Schlafstunden"] = float(zeile["Schlafstunden"])
            zeile["Stresslevel"] = int(zeile["Stresslevel"])
            zeile["Bildschirmzeit"] = float(zeile["Bildschirmzeit"])
            daten.append(zeile)
    return daten

# 1. Durchschnittliche Schlafdauer berechnen
def durchschnitt_schlaf(daten):
    schlafstunden = [person["Schlafstunden"] for person in daten]
    return sum(schlafstunden) / len(schlafstunden)

# 2. Person mit höchster Bildschirmzeit
def max_bildschirmzeit(daten):
    return max(daten, key=lambda p: p["Bildschirmzeit"])

# 3. Anzahl der Informatik-Studierenden
def zaehle_informatiker(daten):
    return sum(1 for p in daten if p["Studiengang"] == "Informatik")

# 4. Filter: Personen mit Stresslevel > 3
def stress_hoch(daten):
    return [p for p in daten if p["Stresslevel"] > 3]

# 5. Durchschnittliche Bildschirmzeit pro Studiengang
def durchschnitt_bildschirmzeit_pro_studiengang(daten):
    gruppiert = defaultdict(list)
    for p in daten:
        gruppiert[p["Studiengang"]].append(p["Bildschirmzeit"])
    
    ergebnis = {}
    for studiengang, werte in gruppiert.items():
        ergebnis[studiengang] = sum(werte) / len(werte)
    return ergebnis

# Hauptprogramm
if __name__ == "__main__":
    daten = lade_umfragedaten("umfrage.csv")
    
    print("📊 Umfrageanalyse")
    print("-" * 30)
    
    print(f"1. Durchschnittlicher Schlaf: {durchschnitt_schlaf(daten):.2f} Stunden")
    
    max_pers = max_bildschirmzeit(daten)
    print(f"2. Höchste Bildschirmzeit: {max_pers['Name']} ({max_pers['Bildschirmzeit']} Std.)")
    
    inf_count = zaehle_informatiker(daten)
    print(f"3. Anzahl Informatik-Studierende: {inf_count}")
    
    stressige = stress_hoch(daten)
    print(f"4. Personen mit hohem Stresslevel (>3):")
    for p in stressige:
        print(f"   - {p['Name']} ({p['Stresslevel']})")
    
    print("5. Durchschnittliche Bildschirmzeit pro Studiengang:")
    for studiengang, schnitt in durchschnitt_bildschirmzeit_pro_studiengang(daten).items():
        print(f"   {studiengang}: {schnitt:.2f} Std.")