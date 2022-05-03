#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    my_new_list = my_list.copy()
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    my_new_list.pop(idx)
    my_new_list.insert(idx, element)
    return my_new_list
