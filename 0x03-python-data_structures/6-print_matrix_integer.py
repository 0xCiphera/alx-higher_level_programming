#!/usr/bin/python3
"""
Welcome to data structures fellas
"""


def print_matrix_integer(matrix=[[]]):
    """
    welcome
    """
    for i in matrix:
        print(" ".join("{:d}".format(j) for j in i))
