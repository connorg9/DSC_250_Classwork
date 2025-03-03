import numpy as np

a1 = np.zeros(4, float)

a2 = np.zeros([3, 4], float)

a3 = np.ones([3, 4], float)

a4 = np.empty([3, 4], float)

r = [[1.0, 2, 3], [5.5, 4.4, 9]]

a5 = np.array(r, int)

print(a5)

#%%

def f(i, j):
    return i*j**2

a = np.fromfunction(f, (100, 100))
print(a)

#%%

import matplotlib.pyplot as plt
plt.imshow(a)
plt.show()

#%%

a =np.array([[1, 2, 3], [4, 5, 6]], float)
np.savetxt('../demo_array.txt', a)

b = np.loadtxt('../demo_array.txt')
print(b)




