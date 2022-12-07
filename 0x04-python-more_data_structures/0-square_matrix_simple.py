#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    new_matrix = [[item**2 for item in row]for row in matrix]
    return new_matrix
