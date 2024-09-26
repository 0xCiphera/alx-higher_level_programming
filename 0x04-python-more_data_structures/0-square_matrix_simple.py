#!/usr/bin/python3
"""
welcome
"""


def square_matrix_simple(matrix=[]):
    """
    (c) leanstix
    """

    if matrix == []:
        return matrix
    new = [[x**2 for x in i] for i in matrix]
    return new
