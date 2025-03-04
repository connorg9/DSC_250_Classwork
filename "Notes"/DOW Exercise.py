
import numpy as np
import matplotlib.pyplot as plt

stuff = np.loadtxt("/Users/connorgood/Downloads/DOW.txt", float)

y = np.fft.rfft(stuff)

maxval = max(y)
for i in range(len(y)):
    if abs(y[i]) < .005 * maxval:
        y[i] = 0

y2 = np.fft.irfft(y)

plt.figure()
plt.subplot(311)
plt.plot(stuff)
plt.subplot(312)
plt.plot(y)
plt.subplot(313)
plt.plot(y2)
plt.show()
