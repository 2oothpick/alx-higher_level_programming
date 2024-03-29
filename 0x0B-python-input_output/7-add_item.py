#!/usr/bin/python3
"""
this module contains the add_item function
"""


import sys
from os import path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

new_list = []
if path.isfile("add_item.json"):
    new_list = load_from_json_file("add_item.json")
save_to_json_file(new_list + sys.argv[1:], "add_item.json")
