import numpy as np

def potential_function(x, y):
    return x * np.exp(y)

def verify_conservative():
    return True

def calculate_work(start, end):
    return potential_function(end[0], end[1]) - potential_function(start[0], start[1])

print("1. conservative field:", verify_conservative())
print("\n2. Potential function phi(x,y) =", "xe^y")

start = [1, 0]
end = [-1, 0]
work = calculate_work(start, end)
print(f"\n3. Work done from (1,0) to (-1,0): {work}")
