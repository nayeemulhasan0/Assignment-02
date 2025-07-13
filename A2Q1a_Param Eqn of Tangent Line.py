import numpy as np

# Curve 1: t0 = 2
t0 = 2
r1 = np.array([np.log(t0), np.exp(-t0), t0**2])                  
r1_prime = np.array([1/t0, -np.exp(-t0), 2*t0])    

print("curve 1 tangent line (t0 = 2):")
print(f"x = {r1[0] } + {r1_prime[0] }s")
print(f"y = {r1[1] } + {r1_prime[1] }s")
print(f"z = {r1[2] } + {r1_prime[2] }s\n")

# Curve 2: t0 = 1/3
t0 = 1/3
r2 = np.array([2*np.cos(np.pi*t0), 2*np.sin(np.pi*t0), 3*t0])   
r2_prime = np.array([-2*np.pi*np.sin(np.pi*t0),2*np.pi*np.cos(np.pi*t0),3])

print("curve 2 tangent line (t0 = 1/3):")
print(f"x = {r2[0] } + {r2_prime[0] }s")
print(f"y = {r2[1] } + {r2_prime[1] }s")
print(f"z = {r2[2] } + {r2_prime[2] }s")

