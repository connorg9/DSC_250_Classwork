
import numpy as np
import matplotlib.pyplot as plt
from cmath import exp

def dft(y):
    N = len(y)
    c = np.zeros(N, complex)
    for k in range(N):
        for n in range(N):
            c[k] += y[n] * exp(-2j * np.pi * k * n / N)
    return c

def idft(c):
    N = len(c)
    y = np.zeros(N, complex)
    for n in range(N):
        for k in range(N):
            y[n] += c[k] * exp(2j * np.pi * k * n / N)
    return y/N

y = np.loadtxt("/Users/connorgood/Downloads/pitch.txt", float)
c = dft(y)

for i in range(len(c)):
    if abs(c[i]) < 30:
        c[i] = 0

y2 = idft(c)

plt.figure()
plt.subplot(311)
plt.plot(y)
plt.xlabel("Time")
plt.ylabel("Signal")

plt.subplot(312)
plt.plot(np.abs(c))
plt.xlabel("Fourier Coefficients")
plt.ylabel("Magnitude")

plt.subplot(313)
plt.plot(y2)
plt.xlabel("Time")
plt.ylabel("Signal")
plt.show()

#%%

fft = np.fft
y = np.loadtxt("/Users/connorgood/Downloads/pitch.txt", float)
c = fft.rfft(y)
y2 = fft.irfft(c)

plt.figure()
plt.subplot(311)
plt.plot(y)
plt.xlabel("Time")
plt.ylabel("Signal")

plt.subplot(312)
plt.plot(np.abs(c))
plt.xlabel("Fourier Coefficients")
plt.ylabel("Magnitude")

plt.subplot(313)
plt.plot(y2.real)
plt.xlabel("Time")
plt.ylabel("Signal")
plt.show()

#%%

from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

sample_rate, wav = wavfile.read("/Users/connorgood/Downloads/WilhelmScream.wav")

s1 = wav[:, 0]
s2 = wav[:, 1]

s1_fft = np.fft.rfft(s1)
s2_fft = np.fft.rfft(s2)

plt.figure()
plt.subplot(221)
plt.plot(s1, "g")
plt.xlabel("Time")
plt.ylabel("Signal")

plt.subplot(223)
plt.plot(s2, "r")
plt.xlabel("Fourier Coefficients")
plt.ylabel("Magnitude")

plt.subplot(222)
plt.plot(abs(s1_fft), "g")

plt.subplot(224)
plt.plot(abs(s2_fft), "r")
plt.xlabel("FFT")

plt.show()
