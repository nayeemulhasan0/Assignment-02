import numpy as np
from scipy.integrate import quad

def integrand(t):
    x = np.cos(t)
    y = np.sin(t)
    z = t
    
    dx_dt = -np.sin(t)
    dy_dt = np.cos(t)
    dz_dt = 1
    
    ds_dt = np.sqrt(dx_dt**2 + dy_dt**2 + dz_dt**2)
    ans= x*y + z**3
    
    return ans * ds_dt

result = quad(integrand, 0, np.pi)

print(f"the line integral is approximately {result[0]}")
