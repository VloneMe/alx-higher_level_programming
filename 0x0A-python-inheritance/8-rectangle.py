#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
8. Rectangle
"""


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
