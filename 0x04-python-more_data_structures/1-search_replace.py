#!/usr/bin/python3

def search_replace(my_list, search, replace):
    for i in my_list:
        newlist = list(map((lambda x: replace if x == search else x), my_list))
    return (newlist) 
