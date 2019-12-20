#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_d = a_dictionary
    return a_d.update(key=value) if key in a_d else {**a_d, **{key: value}}
