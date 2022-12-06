#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    len1 = len(my_list) - 1
    if idx > len1:
        return my_list
    for i in my_list:
        if i == idx:
            del(my_list[idx])
    return my_list
