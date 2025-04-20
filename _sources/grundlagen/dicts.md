# 📘 Dictionaries in Python – Daten als Schlüssel-Wert-Paare
Ein Dictionary ist eine Sammlung von Daten, die als Schlüssel-Wert-Paare organisiert ist.

Syntax:
```python
person = {
    "name": "Anna",
    "alter": 23,
    "studiengang": "Informatik"
}
```

## 🔹 Zugriff auf Werte
```python
print(person["name"])         # → Anna
print(person.get("alter"))    # → 23
``` 

Der Unterschied zwischen direkter Indizierung über den Schlüssel oder die [get](https://www.w3schools.com/python/ref_dictionary_get.asp()) Funktion ist, dass bei der get-Funktion `None` zurückgegeben wird, falls der Schlüssel im Dictionary nicht exisitiert. Bei direkter Indizierung kommt es zum Programmabbruch. 

## Werte ändern / hinzufügen
```python
person["alter"] = 24          # Wert ändern
person["wohnort"] = "Berlin"  # Neuer Eintrag
```

## Elemnte löschen
```python
del person["studiengang"]
```

## Wichtige Dictionary-Methoden
| Methode | Beschreibung
| - | -
dict.keys() | Gibt alle Schlüssel zurück
dict.values() | Gibt alle Werte zurück
dict.items() | Gibt Paare aus (Schlüssel, Wert) zurück
dict.get(k) | Gibt den Wert für k, sonst None
dict.pop(k) | Löscht Schlüssel k und gibt den Wert zurück

## Durch ein Dictionary iterieren
```python
for key in person:
    print(key, "→", person[key])
```

oder

```python
for key, value in person.items():
    print(f"{key}: {value}")

```

## 🎓 Übungsaufgabe: Noch eine Textanalyse
Frage den Benutzer nach einem beliebigen Satz. Verwende wieder [split](https://www.w3schools.com/jsref/jsref_split.asp)()
und [strip](https://www.w3schools.com/python/ref_string_strip.asp)() um den Satz in einzelne Wörter aufzuteilen. Erzeuge dann ein Dictionary, welches jedem Wort die Anzahl zuordnet, mit der es im Satz vorkommt.

```python
# Eingabe: "Hallo Welt Hallo"
# Ausgabe: {"Hallo": 2, "Welt": 1}
```

[Lösung](woertersolution.md)