# Import necessary libraries
import math

# 1. Approximation Algorithm (Basic Numerical Approximation)
def approximation_algorithm(f, x0, tol=1e-4, max_iter=100):
    """Iterative numerical approximation to find a root."""
    x_n = x0
    for _ in range(max_iter):
        x_next = x_n - f(x_n) * 0.1  # Adjust step size for approximation
        if abs(x_next - x_n) < tol:
            return x_next
        x_n = x_next
    return x_n

# 2. Bisection Method
def bisection_method(f, a, b, tol=1e-4):
    """Find root using Bisection Method."""
    if f(a) * f(b) >= 0:
        raise ValueError("Function values at the interval endpoints must have opposite signs.")
    
    iterations = 0
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return iterations, c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterations += 1
    return iterations, (a + b) / 2

# 3. Fixed-Point Iteration
def fixed_point_iteration(g, x0, tol=1e-4, max_iter=100):
    """Fixed-Point Iteration to solve x = g(x)."""
    x_n = x0
    for _ in range(max_iter):
        x_next = g(x_n)
        if abs(x_next - x_n) < tol:
            return x_next
        x_n = x_next
    return x_n

# 4. Newton-Raphson Method
def newton_raphson_method(f, f_prime, x0, tol=1e-4, max_iter=100):
    """Newton-Raphson method for root-finding."""
    x_n = x0
    for _ in range(max_iter):
        if f_prime(x_n) == 0:
            raise ValueError("Derivative is zero. Newton's method fails.")
        x_next = x_n - f(x_n) / f_prime(x_n)
        if abs(x_next - x_n) < tol:
            return x_next
        x_n = x_next
    return x_n

# Example function and its derivative
def f(x):
    return x**3 + 4*x**2 - 10  # Example function

def f_prime(x):
    return 3*x**2 + 8*x  # Derivative of the function

def g(x):
    return (10 - x**3) / 4  # Example for Fixed-Point Iteration (derived from f(x))

# Test inputs
x0 = 1  # Initial guess for root-finding
a, b = -4, 7  # Interval for Bisection Method

# Run all algorithms
approx_result = approximation_algorithm(f, x0)
bisection_iterations, bisection_root = bisection_method(f, a, b)
fixed_point_root = fixed_point_iteration(g, x0)
newton_root = newton_raphson_method(f, f_prime, x0)

# Print results with double newline formatting
print(f"1. Approximation Algorithm Root: {approx_result}\n")
print(f"2. Bisection Method - Iterations: {bisection_iterations}")
print(f"   Approximate Root: {bisection_root}\n")
print(f"3. Fixed-Point Iteration Root: {fixed_point_root}\n")
print(f"4. Newton-Raphson Method Root: {newton_root}\n")
