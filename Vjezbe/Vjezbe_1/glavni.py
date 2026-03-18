from Kinematika import jednoliko_gibanje

import sys
sys.path.append("C:/NewFolder/PAF")

print("Jednoliko gibanje u jednoj dimenziji.\n")

while True:
    try:
        F = float(input("Unesite iznos sile F (N): "))
        m = float(input("Unesite masu čestice m (kg): "))
        break
    except ValueError:
        print("Molim unesite broj u decimalnom zapisu.\n")

jednoliko_gibanje(F, m, t_max=10, dt=1)