import numpy as np

def two_step(f, x, epsilon):
    return (f(x + epsilon) - f(x)) / epsilon

def three_step(f, x, epsilon):
    return (f(x + epsilon) - f(x - epsilon)) / (2 * epsilon)

def derivacija(f, x, epsilon=1e-5, metoda="three-step"):
    if metoda == "two-step":
        return two_step(f, x, epsilon)
    elif metoda == "three-step":
        return three_step(f, x, epsilon)
    else:
        raise ValueError("Nepoznata metoda!")

def raspon(f, x_min, x_max, epsilon=1e-5, metoda="three-step"):
    x_values = np.arange(x_min, x_max, epsilon)
    y_values = []

    for x in x_values:
        y_values.append(derivacija(f, x, epsilon, metoda))

    return x_values, np.array(y_values)


def pravokutna_aproksimacija(f, a, b, n):
    dx = (b - a) / n
    donja = 0
    gornja = 0

    for i in range(n):
        x1 = a + i * dx
        x2 = x1 + dx

        f1 = f(x1)
        f2 = f(x2)

        donja += min(f1, f2) * dx
        gornja += max(f1, f2) * dx

    return donja, gornja


def trapezna_metoda(f, a, b, n):
    dx = (b - a) / n
    suma = 0

    for i in range(n):
        x1 = a + i * dx
        x2 = x1 + dx

        suma += (f(x1) + f(x2)) / 2 * dx

    return suma