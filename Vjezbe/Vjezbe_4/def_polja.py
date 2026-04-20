import numpy as np
import matplotlib.pyplot as plt

class Cestica:
    def __init__(self, masa, naboj, početno_stanje, električno_polje, magnetsko_polje, dt):
        self.masa = masa
        self.naboj = naboj
        self.stanje = np.array(početno_stanje, dtype=float)  # [x,y,z,vx,vy,vz]
        self.E = np.array(električno_polje)
        self.B = np.array(magnetsko_polje)
        self.dt = dt

        #uzmi početne pozicije iz stanja(lista za crtanje putanje)
        self.x = [self.stanje[0]]
        self.y = [self.stanje[1]]
        self.z = [self.stanje[2]]

    def lorentzova_sila(self):
        v = self.stanje[3:]
        return self.naboj * (self.E + np.cross(v, self.B))

    def kretanje(self):
        a = self.lorentzova_sila() / self.masa

        #update brzine
        self.stanje[3:] += a * self.dt

        #update pozicije (direktno iz stanja)
        self.stanje[0] += self.stanje[3] * self.dt
        self.stanje[1] += self.stanje[4] * self.dt
        self.stanje[2] += self.stanje[5] * self.dt

        #spremanje u listu za crtanje grafa
        self.x.append(self.stanje[0]) 
        self.y.append(self.stanje[1])
        self.z.append(self.stanje[2])

    def simulacija(self, trajanje):
        for _ in np.arange(0, trajanje, self.dt): #pitaj jeli točno
            self.kretanje()

    def prikaži_putanju(self, naslov):
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot(self.x, self.y, self.z)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(naslov)
        plt.show()