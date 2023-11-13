#!/usr/bin/python3
"""Squares Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize an instance of a square
        Args:
            size (int): size of the square == width & height
            x (int): offset to shift the square when printing
            y (int): offset to shift the square when printing
            id (int): number of instances of squares"""

        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """Update attributes of a square
        Args:
            args (non-keyword arguments): non-specified amount of arguments
            kwargs (key-word arguments): non-specified amount of arguments
        """

        attrs_square = ["id", "size", "x", "y"]

        for position_square, value in enumerate(args):
            if position_square > (len(attrs_square) - 1):
                break
            setattr(self, attrs_square[position_square], value)

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Informal string representation of the Square"""

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.size)

    def to_dictionary(self):
        """Add to dictionary"""

        new_dict = {}
        attrs = ["id", "size", "x", "y"]

        for att in attrs:
            new_dict[att] = getattr(self, att)

        return new_dict

    @property
    def size(self):
        """ Get size"""

        return self.width

    @size.setter
    def size(self, value):
        """ Set size
        Args:
            value (int): the value to assign to width/height"""

        self.width = value
        self.height = value
