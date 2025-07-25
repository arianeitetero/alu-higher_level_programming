#!/usr/bin/python3
"""Module for text_indentation function"""


def text_indentation(text):
    """Prints text with 2 new lines after ., ?, and :

    Args:
        text: input string

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = text.replace(delim, delim + "\n\n")

    lines = [line.strip() for line in text.split("\n")]
    for line in lines:
        print(line)
