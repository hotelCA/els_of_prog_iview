import collections

def is_subset(A, B):
    a = collections.Counter(A.lower().split())
    b = collections.Counter(B.lower().split())

    result = a - b
    return len(result) == 0

A = 'WALKS a park park and something happened'
B = 'a dog walks in a park and pees on a tree in a park and something else happens.'

print(is_subset(A, B))