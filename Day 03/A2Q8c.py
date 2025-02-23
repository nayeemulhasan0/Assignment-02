import numpy as np
from scipy import integrate

def calculate_flux():
    
    def integrand(z, r, theta):
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        
        divergence = 1 + 3 * (r * np.sin(theta))**2 + 2*z
        
        return divergence * r

    r_lower = 0
    r_upper = 3 
    theta_lower = 0
    theta_upper = 2 * np.pi
    z_lower = 0
    z_upper = 2

    result, error = integrate.tplquad(
        integrand,
        theta_lower, theta_upper,   
        lambda theta: r_lower, lambda theta: r_upper,
        lambda r, theta: z_lower, lambda r, theta: z_upper  
    )
    
    return result

flux = calculate_flux()
print(f"The outward flux is approximately {flux:.4f}")

