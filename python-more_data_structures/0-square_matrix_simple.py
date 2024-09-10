#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[new_matrix ** 2 for new_matrix in row]for row in matrix]
