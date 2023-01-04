#!/usr/bin/python3
"""Module for matrix_divided method."""


def matrix_divided(matrix, div):
    """
    a function that divides all elements of a matrix

    Returns a new matrix
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        if len(row) != len(matrix[0]):
            raise TypeError(
                    "Each row of the matrix must have the same size"
            )
        for items in row:
            if type(items) not in (int, float):
                raise TypeError(
                    "matrix must be a matrix " +
                    "(list of lists) of integers/floats"
                )
    return [[round(items / div, 2) for items in row] for row in matrix]
