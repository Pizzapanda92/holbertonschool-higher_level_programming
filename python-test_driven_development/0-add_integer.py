#!/usr/bin/python3
"""
fuction that adds two numbers
"""


def add_integer(a, b=98):

    """
    Adds two integers or floats after casting them to integers.

    Args:
        a: The first integer or float.
        b: The second integer or float, default is 98.

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
