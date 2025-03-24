import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(r, t):
    x1, y1, x2, y2, vx1, vy1, vx2, vy2= r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]
    fx1 = vx1
    fy1 = vy1
    fx2 = vx2
    fy2 = vy2
    return np.array([fx1, fy1, fx2, fy2], float)


