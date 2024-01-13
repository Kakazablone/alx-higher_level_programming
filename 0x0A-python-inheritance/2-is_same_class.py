#!/usr/bin/python3
""" My Module one testing objects
"""


def is_same_class(obj, a_class):
    """ Function that tests whether an object is part of a class

    Args:
        obj (object): the object to test whether it is part of a class
        a_class (class): tests if obj is part of it

    """
    if type(obj) == a_class:
        return True
    else:
        return False
