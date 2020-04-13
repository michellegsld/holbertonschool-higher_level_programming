#!/usr/bin/python3
"""
Task 7:
Sends a request and displays the body of the response

7-error_code.py
"""
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get(argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
