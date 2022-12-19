#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        while count < x:
            print("{:d}".format(my_list[count]), end='')
            count += 1
        print()
        return count
    except IndexError:
        count += 1
        print("list index out of range")
    except (ValueError, TypeError):
        count += 1
        return False
