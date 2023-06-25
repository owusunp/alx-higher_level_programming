#!/usr/bin/python3
def max_integer(my_list=[]):
    k = float('-inf')
    if len(my_list) == 0:
        return "None"
    for i in my_list:
        if i > k:
            k = i
    return k
