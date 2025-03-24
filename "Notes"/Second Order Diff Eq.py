
import matplotlib.pyplot as plt
import numpy as np

def f(r, t):
    x, y = r[0], r[1]
    fx = y
    fy = -(g / l) * np.sin(x) + C * np.cos(x) * np.sin(o * t)
    return np.array([fx, fy], float)

a = 0.0
b = 100.0
N = 1000
h = (b - a) / N
g = 9.81
l = 0.1
C = 2
o = 10.5

tpoints = np.arange(a, b, h)
xpoints = []
ypoints = []

r = np.array([0.0, 0.0], float)

for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += (k1 + 2 * k2 + 2 * k3 + k4) / 6

plt.figure()
plt.plot(tpoints, xpoints, c = "r", label = "x")
plt.xlabel("t")
plt.legend(loc = "best")
plt.show()

#%%

