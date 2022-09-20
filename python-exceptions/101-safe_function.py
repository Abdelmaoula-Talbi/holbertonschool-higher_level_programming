#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
        return result
    except BaseException as err:
        sys.stderr.write(f"Exception: {err}\n")
        return None
