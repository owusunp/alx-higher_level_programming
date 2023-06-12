#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            upper_case = chr(ord(c) - 32)
        else:
            upper_case = c
        print("{}".format(upper_case), end="")
    print()
