
#Fourier series

import numpy as np
import matplotlib.pyplot as plt

def dft(x, N):
    c = np.zeros_like(x)
    a = 0.75
    lamda = 1
    for i in range(1, N+1):
        k_n = (2 * np.pi * i) / lamda
        A_n = (2 / (np.pi * i)) * np.sin((np.pi * a * i) / lamda)

        for j in range(len(x)):
            c[j] += A_n * np.cos(k_n * x[j])

    return c


x = np.linspace(-2, 2, 1000)

y_2 = dft(x, 2)
y_10 = dft(x, 10)
y_100 = dft(x, 100)

plt.figure()
plt.plot(x, y_2, label="N = 2")
plt.plot(x, y_10, label="N = 10")
plt.plot(x, y_100, label="N = 100")
plt.title("Fourier Series for Square Wave")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(loc = "best")
plt.show()

#%%

import numpy as np
import matplotlib.pyplot as plt

stuff = np.loadtxt("/Users/connorgood/Downloads/DOW.txt", float)

y = np.fft.rfft(stuff)

plt.figure(figsize = (10, 8))

plt.subplot(4, 2, 1)
plt.plot(stuff)
plt.title("Original Signal")

plt.subplot(4, 2, 2)
plt.plot(abs(y))
plt.title("Coefficients")

minval = min(abs(y))
y_high = y.copy()
for i in range(len(y_high)):
    if i < minval:
        y_high[i] = 0
stuff_high = np.fft.irfft(y_high)
plt.subplot(4, 2, 3)
plt.plot(stuff_high)
plt.title("Highpass Filter")

plt.subplot(4, 2, 4)
plt.plot(abs(y_high))
plt.title("Highpass Coefficients")

maxval = max(abs(y))
y_low = y.copy()
for i in range(len(y_low)):
    if i > maxval:
        y_low[i] = 0
stuff_low = np.fft.irfft(y_low)
plt.subplot(4, 2, 5)
plt.plot(stuff_low)
plt.title("Lowpass Filter")

plt.subplot(4, 2, 6)
plt.plot(abs(y_low))
plt.title("Lowpass Coefficients")

t = 0.005 * max(abs(y))
y_mag = y.copy()
for i in range(len(y_mag)):
    if abs(y_mag[i]) < t:
        y_mag[i] = 0

stuff_mag = np.fft.irfft(y_mag)
plt.subplot(4, 2, 7)
plt.plot(stuff_mag)
plt.title("Magnitude Filter")

plt.subplot(4, 2, 8)
plt.plot(abs(y_mag))
plt.title("Magnitude Coefficients")

plt.tight_layout()
plt.show()