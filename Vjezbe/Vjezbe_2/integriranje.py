import numpy as np
import matplotlib.pyplot as plt
import calculus



def f(x):
    return 2*x**2 + 3

a = 0
b = 1

# "točno" rješenje (numerički jako precizno)
analiticko = calculus.trapezna_metoda(f, a, b, 10000)

# brojevi podjela
n_values = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900]

donje = []
gornje = []
trapezna = []



for n in n_values:
    d, g = calculus.pravokutna_aproksimacija(f, a, b, n)
    donje.append(d)
    gornje.append(g)
    trapezna.append(calculus.trapezna_metoda(f, a, b, n))



plt.figure()

plt.plot(n_values, gornje, 'o', label="Gornja međa")
plt.plot(n_values, donje, 'o', label="Donja međa")
plt.plot(n_values, trapezna, 'o', label="Trapezna metoda")

plt.axhline(analiticko, linestyle='-', label="Analitičko rješenje")

plt.xlabel("N steps")
plt.ylabel("Integral")
plt.title("Numerička integracija: f(x)=2x²+3")

plt.legend()
plt.grid(True)

plt.show()