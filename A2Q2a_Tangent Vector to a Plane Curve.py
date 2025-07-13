import numpy as np
import matplotlib.pyplot as plt

# Define time points
t = np.linspace(0, 2*np.pi, 1000)
pi4 = np.pi/4

# Position vectors
x = 5*np.cos(t)
y = 4*np.sin(t)

# Calculate specific position vectors
r_pi4 = np.array([5*np.cos(pi4), 4*np.sin(pi4)])
r_pi = np.array([5*np.cos(np.pi), 4*np.sin(np.pi)])

# Calculate tangent vectors (derivative of position vector)
# r'(t) = [-5sin(t)i + 4cos(t)j]
tangent_pi4 = np.array([-5*np.sin(pi4), 4*np.cos(pi4)])
tangent_pi = np.array([-5*np.sin(np.pi), 4*np.cos(np.pi)])

# Plotting
plt.figure(figsize=(10, 10))
plt.plot(x, y, 'b-', label='Curve C')

# Plot position vectors
plt.quiver(0, 0, r_pi4[0], r_pi4[1], angles='xy', scale_units='xy', scale=1, color='r', label='r(π/4)')
plt.quiver(0, 0, r_pi[0], r_pi[1], angles='xy', scale_units='xy', scale=1, color='g', label='r(π)')

# Plot tangent vectors (from position points)
plt.quiver(r_pi4[0], r_pi4[1], tangent_pi4[0], tangent_pi4[1], 
          angles='xy', scale_units='xy', scale=5, color='orange', label='r\'(π/4)')
plt.quiver(r_pi[0], r_pi[1], tangent_pi[0], tangent_pi[1], 
          angles='xy', scale_units='xy', scale=5, color='purple', label='r\'(π)')

plt.grid(True)
plt.axis('equal')
plt.legend()
plt.title('Curve C with Position and Tangent Vectors')
plt.xlabel('x')
plt.ylabel('y')

# Print the vectors
print(f"Position vector at t=π/4: {r_pi4}")
print(f"Position vector at t=π: {r_pi}")
print(f"Tangent vector at t=π/4: {tangent_pi4}")
print(f"Tangent vector at t=π: {tangent_pi}")

plt.show()