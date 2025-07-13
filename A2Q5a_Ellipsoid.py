import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def create_ellipsoid_visualization():
    # Create the meshgrid for plotting
    x = np.linspace(-3, 3, 50)
    y = np.linspace(-3, 3, 50)
    X, Y = np.meshgrid(x, y)
    
    # Calculate Z for ellipsoid surface: x^2 + 4y^2 + z^2 = 18
    Z_pos = np.sqrt(18 - X**2 - 4*Y**2)
    Z_neg = -np.sqrt(18 - X**2 - 4*Y**2)
    
    # Point of tangency
    point = np.array([1, 2, 1])
    
    # Calculate normal vector at point (1,2,1)
    normal = np.array([2*point[0], 8*point[1], 2*point[2]])
    
    # Tangent plane equation: 2x + 16y + 2z = 20
    Z_plane = (20 - 2*X - 16*Y) / 2
    
    # Create 3D plot
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot ellipsoid
    mask = (18 - X**2 - 4*Y**2) >= 0
    ax.plot_surface(X*mask, Y*mask, Z_pos*mask, alpha=0.3, color='blue', label='Ellipsoid')
    ax.plot_surface(X*mask, Y*mask, Z_neg*mask, alpha=0.3, color='blue')
    
    # Plot tangent plane
    plane_x = np.linspace(0, 2, 20)
    plane_y = np.linspace(1, 3, 20)
    X_plane, Y_plane = np.meshgrid(plane_x, plane_y)
    Z_plane = (20 - 2*X_plane - 16*Y_plane) / 2
    ax.plot_surface(X_plane, Y_plane, Z_plane, alpha=0.5, color='red')
    
    # Plot point of tangency
    ax.scatter(*point, color='green', s=100, label='Point (1,2,1)')
    
    # Plot normal line
    t = np.linspace(-0.2, 0.2, 100)  # Shortened the line for better visualization
    normal_normalized = normal / np.linalg.norm(normal)
    normal_line = point.reshape(3, 1) + normal_normalized.reshape(3, 1) * t
    ax.plot(normal_line[0], normal_line[1], normal_line[2], 'g--', label='Normal Line')
    
    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Ellipsoid with Tangent Plane and Normal Line')
    
    # Add legend
    ax.legend()
    
    # Calculate angle with xy-plane (corrected)
    z_unit = np.array([0, 0, 1])  # Unit vector in z-direction
    normal_unit = normal / np.linalg.norm(normal)
    angle = np.arccos(np.abs(np.dot(normal_unit, z_unit)))
    angle_degrees = np.degrees(angle)
    
    print(f"Acute angle between tangent plane and xy-plane: {angle_degrees:.2f} degrees")
    
    plt.show()

# Run the visualization
create_ellipsoid_visualization()