#!/usr/bin/python3
"""My module for Rectangles"""


class Rectangle:
    """Class for rectangles"""

    def __init__(self, width=0, height=0):
        """Calls getter and setters to initialize values

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter - gets the value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter - sets the value of width

        Args:
            value (int): the value to set to width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter - gets the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter - sets the value of height

        Args:
            value (int): the value to set to height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
