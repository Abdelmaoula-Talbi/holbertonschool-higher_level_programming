#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return (0)
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    string_roman = roman_string[::-1]
    roman_integer = 0
    if len(string_roman) == 1:
        return (roman[string_roman[0]])
    for i in range(1, len(string_roman), 2):
        if string_roman[i] not in roman:
            return 0
        if (roman[string_roman[i]] >= roman[string_roman[i - 1]]):
            roman_integer += roman[string_roman[i-1]] + roman[string_roman[i]]
        elif (roman[string_roman[i]] < roman[string_roman[i - 1]]):
            roman_integer += roman[string_roman[i-1]] - roman[string_roman[i]]
    if (len(string_roman) % 2 != 0):
        roman_integer += roman[string_roman[len(string_roman) - 1]]
    return (roman_integer)
