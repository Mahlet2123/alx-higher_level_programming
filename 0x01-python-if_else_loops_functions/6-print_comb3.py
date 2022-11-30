#!/usr/bin/python3
for num1 in range(0, 10):
    for num2 in range(0, 10):
        if num1 < num2:
            print('{}{}, '.format(num1, num2), end='')
print("")
