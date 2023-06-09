#!/usr/bin/python3
import sys

if __name__ == "__main__":
    output = 0
    for n in range(len(sys.argv) - 1):
        output += int(sys.argv[n + 1])
    print("{}".format(output))
