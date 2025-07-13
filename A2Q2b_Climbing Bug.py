
import numpy as np
import matplotlib.pyplot as plt

# Parametric equation of helix
def helix(t):
    return np.cos(t), np.sin(t), t

# Compute arc length parameterization
t = np.linspace(0, 10, 100)
ds_dt = np.sqrt(1 + np.cos(t)**2 + np.sin(t)**2)  # Speed
s = np.trapz(ds_dt, t)  # Approximate arc length

# Reparametrize using arc length
s_final = 10  # Given arc length to walk
t_final = np.sqrt(s_final**2 / 2)  # Solving for t in arc length equation

# Compute final position
x_final, y_final, z_final = helix(t_final)
print(f"Final Position: ({x_final:.2f}, {y_final:.2f}, {z_final:.2f})")

# Plot helix
t_vals = np.linspace(0, t_final, 100)
x_vals, y_vals, z_vals = helix(t_vals)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_vals, y_vals, z_vals, label="Helix Path")
ax.scatter([x_final], [y_final], [z_final], color='red', label="Final Position")
ax.legend()
plt.show()

