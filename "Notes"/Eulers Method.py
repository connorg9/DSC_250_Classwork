import math
import matplotlib.pyplot as plt
import numpy as np

def f(x, t):
    return -x ** 3 + math.sin(t)

a = 0.0
b = 10.0
N = 1000
h = (b - a) / N
x = 0.0

tpoints = np.arange(a, b, h)
xpoints = []

for t in tpoints:
    xpoints.append(x)
    x += h * f(x, t)

plt.figure()
plt.plot(tpoints, xpoints, c = "r")
plt.xlabel("t")
plt.ylabel("x(t) (Eulers)")

a = 0.0
b = 10.0
N = 20
h = (b - a) / N
x = 0.0

tpoints = np.arange(a, b, h)
xpoints = []

for t in tpoints:
    xpoints.append(x)
    k1 = h * f(x, t)
    k2 = h * f(x + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(x + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(x + k3, t + h)
    x += (k1 + 2 * k2 + 2 * k3 + k4) / 6

plt.plot(tpoints, xpoints, c = "b", linestyle = "--")
plt.show()