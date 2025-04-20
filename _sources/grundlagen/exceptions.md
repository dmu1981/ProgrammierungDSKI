# 🚨 Fehlerbehandlung in Python – ``try``, ``except``, ``finally``
Python meldet zur Laufzeit Fehler mit sogenannten Exceptions. Beispiele:
```python
print(5 / 0)              # ZeroDivisionError
int("abc")                # ValueError
liste = [1, 2, 3]
print(liste[5])           # IndexError
```

## 🔹 Fehler abfangen mit ``try``–``except``
```python
try:
    zahl = int(input("Gib eine Zahl ein: "))
except ValueError:
    print("❌ Das war keine gültige Zahl!")
```

## 🔹 Mehrere Fehlertypen behandeln
```python
try:
    ...
except ValueError:
    print("❌ Ungültige Zahl.")
except ZeroDivisionError:
    print("❌ Division durch 0 nicht erlaubt.")
```

## 🔹 ``finally``: Immer ausführen (egal ob Fehler oder nicht)
```python
try:
    datei = open("daten.txt", "r")
    inhalt = datei.read()
except FileNotFoundError:
    print("❌ Datei nicht gefunden.")
finally:
    print("📦 Versuche Datei zu schließen.")
    if 'datei' in locals():
        datei.close()
```