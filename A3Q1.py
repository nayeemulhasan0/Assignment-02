import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def ode1(y, t): return t*np.exp(t) - 2*y
def exact1(t): return 0.5*t*np.exp(t) - 0.25*np.exp(t) + 0.25*np.exp(2*t)
def ode2(y, t): return 1 + (t - y)**2
def exact2(t): return t + 1/(1-t)

t1 = np.linspace(0, 1, 101)
y1 = odeint(ode1, 0, t1).flatten()
e1 = np.abs(y1 - exact1(t1))

t2 = np.linspace(2, 3, 101)
y2 = odeint(ode2, 1, t2).flatten()
e2 = np.abs(y2 - exact2(t2))

fig, axs = plt.subplots(2, 2, figsize=(12, 10))
axs[0, 0].plot(t1, y1, 'b-', t1, exact1(t1), 'r--')
axs[0, 0].set(title="Problem 1: Solution", xlabel="t", ylabel="y(t)")
axs[0, 0].legend(), axs[0, 0].grid()

axs[0, 1].semilogy(t1, e1, 'g-')
axs[0, 1].set(title="Problem 1: Error", xlabel="t", ylabel="Absolute Error")
axs[0, 1].grid()

axs[1, 0].plot(t2, y2, 'b-', t2, exact2(t2), 'r--')
axs[1, 0].set(title="Problem 2: Solution", xlabel="t", ylabel="y(t)")
axs[1, 0].legend(), axs[1, 0].grid()

axs[1, 1].semilogy(t2, e2, 'g-')
axs[1, 1].set(title="Problem 2: Error", xlabel="t", ylabel="Absolute Error")
axs[1, 1].grid()

plt.tight_layout(), plt.show()
print(f"Problem 1 - Max Error: {np.max(e1):.8e}")
print(f"Problem 2 - Max Error: {np.max(e2):.8e}")