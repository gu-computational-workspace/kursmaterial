# math_operations.py

def add(x, y):
    """Return the sum of two numbers."""
    return x + y


def subtract(x, y):
    """Return the difference between two numbers."""
    return x - y


def multiply(x, y):
    """Return the product of two numbers."""
    return x * y


def divide(x, y):
    """Return the result of dividing x by y."""
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero.")
