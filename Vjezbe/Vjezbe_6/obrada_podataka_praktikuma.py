import numpy as np
from arithm2 import srednja_vrijednost, standardna_devijacija


def volumen_valjka(R, L):
    return np.pi * R**2 * L


def sigma_volumena(R, sigma_R, L, sigma_L):
    return np.sqrt(
        (2 * np.pi * R * L * sigma_R)**2 +
        (np.pi * R**2 * sigma_L)**2
    )


def gustoca(m, V):
    return m / V


def sigma_gustoce(m, sigma_m, V, sigma_V):
    return np.sqrt(
        (sigma_m / V)**2 +
        ((m * sigma_V) / V**2)**2
    )


def relativna_pogreska(rho, rho_lit):
    return abs(rho - rho_lit) / rho_lit * 100



d = [
    np.array([19.98, 20.18, 20.10, 20.08, 19.74]),
    np.array([19.92, 19.82, 19.96, 19.98, 19.88]),
    np.array([24.96, 24.98, 24.98, 24.92, 24.94])
]

L = [
    np.array([49.80, 49.00, 50.48, 49.80, 49.96]),
    np.array([52.56, 52.50, 52.62, 52.58, 52.54]),
    np.array([55.34, 55.40, 55.30, 55.44, 55.48])
]

m = [
    np.array([138.92, 138.98, 139.20, 138.90, 138.92]),
    np.array([128.65, 128.60, 128.65, 128.35, 128.50]),
    np.array([71.89, 71.90, 71.79, 71.85, 71.70])
]

#Pretvorba u cm
R = [x / 20 for x in d]
L = [x / 10 for x in L]




print("\n========== ZADATAK 1 i 2 ==========")

volumeni = []
sigma_vol = []

for i in range(3):

    R_sr = srednja_vrijednost(R[i])
    sR = standardna_devijacija(R[i])

    L_sr = srednja_vrijednost(L[i])
    sL = standardna_devijacija(L[i])

    m_sr = srednja_vrijednost(m[i])
    sm = standardna_devijacija(m[i])

    V = volumen_valjka(R_sr, L_sr)
    sV = sigma_volumena(R_sr, sR, L_sr, sL)

    volumeni.append(V)
    sigma_vol.append(sV)

    print(f"\nVALJAK {i+1}")

    print(f"R = ({R_sr:.5f} ± {sR:.2e}) cm")
    print(f"L = ({L_sr:.5f} ± {sL:.2e}) cm")
    print(f"m = ({m_sr:.5f} ± {sm:.2e}) g")

    print(f"V = ({V:.5e} ± {sV:.2e}) cm^3")



print("\n========== ZADATAK 3 ==========")

rho_lista = []

for i in range(3):

    m_sr = srednja_vrijednost(m[i])
    sm = standardna_devijacija(m[i])

    V = volumeni[i]
    sV = sigma_vol[i]

    rho = gustoca(m_sr, V)
    srho = sigma_gustoce(m_sr, sm, V, sV)

    rho_lista.append(rho)

    print(f"\nVALJAK {i+1}")

    print(f"ρ = ({rho:.5e} ± {srho:.2e}) g/cm^3")



print("\n========== ZADATAK 4 ==========")

materijali = {
    "Aluminij": 2.70,
    "Željezo": 7.87,
    "Mesing": 8.50
}

for i in range(3):

    rho = rho_lista[i]

    najbolji = ""
    min_pogreska = 1e9

    for materijal, rho_lit in materijali.items():

        pog = relativna_pogreska(rho, rho_lit)

        if pog < min_pogreska:
            min_pogreska = pog
            najbolji = materijal

    print(f"\nVALJAK {i+1}")

    print(f"Materijal: {najbolji}")
    print(f"Relativna pogreška: {min_pogreska:.2f} %")