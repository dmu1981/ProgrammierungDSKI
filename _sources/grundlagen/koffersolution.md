```python
koffer =  set()
while True:
  # Alle Items abfragen
  item = input("Ich packe meinen Koffer und nehme mit: ")

  # Am "," splitten
  items = item.split(",")
  items = [item.strip() for item in items]
  
  # Doppelte entfernen
  items = set(items)

  # Wurde etwas vergessen?
  vergessen = koffer - items
  if len(vergessen) > 0:
    print("Du hast", vergessen, "vergessen")
    exit()

  # Wurde mehr als ein neuer Gegenstand hingezufügt?
  neue = items - koffer
  if len(neue) != 1:
    print("Du musst genau einen neuen Gegenstand hinzufügen.")
    exit()

  koffer = koffer | items
```