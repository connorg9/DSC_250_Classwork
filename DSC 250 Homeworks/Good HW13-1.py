import numpy as np
import random

from matplotlib import pyplot as plt

L = 100
d = 2

count = 0
theta = random.uniform(0, 2*np.pi)

x = random.random()
x = x * 2

end_1 = [50 * np.cos(theta), 50 * np.sin(theta)] #horizontal component, vertical component
end_2 = [-end_1[0], -end_1[1]] #negatives of the first end, since symmetrical

coord_1 = [end_1[0] + x, end_1[1]]
coord_2 = [end_2[0] + x, end_2[1]]

if end_2[0] < 0 or end_1[0] < 0:
#if x-coord of either end (since theta can be all the way around) is < 0 (on left side of left line), add one
    count += 1
if end_1[0] > d or end_2[0] > d:
#if x-coord of either end is > d, add one
    count += 1


print(end_1)
print(end_2)
print(count)

plt.plot(coord_1, coord_2)
plt.vlines(0, -100, 100, linestyle='--')
plt.vlines(d, -100, 100, linestyle='--')
plt.xlim(-100, 100)
plt.ylim(-100, 100)
plt.show()