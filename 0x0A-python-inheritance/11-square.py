#!/usr/bin/python3
""" My Square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class that inherits from Rectangle"""
    def __init__(self, size):
        """ Inititalizes the size of the square
        Args:
            size (int): the size of 1 side of the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ Returns the unofficial representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
