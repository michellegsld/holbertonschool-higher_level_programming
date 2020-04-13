#!/usr/bin/python3
"""
Task 3:
Sends a request and displays the body of the response
(decoded in utf-8)

3-error_code.py
"""
from sys import argv
from urllib import request, parse

if __name__ == "__main__":
    try:
        req = request.Request(argv[1])
        with request.urlopen(req) as response:
            print(response.read())
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
