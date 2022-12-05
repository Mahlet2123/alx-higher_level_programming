#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    if len(matrix) == 0:
        print()
    for row in matrix:
        print(' '.join('{}'.format(item) for item in row))
