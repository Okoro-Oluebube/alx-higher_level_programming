#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1, sys
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
            print("{} {} {} = {}".format(a, argv[2], b, calculator_1.add(a, b)))
        elif argv[2] == '-':
            print("{} {} {} = {}".format(a, argv[2], b, calculator_1.sub(a, b)))
        elif argv[2] == '*':
            print("{} {} {} = {}".format(a, argv[2], b, calculator_1.mul(a, b)))
        elif argv[2] == '/':
            print("{} {} {} = {}".format(a, argv[2], b, calculator_1.div(a, b)))
    else:
        print("Unkown operator. Availavle operators: +, -, * and /")
        sys.exit(1)
