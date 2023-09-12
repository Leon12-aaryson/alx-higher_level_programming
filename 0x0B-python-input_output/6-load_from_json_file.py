#!/usr/bin/python3
"""
load Json
"""
import json


def load_from_json_file(filename):
    """
    method to read json files line per line
    """
    with open(filename, "r") as f:
        return json.loads(f.readline())
