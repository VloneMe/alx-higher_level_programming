#!/usr/bin/python3
# 3. Print square
"""
Write a function that prints a square with the character #.
"""


def print_square(size):
    """
    This prints a square made of '#' characters.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print('#' * size)
