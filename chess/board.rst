Die Board-Klasse zur Repräsentation des Schachbretts
=================================================================

Die `Board`-Klasse bildet das Herzstück des Schachprojekts. Sie stellt eine flexible und erweiterbare Datenstruktur dar, mit der sich **Schachstellungen speichern, verändern, bewerten und analysieren** lassen. Die Klasse ist in zwei Ebenen aufgebaut: eine abstrakte Basisklasse (`BoardBase`) mit grundlegender Funktionalität und eine erweiterte Implementierung (`Board`), in der zentrale Methoden von den Studierenden selbst implementiert werden.

Ziel ist es, ein realistisch spielbares Schachbrett in Python zu modellieren, das als Grundlage für weiterführende KI-Algorithmen wie **Mini-Max** dient. Dabei übernimmt die `Board`-Klasse nicht nur das Verwalten der Figurenpositionen, sondern bietet auch Methoden zur Bewertung der Stellung, zur Validierung von Zügen sowie zur Erkennung kritischer Spielsituationen wie Schach.

Funktionalität im Überblick
---------------------------

Die Klasse erlaubt unter anderem folgende Operationen:

- **Initialisierung und Zurücksetzen** eines vollständigen Startbretts (:py:meth:`reset <board.BoardBase.reset>`)
- **Einfügen, Entfernen und Überprüfen** von Figuren auf bestimmten Feldern (:py:meth:`set_cell <board.BoardBase.set_cell>`, :py:meth:`get_cell <board.BoardBase.get_cell>`)
- **Serialisierung** der Stellung zur Anzeige oder Speicherung (:py:meth:`__str__ <board.BoardBase.__str__>`, :py:meth:`hash <board.BoardBase.hash>`, :py:meth:`save_to_disk <board.BoardBase.save_to_disk>`, :py:meth:`load_from_disk <board.BoardBase.load_from_disk>`)
- **Bewertung** der aktuellen Stellung aus Sicht von Weiß (:py:meth:`evaluate <board.Board.evaluate>`)
- **Erkennung von Schach**-Situationen mittels gegnerischer Angriffsreichweiten (:py:meth:`is_king_check <board.Board.is_king_check>`)
- **Zugvalidierung**, etwa ob ein Feld betreten oder angegriffen werden darf (:py:meth:`piece_can_enter_cell <board.Board.piece_can_enter_cell>`, :py:meth:`piece_can_hit_on_cell <board.Board.piece_can_hit_on_cell>`)
- **Iteration über Spielfiguren** nach Farbe (:py:meth:`iterate_cells_with_pieces <board.Board.iterate_cells_with_pieces>`)
- **Laden von Stellungen** aus Strings (z. B. für Spielwiederherstellung oder Tests)

Modularer Aufbau und Erweiterbarkeit
------------------------------------

Die Klasse wurde so entworfen, dass sie sowohl als eigenständiges Brettmodell als auch als Baustein für **Schach-KI-Algorithmen** dient. Insbesondere ermöglicht sie es, die Spiellogik klar von der Bewertungslogik und der KI-Strategie zu trennen. Dadurch können später Suchalgorithmen wie Mini-Max oder Alpha-Beta-Pruning problemlos auf dieser Basis aufbauen.

Die `Board`-Klasse dient somit als zentrales Bindeglied zwischen Spiellogik, Benutzeroberfläche und KI – und ist damit ein essenzieller Bestandteil eures Schachcomputers.

.. _reference_board:

Reference - Board
-----------------

.. autoclass:: board::Board
   :members:
   :undoc-members:

Reference - Base Board
----------------------

.. autoclass:: board::BoardBase
   :members:
