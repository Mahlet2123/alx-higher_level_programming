#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    argv = sys.argv[1:]
    n = len(sys.argv)
    for i in range(1, n):
        sum = sum + int(sys.argv[i])
    print(f"{sum}")
