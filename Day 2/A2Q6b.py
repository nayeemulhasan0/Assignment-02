import numpy as np
from scipy import integrate

def integrand(y, x):
    return np.sqrt(4/(4-x**2))

def calculate_surface_area():
    x_limits = [0, 1]
    y_limits = [0, 4]
    
    # Since the integrand doesn't depend on y,
    # we can first multiply by the y-interval (which is 4)
    # and then integrate with respect to x
    def simplified_integrand(x):
        return 4 * np.sqrt(4/(4-x**2))
    
    result, error = integrate.quad(simplified_integrand, 0, 1)
    return result

if __name__ == "__main__":
    area = calculate_surface_area()
    print(f"The surface area is approximately {area:.6f} square units")