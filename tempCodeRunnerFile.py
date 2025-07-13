from scipy.optimize import minimize
import numpy as np

def objective(x):
    return -(8*x[0]**2 + 4*x[1]*x[2] - 16*x[2] + 600)  # Negative because we minimize

def constraint(x):
    return 4*x[0]**2 + x[1]**2 + 4*x[2]**2 - 16

# Initial guess
x0 = [1, 1, 1]

# Define constraint
con = {'type': 'eq', 'fun': constraint}

# Solve
result = minimize(objective, x0, constraints=con)

# Print results
print(f"Hottest point (x, y, z): {result.x}")
print(f"Maximum temperature: {-result.fun}")  # Remove negative since we minimized negative function