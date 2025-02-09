import math

def calculate_dw_dtheta(theta):
    x = math.cos(theta)
    y = math.sin(theta)
    z = math.tan(theta)
    
    w = math.sqrt(x**2 + y**2 + z**2)
    
    dx_dtheta = -math.sin(theta) 
    dy_dtheta = math.cos(theta)  
    dz_dtheta = 1/math.cos(theta)**2 
    
    dw_dtheta = (1/(2*w)) * (2*x*dx_dtheta + 2*y*dy_dtheta + 2*z*dz_dtheta)
    return dw_dtheta

theta = math.pi/4
result = calculate_dw_dtheta(theta)
print(f" at θ= π/4, dw/dθ: {result}")

