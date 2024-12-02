def test_integrate_linear_function():
    # Test: f(x) = 2x + 1, range [0, 2]
    result = integrate_linear_function(2, 1, 0, 2)
    assert round(result, 2) == 6.0