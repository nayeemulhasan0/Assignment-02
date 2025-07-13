import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define symbols
t = sp.symbols('t')

# Position vector
r = sp.Array([3*t, sp.sin(t), t**2])

# Velocity and acceleration
v = r.diff(t)
a = v.diff(t)

# Compute theta(t)
theta = sp.atan(r[1] / r[0])

# Convert symbolic theta to a numerical function
f_theta = sp.lambdify(t, theta, 'numpy')

# Plot theta(t) vs t
t_vals = np.linspace(0.1, 10, 100)  # Avoid t=0 to prevent division issues
theta_vals = f_theta(t_vals)

plt.plot(t_vals, theta_vals, label=r'$\theta(t)$')
plt.xlabel('t')
plt.ylabel(r'$\theta(t)$')
plt.title(r'Plot of $\theta(t)$ vs $t$')
plt.legend()
plt.grid()
plt.show()

# Print results
print("Velocity:", v)
print("Acceleration:", a)
print("Theta(t):", theta)
