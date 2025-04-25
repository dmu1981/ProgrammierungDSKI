import matplotlib.pyplot as plt
import numpy as np

werte = np.stack([
    np.random.normal(100, 20, 200),
    np.random.normal(80, 15, 200),
    np.random.normal(120, 30, 200),
], axis=1)


plt.boxplot(werte, vert=True, patch_artist=True)
plt.title("Boxplot Beispiel")
plt.xlabel("Wert")
plt.grid(True)
plt.tight_layout()
plt.show()