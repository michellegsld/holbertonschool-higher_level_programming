#!/usr/bin/python3
"""
Task 0:
Fetch https://intranet.hbtn.io/status

0-hbtn_status.py
"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        print(response.read())
