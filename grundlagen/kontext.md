# 📚 Kontextmanager & with-Statement in Python

## 🧠 Was ist ein Kontextmanager?
Ein Kontextmanager verwaltet Ressourcen, z. B. Dateien oder Verbindungen.
Er sorgt dafür, dass automatisch aufgeräumt wird – egal, ob ein Fehler auftritt oder nicht.

➡️ In Python wird ein Kontextmanager mit with verwendet.

## 🔧 Beispiel: Datei öffnen mit with
```python
with open("daten.txt", "r") as f:
    inhalt = f.read()
    print(inhalt)
```

Das ist das gleiche wie:
```python
f = open("daten.txt", "r")
try:
    inhalt = f.read()
finally:
    f.close()  # ❗ wichtig, aber leicht zu vergessen!

``` 

✅ with kümmert sich um das Schließen der Datei automatisch

## 🚀 Eigener Kontextmanager
Eigene Kontextmanager können mit der `__enter__()` und `__exit__()` Methode implementiert werden. 
```python
class EinfacherLogger:
    def __enter__(self):
        print("🔓 Start des Blocks")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("🔒 Ende des Blocks")

# Anwendung:
with EinfacherLogger():
    print("→ Hier passiert etwas")
```

➡️ Ausgabe:
```python
🔓 Start des Blocks
→ Hier passiert etwas
🔒 Ende des Blocks
``` 