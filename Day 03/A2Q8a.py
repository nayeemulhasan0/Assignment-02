import numpy as np
from scipy import integrate

def calculate_work():
    
    def integrand(x, y):
        return 3*x**2 + 3*y**2
    
    def bounds(theta):
        x = np.cos(theta)
        y = np.sin(theta)
        return integrand(x, y)
    
    work = integrate.quad(bounds, 0, 2*np.pi)[0]
    
    return work

result = calculate_work()
print(f"The work done by the force field is: {result:.4f}")