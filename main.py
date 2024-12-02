from scipy.integrate import quad
from scipy.linalg import solve

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