#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_tup = ()
    j = len(tuple_a)
    k = len(tuple_b)
    if j < 2 or k < 2:
        if j == 0 and k == 0:
            for i in range(2):
                tuple_a += 0,
                tuple_b += 0,
            for i in range(2):
                new_tup += (tuple_a[i] + tuple_b[i]),
        elif j == 0:
            for i in range(2):
                tuple_a += 0,
            for i in range(2):
                new_tup += (tuple_a[i] + tuple_b[i]),
        elif k == 0:
            for i in range(2):
                tuple_b += 0,
            for i in range(2):
                new_tup += (tuple_a[i] + tuple_b[i]),
        elif j == 1 and k == 1:
            tuple_a += 0,
            tuple_b += 0,
            for i in range(2):
                new_tup += (tuple_a[i] + tuple_b[i]),
        elif k == 1:
            tuple_b += 0,
            for i in range(2):
                new_tup += (tuple_a[i] + tuple_b[i]),
        elif j == 1:
            tuple_a += 0,
            for i in range(2):
                new_tup += (tuple_a[i] + tuple_b[i]),
    else:
        for i in range(2):
            new_tup += (tuple_a[i] + tuple_b[i]),
    return (new_tup)
