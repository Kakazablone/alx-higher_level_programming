#!/usr/bin/python3
""" My Module for geometry"""


class BaseGeometry():
    """ Base class"""
    def area(self):
        """ Method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method that checks if value is a number and
            if it's an appropriate number
        Args:
            name (string): name of the integer
            value (integer): value given to name"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
