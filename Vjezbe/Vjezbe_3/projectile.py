import numpy as np
import matplotlib.pyplot as plt


class Projectile:
    def __init__(self, x0, y0, v0, kut, masa, otpor):
        self.x0 = x0
        self.y0 = y0
        self.v0 = v0
        self.kut = np.radians(kut)
        self.masa = masa
        self.k = otpor
        self.g = 9.81


    def acc(self, vx, vy):
        ax = - (self.k / self.masa) * vx
        ay = - self.g - (self.k / self.masa) * vy
        return ax, ay


    def euler(self, dt):
        x, y = self.x0, self.y0
        vx = self.v0 * np.cos(self.kut)
        vy = self.v0 * np.sin(self.kut)

        traj_x = [x]
        traj_y = [y]

        while y >= 0:
            ax, ay = self.acc(vx, vy)

            vx += ax * dt
            vy += ay * dt

            x += vx * dt
            y += vy * dt

            traj_x.append(x)
            traj_y.append(y)

        return np.array(traj_x), np.array(traj_y)


    def rk4(self, dt):
        x, y = self.x0, self.y0
        vx = self.v0 * np.cos(self.kut)
        vy = self.v0 * np.sin(self.kut)

        traj_x = [x]
        traj_y = [y]

        while y >= 0:

            ax1, ay1 = self.acc(vx, vy)
            k1vx, k1vy = ax1 * dt, ay1 * dt
            k1x, k1y = vx * dt, vy * dt

            ax2, ay2 = self.acc(vx + k1vx/2, vy + k1vy/2)
            k2vx, k2vy = ax2 * dt, ay2 * dt
            k2x, k2y = (vx + k1vx/2) * dt, (vy + k1vy/2) * dt

            ax3, ay3 = self.acc(vx + k2vx/2, vy + k2vy/2)
            k3vx, k3vy = ax3 * dt, ay3 * dt
            k3x, k3y = (vx + k2vx/2) * dt, (vy + k2vy/2) * dt

            ax4, ay4 = self.acc(vx + k3vx, vy + k3vy)
            k4vx, k4vy = ax4 * dt, ay4 * dt
            k4x, k4y = (vx + k3vx) * dt, (vy + k3vy) * dt

            vx += (k1vx + 2*k2vx + 2*k3vx + k4vx) / 6
            vy += (k1vy + 2*k2vy + 2*k3vy + k4vy) / 6

            x += (k1x + 2*k2x + 2*k3x + k4x) / 6
            y += (k1y + 2*k2y + 2*k3y + k4y) / 6

            traj_x.append(x)
            traj_y.append(y)

        return np.array(traj_x), np.array(traj_y)


    def plot(self, dt, metoda="euler", label=None):
        if metoda == "euler":
            x, y = self.euler(dt)
        elif metoda == "rk4":
            x, y = self.rk4(dt)
        else:
            raise ValueError("Metoda mora biti 'euler' ili 'rk4'")

        plt.plot(x, y, label=label)


# TEST
if __name__ == "__main__": # Pokreni ovaj dio samo ako je ovo glavni file

    proj = Projectile(x0=0, y0=0, v0=50, kut=45, masa=1.0, otpor=0.1)


    plt.figure()

    for dt in [0.1, 0.05, 0.02, 0.01]:
        x, y = proj.euler(dt)
        plt.plot(x, y, label=f"Euler dt={dt}")

    plt.title("Euler stabilnost")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.legend()
    plt.show()


    plt.figure()

    x1, y1 = proj.euler(0.01)
    x2, y2 = proj.rk4(0.01)

    plt.plot(x1, y1, label="Euler dt=0.01")
    plt.plot(x2, y2, label="RK4 dt=0.01")

    plt.title("Euler vs RK4")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.legend()
    plt.show()