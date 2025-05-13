import pytest

from math_operations import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5
    assert add(5, 5) == 10


def test_subtract():
    assert subtract(1, 5) == - 4
    assert subtract(2, 1) == 1
    assert subtract(-1, -1) == 0


def test_multiply():
    assert multiply(6, 7) == 42
    assert multiply(9, 9) == 81


def test_divide():
    assert divide(5, 5) == 1
    assert divide(5, 1) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)

