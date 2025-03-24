
import math
import matplotlib.pyplot as plt
import numpy as np

def f(r, t):
    x, y = r[0], r[1]
    fx = x * y - x
    fy = y - x * y + np.sin(t) ** 2
    return np.array([fx, fy], float)

a = 0.0
b = 10.0
N = 1000
h = (b - a) / N

tpoints = np.arange(a, b, h)
xpoints = []
ypoints = []
r = np.array([1.0, 1.0], float)

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
plt.plot(tpoints, ypoints, c = "b", linestyle = "--", label = "y")
plt.xlabel("t")
plt.legend(loc = "best")
plt.show()

#%%

def lorenz(r, t):
    x, y, z = r[0], r[1], r[2]
    fx = s * (y - x)
    fy = R * x - y - x * z
    fz = x * y - B * z
    return np.array([fx, fy, fz], float)

a = 0.0
b = 50.0
N = 10000
h = (b - a) / N
s = 10
R = 28
B = 8 / 3

tpoints = np.arange(a, b, h)
xpoints = []
ypoints = []
zpoints = []
r = np.array([0.0, 1.0, 0.0], float)

for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    zpoints.append(r[2])
    k1 = h * lorenz(r, t)
    k2 = h * lorenz(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * lorenz(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * lorenz(r + k3, t + h)
    r += (k1 + 2 * k2 + 2 * k3 + k4) / 6

plt.figure()
plt.subplot(211)
plt.plot(tpoints, ypoints, c = "r", label = "y")
plt.subplot(212)
plt.plot(zpoints, xpoints, c = "b", label = "z wrt x")
plt.legend(loc = "best")
plt.show()