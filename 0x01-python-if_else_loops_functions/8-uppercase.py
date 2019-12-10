#!/usr/bin/python3
def uppercase(str):
    for check in str:
        for letter in range(97, 123):
            if letter == ord(check):
                print("{:c}".format(letter - 32), end='')
                break
        if letter == 122:
            print("{:s}".format(check), end='')
    print("")
