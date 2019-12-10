#!/usr/bin/python3
def islower(c):
    for letter in range(97, 123):
        if chr(letter) == c:
            return True
    return False
