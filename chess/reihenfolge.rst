Implementierungsreihenfolge der TODO-Methoden
=============================================

Um den Schachcomputer schrittweise aufzubauen, sollten die mit ``TODO`` markierten Methoden in einer sinnvollen Reihenfolge bearbeitet werden. Diese Seite hilft euch dabei, eine logische Abfolge zu wählen – **von einfachen, unabhängigen Funktionen** bis hin zu **komplexeren, zusammengesetzten Logiken** wie Mini-Max.

Phase 1: Grundlagen im Board-Modul
----------------------------------

Beginnt mit den Methoden, die einfache Prüfungen und Datenzugriffe betreffen:

1. :py:meth:`is_valid_cell() <board.Board.is_valid_cell>`
   - Prüft, ob eine Zelle im gültigen Bereich des Schachbretts liegt.
   - Grundlage fast aller weiteren Bewegungsfunktionen.

2. :py:meth:`cell_is_valid_and_empty() <board.Board.cell_is_valid_and_empty>`
   - Liefert `True`, wenn eine gültige Zelle leer ist.
   - Baut direkt auf `is_valid_cell()` auf.

3. :py:meth:`piece_can_enter_cell(piece, cell) <board.Board.piece_can_enter_cell>`
   - Prüft, ob eine Figur ein Feld betreten darf (leer oder Gegner).
   - Wichtig für Bewegung und Schlagmechaniken.

4. :py:meth:`piece_can_hit_on_cell(piece, cell) <board.Board.piece_can_hit_on_cell>`
   - Prüft, ob eine Figur eine gegnerische Figur auf dem Ziel schlagen kann.

Diese Funktionen müssen **zuerst** korrekt funktionieren, da sie in fast allen Figurenmethoden wiederverwendet werden.

Phase 2: Bewegungsregeln der Figuren
------------------------------------

Im nächsten Schritt implementiert ihr die `get_reachable_cells()`-Methoden jeder Figur. Diese bilden das Fundament für mögliche Züge:

5. :py:meth:`Pawn.get_reachable_cells() <pieces.Pawn.get_reachable_cells>`
6. :py:meth:`Rook.get_reachable_cells() <pieces.Rook.get_reachable_cells>`
7. :py:meth:`Knight.get_reachable_cells() <pieces.Knight.get_reachable_cells>`
8. :py:meth:`Bishop.get_reachable_cells() <pieces.Bishop.get_reachable_cells>`
9. :py:meth:`Queen.get_reachable_cells() <pieces.Queen.get_reachable_cells>`
10. :py:meth:`King.get_reachable_cells() <pieces.King.get_reachable_cells>`

Diese Methoden müssen **nicht prüfen**, ob der eigene König danach im Schach steht – das übernimmt später :py:meth:`get_valid_cells() <pieces.Piece.get_valid_cells>`.

Phase 3: Figurenlogik und Spielfluss
------------------------------------

11. :py:meth:`Piece.get_valid_cells() <pieces.Piece.get_valid_cells>`
    - Kombiniert :py:meth:`get_reachable_cells <pieces.Piece.get_reachable_cells>` mit einer Prüfung auf Schach.
    - Nutzt temporäres Umplatzieren auf dem Brett.
    - **Komplexität**: mittel bis hoch, da Zustand zwischengespeichert und wiederhergestellt werden muss.

12. :py:meth:`Board.iterate_cells_with_pieces() <board.Board.iterate_cells_with_pieces>`    - Generator für alle Figuren einer Farbe.
    - Wird für Bewertung und Mini-Max benötigt.

13. :py:meth:`Board.find_king() <board.Board.find_king>`
    - Sucht die Königsfigur einer bestimmten Farbe.
    - Grundlage für Schachprüfung.

14. :py:meth:`Board.is_king_check() <board.Board.is_king_check>`
    - Prüft, ob ein König im Schach steht.
    - Nutzt vorherige Methoden für Gegnerreichweiten.

Phase 4: Bewertung und KI
--------------------------

15. :py:meth:`Piece.evaluate() <pieces.Piece.evaluate>`
    - Bewertet die Stellung einer einzelnen Figur.
    - Nutzt z. B. Anzahl gültiger Züge, Bedrohungen etc.

16. :py:meth:`Board.evaluate() <board.Board.evaluate>`
    - Aggregiert alle Bewertungen weißer und schwarzer Figuren.
    - Gibt eine numerische Bewertung der Gesamtstellung zurück.

Phase 5: Mini-Max-Logik
-----------------------

17. :py:meth:`evaluate_all_possible_moves() <engine.evaluate_all_possible_moves>`
    - Erzeugt und bewertet alle möglichen Züge einer Farbe.
    - Nutzt fast alle vorhergehenden Methoden.

18. :py:meth:`minMax() <engine.minMax>`
    - Der rekursive Mini-Max-Algorithmus.
    - Komplexität hoch, rekursiv, mit Zustandsänderung.

Überblick
---------

.. mermaid::

   graph TD
       step1[is_valid_cell] --> step2[cell_is_valid_and_empty]
       step2 --> step3[piece_can_enter_cell]
       step2 --> step4[piece_can_hit_on_cell]

       step3 --> pawnReach[Pawn.get_reachable_cells]
       step3 --> rookReach[Rook.get_reachable_cells]
       step3 --> knightReach[Knight.get_reachable_cells]
       step3 --> bishopReach[Bishop.get_reachable_cells]
       step3 --> queenReach[Queen.get_reachable_cells]
       step3 --> kingReach[King.get_reachable_cells]

       pawnReach --> validCells[get_valid_cells]
       rookReach --> validCells
       knightReach --> validCells
       bishopReach --> validCells
       queenReach --> validCells
       kingReach --> validCells

       validCells --> iterate[iterate_cells_with_pieces]
       iterate --> findKing[find_king]
       findKing --> isCheck[is_king_check]

       isCheck --> evalPiece[Piece.evaluate]
       evalPiece --> evalBoard[Board.evaluate]

       evalBoard --> moveEval[evaluate_all_possible_moves]
       moveEval --> miniMax[minMax]


Zusätzliche Hinweise
--------------------

- Fangt **nicht mitten in der Mini-Max-Logik** an, wenn die Bewegungs- und Prüfmethoden noch nicht korrekt funktionieren.
- Testet jede Methode **isoliert**, bevor ihr sie in größere Strukturen einbaut.
- Nutzt Zwischenausgaben (`print()`) und einfache Testszenarien, um eure Implementierung schrittweise zu verifizieren.

