#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
#    if len(argv) < 2:
#        print("{} arguments.".format(len(argv) - 1))
#    elif len(argv) == 2:
#        print("{} argument:".format(len(argv) - 1))
#    elif (len(argv) > 2):
#        print("{} arguments:".format(len(argv) - 1))
    i = 1
    result = 0
    while (i < len(argv)):
        result += int(argv[i])
        i += 1
    print("{}".format(result))
#        print("{}: {}".format(i, argv[i]))
