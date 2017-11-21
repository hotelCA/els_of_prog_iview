import sys
import math
import random as rand

A = [4, 8, 16, 32, 128, 129381293818]

# def parity1(array_of_words):
#     XOR all words together
#     XOR all bits together

def parity1(array_of_words):
    result_a = 0
    for i in range(0, len(array_of_words)):
        result_a ^= array_of_words[i]

    result = 0
    while result_a > 0:
        result ^= result_a & 1
        result_a >>= 1

    return result

# def parity2(array_of_words):
#     for all the words
#         while remaining not zero
#             remove the least significant one
#             count parity

def parity2(array_of_words):
    result = 0
    for word in array_of_words:
        while word:
            word &= word - 1
            result ^= 1

    return result

def parity3(word):
    word ^= word >> 32
    word ^= word >> 16
    word ^= word >> 8
    word ^= word >> 4
    word ^= word >> 2
    word ^= word >> 1
    return word & 0x1


print(parity1(A))
print(parity2(A))
print(parity3(0xFE2345EC25))

# Exercies

# 1) Right propagate the right-most set bit in x, e.g., turns (01010000) into (01011111)
x = 0b1010100
x |= x - 1
print('1) ' + bin(x))

# 2) Compute x mod a power of two, e.g., returns 13 for 77 mod 64. E.g. 1010011100 mod 1000000000 returns 10011100
x = 0b1010011100
d = 0b100000
x &= d-1

print('2) ' + bin(x))

# 3) Test if x is a power of 2, i.e., evaluates to true for x = 1, 2, 4, 8,..., false for all other values
#     10000000 is a power of two. 10001000 is not a power of 2.
x = 0b100000
x &= x - 1
print(False if x else True)
