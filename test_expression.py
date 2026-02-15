import math
import pytest
from expression import evaluate, ParseError


class TestBasicArithmetic:
    def test_addition(self):
        assert evaluate("2 + 3") == 5

    def test_subtraction(self):
        assert evaluate("10 - 4") == 6

    def test_multiplication(self):
        assert evaluate("3 * 4") == 12

    def test_division(self):
        assert evaluate("10 / 4") == 2.5

    def test_modulo(self):
        assert evaluate("10 % 3") == 1


class TestPrecedence:
    def test_mul_before_add(self):
        assert evaluate("2 + 3 * 4") == 14

    def test_div_before_sub(self):
        assert evaluate("10 - 6 / 2") == 7

    def test_power_before_mul(self):
        assert evaluate("2 * 3 ^ 2") == 18


class TestParentheses:
    def test_override_precedence(self):
        assert evaluate("(2 + 3) * 4") == 20

    def test_nested(self):
        assert evaluate("((2 + 3) * (4 - 1))") == 15


class TestUnaryMinus:
    def test_negative_number(self):
        assert evaluate("-5") == -5

    def test_negative_in_expr(self):
        assert evaluate("3 + -2") == 1

    def test_double_negative(self):
        assert evaluate("--5") == 5


class TestPower:
    def test_basic(self):
        assert evaluate("2 ^ 10") == 1024

    def test_right_associative(self):
        # 2^3^2 = 2^(3^2) = 2^9 = 512
        assert evaluate("2 ^ 3 ^ 2") == 512


class TestFunctions:
    def test_sin(self):
        result = evaluate(f"sin({math.pi / 2})")
        assert abs(result - 1.0) < 1e-10

    def test_cos(self):
        assert abs(evaluate("cos(0)") - 1.0) < 1e-10

    def test_sqrt(self):
        assert evaluate("sqrt(16)") == 4.0

    def test_log(self):
        assert abs(evaluate("log(100)") - 2.0) < 1e-10

    def test_ln(self):
        result = evaluate(f"ln({math.e})")
        assert abs(result - 1.0) < 1e-10

    def test_factorial(self):
        assert evaluate("factorial(5)") == 120

    def test_nested_functions(self):
        assert abs(evaluate("sin(0) + cos(0)") - 1.0) < 1e-10


class TestErrors:
    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="divide by zero"):
            evaluate("1 / 0")

    def test_unexpected_character(self):
        with pytest.raises(ParseError):
            evaluate("2 & 3")

    def test_mismatched_paren(self):
        with pytest.raises(ParseError):
            evaluate("(2 + 3")

    def test_empty_expression(self):
        with pytest.raises(ParseError):
            evaluate("")

    def test_sqrt_negative(self):
        with pytest.raises(ValueError):
            evaluate("sqrt(-1)")
