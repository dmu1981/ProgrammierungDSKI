```python
def wortzaehler():
    satz = input("Gib einen Satz ein: ").strip()

    # In Wörter aufteilen
    woerter = satz.split()

    # Dictionary zur Zählung
    wort_haeufigkeit = {}

    for wort in woerter:
        wort = wort.strip(".,!?;:()[]\"'").lower()  # Satzzeichen entfernen, klein schreiben
        if wort in wort_haeufigkeit:
            wort_haeufigkeit[wort] += 1
        else:
            wort_haeufigkeit[wort] = 1

    # Ausgabe
    print("\nWortanzahl im Satz:")
    for wort, anzahl in wort_haeufigkeit.items():
        print(f"'{wort}': {anzahl}x")

# Programm ausführen
wortzaehler()
```