#!/usr/bin/python3
"""
Welcome to data structures fellas
"""


# that retrieves an element from a list like in C.

def element_at(my_list, idx):
    """
    this function that retrieves an element from a list like in C.
    """
    if idx < 0 or idx >= len(my_list):
        return
    return my_list[idx]
