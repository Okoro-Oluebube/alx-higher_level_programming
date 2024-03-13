#!/usr/bin/python3

for i in range(0, 9):
    for j in range(1, 10):
        if (i == j):
            continue
        if (int(str(i) + str(j)) == int(str(j) + str(i))):
            continue
        print("{:d}{:d}".format(i, j), end=", ")

