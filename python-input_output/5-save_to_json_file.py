#!/usr/bin/python3
"""

A modulte that representes the function
save_to_json_file(my_obj, filename)

"""


def save_to_json_file(my_obj, filename):
    """
    A function that writes an Object to a text
    file, using the JSON representation
    """
    import json
    with open(filename, mode="w", encoding='utf-8') as my_file:
        json.dump(my_obj, my_file)
