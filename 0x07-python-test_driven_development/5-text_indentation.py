#!/usr/bin/python3
# 4. Text indentation.
"""
Write a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    This prints a string with 2 new lines after '.', '?', and ':'

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    replacements = ['.\n\n', ':\n\n', '?\n\n']
    for replacement in replacements:
        text = text.replace(replacement, replacement[0])

    print(text, end='')
