#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j != len(matrix[i]) - 1:
                endspace = ' '
            else:
                endspace = ''
            print('{}'.format(matrix[i][j]), end=endspace)
        print()
