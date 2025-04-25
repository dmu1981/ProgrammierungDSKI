import matplotlib.pyplot as plt
import numpy as np

labels = ["Produkt A", "Produkt B", "Produkt C"]
werte = [40, 35, 25]

plt.pie(werte, labels=labels, autopct="%1.1f%%", colors=["#66b3ff", "#99ff99", "#ffcc99"])
plt.title("Marktanteile")
plt.axis("equal")  # sorgt für runde Torte
plt.tight_layout()
plt.show()