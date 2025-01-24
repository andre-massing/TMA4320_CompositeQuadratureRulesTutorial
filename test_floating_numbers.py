import pytest

def calculate_sum(a, b):
    return a + b

def test_calculate_sum():
    a = 0.2
    b = 0.1
    sum = 0.3
    # assert a + b == sum
    assert a + b == pytest.approx(sum)
    

# @pytest.mark.parametrize("a, b, sum", [(0.1, 0.1, 0.2), (0.2, 0.2, 0.4), (0.4, 0.4, 0.8)])
# def test_calculate_sum_parametrized(a, b, sum):
    # assert a + b == sum
    # assert a + b == pytest.approx(sum)
