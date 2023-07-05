import json

""" json to string """

def to_json_string(my_obj):
    """
    Converts a Python object to a JSON string.

    Args:
        my_obj (Any): The Python object to be converted to JSON.

    Returns:
        str: The JSON string representation of the given Python object.

    Usage:
        data = {"name": "John Doe", "age": 30}
        json_string = to_json_string(data)  # Converts the Python object to a JSON string.

    """
    return json.dumps(my_obj)

