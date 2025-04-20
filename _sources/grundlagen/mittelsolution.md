```python
elemente = []
while True:
  zahl = input("Gib die Meßgröße ein:")
  if zahl == "":
    break
  gewicht = input("Gib die Häufigkeit der Meßgröße ein:")
  if gewicht == "":
    break
  elemente.append((float(zahl), int(gewicht)))
print(elemente)
summeX, summeW = 0, 0
for x, w in elemente:
  summeX = summeX + x * w
  summeW = summeW + w

print(f"Das arithmetische Mittel ist {summeX / summeW}") 
```