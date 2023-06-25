#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_List = []
    for value in my_list:
        if value%2 == 0:
            new_List += [True]
        else:
            new_List += [False]
    return new_List
