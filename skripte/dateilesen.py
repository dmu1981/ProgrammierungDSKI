try:
    with open("text.txt", "r") as f:
        zeilen = f.readlines()
        for index, zeile in enumerate(zeilen):
            print(f"{index+1:5} ({len(zeile):5}): {zeile}", end="")
except FileNotFoundError:
    print("❌ Datei nicht gefunden.")