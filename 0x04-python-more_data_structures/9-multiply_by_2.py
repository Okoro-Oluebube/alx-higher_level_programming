#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    diction = a_dictionary.copy()
    for key in diction:
        diction[key] *= 2
    return (diction)
