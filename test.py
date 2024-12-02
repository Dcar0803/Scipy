from main import integrate_linear_function, solve_system, generate_normal_samples

def test_integrate_linear_function():
    # Test: f(x) = 2x + 1, range [0, 2]
    result = integrate_linear_function(2, 1, 0, 2)
    assert round(result, 2) == 6.0


def test_solve_system():
    # Test: 2x + 3y = 6, 4x - y = 5
    coeffs = [[2, 3], [4, -1]]
    constants = [6, 5]
    result = solve_system(coeffs, constants)
    assert round(result["X"], 2) == 1.0
    assert round(result["Y"], 2) == 2.0
    print("test_solve_system passed.")


def test_generate_normal_samples():

    samples = generate_normal_samples(mean=0, stddev=1, size=1000)
    assert len(samples) == 1000
    assert abs(sum(samples) / 1000) < 0.1  # Mean close to 0
    print("test_generate_normal_samples passed.")


if __name__ == "__main__":
    test_integrate_linear_function()
    test_solve_system()
    test_generate_normal_samples()
    print("All tests passed.")