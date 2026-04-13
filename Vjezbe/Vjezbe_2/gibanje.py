import math
import matplotlib.pyplot as plt
from particle import Particle
import numpy as np

g = 9.81

v0 = 10
theta = math.radians(60)

# analitičko rješenje
D_anal = (v0**2 * math.sin(2 * theta)) / g


moja_klasa = Particle(v0, theta)

D_num = moja_klasa.range(dt=0.1)
odstupanje = abs(D_num - D_anal)

print("Numeričko rješenje je {} metara".format(D_num))
print("Analitičko rješenje je {} metara".format(D_anal))
print("Odstupanje iznosi {} metara".format(odstupanje))

moja_klasa.plot_trajectory()


# GRAF RELATIVNE POGREŠKe


dt_values = np.linspace(0.001, 0.1, 300)#promijeni da ide trend gore dolje oscilacije
rel_errors = []

for dt in dt_values:
    p = Particle(v0, theta)
    D_num = p.range(dt=dt)
    
    rel_error = abs(D_num - D_anal) / abs(D_anal) *100
    rel_errors.append(rel_error)

plt.figure()
plt.plot(dt_values, rel_errors)

plt.xlabel("dt")
plt.ylabel("Relativna pogreška [%]")
plt.title("Ovisnost relativne pogreške o koraku dt")
plt.grid(True)

plt.show()