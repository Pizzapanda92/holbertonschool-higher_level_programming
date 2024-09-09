#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ligne in matrix:
        for args in ligne:
            print("{:d}".format(args), end=" ")
        print()
