#!/usr/bin/python3
for alpha in range(ord('a'), ord('z') + 1):
    if alpha != ord('q') and alpha != ord('e'):
        print('{}'.format(chr(alpha)), end="")
