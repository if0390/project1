import pytest
from app.core import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(2, 3) == 5

def test_subtract(calculator):
    assert calculator.subtract(5, 3) == 2

def test_multiply(calculator):
    assert calculator.multiply(2, 3) == 6

def test_divide(calculator):
    assert calculator.divide(6, 3) == 2

def test_divide_by_zero(calculator):
    assert calculator.divide(5, 0) == "Error: Division by zero"