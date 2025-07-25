#!/usr/bin/python3
"""Module for add_integer function"""

def add_integer(a, b=98):
    """Add two integers or floats after casting them to integers

    Args:
        a: int or float
        b: int or float (default: 98)

    Raises:
        TypeError: If a or b is not int or float
        ValueError: If a or b is NaN
        OverflowError: If a or b is too large or infinite

    Returns:
        int: sum of a and b after casting to int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    for var, name in zip((a, b), ("a", "b")):
        if isinstance(var, float):
            if var != var:
                raise ValueError("cannot convert float NaN to integer")
            if var == float("inf") or var == float("-inf"):
                raise OverflowError("cannot convert float infinity to integer")
            try:
                var = int(var)
            except OverflowError:
                raise OverflowError("int too large to convert to float")
        else:
            var = int(var)
        if name == "a":
            a = var
        else:
            b = var
    return a + b

