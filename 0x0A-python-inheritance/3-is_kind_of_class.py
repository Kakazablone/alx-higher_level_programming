#!/usr/bin/python3
""" My Module that tests object types
"""


def is_kind_of_class(obj, a_class):
    """ Function that checks if obj is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class
    Args:
        obj (object): the object to test
        a_class (class): the class to see if object is a part of"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
