import numpy as np
from scipy import integrate

def integrand(theta, phi):
    x = np.sin(theta) * np.cos(phi)
    return x**2 * np.sin(theta)

def calculate_surface_integral():
    theta_limits = [0, np.pi]      
    phi_limits = [0, 2*np.pi]      
    
    result, error = integrate.dblquad(
        integrand,              
        phi_limits[0],         
        phi_limits[1],         
        lambda x: theta_limits[0],  
        lambda x: theta_limits[1]   
    )
    
    return result

result = calculate_surface_integral()
print(f"The surface integral of x² over the unit sphere is: {result:.6f}")

