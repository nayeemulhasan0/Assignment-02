import sympy as sp

def solve_lagrange():
    # Define variables
    x, y, z, lambda_mul = sp.symbols('x y z lambda')
    
    # Define the function to maximize
    T = 8*x**2 + 4*y*z - 16*z + 600
    
    # Define the constraint
    g = 4*x**2 + y**2 + 4*z**2 - 16
    
    # Calculate partial derivatives
    dL_dx = sp.diff(T, x) - lambda_mul * sp.diff(g, x)
    dL_dy = sp.diff(T, y) - lambda_mul * sp.diff(g, y)
    dL_dz = sp.diff(T, z) - lambda_mul * sp.diff(g, z)
    
    # Set up system of equations
    equations = [
        dL_dx,  # = 0
        dL_dy,  # = 0
        dL_dz,  # = 0
        g      # = 0
    ]
    
    # Solve the system of equations
    solution = sp.solve(equations, (x, y, z, lambda_mul))
    
    # Find the maximum temperature
    max_temp = float('inf')
    max_point = None
    
    for sol in solution:
        if all(isinstance(val, sp.Number) for val in sol[:3]):  # Check if solution is real
            point_temp = T.subs([(x, sol[0]), (y, sol[1]), (z, sol[2])])
            if point_temp < max_temp:
                max_temp = point_temp
                max_point = sol[:3]
    
    return max_point, max_temp

# Solve and print results
point, temp = solve_lagrange()
print(f"Hottest point coordinates (x, y, z): {point}")
print(f"Maximum temperature: {temp}")