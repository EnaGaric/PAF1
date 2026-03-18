import matplotlib.pyplot as plt
import numpy as np
print("Program za jednoliko gibanje u jednoj dimenziji\n")


def jednoliko_gibanje(F, m, t_max = 10, dt = 1):
    while True:
        try:
            F = float(input("Unesi iznos sile F(N): "))
            m = float(input("Unesi masu tijela m(kg): "))
            break
        except ValueError:
            print("Molim te da uneseš u decimalnom zapisu.\n")

    t = np.arange(0, t_max + 1, dt) #np.array(start, stop, korak)

    x0 = 0 
    v0 = 0  
    a = F / m 

    brzine=[]
    pomaci=[]
    akceleracije=[]


    x = x0
    v = v0

    for sec in t:
        if sec == 0:
            brzine.append(v0)
            pomaci.append(x0)
            akceleracije.append(a)
        else:
            v = v + a * dt
            x = x + v0 * dt + 0.5 * a * dt**2   # formula iz kinematike kod Eulera
            brzine.append(v)
            pomaci.append(x)
            akceleracije.append(a)
            v0 = v 

    plt.figure(figsize=(12,12))
    plt.subplot(3, 1, 1)
    plt.plot(t, pomaci, label='Položaj (x)', color='red')
    plt.xlabel('Vrijeme (t) [s]')
    plt.ylabel('Položaj (x) [m]')


    plt.subplot(3, 1, 2)
    plt.plot(t, brzine, label='Brzina (v)', color='green')
    plt.xlabel('Vrijeme (t) [s]')
    plt.ylabel('Brzina (v) [m/s]')

    plt.subplot(3, 1, 3)
    plt.plot(t, akceleracije, label='Akceleracija (a)', color='blue')
    plt.xlabel('Vrijeme (t) [s]')
    plt.ylabel('Akceleracija (a) [m/s^2]')

    plt.show()
