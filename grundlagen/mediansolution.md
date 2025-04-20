```python
elemente = []
while True:
  zahl = input("Nächste Zahl bitte:")
  if zahl == "fertig":
    break
  elemente.append(int(zahl))

elemente.sort()
print(elemente)

anzahl = len(elemente)
if anzahl % 2 == 1:
  print(f"Der Median ist {elemente[anzahl//2]}")
else:
  a = elemente[anzahl//2-1]
  b = elemente[anzahl//2]
  print(f"Der Median ist {(a+b)/2}")
```