#!/usr/bin/python3


def read_file(filename=""):
    """
    A function that reads a text file (UTF8) and prints it to stdout:
    """

    with open(filename) as f:
        text = f.read()
        print(text, end="")
