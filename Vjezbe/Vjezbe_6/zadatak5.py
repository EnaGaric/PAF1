import numpy as np



malo_n = np.array([99.8, 100.1, 99.9, 100.2, 100.0])

np.random.seed(42)
veliko_n = np.random.normal(
    loc=100.0,
    scale=0.2,
    size=10000
)


def sigma_n(x):
    x_bar = np.mean(x)
    return np.sqrt(np.sum((x - x_bar)**2) / len(x))


def s(x):
    x_bar = np.mean(x)
    return np.sqrt(np.sum((x - x_bar)**2) / (len(x) - 1))


def sigma_xbar(x):
    return s(x) / np.sqrt(len(x))


def relativna_razlika(a, b):
    return abs(a - b) / b * 100



for naziv, x in [("MALI SKUP", malo_n), ("VELIKI SKUP", veliko_n)]:

    sn = sigma_n(x)
    s_val = s(x)
    sx = sigma_xbar(x)

    print(f"\n========== {naziv} ==========")

    print(f"σn = {sn:.6f}")
    print(f"s  = {s_val:.6f}")
    print(f"σx̄ = {sx:.6f}")

    print(f"rel razlika σn vs s = {relativna_razlika(sn, s_val):.6f} %")



print("\n========== ODGOVORI ==========")

print("(a) Kada povećamo broj mjerenja (n), standardna devijacija s se ne mijenja značajno jer ona opisuje raspršenost samih podataka oko srednje vrijednosti – dakle “širinu” distribucije. Ako su mjerenja iz iste populacije, ta širina ostaje približno ista bez obzira na broj uzoraka. S druge strane, σx̄ (standardna devijacija srednje vrijednosti) se smanjuje kako n raste, jer se računa kao s / √n. To znači da što više mjerenja imamo, to bolje procjenjujemo pravu srednju vrijednost i ona postaje preciznija.")

print("(b) Za mali skup podataka razlika između σn i s može biti primjetna jer σn dijeli s n, dok s dijeli s (n−1), što daje malo veću i statistički ispravniju procjenu varijance za uzorak. Kod velikog skupa (n = 10000) ta razlika postaje praktički zanemariva jer se n i (n−1) gotovo ne razlikuju, pa σn i s daju gotovo identične vrijednosti.")

print("(c) np.std() po defaultu koristi dijeljenje s n (ddof = 0), što znači da računa standardnu devijaciju populacije. To je ispravno koristiti kada imamo kompletne podatke cijele populacije, odnosno kada ne procjenjujemo ništa nego već imamo “sve”. U laboratorijskim mjerenjima i eksperimentima (što je gotovo uvijek slučaj u fizici), ispravno je koristiti ddof = 1 (uzorak), jer pokušavamo procijeniti stvarnu vrijednost iz ograničenog broja mjerenja.")
