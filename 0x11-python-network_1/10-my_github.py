#!/usr/bin/python3
"""
Task 9:
Use the Github API to display the id

10-my_github.py
"""
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get("https://api.github.com/users/", data={'username': argv[1], 'token': argv[2]})
    try:
        if req.json():
            print("{}".format(req.json()["id"]))
        else:
            print("None")
    except:
        print("None")
