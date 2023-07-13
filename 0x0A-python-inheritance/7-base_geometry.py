#!/usr/bin/python3
"""
Integer validator
"""


class BaseGeometry:
    """
    Base class for geometry-related classes.
    """

    def area(self):
        """
        Calculates the area of the geometry object.

        Raises:
            NotImplementedError: If the derived class does not implement this method.
        """
        raise NotImplementedError("area() method is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if a value is an integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
