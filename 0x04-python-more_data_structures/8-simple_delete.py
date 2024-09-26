#!/usr/bin/python3
"""
welcome
"""


def simple_delete(a_dictionary, key=""):
    """
    (c)leanstix
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
