#!/usr/bin/python3
"""
5-text_indentation.py
def text_indentation(text)
tests/5-text_indentation.txt
"""


def text_indentation(text):
    """
    Prints text with two newlines separating each line
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for s in range(len(text)):
        if text[s] is not " ":
            break
    for i in range(s, len(text)):
        if text[i - 1] is "." or text[i - 1] is "?" or text[i - 1] is ":":
            print("")
            print("")
            while text[i] is " ":
                i += 1
        else:
            print("{}".format(text[i]), end='')
