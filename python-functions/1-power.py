#!/usr/bin/env python3
def pow(a, b):
    if b == 0:
        return 1

    result = 1
    is_negative_power = b < 0
    b = abs(b)

    while b > 0:
        if b % 2 == 1:
         result *= a
        a *= a
        b //= 2
    return 1 / result if is_negative_power else result
print(pow(2, 2))
#print(pow(98, 2))
"""
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))
"""
