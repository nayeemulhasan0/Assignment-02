import numpy as np
from scipy import integrate

def line_integral():
    def integrand(t):
        # Simplified after substitution
        return 8  # This becomes constant after all substitutions
    return integrate.quad(integrand, 0, 2*np.pi)[0]

def surface_integral():
    def integrand(r, theta):
        # Simplified after substitution
        return 4 * r
    return integrate.dblquad(integrand, 0, 2*np.pi, 0, 2)[0]

line_result = line_integral()
surface_result = surface_integral()

print(f"Line integral = {line_result:.4f}")
print(f"Surface integral = {surface_result:.4f}")
