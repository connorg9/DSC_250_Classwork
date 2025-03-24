import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

q = 1
m = 1
B = 1

def f(r, t):
    theta, radius, z, z_velo = r
    a = 0.01
    qE = 0.05
    ftheta = (q * B) / m
    fr = a
    fz = z_velo
    fzv = qE
    return np.array([ftheta, fr, fz, fzv], float)


tpoints = np.linspace(0, 50, 1000)
init = [0, 1, 0, 0]

stuff1 = odeint(f, init, tpoints)
stuff2 = odeint(f, init, tpoints)

thetapoints = stuff1[:,0]
rpoints = stuff1[:,1]
xpoints = []
ypoints = []
zpoints = []

for i in range(len(thetapoints)):
    xpoints.append(rpoints[i] * np.cos(thetapoints[i]))
    ypoints.append(rpoints[i] * np.sin(thetapoints[i]))
    zpoints.append(stuff2[i][2])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(xpoints, ypoints, zpoints)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()
