import numpy as np

def potential_function(x, y):
    """Potential function φ(x,y) = xe^y"""
    return x * np.exp(y)

def verify_conservative():
    """Verify if field is conservative"""
    # ∂P/∂y = ∂Q/∂x = e^y, therefore conservative
    return True

def calculate_work(start, end):
    """Calculate work from start to end point"""
    return potential_function(end[0], end[1]) - potential_function(start[0], start[1])

# Main calculations
print("1. Field is conservative:", verify_conservative())
print("\n2. Potential function φ(x,y) =", "xe^y")

# Calculate work from (1,0) to (-1,0)
start = [1, 0]
end = [-1, 0]
work = calculate_work(start, end)
print(f"\n3. Work done from (1,0) to (-1,0): {work}")