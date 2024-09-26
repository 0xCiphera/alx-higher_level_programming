#!/usr/bin/python3
"""
Welcome to data structures fellas
"""


def divisible_by_2(my_list=[]):
    """
   a function that finds all multiples of 2 in a list.
    """
    new_l = my_list.copy()
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            new_l[i] = 1
        else:
            new_l[i] = 0
    return new_l
