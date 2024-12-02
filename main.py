from scipy.integrate import quad
from scipy.linalg import solve
import numpy as np

def integrate_linear_function(a, b, start, end):

    """Integrates a linear function f(x) = ax + b over a specified range.

    Parameters:
        a (float): Coefficient of x.
        b (float): Constant term.
        start (float): Start of the integration range.
        end (float): End of the integration range.

    Returns:
        float: The definite integral result.
    """
    f = lambda x: a * x + b
    result, _ = quad(f, start, end)
    return result


def solve_system(coefficients, constants):
     
    """Solves a system of two linear equations.

    Parameters:
        coefficients (list[list[float]]): Coefficient matrix of the equations.
        constants (list[float]): Constant values of the equations.

    Returns:
        dict: Dictionary containing the solution {'X': x_value, 'Y': y_value}.
    """
    solution = solve(coefficients, constants)
    return {"X": solution[0], "Y": solution[1]}