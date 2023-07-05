#!/usr/bin/python3


""" convert the json string to object """

import json

def load_from_json_file(filename):
    """
    Loads JSON data from a file and returns the corresponding Python object.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        The Python object representing the JSON data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        JSONDecodeError: If the JSON data in the file is not valid.

    Example:
        >>> data = load_from_json_file("data.json")
    """
    with open(filename) as json_obj:
        return json.load(json_obj)

