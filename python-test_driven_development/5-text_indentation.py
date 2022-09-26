#!/usr/bin/python3
"""

A module that representes a function that prints a string

"""


def text_indentation(text):
    """
    A function that prints a text with 2 new lines
    after each of these characters: ., ?, :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == " " and text[i - 1] in (".", "?", ":"):
            pass
        elif text[i] in (".", "?", ":"):
            print(text[i])
            print()
        else:
            print(text[i], end="")
