#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return 0
    elif idx > len(my_list) - 1:
        return "None"
    else:
        return my_list[idx]
#1,4,5,7
    
