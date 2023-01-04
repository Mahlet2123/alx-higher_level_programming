#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = [[]]
    for row in matrix:
        if type(row) not in (list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for items in row:
            if type(items) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        for items in row:
            new_matrix[row][items] = items / div
    return new_matrix
