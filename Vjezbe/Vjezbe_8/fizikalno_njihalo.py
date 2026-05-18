import numpy as np
import matplotlib.pyplot as plt


kut_deg = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40,
                    45, 50, 55, 60, 65, 70, 75, 80, 85])

T_120 = np.array([0.8020, 0.8187, 0.8327, 0.8660, 0.8980,
                  0.9153, 0.9293, 0.9653, 0.9747, 1.0200,
                  1.0373, 1.1160, 1.1780, 1.2733, 1.4180,
                  1.6373, 1.9100, 2.5460])

T_240 = np.array([1.0140, 1.0320, 1.0433, 1.0673, 1.0840,
                  1.1320, 1.1440, 1.1720, 1.1980, 1.2293,
                  1.2813, 1.3573, 1.4200, 1.5600, 1.7413,
                  1.9840, 2.4473, 3.1573])

theta = np.radians(kut_deg)
g = 9.81

L_teor_120 = 0.12
L_teor_240 = 0.24


def T_model(theta, l):
    return 2*np.pi*np.sqrt(l / (g*np.cos(theta)))


#numerička linearizacija
# T^2 cosθ = (4π^2/g) l


x = np.cos(theta)

y120 = T_120**2
y240 = T_240**2

#transformacija: y * cosθ = k l
Y120 = y120 * x
Y240 = y240 * x


#analitički fit (kroz ishodište)


k120 = np.sum(x * Y120) / np.sum(x**2)
k240 = np.sum(x * Y240) / np.sum(x**2)

# l iz konstante
l120 = (k120 * g) / (4 * np.pi**2)
l240 = (k240 * g) / (4 * np.pi**2)



theta_glatko = np.linspace(0, np.radians(85), 300)

T120_teor = T_model(theta_glatko, L_teor_120)
T240_teor = T_model(theta_glatko, L_teor_240)



plt.figure()

plt.scatter(kut_deg, T_120, color='royalblue', label='120 mm mjerenja')
plt.scatter(kut_deg, T_240, color='seagreen', label='240 mm mjerenja')

plt.plot(np.degrees(theta_glatko), T120_teor, color='darkblue', label='120 mm teorija')
plt.plot(np.degrees(theta_glatko), T240_teor, color='darkgreen', label='240 mm teorija')

plt.xlabel("kut θ (°)")
plt.ylabel("period T (s)")
plt.title("Fizikalno njihalo")
plt.grid()
plt.legend()

plt.show()


rel_120 = abs(l120 - L_teor_120) / L_teor_120
rel_240 = abs(l240 - L_teor_240) / L_teor_240


print("===== REZULTATI =====")

print("\n120 mm:")
print("l =", l120)
print("relativna pogreška =", rel_120)

print("\n240 mm:")
print("l =", l240)
print("relativna pogreška =", rel_240)