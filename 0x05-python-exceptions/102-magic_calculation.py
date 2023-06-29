#!/usr/bin/python3


def magic_calculation(a, b):
    """
    Performs a magic calculation using the given values of 'a' and 'b'.

    Args:
        a: The first value.
        b: The second value.

    Returns:
        The result of the magic calculation.
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i
        except:
            result = b + a
            break
    return result
