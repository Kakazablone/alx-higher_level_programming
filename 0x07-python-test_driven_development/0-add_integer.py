#!/usr/bin/python3
"""My addition module

add_integer: adds two integers together

"""


def add_integer(a, b=98):
    """Returns a + b
    Args: a and b (int): the numbers to add
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
