#!/usr/bin/python3
"""
this module contains the add_item function
"""


import sys
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argv_list = []
for i in range(1, len(sys.argv)):
    argv_list.append(sys.argv[i])
if path.isfile("add_file.json"):
    load_from_json_file("add_file.json")
save_to_json_file(argv_list,"add_file.json" )
