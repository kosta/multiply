#!/usr/bin/env python

#
# Multiply - Toolbox for Mathematics
# Four-Spaces-Edition
#
# Author: Philipp
#

import sys
import asyncwaiter

def multiply_by_2(numbers):
    result = []
    for number in numbers:
        result.append(number * 2)
    return result

def is_integer(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def main():
    input = [int(x) for x in sys.argv[1:] if is_integer(x)]
    output = asyncwaiter.executeNow(multiply_by_2, input)
    print(str(input) +' -> '+ str(output))

if __name__ == '__main__':
     main()

