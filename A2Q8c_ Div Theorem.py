import numpy as np
from scipy import integrate

def calculate_flux():
    # The divergence of F is div F = ∂F₁/∂x + ∂F₂/∂y + ∂F₃/∂z
    # For F = xî + y³ĵ + z²k̂, div F = 1 + 3y² + 2z
    
    def integrand(z, r, theta):
        # Convert to cylindrical coordinates
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        
        # Divergence in terms of r, theta, z
        divergence = 1 + 3 * (r * np.sin(theta))**2 + 2*z
        
        # Include r for cylindrical coordinates volume element
        return divergence * r

    # Set up the integration bounds
    r_lower = 0
    r_upper = 3  # sqrt(9) = 3 for x² + y² = 9
    theta_lower = 0
    theta_upper = 2 * np.pi
    z_lower = 0
    z_upper = 2

    # Perform triple integration
    result, error = integrate.tplquad(
        integrand,
        theta_lower, theta_upper,    # theta bounds
        lambda theta: r_lower, lambda theta: r_upper,  # r bounds
        lambda r, theta: z_lower, lambda r, theta: z_upper  # z bounds
    )
    
    return result

# Calculate and display the result
flux = calculate_flux()
print(f"The outward flux is approximately {flux:.4f}")
