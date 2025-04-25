import numpy as np
from matplotlib import pyplot as plt

print(plt.style.available)
plt.style.use("dark_background")

potenzen = np.array([0.5, 0.75, 1.0, 1.5, 2.0])
x = np.linspace(0, 1, 250)
for potenz in potenzen:
    y = np.power(x, potenz)
    plt.plot(x, y)

plt.legend(potenzen)    
plt.xlabel("x")
plt.ylabel("y")
plt.title("Potenzen $y=x^n$")
plt.show()

