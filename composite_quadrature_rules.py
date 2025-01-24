# %% Import required libraries
import numpy as np

def composite_trapezoidal(f, a, b, m):
    """Computes the composite trapezoidal rule for the function f on the interval [a, b] with m subintervals.

    Args:
        f (callable): The function to integrate.
        a (float): The lower limit of the integral.
        b (float): The upper limit of the integral.
        m (int): Number of subintervals.

    Returns:
        float: The approximate value of the integral.
    """
    x = np.linspace(a,b,m+1)
    h = float(b - a)/m
    fx = f(x[1:-1])
    ct = h*(np.sum(fx) + 0.5*(f(x[0]) + f(x[-1])))
    return ct

def composite_midpoint(f, a, b, m):
    """Computes the composite midpoint rule for the function f on the interval [a, b] with m subintervals.

    Args:
        f (callable): The function to integrate.
        a (float): The lower limit of the integral.
        b (float): The upper limit of the integral.
        m (int): Number of subintervals.

    Returns:
        float: The approximate value of the integral.
    """
    
    raise NotImplementedError("The composite_simpson function is not yet implemented.")

    int_f = 0       
    return int_f

def composite_simpson(f, a, b, m):
    """Computes the composite Simpson rule for the function f on the interval [a, b] with m subintervals.

    Args:
        f (callable): The function to integrate.
        a (float): The lower limit of the integral.
        b (float): The upper limit of the integral.
        m (int): Number of subintervals.

    Returns:
        float: The approximate value of the integral.
    """
    
    raise NotImplementedError("The composite_simpson function is not yet implemented.")

    int_f = 0       
    return int_f

if __name__ == '__main__':
    
    # Write a simple test run to check that the function works.
    print("Testing implementation of the trapezoidal rule function.")
    
    f = np.exp
    a, b = 0, 1
    m = 1
    
    int_f = composite_simpson(f, a, b, m)