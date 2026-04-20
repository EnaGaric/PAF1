import numpy as np
import matplotlib.pyplot as plt
from def_polja import Cestica

def run_sim(masa, naboj, početno_stanje, E, B, dt=0.01, t=20):
    c = Cestica(masa, naboj, početno_stanje, E, B, dt)
    c.simulacija(t)
    return c

masa_e = 1
masa_p = masa_e

q_e = -1
q_p = 1

početno = [0, 0, 0, 0.1, 0.1, 0.1]



#1. MULTIPLOT: elektron / pozitron
E = np.array([0, 0, 0])
B = np.array([0, 0, 1])

elektron = run_sim(masa_e, q_e, početno, E, B)
pozitron = run_sim(masa_p, q_p, početno, E, B)

fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(121, projection='3d')
ax1.plot(elektron.x, elektron.y, elektron.z)
ax1.set_title("Elektron (B polje)")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot(pozitron.x, pozitron.y, pozitron.z)
ax2.set_title("Pozitron (B polje)")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Z")

plt.tight_layout()
plt.show()



#2. MULTIPLOT
fig = plt.figure(figsize=(12, 10))

#1: samo B kruženje tj heliks
E1 = np.array([0, 0, 0])
B1 = np.array([0, 0, 1])

e1 = run_sim(masa_e, q_e, početno, E1, B1)
p1 = run_sim(masa_p, q_p, početno, E1, B1)

ax1 = fig.add_subplot(221, projection='3d')
ax1.plot(e1.x, e1.y, e1.z, label="Elektron")
ax1.plot(p1.x, p1.y, p1.z, label="Pozitron")
ax1.set_title("B1 = ([0, 0, 1]), E1 = 0")
ax1.legend()


#2: E + B zakrivljenje
E2 = np.array([0, 1, 0])
B2 = np.array([0, 0, 1])

e2 = run_sim(masa_e, q_e, početno, E2, B2)
p2 = run_sim(masa_p, q_p, početno, E2, B2)

ax2 = fig.add_subplot(222, projection='3d')
ax2.plot(e2.x, e2.y, e2.z, label="Elektron")
ax2.plot(p2.x, p2.y, p2.z, label="Pozitron")
ax2.set_title("E2 + B2 = ([0, 1, 0]) + ([0, 0, 1])")
ax2.legend()


#3: samo E ubrzano gibanje
E3 = np.array([0, 1, 0])
B3 = np.array([0, 0, 0])

e3 = run_sim(masa_e, q_e, početno, E3, B3)
p3 = run_sim(masa_p, q_p, početno, E3, B3)

ax3 = fig.add_subplot(223, projection='3d')
ax3.plot(e3.x, e3.y, e3.z, label="Elektron")
ax3.plot(p3.x, p3.y, p3.z, label="Pozitron")
ax3.set_title("E3 = ([0, 1, 0]), B3 = 0")
ax3.legend()


#4: jače B manji radijus
E4 = np.array([0, 0, 0])
B4 = np.array([0, 0, 2])

e4 = run_sim(masa_e, q_e, početno, E4, B4)
p4 = run_sim(masa_p, q_p, početno, E4, B4)

ax4 = fig.add_subplot(224, projection='3d')
ax4.plot(e4.x, e4.y, e4.z, label="Elektron")
ax4.plot(p4.x, p4.y, p4.z, label="Pozitron")
ax4.set_title("B4 = ([0, 0, 2]), E4 = 0")
ax4.legend()

plt.tight_layout()
plt.show()