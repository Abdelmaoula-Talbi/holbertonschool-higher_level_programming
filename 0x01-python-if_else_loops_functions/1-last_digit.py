#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    abs_number = number * -1
else:
    abs_number = number
if (abs_number % 10) > 5:
    print(f"Last digit of {number} is {abs_number % 10} and is greater than 5")
elif (abs_number % 10) < 6:
    if (abs_number % 10) == 0:
        print(f"Last digit of {number} is {abs_number % 10} and is 0")
    else:
        print(f"Last digit of {number} is {abs_number % 10} and is less than 6 and is not 0")
