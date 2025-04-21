# ✅ `assert` in Python
## 🔍 Was ist assert?
`assert` ist ein einfaches Werkzeug zur Überprüfung, ob eine bestimmte Bedingung wahr ist.
Wenn die Bedingung nicht erfüllt ist, bricht das Programm ab und zeigt eine Fehlermeldung an.
### 🧪 Syntax:
```python
assert bedingung, "Fehlermeldung (optional)"
```

### ✅ Beispiel:
```python
def teile(a, b):
    assert b != 0, "Division durch 0 ist nicht erlaubt"
    return a / b

print(teile(10, 2))   # → 5.0
print(teile(10, 0))   # AssertionError: Division durch 0 ist nicht erlaubt
```

## 🎯 Wozu assert verwenden?
* Um eigene Annahmen im Code zu überprüfen
* Für einfache Tests während der Entwicklung
* Zum Debuggen: „Darf dieser Fall überhaupt auftreten?“

## ⚠️ Wichtig:
assert ist nicht für Benutzerfehler gedacht – nur für Entwicklerprüfungen
Bei Ausführung mit python -O (Optimierung) werden asserts ignoriert