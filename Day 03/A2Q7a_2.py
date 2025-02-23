def calculate_avg_temp():
    nx, ny = 100, 100
    
    dx = 1.0 / nx
    dy = 2.0 / ny
    
    total = 0
    points = 0
    
    for i in range(nx + 1):
        x = i * dx
        for j in range(ny + 1):
            y = j * dy
            temp = 10 - 8*x**2 - 2*y**2
            total += temp
            points += 1
    
    average = total / points
    return average

result = calculate_avg_temp()
print(f"The average temperature is {result:.2f} C")
