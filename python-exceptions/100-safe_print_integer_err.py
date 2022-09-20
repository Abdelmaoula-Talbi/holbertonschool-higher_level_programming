#!/usr/bin/pytihon3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except BaseException as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return False
