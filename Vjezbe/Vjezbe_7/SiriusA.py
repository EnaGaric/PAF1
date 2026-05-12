import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42)
mase = np.random.normal(2.06, 0.05, 57).tolist() + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02]
mase = np.array(mase)

#Zadatak 1

def histogram(x, k):
    edges = np.linspace(min(x), max(x), k+1)
    counts = np.histogram(x, bins=edges)[0]

    for i in range(k):
        print(f"[{edges[i]:.2f}, {edges[i+1]:.2f}): {counts[i]}")

    return edges, counts


edges, counts = histogram(mase[:57], 10)

plt.bar(edges[:-1], counts, width=np.diff(edges), align='edge', edgecolor='black')
plt.title("Ručni histogram")
plt.show()


#Zadatak 2
counts_np, edges_np = np.histogram(mase[:57], bins=10)

mean = np.mean(mase[:57])
median = np.median(mase[:57])

plt.bar(edges_np[:-1], counts_np, width=np.diff(edges_np), align='edge')

plt.axvline(mean, color='r', label='mean')
plt.axvline(median, color='g', label='median')

plt.legend()
plt.show()


#Zadatak 3
def medijan(x):
    x = sorted(x)
    n = len(x)
    return x[n//2] if n % 2 else (x[n//2-1] + x[n//2]) / 2

print("Medijan a:", medijan([3,1,4,1,5,9,2,6]))
print("Medijan b:", medijan([3,1,4,1,5,9,2,6,5]))


#Zadatak 4
mean_all = np.mean(mase)
median_all = np.median(mase)

clean = mase[np.abs(mase - np.mean(mase)) < 3*np.std(mase)]

mean_clean = np.mean(clean)
median_clean = np.median(clean)

print(mean_all, median_all)
print(mean_clean, median_clean)

plt.hist(mase, bins=10, edgecolor='black')

plt.axvline(mean_all, color='r', label='mean (all)')
plt.axvline(median_all, color='g', label='median (all)')
plt.axvline(mean_clean, color='orange', label='mean (clean)')
plt.axvline(median_clean, color='purple', label='median (clean)')

plt.legend()
plt.title("Outlieri efekt")
plt.show()