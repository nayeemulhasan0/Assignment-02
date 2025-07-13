import numpy as np
from scipy import integrate

def integrand(theta, phi):
    # x = sin(theta)cos(phi) in spherical coordinates
    # Surface element dS = sin(theta) for unit sphere
    x = np.sin(theta) * np.cos(phi)
    return x**2 * np.sin(theta)

def calculate_surface_integral():
    # Integration limits
    theta_limits = [0, np.pi]      # theta goes from 0 to pi
    phi_limits = [0, 2*np.pi]      # phi goes from 0 to 2pi
    
    # Compute double integral
    result, error = integrate.dblquad(
        integrand,              # function to integrate
        phi_limits[0],         # lower phi limit
        phi_limits[1],         # upper phi limit
        lambda x: theta_limits[0],  # lower theta limit
        lambda x: theta_limits[1]   # upper theta limit
    )
    
    return result

# Calculate and display result
result = calculate_surface_integral()
print(f"The surface integral of x² over the unit sphere is: {result:.6f}")

