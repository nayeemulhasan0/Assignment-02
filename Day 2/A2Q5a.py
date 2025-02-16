import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

point = np.array([1, 2, 1])
grad = np.array([2*point[0], 8*point[1], 2*point[2]]) 
d = np.dot(grad, point)

tangent_plane_eq = f"{grad[0]}*x + {grad[1]}*y + {grad[2]}*z = {d}"
normal_line_eq = point + sp.symbols('t') * grad
angle_degrees = np.degrees(np.arccos(2 / np.linalg.norm(grad)))

print(f"Tangent plane: {tangent_plane_eq}")
print(f"Normal line: x = {normal_line_eq[0]}, y = {normal_line_eq[1]}, z = {normal_line_eq[2]}")
print(f"Angle with xy-plane: {angle_degrees:.2f}°")

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

u, v = np.meshgrid(np.linspace(0, 2*np.pi, 50), np.linspace(0, np.pi, 50))
x = 3 * np.cos(u) * np.sin(v)
y = 2.12 * np.sin(u) * np.sin(v)
z = 3 * np.cos(v)
ax.plot_surface(x, y, z, color='b', alpha=0.5)

xx, yy = np.meshgrid(np.linspace(-5, 5, 20), np.linspace(-5, 5, 20))
ax.plot_surface(xx, yy, (d - grad[0]*xx - grad[1]*yy)/grad[2], color='r', alpha=0.5)
t = np.linspace(-5, 5, 100)
ax.plot3D(point[0] + t*grad[0], point[1] + t*grad[1], point[2] + t*grad[2], 'g')
ax.scatter(*point, color='k', s=100)

ax.set(xlabel='X', ylabel='Y', zlabel='Z', 
       title='Ellipsoid with Tangent Plane and Normal Line',
       xlim=(-5, 5), ylim=(-5, 5), zlim=(-5, 5))
ax.set_box_aspect([1,1,1])
plt.show()


