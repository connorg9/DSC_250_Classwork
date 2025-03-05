import numpy as np
import matplotlib.pyplot as plt

def func(T):
    p = []
    for i in np.linspace(0.34, 5, 100):
        x = (8 * T) / (3 * i - 1) - (3 / (i ** 2))
        p.append(x)
    return p

xvals = []
for i in np.linspace(0.34, 5, 100):
    xvals.append(i)

list1 = func(1)
list2 = func(0.9)
list3 = func(1.1)

plt.figure()
plt.plot(xvals,list1, label = "T = 1")
plt.plot(xvals,list2, label = "T = 0.9")
plt.plot(xvals,list3, label = "T = 1.1")
plt.ylabel("Pressure (Pa)")
plt.xlabel("Volume")
plt.ylim(0, 3)
plt.legend(loc = "best")
plt.show()

#%%

a = .428
b = 3.71e-5
R = 8.314

T = (8 * a) / (27 * R * b)
p = a / (27 * (b ** 2))
print("Critical temp: ", T, "Critical pressure: ", p)

T = 298
p = 101235
eq = np.polynomial.Polynomial([-a * b, a, -(p * b + R * T), p])
answers = eq.roots()
print("Molar volume of liquid: ", answers[0])
print("Molar volume of gas: ", answers[2])

T = 500
p = 12000000
eq = np.polynomial.Polynomial([-a * b, a, -(p * b + R * T), p])
answers = eq.roots()
print("Molar volume of supercritical fluid: {0:.5f}".format(answers[2].real))

#%%


