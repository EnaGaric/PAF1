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

L_true_120 = 0.12
L_true_240 = 0.24


def T_model(theta, l):
    return 2*np.pi*np.sqrt(l / (g*np.cos(theta)))


cos_theta = np.cos(theta)

# LINEARIZACIJA (FIT BEZ curve_fit)

cos_theta = np.cos(theta)

T2_120 = T_120**2
T2_240 = T_240**2

# linearizirani oblik:
# T^2 * cos(theta) = k * cos(theta)
Y_120 = T2_120 * cos_theta
Y_240 = T2_240 * cos_theta

# least squares fit kroz ishodište: Y = kx
k_120 = np.sum(cos_theta * Y_120) / np.sum(cos_theta**2)
k_240 = np.sum(cos_theta * Y_240) / np.sum(cos_theta**2)

# iz k dobivamo l
L_120 = (k_120 * g) / (4 * np.pi**2)
L_240 = (k_240 * g) / (4 * np.pi**2)

theta_smooth = np.linspace(0, np.deg2rad(85), 300)


T_theory_120 = T_model(theta_smooth, L_true_120)
T_theory_240 = T_model(theta_smooth, L_true_240)

plt.figure()

# mjerenja
plt.scatter(kut_deg, T_120, label="120 mm mjerenja", color="royalblue")
plt.scatter(kut_deg, T_240, label="240 mm mjerenja", color="seagreen")

# teorija
plt.plot(np.rad2deg(theta_smooth), T_theory_120, color="blue", label="120 mm teorija")
plt.plot(np.rad2deg(theta_smooth), T_theory_240, color="green", label="240 mm teorija")

plt.xlabel("kut θ (°)")
plt.ylabel("period T (s)")
plt.title("Fizikalno njihalo – mjerenja vs teorija")
plt.grid()
plt.legend()

plt.show()


print("\n===== REZULTATI =====")

print("\n120 mm:")
print("l =", L_120)
print("relativna pogreška =", abs(L_120 - L_true_120) / L_true_120)

print("\n240 mm:")
print("l =", L_240)
print("relativna pogreška =", abs(L_240 - L_true_240) / L_true_240)