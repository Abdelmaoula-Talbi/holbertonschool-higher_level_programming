#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    sorted_dict = sorted(a_dictionary.items(), key=lambda item: item[1])
    length = len(sorted_dict)
    return (sorted_dict[length - 1][0])
