#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    my_list = my_list[::-1]
    for i in my_list:
        print('{:d}'.format(i))
