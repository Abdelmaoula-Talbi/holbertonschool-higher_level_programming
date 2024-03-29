#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elem_printed_count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            elem_printed_count += 1
        except (TypeError, ValueError):
            pass
    print()
    return elem_printed_count
