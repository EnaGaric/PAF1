import math
import matplotlib.pyplot as plt

g = 9.81
class Particle:
    def __init__(self, v0, theta, x0=0, y0=0):
        self.v0 = v0
        self.theta = theta
        self.x0 = x0
        self.y0 = y0

        self.reset() #koja brise sve info o cestici

    def reset(self):
        self.x = self.x0
        self.y = self.y0

        #cos(kut) = v_x / v_0
        #sin(kut) = v_y / v_0
        self.vx = self.v0 * math.cos(self.theta)
        self.vy = self.v0 * math.sin(self.theta)

        self.x_list = [self.x]
        self.y_list = [self.y]

    def __move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vy -= g * dt

    def range(self, dt = 0.1):
        self.reset() #kreni od nule

        while self.y >= 0: #ako je iznad tla
            self._move(dt) #simuliraj kretanje malo po malo (promjena od vy)

        return self.x #vrati domet
    
    def plot_trajectory(self):
        plt.plot(self.x_list, self.y_list)
        plt.xlabel("x (m)")
        plt.ylabel("y (m)")
        plt.grid(True)
        plt.show()
