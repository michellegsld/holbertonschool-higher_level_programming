#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = max(a_dictionary, key=int)
    for k, v in a_dictionary.items():
        if biggest == v:
            return k
