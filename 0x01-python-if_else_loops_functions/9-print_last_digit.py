#!/usr/bin/python3

def print_last_digit(number):
    num = str(number)
    num = num[-1:]
    num = int(num)
    print("{}".format(num), end="")
    return (num)
