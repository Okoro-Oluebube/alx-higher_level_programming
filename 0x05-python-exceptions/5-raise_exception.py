#!/usr/bin/python3

def raise_exception():
    try:
        raise Exception()
    except Exception as e:
        print ("Exception raised")
