#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """a function that deletes a key in a dictionary."""
    if key in a_dictionary:
        del a_dictionary[key]
    else:
        return a_dictionary
    return a_dictionary
