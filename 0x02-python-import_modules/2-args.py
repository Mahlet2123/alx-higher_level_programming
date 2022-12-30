#!/usr/bin/python3
import sys
argv = sys.argv[1:]
argv_count = len(argv)
index = 1
if argv_count == 0:
    print('{} arguments.'.format(argv_count))
if argv_count > 0:
    print('{} arguments:'.format(argv_count))
    while (index <= argv_count):
        print('{:d}: {:s}'.format(index, sys.argv[index]))
        index += 1
