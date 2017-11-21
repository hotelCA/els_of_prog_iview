import copy
def all_combinations(n):
    cache = {}
    def compute(n):
        if n != 0 :
            if n not in cache:
                cache[n] = ([[2]] if n == 2 else [[2] + x for x in (compute(n-2) if n >= 2 else [])]) + \
                           ([[3]] if n == 3 else [[3] + x for x in (compute(n-3) if n >= 3 else [])]) + \
                           ([[7]] if n == 7 else [[7] + x for x in (compute(n-7) if n >= 7 else [])])
            return cache[n]
    compute(n)
    [[cache[key][i].sort() for i in range(len(value))] for key, value in cache.items()]
    for key in cache:
        cache[key] = set(tuple(x) for x in cache[key])
    return cache

n = 12
cache = all_combinations(n)

# [print('{}: {}'.format(x, y)) for x, y in cache]
[print('{}: {} ---> {}'.format(key, value, len(value))) for key, value in cache.items()]

