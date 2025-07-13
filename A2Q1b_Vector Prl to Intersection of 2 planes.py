import numpy as np

def find_intersection_vector():

    n1 = np.array([3, -6, 2]) 
    n2 = np.array([2, 1, -2])  
    
    direction_vector = np.cross(n1, n2)
    
    unit_direction_vector = direction_vector / np.linalg.norm(direction_vector)
    
    return unit_direction_vector

direction = find_intersection_vector()
print(f"The direction vector parallel to the line of intersection is: {direction}")

