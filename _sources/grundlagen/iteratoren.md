# 🔁 Iteratoren in Python – und wie man eigene erstellt

## 🧠 Was ist ein Iterator?
Ein Iterator ist ein Objekt, das nacheinander Werte liefern kann, z. B. in einer for-Schleife.
Ein Iterator muss zwei Methoden haben:

```python
__iter__()   → liefert das Iteratorobjekt selbst  
__next__()   → liefert das nächste Element oder löst StopIteration aus
```

## 🔨 Eigene Iteratoren schreiben
```python
class Zaehler:
    def __init__(self, n):
        self.n = n
        self.aktuell = 1

    def __iter__(self):
        return self  # Iteratorobjekt ist die Klasse selbst

    def __next__(self):
        if self.aktuell <= self.n:
            wert = self.aktuell
            self.aktuell += 1
            return wert
        else:
            raise StopIteration
```

## 🔄 Was passiert in einer for-Schleife eigentlich?
```python
iterator = iter(objekt)
while True:
    try:
        wert = next(iterator)
        ...
    except StopIteration:
        break
```

## 📚 Zusammenfassung
| Konzept | Bedeutung
| - | -
`__iter__()` | liefert das Iterator-Objekt (oft self)
`__next__()` | liefert das nächste Element oder StopIteration
`iter(obj)` | erzeugt einen Iterator
`next(obj)` | gibt das nächste Element aus dem Iterator

## 🧪 Übungsaufgabe: Fibonacci-Iterator
Schreiben Sie einen Iterator, der die ersten n Fibonacci-Zahlen liefert. Die Fibonacci-Folge ist definiert durch

$$F(0) = F(1) = 1$$
$$F(n+2) = F(n + 1) + F(n)