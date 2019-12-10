#!/usr/bin/python3
def pow(a, b):
    answer = 1
    if b >= 0:
        for i in range(0, b):
            answer = answer * a
    else:
        for i in range(0, -b):
            answer = answer / a
    return answer
