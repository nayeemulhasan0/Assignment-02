def calculate_avg_temp():
    # Number of points for approximation
    nx, ny = 100, 100
    
    # Step sizes
    dx = 1.0 / nx
    dy = 2.0 / ny
    
    total = 0
    points = 0
    
    # Sum up temperatures at many points
    for i in range(nx + 1):
        x = i * dx
        for j in range(ny + 1):
            y = j * dy
            # Temperature function T(x,y) = 10 - 8x² - 2y²
            temp = 10 - 8*x**2 - 2*y**2
            total += temp
            points += 1
    
    # Calculate average
    average = total / points
    return average

# Calculate and print result
result = calculate_avg_temp()
print(f"The average temperature is {result:.2f}°C")