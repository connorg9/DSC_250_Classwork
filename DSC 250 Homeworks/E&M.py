import numpy as np
import matplotlib.pyplot as plt

tol = 0.0005
max_error = 100
yvals = []
test = []
xvals = []
error = []

for i in np.linspace(1, 5, 100):
    yvals.append(-i + 5)
    test.append(np.sin((np.pi / 2) * (i - 1)) + 5 - i)
    xvals.append(i)

while max_error > tol:
    for i in range(len(yvals)):
        if i == 0 or i == len(yvals) - 1:
            continue
        new = (test[i - 1] + test[i + 1]) / 2
        #
        test[i] = new
        error.append(abs(test[i] - yvals[i]))
        max_error = max(error)
    print(max_error)

plt.figure()
plt.plot(xvals, test, label = "computed")
plt.legend()
plt.show()

