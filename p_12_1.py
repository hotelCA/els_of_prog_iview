import functools
import collections

# def string_hash(s, modulus):
#     MULT = 3
#     return functools.reduce(lambda aggregate, c: (aggregate * MULT + ord(c)) % modulus, s, 0)
#
# print(ord('d'))
# print(string_hash('dd', 9))
def can_be_palindrome(s):
    char_counts = collections.Counter(s)
    odd_count = 0
    for value in char_counts.values():
        odd_count += 1 if value % 2 == 1 else 0

    return odd_count <= 1

s = 'abcdedecbaaxxya'
print(can_be_palindrome(s))