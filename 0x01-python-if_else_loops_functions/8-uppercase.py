#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 122:
            ord(i) = ord(i) - 32
        print(chr(i), end="")
    print()
