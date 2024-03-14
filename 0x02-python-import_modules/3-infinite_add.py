#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv
    j = 0
    for i in range(1, len(argv)):
        k = argv[i]
        j += int(k)
    print(j)
