#!/usr/bin/python3
def weight_average(my_list=[]):
    single, f_weight, total = 1, 0, 0

    for i in my_list:
        for j in i:
            single *= j
        total += single
        single = 1
        f_weight += i[1]

    return (total / f_weight)
