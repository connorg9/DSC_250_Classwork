
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def f(r):
    B = 0.5
    C = 0.5
    D = 2.0
    x, y = r[0], r[1]
    fx = A * x - (B * x * y)
    fy = (C * x * y) - D * y
    return np.array([fx, fy], float)




xpoints = []
ypoints = []

def loop(A):
    r = [2.0, 2.0]
    rpoints = odeint(f, r, tpoints, args = (A,))
    return rpoints[:, 0], rpoints[:, 1], max(rpoints[:, 1])

tpoints = np.arange(0, 20, 1000)
max_preds = []

plt.figure()
plt.subplot(211)
trial1_prey, trial1_pred, max_pred = loop(1)
max_preds.append(max_pred)
plt.plot(tpoints, trial1_prey, c = "r", label = "Lions")
plt.plot(tpoints, trial1_pred, c = "b", linestyle = "--", label = "Antelope")
plt.subplot(212)
trial2_prey, trial2_pred, max_pred = loop(1.5)
max_preds.append(max_pred)
trial3_prey, trial3_pred, max_pred = loop(1.8)
max_preds.append(max_pred)
trial4_prey, trial4_pred, max_pred = loop(2.1)
max_preds.append(max_pred)
plt.plot(trial1_prey, trial1_pred, c = "r", label = "1")
plt.plot(trial2_prey, trial2_pred, c = "b", linestyle = "--", label = "2")
plt.plot(trial3_prey, trial3_pred, c = "g", linestyle = ":", label = "3")
plt.plot(trial4_prey, trial4_pred, c = "k", linestyle = "-.", label = "4")
plt.legend(loc = "best")
plt.show()

#%%

