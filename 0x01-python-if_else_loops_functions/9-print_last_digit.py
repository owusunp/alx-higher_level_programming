#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
        print("{:d}".format(number % 10, end=""))
    else:
        print("{}".format(number % 10, end=""))
    return number % 10
