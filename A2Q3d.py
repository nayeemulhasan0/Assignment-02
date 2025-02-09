
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def temperature(x, y):
    return 3 * x**2 * y

def gradient(x, y):
    return np.array([6*x*y, 3*x**2])

def directional_derivative(point, direction):
    unit_direction = direction / np.linalg.norm(direction)
    grad = gradient(point[0], point[1])
    return np.dot(grad, unit_direction)

point = np.array([-1, 3/2])
direction = np.array([-1, -1/2])

grad_at_point = gradient(point[0], point[1])
dir_deriv = directional_derivative(point, direction)

print(f"Gradient at {point}: {grad_at_point}")
print(f"Directional derivative in direction {direction}: {dir_deriv}")

x = np.linspace(-2, 0, 100)
y = np.linspace(0, 2, 100)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)

for i in range(len(x)):
    for j in range(len(y)):
        Z[j,i] = directional_derivative(np.array([X[j,i], Y[j,i]]), direction)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('DirectionalDerivative')
plt.colorbar(surf)
plt.title('Directional Derivative Surf')
plt.show()

