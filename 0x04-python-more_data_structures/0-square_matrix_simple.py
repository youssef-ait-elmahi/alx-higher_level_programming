#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for i in matrix:
        helper = [e * e for e in i]
        square.append(helper)
    return(square)
