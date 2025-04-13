import numpy as np
from scipy.integrate import tplquad
from scipy.integrate import quad

#Q8.2.2
#a
def f(x):
    return ((x**4) * ((1 - x)**4)) / (1 + (x**2))

val, error = quad(f, 0, 1)
print("The integral value is ", val)
print("The exact value is ", (22/7) - np.pi)

#b
def f(x):
    return (x**3) / (np.exp(x) - 1)

val, error = quad(f, 0, np.inf)
print("The integral value is ", val)
print("The exact value is ", (np.pi ** 4) / 15)

#P8.2.1
def f(x):
    y = np.sqrt(x)
    dy_dx = (1/2) / np.sqrt(x)
    ds = np.sqrt(1 + (dy_dx ** 2))
    return (2 * np.pi) * y * ds

a = 0
b = 1
val, error = quad(f, a, b)
print("The integral value is ", val)
print("The exact value is ", (np.pi * ((5**(3/2)) - 1)) / 6)

#12-3
H = 2
R = 2.5
def f(r, z, theta):
    return (z ** 2) * (r**3)

val, error = tplquad(f, 0, R,
                     lambda r: r * (H/R), lambda r: H,
                     lambda r, z: 0, lambda r, z: 2 * np.pi)

print("The moment of inertia for an inverted cone spinning about the z-axis is {0:.3e} kg*m^2".format(val))
