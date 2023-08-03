#!/usr/bin/python3
"""
This module defines a is_kind_of_class, which checks for boolean
is_kind_of_class:
            This checks true for instance of a specific object otherwise, false
"""
def is_kind_of_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Parameters:
        obj: Any-The object to be checked.
        a_class: type - The class to be compared with.

    Returns:
        boolean: True if the object is an instance of the specified class,else, False.
    """
    return isinstance(obj, a_class)