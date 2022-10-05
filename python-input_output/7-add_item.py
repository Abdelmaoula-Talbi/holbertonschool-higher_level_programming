#!/usr/bin/python3
"""

A module taht representes a script

"""

import os
import json
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def append_my_list(my_list=[]):
    i = 1
    while (i < len(argv)):
        my_list.append(argv[i])
        i += 1
    return (my_list)


my_list = []
list_appended = append_my_list(my_list)
if not os.path.isfile("./add_item.json"):
    save_to_json_file(list_appended, "add_item.json")
else:
    my_obj = load_from_json_file("add_item.json")
    append_my_list(my_obj)
    save_to_json_file(my_obj, "add_item.json")
