#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ligne in matrix:
        for args in range(len(ligne)):
            if args < len(ligne) - 1:
                print("{:d}".format(ligne[args]), end=" ")
            else:
                print("{:d}".format(ligne[args]), end="")
        print()
