#!/usr/bin/python3
def uppercase(str):
    ch = ""
    for i in str:
        if 97 <= ord(i) <= 122:
            ch += chr(ord(i) - 32)
#            print(chr(ord(i)-32), end="")
        else:
            ch += i
    print(ch)
