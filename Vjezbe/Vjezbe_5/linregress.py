import numpy as np
import matplotlib.pyplot as plt

# podaci
M = np.array([0.052, 0.124, 0.168, 0.236, 0.284, 0.336])
phi = np.array([0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472])

n = len(M)

# regresija kroz ishodište
Dt = np.sum(phi * M) / np.sum(phi ** 2)

# standardna devijacija
sigma_Dt = np.sqrt((1/n) * (np.sum(M ** 2) / np.sum(phi ** 2) - Dt ** 2))

print("Dt =", Dt)
print("σDt =", sigma_Dt)




phi_line = np.linspace(0, max(phi), 100)
M_fit = Dt * phi_line

plt.scatter(phi, M, label="mjerenja")
plt.plot(phi_line, M_fit, 'r', label="fit: M = Dt·φ")

plt.xlabel("φ (rad)")
plt.ylabel("M (Nm)")
plt.legend()
plt.show()