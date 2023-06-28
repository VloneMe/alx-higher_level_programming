#!/usr/bin/python3
# 10. ByteCode -> Python #5
"""
This class defines a class MagicClass
"""
import math


class MagicClass:
    """
    The class represents a circle.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius=0):
        """
        This initialize a new circle.

        Args:
            radius (float, optional): The radius of the circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        This calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """
        This calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
