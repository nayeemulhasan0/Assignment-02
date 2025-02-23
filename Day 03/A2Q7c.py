import numpy as np
from scipy import integrate

def calculate_cylinder_mass(radius, height):

    def integrand(x, y, z):
        return x**2 + y**2
    
    def bounds_z(x, y):
        return [-height/2, height/2]
    
    def bounds_y(x):
        return [-np.sqrt(radius**2 - x**2), np.sqrt(radius**2 - x**2)]
    
    def bounds_x():
        return [-radius, radius]
    
    mass, error = integrate.nquad(
        integrand,
        [bounds_z, bounds_y, bounds_x]
    )
    
    return mass

mass = calculate_cylinder_mass(radius=2, height=3)

print(f"The mass of the cylinder is {mass:.2f} kg")