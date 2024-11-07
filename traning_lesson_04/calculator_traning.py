import pytest
from calculator import Calculator

calculator = Calculator
@pytest.mark.parametrize('num1, num2, result', [(4, 5, 9),(-6, -10, -16), (-6, 6, 0), (5.61, 4.29, 9.9),
(10, 0, 10), (-10.5, 1234, 1223.5)])
def test_sum_positive_nums(num1, num2, result):
    calculator = Calculator()
    res = calculator.sum(num1, num2)
    assert res == result