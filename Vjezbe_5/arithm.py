import numpy as np

x = []

for i in range(10):
    xi = float(input("Unesi točke: "))
    x.append(xi)

x = np.array(x)
n = len(x)

# (1) aritmetička sredina
x_crtica = np.sum(x) / n

# (2) standardna devijacija po zadanoj formuli
sigma = np.sqrt(np.sum((x - x_crtica) ** 2) / (n * (n - 1)))

print("Sredina:", x_crtica)
print("Std dev:", sigma)