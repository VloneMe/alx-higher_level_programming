#!/usr/bin/python3
"""
4. Only sub class of
"""


def inherits_from(obj, a_class):
    """
     Function that returns True if the object
     is an instance of a class that inherited
    """

    return False if type(obj) is a_class else isinstance(obj, a_class)
