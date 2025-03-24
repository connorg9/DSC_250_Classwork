import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation


xvals = np.linspace(0, 6 * np.pi, 1000)
yvals = np.sin(xvals)

fig = plt.figure()

ax = fig.add_subplot(111)
plt.plot(xvals, yvals)
line, = plt.plot([], [])
marker = ax.scatter([], [])
ax.set_xlim(1.1 * min(xvals), 1.1 * max(xvals))
ax.set_ylim(1.1 * min(yvals), 1.1 * max(yvals))

def update(i):
    line.set_data(xvals[:i], yvals[:i])
    marker.set_offsets([xvals[i], yvals[i]])
    return line,
anim = animation.FuncAnimation(fig, update, frames = 1000, interval = 20, repeat_delay = 300)
plt.show()
