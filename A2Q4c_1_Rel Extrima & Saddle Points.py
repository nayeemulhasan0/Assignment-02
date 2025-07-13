import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the functions
def f1(x, y):
    return 4*x*y - x**4 - y**4

def f2(x, y):
    return 4*x**2*np.exp(y) - 2*x**4 - np.exp(4*y)

# Create grid
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z1 = f1(X, Y)
Z2 = f2(X, Y)

# Plot both functions with critical points
fig = plt.figure(figsize=(12, 5))

# Function (i)
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z1, cmap='viridis', alpha=0.8)
ax1.scatter(0, 0, f1(0, 0), color='red', s=100, label='Saddle')
ax1.scatter(1, 1, f1(1, 1), color='green', s=100, label='Maximum')
ax1.set_title('f(x,y) = 4xy - x⁴ - y⁴')
ax1.legend()

# Function (ii)
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, Z2, cmap='viridis', alpha=0.8)
ax2.scatter(0, 0, f2(0, 0), color='red', s=100, label='Saddle')
ax2.scatter(1, 0, f2(1, 0), color='green', s=100, label='Maximum')
ax2.scatter(-1, 0, f2(-1, 0), color='green', s=100)
ax2.set_title('f(x,y) = 4x²e^y - 2x⁴ - e^(4y)')
ax2.legend()

plt.tight_layout()
plt.show()