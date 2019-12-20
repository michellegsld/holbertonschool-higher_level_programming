#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_d = a_dictionary
    if key in a_d:
        a_d.update(key=value)
    else:
        a_d = {**a_d, **{key: value}}
    return a_d
