#!/usr/bin/python3
"""
this module contains the add_item function
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argv_list = []
for i in range(1, len(sys.argv)):
    argv_list.append(sys.argv[i])
filename = 'add_item.json'
save_to_json_file(argv_list, filename)
load_from_json_file(filename)
