import numpy as np
from scipy import integrate

def calculate_cylinder_mass(radius, height):
    """
    Calculate mass of a cylinder with density ρ(x,y) = x² + y²
    
    Parameters:
    radius: float - radius of cylinder
    height: float - height of cylinder
    
    Returns:
    float - mass of cylinder
    """
    
    def integrand(x, y, z):
        return x**2 + y**2
    
    # Define bounds for triple integral
    def bounds_z(x, y):
        return [-height/2, height/2]
    
    def bounds_y(x):
        return [-np.sqrt(radius**2 - x**2), np.sqrt(radius**2 - x**2)]
    
    def bounds_x():
        return [-radius, radius]
    
    # Compute triple integral
    mass, error = integrate.nquad(
        integrand,
        [bounds_z, bounds_y, bounds_x]
    )
    
    return mass

# Example usage:
mass = calculate_cylinder_mass(radius=2, height=3)

print(f"The mass of the cylinder is {mass:.2f} kg")