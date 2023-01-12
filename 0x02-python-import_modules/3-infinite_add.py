#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argv_count = len(argv)
    all_sum = 0
    i = 2
    if argv_count == 0:
        print("0")
    for i in range(argv_count):
        all_sum += int(argv[i])
        i += 1
    print("{}".format(all_sum))
