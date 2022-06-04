#!/usr/bin/python3


def best_score(a_dictionary):
    """ function that returns a key
    with the biggest integer value"""
    if a_dictionary is None or a_dictionary == {}:
        return None
    biggest_value = max(a_dictionary, key=lambda x: a_dictionary[x])
    return biggest_value
