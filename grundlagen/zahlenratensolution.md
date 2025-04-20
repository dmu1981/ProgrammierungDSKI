```python
import random

# Zufallszahl zwischen 1 und 100 erzeugen
geheimzahl = random.randint(1, 100)

print("🎲 Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht.")
print("Kannst du sie erraten?")

# Endlosschleife zum Raten
while True:
    eingabe = input("Gib deine Schätzung ein: ").strip()

    if not eingabe.isdigit():
        print("❌ Bitte gib eine gültige ganze Zahl ein.")
        continue

    tipp = int(eingabe)

    if tipp < geheimzahl:
        print("🔻 Die gesuchte Zahl ist größer.")
    elif tipp > geheimzahl:
        print("🔺 Die gesuchte Zahl ist kleiner.")
    else:
        print(f"✅ Richtig! Die Zahl war {geheimzahl}. Gut gemacht!")
        break

```