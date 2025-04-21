
# 🔍 Python-Version installieren mit `pyenv`
Wir verwenden `PyEnv` um Python zu installieren und zu managen
Installieren Sie zunächst [PyEnv für Windows](https://github.com/pyenv-win/pyenv-win) oder [PyEnv für Linux](https://github.com/pyenv/pyenv)

## 🐍 Python-Version installieren mit pyenv
```python
pyenv install 3.11.7
```

## 📌 Python-Version verwenden
* Nur für aktuelles Terminal:
```bash
pyenv shell 3.11.7
```
* Für ein ganzes Projektverzeichnis:
```bash
pyenv local 3.11.7
```
* Systemweite Einstellung (nur für den aktuellen Nutzer)
```bash
pyenv global 3.11.7
```

## 🔍 Version prüfen
```bash
python --version
# oder
pyenv versions
```

## 🔄 Beispiel-Workflow für Studierende
```bash
pyenv install 3.11.7
pyenv global 3.11.7
python --version
# → Python 3.11.7
```

## ❓ Warum `pyenv` statt System-Python?
| System-Python | pyenv
| - | - 
Kann nicht ersetzt werden | Beliebige Versionen installierbar
Kann zu Konflikten führen | Kein Risiko für Systemprozesse
Oft veraltet | Du hast immer die Kontrolle

## ✅ Zusammenfassung
| Befehl | Bedeutung
| - | -
`pyenv install 3.x.x` | Neue Version installieren
`pyenv global 3.x.x` | Standardversion setzen
`pyenv local 3.x.x` | Version pro Projekt festlegen
`pyenv versions` | Zeigt alle installierten Versionen
`python --version` | Aktive Version prüfen