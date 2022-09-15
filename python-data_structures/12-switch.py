#!/usr/bin/python3
a = 89
b = 10
((b, a) for b in (a, b) for a in (a, b))
print("a={:d} - b={:d}".format(a, b))
