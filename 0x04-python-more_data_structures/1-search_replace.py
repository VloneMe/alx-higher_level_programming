#!/usr/bin/python3

#1-search_replace.py

def search_replace(my_list, search, replace):
    """
    function that replaces all occurrences of an element by another in a new list
    """
    value = ([element if element != search else replace for element in my_list])
    return value
