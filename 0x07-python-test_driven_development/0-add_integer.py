#!/usr/bin/python3
# 0. Integers addition
"""
Write a function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    This function adds two integers.

    Args:
        a (int): First integer to add.
        b (int, optional): Second integer to add. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b are not integers or convertible to integers.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
