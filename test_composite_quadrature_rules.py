import pytest
from composite_quadrature_rules import composite_trapezoidal

def test_trapezoidal_rule():
    def test_function(x):
        return 1 + x
    
    result = composite_trapezoidal(test_function, 0, 1, 100)
    expected = 3/2  # The exact integral of x^2 from 0 to 1
    assert pytest.approx(result, rel=1e-5) == expected
