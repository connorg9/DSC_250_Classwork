import numpy as np
import matplotlib.pyplot as plt

R = 1.5
F = 2E-4
v0 = 4/3 * np.pi * (R ** 3)
t = v0 / F
n = 100
h = np.empty(n)


time = np.linspace(0, t, n)
for i, t in enumerate(time):
    eq = np.polynomial.Polynomial([F * t - v0, 0, np.pi * R, (-1/3) * np.pi])
    roots = eq.roots()
    roots = [r for r in roots if 0 <= r <= 2 * R]
    h[i] = roots[0]

plt.plot(h)
plt.show()

