import collections
from p_11_8 import find_kth_largest
import math
import random


def find_k_most_frequent(S, k):
    StringCount = collections.namedtuple('StringCount', ('count', 'value'))
    str_freq = {}

    for s in S:
        if s not in str_freq:
            str_freq[s] = 1
        else:
            str_freq[s] += 1

    freq_array = []
    print(str_freq)
    for key, value in str_freq.items():
        freq_array.append(StringCount(value, key))

    return find_kth_largest(freq_array, k)

S = ['a', 'b', 'c', 'd', 'b', 'f', 'a', 'a', 'c', 'c', 'g']
print(find_k_most_frequent(S, 6))
