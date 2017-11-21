import functools
import string

def convert_base(s, b1, b2):
    decimal = functools.reduce(lambda num, x: num * b1 + string.digits.index(x), s, 0)
    return convert_digit(decimal, b2)

def convert_digit(decimal, b):
    if decimal == 0:
        return ''
    digit = decimal % b
    char = chr((ord('0') + digit) if digit < 10 else (ord('A')+ (digit - 10)))
    return convert_digit(decimal // b, b) + char


print(convert_base('615', 7, 13))