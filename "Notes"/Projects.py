import numpy as np
from scipy.integrate import quad, dblquad
import matplotlib.pyplot as plt

k = 1.38e-23
V = .001
p = 6.022e28
theta = 428

def heat_capacity(x):
    return ((x**4)*np.exp(x)) / ((np.exp(x) - 1)**2)

def heat_function(T):
    val, error = quad(heat_capacity, 0,theta/T)
    return 9 * V * p * k * ((T / theta)**3) * val

Cv = []
for T in np.linspace(5,500,1000):
    Cv.append(heat_function(T))

plt.plot(Cv)
plt.title("Heat Capacity of a solid by temperature")
plt.xlabel("Temperature")
plt.ylabel("Heat Capacity")
plt.show()

#%%

lambduh = 1
z = 3

def C(t):
    return np.cos((1/2) * np.pi * (t**2))

def S(t):
    return np.sin((1/2) * np.pi * (t**2))

def diffraction(x):

    c, error = quad(C, 0, x * np.sqrt(2 / (lambduh * z)))
    s, error = quad(S, 0, x * np.sqrt(2 / (lambduh * z)))

    return (1/8) * (((2 * c + 1)**2) + ((2 * s + 1)**2))

answers = []
x_vals = []
range = np.linspace(-5, 5, 1000)
for x in range:
    x_vals.append(x)
    answers.append(diffraction(x))

plt.plot(x_vals, answers)
plt.title("Diffraction of sound by location")
plt.ylabel("I/I0")
plt.xlabel("x")
plt.show()


#%%
m = 10**4
L = 10
G = 6.674e-11
sigma = m / (L**2)

def f(y, x):
    print(y,x,z)
    return 1 / ((x**2 * y**2 * z**2)**3/2)

def force(z):
    integral, error = dblquad(f, -5, 5, -5, 5)
    return G * sigma * z * integral

answers = []
z_vals = []
for z in np.linspace(.01, 10, 1000):
    z_vals.append(z)
    answers.append(force(z))

plt.plot(z_vals, answers)
plt.title("Force of gravity on sheet")
plt.xlabel("z")
plt.ylabel("Force")
plt.show()






