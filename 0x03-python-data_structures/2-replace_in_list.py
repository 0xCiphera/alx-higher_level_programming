#!/usr/bin/python3
"""
Welcome to data structures fellas
"""


def replace_in_list(my_list, idx, element):
    """
    replaces items of the list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
