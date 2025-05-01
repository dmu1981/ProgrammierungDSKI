Die Schachengine mit Mini-Max-Suche
===================================

Die hier implementierte **Schachengine** stellt das zentrale Modul zur automatisierten Entscheidungsfindung in eurem Schachcomputer dar. Sie basiert auf dem klassischen **Mini-Max-Algorithmus**, einem fundamentalen Konzept der Spieltheorie, das systematisch nach dem optimalen Zug für eine Spielfigur sucht. Dabei geht der Algorithmus davon aus, dass sowohl der eigene als auch der gegnerische Spieler stets rational und optimal agieren.

Ziel ist es, für jede gegebene Spielsituation den bestmöglichen Zug zu finden – und zwar unter Einbezug der **potenziellen Antworten des Gegners**. Dies geschieht rekursiv, indem der Spielbaum bis zu einer konfigurierbaren Tiefe durchsucht wird.

Struktur und Komponenten
------------------------

Die Engine setzt sich aus mehreren Schlüsselkomponenten zusammen:

- :py:class:`MinMaxArg <engine.MinMaxArg>`: Kapselt die aktuelle Suchtiefe und die Spielerfarbe (weiß oder schwarz). Dient als Steuerstruktur für den rekursiven Ablauf der Suche.
- :py:class:`Move <engine.Move>`: Repräsentiert einen möglichen Zug samt zugehöriger Bewertung (Score). Wird zur Ergebnisübermittlung und Anzeige genutzt.
- :py:func:`evaluate_all_possible_moves <engine.evaluate_all_possible_moves>`: Bewertet alle legalen Züge für die aktuelle Farbe auf Basis der `evaluate()`-Funktion des Bretts. Simuliert jeden Zug temporär, analysiert die Stellung und verwirft sie danach wieder.
- :py:func:`minMax <engine.minMax>`: Kern des rekursiven Mini-Max-Algorithmus. Er simuliert eigene Züge und prüft rekursiv die besten Antworten des Gegners, um daraus den besten Gesamtzug abzuleiten.
- :py:func:`minMax_cached <engine.minMax_cached>`: Erweiterung des Standard-Mini-Max mit **Caching**. Doppelte Berechnungen identischer Spielstellungen werden vermieden, was zu erheblichen Performancegewinnen führt.
- :py:func:`suggest_move <engine.suggest_move>`: Einstiegspunkt für die Engine. Startet den Suchprozess und liefert einen spielbaren Zug zurück.

Algorithmische Idee
-------------------

Das Grundprinzip des Mini-Max-Algorithmus ist einfach, aber wirkungsvoll:

1. **Simulation**: Für jeden legalen Zug wird der resultierende Spielzustand simuliert.
2. **Rekursion**: Der Gegnerzug wird rekursiv ebenfalls mit Mini-Max simuliert.
3. **Bewertung**: Die resultierenden Stellungen werden numerisch bewertet (immer aus Sicht von Weiß).
4. **Auswahl**: Der Zug, der langfristig zur besten Bewertung führt, wird zurückgegeben.

Dabei wird zwischen zwei Modi unterschieden:

- **Maximierer** (z. B. Weiß): Wählt den Zug mit dem höchsten Score.
- **Minimierer** (z. B. Schwarz): Wählt den Zug mit dem niedrigsten Score.

Die Bewertung basiert auf der `Board.evaluate()`-Funktion, welche das Material, Mobilität und taktische Motive (z. B. Bedrohungen) berücksichtigt.

Leistungsoptimierung
--------------------

Um den hohen Rechenaufwand zu reduzieren, implementiert die Engine ein **Hash-basiertes Caching**: Spielstellungen werden eindeutig identifiziert und einmal berechnete Bewertungen gespeichert. So lassen sich insbesondere in tieferen Suchtiefen erhebliche **Performancegewinne** erzielen.

Außerdem werden in der letzten Phase der Suche **zufällige Elemente** eingeführt, um die Vorhersagbarkeit zu verringern und die Spielvielfalt zu erhöhen (z. B. Zufallsauswahl aus gleichwertigen Top-Zügen).

Fazit
-----

Diese Schachengine bietet eine robuste, nachvollziehbare und erweiterbare Grundlage für KI-gesteuertes Schachspiel. Sie verbindet algorithmische Eleganz mit praktischer Spielstärke – und bildet damit den **entscheidenden Baustein** für euren eigenen Schachcomputer.

Die Kern-Methoden der Engine
----------------------------

.. autofunction:: engine::evaluate_all_possible_moves
  
.. autofunction:: engine::minMax

.. _reference_MinMaxArg:

Reference - MinMaxArg
---------------------

.. autoclass:: engine::MinMaxArg
   :members:


.. _reference_Move:

Reference - Move
---------------------

.. autoclass:: engine::Move
   :members:

Hilfsmethoden
-------------

.. autofunction:: engine::minMax_cached
.. autofunction:: engine::suggest_move