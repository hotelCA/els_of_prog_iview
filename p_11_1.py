def find_first_occurence(A, x):
    L = 0
    U = len(A) - 1
    result = -1
    while L <= U:
        M = L + (U - L) // 2
        if A[M] < x:
            L = M + 1
        elif A[M] > x:
            U = M - 1
        else:
            result = M
            U = M - 1

    return result

A = [1,2,4,4,4,4,9,10,11,12,13]
print(find_first_occurence(A, 4))