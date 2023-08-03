#!/usr/bin/python3
"""
This module defines a inherits_from, which checks for boolean
inherits_from:
            This checks true for instance of a specific object otherwise, false
"""


def inherits_from(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Parameters:
        obj: Any-The object to be checked.
        a_class: type - The class to be compared with.

    Returns:
        boolean: True if the object is an instance of the specified class,else, False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
