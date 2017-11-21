def multiplier(numbA, numbB):
    sign = -1 if (numbA[0] < 0) ^ (numbB[0] < 0) else 1
    numbA[0], numbB[0] = abs(numbA[0]), abs(numbB[0])
    prod = (len(numbA) + len(numbB)) * [0]
    for i, x in reversed(list(enumerate(numbA))):
        carry = 0
        for j, y in reversed(list(enumerate(numbB))):
            aggregate = (x * y) + carry + prod[j+i+1]
            digit = aggregate % 10
            carry = aggregate // 10

            prod[j+i+1] = digit

    if prod[0] == 0:
        prod = prod[1:]

    prod[0] *= sign

    return prod

print(multiplier([-3,2,1],[1,5,7,6,3]))
print(multiplier([3,2,1],[1,0,0,0,0]))
print(multiplier([0],[1]))
print(multiplier([0],[-1]))
print(multiplier([0],[7]))
result = [0,0,3,4,5]
print(next(i for i, x in enumerate(result) if x != 0))