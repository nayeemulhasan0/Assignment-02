import numpy as np

def compute_tnb_curve1(t):
    # r(t) = e^t i + e^t cos(t) j + e^t sin(t) k
    # First derivative (velocity)
    r_prime = np.array([np.exp(t), 
                       np.exp(t) * (np.cos(t) - np.sin(t)),
                       np.exp(t) * (np.sin(t) + np.cos(t))])
    
    # Second derivative (acceleration)
    r_double_prime = np.array([np.exp(t),
                              np.exp(t) * (-np.sin(t) - np.cos(t)),
                              np.exp(t) * (np.cos(t) - np.sin(t))])
    
    # Calculate T (tangent vector)
    T = r_prime / np.linalg.norm(r_prime)
    
    # Calculate cross product r' × r''
    cross_prod = np.cross(r_prime, r_double_prime)
    
    # Calculate B (binormal vector)
    B = cross_prod / np.linalg.norm(cross_prod)
    
    # Calculate N (normal vector)
    N = np.cross(B, T)
    
    # Calculate κ (curvature)
    kappa = np.linalg.norm(cross_prod) / (np.linalg.norm(r_prime) ** 3)
    
    # Calculate τ (torsion)
    r_triple_prime = np.array([np.exp(t),
                              np.exp(t) * (-np.cos(t) + np.sin(t)),
                              np.exp(t) * (-np.sin(t) - np.cos(t))])
    scalar_triple = np.dot(cross_prod, r_triple_prime)
    tau = scalar_triple / np.linalg.norm(cross_prod)**2
    
    return T, N, B, kappa, tau

def compute_tnb_curve2(t):
    # r(t) = 2cos(t)i + 3sin(t)j
    # First derivative
    r_prime = np.array([-2 * np.sin(t), 3 * np.cos(t), 0])
    
    # Second derivative
    r_double_prime = np.array([-2 * np.cos(t), -3 * np.sin(t), 0])
    
    # Calculate T
    T = r_prime / np.linalg.norm(r_prime)
    
    # Calculate cross product r' × r''
    cross_prod = np.cross(r_prime, r_double_prime)
    
    # Calculate B
    B = cross_prod / np.linalg.norm(cross_prod)
    
    # Calculate N
    N = np.cross(B, T)
    
    # Calculate κ
    kappa = np.linalg.norm(cross_prod) / (np.linalg.norm(r_prime) ** 3)
    
    # τ = 0 for planar curves
    tau = 0
    
    return T, N, B, kappa, tau

# Example usage
t = 0  # For curve 1 at t=0
T1, N1, B1, k1, tau1 = compute_tnb_curve1(t)

print("Curve 1 at t=0:")
print(f"T = {T1}")
print(f"N = {N1}")
print(f"B = {B1}")
print(f"κ = {k1}")
print(f"τ = {tau1}")

t = 0 # Example for curve 2
T2, N2, B2, k2, tau2 = compute_tnb_curve2(t)

print("\nCurve 2 at t=π/4:")
print(f"T = {T2}")
print(f"N = {N2}")
print(f"B = {B2}")
print(f"κ = {k2}")
print(f"τ = {tau2}")


####################################################################################################

import numpy as np
import matplotlib.pyplot as plt

def compute_kappa_curve1(t):
    # r'(t)
    r_prime = np.array([np.exp(t), 
                       np.exp(t) * (np.cos(t) - np.sin(t)),
                       np.exp(t) * (np.sin(t) + np.cos(t))])
    
    # r''(t)
    r_double_prime = np.array([np.exp(t),
                              np.exp(t) * (-np.sin(t) - np.cos(t)),
                              np.exp(t) * (np.cos(t) - np.sin(t))])
    
    # Calculate κ
    cross_prod = np.cross(r_prime, r_double_prime)
    kappa = np.linalg.norm(cross_prod) / (np.linalg.norm(r_prime) ** 3)
    return kappa

def compute_kappa_curve2(t):
    # r'(t)
    r_prime = np.array([-2 * np.sin(t), 3 * np.cos(t), 0])
    
    # r''(t)
    r_double_prime = np.array([-2 * np.cos(t), -3 * np.sin(t), 0])
    
    # Calculate κ
    cross_prod = np.cross(r_prime, r_double_prime)
    kappa = np.linalg.norm(cross_prod) / (np.linalg.norm(r_prime) ** 3)
    return kappa

# Generate points for plotting
t1 = np.linspace(0, 2, 1000)  # For curve 1
t2 = np.linspace(0, 2*np.pi, 1000)  # For curve 2

# Calculate κ values
kappa1 = [compute_kappa_curve1(t) for t in t1]
kappa2 = [compute_kappa_curve2(t) for t in t2]

# Create plots
plt.figure(figsize=(12, 5))

# Plot for Curve 1
plt.subplot(1, 2, 1)
plt.plot(t1, kappa1, 'b-', label='κ(t)')
plt.title('Curvature for Curve 1')
plt.xlabel('t')
plt.ylabel('κ(t)')
plt.grid(True)
plt.legend()

# Plot for Curve 2
plt.subplot(1, 2, 2)
plt.plot(t2, kappa2, 'r-', label='κ(t)')
plt.title('Curvature for Curve 2')
plt.xlabel('t')
plt.ylabel('κ(t)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# Print some specific values
print("Curve 1 κ(t) at t=0:", compute_kappa_curve1(0))
print("Curve 2 κ(t) at t=0:", compute_kappa_curve2(0))
print("Curve 2 κ(t) at t=π/2:", compute_kappa_curve2(np.pi/2))





