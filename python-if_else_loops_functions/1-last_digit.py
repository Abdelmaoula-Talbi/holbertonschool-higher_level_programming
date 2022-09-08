#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    abs_val = - number
else:
    abs_val = number
print(f"Last digit of {number} is", end=" ")
if number < 0:
    if ((abs_val % 10) != 0):
        print(f"{(abs_val % 10) * -1} and is less than 6 and not 0")
    else:
        print(f"{abs_val % 10} and is 0")
else:
    print(f"{abs_val % 10}", end=" ")
    if ((abs_val % 10) > 5):
        print(f"and is greater than 5")
    elif ((abs_val % 10) == 0):
        print(f"and is 0")
    else:
        print(f"and is less than 6 and not 0")
