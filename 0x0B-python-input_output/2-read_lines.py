#!/usr/bin/python3
"""
2-read_lines.py
read_lines(filename="", nb_lines=0)
"""


def read_lines(filename="", nb_lines=0):
    """
    Reads/prints a certain amount of lines from a file
    """
    count = 0
    with open(filename) as fil:
        for line in fil:
            if nb_lines <= 0:
                print("{}".format(line), end='')
            else:
                if count < nb_lines:
                    print("{}".format(line), end='')
                    count += 1
