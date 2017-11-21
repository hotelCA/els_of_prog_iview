import collections
import time

def replace_and_remove(S):

    cache, shift_left, i = collections.deque(), 0, 0

    while i < len(S):
        if S[i] == 'b':
            shift_left -= 1
        else:
            cache.extend(['d', 'd'] if S[i] == 'a' else [S[i]])
            while cache and shift_left < 0:
                S[i + shift_left] = cache.popleft()
                if cache:
                    shift_left += 1
            if cache:
                S[i] = cache.popleft()
        i += 1

    S = S[:(i+shift_left)] + list(cache)

    return S

def replace_and_remove_2(S):

    b_count = 0
    a_count = 0
    for i in range(len(S)):
        if S[i] == 'b':
            b_count += 1
        else:
            S[i-b_count] = S[i]
            if S[i] == 'a':
                a_count += 1

    diff = a_count - b_count
    i = len(S) - 1 - b_count
    j = len(S) - 1 + diff

    if diff > 0:
        S.extend([0] * diff)

    while i >= 0:
        if S[i] != 'a':
            S[j] = S[i]
            j -= 1
        else:
            S[j-1:j+1] = ['d','d']
            j -= 2
        i -= 1

    return S


S = ['c','b','e','f','g','b','h'] * 1000000
S_2 = ['c','b','e','f','g','b','h'] * 1000000

start_time = time.time()
replace_and_remove(S)
print(time.time() - start_time)

start_time = time.time()
replace_and_remove_2(S_2)
print(time.time() - start_time)
