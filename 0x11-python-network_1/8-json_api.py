#!/usr/bin/python3
"""
Task 8:
Sends POST request to http://0.0.0.0:5000/search_user

8-json_api.py
"""
import requests
from sys import argv

if __name__ == "__main__":
    q = ""
    if len(argv) > 1:
        q = argv[1]
    req = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        if req.json():
            print("[{}] {}".format(req.json()["id"], req.json()["name"]))
        elif len(req.json()) is 0:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
