import numpy as np
import matplotlib.pyplot as plt

class Projectile:

    def __init__(self, v0, theta, k=0.1, m=1.0, x0=0, y0=0):
        self.v0 = v0
        self.theta = theta
        self.k = k
        self.m = m
        self.x0 = x0
        self.y0 = y0


    def derivatives(self, state):
        x, y, vx, vy = state
        g = 9.81

        v = np.sqrt(vx**2 + vy**2)

        ax = - (self.k / self.m) * vx * v
        ay = -g - (self.k / self.m) * vy * v

        return np.array([vx, vy, ax, ay])

    # EULER
    def step_euler(self, state, dt):
        return state + dt * self.derivatives(state)

    # RK4
    def step_rk4(self, state, dt):
        k1 = self.derivatives(state)
        k2 = self.derivatives(state + 0.5 * dt * k1)
        k3 = self.derivatives(state + 0.5 * dt * k2)
        k4 = self.derivatives(state + dt * k3)

        return state + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)


    def simulate(self, dt, metoda="euler"):

        state = np.array([
            self.x0,
            self.y0,
            self.v0 * np.cos(self.theta),
            self.v0 * np.sin(self.theta)
        ])

        states = [state.copy()]

        while state[1] >= 0:  # y >= 0
            if metoda == "euler":
                state = self.step_euler(state, dt)
            elif metoda == "rk4":
                state = self.step_rk4(state, dt)
            else:
                raise ValueError("Nepoznata metoda!")

            states.append(state.copy())

        states = np.array(states)

        return states[:,0], states[:,1]  # x, y


    def plot_trajectory(self, dt, metoda="euler", label=None):
        x, y = self.simulate(dt, metoda)
        plt.plot(x, y, label=label)
    
proj = Projectile(v0=50, theta=np.radians(45), k=0.1)

plt.figure()

for dt in [0.1, 0.05, 0.02, 0.01]:
    x, y = proj.simulate(dt, metoda="euler")
    plt.plot(x, y, label=f"Euler dt={dt}")

plt.legend()
plt.grid()
plt.title("Euler stabilnost testa")
plt.show()

proj = Projectile(v0=50, theta=np.radians(45), k=0.1)

plt.figure()

x1, y1 = proj.simulate(0.01, metoda="euler")
x2, y2 = proj.simulate(0.01, metoda="rk4")

plt.plot(x1, y1, label="Euler dt=0.01")
plt.plot(x2, y2, label="RK4 dt=0.01")

plt.legend()
plt.grid()
plt.title("Euler vs RK4")
plt.show()