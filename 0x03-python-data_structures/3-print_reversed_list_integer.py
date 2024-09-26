#!/usr/bin/python3
"""
Welcome to data structures fellas
"""


def print_reversed_list_integer(my_list=[]):
    """
     a function that prints all integers of a list, in reverse order.
     """
    if my_list:
        for i in reversed(my_list):
            print("{:d}".format(i))
