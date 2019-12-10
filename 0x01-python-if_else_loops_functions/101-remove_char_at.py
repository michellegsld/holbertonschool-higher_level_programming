#!/usr/bin/python3
def remove_char_at(str, n):
    check = 0
    newstr = ""
    for i in str:
        if check != n:
            newstr = newstr + i
        check = check + 1
    return newstr
