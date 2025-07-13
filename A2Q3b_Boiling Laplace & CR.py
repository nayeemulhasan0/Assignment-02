import sympy as sp

# Define variables
x, y = sp.symbols('x y')

# Define the function
f = y**2 * sp.cos(x - y)

# Compute second-order partial derivatives for Laplace's equation
f_xx = sp.diff(f, x, x)
f_yy = sp.diff(f, y, y)

# Check Laplace's equation (Δf = 0)
laplace_eq = sp.simplify(f_xx + f_yy)
print("Laplace's Equation holds:", laplace_eq == 0)

# Define u and v for Cauchy-Riemann equations
u, v = sp.re(f), sp.im(f)
u_x, u_y = sp.diff(u, x), sp.diff(u, y)
v_x, v_y = sp.diff(v, x), sp.diff(v, y)

# Check Cauchy-Riemann equations
cr_eq = sp.simplify(u_x - v_y) == 0 and sp.simplify(u_y + v_x) == 0
print("Cauchy-Riemann Equations hold:", cr_eq)

# Verify f_xy = f_yx
f_xy = sp.diff(f, x, y)
f_yx = sp.diff(f, y, x)
print("f_xy = f_yx:", sp.simplify(f_xy - f_yx) == 0)
