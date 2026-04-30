import numpy as np
import matplotlib.pyplot as plt



def obradi_otpornik(naziv, U, I):
    print(f"\n=== OTPORNIK: {naziv} ===")

    U = np.array(U)
    I = np.array(I)

    R_pojed = U / I
    R_srednji = np.mean(R_pojed)

    print("Srednji otpor:", R_srednji, "Ω")

    koef = np.polyfit(I, U, 1)
    R_reg = koef[0]

    print("Otpor iz regresije:", R_reg, "Ω")

    return koef


# CEKAS
U_cekas = [3.1, 3.2, 3.35, 3.5, 3.8, 4.2, 5.0, 6.0, 6.6, 7.0]
I_cekas = [0.091, 0.099, 0.101, 0.109, 0.118, 0.129, 0.155, 0.187, 0.206, 0.219]

# ŽELJEZO
U_zeljezo = [0.44,0.49,0.5,0.54,0.6,0.7,0.8,0.9,1.0,1.3]
I_zeljezo = [0.10,0.11,0.12,0.13,0.14,0.18,0.22,0.23,0.26,0.35]

# BAKAR
U_bakar = [0.17,0.20,0.25,0.26,0.28,0.30,0.32,0.36]
I_bakar = [0.11,0.14,0.17,0.181,0.20,0.21,0.24,0.26]



k_cekas = obradi_otpornik("Cekas", U_cekas, I_cekas)
k_zeljezo = obradi_otpornik("Željezo", U_zeljezo, I_zeljezo)
k_bakar = obradi_otpornik("Bakar", U_bakar, I_bakar)



print("\n=== AKUMULATOR ===")

I_bat = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
U_bat = np.array([12.2,12.1,12.0,11.9,11.8,11.7,11.6,11.5,11.4,11.3])

koef_bat = np.polyfit(I_bat, U_bat, 1)

Ru = -koef_bat[0]
epsilon = koef_bat[1]

print("Unutarnji otpor Ru =", Ru, "Ω")
print("EMF ε =", epsilon, "V")



fig, axs = plt.subplots(2, 2, figsize=(10, 8))

def nacrtaj(ax, I, U, koef, naslov):
    ax.scatter(I, U)
    ax.plot(I, np.polyval(koef, I))
    ax.set_title(naslov)
    ax.set_xlabel("I [A]")
    ax.set_ylabel("U [V]")


nacrtaj(axs[0,0], I_cekas, U_cekas, k_cekas, "Cekas")
nacrtaj(axs[0,1], I_zeljezo, U_zeljezo, k_zeljezo, "Željezo")
nacrtaj(axs[1,0], I_bakar, U_bakar, k_bakar, "Bakar")
nacrtaj(axs[1,1], I_bat, U_bat, koef_bat, "Akumulator")

plt.tight_layout()
plt.show()