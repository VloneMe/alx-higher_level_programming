#!/usr/bin/python3
"""
Search and update
"""


def append_after(filename="", search_string="", new_string=""):
    """
    A function that inserts a line of text to a file,
    after each line containing a specific string (see example)

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within each line of the file.
        new_string (str): The string to insert after each line containing the search string.
    """
    text = ""
    with open(filename) as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as file:
        file.write(text)
