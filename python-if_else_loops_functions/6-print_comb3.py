#!/usr/bin/python3
for i in range(0, 100):
    if ((i // 10) < (i % 10)):
        print("{}{}".format((i // 10), (i % 10)), end="")
        break
for j in range((i + 1), 100):
    if ((j // 10) < (j % 10)):
        print(", {}{}".format((j // 10), (j % 10)), end="")
print()
