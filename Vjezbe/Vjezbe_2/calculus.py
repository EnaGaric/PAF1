import numpy as np

# two-step metoda
def two_step(f, x, epsilon):
    return (f(x + epsilon) - f(x)) / epsilon

# three-step metoda
def three_step(f, x, epsilon):
    return (f(x + epsilon) - f(x - epsilon)) / (2 * epsilon)

def derivacija(f, x, epsilon, metoda = "three_step"):
    if metoda == "two_step":
        return two_step(f, x, epsilon)
    else:
        return three_step(f, x, epsilon)
    
def raspon(f, x_min, x_max, epsilon, metoda="three_step"):
    x_values = np.arange(x_min, x_max, epsilon)
    y_values = []

    for x in x_values:
        y_values.append(derivacija(f, x, epsilon, metoda))

    return x_values, np.array(y_values)

def pravokutna_aproksimacija(f, a, b, n):
    dx = (b - a) / n
    donja_granica = 0
    gornja_granica = 0

    for i in range(n):
        x1 = a + dx * i
        x2 = x1 + dx

        f1 = f(x1)
        f2 = f(x2)

        donja_granica += min(f1, f2) * dx
        gornja_granica += max(f1, f2) * dx

    return donja_granica, gornja_granica
    
def trapezna_metoda(f, a, b, n):
    dx = (b - a) / n
    suma = 0

    for i in range(n):
        x1 = a + dx * i
        x2 = x1 + dx

        suma += (f(x1) + f(x2)) / 2 * dx
    
    return suma