#!/usr/bin/python3
"""Module for Pascal's Triangle"""


def pascal_triangle(n):
    """Create Pascal's Triangle as a list of lists
    Args:
        n (int): Number of rows to generate
    Returns:
        list: Pascal's Triangle as a list of lists"""
    if n <= 0:
        return []

    pascal = []
    for row in range(n):
        """Initialize each row with 1"""
        if row == 0:
            pascal.append([1])
        else:
            """Calculate the current row based on the previous row"""
            previous_row = pascal[row - 1]
            current_row = [1]
            for i in range(1, len(previous_row)):
                current_row.append(previous_row[i - 1] + previous_row[i])
            current_row.append(1)
            pascal.append(current_row)

    return pascal
