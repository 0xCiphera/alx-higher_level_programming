#!/usr/bin/python3
"""
Welcome to data structures fellas
"""


def new_in_list(my_list, idx, element):
    """
    welcome
    """
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
