import numpy as np
from scipy import integrate

def triple_integral():
    def integrand(z, y, x):
        return x * np.exp(-y) * np.cos(z)
    
    def z_limits(y, x):
        return [3, 4-x**2-y**2]
    
    def y_limits(x):
        return [0, 1-x**2]
    
    x_limits = [0, 1]
    
    result, error = integrate.nquad(
        integrand,
        [
            lambda x, y: z_limits(y, x),  # z limits
            lambda x: y_limits(x),        # y limits
            x_limits                      # x limits
        ]
    )
    return result

def double_integral():
    def integrand(y, x):
        return (x * y) / np.sqrt(x**2 + y**2 + 1)
    
    x_limits = [0, 1]
    y_limits = [0, 1]
    
    result, error = integrate.nquad(
        integrand,
        [y_limits, x_limits]
    )
    return result

if __name__ == "__main__":
    print("Result of triple integral (i):", triple_integral())
    print("Result of double integral (ii):", double_integral())