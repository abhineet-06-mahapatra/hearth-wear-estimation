import numpy as np, scipy, pandas as pd, sklearn
import matplotlib.pyplot as plt

print("NumPy:", np.__version__)
print("SciPy:", scipy.__version__)
print("pandas:", pd.__version__)
print("scikit-learn:", sklearn.__version__)

x = np.linspace(0, 1.0, 50)
T = 1500 - 1200 * x
plt.plot(x, T)
plt.xlabel("Distance from hot face (m)")
plt.ylabel("Temperature (°C)")
plt.title("Test plot: wall temperature profile")
plt.grid(True)
plt.show()