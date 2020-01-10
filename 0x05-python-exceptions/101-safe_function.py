#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        answer = fct(*args)
        return answer
    except Exception as msg:
        print("Exception: {}".format(msg), file=stderr)
        return None
