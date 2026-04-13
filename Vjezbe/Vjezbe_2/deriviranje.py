import calculus
import numpy as np
import matplotlib.pyplot as plt

# =========================
# FUNKCIJE
# =========================

def f1(x):
    return x**3

def f2(x):
    return np.sin(x)

# analitičke derivacije
def dt1(x):
    return 3 * x**2

def dt2(x):
    return np.cos(x)

# =========================
# UNOS
# =========================

print("Unos korisnika:\n")
x_min = float(input("Unesi donju granicu: \n"))
x_max = float(input("Unesi gornju granicu: \n"))
epsilon = float(input("Unesi veličinu koraka (npr. 0.5, 0.1, 0.01): "))

# =========================
# NUMERIČKA DERIVACIJA
# =========================

x1, y1_three = calculus.raspon(f1, x_min, x_max, epsilon=epsilon, metoda="three-step")
_,  y1_two   = calculus.raspon(f1, x_min, x_max, epsilon=epsilon, metoda="two-step")

x2, y2_three = calculus.raspon(f2, x_min, x_max, epsilon=epsilon, metoda="three-step")
_,  y2_two   = calculus.raspon(f2, x_min, x_max, epsilon=epsilon, metoda="two-step")

# analitičko
y_anal1 = dt1(x1)
y_anal2 = dt2(x2)

# =========================
# GRAF DERIVACIJA
# =========================

plt.figure(figsize=(12,12))

# x^3
plt.subplot(2,1,1)
plt.plot(x1, y_anal1, color='black', linewidth=2, label="Analitičko rješenje")
plt.plot(x1, y1_three, '--', color='red', label="Numerički (three-step)")
plt.plot(x1, y1_two, ':', color='blue', label="Numerički (two-step)")
plt.title("Derivacija funkcije f(x) = x^3 → prikaz f'(x)")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.legend()
plt.grid(True)

# sin(x)
plt.subplot(2,1,2)
plt.plot(x2, y_anal2, color='black', linewidth=2, label="Analitičko rješenje")
plt.plot(x2, y2_three, '--', color='red', label="Numerički (three-step)")
plt.plot(x2, y2_two, ':', color='blue', label="Numerički (two-step)")
plt.title("Derivacija funkcije f(x) = sin(x) → prikaz f'(x)")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.legend()
plt.grid(True)

plt.show()


# =========================
# GRAF POGREŠKE (BITNO!!)
# =========================

# apsolutna pogreška
error_three_1 = abs(y1_three - y_anal1)
error_two_1   = abs(y1_two - y_anal1)

error_three_2 = abs(y2_three - y_anal2)
error_two_2   = abs(y2_two - y_anal2)

plt.figure(figsize=(12,10))

# x^3 error
plt.subplot(2,1,1)
plt.plot(x1, error_three_1, '--', label="Greška (three-step)")
plt.plot(x1, error_two_1, ':', label="Greška (two-step)")
plt.title("Apsolutna pogreška derivacije za f(x)=x^3")
plt.xlabel("x")
plt.ylabel("Greška")
plt.legend()
plt.grid(True)

# sin(x) error
plt.subplot(2,1,2)
plt.plot(x2, error_three_2, '--', label="Greška (three-step)")
plt.plot(x2, error_two_2, ':', label="Greška (two-step)")
plt.title("Apsolutna pogreška derivacije za f(x)=sin(x)")
plt.xlabel("x")
plt.ylabel("Greška")
plt.legend()
plt.grid(True)

plt.show()