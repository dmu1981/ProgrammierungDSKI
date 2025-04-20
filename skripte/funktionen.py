def add(a, b):
  return a + b

def sub(a, b):
  return a - b

def calc(a, b, func):
  return f"Das Ergebniss ist {func(a, b)}"

def auswahl():
  while True:
    wahl = input("Möchte Sie addieren (a) oder subtrahieren (s)?")
    if wahl == "a":
      return add

    if wahl == "s":
      return sub

func = auswahl()
print(calc(3,4, func))