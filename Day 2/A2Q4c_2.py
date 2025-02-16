import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the functions
def f1(x, y):
    return 4*x*y - x**4 - y**4

def f2(x, y):
    return 4*x**2*np.exp(y) - 2*x**4 - np.exp(4*y)

# Create a grid with appropriate bounds
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z1 = f1(X, Y)

# For function 2, we need to be careful with the exponential
# Let's use a more appropriate range for y
y2 = np.linspace(-4, 2, 100)  # Using lower y values to see structure better
x2 = np.linspace(-2, 2, 100)
X2, Y2 = np.meshgrid(x2, y2)
Z2 = f2(X2, Y2)

# Plot function (ii) with better visualization
fig = plt.figure(figsize=(15, 10))

# 3D surface plot
ax1 = fig.add_subplot(221, projection='3d')
surf = ax1.plot_surface(X2, Y2, Z2, cmap='viridis', alpha=0.8)
ax1.scatter(1, 0, f2(1, 0), color='green', s=100, label='Local maximum (1,0)')
ax1.scatter(-1, 0, f2(-1, 0), color='green', s=100, label='Local maximum (-1,0)')
ax1.scatter(0, 0, f2(0, 0), color='red', s=100, label='Saddle point (0,0)')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('f(x,y)')
ax1.view_init(elev=30, azim=30)  # Adjust viewing angle
ax1.set_title('3D plot of f(x,y) = 4x²e^y - 2x⁴ - e^(4y)')
ax1.legend()

# Contour plot
ax2 = fig.add_subplot(222)
contour = ax2.contour(X2, Y2, Z2, 20, cmap='viridis')
ax2.clabel(contour, inline=True, fontsize=8)
ax2.scatter(1, 0, color='green', s=100, marker='o', label='Local maximum')
ax2.scatter(-1, 0, color='green', s=100, marker='o')
ax2.scatter(0, 0, color='red', s=100, marker='x', label='Saddle point')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('Contour plot')
ax2.grid(True)
ax2.legend()

# Y-axis cross-section plot
ax3 = fig.add_subplot(223)
y_values = np.linspace(-4, 2, 100)
ax3.plot(y_values, f2(0, y_values), 'b-', label='f(0,y)')
ax3.plot(y_values, f2(0, y_values) * 0, 'k--', alpha=0.3)  # Zero line
ax3.scatter(0, f2(0, 0), color='red', s=100, marker='x')
ax3.set_xlabel('Y')
ax3.set_ylabel('f(0,y)')
ax3.set_title('Cross-section along Y-axis (x=0)')
ax3.grid(True)
ax3.legend()

# X-axis cross-section plot
ax4 = fig.add_subplot(224)
x_values = np.linspace(-2, 2, 100)
ax4.plot(x_values, f2(x_values, 0), 'r-', label='f(x,0)')
ax4.plot(x_values, f2(x_values, 0) * 0, 'k--', alpha=0.3)  # Zero line
ax4.scatter(1, f2(1, 0), color='green', s=100, marker='o')
ax4.scatter(-1, f2(-1, 0), color='green', s=100, marker='o')
ax4.scatter(0, f2(0, 0), color='red', s=100, marker='x')
ax4.set_xlabel('X')
ax4.set_ylabel('f(x,0)')
ax4.set_title('Cross-section along X-axis (y=0)')
ax4.grid(True)
ax4.legend()

plt.tight_layout()
plt.show()

# Print values at critical points
print(f"Function (ii): f(x,y) = 4x²e^y - 2x⁴ - e^(4y)")
print(f"At (0,0): f(0,0) = {f2(0,0)}")
print(f"At (1,0): f(1,0) = {f2(1,0)}")
print(f"At (-1,0): f(-1,0) = {f2(-1,0)}")

# Verify that points along y-axis are saddle points
y_test = [-2, -1, 0, 1]
for y_val in y_test:
    # Calculate second derivatives
    d2f_dx2 = 8 * np.exp(y_val)
    d2f_dy2 = -16 * np.exp(4*y_val)
    d2f_dxdy = 0
    # Calculate Hessian determinant
    D = d2f_dx2 * d2f_dy2 - d2f_dxdy**2
    print(f"At (0,{y_val}): f(0,{y_val}) = {f2(0,y_val)}, D = {D}")