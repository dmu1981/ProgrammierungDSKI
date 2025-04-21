```python
import math

# Funktion zur Eingabe eines einzelnen 2D-Vektors
def eingabe_vektor():
    eingabe = input("Gib einen Vektor ein (x1, x2), oder nur Enter zum Beenden: ").strip()
    
    if eingabe == "":
        return None

    x1_str, x2_str = eingabe.split(",")
    x1 = float(x1_str.strip())
    x2 = float(x2_str.strip())
    return (x1, x2)

# Funktion zur Berechnung der euklidischen Länge
def vektorlaenge(vektor):
    x1, x2 = vektor
    return math.sqrt(x1**2 + x2**2)

# Hauptprogramm
vektoren = []

print("🔢 Vektor-Eingabeprogramm (2D-Vektoren)")
print("Beispiel-Eingabe: 0.5, -0.8")

# Eingabeschleife
while True:
    vektor = eingabe_vektor()
    if vektor is None:
        break
    vektoren.append(vektor)

# Sortieren nach euklidischer Länge
vektoren.sort(key=vektorlaenge)

# Ausgabe aller Vektoren mit Länge ≤ 1
print("\n📋 Vektoren mit Länge ≤ 1:")
for v in vektoren:
    if vektorlaenge(v) <= 1:
        print(f"  {v}  → Länge = {vektorlaenge(v):.3f}")

```

