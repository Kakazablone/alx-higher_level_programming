#!/usr/bin/python3
""" My Module for looking up available attributes
    and methods of an object
"""


def lookup(obj):
    """ This function returns the available attributes and methods of an object
    Args:
        obj (object): The object to check"""
    return dir(obj)
