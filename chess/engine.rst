Die Schachengine
================

Die eigentliche Schachengine ist in der Datei engine.py implementiert. Diese besteht auf zwei Hilfsklassen (:py:class:`engine.MinMaxArg` sowie 
:py:class:`engine.Move`) sowie den zwei Kernmethoden des Mini-Max Algorithmus  (:py:func:`engine.evaluate_all_possible_moves` und 
:py:func:`engine.minMax`)

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

