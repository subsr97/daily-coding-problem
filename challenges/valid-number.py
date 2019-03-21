"""
#123
LinkedIn

Given a string, return whether it represents a number. Here are the different kinds of numbers:
    "10", a positive integer
    "-10", a negative integer
    "10.1", a positive real number
    "-10.1", a negative real number
    "1e5", a number in scientific notation

And here are examples of non-numbers:
    "a"
    "x 1"
    "a -2"
    "-"

"""

import re

def isValidNumber(numStr):
    numStr = numStr.strip()
    regex = re.compile("^[-+]?\d+(\.\d+)?([eE][+-]?\d+(\.\d+)?)?$")
    return regex.match(numStr) != None


def main():
    print(isValidNumber("11.5"))        # True
    print(isValidNumber("abc"))         # False
    print(isValidNumber("2e10"))        # True
    print(isValidNumber("2e.10"))       # False
    print(isValidNumber("10e5.4"))      # True
    print(isValidNumber("-10E5.4"))     # True


if __name__ == "__main__":
    main()