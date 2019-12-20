#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    return [print("%s: %s" % (k, a_dictionary[k])) for k in sorted(a_dictionary.keys())]
