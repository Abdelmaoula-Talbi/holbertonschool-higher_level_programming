#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "and is greater than 5"
str2 = "and is less than 6 and not 0"
if number < 0:
    abs_number = number * -1
    if (abs_number % 10) == 0:
        print(f"Last digit of {number} is {abs_number % 10} and is 0")
    else:
        print(f"Last digit of {number} is -{abs_number % 10} {str2}")


else:
    if (number % 10) > 5:
        print(f"Last digit of {number} is {number % 10} {str1}")
    elif (number % 10) < 6:
        if (number % 10) == 0:
            print(f"Last digit of {number} is {number % 10} and is 0")
        else:
            print(f"Last digit of {number} is {number % 10} {str2}")
