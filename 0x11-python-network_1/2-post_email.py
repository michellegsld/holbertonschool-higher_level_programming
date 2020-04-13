#!/usr/bin/python3
"""
Task 2:
Sends POST request with an email as a parameter
To display body of the response (decoded in utf-8)

2-post_email.py
"""
from sys import argv
from urllib import request, parse

if __name__ == "__main__":

    value = {'email': argv[2]}
    data = parse.urlencode(value)
    data = data.encode('utf-8')

    url = request.Request(argv[1], data)

    with request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print(body)
