# 🐍 Python: Hello World Beispiel

Ein klassisches erstes Programm in Python – es gibt einfach `"Hello, World!"` auf der Konsole aus:

```python
# hello.py

print("Hello, World!")
```

Erstellen Sie eine neue Datei mit Namen "hello.py" und übernehmen Sie den obigen Programmcode. Führen Sie das Programm aus. 

## 🧩 Benutzereingaben

Mit der Funktion [input](https://www.w3schools.com/python/ref_func_input.asp) können wir eine Benutzereingabe entgegennehmen und in einer *Variable* speichern. Wir können auch den Inhalt einer Variable (das was dort aktuell gespeichert ist) wieder auf der Konsole ausgeben. 

```python
name = input("Wie heißt du? ")
print(f"Hallo, {name}!")
```

## Formatierte Zeichenketten (f-Strings) in Python

Formatierte Zeichenketten, auch **f-Strings** genannt, ermöglichen es, **Variablen direkt in einen String einzubetten**. Sie wurden mit **Python 3.6** eingeführt und sind eine **lesbare und effiziente** Möglichkeit, Strings zusammenzusetzen.

### Syntax

```python
name = "Maria"
print(f"Hallo, {name}!")
```

## Kommentare in Python

Kommentare sind Texte im Code, die **nicht ausgeführt** werden. Sie dienen dazu, den Code zu erklären, Notizen zu machen oder bestimmte Teile vorübergehend zu deaktivieren.

Kommentare beginnen mit dem **Rautezeichen `#`**.

```python
# Das ist ein Kommentar
name = "Sofia"  # Diese Variable speichert den Namen
```

Alles nach dem `#` in einer Zeile wird von Python ignoriert.

💡 Tipp: Schreibe immer dann Kommentare, wenn du dir oder anderen den Code später verständlicher machen willst.

## 📝 Übung: Begrüßung mit Name und Alter

### Aufgabe

Schreibe ein kleines Python-Programm, das folgende Schritte ausführt:

1. Fragt die Benutzerin oder den Benutzer nach dem **Namen**.
2. Fragt nach dem **Alter**.
3. Gibt eine persönliche Begrüßung aus, z. B.:

    Hallo Anna, dein Alter ist 23

### Hinweise

- Verwende `input()` für die Eingaben.
- Verwende einen **f-String** für die Ausgabe.

### Musterlösung

[Lösung](helloworldsolution.md)


