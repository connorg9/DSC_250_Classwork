import numpy as np

R1 = 0.5
R2 = 2.5
R3 = 1.5

a = [[1, -1, -1],
     [6, 3, 0],
     [6, 0, 2]]

b = [0, 18, 45]

solve = np.linalg.solve(a, b)
print(solve)

