#!/usr/bin/python3
"""
9. Full rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        A method to initialize the attributes
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        A method to override the area method in the parent class
        """
        return self.__width * self.__height

    def __str__(self):
        """__str__ method to return the formatted string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
