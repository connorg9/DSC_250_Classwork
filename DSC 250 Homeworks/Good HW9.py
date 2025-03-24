
#HW 9-1

import numpy as np
import matplotlib.pyplot as plt

amount = 100 #"resolution" basically
xvals = np.linspace(-2, 2, amount)
yvals = np.linspace(-2, 2, amount)
grid = [[0] * amount for i in range(amount)]
#makes an array of zeros with the same size as amount:
# [ [0, 0, ..., 0]
#   [0, 0, ..., 0]
#            ... ] ]

for i in range(amount):
    for j in range(amount):
        c = xvals[i] + (yvals[j] * 1j) #for each of the values in both x and y (make y a complex number)
        z = [0 + 0j] #start z at 0, but make it a list so that it can be iterated later
        count = 0

        while abs(z[-1]) <= 2 and count < amount: #as long as |z| is not 2 or greater, and we haven't done the amount "resolution"
            z.append(z[-1]**2 + c)
            count += 1

        grid[j][i] = count #make a grid of the counts, since we are not showing z or c in the graph

plt.figure()
plt.imshow(grid)
plt.title("Mandelbrot Set")
plt.show()

