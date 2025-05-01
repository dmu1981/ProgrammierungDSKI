Einleitung: Objektorientierte Modellierung der Schachfiguren 
=============================================================

Die Spielmechanik der einzelnen Schachfiguren ist über eine allgemeine Klasse :ref:`Piece <reference_piece>` sowie spezialisierte Klasse 
:ref:`King <reference_king>`, :ref:`Queen <reference_queen>`, :ref:`Rook <reference_rook>`, :ref:`Knight <reference_knight>`,
:ref:`Bishop <reference_bishop>` und :ref:`Pawn <reference_pawn>` abgebildet. 


Im Zentrum jeder Schach-KI steht die Fähigkeit, die Regeln der einzelnen Figuren korrekt umzusetzen. In dieser Datei werden die sechs grundlegenden **Schachfigurenklassen** – `Pawn`, `Rook`, `Knight`, `Bishop`, `Queen`, `King` – zusammen mit einer gemeinsamen abstrakten Basisklasse `Piece` implementiert. Ziel ist es, jede Figur mit ihren **bewegungsspezifischen Regeln**, einer **Bewertungsfunktion** und einer strukturierten Schnittstelle zur Interaktion mit dem Spielbrett auszustatten.

Diese Klassen bilden die Grundlage für die Spiellogik, die Bewertung der Spielsituationen sowie für das spätere **Mini-Max-gestützte Entscheidungsverhalten** eures Schachcomputers.

Objektorientierter Aufbau
-------------------------

Alle Figuren erben von der Klasse `Piece`, welche gemeinsame Funktionalitäten kapselt:

- Referenz zum aktuellen **Brett** und zur **Position** der Figur
- Informationen über die **Farbe** (weiß oder schwarz)
- Ein universelles Interface für **Bewertung** (:py:meth:`evaluate <pieces.Piece.evaluate>`) und die Ermittlung **gültiger Züge** (:py:meth:`get_valid_cells <pieces.Piece.get_valid_cells>`)

Jede abgeleitete Klasse (`Pawn`, `Rook`, `Knight` etc.) implementiert ihre eigene **`get_reachable_cells()`**-Methode, um die figurenspezifische Bewegungslogik zu definieren.

Intelligente Bewertung
----------------------

Die `evaluate()`-Methode quantifiziert den Wert einer Figur auf dem Brett. Neben einem **Basiswert** (z. B. 1 für einen Bauern, 9 für eine Dame) berücksichtigt sie zusätzliche Heuristiken wie:

- **Mobilität**: Wie viele Züge sind möglich?
- **Bedrohungspotential**: Welche gegnerischen Figuren können geschlagen werden?
- **Taktische Vorteile** wie Gabeln (mehrere Bedrohungen gleichzeitig)

Dadurch entsteht eine feinjustierte Bewertungsgrundlage für den Mini-Max-Algorithmus, die über bloße Materialzählung hinausgeht.

Gültige Züge und Regelkonformität
---------------------------------

Während die `get_reachable_cells()`-Methoden ausschließlich die **potenziellen Bewegungsmöglichkeiten** der jeweiligen Figur auf Basis der Schachregeln berechnen, filtert `get_valid_cells()` diese Liste durch eine **Sicherheitsprüfung**: Nur Züge, die den eigenen König nicht ins Schach bringen, werden als gültig markiert. Diese Trennung erlaubt sowohl einfache Tests der Bewegung als auch regelkonformes Spielverhalten.

Fazit
-----

Die modellierten Figurenklassen sind ein essenzielles Bindeglied zwischen statischer Brettlogik und dynamischer Spielentscheidung. Sie ermöglichen eine **regelkonforme, bewertbare und erweiterbare** Darstellung der Spielfiguren – und bilden damit den Kern eines funktionsfähigen Schachcomputers.


.. _reference_piece:

Reference - Piece
-----------------

.. autoclass:: pieces::Piece
   :members:

.. _reference_king:

Reference - King
----------------


.. autoclass:: pieces::King
   :members:

.. _reference_queen:

Reference - Queen
-----------------

.. autoclass:: pieces::Queen
   :members:   

.. _reference_rook:

Reference - Rook
----------------

.. autoclass:: pieces::Rook
   :members:   

.. _reference_knight:

Reference - Knight
------------------

.. autoclass:: pieces::Knight
   :members:   

.. _reference_bishop:

Reference - Bishop
------------------

.. autoclass:: pieces::Bishop
   :members:   

.. _reference_pawn:

Reference - Pawn
----------------

.. autoclass:: pieces::Pawn
   :members:   