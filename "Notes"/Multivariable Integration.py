import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def f(x, y):
    return x ** 2 * y

N = 100
x_low = 1
x_high = 4
y_low = 0
y_high = 2
xvals = np.linspace(x_low, x_high, N)
yvals = np.linspace(y_low, y_high, N)

Z = np.zeros((N, N))
for i, x in enumerate(xvals):
    for j, y in enumerate(yvals):
        Z[i, j] = f(x, y)

X, Y = np.meshgrid(xvals, yvals)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.plot_surface(X, Y, Z)
fig.tight_layout()
#plt.show()

#%%

from scipy.integrate import dblquad, tplquad

def f(theta, phi):
    return (R ** 2) * np.sin(theta)

R = 3
def y_lower(theta):
    return 0
def y_higher(theta):
    return np.pi

val1, error1 = dblquad(f, 0, 2 * np.pi, y_lower, y_higher)

print(val1)
print(4 * np.pi * (3 ** 2))

#%%


def f(r, theta, phi):
    return (r ** 2) * np.sin(theta)
R = 2

val, error = tplquad(f, 0, 2 * np.pi,
                     lambda phi: 0, lambda phi: np.pi,
                     lambda phi, theta: 0, lambda phi, theta: R)
print(val)

