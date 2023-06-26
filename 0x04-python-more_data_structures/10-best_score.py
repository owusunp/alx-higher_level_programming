#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return "None"
    large_score = float('-inf')
    key = ""
    for i,v in a_dictionary.items():
        if v > large_score:
            large_score = v
            k = i
    return k
    

