#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = str(number)
string = "Last digit of {} is {} "
if num[-1:] > '5' and number > 0:
    print(string.format(number, num[-1:]) + "and is greater than 5")
elif num[-1:] == '0' and number == 0:
    print(string.format(number, num[-1:]) + "and is 0")
elif num[-1:] < '6' and num[-1:] != '0' and number > 0:
    print(string.format(number, num[-1:]) + "and is less than 6 and not 0")
string = "Last digit of {} is -{} "
if num[-1:] > '5' and number < 0:
    print(string.format(number, num[-1:]) + "and is greater than 5")
elif num[-1:] < '6' and num[-1:] != '0' and number < 0:
    print(string.format(number, num[-1:]) + "and is less than 6 and not 0")
