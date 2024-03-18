#!/usr/bin/python3

def no_c(my_string):
    j = 0
    for i in range(0, len(my_string)):
        my_stringg = " "
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        else:
            my_stringg[j] = my_string[i]
            j += 1
    return (my_stringg)
