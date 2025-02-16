import numpy as np
import matplotlib.pyplot as plt

# Create grid of points
x = np.linspace(-10, 10, 300)
y = np.linspace(-10, 10, 300)
X, Y = np.meshgrid(x, y)

# Specified height values
levels = [1, 4, 9, 16, 26, 36]

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# (i) f(x,y) = 4x^2 + y^2
Z1 = 4*X**2 + Y**2
cs1 = ax1.contour(X, Y, Z1, levels=levels)
ax1.clabel(cs1, inline=True, fontsize=10)
ax1.set_title('f(x,y) = 4x² + y²')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.grid(True)
ax1.axis('equal')

# (ii) f(x,y,z) = z^2 - x^2 - y^2 with z=8
z_fixed = 8
Z2 = z_fixed**2 - X**2 - Y**2
cs2 = ax2.contour(X, Y, Z2, levels=levels)
ax2.clabel(cs2, inline=True, fontsize=10)
ax2.set_title(f'f(x,y,z) = z² - x² - y² with z={z_fixed}')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.grid(True)
ax2.axis('equal')

plt.tight_layout()
plt.show()