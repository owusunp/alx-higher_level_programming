#!/usr/bin/python3

"""json to pythob """

import json

def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.

    Args:
        my_str (str): The JSON string to be converted to a Python object.

    Returns:
        Any: The Python object representation of the given JSON string.

    Usage:
        json_string = '{"name": "John Doe", "age": 30}'
        data = from_json_string(json_string)  # Converts the JSON string to a Python object.

    """
    return json.loads(my_str)

