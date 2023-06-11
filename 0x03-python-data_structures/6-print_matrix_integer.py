#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for colm in (matrix):
        for row in (colm):
            print("{:d}".format(row), end=" " if row != colm[-1] else "")
        print()
