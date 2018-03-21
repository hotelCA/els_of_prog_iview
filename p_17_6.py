import sys
import collections

DistanceAndGas = collections.namedtuple('DistanceAndGas', ('distance', 'gas'))


def find_ample_city(A):
    ample_city = [0, sys.maxsize]
    current_gas = 0
    for i in range(len(A)):
        current_gas = current_gas + A[i].gas - A[i].distance
        if current_gas < ample_city[1]:
            ample_city = [i, current_gas]

    return ample_city[0] + 1 if ample_city[0] + 1 < len(A) else 0


A = [DistanceAndGas(3, 3),
     DistanceAndGas(3, 5),
     DistanceAndGas(6, 3),
     DistanceAndGas(3, 6),
     DistanceAndGas(4, 2)]

print(find_ample_city(A))