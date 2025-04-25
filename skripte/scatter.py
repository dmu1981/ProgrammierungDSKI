import matplotlib.pyplot as plt
import numpy as np

# Daten
werbung = [5, 7, 8, 4, 6, 9, 10, 6.5]
preis = [15, 14, 13, 16, 14, 13, 12, 13.5]
verkaeufe = [100, 220, 260, 180, 210, 290, 450, 250]  # bestimmt die Punktgröße
kategorie = ["A", "B", "A", "B", "A", "C", "C", "B"]

# Farben zuweisen
farben_map = {"A": "blue", "B": "green", "C": "red"}
farben = [farben_map[k] for k in kategorie]

# Punktgrößen skalieren
sizes = [v * 0.8 for v in verkaeufe]

# Scatter Plot
plt.figure(figsize=(8, 6))
scatter = plt.scatter(werbung, preis, s=sizes, c=farben, alpha=0.7, edgecolors="black")

plt.xlabel("Werbebudget (Tsd. €)")
plt.ylabel("Verkaufspreis (€)")
plt.title("Verkaufsanalyse: Werbung vs. Preis")

# Legende manuell erzeugen
from matplotlib.lines import Line2D
legende = [Line2D([0], [0], marker='o', color='w', label='Kategorie A',
                  markerfacecolor='blue', markersize=10, markeredgecolor='black'),
           Line2D([0], [0], marker='o', color='w', label='Kategorie B',
                  markerfacecolor='green', markersize=10, markeredgecolor='black'),
           Line2D([0], [0], marker='o', color='w', label='Kategorie C',
                  markerfacecolor='red', markersize=10, markeredgecolor='black')]

plt.legend(handles=legende, title="Produktkategorie")
plt.grid(True)
plt.tight_layout()
plt.show()
