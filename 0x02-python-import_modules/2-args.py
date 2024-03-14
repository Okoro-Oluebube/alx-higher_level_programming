#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv
    i = len(argv)
    if i == 1:
        print("0 arguments.")
    elif i == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    elif i > 2:
        print("{} arguments:".format(i - 1))
        for i in range(1, i):
            print("{}: {}".format(i, argv[i]))
