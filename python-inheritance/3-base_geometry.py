#!/usr/bin/python3
"""
This module defines class BaseGeometry, which chekcs for geometry
    BaseGeometry:
            This checks for geometry-related classes
"""


from collections.abc import Iterable


class BaseGeometry:
    """
    A base class representing the foundation for geometry-related classes.

    This class serves as a base for other classes that deal with geometry.
    It is an empty class, meaning it does not have methods or attributes of its own
    """
    def __dir__(cls) -> None:
        """
        controls access to inherited attributes
        """
        attributes = super().__dir__()

        return[attribute for attribute in attributes if attribute != '__init_subclass__']
