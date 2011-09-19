#!/usr/bin/env python

#
# Multiply - Toolbox for Mathematics
# Four-Spaces-Edition
#
# Author: Philipp
#

def multiply_by_2(numbers):
    result = []
    for number in numbers:
        result.append(number * 2)
    return result


def main():
    input = [1, 2, 3, 4]
    output = multiply_by_2(input)
    print(str(input) +' -> '+ str(output))


if __name__ == '__main__':
     main()

