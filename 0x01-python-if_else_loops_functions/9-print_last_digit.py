#!/usr/bin/python3
"""
function that prints the last digit of a number.
"""
def print_last_digit(number):
    if number < 0:
        last_num =  ((-1 * number) % 10)
    else:
        last_num = number % 10
    print("{}".format(last_num), end="")
    return last_num
