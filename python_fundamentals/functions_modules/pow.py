#!/usr/bin/env python3

def pow(a, b):
    result = 1
    exponent = b
    if exponent < 0:
        exponent = -exponent
    for i in range(exponent):
        result *= a
    if b < 0:
        result = 1 / result
    return result
