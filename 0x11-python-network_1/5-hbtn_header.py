#!/usr/bin/python3
"""
Task 5:
Sends a request and displays the value of X-Request-Id

5-hbtn_header.py
"""
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get(argv[1])
    print(req.headers["X-Request-Id"])
