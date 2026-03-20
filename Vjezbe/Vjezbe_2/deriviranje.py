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


x1, y1_three = calculus.raspon(f1, x_min, x_max, epsilon=epsilon, metoda="three-step")
x1, y1_two   = calculus.raspon(f1, x_min, x_max, epsilon=epsilon, metoda="two-step")

x2, y2_three = calculus.raspon(f2, x_min, x_max, epsilon=epsilon, metoda="three-step")
x2, y2_two   = calculus.raspon(f2, x_min, x_max, epsilon=epsilon, metoda="two-step")

y_anal1 = dt1(x1)
y_anal2 = dt2(x2)

plt.figure(figsize=(12,12))
plt.subplot(2,1,1)
plt.plot(x1, y_anal1, label="Analitičko", linewidth=2)
plt.plot(x1, y1_three, '--', label="Three-step")
plt.plot(x1, y1_two, ':', label="Two-step")
plt.title("Derivacija x^3")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.legend()
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(x2, y_anal2, label="Analitičko", linewidth=2)
plt.plot(x2, y2_three, '--', label="Three-step")
plt.plot(x2, y2_two, ':', label="Two-step")
plt.title("Derivacija sin(x)")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.legend()
plt.grid(True)

plt.show