#!/usr/bin/python3
# 2. Say my name
"""
Write a function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints a full name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to "".

    Raises:
        TypeError: If the arguments are not of type str.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
