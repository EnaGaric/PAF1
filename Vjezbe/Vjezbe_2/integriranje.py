import numpy as np
import matplotlib.pyplot as plt
import calculus

def f(x):
    return np.sin(5*x) + 0.5*x

a = 0
b = 2
n = 4

if a > b:
    a, b = b, a


#integrali
donja_granica, gornja_granica = calculus.pravokutna_aproksimacija(f, a, b, n)
pravokutna_srednja = (donja_granica + gornja_granica)/2
trap = calculus.trapezna_metoda(f, a, b, n)

# analitičko rješenje
analiticko = calculus.trapezna_metoda(f, a, b, 10000)


print("\nRezultati:")
print(f"Donja međa: {donja_granica:.2f}")
print(f"Gornja međa: {gornja_granica:.2f}")
print(f"Pravokutna metoda: {pravokutna_srednja:.2f}")
print(f"Trapezna metoda: {trap:.2f}")
print(f"Točno rješenje je: {analiticko:.2f}")

# Brojevi podjela za usporedbu
n_values = [2, 4, 8, 16]  # manje n da se vidi razlika
pravokutna = []
trapezna = []

x = np.linspace(a, b, 100)
plt.figure(figsize=(12,5))

for nn in n_values:
    d, g = calculus.pravokutna_aproksimacija(f, a, b, nn)
    pravokutna.append(d) 
    trapezna.append(calculus.trapezna_metoda(f, a, b, nn))


plt.subplot(2,2,1)
plt.plot(x, f(x), color='blue', label='f(x)')
plt.title("Funkcija f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()


# subplot 1: pravokutna metoda
plt.subplot(2,2,2)
plt.plot(n_values, pravokutna, 'o--', color='red', markersize=8, label="Pravokutna metoda")
plt.axhline(analiticko, linestyle=':', color='blue', label="Analitičko rješenje")
plt.title("Pravokutna metoda")
plt.xlabel("Broj podjela n")
plt.ylabel("Vrijednost integrala")
plt.legend()

# subplot 2: trapezna metoda
plt.subplot(2,2,3)
plt.plot(n_values, trapezna, 's-', color='green', markersize=8, label="Trapezna metoda")
plt.axhline(analiticko, linestyle=':', color='blue', label="Analitičko rješenje")
plt.title("Trapezna metoda")
plt.xlabel("Broj podjela n")
plt.ylabel("Vrijednost integrala")
plt.legend()

plt.subplot(2,2,4)
plt.plot(n_values, pravokutna, 'o--', color='red', markersize=8, label="Pravokutna metoda")
plt.plot(n_values, trapezna, 's-', color='green', markersize=8, label="Trapezna metoda")
plt.axhline(analiticko, linestyle=':', color='blue', label="Analitičko rješenje")
plt.title("Usporedba metoda")
plt.xlabel("Broj podjela n")
plt.ylabel("Vrijednost integrala")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()