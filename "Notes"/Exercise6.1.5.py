import numpy as np

a = np.linspace(1, 48, 48).reshape(3, 4, 4)

print(a[1][0][3])
print(a[0][2])
print(a[2])
print(a[:, 1, :2])

