import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

e = 0.1 #eccentricity
x = 0.265 # (B - A) / C

def f(phi, r): #I tried using (r, phi) but the solve_ivp used later creates an error with that order

    theta = r[0]
    omega = r[1]

    r_a = (1 - (e ** 2)) / (1 + e * np.cos(phi)) #have to use r/a here, since a value for a is not specified yet

    d_theta = (r_a ** 2) * omega #original equation has a/r, but it is flipped when solved for dtheta/dphi
    d_omega = -x * (3 / (2 * (1 - (e ** 2)))) * (r_a ** -1) * (np.sin(2 * (theta - phi)))

    return np.array([d_theta, d_omega])

initial = np.array([0, 0]) #initial conditions

across = (0, 200) #solve_ivp takes a beginning and ending value to work across, not a linspace
solution = solve_ivp(f, across, initial, dense_output=True) #dense output used later for .sol

phi_points = np.linspace(0, 200, 10000)
y_points = solution.sol(phi_points)
theta_values = y_points[0]
omega_values = y_points[1]

"""
After looking at documentation, solve_ivp stores multiple things in the solution variable, one of which is a function
that can be calculated for continuous points. Simply graphing the theta and omega as solution.y[0] and y[1] creates a 
very rough graph that is not smooth at all. Calculating y_points from solution.sol() across a linspace results in the 
same values, but a much smoother curve. Dense_output must be used in the function call because otherwise the result 
will not contain that continuous equation. 
"""

initial2 = np.array([0, 2]) #second initial conditions
solution2 = solve_ivp(f, across, initial2, dense_output=True)

y2_points = solution2.sol(phi_points)
theta2_values = y2_points[0]
omega2_values = y2_points[1]

plt.figure()
plt.subplot(211)
plt.plot(phi_points, omega_values)
plt.xlabel("Phi")
plt.ylabel("Omega")
plt.title("Original")

plt.subplot(212)
plt.plot(phi_points, omega2_values)
plt.xlabel("Phi")
plt.ylabel("Omega")
plt.title("Adjusted initial conditions")
plt.tight_layout()
plt.show()