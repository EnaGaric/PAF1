import numpy as np

def srednja_vrijednost(x):

    x = np.array(x)

    return np.sum(x) / len(x)


def standardna_devijacija(x):

    x = np.array(x)

    n = len(x)

    x_crtica = srednja_vrijednost(x)

    sigma = np.sqrt(
        np.sum((x - x_crtica) ** 2)
        / (n * (n - 1))
    )

    return sigma