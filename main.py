from scipy.integrate import quad

def integrate_linear_function(a, b, start, end):
    f = lambda x: a * x + b
    result, _ = quad(f, start, end)
    return result