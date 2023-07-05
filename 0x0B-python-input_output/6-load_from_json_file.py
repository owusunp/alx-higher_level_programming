#!/usr/bin/python3

import json

def load_from_json_file(filename):
    with open(filename) as json_obj:
        return json.load(json_obj)

