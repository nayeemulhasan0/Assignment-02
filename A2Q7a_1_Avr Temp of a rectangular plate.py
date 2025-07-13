import numpy as np
from scipy import integrate

def avg_temperature():
    # Temperature function
    def T(x, y):
        return 10 - 8*x**2 - 2*y**2
    
    # Calculate double integral of temperature function
    total_temp, _ = integrate.dblquad(
        T,                # function to integrate
        0, 2,            # y limits: 0 to 2
        lambda y: 0,      # x lower limit
        lambda y: 1       # x upper limit
    )
    
    # Area of the rectangle
    area = 1 * 2  # width * height
    
    # Average temperature = total temperature / area
    avg_temp = total_temp / area
    
    return avg_temp

# Calculate and print result
result = avg_temperature()
print(f"The average temperature is {result:.2f}°C")