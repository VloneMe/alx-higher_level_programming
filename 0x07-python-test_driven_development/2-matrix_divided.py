#!/usr/bin/python3
# 1. Divide a matrix
"""
Write a function that divides all elements of a matrix.
"""


def is_valid_matrix(matrix):
    """
    Helper function to check if a matrix is valid.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        return False
    row_lengths = set(len(row) for row in matrix)
    return len(row_lengths) == 1


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by the given divisor.

    Args:
        matrix (list of list): A list of lists containing int or float values.
        div (int or float): The divisor.

    Raises:
        TypeError: If the matrix or the divisor is not of type int or float.
        ZeroDivisionError: If the divisor is zero.
        ValueError: If the matrix does not have consistent row lengths.

    Returns:
        list of list: A new matrix with elements divided by the divisor,
        rounded to 2 decimal places.

    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not is_valid_matrix(matrix):
        raise ValueError("matrix must be a matrix (list of lists) of integers/floats")

    new_matrix = [list(row) for row in matrix]  # Create a new matrix with the same values as the original

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_matrix[i][j] = round(matrix[i][j] / div, 2)

    return new_matrix
