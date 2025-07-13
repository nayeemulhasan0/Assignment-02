import numpy as np
from scipy import integrate

def calculate_volume():
    def integrand(y, x):
        # z = 4 - x^2 - y^2 is the upper bound
        # z = 0 (xy-plane) is the lower bound
        # The volume is the difference between upper and lower bounds
        return 4 - x**2 - y**2
    
    def y_limits(x):
        # From the cylinder equation (x-1)^2 + y^2 = 1
        # Solve for y: y = ±√(1 - (x-1)^2)
        return [-np.sqrt(1 - (x-1)**2), np.sqrt(1 - (x-1)**2)]
    
    # x limits are from the cylinder equation
    # When y = 0, (x-1)^2 = 1
    # So x goes from 0 to 2
    x_limits = [0, 2]
    
    # Calculate the volume using double integral
    result, error = integrate.nquad(
        integrand,
        [
            lambda x: y_limits(x),  # y limits are functions of x
            x_limits                # x limits are constants
        ]
    )
    
    return result

if __name__ == "__main__":
    volume = calculate_volume()
    print(f"The volume of the solid is approximately {volume:.6f} cubic units")