import math
import matplotlib.pyplot as plt
from particle import Particle

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


dt_values = [0.5, 0.2, 0.1, 0.05, 0.01]
rel_errors = []

for dt in dt_values:
    p = Particle(v0, theta)
    D_num = p.range(dt=dt)
    
    rel_error = abs(D_num - D_anal) / abs(D_anal)
    rel_errors.append(rel_error)

# crtanje grafa
plt.figure()
plt.plot(dt_values, rel_errors, marker='o')

plt.xlabel("dt")
plt.ylabel("Relativna pogreška")
plt.title("Ovisnost relativne pogreške o koraku dt")
plt.grid(True)

plt.show()