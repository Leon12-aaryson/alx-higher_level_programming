#!/usr/bin/python3
"""from_json_string """


import json


def from_json_string(my_str):
    """returns an object(python)

    Args: my_str (JSON string): json string.
    Return: object, the python data structure
    """
    object = json.loads(my_str)
    return object
