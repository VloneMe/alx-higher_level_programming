#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
10. Square #1
"""


class Square(Rectangle):
    """
     A class Square that inherits from Rectangle
    """

    def __init__(self, size):
        """
        A method for initialized the attrubutes
        """

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        A rectangle area
        """

        return self.__size ** 2
