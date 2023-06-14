#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    function that computes the square value of all integers of a matrix.
    """
    matrix = ([[(n**2) for n in row] for row in matrix])
    return matrix
