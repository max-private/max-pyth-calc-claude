import math
import pytest
from calculator import (
    add, subtract, multiply, divide,
    power, modulo, square_root, factorial,
    sin, cos, tan, log, ln,
)


# --- Basic arithmetic (existing) ---

class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -2) == -3

    def test_mixed_signs(self):
        assert add(-1, 3) == 2

    def test_zeros(self):
        assert add(0, 0) == 0

    def test_floats(self):
        assert add(1.5, 2.5) == 4.0


class TestSubtract:
    def test_positive_numbers(self):
        assert subtract(5, 3) == 2

    def test_negative_result(self):
        assert subtract(3, 5) == -2

    def test_negative_numbers(self):
        assert subtract(-1, -2) == 1

    def test_zeros(self):
        assert subtract(0, 0) == 0


class TestMultiply:
    def test_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_by_zero(self):
        assert multiply(5, 0) == 0

    def test_negative_numbers(self):
        assert multiply(-2, -3) == 6

    def test_mixed_signs(self):
        assert multiply(-2, 3) == -6


class TestDivide:
    def test_positive_numbers(self):
        assert divide(10, 2) == 5.0

    def test_float_result(self):
        assert divide(7, 2) == 3.5

    def test_negative_numbers(self):
        assert divide(-6, -3) == 2.0

    def test_mixed_signs(self):
        assert divide(-6, 3) == -2.0

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)

    def test_zero_divided(self):
        assert divide(0, 5) == 0.0


# --- New operations ---

class TestPower:
    def test_basic(self):
        assert power(2, 3) == 8

    def test_zero_exponent(self):
        assert power(5, 0) == 1

    def test_negative_exponent(self):
        assert power(2, -1) == 0.5

    def test_fractional_exponent(self):
        assert power(4, 0.5) == 2.0


class TestModulo:
    def test_basic(self):
        assert modulo(10, 3) == 1

    def test_even_division(self):
        assert modulo(10, 5) == 0

    def test_modulo_by_zero(self):
        with pytest.raises(ValueError, match="Cannot modulo by zero"):
            modulo(10, 0)


class TestSquareRoot:
    def test_perfect_square(self):
        assert square_root(9) == 3.0

    def test_zero(self):
        assert square_root(0) == 0.0

    def test_non_perfect(self):
        assert abs(square_root(2) - math.sqrt(2)) < 1e-10

    def test_negative(self):
        with pytest.raises(ValueError, match="negative"):
            square_root(-1)


class TestFactorial:
    def test_basic(self):
        assert factorial(5) == 120

    def test_zero(self):
        assert factorial(0) == 1

    def test_one(self):
        assert factorial(1) == 1

    def test_negative(self):
        with pytest.raises(ValueError, match="negative"):
            factorial(-1)

    def test_non_integer(self):
        with pytest.raises(ValueError, match="non-integer"):
            factorial(3.5)


# --- Scientific functions ---

class TestScientific:
    def test_sin(self):
        assert abs(sin(math.pi / 2) - 1.0) < 1e-10

    def test_cos(self):
        assert abs(cos(0) - 1.0) < 1e-10

    def test_tan(self):
        assert abs(tan(0)) < 1e-10

    def test_log_base10(self):
        assert abs(log(100) - 2.0) < 1e-10

    def test_log_nonpositive(self):
        with pytest.raises(ValueError, match="non-positive"):
            log(0)

    def test_ln(self):
        assert abs(ln(math.e) - 1.0) < 1e-10

    def test_ln_nonpositive(self):
        with pytest.raises(ValueError, match="non-positive"):
            ln(-1)
