#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object for which to retrieve attributes and methods.

    Returns:
        A list of attributes and methods of the object.

    """
    return dir(obj)

