#!/usr/bin/python3
"""
Class to JSON
"""


def class_to_json(obj):
    """
    This converts a class object to a JSON-compatible dictionary.
    """
    return obj.__dict__
