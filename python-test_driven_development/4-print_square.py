#!/usr/bin/python3
"""Module for print_square function"""


def print_square(size):
    """Prints a square with the character #

    Args:
        size: the size of the square (must be an integer >= 0)

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
