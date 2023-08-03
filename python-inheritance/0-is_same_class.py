#!/usr/bin/python3
#function that returns True 
#if the object is exactly an instance of the specified class ; otherwise False
def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Parameters:
        obj: Any-The object to be checked.
        a_class: type - The class to be compared with.

    Returns:
        boolean: True if the object is an instance of the specified class,else, False.
    """
    return type(obj) is a_class #using 'is' to check for the boolean
