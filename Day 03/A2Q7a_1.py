import numpy as np
from scipy import integrate

def avg_temperature():
    def T(x, y):
        return 10 - 8*x**2 - 2*y**2
    
    total_temp, _ = integrate.dblquad(
        T,                
        0, 2,            
        lambda y: 0,     
        lambda y: 1     
    )
    area = 1 * 2  

    avg_temp = total_temp / area
    return avg_temp

result = avg_temperature()
print(f"The average temperature is {result:.2f} C")

