import numpy as np
from matplotlib import pyplot as plt
from scipy import stats


def analyze(method, loc = 0, scale = 1):

    x = np.linspace(method.ppf(0.01, loc = loc, scale = scale),
                    method.ppf(0.99, loc = loc, scale = scale))

    y = method.pdf(x, loc = loc, scale = scale)

    r = method.rvs(size = 1000, loc = loc, scale = scale)

    return x, y, r

plt.figure()
plt.subplot(131)
x, y, r = analyze(stats.uniform)
plt.plot(x, y)
plt.hist(r, density = True, alpha = 0.3)

plt.subplot(132)
x, y, r = analyze(stats.expon)
plt.plot(x, y)
plt.hist(r, density = True, alpha = 0.3)

plt.subplot(133)
x, y, r = analyze(stats.norm)
plt.plot(x, y)
plt.hist(r, density = True, alpha = 0.3)

plt.tight_layout()
#plt.show()

#%%

A, B, C = [50], [50], [0]
k1 = 2
k2 = 20

N = 200
t = [0]

for step in range(N):
    R = A[-1] * B[-1] * k1 + C[-1] * k2

    if np.random.random() < A[-1] * B[-1] * k1/R:
        A.append(A[-1] - 1)
        B.append(B[-1] - 1)
        C.append(C[-1] + 1)

    else:
        A.append(A[-1] + 1)
        B.append(B[-1] + 1)
        C.append(C[-1] - 1)

    t.append(t[-1] + float(stats.expon.rvs(size = 1, scale = 1/R)[0]))

plt.figure()
plt.plot(t, A, color = 'blue')
plt.plot(t, C, color = 'red')
plt.show()

#%%




