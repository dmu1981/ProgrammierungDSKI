Einleitung: Bau eines einfachen Schachcomputers mit Mini-Max
=============================================================

Stellt euch vor, ihr könntet einem Computer das Schachspielen beibringen – so, dass er selbstständig Züge macht, dabei plant und sogar gegnerische Absichten „voraussieht“. Genau das ist das Ziel dieses Projekts: Ihr entwickelt euren eigenen Schachcomputer, der mithilfe eines einfachen, aber wirkungsvollen Entscheidungsverfahrens spielt – dem sogenannten **Mini-Max-Algorithmus**.

Der Mini-Max-Algorithmus stammt aus der Welt der Spieltheorie und hilft dem Computer dabei, Entscheidungen zu treffen, die langfristig zu einem Vorteil führen. Er betrachtet abwechselnd eigene und gegnerische Züge und bewertet die entstehenden Spielsituationen. Ziel ist es, **den besten eigenen Zug** zu finden, indem man davon ausgeht, dass der Gegner ebenfalls **immer den besten möglichen Zug** machen wird.

Dabei geht es nicht darum, gleich einen Weltklasse-Computer wie Stockfish zu bauen. Vielmehr lernt ihr die grundlegenden Ideen kennen, die hinter künstlicher Intelligenz in Spielen stecken: systematisches Durchsuchen von Möglichkeiten, Bewertung von Positionen und strategisches Vorausplanen.

Am Ende habt ihr einen einfachen, aber funktionierenden Schach-Bot, der mit euch (oder gegeneinander) Partien spielen kann – ganz aus eigener Umsetzung.

Mini-Max-Algorithmus im Detail
==============================

Grundidee
---------

Der Mini-Max-Algorithmus ist ein rekursives Verfahren zur Entscheidungsfindung in Zwei-Spieler-Nullsummenspielen wie Schach. Der Algorithmus basiert auf der Annahme, dass beide Spieler **optimal** spielen – das heißt, jeder versucht, seinen eigenen Nutzen zu maximieren und den des Gegners zu minimieren.

Im Kontext eines Schachcomputers bedeutet das: Der eigene Zug (Maximierer) wird so gewählt, dass der schlechtestmögliche Gegenzug (Minimierer) noch zu einem relativ guten Ergebnis führt.

Rekursive Struktur
------------------

Der Mini-Max-Algorithmus durchsucht den Spielbaum bis zu einer bestimmten **Suchtiefe** und bewertet die entstehenden Stellungen mit einer **Bewertungsfunktion**. Danach propagiert er die Bewertungen zurück nach oben, wobei auf jeder Ebene je nach Spielerrolle der maximale oder minimale Wert weitergegeben wird.

Der Ablauf sieht folgendermaßen aus:

1. **Generiere alle legalen Züge** für die aktuelle Stellung.
2. **Simuliere** jeden Zug und rufe rekursiv Mini-Max für den entstehenden Zustand auf.
3. Wenn die maximale Tiefe erreicht ist oder das Spiel vorbei ist:
   - **Bewerte** die Stellung numerisch (z. B. Material, Stellungsvorteile).
4. Der **Maximierer** (z. B. Weiß) wählt den Zug mit dem **höchsten Bewertungswert**.
5. Der **Minimierer** (z. B. Schwarz) wählt den Zug mit dem **niedrigsten Bewertungswert**.

Bewertungsfunktion
------------------

Eine einfache Bewertungsfunktion kann auf der **Materialverteilung** basieren:

- Bauer = 1 Punkt
- Springer / Läufer = 3 Punkte
- Turm = 5 Punkte
- Dame = 9 Punkte
- König = ∞ (oder sehr hoher Wert)

Diese Funktion kann durch **Positionsboni** (z. B. Zentrumskontrolle, Entwicklung, Königssicherheit) ergänzt werden.

