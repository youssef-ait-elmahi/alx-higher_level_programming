#!/usr/bin/python3
"""Divides all elements of a matrix by a given number."""


def matrix_divided(matrix, div):
    """
    Args:
        matrix (list): A matrix represented as a list of lists of integers or
        floats.
        div (int or float): The number to divide the matrix elements by.
    Returns:
        list: A new matrix with the divided elements.
    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
        or if div is not a number.
        TypeError: If each row of the matrix does not have the same size.
        ZeroDivisionError: If div is equal to 0.

    """
    if not isinstance(matrix, list) or \
            any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix \
            (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
