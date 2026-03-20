import calculus
import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return x**3

def f2(x):
    return np.sin(x)

def dt1(x):
    return 3 * x**2

def dt2(x):
    return np.cos(x)

print("Unos korisnika:\n")
x_min = float(input("Unesi donju granicu: \n"))
x_max = float(input("Unesi gornju granicu: \n"))
epsilon = float(input("Unesi veličinu koraka (npr. 0.1 ili 0.01): "))


x, y_three = calculus.raspon(f1, x_min, x_max, epsilon=epsilon, metoda="three-step")
x, y_two   = calculus.raspon(f1, x_min, x_max, epsilon=epsilon, metoda="two-step")

y_anal = dt1(x)

plt.plot(x, y_anal, label="Analitičko rješenje", linewidth=2)
plt.plot(x, y_three, '--', label=f"Three_step eps={epsilon}")
plt.plot(x, y_two, ':', label=f"Two_step eps={epsilon}")

plt.title("Derivacija funkcije x^3")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.legend()
plt.grid(True)
plt.show()