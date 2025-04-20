# 🧮 Einführung in `math` und `random` in Python

Python bringt viele nützliche Standard-Module mit, die man einfach importieren und direkt nutzen kann. Zwei davon sind:

`math`: für mathematische Funktionen (wie Wurzeln, Sinus, Pi, Runden …)
`random`: für Zufallszahlen und Zufallsauswahl (z. B. für Spiele oder Simulationen)

## Mathematische Funktionen mit dem `math` Paket
```python
import math
print(math.sqrt(16))       # Quadratwurzel → 4.0
print(math.pow(2, 3))      # Potenzieren → 2³ = 8.0
print(math.factorial(5))   # Fakultät → 5! = 120
print(math.floor(3.7))     # Abrunden → 3
print(math.ceil(3.1))      # Aufrunden → 4
print(math.pi)             # Kreiszahl π → 3.14159...
```

## Zufallszahlen mit dem `random` Paket:
```python
import random
print(random.randint(1, 6))                   # Zufallszahl zwischen 1 und 6 (inkl.)
print(random.random())                        # Zufalls-Float zwischen 0.0 und 1.0
print(random.choice(["rot", "blau", "grün"])) # Zufälliges Element aus Liste
print(random.shuffle(liste))                  # Liste zufällig durchmischen (in-place)
```

**Beispiel**: 
```python
import random
for _ in range(5):
    wurf = random.randint(1, 6)
    print("Du hast eine", wurf, "gewürfelt!")
```    

## 🎓 Übungsaufgabe:
### Kreisfläche und Umfang
Schreibe ein Programm welches den Benutzer nach dem Radius eines Kreises fragt. Nutze dann das `math`-Paket um den Kreisumfang $$U = 2\pi\cdot r$$ sowie die Kreisfläche $$A = \pi\cdot r^2$$ zu berechnen. Gib Umfang und Fläche auf zwei Nachkommastellen gerundet auf der Konsole aus. 
### Zahlenraten
Schreibe ein Programm, welches sich eine Zufallszahl zwischen 1 und 100 ausdenkt. Verwende dazu
[random.randint](https://www.w3schools.com/python/ref_random_randint.asp)() wie im Beispiel oben. Schreibe dann eine `while True:` Endloß-Schleife, die den Benutzer die Zahl erraten läßt. Frage dazu im Schleifenkörper nach einer Zahl. Gib aus ob die zu erratenden Zahl größer oder kleiner ist. Beende die Schleife mit `break` falls der Benutzer richtig geraten hat. 