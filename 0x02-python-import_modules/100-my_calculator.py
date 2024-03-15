#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as cal
    import sys
    argv = sys.argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if argv[2] == '+' or argv[2] == '-' or argv[2] == '*' or argv[2] == '/':
        a = argv[1]
        a = int(a)
        b = argv[3]
        b = int(b)
        if argv[2] == '+':
            print("{} {} {} = {}".format(a, argv[2], b, cal.add(a, b)))
        elif argv[2] == '-':
            print("{} {} {} = {}".format(a, argv[2], b, cal.sub(a, b)))
        elif argv[2] == '*':
            print("{} {} {} = {}".format(a, argv[2], b, cal.mul(a, b)))
        elif argv[2] == '/':
            print("{} {} {} = {}".format(a, argv[2], b, cal.div(a, b)))
    else:
        print("Unkown operator. Availavle operators: +, -, * and /")
        sys.exit(1)
