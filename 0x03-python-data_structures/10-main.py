#!/usr/bin/python3
"""
welcome
"""


divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    """
    Write a function that finds all multiples of 2 in a list.
    """
    print("{:d} {:s} divi\
        sible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1
