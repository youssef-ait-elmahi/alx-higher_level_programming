#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    Returns:
        int: The sum of the two numbers.
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
