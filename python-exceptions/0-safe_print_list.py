#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        elem_count = 0
        for i in range(x):
            print(my_list[i], end="")
            elem_count += 1
    except IndexError:
        pass
    finally:
        print()
    return elem_count
