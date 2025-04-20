try:
    with open("text.txt", "r") as f:
        zeilen = f.readlines()
        
        bester = None
        schlechtester = None
        durchschnitt = 0
        anzahl = 0

        for zeile in zeilen:
            
            zeile = zeile.split(',')
            name = zeile[0].strip()
            note = float(zeile[1].strip())

            durchschnitt = durchschnitt + note
            anzahl = anzahl + 1
            if bester is None or note < bester[1]:
                bester = (name, note)
            if schlechtester is None or note > schlechtester[1]:
                schlechtester = (name, note)

        print(f"Der Durschnitt beträgt {durchschnitt/anzahl:.2}.")
        print(f"{bester[0]} hat die beste Note mit {bester[1]}.")
        print(f"{schlechtester[0]} hat die schlechteste Note mit {schlechtester[1]}.")

except FileNotFoundError:
    print("❌ Datei nicht gefunden.")