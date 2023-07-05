#!/usr/bin/python3

""" json represenation """

import json

def save_to_json_file(my_obj, filename):
    """
    Serializes and saves a Python object to a JSON file.

    Args:
        my_obj (Any): The Python object to be serialized and saved.
        filename (str): The name of the file to save the JSON data.

    Usage:
        data = {"name": "John Doe", "age": 30}
        save_to_json_file(data, "output.json")  # Serializes and saves the Python object to a JSON file.

    """
    with open(filename, "w", encoding='utf-8') as json_write:
        json.dump(my_obj, json_write)

