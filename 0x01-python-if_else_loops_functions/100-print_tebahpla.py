#!/usr/bin/python3

for char in range(0, 26):
    if char % 2 == 0:
        print("{:c}".format(122 - char), end="")
    else:
        print("{:c}".format(90 - char), end="")
