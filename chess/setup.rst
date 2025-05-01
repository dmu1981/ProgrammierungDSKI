Einrichtung der Python-Umgebung
===============================

Damit ihr das Schachprojekt lokal entwickeln und ausführen könnt, müsst ihr eine geeignete Python-Umgebung einrichten. Im Folgenden findet ihr eine Schritt-für-Schritt-Anleitung zur Installation aller benötigten Werkzeuge und Bibliotheken.

Voraussetzungen
---------------

- **Python 3.11 oder höher** muss installiert sein.
- Ein Terminal / eine Shell (z. B. `cmd`, PowerShell, Terminal, oder VSCode-Terminal)
- Optional, aber empfohlen: Virtuelle Umgebung (pyenv)

1. Wechselt in das Verzeichnis eures Projekts:

   .. code-block:: bash

        cd pfad/zum/projekt

2. Installiert die benötigten Pakete:

     .. code-block:: bash

        pip install numpy pygame unittest unittest-prettify

Hinweise zur IDE
----------------

- Für das Projekt empfehlen wir **Visual Studio Code**, **PyCharm** oder **Thonny**.
- Achtet darauf, dass in der IDE auch die richtige Python-Umgebung (virtuell oder systemweit) ausgewählt ist.

Tests und erste Ausführung
--------------------------

Nach der Installation könnt ihr prüfen, ob das Projekt lauffähig ist:

1. Startet Python:

   .. code-block:: bash

      python

2. Importiert eine Beispielklasse:

   .. code-block:: python

      from board import Board
      b = Board()
      print(b)

3. Beendet Python mit `exit()` oder `Strg + D`.

Fehlerbehandlung
----------------

- Falls `ModuleNotFoundError` auftaucht, überprüft:
  - Ist die virtuelle Umgebung aktiviert?
  - Wurde das Paket korrekt installiert?

- Bei Problemen mit `numpy`: Aktualisiert pip:

  .. code-block:: bash

     python -m pip install --upgrade pip

Ausführen der automatischen Tests
=================================

Um eure Implementierungen systematisch zu überprüfen, steht eine **Testsuite** zur Verfügung, die alle zentralen Methoden mit automatisierten **Unit-Tests** abdeckt.

Diese Tests prüfen, ob ihr die `TODO`-Methoden korrekt umgesetzt habt – einschließlich Funktionalität, Rückgabewerte, und in vielen Fällen auch Randbedingungen. Sie liefern möglichst aussagekräftige Fehlermeldungen, um euch gezielt bei der Fehlersuche zu unterstützen.

Testausführung
--------------

Sobald ihr eine oder mehrere Methoden implementiert habt, könnt ihr die Tests jederzeit ausführen:

.. code-block:: bash

   python tests.py

Dabei wird eine Reihe vordefinierter Tests durchlaufen, die auf allen Ebenen des Projekts ansetzen – von einfachen Gültigkeitsprüfungen (`is_valid_cell`) bis hin zur korrekten Funktionsweise des Mini-Max-Algorithmus.

Testausgabe interpretieren
--------------------------

- **Erfolgreicher Test**:
Nachdem alle Methoden korrekt implementiert wurden laufen die Tests ohne Fehlermeldung durch:

  .. code-block::

    python tests.py

    ...................
    ----------------------------------------------------------------------
    Ran 19 tests in 1.755s

    OK

- **Fehlgeschlagener Test**:
Ist eure Implementierung fehlerhaft oder unvollständig, erhaltet ihr eine
möglichst sprechende Beschreibung des Fehlers.

  .. code-block::

    python tests.py

    ............
    Testcase name:  Queen Movement Rules
    Movability wrongly implemented. In this configuration

            8 . . . . . . . .
            7 . . . . . . . .
            6 . . . . . . . .
            5 . r . Q . . K .
            4 . . . . . . . .
            3 . . . . . . . .
            2 . . q . . . k .
            1 . . . . . . . .
              a b c d e f g h

    Queen on c2 (red) should be able to move to b2 (green).

In diesem Fall wird euch (wenn sinnvoll) eine Erklärung mitgegeben, **warum der Test fehlgeschlagen ist** – etwa welche Eingabewerte verwendet wurden und was erwartet wurde.

Testabdeckung
-------------

Die Tests decken alle Methoden ab, die ihr gemäß Anleitung selbst implementieren müsst, darunter u. a.:


