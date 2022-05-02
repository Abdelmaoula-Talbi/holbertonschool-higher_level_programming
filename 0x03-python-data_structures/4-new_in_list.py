#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        my_list2 = my_list.copy()
        my_list2.pop(idx)
        my_list2.insert(idx, element)
        return my_list2
