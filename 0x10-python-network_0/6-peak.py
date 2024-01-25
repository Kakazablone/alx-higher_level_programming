#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """Args:
        list_of_integers(list): list of integers to find peak of
        Returns: peak of list_of_integers or None"""

    size = len(list_of_integers)
    middle_element = size
    mid_index = size // 2

    if size == 0:
        return None

    while True:
        middle_element = middle_element // 2
        if (mid_index < size - 1 and
                list_of_integers[mid_index] < list_of_integers[mid_index + 1]):
            if middle_element // 2 == 0:
                middle_element = 2
            mid_index = mid_index + middle_element // 2
        elif middle_element > 0 and list_of_integers[mid_index]\
                < list_of_integers[mid_index - 1]:
            if middle_element // 2 == 0:
                middle_element = 2
            mid_index = mid_index - middle_element // 2
        else:
            return list_of_integers[mid_index]
