#!/usr/bin/python3

for i in range(0, 10):
    for y in range(1, 10):
        if i == y or i > y:
            continue
        elif i == 8 and y == 9:
            print("{:01}".format(i) + "{:01}".format(y), end="")
        else:
            print("{:01}".format(i) + "{:01}".format(y), end=", ")
