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