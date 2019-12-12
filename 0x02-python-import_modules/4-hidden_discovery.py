#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    list = dir(hidden_4)
    for name in range(list):
        if name[0] != "_" and name[1] != "_":
            print("{:s}".format(name))
