import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def f4(x):
    return (a**4 - x**4)**(-0.5)

T4_vals = []

avals = np.linspace(0.01,2,1000)

for a in avals:
    val, error = integrate.quad(f4, 0, a)
    T4_vals.append(val * 2 * 2 ** 0.5)

plt.figure()
plt.plot(avals, T4_vals)
plt.xlabel("Amplitude")
plt.ylabel("Period")
plt.show()

