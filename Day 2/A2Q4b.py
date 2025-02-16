import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(15, 6))

# (i) 
ax1 = fig.add_subplot(121, projection='3d')
x = np.linspace(1, 7, 100)
y = np.linspace(-3, 3, 100)  # Reasonable y range
X, Y = np.meshgrid(x, y)
Z1 = Y**2 - 2*Y*np.cos(X)

surf1 = ax1.plot_surface(X, Y, Z1, cmap='viridis', alpha=0.8)
ax1.set_title('f(x,y) = y² - 2y·cos(x)')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('f(x,y)')

# (ii)
ax2 = fig.add_subplot(122, projection='3d')
x = np.linspace(0, 2*np.pi, 100)
y = np.linspace(0, 2*np.pi, 100)
X, Y = np.meshgrid(x, y)
Z2 = np.abs(np.sin(X) * np.sin(Y))

surf2 = ax2.plot_surface(X, Y, Z2, cmap='plasma', alpha=0.8)
ax2.set_title('f(x,y) = |sin(x)·sin(y)|')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('f(x,y)')

fig.colorbar(surf1, ax=ax1, shrink=0.5)
fig.colorbar(surf2, ax=ax2, shrink=0.5)

plt.tight_layout()
plt.show()