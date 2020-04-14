#!/usr/bin/python3
"""
Task 10:
Use the Github API to display the id

10-my_github.py
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/users/" + argv[1]
    req = requests.get(url)
try:
    if req.json():
        print("{}".format(req.json()["id"]))
    else:
        print("None")
except:
    pass
