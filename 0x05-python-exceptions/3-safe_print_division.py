#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return a/b
    except:
        print("Inside result: {:s}".format("None"))
    finally:
        if b == 0:
            return "None"
        else:
            print("Inside result: {:.1f}".format(a/b))
    
