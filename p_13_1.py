def intersection(A,B):
    result = ['dummy']
    a_iter, b_iter = iter(A), iter(B)
    a, b = next(a_iter, None), next(b_iter, None)
    while a is not None and b is not None:
        if a == b:
            if a!= result[-1]:
                result.append(a)
            a, b = next(a_iter, None), next(b_iter, None)
        elif a > b:
            b = next(b_iter, None)
        else:
            a = next(a_iter, None)

    return result[1:]

A = [1,1,2,3,5,5,6,7,8,9]
B = [2,4,4,5,5,6,6,7,9,10]
print(intersection(A,B))
