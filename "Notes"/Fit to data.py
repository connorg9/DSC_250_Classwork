import random
import matplotlib.pyplot as plt
import numpy as np

Polynomial = np.polynomial.Polynomial

xvals = np.linspace(-10, 10, 100)
yvals = [(x + 0.1 * x * random.random()) ** 2 for x in xvals]

p, stats = Polynomial.fit(xvals, yvals, 2, full=True)

y_fit = p(xvals)

plt.figure()
plt.scatter(xvals, yvals, s = 5, c = 'k')
plt.plot(xvals, y_fit, c = 'g')
plt.show()

print("Residual = ", stats[0])

print(p)