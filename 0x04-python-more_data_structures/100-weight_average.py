#!/usr/bin/python3
"""
Welcome
"""


def weight_average(my_list=[]):
    """
    (c)leanstix
    """
    if my_list == []:
        return 0
    cu = 0
    ws = 0
    for i in my_list:
        ws += (i[0] * i[1])
        cu += i[1]
    average = ws / cu
    return average
