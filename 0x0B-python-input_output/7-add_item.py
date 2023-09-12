#!/usr/bin/python3
"""
Modulejson
"""
import json


def load_from_json_file(filename):
    """
    load fromjason
    """
    with open(filename, "r") as f:
        return json.loads(f.readline())
