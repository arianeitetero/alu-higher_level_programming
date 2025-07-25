#!/usr/bin/python3
"""Module for matrix_divided function"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div and returns a new matrix

    Args:
        matrix: list of lists of integers/floats
        div: int or float

    Raises:
        TypeError: if matrix or div is invalid
        ZeroDivisionError: if div is zero

    Returns:
        new matrix with elements divided and rounded to 2 decimal places
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if any(not all(isinstance(x, (int, float)) for x in row) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return [[round(x / div, 2) for x in row] for row in matrix]
