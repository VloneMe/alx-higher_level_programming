#!/usr/bin/python3
"""
Module for the Rectangle class that inherits from the Base class
"""

from models.base import Base


class Rectangle(Base):
    """
    This rectangle class representing a rectangle, inheriting from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This initializes an instance of the Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-coordinate of the rectangle's position.
            y (int, optional): y-coordinate of the rectangle's position.
            id (int, optional): ID of the rectangle.
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        This getter method for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        This setter method for the width attribute.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        '''
        This getter method for the height attribute.
        '''
        return self.__height

    @height.setter
    def height(self, height):
        '''
        This setter method for the height attribute.
        '''
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        '''
        This getter method for the x attribute.
        '''
        return self.__x

    @x.setter
    def x(self, x):
        '''
        This setter method for the x attribute.
        '''
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        '''
        This getter method for the y attribute.
        '''
        return self.__y

    @y.setter
    def y(self, y):
        '''
        This setter method for the y attribute.
        '''
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        '''
        This calculates the area of the rectangle.
        '''
        return self.width * self.height

    def display(self):
        '''
        This displays the rectangle using the character #.
        '''
        [print() for space in range(self.y)]
        [print(" " * self.x + "#" * self.width) for line in range(self.height)]

    def __str__(self):
        '''
        This returns a string representation of the Rectangle instance.
        '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        '''
        This updates the attributes of the Rectangle.

        Args:
            *args: Variable number of arguments (id, width, height, x, y).
            **kwargs: Variable number of keyword arguments.
        '''

        if args and len(args) > 0:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)

        else:
            for key, value in kwargs.items():
                if key in ["id", "width", "height", "x", "y"]:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        This returns a dictionary representation of the Rectangle instance.

        Returns:
            dict: Dictionary containing the attributes of the Rectangle.
        """

        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
