#!/usr/bin/python3

def max_integer(my_list=[]):
    for j in my_list:
        for i in range(1, len(my_list)):
            if j > my_list[i]:
                list1 = j
            else:
                list1 = my_list[i]
            break
    return (list1)
