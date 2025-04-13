import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def f(x):
    return np.exp(-x**2/(2*sigma**2))/(2*np.pi*sigma**2)**0.5

s_vals = np.arange(0.5, 20.5, 4)
for sigma in s_vals:
    val, error = integrate.quad(f, -np.inf, np.inf)
    print(sigma, val, error)

