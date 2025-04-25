import matplotlib.pyplot as plt
import numpy as np

daten = np.random.normal(loc=0, scale=1, size=1000)

plt.hist(daten, bins=20, color="skyblue", edgecolor="black")
plt.title("Histogramm einer Normalverteilung")
plt.xlabel("Wert")
plt.ylabel("Häufigkeit")
plt.grid(True)
plt.tight_layout()
plt.show()