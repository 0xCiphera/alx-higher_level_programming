#!/usr/bin/python3
"""
welcome
"""


def search_replace(my_list, search, replace):
    """
    searches and replaces
    """

    if my_list == []:
        return my_list
    replaced = my_list[:]
    for i in range(len(replaced)):
        if replaced[i] == search:
            replaced[i] = replace
    return replaced
