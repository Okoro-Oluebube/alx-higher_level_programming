#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    if my_list == [] or my_list == None:
        pass
    else:
        for i in range(0, len(my_list)):
            print("{:d}".format(my_list[i]))
