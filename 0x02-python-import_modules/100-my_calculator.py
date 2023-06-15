#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

def calculate_expression(a, operator, b):
    if operator == '+':
        return add(a, b)
    elif operator == '-':
        return sub(a, b)
    elif operator == '*':
        return mul(a, b)
    elif operator == '/':
        return div(a, b)
    else:
        return None

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    result = calculate_expression(a, operator, b)
    if result is None:
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, operator, b, result))
