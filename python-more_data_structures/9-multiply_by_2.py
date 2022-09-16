#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for i, v in new_dict.items():
        new_dict[i] = v * 2
    return new_dict
#    a_dictionary = map(lambda x,v : v * 2, a_dictionary)
