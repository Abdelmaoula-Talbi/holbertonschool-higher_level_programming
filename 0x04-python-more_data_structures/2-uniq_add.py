#!/usr/bin/python3


def uniq_add(mylist=[]):
    """function that adds all unique integers in a
    list (only once for each integer)."""

    new_list = set(mylist)
    sum = 0
    for i in new_list:
        sum += i
    return sum
