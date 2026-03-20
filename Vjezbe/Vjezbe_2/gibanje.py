import math
import matplotlib.pyplot as plt
from particle import Particle
g = 9.81

#D_anal = \frac{v^2_0 * sin(2\theta)}{g}
#D_num = funkcija range u klasi

v0 = 10
theta = math.radians(60)

moja_klasa = Particle(v0, theta)

D_num = moja_klasa.range(dt = 0.1)
D_anal = (v0**2 * math.sin(2*theta)) / g

odstupanje = abs(D_num - D_anal)

print("Numeričko rješenje je {} metara".format(D_num))
print("Analitičko rješenje je {} metara".format(D_anal))
print("Odstupanje iznosi {} metara".format(odstupanje))
print(len(moja_klasa.x_list), len(moja_klasa.y_list)) #test

moja_klasa.plot_trajectory() #samo pozivam funkciju
