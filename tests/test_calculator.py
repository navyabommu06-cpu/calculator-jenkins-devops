
import pytest

from calculator import add, subtract, multiply, divide


def test_addition():
    assert add(10, 20) == 30


def test_subtraction():
    assert subtract(20, 10) == 10


def test_multiplication():
    assert multiply(5, 4) == 20


def test_division():
    assert divide(20, 5) == 4


def test_division_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_negative_numbers():
    assert add(-5, -5) == -10
