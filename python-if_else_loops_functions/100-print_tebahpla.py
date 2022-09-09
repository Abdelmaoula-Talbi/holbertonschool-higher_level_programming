#!/usr/bin/python3
for i in range(90, 65, -2):
    print("{}".format(chr(i + 32)), end="")
    i -= 1
    print("{}".format(chr(i)), end="")
