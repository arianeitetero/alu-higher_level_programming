#!/usr/bin/python3
"""Inserts a line of text after each line containing a given string in a file."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a new_string after lines containing search_string"""
    new_lines = []
    with open(filename, "r") as f:
        for line in f:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)
    with open(filename, "w") as f:
        f.writelines(new_lines)

