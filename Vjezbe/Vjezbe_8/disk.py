import numpy as np
import matplotlib.pyplot as plt

h0 = 0.54
m = 0.5257
r = 4.025e-3
g = 9.81

h = np.array([0.14, 0.17, 0.19, 0.22, 0.25,
              0.28, 0.31, 0.34, 0.37, 0.40])

t = np.array([1.740, 1.793, 2.043, 2.190, 2.280,
              2.417, 2.540, 2.640, 2.670, 2.813])

s = h0 - h
n = len(s)

# log-log

x = np.log(t)
y = np.log(s)

a = (n*np.sum(x*y) - np.sum(x)*np.sum(y)) / (n*np.sum(x**2) - (np.sum(x))**2)

b = (np.sum(y) - a*np.sum(x)) / n

y_fit = a*x + b

aef1 = 2*np.exp(b)


# error bars na uzor od gnuplota


s_std = np.std(s, ddof=1)
y_err = s_std / s   # propagacija u log(s)

plt.figure()

plt.errorbar(
    x, y,
    yerr=y_err,
    fmt='o',
    color='royalblue',
    ecolor='gray',
    capsize=3,
    label='mjerenja'
)

plt.plot(x, y_fit, color='darkorange', label='fit')

plt.xlabel("log(t)")
plt.ylabel("log(s)")
plt.title("log(s) - log(t)")
plt.grid()
plt.legend()

plt.show()

print("*** LOG-LOG ***")
print("a =", a)
print("b =", b)
print("aef =", aef1)


# s - t^2

x2 = t**2
y2 = s

a2 = np.sum(x2*y2) / np.sum(x2**2)

y_fit2 = a2*x2

aef2 = 2*a2


plt.figure()

plt.scatter(x2, y2, color='seagreen', label='mjerenja')
plt.plot(x2, y_fit2, color='crimson', label='fit')

plt.xlabel("t²")
plt.ylabel("s")
plt.title("s - t²")
plt.grid()
plt.legend()

plt.show()

print("\n*** s - t² ***")
print("a =", a2)
print("aef =", aef2)


# moment tromosti

Iz = (m*g*r**2)/aef2 - m*r**2

print("\n*** MOMENT TROMOSTI ***")
print("Iz =", Iz, "kg m^2")