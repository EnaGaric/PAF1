import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57)
mase = list(mase_ciste) + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02]

mase = np.array(mase)

# Zadatak 1
def histogram(podaci, k):
    xmin = np.min(podaci)
    xmax = np.max(podaci)

    h = (xmax - xmin) / k #širina razreda
    #rubovi razreda
    granice = [xmin + i*h for i in range(k+1)]

    frekvencije = [0]*k
    #brojanje po razredima
    for x in podaci:
        for i in range(k):
            if i < k-1:
                if granice[i] <= x < granice[i+1]:
                    frekvencije[i] += 1
                    break
            else:
                if granice[i] <= x <= granice[i+1]:
                    frekvencije[i] += 1

    
    for i in range(k):
        print(f"[{granice[i]:.2f}, {granice[i+1]:.2f}): {frekvencije[i]}")

    return granice, frekvencije

edges, freq = histogram(mase_ciste, k = 10)

plt.bar(edges[:-1], freq, width=np.diff(edges), align='edge')
plt.title("Histogram (ručno)")
plt.xlabel("Masa")
plt.ylabel("Frekvencija")
plt.grid(axis='y')
plt.show()

# Zadatak 2
freq_np, bins = np.histogram(mase_ciste, bins=10)

plt.bar(bins[:-1], freq_np, width=np.diff(bins), align='edge', alpha=0.6)

plt.axvline(np.mean(mase_ciste), color='r', label='mean')
plt.axvline(np.median(mase_ciste), color='g', label='median')

plt.title("NumPy histogram + mean/median")
plt.xlabel("Masa")
plt.ylabel("Frekvencija")
plt.legend()
plt.show()


# Zadatak 3
def medijan(podaci):
    x = sorted(podaci)
    n = len(x)

    if n % 2 == 1:
        return x[n//2]
    else:
        return (x[n//2 - 1] + x[n//2]) / 2
    
# testovi
a = [3, 1, 4, 1, 5, 9, 2, 6]
b = [3, 1, 4, 1, 5, 9, 2, 6, 5]

print(medijan(a))
print(medijan(b))

print(np.median(a))
print(np.median(b))

# Zadatak 4
mean_all = np.mean(mase)
median_all = np.median(mase)

mean_clean = np.mean(mase_ciste)
median_clean = np.median(mase_ciste)

print("ALL mean:", mean_all)
print("ALL median:", median_all)
print("CLEAN mean:", mean_clean)
print("CLEAN median:", median_clean)

print("Δ mean:", mean_clean - mean_all)
print("Δ median:", median_clean - median_all)

plt.hist(mase, bins=10, alpha=0.4, label="all")

plt.axvline(mean_all, color='r', linestyle='--', label='mean all')
plt.axvline(median_all, color='g', linestyle='--', label='median all')

plt.axvline(mean_clean, color='r', linestyle='-')
plt.axvline(median_clean, color='g', linestyle='-')

plt.title("Sirius A mase - robusnost srednjih vrijednosti")
plt.xlabel("Masa")
plt.ylabel("Frekvencija")
plt.legend()
plt.show()
#Median bolje procjenjuje stvarnu masu zvijezde jer je robustan na grube pogreške, 
#dok aritmetička sredina značajno odstupa zbog outliera.