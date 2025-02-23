import numpy as np
from scipy.integrate import quad

def integrand(t):
    # Parametric equations
    x = np.cos(t)
    y = np.sin(t)
    z = t
    
    # Derivatives for ds
    dx_dt = -np.sin(t)
    dy_dt = np.cos(t)
    dz_dt = 1
    
    # Calculate ds = sqrt((dx/dt)^2 + (dy/dt)^2 + (dz/dt)^2)
    ds_dt = np.sqrt(dx_dt**2 + dy_dt**2 + dz_dt**2)
    
    # Calculate xy + z^3
    function_value = x*y + z**3
    
    return function_value * ds_dt

# Integrate from 0 to π
result = quad(integrand, 0, np.pi)

print(f"The line integral is approximately {result[0]}")
