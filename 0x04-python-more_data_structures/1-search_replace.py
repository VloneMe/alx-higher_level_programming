#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    This replaces all occurrences of an element by another in a new list
    """
    x = ([element if element != search else replace for element in my_list])
    return x
