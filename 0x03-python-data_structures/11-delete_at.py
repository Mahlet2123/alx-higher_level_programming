#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    if idx == 0:
        del(my_list[0])
    else:
        for i in my_list:
            if i == idx:
                del(my_list[i])
    return my_list
