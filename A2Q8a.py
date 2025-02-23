import numpy as np
from scipy import integrate

def calculate_work():
    # For Green's Theorem, we need to calculate ∂Q/∂x - ∂P/∂y
    # where P = e^x - y^3 and Q = cos(y) + x^3
    
    def integrand(x, y):
        # ∂Q/∂x = 3x^2
        # ∂P/∂y = -3y^2
        # ∂Q/∂x - ∂P/∂y = 3x^2 + 3y^2
        return 3*x**2 + 3*y**2
    
    # For unit circle, we can use polar coordinates
    def bounds(theta):
        # x = cos(theta), y = sin(theta)
        x = np.cos(theta)
        y = np.sin(theta)
        return integrand(x, y)
    
    # Area integral becomes a line integral
    # Multiply by radius (which is 1 in this case)
    work = integrate.quad(bounds, 0, 2*np.pi)[0]
    
    return work

# Calculate and display the result
result = calculate_work()
print(f"The work done by the force field is: {result:.4f}")