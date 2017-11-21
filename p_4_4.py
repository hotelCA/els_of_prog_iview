def find_closest_same_weight(x):
    lsb = x & 1
    mask = 0b10
    MAX_INT_SIZE = 64
    for i in range(1, MAX_INT_SIZE):
        if ((mask & x) >> i) != lsb:
            x = x ^ (mask | (mask >> 1))
            return x
        mask = mask << 1

    raise ValueError('X is all 0 or all 1')

def find_closest_same_weight_2(x):
    ls_zero = (x + 1) ^ ((x + 1) & x)
    if ls_zero != 1:
        x = x ^ (ls_zero | (ls_zero >> 1))
    else:
        ls_one = x ^ ((x - 1) & x)
        x = x ^ (ls_one | (ls_one >> 1))
    return x

x = 0
print(find_closest_same_weight(x))
print(find_closest_same_weight_2(x))