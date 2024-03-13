#!/usr/bin/python3

def remove_char_at(str, n):
    s = ""
    i = len(str)
    for i in range(i):
        if i != n:
            s = s + str[i]
    return (s)
