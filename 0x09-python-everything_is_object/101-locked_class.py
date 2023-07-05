#!/usr/bin/python3
# 30. Low memory cost
"""
Write a class LockedClass
"""


class LockedClass:
    """
    a class LockedClass with no class or object attribute, that
    prevents the user from dynamically creating new instance
    """
    __slots__ = ['first_name']
