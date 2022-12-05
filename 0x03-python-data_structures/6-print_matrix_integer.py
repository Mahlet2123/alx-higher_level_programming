#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    if len(matrix) == 0:
        print()
    for i in matrix:
        print(' '.join('{:d}'.format(j)for j in i))
