#!/usr/bin/python3
""" My reverse integer module"""


class MyInt(int):
    """ Class MyInt that inherits from int
        Uses comparisons on numbers passed"""
    def __eq__(self, other):
        """ Method that calls not equals in int super class
        Args:
            other (int): the integer to compare to"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ Method that calls equals in int super class
        Args:
            other (int): the integer to compare to"""
        return int.__eq__(self, other)
