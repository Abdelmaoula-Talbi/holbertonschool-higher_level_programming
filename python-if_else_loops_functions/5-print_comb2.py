#!/usr/bin/python3
for i in range(0, 100):
    if (i + 1) == 100:
        print(f"{i//10}{i%10}")
    else:
        print(f"{i//10}{i%10}, ", end="")
