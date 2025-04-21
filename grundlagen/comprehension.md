# 🧠 Dict- & Set-Comprehensions in Python
## 🔄 Erinnerung: List Comprehension
```python 
quadrate = [x**2 for x in range(5)]
# → [0, 1, 4, 9, 16]
```

## 🔶 Set Comprehension

### 📌 Syntax:
```python
{ausdruck for element in iterable}
```
### ✅ Beispiel:
```python
zahlen = [1, 2, 2, 3, 4, 4, 5]
einzigartige_quadrate = {x**2 for x in zahlen}
print(einzigartige_quadrate)
# → {1, 4, 9, 16, 25}
```
### ➕ Mit Bedingung:
```python
gerade_quadrate = {x**2 for x in range(10) if x % 2 == 0}
# → {0, 4, 16, 36, 64}
```

## 🟨 Dict Comprehension
### 📌 Syntax:
```python
{key_expr: value_expr for element in iterable}
```

### ✅ Beispiel: Zahlen und ihre Quadrate
```python
quadrat_dict = {x: x**2 for x in range(5)}
# → {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### 📄 Beispiel: Wörter und ihre Längen

```python
woerter = ["Apfel", "Banane", "Kirsche"]
laengen = {wort: len(wort) for wort in woerter}
# → {'Apfel': 5, 'Banane': 6, 'Kirsche': 7}
```

### ➕ Mit Bedingung (z. B. nur kurze Wörter)
```python 
kurze_woerter = {wort: len(wort) for wort in woerter if len(wort) <= 6}
# → {'Apfel': 5, 'Banane': 6}
```

## ✅ Zusammenfassung
| Comprehension | Zweck | Syntax
| - | - | -
List | geordnete Liste | `[ausdruck for x in ...]`
Set | einzigartige Werte | `{ausdruck for x in ...}`
Dict | Schlüssel-Wert-Paare | `{key: value for x in ...}`