#!/usr/bin/python3
"""
9-add_item.py
load_from_json_file(filename)
imports sys, os.path, save_to_json_file, load_to_json_file
"""
from sys import argv
import os.path
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
arguments = []
if os.path.isfile(filename):
    arguments = load_from_json_file(filename)

for i in range(1, len(argv)):
    arguments.append(argv[i])

save_to_json_file(arguments, filename)
