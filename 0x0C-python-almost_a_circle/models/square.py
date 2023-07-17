#!/usr/bin/python3
"""
Module for the Square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This square class that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        This initializes an instance of the Square class.

        Args:
            size (int): Size of the square (width and height).
            x (int, optional): x-coordinate of the square's position.
            y (int, optional): y-coordinate of the square's position.
            id (int, optional): ID of the square.
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square instance.
        Overwrites the __str__ method inherited from Rectangle.
        """

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """
        This getter method for the size attribute.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        This setter method for the size attribute.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        This updates the attributes of the Square.

        Args:
            *args: Variable number of arguments (id, size, x, y).
            **kwargs: Variable number of keyword arguments.
        """

        if args and len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)

        else:
            for key, value in kwargs.items():
                if key in ["id", "size", "x", "y"]:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        This returns a dictionary representation of the Square instance.

        Returns:
            dict: Dictionary containing the attributes of the Square.
        """

        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
